# Claude Code hook events — the current registrable set, and what `tool_name` carries

Researched 2026-08-05 from Claude Code's own hook documentation
(`https://code.claude.com/docs/en/hooks`) while processing
[subagent-gate-tool-name-stale]. Filed because three separate queue items rest on
claims about which hook events exist and what they can do, and the answers are not
inferable from this repo's own hooks.

## The question that prompted it, and its non-answer

`pre_tool_use.py` gates subagent spawns on `tool_name == "Task"`, while the desktop
app presents the subagent-spawning tool as `Agent`.

**The documentation does not resolve this.** Its `tool_name` examples are `Bash`,
`Edit`, `Write` and MCP tool patterns (`mcp__memory__.*`). It never names the
subagent-spawning tool for a `PreToolUse` payload. So whether "Task" still arrives
in hook payloads is undocumented — neither confirmed nor refuted — and the
diagnosis-order rule forbids assuming either way. The safe fix is to match both
names, which is correct under either payload.

A worked payload example, for reference:

```json
{
  "session_id": "abc123",
  "hook_event_name": "PreToolUse",
  "tool_name": "Bash",
  "tool_input": { "command": "npm test" },
  "tool_use_id": "toolu_01ABC123..."
}
```

## `SubagentStart` exists, and is NOT a home for a cost gate

It fires once per subagent spawn, before execution, and carries `agent_id` and
`agent_type` (e.g. `"Explore"`, `"Plan"`, or plugin-scoped `my-plugin:reviewer`).
Matchers match on `agent_type`.

**It cannot block and it cannot ask.** It supports `additionalContext`,
`systemMessage`, `terminalSequence`, and exit-code-2 stderr — no
`permissionDecision`, no `deny`, no `ask`. It is documented as informational only.

This matters because it looks like the obvious replacement for the `PreToolUse`
cost gate and would silently downgrade it from a decision the user makes to a
notice they receive after the fact.

## The full registrable event set

Recorded because [no-session-end-or-compaction-hook] asks for exactly this
confirmation before designing, and the set is larger than that item assumed.
This plugin currently registers only the first, fifth and eighth.

```
SessionStart · Setup · UserPromptSubmit · UserPromptExpansion
PreToolUse · PermissionRequest · PermissionDenied
PostToolUse · PostToolUseFailure · PostToolBatch
Notification · MessageDisplay
SubagentStart · SubagentStop
TaskCreated · TaskCompleted
Stop · StopFailure · TeammateIdle
InstructionsLoaded · ConfigChange · CwdChanged
DirectoryAdded · FileChanged
WorktreeCreate · WorktreeRemove
PreCompact · PostCompact
Elicitation · ElicitationResult
SessionEnd
```

Three of these are load-bearing for queued work:

- **`Stop`, `SessionEnd`, `PreCompact`, `PostCompact`** — [no-session-end-or-compaction-hook]
  proposes re-injecting rules after compaction and checking for unrouted work at
  session end. Both events exist, and `PostCompact` (unanticipated by that item) may
  be the better re-injection point than `PreCompact`.
- **`WorktreeCreate`** — [worktree-override-hook] depends on it. Confirmed present.
- **`PermissionRequest` / `PermissionDenied`** — not currently used anywhere in the
  method, and not yet weighed by any queue item.

**Blocking capability was not checked per-event** beyond `SubagentStart`. Anything
built on `Stop`, `PreCompact` or `PostCompact` must re-read the documentation for
what that specific event may return — `SubagentStart` is the standing proof that
"the event exists" and "the event can act" are different claims.
