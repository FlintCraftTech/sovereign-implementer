# 7b751b6 — plan — cross-project research is copied in and labelled a snapshot; the absolute-path option was already barred

A consumer project reported that a work item citing research a sibling project owns must either use an absolute path that breaks silently, or a copy with no link to the original — and that the `Superseded by:` safety net stops at the project boundary.

**One of their two options was already barred, which narrowed the design rather than weighing it.** The always-loaded scrub checklist bans file paths that identify a person or an organisation from a committed doc — the same reason the address book lives inside the gitignored mailbox. So citing by absolute path is not merely fragile; where the citing project's queue is tracked, it is already a violation.

**That makes their own workaround the answer, with one change**: copy the finding in, and name **the correspondent** in the provenance line rather than a path. The committed text then names a project, the path stays inside the mailbox where the address book already maps it, and the dead-path problem goes with it.

**The staleness half is answered by a label, not a check.** The digest flags any item resting on a copied finding as resting on a **snapshot** — permanent, honest, impossible to rot, and explicitly not a staleness check.

**Refused: a pull-check** reading the owning project's research index at the citing project's opening. The precedent exists — the subprojects rule already permits one circumscribed cross-project read — but it costs a standing check, works only where both projects sit on one machine, and rests on a gitignored address book. One reported instance did not carry it.

**Rule gate: run — an amendment that authors no prohibition.** The ban on absolute paths already exists in the scrub list; what is added is the positive action.

A reply is owed to the sending project, whose mail asked whether this shape was worth designing at all. Nothing drafted or sent.

**Queue changes:** [cross-project-research-citation] kept and cleared; SPEC sentence written.
**Work processed:** kept — [cross-project-research-citation].
