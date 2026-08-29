# 819f7f1 — The queue digest answers "what is next" without printing everything

Re-deriving the ladder's rung and its top item by hand cost about 350 tokens a pick, most of it Claude emitting the script rather than running it; re-running the whole digest instead — the route the procedure sanctioned — produces around 3,600. The sanctioned route was the expensive one, and the cost recurs at every pick because the queue changes underneath the answer.

The scoped mode prints the rung the ladder fell to, that rung's top item, where it starts in the file, and its text. Measured on this project's own queue at the moment it shipped: 1,652 characters against 16,959, roughly a tenth. Building it required computing the incoming-citation count per entry, which is rung 2's ordering principle and which nothing computed before — so the claim that every rung reads a computed field is now true rather than aspirational.

Two flags went beyond the item's wording and are recorded rather than buried. Rung 1 and rung 4 both depend on session state the script cannot see: which entries were set aside this session, and how many picks have been made, since rung 4 alternates on that parity. Without `--skip` and `--picked` the mode answers the wrong pick the moment anything is skipped, which is the exact case it was built for.

The item's refusals stand. Not an MCP tool — the measured saving comes from scoping the answer rather than from the transport, and this run's own audit puts numbers behind that. And rung 2 is not dropped as too heavy: it was heavy only because nothing computed it.

Tick: done, confirmed — the suite passes with a case proving the rung reported changes when the queue changes beneath it.

Depth: full — alternative seriously weighed, per the two flags above.

Rule gate: run — admitted as an amendment. Parent named: `plan.md`'s existing instruction to re-run the digest whenever the picture needs to be current. The scoped mode replaces the full re-print at that site rather than sitting beside it, so the old sentence was evicted in the same edit.

**Files touched:** `plugin/throughliner/scripts/queue_digest.py`, `plugin/throughliner/docs/plan.md`, `resources/testing/test_queue_digest.py`.

**Routed to Captures:** none.
