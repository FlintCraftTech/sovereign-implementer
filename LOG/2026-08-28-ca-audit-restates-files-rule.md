# 2e9cb18 — Audit finding kept: next-audit's restated Files rule consolidates to a one-clause pointer

The eviction-debt case: the child restates the parent's empty-Files-list rule at a moment the list is already locked, so the restatement instructs nobody and the two copies can drift. Kept as the item suggested, caveat included: the parent keeps the rule, the child keeps one pointer clause naming the parent's self-scoping step by name (never step number), so a mid-run reader still knows why the list is empty. Rule gate: run — an eviction repealing a restatement, one pointer clause added.

**Queue changes:** [ca-audit-restates-files-rule] into Processed, cleared to run.
**Work processed:** kept — [ca-audit-restates-files-rule].
