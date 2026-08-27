# beac9d2 — rescan.md stops writing a capture for an item the user chose to process now

Two shipped docs disagreed and a live session followed the wrong one. `rescan.md`'s Step 2 said unconditionally that after the user answers the numbered set "the writes then land", while `plan.md`'s process-now rule says an item taken now is never written as a capture — it is written once, as a work item, after the interview. A /rescan set was answered "process now" and the captures were written first anyway.

The user's words when she caught it: *"Claude is not supposed to write until it has checked the user wants to process now or not."*

**The planning rule is the load-bearing side, so rescan.md is what changes.** Filing first spends a write that is immediately thrown away, and process-now is the common answer by the user's own recorded estimate. Step 2 now states two arms: answered *file* → the capture is written exactly as before; answered *process now* → **nothing** is written, the item enters the planning loop and is written once as a work item. `plan.md`'s rule is cited by name rather than restated, so the two cannot drift apart again the way they just did.

**The eviction is the reworded sentence itself.** The old unconditional "the writes then land" is gone rather than qualified — a rule left standing beside its own correction is the eviction debt this project keeps finding in its own corpus.

**The identical sentence in `done.md` was left standing, deliberately.** The close files and never processes, so it has no process-now arm to state and the unconditional form is correct there. Checked rather than assumed: a grep found it, and it was read before being left alone.

**Files:** `plugin/throughliner/docs/rescan.md`.

Rule gate: run — amendment to rescan.md Step 2; the conflicting unconditional sentence is reworded, which is the eviction; plan.md untouched; nothing else added.
