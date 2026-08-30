# [HASH] — `workshop/` becomes a method folder and `resources/` moves inside it, epoch 4→5

Working material stops sitting at the repository root. The user's reason, in her own framing at the decision step: only what is part of Throughliner stays in view, so someone shopping online for a method sees the method rather than the workshop. The method's own documents stay visible because they demonstrate it; everything they merely refer to does not.

The file list was derived from a grep for `resources/` across the package rather than from the design discussion, which is what caught the sites nobody would have listed — the scope-lock's writable path in `pre_tool_use.py`, the digest's citation regex, the retired-terms exemption.

Two decisions were made inside the build that the item did not settle, both recorded because a later reader will meet them. **The digest and the session-start board resolve either location**, new home first, falling back to the old root: a project mid-migration would otherwise lose its research citations and its rule board silently, and both are advisory surfaces where a silent failure is the worse one. **`post_tool_use.py`'s gate-trigger paths were deliberately left unprefixed** — they are matched as substrings, so `resources/self-authoring-rules.md` already matches the `workshop/`-prefixed form, and a comment now records that rather than leaving the next reader to work it out.

`measure_written_shape_length.py` carried a stale self-reference to a path that never existed; corrected to the plugin's own `scripts/` while the grep had it open.

The epoch bump is the mechanism working rather than a cost: every existing project halts at its next session until /setup migrates it, which is how the user's other projects get carried across. `migrate-checklist.md` gained an Epoch 5 section and was retitled, since it is no longer a queue-only checklist — a folder move is the first migration step that converts nothing.

Two options were refused at processing and are recorded so they are not re-proposed: renaming `resources/` to `workshop/` outright, which leaves one folder holding three kinds of thing; and nesting the other way as `resources/workshop/`, which puts a host-shaped folder inside a method-shaped one.

**Observable met**, with a stated exception: a grep for `resources/` across the package returns only `workshop/resources/` paths, apart from the migration section that must name the old path to tell a project what to move, the tolerant citation regex, and the substring comment. All 29 hook suites pass.

**Depth:** full — alternative seriously weighed.
**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md`, `plan.md`, `setup.md`, `migrate-checklist.md`, `next.md`, `done-build.md`, `rescan.md`, `feedback-and-inbox.md`; `plugin/throughliner/hooks/pre_tool_use.py`, `session_start.py`, `post_tool_use.py`, `stop.py`; `plugin/throughliner/scripts/queue_digest.py`, `measure_written_shape_length.py`; `README.md`; `resources/testing/hook_schema_check.py`, `test_plan_quiet_list.py`, `test_queue_digest.py`.
**Routed to Captures:** none from this item.
