# Subagent ask-gate hook — feasibility

Filed 2026-06-24, during the /plan that addressed the silent-deep-research-fan-out cost incident.

## Question

Can a Claude Code `PreToolUse` hook force a permission prompt (not a hard block) before a subagent is spawned, so the user is always asked but keeps the choice?

## Finding — yes

- `PreToolUse` hooks return `hookSpecificOutput.permissionDecision`, one of `"allow"`, `"deny"`, `"ask"` (and `"defer"`), plus `permissionDecisionReason` (text shown to the user) and optional `updatedInput`.
- **`"ask"` is the relevant one:** it surfaces a permission prompt the user approves or declines, rather than silently allowing or hard-denying. This is the "guarantee the ask, keep the choice" behaviour — not a block.
- **Matchers match on tool name only** (not file paths or other arguments). The subagent-spawning tool is `Task`, so a matcher on `Task` catches subagent spawns. Matching at the spawn point means one prompt when a subagent is started, not one per tool the subagent later runs.
- `agent_id` / `agent_type` are populated when a hook fires *inside* a subagent; spawned subagents do not inherit parent permissions and may each prompt separately — another reason to gate at the `Task` spawn point rather than inside.

## Consequence for the design

The hybrid fix is buildable as intended: harden the behavioural tool-use rule (steering) **and** add a `PreToolUse` gate on `Task` returning `"ask"` with a cost reason (guarantee). The gate does not control what the user can do — it makes the cost decision visible before a subagent runs.

## Sources

- [Intercept and control agent behavior with hooks — Claude Code Docs](https://code.claude.com/docs/en/agent-sdk/hooks)
- [Claude Code Hooks: Complete Guide to All 12 Lifecycle Events](https://claudefa.st/blog/tools/hooks/hooks-guide)
- [hook-development SKILL.md — anthropics/claude-code](https://github.com/anthropics/claude-code/blob/main/plugins/plugin-dev/skills/hook-development/SKILL.md)
