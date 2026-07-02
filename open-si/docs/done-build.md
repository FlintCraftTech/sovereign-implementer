# Build close-out

Close-out for build batches (including their test entries). Reached from done.md's router when _build.md's Entry carries a Build subheading. A build that changed SPEC.md (because it listed SPEC in its Files, or grew scope to include it mid-build) closes here like any other build — there is no separate spec-edit close.

## Phase 1: Judgment (while context is fresh)

Captures meaning that would be lost after compaction.

### Mid-close directive — new scope vs build-completing fix [PROMPT]

If a new directive arises during the close — the user raises a change, or verification turns one up — decide where it goes by one line: does it complete the just-built work's own verification, or is it new scope? A fix to a genuine bug in what this build was meant to deliver folds in (finish it, tick it — it's part of the build). New scope — a redesign, a new feature, a change to something that already worked — routes out: a fresh /next, or a capture if it isn't urgent, even if it looks small and even if the user raises it here. /done records and commits; it doesn't take on new build scope. This applies the general mid-close rule in plugin-behaviour.md (Routing and discipline) at the build close.

### 1.1 Verify completion

Read _build.md. All entries ticked?
- **Yes:** Proceed. A test ticked `deferred (reason)` counts as closed, not unfinished — it ran as far as this session could take it, and step 1.3 turns it into a queue line.
- **Some unticked:** [PROMPT] Ask — finish (/next) or close partial (defer unticked, route back to QUEUE.md). Wait for the user's call.

Reconcile the file against memory where the session is still remembered: if _build.md and what you recall disagree — work that happened but went unticked, a Changes note missing something memory knows was done — that mismatch is itself a finding about build discipline, and it routes to Captures (per 1.2). It's the only routine check _build.md's accuracy gets before a fresh session has to rely on it.

When an entry's verification was a user-review of generated output (the user eyeballing a doc, copy, or draft) rather than a pass/fail test, it's closed by asking the user to read it in plain language, not by a test tick — see 1.3.

### 1.2 Route findings to Captures [PROMPT]

Each routed finding is drafted, shown, and approved before it's written, so this step waits on the user. The record of what was flagged is _build.md's notes plus any captures already routed at the moment of noticing — sweep those. Conversation memory, when present, is a same-session bonus pass, never a source this step depends on. Route each finding to Captures, placed per plugin-behaviour.md Captures placement (Claude-directed where applicable, oldest-first as fallback — narrate the placement). Route test failure fixes too.

### 1.3 Write deferred tests

Any planned test from the batch that couldn't run in this session goes to QUEUE.md's "## Deferred tests" section, per done.md Deferred tests — never as LOG-entry prose alone. Each entry ticked `deferred (reason)` in Progress converts mechanically into one queue line: source batch slug, what to verify, what confirms it, and both axes done.md defines — the deferral reason (host-side / needs-user / external) and the runnability once unblocked (Claude-runnable / user-run).

**A user-review of generated output is not a deferred test.** When the batch's verification was the user eyeballing generated output (a doc, copy, a draft) rather than a behaviour check, don't write it as a Deferred-tests line and don't frame it as "mark the test passed" or "defer it to a queue line." Frame the close as a plain request — "have a read of X and tell me if anything's off." If the user hasn't read it yet, hold that as a plain reminder in the recommend-next step, not a Deferred-tests test line. The obligation to look is kept; only the test framing goes (see done.md Deferred tests).

### 1.4 Spec-sync gate [SILENT] when nothing drifts, [PROMPT] when drift found

Build closes only (test and audit land no product changes). Read SPEC.md against the changes this build landed and apply the spec-entry trigger test — whether any sentence in SPEC goes wrong or incomplete given these changes. That is the test plan.md's "SPEC changes are normal build scope" rule names; quote its wording rather than restating it, so the two don't drift.

If the test fires, stop the close — don't commit yet. Surface the drift in plain words, naming which SPEC sentence the build made wrong or incomplete, and get the user's approval to fix it. Then add SPEC.md to _build.md's `Files:` list (so the scope-lock allows the edit), edit SPEC to match what the build landed, and commit SPEC together with the build in this same commit. Don't file it as a capture for a later session.

The why this is now a stop-the-close gate, not a detect-and-file backstop: SPEC is in-session-editable now — the spec-edit batch type is retired (plan.md) — so a build that changed product truth can and must bring SPEC into line in the same commit. Spec-driven development's contract is that the spec moves in the same commit as the behaviour change (resources/research/spec-driven-development-edit-workflow.md); deferring the SPEC fix to a capture would close a commit with SPEC already behind, breaking that atomicity — the exact drift this gate prevents. The gate also catches the leak the old detect-and-file backstop existed for: a build landing a spec-affecting change with no prior spec entry, now fixed in-session rather than filed for luck to catch later. Path-split like the staleness sweep: silent when nothing drifts; stop and surface when it does. Scope: every build close where the build changed product truth.

## Phase 2: Record

### 2.1 Write LOG entry [DISCUSS, PROMPT]

Narrate first [BRIEF]: one sentence noting the batch's reasoning is being carried from _build.md into the LOG entry — the file's last job before /done deletes it.

Draft the entry as its own file under `LOG/`, named per done.md LOG entry files, using this template (placeholder hash — backfilled automatically at the next session start):

```markdown
# [HASH] — [one-line summary]

[Prose rationale — re-authored from the batch's rationale in _build.md, expanded with what was learned during the build (tradeoffs, constraints, approach changes). Inline prose, no `Why:` label.]

**Files touched:**
- [from _build.md Changes]

**Routed to Captures:** [items added, or "none"]
```

Show the wording to the user for approval before writing — the rationale prose carries the why forward, see Why-pipeline in plugin-behaviour.md. This one approval also covers the commit message: the commit title and body derive verbatim from this entry's one-liner and rationale, so the commit step reviews nothing new (see done.md commit core and LOG entry files). This entry is the session's summary — there is no separate chat recap. Before showing it, check whether this session raised and resolved a concern or weighed an alternative that lost; if so, carry it with why it lost (plugin-behaviour.md why-pipeline Preserve). After approval, write it to the new entry file.

If a red flag was accepted during this session, also record the decision in this entry per done.md Accepted red flags — what the user was warned about, and that they chose to proceed.

Prepend to `LOG/index.md` after the header, per plugin-behaviour.md Index entries, ending with the entry's filename:

```
- [HASH] — [index entry] → [entry filename]
```

If _build.md contains an `Index entry candidate:` line and the build ran as planned (no scope shifts that change what the entry should say), reuse that candidate verbatim. If scope shifted, author fresh against the same rule.

### 2.2 Staleness sweep [SILENT] when clean, [BRIEF] when flagging

Path-split like next.md's pre-flight: stay silent when the sweep finds nothing; surface a flag in one or two sentences when it does. Quick check of QUEUE.md against plugin-behaviour.md Dependency ownership Staleness watch — any staleness from any cause, not just what this build changed:
- Remaining batches or Captures reference renamed/deleted files?
- Reference behaviour or rules that this build (or any prior shift the queue hasn't caught up to) has moved past?
- Items sitting long enough that surrounding code or rules have drifted away from them?
- If so, flag — and split the flag by the fix path in plugin-behaviour.md Staleness watch: a fate-decision flag (drop / rewrite / keep) defers to /plan; mechanical maintenance — a drifted pointer whose target content is unchanged, or clearing a met dependency note whose blocker has shipped — is narrate-and-do: fix it here and report it in one line, riding this commit, with no approval ask. Run the unpark watch on the same pass — anything parked that's now newly unblocked? Flag for /plan.

### 2.3 Delete _build.md [SILENT]

Routine bookkeeping — delete the file, no narration. Unlocks future builds. Only after everything above is complete.

### 2.4 Commit

Run the commit core in done.md.

## Phase 3: Recommend next [BRIEF, PROMPT]

Plain-language guard: narrate the captures situation in everyday words — never the background term "processed / unprocessed captures" (see plugin-behaviour.md Vocabulary). Keep the plain statement accurate: don't say the queue is clear when captures are still waiting to be sorted. The scan instruction's "unprocessed Captures" wording below stays as-is — this guard governs only what's said to the user.

Before recommending, scan unprocessed Captures for overlap with the top batch — items that contradict, invalidate, or would benefit the batch if incorporated first (mirrors the capture-overlap scan in next.md's pre-flight blocker gate). State the scan's result either way, not only when it blocks: Captures empty — say nothing's waiting for /plan; Captures waiting but none overlap the next batch — name what's waiting and give the plain verdict that nothing blocks it; overlap found — recommend /plan first and name the overlap. The clean case is a plain assessment, not a hedge — "Three captures are waiting; none touches the next batch, so nothing blocks it," never "there may be overlap worth checking."

Otherwise, based on queue state:
1. Captures routed this session that affect the next batch → recommend /plan, name the blocker.
2. Parked items unblocked by this session's work (per plugin-behaviour.md Dependency ownership Unpark watch) → recommend /plan, name the unpark candidate(s).
3. More batches → name the next batch, then ask whether the user is continuing into another /next now. If yes and a reorder is applicable (per plugin-behaviour.md Dependency ownership), offer to reorder the queue first so the next /next picks the right item.
4. Batches empty → "Queue is clear. Run /plan when you have more."
