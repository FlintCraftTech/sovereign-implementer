# [HASH] — Queue lint flags a field marker written anywhere but the start of a line

The instance, from 2026-08-29: an item's red-flag marker sat at the end of a prose sentence, the digest's pattern is anchored to the start of a line, and so the digest never reported the flag. Rung 1 of the ordering ladder — an uncleared red flag outranks everything — fired by luck rather than by machinery, because someone happened to grep more loosely than the tool does.

It was kept as the third instance of one family rather than as one repair. A bolded `Rule gate:` hid a whole session's dispositions from the board twice, and `Blocked by:` carries a written instruction to stay plain for the same reason. Each time a canonical shape existed, an ordinary Markdown instinct produced a variant, and the reader went quiet instead of complaining.

Widened to all three markers at processing, on a check run rather than assumed: every reader of the three field lines — the digest, the session opening, the lint, the queue mover — anchors to the start of a line, so `Blocked by:` and `Not before:` have exactly the red flag's exposure. A vanished hold releases held work early, which is worse than a missed flag.

Refused and carried so it is not re-proposed: widening every reader's pattern. That is the tolerate-at-the-reading-end move, already taken twice in this family, and it leaves the deviation itself invisible. Flagging at the writing end keeps one canonical shape, the same posture this project took on the `#### ` heading.

Two decisions inside the build, both to stop the check crying wolf: emphasis is tolerated, since `**Blocked by:**` is what every reader already accepts; and fenced blocks are skipped entirely, because a fence is where the shapes are legitimately quoted — the section preamble shows the line format, and items show examples.

**Observable met:** three suite cases added and passing — a mid-line marker draws the flag for every field, own-line and emphasised forms do not, and a marker quoted inside a fence does not. No epoch bump: nothing an existing project has becomes structurally wrong, checked against the trigger list.

**Depth:** full — alternative seriously weighed.
**Files touched:** `plugin/throughliner/hooks/post_tool_use.py`, `resources/testing/test_queue_lint_flags.py`.
**Routed to Captures:** none from this item.
