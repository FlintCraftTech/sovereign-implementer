# [HASH] — The scope-lock lets the rezip write its own archive

The archive step was denied on its first ever run. A rezip runs after a close, so no build working file exists and the scope-lock classifies the session as planning — and `plugin/rezip-archive/` was not on the planning session's standing list. There was no chat shape in which the step could run at all, which is the same failure the `plugin.json` carve-out already answers one path over.

The permission is a folder where its sibling is one path, and that is said plainly in the code rather than passed off as the same move. It is defensible because the archive is gitignored build output rather than part of the plugin package: permitting it opens nothing under `plugin/throughliner/`, which the suite pins with a still-denied sibling.

This is the narrow half of a sequence the user agreed on 2026-08-29. It took the carve-out now because the weekly release falls due 2026-09-02 with the archive empty; [ritual-declares-writable-paths] is the general fix, built in this same run, and the comment records the condition under which it evicts this.

Tick: done, confirmed — the suite passes with the archive write permitted and a sibling under the plugin package still denied.

Depth: short.

Rule gate: not needed — no method rule is authored. The shipped planning list in `plan.md` is untouched, as the `plugin.json` carve-out left it, because a host-only path stated in shipped text would put a folder in front of consumers who do not have one.

**Files touched:** `plugin/throughliner/hooks/pre_tool_use.py`, `resources/testing/test_plan_quiet_list.py`.

**Routed to Captures:** none. The archive is still empty — this build permits the write, and the next rezip performs it.
