# Can Claude read its own remaining context window mid-run?

**Question (2026-07-14):** A claim (relayed via Gemini) said Anthropic injects live token-budget tags into the system prompt/text stream — `<budget:token_budget>1000000</budget:token_budget>` and `<system_warning>Token usage: 750000/1000000; 250000 remaining</system_warning>` — letting Claude read its remaining budget and self-throttle. If true, /next could run until context hit ~40% then wrap, removing the need for user-placed session-break lines.

## Finding: the specific mechanism is not real

- No such tags exist in the Anthropic Messages API. Web search (2026-07) surfaced nothing supporting them; they don't match documented API behaviour.
- The real `budget_tokens` parameter is for **extended thinking** — a thinking-token budget the *developer sets*, not a live usage counter fed back to the model. The claim conflates the two.
- Conclusion: the raw API does **not** silently feed Claude a running token counter it can read.

## What Claude Code (the harness) actually does expose

- A **status bar** shows the *user* their context/token percentage in real time.
- The status line exposes `context_window.used_percentage` and `context_window.remaining_percentage` — **UI fields for display**, not a signal reliably injected into the model's text stream at arbitrary thresholds.
- The one automatic model-facing event is a **hint near ~80%**, just before **auto-compaction** triggers (buffer reduced to ~33K tokens / ~16.5% as of early 2026) and summarises earlier turns.

## Design implication for [session-sizing-and-break-lines]

- Claude **cannot** reliably self-measure "I'm at 40%" mid-run and wrap — there is no continuous model-facing signal it acts on at that threshold. This matches the method's earlier conclusion (cruise budget ceiling was "best-effort" because "Claude can't read an exact token meter").
- The only automatic mechanism, compaction at ~80%, is exactly what the method wants to **avoid**: it's lossy and fires too late to prevent a mid-build squeeze.
- Therefore session-break lines + plan-time sizing stay the design; they are not replaced by a self-throttling /next.
- **Open lever:** `context_window.remaining_percentage` is a real field. A future design could investigate whether a hook or status-line integration surfaces it usefully — to the user, or to Claude in an actionable form — to partly automate sizing. Unverified; a research item, not a settled capability.

## Sources
- https://code.claude.com/docs/en/context-window
- https://platform.claude.com/docs/en/build-with-claude/context-windows
- https://deepwiki.com/anthropics/claude-code/3.3-context-window-and-compaction
