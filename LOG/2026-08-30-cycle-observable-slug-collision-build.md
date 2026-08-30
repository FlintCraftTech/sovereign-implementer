# [HASH] — A LOG-based cycle observable must be distinguishable from planning's own records

Found live on 2026-08-30, in the first session to compute the defective observable. The announced-claims sweep's observable was "the most recent LOG entry under this cycle's slug" — and the planning session that *authored* the cycle wrote a record under that slug, as the shipped procedure has it do for every item processed. The due-ness check read the authoring record as a completed turn, and that session's opening reported the claims sweep as having run today. It had never run once.

The defect is the method's rather than this project's configuration. Two shipped mechanisms share a namespace: /plan writes per-item records named by slug, and /plan's cycle-authoring step lets a definition's observable be a LOG entry under that same slug. Any consumer who picks a LOG-based observable inherits the collision, and it fires at the worst possible moment — the first check after authoring, when the cycle has by definition never run.

`plan.md`'s cycle-authoring step now carries the requirement, with the cheap form named rather than merely demanded: each turn's record opens by saying it records a completed turn, and the observable reads only those records.

The same build brought this project's one live LOG-based definition into compliance, as the first application of the amended rule rather than as a separate hand-fix. **That was the user's decision on 2026-08-30 and it is the part worth carrying:** no local hotfix ahead of the method — this project tests the method and waits for the fix to arrive the way a consumer would.

**Observable met:** `plan.md` carries the distinguishability requirement, `CYCLES.md`'s sweep observable names the turn-record form, and a grep for the old wording returns nothing.

**Depth:** full — reasoning contested.
**Files touched:** `plugin/throughliner/docs/plan.md`, `CYCLES.md`.
**Routed to Captures:** none from this item.
