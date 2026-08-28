# [HASH] — Every commit step in the done family now carries [BRIEF, PROMPT]

done-build.md §2.4 and done-plan.md §2 gained the tag matching done.md's Commit core — and the build found a third untagged commit step the audit finding had not noticed, in done-audit.md §2.4. It was included because the item's own observable ("no untagged commit step remains in the done family") cannot be met without it; the file was added to the run's Files list before editing.

Tick: done, confirmed — a grep of every commit heading across the done family shows all four tagged.
Files touched: plugin/throughliner/docs/done-build.md, done-plan.md, done-audit.md.
Rule gate: run — the existing tag system applied to steps that missed it (parents: the response-shape tag rules, done.md's Commit core); nothing evicted.
