# Audit close-out

Close-out for audit batches. Reached from done.md's router when _build.md's Entry carries an Audit subheading. Audits edit no source files — the session's product is the captures it routed.

## Phase 1: Judgment (while context is fresh)

### 1.1 Verify completion

Read _build.md. All findings ticked (captured or dropped)?
- **Yes:** Proceed.
- **Some unticked:** [PROMPT] Ask — finish presenting them (/next) or close partial (defer unticked, route the remainder back to QUEUE.md). Wait for the user's call.

### 1.2 Route stragglers to Captures [PROMPT]

Each straggler is drafted, shown, and approved before it's written, so this step waits on the user. The findings themselves were routed during the audit. The record of anything else flagged along the way — observations outside the audit's criteria, process issues — is _build.md's notes plus any captures already routed at the moment of noticing; sweep those. Conversation memory, when present, is a same-session bonus pass, never a source this step depends on. Route each to Captures, placed per plugin-behaviour.md Captures placement (narrate the placement).

## Phase 2: Record

### 2.1 Write LOG entry [DISCUSS, PROMPT]

Draft the entry as its own file under `LOG/`, named per done.md LOG entry files, using this template (placeholder hash — backfilled automatically at the next session start):

```markdown
# [HASH] — [one-line summary]

[Prose rationale — what was audited against which criteria and why, re-authored from the batch's rationale in _build.md; what the read surfaced. Inline prose, no `Why:` label.]

**Files touched:**
- [the target artifacts that were read — the audit edited nothing]

**Routed to Captures:** [findings captured, or "none"]

**Approval outcomes:** [what happened at bulk approval — findings dropped or reworded, each with the user's reason; or "all findings approved as-is"]
```

The Approval outcomes line records what the bulk-approval step decided: a finding the user dropped, or reworded, with the reason they gave. Recording it means a decision made at audit time doesn't vanish — without it, the only trace of a dropped or reworded finding is its absence. When every finding was approved as-is, say so in one phrase rather than omitting the line.

Show the wording to the user for approval before writing — see Why-pipeline in plugin-behaviour.md. This one approval also covers the commit message: the commit title and body derive verbatim from this entry's one-liner and rationale, so the commit step reviews nothing new (see done.md commit core and LOG entry files). This entry is the session's summary — there is no separate chat recap. Before showing it, check whether this session raised and resolved a concern or weighed an alternative that lost; if so, carry it with why it lost (plugin-behaviour.md why-pipeline Preserve). After approval, write it to the new entry file.

If a red flag was accepted during this session, also record the decision in this entry per done.md Accepted red flags — what the user was warned about, and that they chose to proceed.

Prepend to `LOG/index.md` after the header, per plugin-behaviour.md Index entries, ending with the entry's filename:

```
- [HASH] — [index entry] → [entry filename]
```

If _build.md contains an `Index entry candidate:` line and the audit ran as planned (no scope shifts that change what the entry should say), reuse that candidate verbatim. If scope shifted, author fresh against the same rule.

### 2.2 Staleness sweep [SILENT] when clean, [BRIEF] when flagging

Path-split like next.md's pre-flight: stay silent when the sweep finds nothing; surface a flag in one or two sentences when it does. Quick check of QUEUE.md against plugin-behaviour.md Dependency ownership Staleness watch — any staleness from any cause, not just what this audit surfaced:
- Remaining batches or Captures reference renamed/deleted files?
- Reference behaviour or rules that anything since has moved past?
- Items sitting long enough that surrounding code or rules have drifted away from them?
- If so, flag — and split the flag by the fix path in plugin-behaviour.md Staleness watch: a fate-decision flag (drop / rewrite / keep) defers to /plan; mechanical maintenance — a drifted pointer whose target content is unchanged, or clearing a met dependency note whose blocker has shipped — is narrate-and-do: fix it here and report it in one line, riding this commit, with no approval ask. Run the unpark watch on the same pass — anything parked that's now newly unblocked? Flag for /plan.

### 2.3 Delete _build.md [SILENT]

Routine bookkeeping — delete the file, no narration. Unlocks future builds. Only after everything above is complete.

### 2.4 Commit

Run the commit core in done.md. No source file edits are staged because the audit produced none — the staged paths are the QUEUE.md capture additions, the LOG/ changes, and the _build.md deletion.

## Phase 3: Recommend next [BRIEF, PROMPT]

Plain-language guard: narrate the captures situation in everyday words — never the background term "processed / unprocessed captures" (see plugin-behaviour.md Vocabulary). Keep the plain statement accurate: don't say the queue is clear when captures are still waiting to be sorted. The scan instruction's "unprocessed Captures" wording below stays as-is — this guard governs only what's said to the user.

Findings routed this session sit unprocessed in Captures — the default recommendation after an audit is /plan, to process them into batches. Name the count.

If nothing was routed, scan unprocessed Captures for overlap with the top batch — items that contradict, invalidate, or would benefit the batch if incorporated first (mirrors the capture-overlap scan in next.md's pre-flight blocker gate). State the scan's result either way, not only when it blocks: Captures empty — say nothing's waiting for /plan; Captures waiting but none overlap the next batch — name what's waiting and give the plain verdict that nothing blocks it; overlap found — recommend /plan first and name the overlap. The clean case is a plain assessment, not a hedge — "Three captures are waiting; none touches the next batch, so nothing blocks it," never "there may be overlap worth checking." Then, if nothing blocks, recommend by queue state:
1. Parked items unblocked by this session (per plugin-behaviour.md Dependency ownership Unpark watch) → recommend /plan, name the unpark candidate(s).
2. More batches → name the next batch, then ask whether the user is continuing into another /next now. If yes and a reorder is applicable (per plugin-behaviour.md Dependency ownership), offer to reorder the queue first.
3. Batches empty → "Queue is clear. Run /plan when you have more."
