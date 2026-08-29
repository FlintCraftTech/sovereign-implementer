# 7b751b6 — plan — /rescan's undetectability claim is reworded out, and the asymmetry is written in as untouchable

`/rescan` claims compaction is undetectable from the inside, and its whole design — a stopping point held in the conversation, no durable marker — rests on that. The user's observation: a `/next` run leaves recognisable traces, and their absence is a tell.

**The item had already sharpened it into something mechanical**, and the sharpening is what makes it safe: cross-check the conversation against durable artifacts on disk, and state the asymmetry — absent artifacts are positive evidence something dropped; **present** artifacts prove only that the recent window is intact and nothing about the earliest stretch, which is exactly what the scan reaches for.

**Two things were added at processing to make it buildable.**

The two durable sources are named, one per chat type, so a build does not invent them: a build chat has its working file, which lists exactly which items were ticked — thirty listed against six visible is two counts disagreeing, not a judgement about memory — and a planning chat has `git diff HEAD -- QUEUE.md`, already how the close recovers what it did.

And the eviction is named. This cannot be a pure addition: the sentence claiming undetectability is the thing being falsified, so it is reworded out in the same edit rather than left standing beside its own refutation.

**It reaches `done.md` too**, which the item had left open — the wind-down re-scan looks back over the same conversation with the same blind spot.

**Written in as what the build must not soften:** the check admits a warning and never an all-clear. The current sentence over-claims ignorance; the naive fix would over-claim knowledge.

**Queue changes:** [compaction-has-a-designable-tell] kept and cleared; SPEC sentence written.
**Work processed:** kept — [compaction-has-a-designable-tell].
