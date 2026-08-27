# d31b553 — rescan/plan contradiction on process-now found live and queued

Found by the user mid-session: /rescan's candidate set was answered "process now" and captures were written first anyway. The cause is a genuine contradiction between two shipped docs — rescan.md's Step 2 says unconditionally "the writes then land", plan.md's process-now rule says an item taken now is never written as a capture. The session followed the wrong one; her words: *"Claude is not supposed to write until it has checked the user wants to process now or not."* The planning rule is load-bearing (filing first spends a thrown-away write, and process-now is the common answer), so the fix amends rescan.md's sentence into two arms, plan.md cited and untouched. Rule gate: run — the conflicting sentence reworded, which is the eviction.

**Queue changes:** [rescan-processnow-no-double-write] written and cleared.
**Work processed:** kept — [rescan-processnow-no-double-write].
