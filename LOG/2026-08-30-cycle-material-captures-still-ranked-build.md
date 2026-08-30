# [HASH] — A `Cycle:` field bows a capture out of the planning ladder

Filed at the authoring of the tips-posting cycle, which was created to stop eighteen near-identical tip candidates being met one at a time. Those eighteen became material a cycle's turns draw from, and the definition said so — but nothing told the planning ladder, which would rank them as ordinary captures and present them one by one again. The exact tedium the cycle was created to end, in the user's own words: the interaction was long and probably too tedious.

Neither existing field fitted, checked rather than assumed. On a capture, `Blocked by:` bows it out while a named *entry* is open, and a cycle is not a queue entry — its capture exists only while a turn is due, so the hold would lapse between turns. `Not before:` needs a date per capture and the user's approval for each, which is eighteen approvals to avoid eighteen presentations.

So the capture carries a field: one line, `Cycle: [slug]`, same family as `Blocked by:`. The prose-matching version stays refused.

Wired at every site that reads it — `plan.md` gains a third pass-over arm beside the dated and blocked ones, the digest parses and prints the field so the arm reads a computed fact like its siblings, and the lint's mid-line guard covers it. **A capture naming a cycle that does not exist ranks normally**, so deleting a cycle releases its material by itself, which is the same self-lifting logic the sibling arms use.

The claiming of the existing tip captures was planning work and was done in the planning session itself, so this build shipped the readers and found seventeen captures already carrying the field.

**Observable met:** the digest prints `Cycle:` on all seventeen claimed captures, and the widened lint cases pass. No epoch bump — the field is optional and a project without it is structurally fine.

**Depth:** full — alternative seriously weighed.
**Files touched:** `plugin/throughliner/docs/plan.md`, `plugin/throughliner/scripts/queue_digest.py`, `plugin/throughliner/hooks/post_tool_use.py`, `CYCLES.md`, `resources/testing/test_queue_lint_flags.py`.
**Routed to Captures:** [cycle-field-missing-from-line-format] — the field is now read by three tools and shown by no shipped line-format block, which is the write-path-with-no-read-path failure running in the other direction.
