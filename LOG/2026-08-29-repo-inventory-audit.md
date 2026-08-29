# 7b751b6 — plan — an inventory audit answers "I don't know what half these files are", scoped by the revert rather than by a vague brief

Reasoning in [2026-08-29-repo-debris-proven-fixes](2026-08-29-repo-debris-proven-fixes.md), which took the part that needed no investigation. The user's complaint was that she has no idea what half the files in the repository are for; an inventory that explains each one is the answer, and deciding their fates is separate work.

**Surveyed at processing so the audit does not start cold.** The tree is about 12MB: `LOG/` is 7.4MB across 1,375 tracked files, `resources/` 2.7MB, `plugin/` 1.4MB, with 17 tracked files at the root. `resources/` mixes live tooling with dead history at one level — `discord_post.py` and `rule_signals.py` beside `plugin-behaviour-retired.md`, the emergency-revert plan, a migration recipe and a stray `reader-test-workflow.js`.

**One mechanical test was derived rather than invented.** The 2026-08-09 revert restored the whole tree, so anything retired in the week before it came back; 329 files still carry its timestamp. **Restored is not debris** — most are LOG entries and research findings restored deliberately. What made the captures folder debris is that its contents had been *relocated*, so it returned as a duplicate. The test is therefore: among restored files, those that duplicate something elsewhere, or that nothing references.

**`LOG/` entry files are excluded from the fate question** — 1,375 session records are the archive working as designed. The index's size is reported as a fact without a verdict.

**The honest limit is written in:** an inventory finds what it can trace, a file nothing references may still matter to a person, and this pass proposes no fates.

**Queue changes:** [repo-inventory-audit] filed and cleared, at the end of the region with the other audits.
**Work processed:** kept — [repo-inventory-audit].
