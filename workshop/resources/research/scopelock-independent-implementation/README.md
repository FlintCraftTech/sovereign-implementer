# scopelock v1

A zero-ceremony scope lock for AI coding agents. Hermes remembers what was
decided; scopelock enforces what hasn't been decided yet.

v1 is deliberately the **deterministic subset**: enforcement only happens from
an explicit `SCOPE.md`. There is no scope inference from branch names or
prompts in v1 — inferred scope produces false denials, and false denials train
workarounds. Inference is planned as a *suggester* (drafts a SCOPE.md for you
to glance at), never as a thing that enforces directly.

## What it does

- **File lock** (PreToolUse): denies any file edit (`apply_patch` on Codex;
  `Edit`/`Write` on Claude Code; `apply_patch` heredocs through the shell)
  whose target is not covered by the `## Files` list in `SCOPE.md`. Every
  denial explains why and names the alternative.
- **Git safety** (PreToolUse, always on, even with no SCOPE.md): blocks
  `git reset --hard`, `git push --force` (allows `--force-with-lease`),
  `git add -A` / `git add .` / `git add --all`, and `git commit -a`, each with
  the safer alternative named.
- **Scope injection** (SessionStart): injects SCOPE.md into session context,
  along with the capture-instead-of-act and halt rules. If there is no
  SCOPE.md, it says so and runs without file enforcement — fail open, always.
- **Capture files**: `BACKLOG.md` and `NOTICES.md` are always editable, so
  capturing out-of-scope work can never be blocked. `SCOPE.md` itself is also
  always editable — scope expansion is meant to be *visible*, not impossible
  (an unexplained SCOPE.md edit shows up in your diff; the AGENTS.md fragment
  forbids silent expansion).

## Requirements

- [Bun](https://bun.sh) (you already have it if you run Hermes)
- Codex CLI with hooks enabled — in `~/.codex/config.toml`:

  ```toml
  [features]
  codex_hooks = true
  ```

## Install (per project)

1. Copy this folder to `<project>/.codex/scopelock/`.
2. Wire the hooks. If the project has no `.codex/hooks.json`, copy the
   provided `hooks.json` to `<project>/.codex/hooks.json`. **If a hooks.json
   already exists (e.g. from Hermes), merge instead of overwriting**: append
   scopelock's entries to the existing `SessionStart` and `PreToolUse` arrays.
   Multiple handlers per event are supported and run independently.
3. Copy `templates/SCOPE.md` to the repo root and fill in the task and file
   list. Plain English everywhere except the `## Files` bullets, which are
   paths/globs. (Skip this step and scopelock runs advisory-only: git safety
   still active, no file lock.)
4. Append `AGENTS.scopelock.md` to your project's `AGENTS.md`.

Check the exact `hooks.json` nesting against your Codex version's docs —
the matcher-group format changed between releases; if hooks don't fire, try
flattening each event to `[{ "command": "bun …" }]`.

## Using it

Work normally. Start each task by writing two lines in SCOPE.md (task
sentence + file globs). Mid-session scope change: add a path under
`## Files`; the lock re-reads the file on every check, so it applies
immediately.

## Hermes compatibility

scopelock shares nothing with Hermes except the hooks.json file (merge, don't
overwrite). It reads SCOPE.md and hook stdin only; it writes nothing. Its
SessionStart context is additive alongside Hermes's injected memory. If
Hermes later wants to *write* SCOPE.md drafts from its decision log, that's
the natural v2 integration point.

## Known gaps (deliberate in v1)

- **Shell-side writes are not scope-checked.** `echo x > file`, `tee`,
  `sed -i` bypass the file lock. Blocking these reliably means parsing
  arbitrary shell, which produces false denials — the worse failure. The
  AGENTS.md fragment forbids routing around denials; the gap is behavioural,
  not mechanical.
- **No scope inference.** By design in v1 (see above).
- **Capture and halt rules are instructions, not enforcement.** They live in
  AGENTS.md and can degrade in long sessions. Hooks can't make an agent
  *want* to capture; they can only stop it editing.
- **Codex hook schemas are young.** Field names verified against current
  third-party references (Aug 2026); if OpenAI changes the payload shape, the
  script fails open (never blocks), so breakage is silent-permissive — test
  after Codex upgrades with `bun test/run-tests.ts`.

## Testing

```
bun test/run-tests.ts
```

Feeds simulated hook payloads through the script and checks every decision.
