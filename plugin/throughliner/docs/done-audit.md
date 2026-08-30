---
name: done-audit
docset: current
note: >
  Close-out for audit-flavor work items. Reached from done.md's router for the
  run's [audit] items.
---

# Audit close-out

Audits edit no source files — **the session's product is the captures it appended
to Unprocessed.**

```
a run may contain SEVERAL audit items:
    per audit item  ->  one LOG entry each
    once per close  ->  the staleness sweep, the commit, the recommendation
```

## Phase 1: Judgment (while context is fresh)

### 1.1 Verify completion  [SILENT] when every finding is ticked; [PROMPT] when any is not

Read the build working file. Is every finding ticked — captured or dropped?

```
yes             ->  proceed
some unticked   ->  [PROMPT] ask: finish the rest (/next), or close partial?
                    Wait for the user's call.
```

Close partial by deleting the build working file and leaving the queue alone —
an unticked item is still sitting in Processed exactly where it was. Before
deleting it, confirm the two halves agree: every ticked item is gone from
QUEUE.md, every unticked one still there; fix a mismatch rather than proceeding.
An audit close carries **no** memory-reconcile delta — a finding is ticked when
captured or dropped.

### 1.2 Route stragglers to Unprocessed  [PROMPT]

Each straggler is written to Unprocessed first, then reported — the whole set as
one numbered report.

The findings themselves were appended during the audit; this
sweeps anything *else* flagged along the way — observations outside the audit's
criteria, process issues.

```
the RECORD this step sweeps:
    the build working file's notes — an audit run has one like any other run,
    its findings ticked there
    any captures already appended at the moment of noticing
conversation memory  ->  a same-session BONUS pass, never a source the step
                         depends on
```

Append each to Unprocessed, placed per the Captures placement rule (narrate the
placement).

## Phase 2: Record

### 2.1 Write LOG entry  [DISCUSS, PROMPT]

Write **one LOG entry file per audit item**, each named after that item's slug.
Follow done.md's **LOG entry files** section, using its **Audit** body fields:

```
Files touched       the target artifacts READ — the audit edited nothing
Routed to Captures  findings captured, or "none"
Findings routing    how many were filed as captures, and any dropped on
                    Claude's own re-reading before filing, with the reason
```

**An audit item that itself carries a `Red flag · State:` marker:** its flag was
cleared at an earlier /plan run, so carry the cleared flag into its entry; a
marker still reading uncleared is the impossible case — stop and surface it
rather than committing.

**An audit doesn't clear red flags** — clearing happens at processing. A security,
privacy or breach risk this audit surfaces is filed as an ordinary **uncleared**
capture in Unprocessed (`Red flag · State: uncleared`), which a later /plan clears.
Note in this entry that the audit surfaced it.

### 2.2 Staleness sweep  [SILENT] when clean; [BRIEF] when flagging

Run done.md's **Staleness sweep**.

### 2.3 Delete the build working file  [SILENT]

Routine bookkeeping — delete the file, no narration. Unlocks future builds. **Only
after everything above is complete.**

### 2.4 Commit  [BRIEF, PROMPT]

Run the commit core in done.md. No source-file edits are staged because the audit
produced none — the staged paths are the QUEUE.md capture additions, the LOG/
changes, and the build working file's deletion.

## Phase 3: Recommend next  [BRIEF, PROMPT]

Run done.md's **Recommend next** and apply its **Audit close** delta: findings
appended this session sit unprocessed, so the default recommendation is /plan, to
sort them into work — name the count. Only when nothing was appended does the
shared overlap scan run and the ladder apply.
