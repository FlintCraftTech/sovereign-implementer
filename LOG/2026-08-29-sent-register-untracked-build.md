# [HASH] — The outbound register cannot be overwritten or deleted through Claude's tools

`INBOX/sent.md` is the index of everything this project has sent or posted, and it is what the repeal check greps for claims already announced. Its folder is gitignored on every path, so unlike every other project document it has no history, no backup, and one accidental deletion ends it.

The exposure is per-file, and reading the folder at processing is what established that rather than inheriting the report's framing: the register holds no absolute paths and names only projects that are already public, while the address book beside it holds paths identifying the user and their machine. So the blanket ignore is wrong for one file and load-bearing for the other, which is why the fix is a guard rather than a folder-level change. Un-ignoring the register stays refused — the repository is public and the user declined publishing it — and so does moving it out of the mailbox, which fails on the same ground.

The guard is Write-only, like its LOG sibling: the register is appended to and edited at every approved send, and both go through Edit, so nothing correct is caught. The shell half matches removal, truncation and rename while letting append and read through.

The residual is stated in the guard's own docstring rather than only here, because that is where the next reader meets it: a hook sees only what goes through Claude's tools, so a deletion outside the app, or a lost disk, is not reached by this.

Tick: done, confirmed — a Write onto the register is refused, an Edit is not, and shell removal, truncating redirect and rename-away are refused while append, read and an unrelated mailbox file pass.

Depth: short.

Red flag: carried one, cleared at processing — designed out for the reported failure, with the residual above accepted by the user at that point.

**Files touched:** `plugin/throughliner/hooks/pre_tool_use.py`, `resources/testing/test_pre_tool_use_overwrite_guard.py`, `README.md`.

**Routed to Captures:** none.
