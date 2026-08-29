# [HASH] — A finding another project owns is copied in, and the work resting on it is flagged as a snapshot

A consumer project reported that the method files and indexes research per project and has no shape for a finding one project owns and another's work depends on. Both available answers were poor: an absolute path that breaks silently, or a copy with no link to the original.

One of the two was already barred, which narrowed the design rather than weighing it. The always-loaded scrub checklist bans a file path that identifies a person or an organisation from a committed document — the same reason the address book lives inside the gitignored mailbox — so citing by absolute path was never merely fragile. That makes the reporter's own workaround the answer, with one change: the copy carries a `Copied from:` line naming the owning **project**, never a path.

The staleness half is answered by a label rather than a check. The digest flags every item citing such a file as resting on a **snapshot**, which is permanent, honest and impossible to rot — nothing reads the other project's folder, so nothing can say whether the original moved on. That limit is written into the rule, into the code comment and into the digest's own printed output, because a label like this is exactly the kind that gets read as a staleness check by whoever meets it next.

Tick: done, confirmed — a research file carrying the line makes its citing item print the flag naming the owning project; a file without it prints nothing.

Depth: short.

Rule gate: run — admitted as an amendment authoring no prohibition. Parent named: the research-filing block's `Superseded by:` convention, which this sits beside as the cross-project case. The ban on absolute paths is not restated, because the scrub checklist already carries it; what is added is the positive action.

**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md`, `plugin/throughliner/scripts/queue_digest.py`, `resources/testing/test_queue_digest.py`.

**Routed to Captures:** none. A reply is owed to the sending project, whose mail asked whether this shape was worth designing at all; nothing has been drafted and the send needs the user's explicit yes.
