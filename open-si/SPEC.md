# SPEC — Sovereign Implementer (OpenCode)

## What this is

An OpenCode workflow for non-coders. It gives users a structured workflow for building apps with an AI coding agent without needing to know how to code.

## Who it's for

Non-coders who know what their app should do but need a framework to keep the AI aligned.

## How it works

Splits changes into a build queue that helps the user harness the agent's skills in dependency management, not just coding. The secondary core functionality is basic context window management.

Four commands drive the workflow:
- `/setup` — scaffold project docs and run the onboarding interview.
- `/plan` — manage the queue, add ideas, resolve questions, check for drift.
- `/next` — pick the top queue entry and execute it. A freeform form (`/next freeform`) runs unqueued work — discussion-first sessions, ad-hoc audits, wrapping up changes made by hand — under the same scope and capture discipline.
- `/done` — close the build, record what happened, commit.

Three project docs structure each project:
- `SPEC.md` — product truth. What the app is, who it's for, how it works.
- `QUEUE.md` — work batches, captured ideas, and red flags (security, privacy, and breach risks the agent has surfaced).
- `LOG/` — per-session records of what was built, tested, and decided.

Two hooks enforce discipline mechanically, and a third advises:
- `session_start` — detect project state and load behaviour rules.
- `pre_tool_use` — enforces the scope-lock (which governs SPEC.md like any other file) and git safety, and asks for your approval before the agent spawns a subagent (a cost guard that asks, never blocks).
- `post_tool_use` — advisory QUEUE.md structure lint; flags format drift, never blocks.

One behaviour doc steers everything the hooks can't enforce:
- `plugin-behaviour.md` — loaded at every session start in adopted projects. Carries the cross-skill rules (communication, capture routing, dependency ownership, file safety) and five response-shape tags ([SILENT], [BRIEF], [DISCUSS], [PROMPT], [SEQUENCE]) that procedure docs place on individual steps to control verbosity and interaction. Rule and tag definitions are compliance-hardened: each carries a why-clause, quantified constraints, and an explicit scope statement so it holds against the helpfulness pull of current models.

**Keeping projects current.** The workflow keeps improving while projects sit set up, so a project can fall behind what the current method scaffolds. At the start of a working session, before /plan or /next, the session-start hook catches this two ways: it flags whole docs or folders the project is missing (offering /setup to add them), and it tops up an existing doc that's missing a newer *setting* the method has since added. The top-up is add-only — it never rewrites or clobbers anything the user has written; where a setting needs an answer (like which editor they work in), the agent opens with a one-line question and writes the answer, and settings needing no answer are added silently with a note. The missing-setting check is a list, so new settings join it over time.

**Red flags.** The agent watches for anything that could expose the user's data or their users' data, or amount to a breach, and surfaces it as a red flag instead of quietly building past it. Red flags collect in a section at the top of QUEUE.md, so they're the first thing seen each session. Each flag carries a state — open, resolved, or accepted. An accepted flag records the user's decision in the LOG: what they were warned about, and that they chose to proceed anyway.

## Principles

- Never restrict ideation, just direct it. The user must be able to ideate at any point in the build cycle.
- Hooks enforce what must never happen; hardened rules and tags steer what should usually happen. Mechanical enforcement is cheap and unskippable; behavioural steering is written to survive priority conflicts on the models users actually run.
- Execution sessions trend toward pure execution. Ideas and discoveries can be captured anywhere, but deciding their fate is planning work and happens in planning sessions.
- Surface risk in plain language; never bury it. The agent screens for data-exposure and breach risks and flags them where the user can't miss them.
- Readable output is a control requirement, not a style preference. The user keeps the agent aligned by reading and approving what it does, so output too long to get through breaks that control. Lead with the decision, then stop; gate detail behind an explicit request. This is anti-overwhelm, not terseness — the levers are sequencing and leading with the decision, never a word-count cap, and plain English is the standard the concision serves.
