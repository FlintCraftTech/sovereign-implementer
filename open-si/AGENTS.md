# AGENTS.md — Sovereign Implementer (OpenCode)

OpenCode auto-loads this file on session start.

## What this is

The Sovereign Implementer — an OpenCode workflow that gives non-coders a structured workflow for building apps with an AI coding agent.

**Who it's for.** Non-coders who know what their app should do but need a framework to keep the agent aligned.
**Core tension it solves.** Non-coders need heavy docs to keep the agent on track, but heavy docs burn context window. The workflow balances this: hooks enforce mechanically (cheap), commands load procedures on demand (only when needed).

## Audience

The workflow's users are external non-coders building their own apps with OpenCode — not the person developing the workflow. This project is the unusual case: the developer (Alex) is also a non-coder using the workflow to build the workflow. Command docs must be written for the external user, not for Alex.

Concretely: anything a command causes the agent to *say to the user* — chat narration, drafts, prompts, headings, status lines, error messages — must read cleanly for an external non-coder. No internal procedure terms (e.g. "plugin-behaviour.md," "the [SILENT] tag," "Step 2.4," "Pass B," "trickle-up"). Internal terms belong inside procedure docs where the agent reads them; they must not leak into output the user sees.

When editing any command or doc, check the output-facing strings against this audience before saving.

## Model target

This workflow is model-agnostic — it runs on any capable model OpenCode supports (Claude, GPT, Gemini). The original Claude Code version targeted Opus 4.8 specifically. This OpenCode port drops that single-model dependency: response-shape tags and behaviour rules are written to hold across models. If a particular model shows compliance issues, steer it with the general authoring heuristic (`resources/authoring-heuristic.md`), updated for the current model landscape.

## Architecture

**3 project docs** (created by `/setup` in consumer projects):
- `SPEC.md` — product truth. What the app is, who it's for, how it works.
- `QUEUE.md` — red flags (security/privacy/breach risks the agent surfaced, kept at the top, each with an open/resolved/accepted state), work batches (Build/Test/Audit subheadings), and captured ideas (plain bullets).
- `LOG/` — per-session records. `LOG/index.md` for summaries (newest first), one file per session entry.

**4 commands:**
- `/setup` — scaffold docs + ask 5 questions to populate SPEC.md.
- `/plan` — all thinking work: queue management, read-back, ideas, questions, drift detection.
- `/next` — pick the top queue entry, execute it (build, test, or audit).
- `/done` — record what happened, clean up, commit.

**3 hooks** — two enforcing, one advisory. Implemented as a TypeScript plugin loaded by `hooks.md`:
- `session.created` hook — detect project state (unadopted / adopted / active build), load behaviour rules, check version against .si-version, backfill LOG hashes.
- `tool.before.*` hook — scope-lock to the active batch's file list, git safety, subagent cost gate.
- `tool.after.write` hook — QUEUE.md structure lint; flags format drift after a QUEUE.md edit, never blocks.

## Where things live

```
open-si/
  AGENTS.md               — this file
  opencode.json           — plugin & config registration
  .gitignore
  .opencode/
    commands/              — setup, plan, next, done (.md files)
    hooks/
      hooks.md             — hook declarations
    plugin/
      si-plugin/           — TypeScript plugin (session start, scope gate, queue lint)
        src/
          index.ts
          session-start.ts
          pre-tool-use.ts
          post-tool-use.ts
  SPEC.md                  — this project's spec
  QUEUE.md                 — this project's work queue
  LOG/                     — this project's session logs
  docs/                    — procedure docs loaded by commands
    plugin-behaviour.md
    setup.md, plan.md, next.md, done.md
    next-build.md, next-test.md, next-audit.md, next-freeform.md
    done-build.md, done-test.md, done-audit.md, done-plan.md, done-freeform.md
  templates/
    AGENTS-TEMPLATE.md     — consumer project template
    faq-template.md
    faq-index-template.md
  resources/               — authoring guides, research, E2E test workflows
```

## Working conventions

- **Run commands directly.** Don't ask Alex to run them unless they require a separate session.
- **Route decisions to QUEUE.md.** Don't hold design decisions in conversation only.
- **Cross-doc references go by name.** When editing docs, reference steps by name, never step number.
- **Author method text with the authoring heuristic.** Every self-hosting build batch runs against `resources/authoring-heuristic.md` before its authored text ships.
- **FAQ entries are part of batch authoring.** A batch that introduces something a consumer would ask about carries a faq-template.md entry.
- **A new batch type touches four places.** Adding a batch type must wire: `docs/next.md`, `docs/done.md`, `post_tool_use.ts`'s ALLOWED_SUBHEADINGS, and `docs/plan.md`'s batch structure step.

### Self-hosting dependency ordering

Batch ordering in QUEUE.md implicitly assumes the next batch sees the previous batch's effects. That's true for most changes. It's false for **plugin-side** changes — edits to the TypeScript plugin files (`src/*.ts`) which only take effect after a rebuild.

When a batch depends on a previous batch's plugin-side effects, /plan must place the dependent batch after a push marker:

**Push-marker convention.** A line `--- Rebuild required before continuing ---` between batches in QUEUE.md indicates /next must halt until the plugin has been rebuilt (`npm run build`).

## Build and Release

### Build (local testing)

When Alex says "build" or asks to test:
1. Run `npm run build` in `.opencode/plugin/si-plugin/`.
2. Restart OpenCode so the new plugin loads.

### Release

When Alex says "release" — bump version, tag, and publish:
1. Backfill any unfilled commit-hash placeholders in `LOG/`.
2. Bump version in `.opencode/plugin/si-plugin/package.json`.
3. Pre-release consistency sweep: read git log for unpushed changes, check templates against procedure docs, check docs against current state.
4. Stage everything, commit: "Bump to v<VERSION>".
5. `git push`.
6. Publish a GitHub Release with release notes.

## Goal sessions

A goal session is the developer's autonomous-build workflow: the agent works through several build batches back-to-back in one chat, closed by a manual /done.

**The run.** The agent works the batches back-to-back in one session, owning the sequencing itself and stopping only for what genuinely needs the user. It uses a single aggregate `_build.md` that lists the batches it will work through, kept as a working-state and resume record. List every file across the batches in its `Files:` section.

**The close.** One manual /done closes the whole run:
- It writes a separate LOG entry per batch — one entry file and one index line each — and lands them all in a single end-of-run commit.
- It runs the shipped-slug cross-check.
- It runs the deferred-test and staleness sweeps once across all the batches at the close.
- It does the LOG-hash backfill by hand.

Handoff-claim provenance. When a session opens from an agent-authored handoff or context prompt, treat its claims as unverified until the user confirms them.

## E2E testing

Test consumer project lives separately. Alex runs E2E in a separate OpenCode session; observations come back here as queue items.

## User context

Alex is a non-coder using OpenCode. Explain things in plain English.

Editor: Zettel — the .md editor Alex works in.

## Current state

**Status:** Port v2.0.0 — initial OpenCode port from Claude Code v1.15.0.

## Workflow

- `/setup` — initial project scaffolding.
- `/plan` — manage the queue, add ideas, resolve questions, check for drift.
- `/next` — execute the top queue entry (build, test, or audit).
- `/done` — close the session, record what happened, commit.

## Rules for the agent

- SPEC.md is a normal doc any batch can edit.
- Only touch files listed in the active build scope. Halt and ask if you need more.
- One build at a time. Finish and /done before starting another.
- State problems plainly. Don't hide them or silently fix unrelated things.
- Design for fresh, short sessions. The system must work for a fresh, short session that carries none of a prior session's memory: the files must suffice on their own.
- Route discoveries to QUEUE.md rather than acting on them immediately.
- All use of the workflow to develop the workflow is testing the workflow. Any observation of the agent's behaviour is a testing outcome and must be routed to Captures.
- Memory boundaries — the project's records belong in the project's docs, never in memory. Route: ideas and discoveries to Captures, design decisions to QUEUE.md and SPEC.md, project state to the method docs.
