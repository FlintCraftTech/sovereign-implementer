# [HASH] — setup.md's Step 3 heading stops promising two settings the step no longer asks about

The heading read "Step 3: Interview (adaptive discovery + two settings)" while the step's own body states there is no settings question anywhere — the last one was dropped in favour of ignoring `INBOX/` on both paths.

**A heading is what a session jumping into a step reads first**, so the stale half steered the read before the correcting sentence was reached. That is the whole reason a heading is worth a build of its own rather than being left as cosmetic drift: it is not describing the step to a reader who will go on to check, it is orienting a session that is about to act.

The heading becomes "Step 3: Interview (adaptive discovery)". A grep across the docs for the two-settings phrasing confirmed nothing else promises it, which was the expected result — cross-doc references go by name here rather than by step number, so no other doc had a reason to carry it.

Noticed during the 2026-08-27 build run and deliberately left out of the tagging build that found it, since a heading rewrite is not tagging.

**Files:** `plugin/throughliner/docs/setup.md`.

Rule gate: not needed — a stale-heading correction; no rule is authored, amended or repealed.
