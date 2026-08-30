# 077b8b9 — plan — the shared mail-triage step gains its stop-and-wait arm

The shared close's mail step ends in something leaving the machine and carried only quiet-and-brief tags; its build-close sibling carries stop-and-wait. The missing arm is added with the condition outside the brackets: silent when the mailbox is empty, brief when triaged with nothing to send, stop-and-wait where a reply is drafted. The prose requirement stays; the tag now encodes the stop, which is the mechanism's whole point.

Rule gate: run — a tag correction on an existing step; no slot spent.

**Queue changes:** [done-mail-triage-missing-prompt-arm] kept and cleared.
**Work processed:** kept — [done-mail-triage-missing-prompt-arm].
