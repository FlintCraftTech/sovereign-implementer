# Context window data in plugin hooks

Research into whether a plugin can access context window token usage to trigger threshold-based actions (e.g. auto-recommend /compact at 60%).

## Current state (June 2026)

The Claude Code desktop app calculates and displays a full context window breakdown (token counts per category, percentage used) in the UI. This data is **not exposed to hooks or plugins**.

### What hooks receive

Hook events receive JSON input with common fields (`session_id`, `cwd`, `hook_event_name`, `tool_name`, `tool_input`) plus event-specific fields:

- **Stop event:** `stop_hook_active`, `last_assistant_message`, `background_tasks`, `session_crons`
- **SessionStart:** `source`, `model`, optionally `agent_type` and `session_title`
- **PreToolUse / PostToolUse:** tool name and input/output

No event includes token counts, context utilization percentage, or remaining capacity.

### What exists externally

- The **Messages API** returns `usage.input_tokens` and `usage.output_tokens` in response metadata — but this is per-request, post-hoc, and not available inside the hook context.
- The **Agent SDK** exposes per-step token breakdowns on result messages — same limitation, it's SDK-level not hook-level.
- The **token counting endpoint** lets you pre-count tokens before sending — useful for API callers, not for plugins.
- One guide described using `UserPromptSubmit` + `Stop` hooks together to track token deltas via external logging, but this is a workaround, not native data.

## Feasibility

Adding a field like `context_usage_pct` or `tokens_used` / `tokens_remaining` to hook event data is architecturally plausible — the harness already computes this for the UI. It's a feature request, not a design impossibility.

## Implication for the plugin

Until hooks gain token data, context management must be rule-based (compact after skill handoffs, clear after push/commit) rather than threshold-based. The batch entry queued in V38 reflects this.

## Sources

- [Hooks reference - Claude Code Docs](https://code.claude.com/docs/en/hooks)
- [Automate actions with hooks - Claude Code Docs](https://code.claude.com/docs/en/hooks-guide)
- [Plugins reference - Claude Code Docs](https://code.claude.com/docs/en/plugins-reference)
- [Claude Code Hooks: Complete Guide](https://claudefa.st/blog/tools/hooks/hooks-guide)
