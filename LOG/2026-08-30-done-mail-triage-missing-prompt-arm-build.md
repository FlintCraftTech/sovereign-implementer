# [HASH] — Shared mail-triage step gains the stop-and-wait arm its own child carried

From the compliance audit of 2026-08-29, lens 2. The reasoning common to this run's five compliance fixes is carried in `2026-08-30-done-audit-records-a-repealed-approval-step-build.md`; this entry adds only what is particular to this one.

Two steps did the same thing with different tags. `done.md`'s mail triage read `[SILENT]` when the mailbox is empty and `[BRIEF]` when it isn't, and then required a reply drafted and the exact wording shown before anything is sent. `done-build.md`'s equivalent read `[SILENT]` when no mail arrived and `[PROMPT]` when it did. A build close reaches both, and the two gave different instructions about the same moment: one says be brief, the other says stop and wait.

The missing arm matters because the step it governs ends in something leaving the machine, which is this method's hardest gate. `[BRIEF]` says how much to say; it does not say to stop — and the tag is the mechanism the method uses precisely so that stopping is not left to the surrounding prose. A close that reads only `done.md` — a planning close, an audit close, a completed `[user]` item — had no tag telling it to wait at all. The prose did carry it, which is lens 2's own third failure mode: a step describing its output behaviour in a sentence instead of carrying the tag that encodes it.

The step now reads `[SILENT]` when the mailbox is empty, `[BRIEF]` when mail is triaged with nothing to send, and `[PROMPT]` where a reply is drafted, with the conditions outside the brackets as the tag rules require. The prose requirement stays; the tag now encodes the stop.

**Observable met:** the step's tag line carries all three arms.

**Depth:** short.
**Files touched:** `plugin/throughliner/docs/done.md` — shared with [done-md-states-the-scrub-rule-twice] and built adjacently, each reading the file as it found it.
**Routed to Captures:** none from this item.
