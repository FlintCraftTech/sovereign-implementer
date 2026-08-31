# Hook context-injection vs a companion CLI

Filed 2026-06-23, during a /plan discussion of a proposed "companion CLI tool" shipped to consumers and auto-installed on each plugin update. The motivating example: collapse the multi-read skill startup (Claude reads next.md to learn the route, then reads next-build.md / next-test.md / etc.) into a single read — a tool scans the top batch, decides the route, and hands Claude one pre-assembled bundle (universal behaviour + the relevant current procedure docs). The user's own crux question: "maybe the mechanism doesn't exist to engage the tool in the first place."

## Headline

The mechanism to do the flagship example exists — and it is a **hook, not a companion CLI**. SI already uses the same pattern (its `session_start` hook injects `plugin-behaviour.md` and state at session start). So the motivating example needs no new CLI; it is a hook + packaging change.

## What the authoritative docs say (code.claude.com/docs/en/hooks)

Hook events that can inject context (via `additionalContext`):
- **SessionStart** — "String added to Claude's context at the start of the conversation, before the first prompt." (This is what SI's session_start hook already does.)
- **UserPromptSubmit** — injects `additionalContext` "alongside the submitted prompt"; purpose "add additional context based on the prompt/conversation." Fires the moment a prompt is submitted, before Claude processes it. A slash command/skill has expanded into the prompt by this point, so the hook can detect "/next", scan QUEUE.md for the top batch type, and inject either the route or the assembled bundle text.
- **Setup, SubagentStart, PreToolUse/PostToolUse/PostToolBatch, Stop/SubagentStop** — also support `additionalContext` at their respective moments.

Skill/command-specific event:
- **UserPromptExpansion** — the dedicated event for a slash command or skill expanding into a prompt. Has a **matcher on the command/skill name**. But it is designed for validation/**blocking** the expansion (exit code 2), and is **not** listed in the context-injection table. So: match the command here, but inject via UserPromptSubmit.

So the clean shape for the flagship example: detect the command (UserPromptExpansion matcher, or just parse the submitted prompt in UserPromptSubmit) → scan QUEUE.md's top batch to classify build/test/audit/freeform → inject a pre-assembled bundle via UserPromptSubmit `additionalContext`. The bundle itself can be assembled at **packaging time** (ship a pre-rolled file in the zip) so the runtime hook only has to pick the right one. No CLI in the loop.

## Reliability caveat — verify before relying

An open issue, anthropics/claude-code #37559 ("Hook documentation is misleading — Stop hooks broken, prompt hooks can't inject context, capabilities undocumented per event type"), reports that prompt-hook context injection has been unreliable / underdocumented per event type. The official docs say it works; at least one user reports it doesn't always. Implication: any design resting on UserPromptSubmit injection needs a real host-side test on the desktop app before being trusted — exactly the kind of thing that goes to Deferred tests (host-side) if built.

## Implications for the companion-CLI idea

- For the **flagship example (route + one read), a companion CLI is not justified** — hooks + packaging-time bundling cover it, using infrastructure SI already ships.
- A companion CLI would only earn its place for automation a hook genuinely *cannot* do: on-demand, mid-session, multi-step work Claude calls when it needs it. The startup preload is not that shape.
- "Auto-install an executable on each update for the user" remains a separate, heavier question (consent, cross-platform packaging, trust surface) and is not needed for the hook-based path.
- This startup-read cost overlaps existing queued thinking: [behaviour-doc-size-watch], [firing-map-middle-band], [behaviour-doc-double-load] — all about what is injected every session vs loaded on demand. Note the tension: "roll everything into one read" pulls the *opposite* way from the progressive-disclosure direction those lean toward (inject less, load on demand). The two should be decided together.

## Sources

- [Hooks reference — Claude Code Docs](https://code.claude.com/docs/en/hooks)
- [Automate actions with hooks — Claude Code Docs](https://code.claude.com/docs/en/hooks-guide)
- [Issue #37559 — Hook documentation is misleading / prompt hooks can't inject context](https://github.com/anthropics/claude-code/issues/37559)
