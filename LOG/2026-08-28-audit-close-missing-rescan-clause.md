# 2e9cb18 — The audit close gains the rescan-first clause — the fourth and last close-naming site

The build that fixed the other three sites correctly refused to expand its own scope; this session extended the already-decided rule to the site it deliberately left. `next-build.md`'s abort path stays excluded, as the capture already settled — a failed-item exit is a different moment.

Rule gate: run — extension of [rescan-before-done]'s decided rule to its fourth site; nothing evicted.
**Queue changes:** [audit-close-missing-rescan-clause] into Processed, cleared to run.
**Work processed:** kept — [audit-close-missing-rescan-clause].
