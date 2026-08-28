# 2e9cb18 — content_stamp() to normalise line endings and exclude .orphaned_at

Finding 3 of the release-chain report, kept as its own build: with `core.autocrlf=true` and no `.gitattributes`, a commit's LF blobs never stamp equal to the CRLF installed build, so the one mechanical build-identity check fails exactly where the archive model (see this date's rezip-archive entry) needs it. In-function normalisation won over a `.gitattributes` because it touches nothing else; every stamp changes once when it ships, said in the item rather than discovered. Hook change — the building session's close runs the suites.

**Queue changes:** [content-stamp-normalises-line-endings] into Processed, cleared to run.
**Work processed:** kept — [content-stamp-normalises-line-endings].
