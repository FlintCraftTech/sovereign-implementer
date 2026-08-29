# 819f7f1 — A kept item names the files its observation reaches, not only the files it changes

A /next run derives its file list from what an item says it changes, which in practice means the Changes line. An observation routinely reaches others — the suite that has to pass, the sibling doc an acceptance check greps — and twice in one run those went missing, so the run stopped mid-flight to ask for a scope addition it should never have needed.

The fix goes at the decision step and nowhere else. The enumeration a kept item carries goes from four things to five, with the fifth naming the observation's files among the files that change. A matching clause at /next's self-scoping step stays refused: fixing the input removes the failure rather than catching it downstream, and /next already handles a genuine ripple correctly.

The cost of that refusal was stated when the item was processed and is worth repeating in the record: every item already in the queue was written under the four-item form, so /next will keep meeting this on legacy items until they build out. It decays rather than persisting.

Tick: done, confirmed — the enumeration lists five things, with one paragraph beneath naming the failure it prevents.

Depth: short.

Rule gate: run — admitted as an amendment. Parent named: the four-item enumeration already at the decision step. A fifth unit in an existing list, sharing its grammatical shape, so it costs no freestanding slot.

**Files touched:** `plugin/throughliner/docs/plan.md`.

**Routed to Captures:** none.
