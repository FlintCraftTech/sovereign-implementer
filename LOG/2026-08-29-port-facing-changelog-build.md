# [HASH] — A port can survey what changed in the shipped package since the version it ported from

The question behind this was whether a port's own sessions can read this repository's changelogs and apply what changed. They can, conditional on what the changelog carries: a human release note names no file, no rule and no wording, while this project's session records already carry exactly the right shape. Only a port-facing view of them per release was missing.

The generator walks the commits in a release range that touch `plugin/throughliner/`, matches each to the session records stamped with its hash, and prints one entry per shipped change with that record's behavioural summary, its shipped files, and a pointer to the record. Epoch bumps are read from the diff rather than from the file, so the entry says what the commit did rather than what the value happens to be now. Records that discuss host-only reasoning are marked, which is the part a porter most needs: a large share of this project's work is explicitly not meant to leave, and following the records blind would carry it across.

Two matching questions had to be settled against the corpus rather than designed, and both are worth keeping. An entry's shipped-ness is decided from git's own file list, because records name a doc by the name a reader would use rather than by its repository path — a first pass that tested the prose against a path prefix classified every entry as host-only. And a commit whose only shipped change is the manifest's version key is skipped, mirroring the content stamp's documented reason for dropping that key, so a rezip stamp does not produce an entry reading "read the diff".

Tick: done, confirmed — the suite passes all nine cases, and a live run over `v1.21.0..v1.21.1` printed 39 entries with no unmatched commit.

Depth: full — alternative seriously weighed, per the two matching decisions above.

Rule gate: run — admitted as an amendment. Parent named: the release ritual's step list, which gains one step, written as a bullet inside the publish step where the attach happens. The generator is a script rather than a rule and adds nothing to the always-loaded set.

**Files touched:** `plugin/throughliner/scripts/port_changelog.py` (created), `resources/release-ritual.md`, `resources/testing/test_port_changelog.py` (created).

**Routed to Captures:** none.
