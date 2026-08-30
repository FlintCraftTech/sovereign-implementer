# [HASH] — Audit close's `Approval outcomes` field becomes `Findings routing`

From the compliance audit of 2026-08-29. This entry carries the reasoning for the five findings that audit produced and that this run built; the sibling entries cite it rather than restating it.

**The contradiction, in two shipped docs a single audit close reads together.** `next-audit.md` says plainly that nothing waits for approval when findings are filed — asking the user to accept a set before filing them makes her assess the same material twice. `done-audit.md`'s step 2.1 then required a body field recording "what happened at bulk approval — findings dropped or reworded, each with the user's reason; or 'all findings approved as-is'".

There is no bulk approval in an audit run any more, so the honest value of that field was always "all findings approved as-is" — which asserts an approval that never happened. **A required field whose only truthful value is a fiction is worse than no field.** The retirement left the artifact: the step went, and the body field the step produced stayed, which is the eviction rule's own failure mode.

The choice the audit left open was settled at processing as replace rather than delete. The field becomes **Findings routing** — how many findings were filed as captures, and any dropped on Claude's own re-reading before filing, with the reason. That records what the run actually did, fabricates no approval, and keeps the one trail deletion would lose, since `next-audit.md`'s dropped route still exists.

The ripple was traced by grep at processing rather than assumed: the wording lives in `done-audit.md` alone, and the one other "bulk approval" hit is the general inversions block, which governs bulk approval elsewhere and is correct — excluded, not changed. No announced claim is touched.

It was exercised the same session: this run's own audit close wrote the new field, reporting five filed and none dropped.

**Observable met:** a grep for "Approval outcomes" over the shipped docs returns nothing, and the Findings routing field sits in its place.

**Depth:** full — alternative seriously weighed.
**Files touched:** `plugin/throughliner/docs/done-audit.md`.
**Routed to Captures:** none from this item.
