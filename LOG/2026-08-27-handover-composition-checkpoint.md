# beac9d2 — Three scattered rules become one named checkpoint at the moment a message hands work over

Three shipped, clearly written rules each failed to fire at the moment they applied, in a single build run: the tool-check, when a Discord message's text was handed to the user to supply by hand twenty minutes after the same session provisioned a bot with Read Message History for exactly that; the jargon rule, broken within the hour by the session that authored it; and the view-in-doc link rule, months shipped and correctly applied elsewhere in the same run, yet a file was named in prose with no link until the user asked. A fourth instance, added at processing, was the shared-vocabulary rule broken in the planning session itself.

**What makes them one finding rather than four.** All four failures happened while composing a message that handed something over. None happened while editing a file. File edits have several checkpoints; hand-over composition had none.

So the pre-send read-back that already existed — one question, about vocabulary — is widened into the checkpoint, carrying three questions in one pass: does any step use a term naming nothing on the user's own screen, is any part of the method called by anything other than its own name, and does each step name the thing to click **and** the thing to look for; is there a tool that could do this instead of the user, read from `TOOLS.md` rather than from memory; and is every file the message points at given as a link.

**The tool-check and view-in-doc rules stay canonical where they are and are cross-referenced, not restated** — which is what makes this an amendment consuming no slot.

**One judgment the item did not anticipate.** The item named two sites, `skill-nonspecific-rules.md` and `next.md`, and told the build to grep first. The grep found the shipped read-back at **one** site, in `next.md`. Rather than inventing a second, the canonical statement went to the always-loaded file — the checkpoint fires in every skill and in conversation with no skill running, which is that file's own admission test — and `next.md`'s site became a pointer. Same two files, no third copy, and the rule now reaches the sessions that need it.

**The honest limit is written into the rule itself:** one named checklist at one named moment makes the three checks more likely to fire than three rules scattered across the corpus. Nothing verifies that the read-back ran. It must not be described as enforcing anything.

**The rule was broken again within the hour, by this same run.** The very next hand-over composed after the checkpoint shipped said "the quoted install line" about a post containing two quote blocks, and the user had to ask which. That is the second recorded instance of this project breaking a hand-over rule immediately after writing it — filed as [handover-named-neither-of-two-quotes], and it is evidence about the limit above rather than against the change.

**Files:** `plugin/throughliner/docs/skill-nonspecific-rules.md`, `plugin/throughliner/docs/next.md`.

Rule gate: run — amendment to the hand-over read-back rule shipped by [general-jargon-translate-and-walkthrough-readback]; parent named, the other two rules cross-referenced rather than restated, nothing evicted.

Routed to Captures: [handover-named-neither-of-two-quotes]
