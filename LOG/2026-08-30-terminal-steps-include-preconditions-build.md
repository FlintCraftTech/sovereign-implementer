# 778d6a3 — Terminal steps in a walkthrough supply the commands that come before the run

Captured by the user on 2026-08-30 from a live walkthrough in another of her projects, with a screenshot as the evidence. The step said a separate terminal was needed "sitting in the project folder" and then gave only the command to run. Pasted as instructed, it would have run from `C:\` and failed, because nothing ever supplied the `cd` that gets the terminal there.

Her words: she is tired of having to explain, in user terminal walkthroughs, that Claude needs to show what to run first — and the users of this method are assumed to need the steps that come before the run.

The defect's shape is what makes it worth a rule rather than a correction: the precondition was stated as a *description* ("sitting in the folder") rather than as a step the user performs, so it read as already done. A non-coder does not translate "sitting in the folder" into a `cd` command; the walkthrough owns that translation.

One subordinate bullet on the walkthrough requirements, whose parent is the each-step-names-the-thing-to-click-or-type rule — so it costs no slot. A fresh terminal opens somewhere the user did not choose, which is why location is never assumed rather than usually stated.

Corrected in passing while the list was open: its opening read "Two further requirements" while governing four. Replaced with an uncounted opening, since the count had already gone stale once.

Ships — every consumer's walkthroughs carry the same exposure. No SPEC sentence owed, checked: SPEC describes walkthroughs at the names-the-thing level and stays true; this is authoring detail one level below it.

**Observable met:** a grep finds the terminal-precondition bullet once, in the walkthrough requirements list.

**Depth:** short.
**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md`.
**Routed to Captures:** none from this item.
