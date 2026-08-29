# [HASH] — plan — `resources/captures/` is revert debris, and deleting it is the one repo fix that needed no investigation

The user asked what the captures folder was, on the way to a wider repo cleanup. The answer settled its fate.

**It is not captures. It holds attachments *to* captures** — created 2026-06-14 for a session transcript too large to embed in a queue entry, so the transcript went to a file and the capture linked out. Her reading, "captures go in the queue", is correct and is exactly the confusion the name causes.

**And it was already retired.** On 2026-08-02 its contents were moved into `resources/testing/`, where re-read-later evidence belongs. The 2026-08-09 emergency revert restored the whole tree to its 2026-08-02 state and resurrected the folder; all four files carry that revert's timestamp.

**Verified rather than assumed:** three of its four files are byte-identical to copies in `resources/testing/` — checksums compared — and the fourth, `532ea359-spec-write-slim.txt`, exists nowhere else, so a blind folder delete would lose it. Its only reference anywhere is one line in `rule_signals.py`'s exclusion list, beside `resources/testing/`, which already covers the survivors.

**The 4.7MB root icon was pulled out of the "proven" pile deliberately.** Deleting it reclaims nothing that matters — the blob stays in git history, and this project refuses history rewrites because its records are full of commit hashes. It is a presentation question and rides [repo-cleanup-product-forward].

Rule gate: not needed — deleting the folder makes the repository match the existing `resources/` rule rather than changing it.

**Queue changes:** [repo-debris-proven-fixes] filed and cleared.
**Work processed:** kept — [repo-debris-proven-fixes].
