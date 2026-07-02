#!/usr/bin/env node
/**
 * session-start hook for OpenCode.
 *
 * Detects project state: not adopted / adopted / active build.
 * Loads behaviour rules, checks plugin version, backfills LOG hashes,
 * detects missing scaffold files/settings.
 *
 * Writes session context to .opencode/data/si-session-context.md
 * which the agent reads at session start (per AGENTS.md instructions).
 */
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const { execSync } = require("child_process");

async function main() {
  // Read stdin JSON from OpenCode
  const chunks = [];
  for await (const chunk of process.stdin) {
    chunks.push(chunk);
  }
  const raw = Buffer.concat(chunks).toString("utf-8");
  if (!raw) process.exit(0);

  let data;
  try { data = JSON.parse(raw); } catch { process.exit(0); }

  const cwd = data.cwd || "";
  if (!cwd || !fs.existsSync(cwd)) process.exit(0);

  const specPath = path.join(cwd, "SPEC.md");
  const queuePath = path.join(cwd, "QUEUE.md");
  const buildPath = path.join(cwd, "_build.md");
  const planStatePath = path.join(cwd, "_plan.md");
  const siVersionPath = path.join(cwd, ".si-version");

  const hasSpec = fs.existsSync(specPath);
  const hasQueue = fs.existsSync(queuePath);
  const hasActiveBuild = fs.existsSync(buildPath);
  const hasPlanState = fs.existsSync(planStatePath);

  // Plugin root: dist/ -> parent -> plugin root
  const pluginRoot = path.resolve(__dirname, "..");
  const behaviourPath = path.join(pluginRoot, "..", "..", "..", "docs", "plugin-behaviour.md");

  let behaviourRules = "";
  if (fs.existsSync(behaviourPath)) {
    try { behaviourRules = fs.readFileSync(behaviourPath, "utf-8"); } catch {}
  }

  const pkgJsonPath = path.join(pluginRoot, "package.json");
  let pluginVersion = "";
  if (fs.existsSync(pkgJsonPath)) {
    try {
      const pkg = JSON.parse(fs.readFileSync(pkgJsonPath, "utf-8"));
      pluginVersion = pkg.version || "";
    } catch {}
  }

  let projectVersion = "";
  if (fs.existsSync(siVersionPath)) {
    try { projectVersion = fs.readFileSync(siVersionPath, "utf-8").trim(); } catch {}
  }

  const contextParts = [];

  // State 1: Not adopted
  if (!hasSpec) {
    let msg = "[Sovereign Implementer] Empty project folder. Run /setup to scaffold the project docs and describe what you're building.";
    try {
      const entries = fs.readdirSync(cwd);
      const nonInfra = entries.filter(e =>
        !["AGENTS.md", ".opencode", "__pycache__", "node_modules", ".venv"].includes(e)
      );
      if (nonInfra.length > 3) {
        msg = "[Sovereign Implementer] This folder has files but no SI docs yet. If it's a fresh project, run /setup to get started. If it already has planning or spec docs under other names — from another tool or an older version — /setup can treat it as a migration and map them into the method's docs.";
      }
    } catch {}
    writeContext(cwd, msg);
    process.exit(0);
  }

  // State 2 or 3: Adopted
  if (behaviourRules) {
    contextParts.push(
      "=== PLUGIN-WIDE BEHAVIOUR RULES (active every session, govern every command) ===\n" +
      behaviourRules + "\n=== END BEHAVIOUR RULES ==="
    );
  }

  contextParts.push("[Sovereign Implementer] Project is set up.");
  contextParts.push("  SPEC.md: " + (hasSpec ? "found" : "MISSING"));
  contextParts.push("  QUEUE.md: " + (hasQueue ? "found" : "MISSING"));

  if (pluginVersion) {
    contextParts.push("  Installed workflow version: " + pluginVersion);
  }

  // Presence-based drift check
  const missingScaffold = [];
  if (!hasQueue) missingScaffold.push("QUEUE.md (your work queue)");
  if (!fs.existsSync(path.join(cwd, "LOG", "index.md"))) missingScaffold.push("the LOG folder (your session records)");
  if (!fs.existsSync(siVersionPath)) missingScaffold.push("the .si-version marker (records which workflow version set the project up)");

  if (missingScaffold.length > 0) {
    contextParts.push("");
    contextParts.push(
      "PROJECT OUT OF DATE — the current workflow creates files and folders this project doesn't have yet: " +
      missingScaffold.join("; ") + ". Because there is a real gap, you must open your first reply by telling " +
      "the user plainly, in everyday language, which parts are missing, and offer to bring the project up to date " +
      "by running /setup — it adds what's missing without touching their existing work. State this as your own " +
      "first message before doing anything else; don't bury it in other output or wait to be asked."
    );
  }

  // Content-level top-up: check AGENTS.md for Editor setting
  const agentsPath = path.join(cwd, "AGENTS.md");
  if (fs.existsSync(agentsPath)) {
    try {
      const agentsContent = fs.readFileSync(agentsPath, "utf-8");
      if (!agentsContent.includes("## Editor")) {
        contextParts.push("");
        contextParts.push(
          "PROJECT MISSING NEWER SETTINGS — this project was set up before the method added the Editor setting. " +
          "Bring it up to date now: your AGENTS.md is missing the Editor setting. Open your first reply by asking, " +
          "in one line, which editor the user works in here (they can say to skip if they don't use one). " +
          "Then write their answer into a new '## Editor' section of AGENTS.md. Add only that section — change nothing else the user has written."
        );
      }
    } catch {}
  }

  if (hasActiveBuild) {
    contextParts.push("");
    contextParts.push(
      "ACTIVE BUILD in progress (_build.md exists). Run /next to resume, or /done if the work is complete. " +
      "A planning session (/plan) may run in a separate chat alongside this build — if this chat was opened to plan, that is allowed; don't refuse it."
    );
  } else {
    contextParts.push("");
    contextParts.push("Ready. Run /plan to manage the queue, or /next to start the top batch.");
  }

  if (hasPlanState) {
    contextParts.push("");
    contextParts.push(
      "INTERRUPTED PLANNING SESSION (_plan.md exists). A previous /plan was left mid-processing. " +
      "Run /plan to resume from the recorded item and beat, or /done to close out what was already routed."
    );
  }

  // Dirty-tree warning
  if (!hasActiveBuild && !hasPlanState) {
    try {
      const result = execSync("git status --porcelain", { cwd, timeout: 15000, encoding: "utf-8" });
      const dirtyCount = result.split("\n").filter(l => l.trim()).length;
      if (dirtyCount > 0) {
        contextParts.push("");
        contextParts.push(
          "[Sovereign Implementer] " + dirtyCount + " file(s) have uncommitted changes from a " +
          "previous session — /done will pick them up."
        );
      }
    } catch {}
  }

  // Backfill LOG hashes
  const backfillReport = backfillLogHashes(cwd);
  if (backfillReport) {
    contextParts.push("");
    contextParts.push(backfillReport);
  }

  // FAQ index
  const faqIndexPath = path.join(cwd, "FAQ", "index.md");
  if (fs.existsSync(faqIndexPath)) {
    try {
      const faqIndex = fs.readFileSync(faqIndexPath, "utf-8");
      contextParts.push("");
      contextParts.push(faqIndex);
    } catch {}
  }

  writeContext(cwd, contextParts.join("\n"));
  process.exit(0);
}

function writeContext(cwd, text) {
  const outputPath = path.join(cwd, ".opencode", "data", "si-session-context.md");
  const outputDir = path.dirname(outputPath);
  if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });
  fs.writeFileSync(outputPath, text, "utf-8");
}

// ── Hash backfill ──
const HASH_POSITION = /^(#{1,6}\s+|-\s+)\[HASH\](\s+[—–-]\s+)/m;

function oldestCommitFor(cwd, entryTitle) {
  try {
    const cmd = 'git log -S "' + entryTitle + '" --pretty=%h -- LOG/';
    const result = execSync(cmd, { cwd, timeout: 15000, encoding: "utf-8" });
    const hashes = result.split("\n").map(l => l.trim()).filter(l => l);
    return hashes[hashes.length - 1] || "";
  } catch { return ""; }
}

function backfillLogHashes(cwd) {
  const logDir = path.join(cwd, "LOG");
  if (!fs.existsSync(logDir)) return "";
  let names;
  try { names = fs.readdirSync(logDir).sort(); } catch { return ""; }

  let filled = 0;
  const touchedFiles = [];

  for (const name of names) {
    if (!name.endsWith(".md")) continue;
    const filePath = path.join(logDir, name);
    let content;
    try { content = fs.readFileSync(filePath, "utf-8"); } catch { continue; }

    const lines = content.split(/\r?\n/);
    let changed = false;

    for (let i = 0; i < lines.length; i++) {
      const match = lines[i].match(HASH_POSITION);
      if (!match) continue;
      const rest = lines[i].substring(match.index + match[0].length).trim();
      if (!rest) continue;
      const commit = oldestCommitFor(cwd, rest);
      if (!commit) continue;
      lines[i] = match[1] + commit + match[2] + lines[i].substring(match.index + match[0].length);
      changed = true;
      filled++;
    }

    if (changed) {
      try { fs.writeFileSync(filePath, lines.join("\n"), "utf-8"); } catch { continue; }
      touchedFiles.push(name);
    }
  }

  if (filled === 0) return "";
  return "[Sovereign Implementer] Log housekeeping: filled " + filled +
    " commit-hash placeholder(s) in " + touchedFiles.join(", ") +
    ". This is an uncommitted working-tree edit — fold it into this session's commit.";
}

main().catch(() => process.exit(0));
