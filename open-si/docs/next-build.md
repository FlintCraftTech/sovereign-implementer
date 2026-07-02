# Build procedure

Execution procedure for build batches. Reached from next.md after pre-flight checks and scope lock are complete.

## Execute [SILENT]

Execute entry by entry.

The silence here governs the success path — the routine bookkeeping of making changes and ticking entries when things go fine. It is not a gag on the moments that must speak: reporting a failure, asking before scope grows, handing a test to the user, and revealing a readable edit's new text (below) all speak. A response-shape tag on one of those specific moments overrides this step's silence — that's the precedence rule working as intended, not a conflict.

**No pre-edit preview.** Don't precede an edit with a point-form list of the changes you're about to make. The work was already agreed in /plan, and a "here's what I'm about to change" beat right before an edit that lands almost instantly is just noise. This holds for every edit, readable or code — the success path stays quiet until the entry is done, minus that preview.

**Readable edits reveal their new text** [the reveal speaks; informational, not an ask]. When an edit changes readable (non-code) content — a doc, copy, a spec section, anything a person reads rather than runs — show the actual new wording in chat *after* making the edit, as a wrapped, readable block. It's an informational reveal, so don't append an approval ask: the change was already agreed in /plan. Why it's worth surfacing: the exact wording is produced here in /next and was never seen in /plan, which agreed only the intent — so this is the first time the user meets the real words. A code edit doesn't get this half — a non-coder can't review code text the same way — so a code edit stays silent on the success path (still no preview).

**A small mid-build tweak to a just-surfaced readable edit is in scope** [PROMPT]. Once the new text is visible, the user may ask for a small "just change this one bit" tweak. A tweak that refines the build's already-agreed work product is refining the work, not new planning: make it, reveal the updated text, and record it in _build.md Changes so it folds into the single LOG entry /done writes — no separately logged object (a new index line would bloat the index), and no /plan round-trip. A request that's actually new scope — a different feature, or a change to something that already worked — is not this; route it out via Scope management below, like any out-of-scope ask.

### Build entries

For each:

1. Read any relevant existing code or context.
2. Make the changes — no point-form preview first (see Execute above).
3. If the change is readable (non-code) content, reveal the new text in chat as a wrapped, readable block — informational, no approval ask. Code edits skip this; the success path stays silent.
4. Tick it in _build.md Progress: `- [x] entry description — done`

### Test entries

When the batch contains test entries (under a Test subheading), execution is verification, not file editing. Route each test into one of three categories — this mirrors plan.md's testing categories, restated here because a /next session doesn't load plan.md:

- **Run-now (inline)** — any test you can run this session (read code, run commands, inspect output, check file content), including environment-dependent tests when the environment is available. The default.
- **User-must-run** — a visual, point-and-click, physical, or subjective check only the user can make. Hand it over: [PROMPT] state what you need checked and wait.
- **Environment-dependent or host-side** — a test you'd run yourself but that needs a device, emulator, or environment absent this session, or that awaits a push + reinstall. Defer it.

Run-now is the default; defer is the exception, justified only by user-must-run or environment-absent, never a catch-all for "can't run this second."

For each:

1. Read the test description to understand what's checked.
2. Route it by the categories above — run every run-now test yourself; hand user-must-run tests to the user; defer the environment-dependent or host-side ones.
3. Tick each in _build.md Progress, pass/fail:
   - `- [x] Test description — ✓`
   - `- [x] Test description — ✗ (reason)`
   - `- [x] Test description — deferred (reason)` — written the moment a test is determined unrunnable in this session (host-side, needs the user, waiting on an external event). Records the determination in the file so a post-/clear /done doesn't misread the entry as unfinished work; it becomes a Deferred tests line at /done carrying its deferral reason and runnability.
4. Accumulate results in Changes: what was checked, what passed, what failed.

**On test failure:**
- Isolated (one test, rest unaffected): [BRIEF] note it, continue, route the fix to Captures at close.
- Fundamental (invalidates the batch premise or blocks remaining tests): stop, go to Course-correction below.

**Before deferring a test for a missing device or environment, don't assume it's absent — check.** When a test would otherwise be deferred because a device, emulator, or environment "isn't available here," ask the user whether one is available rather than assuming none is. And before using any connected device, ask permission first: "May I use your connected device to test this?" — then wait for a yes. This applies the Device and hardware access rule in plugin-behaviour.md at the verification step. The why: a connected device the user didn't expect Claude to touch is a consent surprise, and a test wrongly deferred on a guess that no device was present sits unrun for weeks.

### Rules during build

Absolute regardless of entry type:

- Stay within the active batch's described work — that's build scope (see plugin-behaviour.md Scope). Growing past it needs approval first (see Scope management below).

**Accumulate close notes** as you go — jot what changed in _build.md so /done needn't re-explore:
```
Changes:
- file1.ext: created new component, 45 lines
- file2.ext: added import + handler function
- [test] walked through mixed batch scenario — ✓, procedure unambiguous
```

## Scope management

These sections elaborate the discovery decision rule in plugin-behaviour.md (Routing and discipline): work needed to complete the batch is added or split; work not needed is captured and the session continues. The cases below are how that rule plays out during a build.

### User raises something out of scope [PROMPT]

1. Route it to Captures in QUEUE.md, placed per plugin-behaviour.md Captures placement (Claude-directed where applicable, oldest-first as fallback — narrate the placement). Draft the wording first as a blockquote with a content-type lead-in (**Capture draft:**) for approval, per plugin-behaviour.md (Captures + approval-time outputs).
2. Ask "anything else?" — repeat until no.
3. Resume the build.

**Coherence exception:** Default is capture, per above. The exception is narrow and keyed to why-pipeline coherence: if the item would share the build's log entry and index line — per plugin-behaviour.md Index entries — and folding it in makes the batch easier to find later rather than harder, add it to _build.md as a new entry (appending any files it names to the `Files:` section) and continue. Evaluate against the coherence rules, not user convenience. When uncertain, capture.

### Scope grows during the build [PROMPT]

Both paths below ask and wait, so the tag sits on the whole section. If the work needs to grow past what the entries describe — whether that means a new file or more change inside a file already listed — the trigger is the same: growth is measured against the described work, not the Files: list. Name the new work and the files it needs, then:

- **Minor** (a small prerequisite, one or two files): ask to add, naming the work and the files: "This needs [work], which means editing [file] — add it to scope?" Once approved, append any not-yet-listed file to _build.md's `Files:` section before editing it — the scope-lock denies edits to unlisted files.
- **Significant** (multiple new files, design uncertainty): propose splitting. Finish what's scoped, /done to close, then /plan to queue the rest.

**A SPEC change the build discovers it needs is a legitimate scope-grow.** SPEC.md is a normal file a build can add to scope — the separate spec-edit batch a build used to be forced to queue is retired. When the build finds a SPEC sentence must change for the work to be correct, treat it like any scope-grow: name the change and ask ("this needs SPEC to say X instead of Y — add SPEC.md to scope?"), and once approved, append SPEC.md to _build.md's `Files:` section before editing it (the scope-lock denies SPEC until it's listed). Then edit SPEC inline as part of the build. The why this is safe in-build now: spec-driven development wants the spec to move in the same commit as the behaviour change, and the /done-build spec-sync gate (done-build.md) backstops it — that gate stops the close if the build changed product truth and SPEC wasn't brought into line. So the build edits SPEC inline with the user's approval and the close guarantees the two ship together. A SPEC change is product truth, so it always gets the explicit ask — it never rides in silently.

## Mid-build course-correction

### Claude discovers user-runnable testing is needed [PROMPT]

When Claude notices something will need user-runnable testing beyond the batch's Test section — visual check, physical-device behaviour, subjective judgment Claude can't verify:

1. Route the discovery to Captures in QUEUE.md as a future test-only batch. Draft the wording (what needs testing and why), show before writing per plugin-behaviour.md Captures.
2. Ask "anything else?" — repeat until no.
3. Resume the build.

Don't attempt the test inline. Don't extend the current batch's scope to include it.

### Approach not working [DISCUSS, PROMPT]

If something goes wrong — a false assumption, a missing dependency, an approach that isn't working:

1. **Stop building.** Don't push through a broken approach.
2. **State the problem plainly.** What you expected, what happened, why the current approach won't work.
3. **Propose a path forward:**
   - **Adjust scope:** drop an entry, add a prerequisite, change the approach. Update _build.md to match.
   - **Abort and requeue:** if the whole batch is unsalvageable:
     1. Return the batch text to QUEUE.md under Batches. Placement is Claude's call per plugin-behaviour.md Dependency ownership — original position or top, by what was learned.
     2. Route any captures surfaced during the attempt to Captures as normal.
     3. Route the reshape direction to Captures, pointing at the batch slug. The trigger is mechanical: abort + batch returned + a reshape direction or learning the queue needs in conversation = capture needed. Unrouted, the direction survives only in the LOG entry, which /plan doesn't read at planning time, and the batch re-presents unchanged at the next /next.
     4. Tell the user to run /done. _build.md stays in place so /done's router still fires the build close-out — see done.md. Differences from a completed build: the LOG entry describes the attempt and why it was aborted, and the batch returns to QUEUE.md rather than disappearing into the log.
4. **Wait for the user's call.** Don't pick a path without confirmation.

## Context management

If context is running low, prefer in order:

1. **Finish and /done.** If most entries are ticked, push through. Short-term memory is enough.
2. **Close partial.** If significant work remains, /done what's ticked and requeue the rest. The next session picks up cleanly from _build.md and QUEUE.md.

## Completion [BRIEF, PROMPT]

When all entries are ticked:

1. Tell the user the build is complete.
2. Say: "Run /done to record this and commit, or tighten what's already built before closing." Tightening means refining done entries — not raising new work. Anything new routes through the existing paths: out-of-scope via Scope management above, thinking work via Captures. No chat summary of the changes — the LOG entry /done writes is the single session summary.

Do NOT delete _build.md yourself. That's /done's job.
