# 7b751b6 — plan — the issue check gains a third limb, and its first run found a live dependency on work cleared the same morning

A consumer reported that the planning opening's issue check sees only issues the register records and new ones on a repository the project owns — so issues elsewhere, including on the tool the method runs inside, are invisible to every project.

**The query was run at processing rather than reasoned about, and that decided it.** `gh search issues --involves @me --state open` returned twenty open issues. Among them, `anthropics/claude-code#83476` asks for `.md` files to be editable in the desktop file viewer — which is the premise of [co-authoring-txt-draft-loop], cleared to run hours earlier. `.txt` was chosen *because* `.md` opens read-only. Nothing in this project knew the issue existed. Two more bear on [rendering-for-a-reader-away-from-the-files].

**Half the mail's limit is accepted and half is answered.** Deriving *relevance* is a judgement and stays one. But the set does not need deriving — it needs narrowing, and the anchor the existing limbs already use does it: issues that moved since the last planning record turn twenty into a few worth reading. **No per-project declaration of outside repositories is built**, and the check does not pretend to filter by relevance mechanically.

**Rule gate: run — an amendment**, a third limb on a step that already has two and an anchor.

**The bound is written in and must be stated where this reports:** it reaches issues the account is *involved in*. One nobody here has touched stays invisible — a real widening, not full coverage.

The dependency was written onto the co-authoring item the same turn, marked do-not-wait.

**Queue changes:** [issue-check-foreign-repos] kept and cleared; SPEC's correspondence-scan sentence extended at the close's spec-sync gate.
**Work processed:** kept — [issue-check-foreign-repos].
