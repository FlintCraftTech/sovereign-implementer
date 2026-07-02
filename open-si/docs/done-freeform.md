# Freeform close-out

Close-out for freeform sessions. Reached from done.md's router when _build.md's Entry carries a Freeform subheading, or when _build.md came from an on-demand `/next freeform` run. Freeform has no entry list to verify and no batch to return to the queue — the record is what changed and what was discussed.

## Phase 1: Judgment (while context is fresh)

### 1.1 Route findings to Captures [PROMPT]

Each routed finding is drafted, shown, and approved before it's written, so this step waits on the user. The record of what was flagged — ideas raised, observations, follow-up work — is _build.md's notes plus any captures already routed at the moment of noticing; sweep those. Conversation memory, when present, is a same-session bonus pass, never a source this step depends on. Route each to Captures, placed per plugin-behaviour.md Captures placement (Claude-directed where applicable, oldest-first as fallback — narrate the placement). Freeform files captures but never processes them; processing waits for /plan.

## Phase 2: Record

### 2.1 Write LOG entry [DISCUSS, PROMPT]

Draft the entry as its own file under `LOG/`, named per done.md LOG entry files. A freeform session has no batch slug, so name it by session type and date — `LOG/freeform-<YYYY-MM-DD>.md` (append `-2`, `-3` if the name is taken). Use this template (placeholder hash — backfilled automatically at the next session start):

```markdown
# [HASH] — [one-line summary]

[Prose rationale — what the session did and why, re-authored as inline prose: what was changed, what was discussed, what was decided. No `Why:` label.]

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

There's no pre-generated candidate for a freeform session — author the index entry fresh against the Index entries rule.

### 2.2 Staleness sweep [SILENT] when clean, [BRIEF] when flagging

Path-split like next.md's pre-flight: stay silent when the sweep finds nothing; surface a flag in one or two sentences when it does. Quick check of QUEUE.md against plugin-behaviour.md Dependency ownership Staleness watch — any staleness from any cause:
- Remaining batches or Captures reference renamed/deleted files?
- Reference behaviour or rules that this session (or any prior shift the queue hasn't caught up to) has moved past?
- Items sitting long enough that surrounding code or rules have drifted away from them?
- If so, flag — and split the flag by the fix path in plugin-behaviour.md Staleness watch: a fate-decision flag (drop / rewrite / keep) defers to /plan; mechanical maintenance — a drifted pointer whose target content is unchanged, or clearing a met dependency note whose blocker has shipped — is narrate-and-do: fix it here and report it in one line, riding this commit, with no approval ask. Run the unpark watch on the same pass — anything parked that's now newly unblocked? Flag for /plan.

### 2.3 Delete _build.md [SILENT]

Routine bookkeeping — delete the file, no narration. Unlocks future builds. Only after everything above is complete.

### 2.4 Commit

Run the commit core in done.md. Freeform sessions may or may not change source files — stage what _build.md's Changes records, plus the method docs and the _build.md deletion.

## Phase 3: Recommend next [BRIEF, PROMPT]

Plain-language guard: narrate the captures situation in everyday words — never the background term "processed / unprocessed captures" (see plugin-behaviour.md Vocabulary). Keep the plain statement accurate: don't say the queue is clear when captures are still waiting to be sorted. The scan instruction's "unprocessed Captures" wording below stays as-is — this guard governs only what's said to the user.

Before recommending, scan unprocessed Captures for overlap with the top batch — items that contradict, invalidate, or would benefit the batch if incorporated first (mirrors the capture-overlap scan in next.md's pre-flight blocker gate). State the scan's result either way, not only when it blocks: Captures empty — say nothing's waiting for /plan; Captures waiting but none overlap the next batch — name what's waiting and give the plain verdict that nothing blocks it; overlap found — recommend /plan first and name the overlap. The clean case is a plain assessment, not a hedge — "Three captures are waiting; none touches the next batch, so nothing blocks it," never "there may be overlap worth checking."

Otherwise, based on queue state:
1. Captures routed this session that need processing → recommend /plan, name them. Freeform often leaves captures behind, so this is the common recommendation.
2. Parked items unblocked by this session's work (per plugin-behaviour.md Dependency ownership Unpark watch) → recommend /plan, name the unpark candidate(s).
3. More batches → name the next batch, then ask whether the user is continuing into another /next now.
4. Batches empty → "Queue is clear. Run /plan when you have more."
