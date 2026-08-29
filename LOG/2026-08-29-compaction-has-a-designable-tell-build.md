# 819f7f1 — The look-back stops claiming compaction is undetectable, and warns when the files disagree with the conversation

`rescan.md` said that where a conversation has been summarised the memory of it is gone, "and that is undetectable from the inside". The user's observation falsified it: a run leaves structurally recognisable traces, and a session that can still see them has not had them summarised away. The stronger version, which is what makes it mechanical rather than introspective, cross-checks the conversation against durable artifacts on disk — the build working file lists exactly which items were ticked, and thirty listed against six visible is two counts disagreeing rather than a judgement about memory.

The claim was reworded out in the same edit that added the failure-case statement, since leaving it standing would have put a rule beside its own refutation. Both durable sources are named per chat type, as the item required, so the build invented neither: the working file for a build chat, `git diff HEAD -- QUEUE.md` for a planning one.

**The safety property is the whole of the difficulty and is written out rather than summarised.** Absent artifacts are positive evidence that earlier material dropped out of view. Present artifacts prove only that the recent stretch is intact and say nothing at all about the earliest — which is exactly what the scan reaches for, since summarising takes the oldest material first. So the check admits a warning and never an all-clear: the old sentence over-claimed ignorance, and the naive fix would have over-claimed knowledge.

It reaches `done.md`'s wind-down re-scan too, which looks back over the same conversation with the same blind spot.

Tick: done, confirmed — neither doc claims compaction is undetectable, both carry the failure-case statement, and a grep for "undetectable" across the shipped docs returns nothing.

Depth: full — reasoning contested, per the asymmetry above.

Rule gate: run — admitted as an amendment with an eviction. Parent named: `rescan.md`'s existing limit statement, which this rewords rather than sits beside. It fires only when it has something to say, which is the shape this project's checks already take.

**Files touched:** `plugin/throughliner/docs/rescan.md`, `plugin/throughliner/docs/done.md`.

**Routed to Captures:** none.
