# [HASH] — content_stamp() normalises CRLF to LF and excludes .orphaned_at, so a commit and its installed build can stamp equal

With `core.autocrlf=true` and no `.gitattributes`, a commit's LF blobs could never stamp equal to the CRLF installed build, defeating the one mechanical answer to "is this build the build I think it is" — including the new release ritual's archive check, which compares against `git archive` output. The fix is in-function: bytes normalised before hashing, `.orphaned_at` joining the exclusions. A `.gitattributes` was refused as recorded — it renormalises the whole tree where this touches nothing else. Every stamp moves once on this build; the docstring says so, so the first fresh-stamp session reads it as expected rather than as a fault.

Tick: done, confirmed — an LF `git archive` extraction and a CRLF copy of it stamped identically (018434a0db9a both ways, 34 files converted); all 27 suites passed.
Files touched: plugin/throughliner/hooks/session_start.py.
Rule gate: not needed — hook code, no method rule authored.
