# Test procedure

Execution procedure for test-only batches. Reached from next.md after pre-flight checks and scope lock are complete.

## Execute [SILENT]

The silence here governs the success path — the routine bookkeeping of running checks and ticking entries when things go fine. It is not a gag on the moments that must speak: reporting a failure, asking before scope grows, and handing a test to the user all speak. A response-shape tag on one of those specific moments overrides this step's silence — that's the precedence rule working as intended, not a conflict.

For each test entry:

1. Read the test description to understand what's checked.
2. Run every test you can verify yourself: read code, run commands, inspect output, check file content. Only tests needing real human interaction (visual appearance, physical device behaviour, subjective judgment) go to the user — handing one over is a speaking moment: [PROMPT] state what you need the user to check and wait.
3. Tick each in _build.md Progress, pass/fail:
   - `- [x] Test description — ✓`
   - `- [x] Test description — ✗ (reason)`
   - `- [x] Test description — deferred (reason)` — written the moment a test is determined unrunnable in this session (host-side, needs the user, waiting on an external event). Records the determination in the file so a post-/clear /done doesn't misread the entry as unfinished work.
4. Accumulate results in Changes: what was checked, what passed, what failed.

**On test failure:**
- Isolated (one test, rest unaffected): [BRIEF] note it, continue, route the fix to Captures at close.
- Fundamental (invalidates the batch premise or blocks remaining tests): stop, go to Course-correction below.

### Rules during test

- Stay within the test entries' described scope. If a test reveals something unrelated, route it per the discovery rule in plugin-behaviour.md (Routing and discipline): capture at the moment of noticing, then continue.

**Accumulate close notes** as you go:
```
Changes:
- [test] walked through mixed batch scenario — ✓, procedure unambiguous
- [test] checked error handling path — ✗ (missing fallback for empty input)
```

## Scope management

These sections elaborate the discovery decision rule in plugin-behaviour.md (Routing and discipline): work needed to complete the batch is added or split; work not needed is captured and the session continues. The cases below are how that rule plays out during testing.

### User raises something out of scope [PROMPT]

1. Route it to Captures in QUEUE.md, placed per plugin-behaviour.md Captures placement (Claude-directed where applicable, oldest-first as fallback — narrate the placement). Draft the wording first as a blockquote with a content-type lead-in (**Capture draft:**) for approval, per plugin-behaviour.md (Captures + approval-time outputs).
2. Ask "anything else?" — repeat until no.
3. Resume testing.

### Test surfaces unexpected scope

If a test reveals additional verification is needed beyond the batch's entries:

- **Minor** (one related check): [PROMPT] ask to add, continue if approved.
- **Significant** (new test area, design uncertainty): capture it as a future test need and finish the scoped tests first. (No wait — this notes for the queue and continues, so the tag stays off the significant path.)

## Course-correction

### Approach not working [DISCUSS, PROMPT]

If something goes wrong — a test is impossible to run as described, a prerequisite is missing, or the test batch's premise is invalid:

1. **Stop testing.** Don't push through a broken premise.
2. **State the problem plainly.** What you expected, what happened, why the current approach won't work.
3. **Propose a path forward:**
   - **Adjust scope:** drop a test, add a prerequisite, change the verification approach. Update _build.md to match.
   - **Abort and requeue:** if the whole batch is unsalvageable:
     1. Return the batch text to QUEUE.md under Batches.
     2. Route any captures surfaced during the attempt to Captures as normal.
     3. Route the reshape direction to Captures, pointing at the batch slug. The trigger is mechanical: abort + batch returned + a reshape direction or learning the queue needs in conversation = capture needed. Unrouted, the direction survives only in the LOG entry, which /plan doesn't read at planning time, and the batch re-presents unchanged at the next /next.
     4. Tell the user to run /done.
4. **Wait for the user's call.** Don't pick a path without confirmation.

## Context management

If context is running low, prefer in order:

1. **Finish and /done.** If most tests are ticked, push through.
2. **Close partial.** If significant tests remain, /done what's ticked and requeue the rest.

## Completion [BRIEF, PROMPT]

When all tests are ticked:

1. Tell the user testing is complete, with the pass/fail counts — failures were already stated plainly as they happened.
2. Say: "Run /done to record this and commit, or review what's already tested before closing." Reviewing means re-examining what was already tested — not raising new work. Anything new routes through the existing paths: out-of-scope via Scope management above, thinking work via Captures. No chat summary of the results — the LOG entry /done writes is the single session summary.

Do NOT delete _build.md yourself. That's /done's job.
