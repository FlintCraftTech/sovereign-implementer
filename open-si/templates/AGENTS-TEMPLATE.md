# AGENTS.md

<!-- ▼ WORKFLOW-MANAGED — do not edit between these markers. Updated on /setup and reinstall. ▼ -->

This project uses the Sovereign Implementer method.

## Project docs

- **SPEC.md** — product truth. What it is, who it's for, how it works.
- **QUEUE.md** — work queue, top-to-bottom. Red flags (security, privacy, and breach risks Claude surfaced, kept at the top so they're seen first — each carries an open, resolved, or accepted state), Batches (Build/Test/Audit subheadings), Deferred tests (one line per planned test that couldn't run in its own session — source batch slug, what to verify, what confirms it, and two axes: the deferral reason (host-side / needs-user / external) and the runnability once unblocked (Claude-runnable / user-run); /done writes entries here, /plan reads the section each session and asks which deferrals have cleared, rolling the now-runnable user-run ones into a test batch, /done's close-out removes any line this session's activity already confirmed), Captures (split by `---` — processed above with slugs, raw appended below). Items removed from active flow carry `Blocked by:` (trigger-based) or `Parked:` (indefinite) headers. A `--- Plan session here: <reason> ---` marker between batches means /next halts there until a /plan session addresses the named reason.
- **LOG/** — session records: what was built, tested, decided. One file per session entry, plus index.md one-line summaries naming each entry file.
- **FAQ/** — workflow FAQ. Index loaded at session start; details in FAQ/faq.md.

## Workflow

- `/setup` — scaffold project docs (done if you're reading this).
- `/plan` — queue management, captures, design questions.
- `/next` — execute the top batch (build, test, or audit). `/next freeform` does loosely-scoped work that isn't any of those — an ad-hoc change or a discussion of edits already made.
- `/done` — record, update docs, commit.

## Rules for Claude

- SPEC.md is a normal doc — it changes during planning or a build, always with your approval, and there's no separate spec batch. A planning decision that changes what SPEC says edits SPEC in that /plan session; a build that needs a SPEC change asks you and adds SPEC.md to its file list. The safety check still blocks a build from editing SPEC unless its batch lists it, so a spec change never rides in silently. Note spec issues for /plan as they come up.
- Only touch files listed in the active build scope. Halt and ask if you need more.
- One build at a time. Never start a second build while _build.md exists — finish and /done before starting another. (A planning session in a separate chat alongside a build is allowed.)
- State problems plainly. Don't hide them or silently fix unrelated things.
- Route discoveries to QUEUE.md rather than acting on them immediately.

## Language

Language: English

## Editor

Editor: not recorded

<!-- The `.md` editor you work in, from the optional /setup question. When it names an editor, Claude points you to your open docs with a link instead of re-pasting their text into chat, saving tokens. Left as `not recorded` if you skipped the question — Claude then quotes the text inline as usual. -->

<!-- ▲ PLUGIN-MANAGED — do not edit above this line. ▲ -->

## Project rules

<!-- Add your own rules, conventions, and context below. This section is yours — the plugin won't touch it.
     If your project has specific test procedures (how to run tests, what to check, environment setup),
     add them here or point to where they live — Claude will follow them during test entries and /done verification. -->
