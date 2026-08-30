# [HASH] — Build close drops the walk-through outcome definitions it restated after citing them

From the compliance audit of 2026-08-29, lens 1 on the parent axis. Common reasoning for this run's five compliance fixes is in `2026-08-30-done-audit-records-a-repealed-approval-step-build.md`.

The pattern is cite-and-restate, which is the harder half of eviction debt to see: the child does the right thing by naming where the definitions live, and then carries them anyway, so the duplication reads as a courtesy. `done-build.md`'s step 2.1 named the three outcomes, pointed at `done.md`'s block and `next.md`'s walk-through branch for the definitions, and then restated that `deferred` requires the user's own word and that an unpresented item is `not reached`.

Both fire in a build close, minutes apart — which is exactly the parent-axis case, where the child is loaded *with* the parent and the reader has both. The citation is what makes it cheap to fix: the sentence already named its source, so the restatement goes and the pointer stays. The parenthesis is the whole of what the child needs.

**The exclusion the build had to honour, and did:** `next.md` carrying the same block is *not* a finding. `next.md` and `done.md` are siblings, not parent and child, and no single session reads the walk-through branch and the close's routing step for the same purpose. That is the sibling-axis trap the checklist records a worked instance of, and it was deliberately not swept up.

**Observable met:** a grep for the restated deferred-and-not-reached clauses in that step returns nothing, while the parent's block is untouched. The merge came out shorter.

**Depth:** short.
**Files touched:** `plugin/throughliner/docs/done-build.md`.
**Routed to Captures:** none from this item.
