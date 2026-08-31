# Plan Panel Integration Research

Researched 2026-06-03. Context: the plugin's /plan and /next skills don't integrate with the Claude Code desktop app's Plan panel.

## How the Plan panel works

The desktop app (redesigned April 2026) has a Plan side panel that renders plans with Approve/Reject buttons. The mechanism:

1. Claude calls `EnterPlanMode` — enters read-only mode (only Read, Glob, Grep, LS available)
2. Claude writes a plan as markdown to a file in `~/.claude/plans/` (or a project-configured `plansDirectory` in `.claude/settings.json`)
3. Claude calls `ExitPlanMode` — the plan renders in the side panel
4. User approves or rejects

Plans are plain markdown files with auto-generated names (e.g. `jaunty-petting-nebula.md`). No special structure beyond text.

## Why SI is incompatible

- `/plan` writes to QUEUE.md, never calls EnterPlanMode/ExitPlanMode. Plan panel stays empty.
- `/next` presents batches for approval in chat, not through the panel.
- `EnterPlanMode` restricts Claude to read-only tools — can't write QUEUE.md while in Plan Mode.

## Prior art: Superpowers plugin

The Superpowers plugin (obra/superpowers, issue #1260) hit the same problem. Their writing-plans skill writes plans to markdown but never enters native Plan Mode.

Three approaches proposed:
- **Option A — Post-write sync:** After the planning skill finishes, enter Plan Mode, write a summary to the plan file, call ExitPlanMode. Panel gets a rendered copy; the real plan file on disk stays the source of truth.
- **Option B — Parallel write:** Write to both the skill's target file and the plan-mode file simultaneously.
- **Option C — Config flag:** Let users opt into native panel integration via a setting.

## Hook integration

- PreToolUse/PostToolUse hooks do NOT fire for EnterPlanMode/ExitPlanMode (GitHub issue #21282 requests this).
- PermissionRequest hooks CAN intercept ExitPlanMode — this is how the Plannotator plugin works.
- Known bug: ExitPlanMode hooks execute with cwd set to ~ instead of the project directory (GitHub issue #22343).

## Considerations for SI

1. **Read-only constraint is the main blocker.** EnterPlanMode disables Write/Edit/Bash. Our /plan skill needs to write QUEUE.md. We can't wrap /plan inside Plan Mode without fundamental restructuring.

2. **Post-write sync (Option A) is most feasible.** After /plan finishes processing captures and creating batches, we could enter Plan Mode, write a summary of what changed to the plan file, and exit. The panel would show the planning outcome for approval. But this adds ceremony to a workflow that already has its own approval flow.

3. **/next is a better fit than /plan.** When /next presents a batch with "Ready?", that's closer to what the Plan panel is designed for — "here's what I'm about to do, approve it." We could enter Plan Mode, write the batch details to the plan file, and let the user approve via the panel instead of (or in addition to) the chat prompt.

4. **Cost: extra tool calls and context.** EnterPlanMode and ExitPlanMode are tool calls that add to the conversation. Plan Mode also injects additional system prompt content. For a plugin focused on context efficiency, this is a real tradeoff.

5. **Cross-platform concern.** SI targets Claude Code broadly (desktop app, CLI, IDE extensions). Plan panel is desktop-app-specific. Any integration should be opt-in or gracefully degrade.

## Sources

- [Desktop application - Claude Code Docs](https://code.claude.com/docs/en/desktop)
- [Redesigning Claude Code on desktop for parallel agents](https://claude.com/blog/claude-code-desktop-redesign)
- [Superpowers issue #1260 — Plan panel integration](https://github.com/obra/superpowers/issues/1260)
- [Feature request: Plan mode hook events (issue #21282)](https://github.com/anthropics/claude-code/issues/21282)
- [ExitPlanMode cwd bug (issue #22343)](https://github.com/anthropics/claude-code/issues/22343)
- [Plannotator plugin docs](https://plannotator.ai/docs/guides/claude-code/)
- [What Actually Is Claude Code's Plan Mode? — Armin Ronacher](https://lucumr.pocoo.org/2025/12/17/what-is-plan-mode/)
