# [HASH] — A ritual names the paths its steps write, instead of the lock accumulating carve-outs

The same failure had happened twice — a ritual step needing to write somewhere the session running it may not — so it is a class rather than a case. A ritual definition now carries a `Writes:` field, and the planning branch of the scope-lock reads the project's own `CYCLES.md` and permits exactly what it names.

This is not the self-declared marker the record already refused. That objection is against a session granting itself permission; a ritual's declaration lives in a committed file written at a planning session with the user present, exactly as a `[freeform]` session's list comes from a queued item. Who wrote the permission and when is the distinction, and the code comment says so, because a later change that lost it would turn this into the refused thing.

The user's decision, with its cost recorded rather than buried: declared paths are permitted whenever the project is open, not only while the ritual runs. Nothing has to detect which ritual is running, and the manifest carve-out has worked that way unconditionally with nothing going wrong.

One implementation choice went beyond the item's wording. The field is read wherever it appears rather than only on definitions with no cadence, because a cycle whose turn runs a ritual's steps has the identical need and a definition declaring nothing contributes nothing either way. The authoring rule still sites the field on rituals, as the item specified.

Tick: done, confirmed — a declared path is permitted, an undeclared near-miss sibling refused, and a project with no cycles doc behaves exactly as before.

Depth: full — alternative seriously weighed, per the read-wherever-it-appears choice above.

Rule gate: run — admitted as an amendment. Parent named: `plan.md`'s ritual-authoring instruction, which already enumerates what a definition carries; this is a fourth item in that list. Eviction, condition unchanged: it supersedes the `plugin/rezip-archive/` carve-out once the rezip exists as a ritual definition declaring that path — not before, or the rezip loses its only permitted route. Both are in the file today, deliberately.

**Files touched:** `plugin/throughliner/hooks/pre_tool_use.py`, `plugin/throughliner/docs/plan.md`, `resources/testing/test_plan_quiet_list.py`.

**Routed to Captures:** none.
