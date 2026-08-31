#!/usr/bin/env bun
/**
 * scopelock — a zero-ceremony scope lock for Codex (and Claude Code) hooks.
 *
 * One script, two events:
 *   SessionStart → reads SCOPE.md, injects it as session context.
 *   PreToolUse   → denies file mutations outside SCOPE.md's file list,
 *                  and blocks a small set of dangerous git commands.
 *
 * Design rules:
 *   - Fail open. No SCOPE.md → no enforcement (a note is injected instead).
 *   - Every denial names the legitimate alternative.
 *   - Zero dependencies. Runs on Bun or Node >= 18 (uses only fs/path/stdin).
 *
 * Runs alongside Hermes: it only reads SCOPE.md and stdin; it never touches
 * Hermes state, and its SessionStart context is additive.
 */

import * as fs from "node:fs";
import * as path from "node:path";

// ---------------------------------------------------------------- constants

const CAPTURE_FILES = ["BACKLOG.md", "NOTICES.md"];
const SCOPE_FILE = "SCOPE.md";
// Files that may always be edited, regardless of scope. SCOPE.md is included
// deliberately: blocking scope expansion produces workarounds, and an edit to
// SCOPE.md is visible in the diff. The AGENTS.md fragment tells the agent to
// capture first and only expand scope when the user agrees.
const ALWAYS_ALLOWED = [SCOPE_FILE, ...CAPTURE_FILES];

// ---------------------------------------------------------------- utilities

function readStdin(): Promise<string> {
  return new Promise((resolve) => {
    let data = "";
    process.stdin.setEncoding("utf8");
    process.stdin.on("data", (c) => (data += c));
    process.stdin.on("end", () => resolve(data));
    // Safety: if nothing arrives, resolve empty after 5s rather than hanging.
    setTimeout(() => resolve(data), 5000).unref?.();
  });
}

function emit(obj: unknown): never {
  process.stdout.write(JSON.stringify(obj));
  process.exit(0);
}

function allow(): never {
  emit({});
}

/** Find the repo root (nearest ancestor with .git), falling back to cwd. */
function findRoot(cwd: string): string {
  let dir = path.resolve(cwd || process.cwd());
  while (true) {
    if (fs.existsSync(path.join(dir, ".git"))) return dir;
    const parent = path.dirname(dir);
    if (parent === dir) return path.resolve(cwd || process.cwd());
    dir = parent;
  }
}

function findScopeFile(cwd: string): string | null {
  const candidates = [
    path.join(path.resolve(cwd || process.cwd()), SCOPE_FILE),
    path.join(findRoot(cwd), SCOPE_FILE),
  ];
  for (const c of candidates) if (fs.existsSync(c)) return c;
  return null;
}

// ---------------------------------------------------------- SCOPE.md parsing

interface Scope {
  raw: string;
  globs: string[];
  file: string;
}

/**
 * Parse SCOPE.md. File globs are bullet lines ("- " or "* ") under a heading
 * whose text contains "file" (e.g. "## Files", "## Files in scope").
 * Everything else is free-form plain English and is only used as context.
 */
function parseScope(scopePath: string): Scope {
  const raw = fs.readFileSync(scopePath, "utf8");
  const globs: string[] = [];
  let inFiles = false;
  for (const line of raw.split(/\r?\n/)) {
    const heading = line.match(/^#{1,6}\s+(.*)/);
    if (heading) {
      inFiles = /file/i.test(heading[1]);
      continue;
    }
    if (!inFiles) continue;
    const bullet = line.match(/^\s*[-*]\s+(.+?)\s*$/);
    if (bullet) {
      // Strip surrounding backticks or quotes.
      const g = bullet[1].replace(/^[`"']|[`"']$/g, "").trim();
      if (g) globs.push(g);
    }
  }
  return { raw, globs, file: scopePath };
}

/** Convert one glob to a RegExp. Supports **, *, ? . A trailing "/" or a
 *  bare directory name is treated as "everything underneath". */
function globToRegExp(glob: string): RegExp {
  let g = glob.replace(/\\/g, "/").replace(/^\.\//, "");
  if (g.endsWith("/")) g += "**";
  let re = "";
  let i = 0;
  while (i < g.length) {
    const ch = g[i];
    if (ch === "*") {
      if (g[i + 1] === "*") {
        // "**" — match across directory separators. Swallow a following "/".
        re += "(?:.*)";
        i += g[i + 2] === "/" ? 3 : 2;
        continue;
      }
      re += "[^/]*";
      i++;
      continue;
    }
    if (ch === "?") {
      re += "[^/]";
      i++;
      continue;
    }
    re += ch.replace(/[.+^${}()|[\]\\]/g, "\\$&");
    i++;
  }
  return new RegExp(`^${re}$`);
}

function normalise(p: string, cwd: string): string {
  let out = p.replace(/\\/g, "/").trim();
  // Make absolute paths repo-relative when possible.
  if (path.isAbsolute(out)) {
    const root = findRoot(cwd);
    const rel = path.relative(root, out);
    if (!rel.startsWith("..")) out = rel.replace(/\\/g, "/");
  }
  return out.replace(/^\.\//, "");
}

function inScope(filePath: string, scope: Scope, cwd: string): boolean {
  const p = normalise(filePath, cwd);
  const base = path.basename(p);
  if (ALWAYS_ALLOWED.includes(base) && !p.includes("..")) return true;
  for (const glob of scope.globs) {
    const g = normalise(glob, cwd);
    if (globToRegExp(g).test(p)) return true;
    // A glob with no wildcard that names a directory covers its contents.
    if (!/[*?]/.test(g) && p.startsWith(g.replace(/\/$/, "") + "/")) return true;
  }
  return false;
}

// ------------------------------------------------------- patch path parsing

/** Extract target file paths from an apply_patch envelope. */
function pathsFromPatch(text: string): string[] {
  const out: string[] = [];
  const re = /^\s*\*\*\*\s+(Update|Add|Delete)\s+File:\s*(.+?)\s*$|^\s*\*\*\*\s+Move\s+to:\s*(.+?)\s*$/gim;
  let m: RegExpExecArray | null;
  while ((m = re.exec(text)) !== null) {
    const p = (m[2] || m[3] || "").trim();
    if (p) out.push(p);
  }
  return out;
}

// ------------------------------------------------------------- git safety

interface GitVerdict {
  deny: boolean;
  reason?: string;
}

function checkGitSafety(command: string): GitVerdict {
  // Normalise whitespace; check each simple segment of compound commands.
  const segments = command.split(/&&|\|\||;|\n/).map((s) => s.trim());
  for (const seg of segments) {
    if (!/^git\s/.test(seg)) continue;
    const s = seg.replace(/\s+/g, " ");

    if (/^git\s+reset\b.*\s--hard\b/.test(s))
      return {
        deny: true,
        reason:
          "git reset --hard destroys uncommitted work. Safer: `git stash` to set changes aside, or `git reset --keep` which refuses to overwrite local modifications.",
      };

    if (/^git\s+push\b.*(\s--force\b|\s-f\b)/.test(s) && !/--force-with-lease/.test(s))
      return {
        deny: true,
        reason:
          "git push --force can overwrite others' commits. Safer: `git push --force-with-lease`, which fails if the remote moved since your last fetch.",
      };

    if (/^git\s+add\b.*(\s-A\b|\s--all\b)/.test(s) || /^git\s+add\s+\.\s*$/.test(s) || /^git\s+add\s+\.\s/.test(s))
      return {
        deny: true,
        reason:
          "git add -A / git add . stages everything, including files you didn't mean to commit. Safer: name the files explicitly, e.g. `git add src/auth/login.ts`.",
      };

    if (/^git\s+commit\b.*(\s-a\b|\s--all\b)/.test(s) && !/--amend/.test(s))
      return {
        deny: true,
        reason:
          "git commit -a stages every modified file implicitly. Safer: `git add <specific files>` then `git commit`, so the commit contains only what you intend.",
      };
  }
  return { deny: false };
}

// ---------------------------------------------------------------- denials

function denyPreToolUse(reason: string): never {
  emit({
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: reason,
    },
  });
}

function scopeDenialReason(files: string[], scope: Scope): string {
  const list = files.map((f) => `\`${f}\``).join(", ");
  return (
    `Out of scope: ${list} is not in the file list in ${path.basename(scope.file)} for the current task. ` +
    `If this genuinely needs doing: (1) if it can wait, append a one-line note to BACKLOG.md instead of editing it now; ` +
    `(2) if the current task truly requires it, ask the user, and once they agree add the path under "## Files" in SCOPE.md — the lock updates immediately, no restart needed.`
  );
}

// ---------------------------------------------------------------- handlers

function handleSessionStart(input: any): never {
  const cwd = input.cwd || process.cwd();
  const scopePath = findScopeFile(cwd);
  let context: string;
  if (scopePath) {
    const scope = parseScope(scopePath);
    context =
      `[scopelock] Scope lock is ACTIVE. The declared scope for this session (from ${path.basename(scopePath)}):\n\n` +
      scope.raw.trim() +
      `\n\nRules: file edits outside the "## Files" list will be denied by a hook. ` +
      `When you notice out-of-scope work that probably needs doing, append a one-line note to BACKLOG.md and continue — do not act on it and do not interrupt the user with it. ` +
      `If a work item is so ambiguous you would have to invent scope the user never agreed to, halt and ask rather than guessing.`;
  } else {
    context =
      `[scopelock] No SCOPE.md found — scope lock is running WITHOUT file enforcement this session. ` +
      `Dangerous-git protection is still active. To enable the file lock, create a SCOPE.md in the repo root with a "## Files" section listing paths or globs in scope. ` +
      `Behavioural rules still apply: capture out-of-scope work to BACKLOG.md instead of acting on it; halt if a task is too ambiguous to know which files it touches.`;
  }
  emit({
    continue: true,
    hookSpecificOutput: { hookEventName: "SessionStart", additionalContext: context },
  });
}

function handlePreToolUse(input: any): never {
  const cwd = input.cwd || process.cwd();
  const toolName: string = input.tool_name || "";
  const toolInput: any = input.tool_input || {};

  // ---- 1. Dangerous git (Bash tool) — active even with no SCOPE.md.
  const isBash = /^(bash|shell)$/i.test(toolName);
  const command: string = typeof toolInput.command === "string" ? toolInput.command : "";
  if (isBash && command) {
    const verdict = checkGitSafety(command);
    if (verdict.deny) denyPreToolUse(verdict.reason!);
  }

  // ---- 2. File lock — only when a SCOPE.md exists.
  const scopePath = findScopeFile(cwd);
  if (!scopePath) allow();
  const scope = parseScope(scopePath!);
  if (scope.globs.length === 0) allow(); // No file list declared → advisory only.

  let targets: string[] = [];

  if (/^apply_patch$/i.test(toolName)) {
    // Codex: tool_input.command holds the patch envelope (or the full
    // apply_patch invocation). Fall back to input/patch fields defensively.
    const patchText = command || toolInput.input || toolInput.patch || "";
    targets = pathsFromPatch(String(patchText));
  } else if (/^(edit|write|multiedit|notebookedit)$/i.test(toolName)) {
    // Claude Code shapes: tool_input.file_path (or notebook_path).
    const p = toolInput.file_path || toolInput.notebook_path;
    if (p) targets = [String(p)];
  } else if (isBash && command.includes("apply_patch")) {
    // apply_patch driven through the shell as a heredoc.
    targets = pathsFromPatch(command);
  } else {
    allow(); // Reads, MCP tools, anything unrecognised: not our concern.
  }

  if (targets.length === 0) allow(); // Could not parse → fail open.

  const outOfScope = targets.filter((t) => !inScope(t, scope, cwd));
  if (outOfScope.length > 0) denyPreToolUse(scopeDenialReason(outOfScope, scope));
  allow();
}

// ------------------------------------------------------------------- main

async function main() {
  let input: any = {};
  try {
    const raw = await readStdin();
    input = raw.trim() ? JSON.parse(raw) : {};
  } catch {
    allow(); // Unparseable input → fail open, never block the user's work.
  }
  try {
    const event = input.hook_event_name || "";
    if (event === "SessionStart") handleSessionStart(input);
    if (event === "PreToolUse") handlePreToolUse(input);
    allow(); // Unknown event → no-op.
  } catch {
    allow(); // Any internal error → fail open.
  }
}

main();
