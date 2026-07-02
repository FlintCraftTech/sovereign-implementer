#!/usr/bin/env node
/**
 * post-tool-use hook for OpenCode — advisory QUEUE.md structure lint.
 *
 * Fires after write/edit to QUEUE.md. Flags known format violations.
 * All advisory — never blocks (exit 0 always).
 */
const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

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

  if (toolName !== "edit" && toolName !== "write") process.exit(0);

  const filepath = toolArgs.filePath || toolArgs.file_path || "";
  if (!filepath || !cwd) process.exit(0);

  const queuePath = path.join(cwd, "QUEUE.md");
  if (path.normalize(filepath).toLowerCase() !== path.normalize(queuePath).toLowerCase()) {
    process.exit(0);
  }

  const specPath = path.join(cwd, "SPEC.md");
  if (!fs.existsSync(specPath)) process.exit(0);

  let content;
  try { content = fs.readFileSync(queuePath, "utf-8"); } catch { process.exit(0); }

  const warnings = lint(content, cwd);
  if (warnings.length === 0) process.exit(0);

  const message =
    "[Sovereign Implementer] QUEUE.md structure lint (advisory). " +
    "These flag known violations only — novel structure is allowed and never flagged. " +
    "Judge each one: fix what's genuinely wrong in a follow-up edit, leave what isn't.\n" +
    warnings.map(w => "- " + w).join("\n");

  process.stderr.write(message + "\n");

  // Also write to context file for next-turn visibility
  const ctxDir = path.join(cwd, ".opencode", "data");
  if (!fs.existsSync(ctxDir)) fs.mkdirSync(ctxDir, { recursive: true });
  fs.writeFileSync(path.join(ctxDir, "si-queue-lint.md"), message, "utf-8");

  process.exit(0);
}

// ── Lint engine ──
const FULL_BOLD_LINE = /^(?:\*\*[^*]+\*\*)(?:\s+\*\*[^*]+\*\*)*$/;
const SLUG_MARKER = /\*\*\[([a-z0-9][a-z0-9-]+)\]\*\*/g;
const SLUG_REF = /\[([a-z0-9][a-z0-9-]+)\](?!\()/g;
const DEP_HEADER = /^(Depends on|Blocks|Blocked by):/;
const SUBHEADING = /^([A-Z][A-Za-z-]*):$/;
const MARKER_LINE = /^---.+---$/;
const ALLOWED_SUBHEADINGS = new Set(["Build", "Test", "Audit", "Freeform"]);

function lint(content, cwd) {
  const lines = content.split("\n");
  const warnings = [];
  let h2 = null;
  let h3 = null;

  // Check 1: batch slugs — every bold title under ## Batches needs a **[slug]**
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();
    if (line.startsWith("### ")) { h3 = line.substring(4).trim(); continue; }
    if (line.startsWith("## ")) { h2 = line.substring(3).trim(); h3 = null; continue; }
    if (h2 !== "Batches" || !line || line.startsWith("#")) continue;
    if (FULL_BOLD_LINE.test(line) && !new RegExp(SLUG_MARKER.source).test(line)) {
      warnings.push(
        "line " + (i + 1) + ": batch title '" + line + "' has no **[slug]** marker — " +
        "every batch needs one so other items can reference it across reorders."
      );
    }
  }

  // Check 3: captures divider (bare ---) exists under ## Captures
  let inCaptures = false;
  let foundDivider = false;
  for (const line of lines) {
    const trimmed = line.trim();
    if (trimmed === "## Captures") { inCaptures = true; continue; }
    if (inCaptures && trimmed.startsWith("## ") && trimmed !== "## Captures") break;
    if (inCaptures && trimmed === "---") { foundDivider = true; break; }
  }
  if (inCaptures && !foundDivider) {
    warnings.push(
      "the Captures processed/unprocessed divider (a line holding just ---) is missing — " +
      "restore it: processed captures sit above it, raw captures collect below."
    );
  }

  // Check 5: subheadings under ## Batches are Build/Test/Audit/Freeform only
  h2 = null;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();
    if (line.startsWith("### ")) { h3 = line.substring(4).trim(); continue; }
    if (line.startsWith("## ")) { h2 = line.substring(3).trim(); h3 = null; continue; }
    if (h2 !== "Batches" || line.startsWith("#")) continue;
    const m = line.match(SUBHEADING);
    if (m && !ALLOWED_SUBHEADINGS.has(m[1])) {
      warnings.push(
        "line " + (i + 1) + ": subheading '" + line + "' isn't one of Build:/Test:/Audit:/Freeform: — " +
        "a typo, or a new batch type this lint doesn't know yet?"
      );
    }
  }

  // Check 2: parked items have Blocked by:/Parked: header
  h2 = null; h3 = null;
  let currentParked = null;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();
    if (line.startsWith("### ")) { h3 = line.substring(4).trim(); }
    else if (line.startsWith("## ")) { h2 = line.substring(3).trim(); h3 = null; }
    if (h3 !== "Parked" || line.startsWith("#")) {
      if (currentParked) {
        if (!currentParked.lines.some(l => l.startsWith("Blocked by:") || l.startsWith("Parked:"))) {
          warnings.push(
            "line " + (currentParked.start + 1) + ": parked item has no Blocked by:/Parked: header — " +
            "nothing leaves active flow without a stated reason in one of those two slots."
          );
        }
        currentParked = null;
      }
      continue;
    }
    const indent = lines[i].length - lines[i].replace(/^\s+/, "").length;
    const startsItem = indent === 0 && (line.startsWith("- ") || FULL_BOLD_LINE.test(line));
    if (startsItem) {
      if (currentParked) {
        if (!currentParked.lines.some(l => l.startsWith("Blocked by:") || l.startsWith("Parked:"))) {
          warnings.push(
            "line " + (currentParked.start + 1) + ": parked item has no Blocked by:/Parked: header."
          );
        }
      }
      currentParked = { start: i, lines: [line] };
    } else if (currentParked) {
      currentParked.lines.push(line);
    }
  }
  if (currentParked && !currentParked.lines.some(l => l.startsWith("Blocked by:") || l.startsWith("Parked:"))) {
    warnings.push("line " + (currentParked.start + 1) + ": parked item has no Blocked by:/Parked: header.");
  }

  return warnings;
}

main().catch(() => process.exit(0));
