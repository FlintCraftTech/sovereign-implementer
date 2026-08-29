# [HASH] — plan — the orphaned artifact is a delivery problem, not an eviction-rule failure, and the report's diagnosis is corrected

A consumer reported that retiring the generated build view left a 15KB `BUILD-VIEW.md` at their project root, that their version top-up reported nothing to do, and that this project's eviction rule had fired for the in-queue half and missed the generated file.

**That diagnosis is wrong, and checking it changed the fix.** The retiring build's own record carries the line: `Retired artifacts: … BUILD-VIEW.md …`. The file is named explicitly. Nothing failed at the recording end.

**What is missing is delivery.** That line lands in a session record in this project, and nothing carries it to the projects holding the orphan. Which disposes of their second candidate route — a new limb on the eviction rule — because the rule already records exactly what is needed, and a second obligation would duplicate it.

**So the fix is a shipped manifest read by `session_start`**, appended at the same moment the `Retired artifacts:` line is already required. It **reports and never deletes**, consistent with the top-up being add-only and never clobbering anything the user wrote — and the report names what produced the file, which answers their real complaint: that the orphan explains itself to nobody.

**Rule gate: run — an amendment adding no detection point**, riding the existing close obligation the way README-sync rides SPEC-sync. Authoring stays host-only; the reading half ships, because the orphan is in consumers' projects.

**An honest limit on verification, unusual here:** this project has no `BUILD-VIEW.md`, so the check cannot be dogfooded and is provable only against a fixture. No epoch bump — nothing about an existing project's own documents becomes wrong.

**Queue changes:** [retired-feature-leaves-orphan] kept and cleared, with the sender's misdiagnosis corrected in its prose; SPEC sentence written.
**Work processed:** kept — [retired-feature-leaves-orphan].
