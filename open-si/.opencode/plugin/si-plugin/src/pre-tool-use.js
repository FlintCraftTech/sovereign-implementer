#!/usr/bin/env node
/**
 * pre-tool-use hook for OpenCode.
 *
 * Three rules:
 * 1. Scope-lock: _build.md's Files: governs editable files. Method docs always editable.
 * 2. Git safety: blocks git reset --hard, push --force, blanket add, commit -a/-am.
 * 3. Subagent cost gate: warns on agent/task tool use.
 *
 * Exit code 2 = BLOCK. Exit code 0 = allow.
 */
const fs = require("fs");
const path = require("path");

async function main() {
  const chunks = [];
  for await (const chunk of process.stdin) {
    chunks.push(chunk);
  }
  const raw = Buffer.concat(chunks).toString("utf-8");
  if (!raw) process.exit(0);

  let data;
  try { data = JSON.parse(raw); } catch { process.exit(0); }

  const cwd = data.cwd || "";
  const toolName = data.tool_name || "";
  const toolArgs = data.tool_args || {};

  // ── Rule 3: Subagent cost gate ──
  if (toolName === "agent" || toolName === "task") {
    process.stderr.write(
      "[Sovereign Implementer] Subagent cost gate: " + toolName + " tool invoked. " +
      "Subagents burn tokens fast — a single run can exhaust usage. " +
      "Confirm this genuinely needs wide, open-ended exploration; " +
      "declining to let the agent do the work directly is a normal, safe choice.\n"
    );
    process.exit(0);
  }

  if (!cwd) process.exit(0);

  // Only enforce in adopted projects
  const specPath = path.join(cwd, "SPEC.md");
  if (!fs.existsSync(specPath)) process.exit(0);

  const buildPath = path.join(cwd, "_build.md");
  const hasActiveBuild = fs.existsSync(buildPath);

  // ── Rule 2: Bash → git safety ──
  if (toolName === "bash" || toolName === "shell") {
    const command = toolArgs.command || "";
    if (typeof command !== "string") process.exit(0);

    const segments = command.split(/&&|\|\||[;|\n]/);

    for (const segment of segments) {
      if (/\bgit\b.*\breset\b.*--hard\b/i.test(segment)) {
        process.stderr.write(
          "[Sovereign Implementer] BLOCKED: git reset --hard destroys uncommitted work and cannot be undone.\n\n" +
          "Safer alternatives:\n- git stash — saves changes for later\n" +
          "- git checkout -- <file> — discards one file's changes\n" +
          "- git reset HEAD~1 — moves HEAD back, keeps working tree\n"
        );
        process.exit(2);
      }
      if (/\bgit\s+push\b.*(?:--force(?!-with-lease)\b|-f\b)/i.test(segment)) {
        process.stderr.write(
          "[Sovereign Implementer] BLOCKED: git push --force can overwrite remote commits.\n\n" +
          "Use git push --force-with-lease instead — it refuses to push if the remote " +
          "has commits you haven't fetched.\n"
        );
        process.exit(2);
      }
      if (/\bgit\b.*\badd\b.*(?:\s-A\b|\s--all\b|\s\.(?=\s|$|[;&|"')]))/i.test(segment)) {
        process.stderr.write(
          "[Sovereign Implementer] BLOCKED: blanket adds (git add -A, git add --all, git add .) " +
          "stage everything in the tree, including files never meant for the commit.\n\n" +
          "Stage explicitly — name each path: git add <path> <path>.\n"
        );
        process.exit(2);
      }
      if (/\bgit\b.*\bcommit\b.*\s(?:-a\b|-am\b|--all\b)/i.test(segment)) {
        process.stderr.write(
          "[Sovereign Implementer] BLOCKED: git commit -a / -am auto-stages every modified file, " +
          "including changes never meant for the commit.\n\n" +
          "Stage explicitly, then commit: git add <path> <path>, then git commit -m \"<message>\".\n"
        );
        process.exit(2);
      }
    }
    process.exit(0);
  }

  // ── Rule 1: File scope enforcement ──
  if (toolName !== "edit" && toolName !== "write") process.exit(0);

  const filepath = toolArgs.filePath || toolArgs.file_path || "";
  if (!filepath) process.exit(0);
  if (!hasActiveBuild) process.exit(0);

  const buildFiles = parseBuildFiles(buildPath);
  if (buildFiles === null) process.exit(0); // No Files: section — no enforcement

  if (isMethodDoc(filepath, cwd)) process.exit(0);

  if (!buildFiles || buildFiles.length === 0) {
    process.stderr.write(
      "[Sovereign Implementer] BLOCKED: this session's _build.md lists no editable files, " +
      "so only QUEUE.md, LOG/, and _build.md can be edited. Audit and test sessions " +
      "don't edit source files — route findings to Captures in QUEUE.md instead. " +
      "If a file genuinely needs editing, halt and add it to _build.md's Files: section " +
      "with the user's approval.\n"
    );
    process.exit(2);
  }

  if (!isBuildFile(filepath, cwd, buildFiles)) {
    process.stderr.write(
      "[Sovereign Implementer] BLOCKED: this file is not in the current build's file list.\n\n" +
      "_build.md allows: " + buildFiles.join(", ") + "\n\n" +
      "Files: lines must be bare paths — one path per line, nothing else on the line. " +
      "A note or annotation on a line becomes part of the path and silently breaks the match, " +
      "so if this file looks listed above, check its line for trailing text.\n\n" +
      "If this file genuinely needs editing, halt the build and, with the user's approval, " +
      "add it to _build.md's Files: section.\n"
    );
    process.exit(2);
  }

  process.exit(0);
}

function parseBuildFiles(buildPath) {
  let content;
  try { content = fs.readFileSync(buildPath, "utf-8"); } catch { return null; }

  const files = [];
  let inBullets = false;
  let foundSection = false;

  for (const line of content.split("\n")) {
    const stripped = line.trim();
    if (stripped.toLowerCase().startsWith("files:")) {
      foundSection = true;
      const inline = stripped.substring(6).trim();
      if (inline) {
        inBullets = false;
        for (const part of inline.split(",")) {
          const entry = part.trim();
          if (entry) files.push(entry);
        }
      } else {
        inBullets = true;
      }
      continue;
    }
    if (inBullets) {
      if (stripped.startsWith("- ")) {
        const entry = stripped.substring(2).trim();
        if (entry) files.push(entry);
      } else if (stripped && !stripped.startsWith("-")) {
        inBullets = false;
      }
    }
  }
  if (!foundSection) return null;
  return files;
}

function isMethodDoc(filepath, cwd) {
  const norm = path.normalize(filepath).toLowerCase();
  for (const doc of ["QUEUE.md", "_build.md", "_plan.md"]) {
    if (norm === path.normalize(path.join(cwd, doc)).toLowerCase()) return true;
  }
  const logDir = path.normalize(path.join(cwd, "LOG")).toLowerCase();
  if (norm.startsWith(logDir + path.sep) || norm === logDir) return true;
  return false;
}

function isBuildFile(filepath, cwd, buildFiles) {
  const norm = path.normalize(filepath).toLowerCase();
  for (const bf of buildFiles) {
    if (norm === path.normalize(path.join(cwd, bf)).toLowerCase()) return true;
  }
  return false;
}

main().catch(() => process.exit(0));
