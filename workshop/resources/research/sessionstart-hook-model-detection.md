# Can the SessionStart hook detect which model is running?

Researched 2026-07-12 (web) for [fable-docset-model-detection] — the load-bearing feasibility question: automatic per-model docset selection is only possible if session_start.py can see the running model.

## Finding

**Yes, feasibility-wise — with a caveat.** Claude Code's hook input JSON differs per event. Common fields on every event: `session_id`, `transcript_path`, `cwd`, `hook_event_name`. SessionStart adds `source` (startup | resume | clear | compact) and — importantly — is the **one hook type that can carry a `model` field** (e.g. `"model": "claude-sonnet-5"`).

**The caveat that shapes the design:** the `model` field is reported as **not guaranteed to be present**. So a docset-selection design keyed on it must define a fallback when `model` is absent — it can't assume the field is always there.

## Design implications

- session_start.py already does `data = json.load(sys.stdin)` and only reads `cwd`. Reading `data.get("model")` is a one-line addition — the plumbing is already there.
- Because presence isn't guaranteed, the fallback matters: when `model` is missing, the method needs a defined default docset (candidate: the Opus docset, the current model target) rather than a silent failure.
- Worth an empirical confirm on the user's actual platform (Windows 11 desktop app) before building — a blog verified SessionStart hook patterns on Windows 11 + MINGW64, but presence of `model` specifically should be confirmed live.

## Sources

- [Hooks reference — Claude Code Docs](https://code.claude.com/docs/en/hooks)
- [claude-code-hooks-schemas.md (gist)](https://gist.github.com/FrancisBourre/50dca37124ecc43eaf08328cdcccdb34)
- [SessionStart hook verification, Windows 11 + MINGW64 — DevelopersIO](https://dev.classmethod.jp/en/articles/claude-code-session-start-hook-verification/)
