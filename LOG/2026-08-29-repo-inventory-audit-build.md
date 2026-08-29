# [HASH] — Every root and `resources/` entry now has a line saying what it is and what reads it

The item came from the user saying she has no idea what half the files in the repository are for. An inventory that explains each one is the answer to that; deciding their fates is separate work, and this pass deleted nothing and proposed no fate.

The mechanical test the item derived was applied rather than a general tidy-up: among the 329 files the 2026-08-09 emergency revert restored, look for those that duplicate something elsewhere or that nothing references. **Restored is not the same as debris** — `plugin-behaviour-retired.md` and the revert's own plan came back correctly and are live history, which is stated in the inventory so a later pass does not re-find them as clutter.

Four entries needed their own fate and were filed separately: a tracked JavaScript file nothing references in a Python project, a pytest cache at the root from a tool this project's own constraints ban, and two brand images plus a model brief that no reference reaches. The images are the case where a grep is the wrong instrument, and the finding says so rather than implying they are dead — an icon's real use is outward, where nothing in this repository can see it.

**The form departs from the item's observable and the departure is stated in the artifact rather than made quietly.** One finding per entry would have been about thirty-five captures, each ranked independently by the ladder; the inventory's value is in being read whole, so every entry has its line inside one capture, and the top of that capture invites the user to ask for them split.

Tick: captured — four findings.

Depth: full — reasoning contested, per the form departure above.

**Files touched:** none. The audit read the repository and edited nothing.

**Routed to Captures:** [repo-inventory-table], [reader-test-workflow-unreferenced], [pytest-cache-at-the-root], [unreferenced-brand-files-and-brief].
