# Can a hook force the behaviour rules to be read?

**Decision recorded 2026-08-19: the findings below stand, and enforcement was
put to the user and refused.** Nothing here is superseded — a `PreToolUse` hook
can still do what §2 describes. What was answered is whether it is worth doing,
and the answer is no. A read-gate enforces that the file was *opened*, and every
recorded failure in this corpus is a read-and-not-followed failure: the
provenance rule shipped, sharpened and still not holding; the file-the-blocker
rule explained five to ten times in a month; the INBOX-opening step skipped in
the session that authored it. There is no recorded instance of the rules going
unread. So the gate would pay the most expensive option in this document's own
cost ordering — a transcript scan on every tool call — to close a hole nobody
has observed, one layer above the hole everyone has. The rule board is the same
experiment already run: built so the rules could watch themselves, it reported
clean while five real rule defects shipped in one session. The queue item
carrying this question, `[behaviour-rules-read-is-enforceable]`, was deleted in
the same move. **Re-propose only against new evidence that the rules are going
unread**, which is the specific thing nobody has yet seen.

Fetched 2026-08-10 from the Claude Code hooks reference
(`https://code.claude.com/docs/en/hooks`, reached via a 301 from the older
`docs.claude.com/en/docs/claude-code/hooks`). Run because `session_start.py`'s
behaviour-rules directive is an instruction with no enforcement behind it, and
its own docstring names "a skimmed redirect" as the failure mode it accepts.

## Finding 1 — `SessionStart` cannot force anything

`SessionStart` hooks support context only. They **cannot block or deny**. The
fields available under `hookSpecificOutput` are `additionalContext`,
`initialUserMessage`, `watchPaths`, `sessionTitle` and `reloadSkills`.

So there is no way to make the read happen *at session start*. Any forcing
mechanism has to fire later, at the first tool call.

## Finding 2 — the 10,000-character cap is PER HOOK COMMAND, not aggregate

The documented wording: hook output strings, including `additionalContext`,
`systemMessage`, and plain stdout, are capped at 10,000 characters, and output
exceeding the limit is saved to a file and replaced with a preview and file
path.

The reference states this limit applies **per hook command**, not in aggregate.
When one hook's output exceeds the cap, Claude Code writes the full text to a
file and passes a preview plus the path instead.

**This matters because it contradicts the stated premise of the current
design.** `session_start.py:360-384` says the rules are pointed at rather than
pasted because the file "is tens of kilobytes, so appending it whole blew the
cap by a wide margin and the rules reached no session at all". That is true of
*one* hook command. Several `SessionStart` commands, each emitting under 10,000
characters, could carry the rules directly into the session with no read
required.

Unmeasured and not to be assumed: whether the harness concatenates multiple
SessionStart outputs cleanly, in a stable order, and whether the total is
subject to any separate limit further up. The doc says nothing either way.
Verify by experiment before designing on it.

## Finding 3 — `PreToolUse` receives `transcript_path`, and can deny

Input fields to a `PreToolUse` hook include `session_id`, `prompt_id`,
**`transcript_path`**, `cwd`, `permission_mode`, `effort`, `hook_event_name`,
plus `agent_id` / `agent_type` in a subagent, and the tool-specific
`tool_name`, `tool_input`, `tool_use_id`.

Example shape given in the reference:

```json
{
  "session_id": "abc123",
  "prompt_id": "550e8400-e29b-41d4-a716-446655440000",
  "transcript_path": "/home/user/.claude/projects/.../transcript.jsonl",
  "cwd": "/home/user/my-project",
  "permission_mode": "default",
  "hook_event_name": "PreToolUse",
  "tool_name": "Bash",
  "tool_input": { "command": "rm -rf /tmp/build" },
  "tool_use_id": "toolu_01ABC123..."
}
```

Denial is available two ways — structured output:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Destructive command blocked by hook"
  }
}
```

with `permissionDecision` accepting `"allow"`, `"deny"`, `"ask"` or `"defer"`;
or exit code 2 with the reason on stderr.

**So a read-gate is constructible:** a `PreToolUse` rule that reads
`transcript_path`, looks for a completed Read of the behaviour doc, and denies
(or asks) until it finds one.

Unmeasured: the transcript's on-disk format and whether a Read's target path is
recoverable from it reliably; how the gate behaves on resume, on compaction, and
in a subagent, all of which change what the transcript holds. The mechanism is
confirmed available; its reliability is not.

## Finding 4 — `Stop` receives the final assistant message directly (added 2026-08-11)

Looked up while designing a mechanism for [write-first-report-without-write], and
recorded here because the answer would otherwise have to be found again.

A `Stop` hook exists and fires when Claude finishes responding. Its stdin carries
`session_id`, `prompt_id`, `transcript_path`, `cwd`, `permission_mode`,
`hook_event_name`, `effort`, and — the field that matters —
**`last_assistant_message`**: the complete final response text for that turn. So a
check on what Claude *said* needs no transcript parsing at all, which is what
Finding 2's gate would have required.

It can return `{"decision": "block", "reason": "..."}` (or exit 2), which does not
end the turn: it prevents stopping and continues the conversation with the reason
fed back. It can also return `additionalContext` in `hookSpecificOutput` to inject
feedback without blocking. Unlike `PreToolUse`, it **cannot** escalate to the user
for a permission decision.

Caveats from the same source: it fires once per turn including turns that end in a
question to the user, but does **not** fire for `EndConversation` tool calls; the
default hook timeout is 600 seconds; and a `stop_hook_active` loop-protection flag
is **not documented**, so any blocking hook must carry its own loop protection.

**The consequence for enforcement design.** `PreToolUse` and `Stop` guard different
failures and are not interchangeable. A rule about what Claude must *do before
acting* (read the behaviour doc) is gated at the tool call. A rule about what Claude
must not *claim* has no tool call attached — the false claim is text — so only an
end-of-response hook can see it. Source: https://code.claude.com/docs/en/hooks.md

## What this does not settle

Whether either mechanism is worth building. Both have real costs — a per-call
transcript scan on every tool use, or several hook commands whose combined
behaviour is undocumented. This file records that the options exist, against a
shipped design that assumed they did not.
