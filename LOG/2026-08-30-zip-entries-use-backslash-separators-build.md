# 778d6a3 — Rezip ritual's zip step moves from Compress-Archive to Python zipfile

The item was filed against an observation made during the 1.21.1-test2 rezip: archive zip entries reading `throughliner\skills\`, with the committed release zip said to have the identical shape. The zip format specifies forward slashes; Windows tools tolerate backslashes, which is why nobody here had seen a problem while building, installing and testing on one Windows machine. A macOS or Linux tester unzipping the release would plausibly get flat files literally named `throughliner\skills\next.md`.

The fix chosen at processing, on Claude's recommendation and the user's agreement, was to rebuild the ritual's zip step in Python's `zipfile` — conformant paths, no PowerShell dependency, and already what everything else here runs on. Post-processing the entries was the alternative and lost as the more fragile half-measure.

Merged in at that processing: the bytecode-sweep ordering. The ritual's `__pycache__` sweep runs before the test suites, and those suites import the hooks and regenerate exactly the folders the sweep deleted, so the zip caught them. Excluding at the moment of writing cannot be outrun by a later step, which is why the exclusion lives in the zip call rather than in a re-ordered sweep. Step 2's sweep survives as belt-and-braces for the install, with the trap stated in the doc so nobody re-orders around it again.

The release's repackage check was extended in the same pass: it now counts backslash entries as well as bytecode, and says to rebuild rather than ship a zip that fails.

**Observable met, on a scratchpad build rather than by trusting the code:** 40 entries, 0 backslashes, 0 `__pycache__`, every path starting `throughliner/`.

**And the finding's own premise did not survive the day.** Driving the nerds-channel entry later in the same session, that new check was run against all three zips on disk — both archived rezips and the committed `plugin/throughliner.zip`, which has not been rebuilt since `743aa63` and so is the artifact the finding cited. All three are conformant: zero backslash entries, zero bytecode. The build is kept on its own merits and is not called a mistake, but the record it was made from is now in question. Filed as [zip-backslash-finding-does-not-reproduce], which carries the one-minute experiment that would settle it.

**Depth:** full — alternative seriously weighed.
**Files touched:** `resources/release-ritual.md`.
**Routed to Captures:** [zip-backslash-finding-does-not-reproduce].

**Correction, 2026-08-31 — the one-minute experiment was run, and it buries the finding.** In the planning session processing [zip-backslash-finding-does-not-reproduce], `Compress-Archive` on this machine's PowerShell 5.1 (5.1.22621.6133) built a fresh two-entry zip in the scratchpad, and `zipfile.namelist()` — the same reader the finding used — returned `pkg/a.txt`, `pkg/sub/b.txt`: forward slashes, zero backslash entries. The named cause cannot produce the claimed defect on this machine, so the original observation was wrong; the display-artifact hypothesis stands as the likeliest account and the stored-bytes claim is withdrawn from the record. No non-conformant zip is known to have ever existed or shipped. The build this entry records is unaffected and stands on its own merits, as stated above. The capture was deleted with the correction written.
