# [HASH] — Retired artifacts are named in a shipped list, so an orphan explains itself

A consumer project ran a migration that generated `BUILD-VIEW.md` at its root, the generated view was retired four days later, and their version top-up then reported nothing to do with the 15KB orphan still sitting there. A retirement removes the code that writes an artifact; it never removes the artifact from projects that already ran it.

The sender's diagnosis is corrected here so it is not inherited. The eviction rule did not fail — the retiring build's own record names every retired artifact explicitly. What is missing is delivery: that line lands in a session record in this project, and nothing carried it to the projects holding the orphan. So a second obligation on the eviction rule would have duplicated a line that already exists. What ships instead is the list, read at every session opening.

It reports and never deletes. Removing a file from someone's project is precisely what the add-only posture exists to prevent, and whether to keep it stays theirs; the suite pins that the file is still present after the check has run.

One honest limit, unusual enough to state twice: this project has no `BUILD-VIEW.md` — its own was never generated — so the check cannot be dogfooded here and is provable only against a fixture. The suite's docstring says so.

Tick: done, confirmed — eight cases pass, including that the doc's own fenced format example is not read as an entry, which a first pass got wrong and the suite caught.

Depth: short.

Rule gate: run — admitted as an amendment adding no detection point. Parent named: the `Retired artifacts:` close obligation in `CLAUDE.md`, which already fires at the right moment; the list append rides that same trigger, the way README-sync rides the SPEC-sync trigger. The authoring half stays host-only; the reading half ships, because the orphan sits in consumers' projects.

**Files touched:** `plugin/throughliner/retired-artifacts.md` (created), `plugin/throughliner/hooks/session_start.py`, `CLAUDE.md`, `resources/testing/test_session_start_retired_artifacts.py` (created).

**Routed to Captures:** none.
