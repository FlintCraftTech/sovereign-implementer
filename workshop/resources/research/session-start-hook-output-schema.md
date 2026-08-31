# SessionStart hook output schema — why our injection stopped reaching sessions

Researched 2026-08-03, during the `[session-start-output-not-reaching-sessions]`
diagnostic. Filed because the finding changed a decision (it cancelled a planned
Claude Code bug report) and would have to be redone if lost.

## The finding

Claude Code requires a SessionStart hook to nest its injected context:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "..."
  }
}
```

`hooks/session_start.py` emits `additionalContext` at the **top level** instead,
at both of its output points. Top-level is not the documented format. A hook that
emits it exits 0, prints valid JSON, and has its output silently discarded — no
error anywhere.

Source: <https://code.claude.com/docs/en/hooks>, SessionStart decision control.

## Corroboration

Others report the same symptom:

- [anthropics/claude-code#16538](https://github.com/anthropics/claude-code/issues/16538)
  — plugin SessionStart hooks don't surface `hookSpecificOutput.additionalContext`
  to Claude.
- [anthropics/claude-code#13650](https://github.com/anthropics/claude-code/issues/13650)
  — SessionStart hook stdout silently dropped despite valid JSON and exit code 0.
- [anthropics/claude-code#9591](https://github.com/anthropics/claude-code/issues/9591)
  — SessionStart hook context not displayed after an update.

## Two false leads recorded, because the reasoning matters more than the conclusion

**The CLI test proved less than it appeared to.** Running
`claude -p --include-hook-events --output-format stream-json` showed the hook's
full 92,000-character output in the event stream, which was read as proof the
injection worked. It is not: `--include-hook-events` echoes a hook's raw stdout
whether or not Claude Code accepts the payload, and that run failed
authentication before any model call, so injection was never exercised. This is
the second time in one diagnostic that one matching symptom was taken for a
confirmed cause.

**The size hypothesis was never actually tested.** The theory was that the
desktop app silently drops oversized `additionalContext` (92,000 characters at
every session start). The control was a throwaway hook emitting ~190 characters,
which also produced nothing — but it was written by copying the plugin's
top-level shape, so it carried the same defect. It varied size while holding the
*bug* fixed, not the mechanism. It is no evidence either way.

The apparent "two independent registration paths, both silent" argument — the
plugin's `hooks.json` and a project `settings.local.json` hook — collapses for
the same reason. It was one bug tested twice.

## The version gap, probably a red herring

The desktop app runs Claude Code 2.1.219; the standalone CLI at
`~/.local/bin/claude.exe` is 2.1.146. That gap looked like the likely home of a
regression. It probably isn't: the schema mismatch explains the symptom without
needing a version change. The plausible history is that top-level
`additionalContext` was tolerated at some point and later tightened, but nothing
here establishes that, and it doesn't need to be established to make the fix.

## What this does not settle

Whether the desktop app sends a `model` field — the open question behind
`[opus5-docset-switch-live-verification]`. Nothing observed here touches it,
because no injection reached a session at all. It stays open until the corrected
hook ships and a real session reports which docset it was told to load.
