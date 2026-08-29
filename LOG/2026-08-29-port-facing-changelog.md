# [HASH] — plan — a changelog written for ports, because the ship boundary is already a folder

**The user's question decided this item's existence:** can their AI systems simply survey the changelogs on the repo since the version they last ported from, and apply the changes from there?

**The answer is yes, conditional on what the changelog carries.** A human release note is unusable — it names no file, no rule, no wording. What a port's session needs per change is which shipped file changed, what changed inside it in behavioural terms, and why. This project's session records already carry that shape, so only a port-facing view of them per release is missing.

**And it is derivable rather than hand-written, because the ship boundary is a folder.** Everything under `plugin/throughliner/` ships; everything outside is host-only. That distinction is load-bearing here rather than incidental: a large share of this project's work is explicitly host-only — release rituals, the rule gate, the compliance checklist — so **a porter following the LOG blind would try to port things never meant to ship.**

**Three limits the changelog states about itself**, so it cannot be over-read: it says what changed and never how to map it; a hook change may have no equivalent on the other side; and an epoch bump means the port's own users' documents need migrating, which is theirs.

**Rule gate: run — an amendment**; the release ritual's step list gains one step, and the generator is a script rather than a rule.

**It closes a second gap already on record:** [marketplace-submission] states that a changelog does not exist and that version-consistency discipline is the commonest submission rejection cause.

**Queue changes:** [port-facing-changelog] filed and cleared, third of the four port items; SPEC sentence written at the close's gate.
**Work processed:** kept — [port-facing-changelog].
