# Emergency revert: whole repo back to 6ba51d3 (2026-08-02)

Executed 2026-08-09. Kept as the record of what was reverted, why, and how to get any of it back.

**Host-only, and finalised 2026-08-09.** This file is the record of one specific revert of this repository. The *general* lessons it produced — what a rollback does to a project afterwards — were extracted into `plugin/si-plugin/docs-b/recovery.md`, which ships to consumers and is fetched on demand. Don't add general guidance here; add it there.

**What stayed here rather than shipping, and why.** A consumer reverting their own project never reinstalls this plugin, so these three don't apply to them:

- The "lowest available rather than small enough" reasoning *as it applies to this plugin's own docs* — the shipped doc carries the general form of the point without the word counts.
- **The plugin CLI will not install backwards** (the gotcha below). A revert that lowers the version must bump *above* the installed one before an update takes.
- **`claude` is not on PATH** in the desktop app's shell tools.

The third gotcha — orphaned files after `git rm --cached` plus `checkout`, and rename-detected pairs escaping the deletion list — is general and did ship.

**The first real test of this document, recorded 2026-08-09.** The /plan session that followed the revert used it and found it strong on *how to execute* a revert and near-silent on *what a revert does to the project afterwards*. That gap is what `recovery.md` now fills. Its lead finding — the queue keeps asking for work already done — has since been evidenced twice: seven instances in the session immediately after the revert, and once more during the /next run of 2026-08-09, where a queue item asked for a fix that had shipped at `f9326dc`.

**The verification section below is the model to reuse**, and `[rezip-verification-steps-restored]` restored the same shape for rezips.

## Context

plugin-behaviour.md had ballooned from 6,162 words (its birth, 2026-08-02, commit `6ba51d3`) to 21,445 words at HEAD. Alex called an emergency step back to that lowest point, accepting the loss of all work since — the docset-A retirement, cycle machinery, glossary, and the rest. Chosen scope: **whole repo**, not just the one file.

Word count of `plugin/si-plugin/docs-b/plugin-behaviour.md` per commit, which is how the revert point was chosen:

| Date | Commit | Words |
|---|---|---|
| 2026-08-09 00:20 | `7a4b377` | 21,445 |
| 2026-08-08 13:48 | `ffab488` | 20,326 |
| 2026-08-07 10:06 | `96166c6` | 16,774 |
| 2026-08-06 03:03 | `7a161aa` | 11,938 |
| 2026-08-05 10:36 | `d5378c7` | 9,549 |
| 2026-08-04 01:29 | `68ca27e` | 6,430 |
| 2026-08-03 02:14 | `f37e332` | 6,430 |
| **2026-08-02 14:12** | **`6ba51d3`** | **6,162** ← revert target (the file's birth) |

## Approach: revert-commit, not history rewrite

The repo is public and the rules bar `--force` pushes, so history was not rewound. Instead: **one new commit whose tree is exactly `6ba51d3`'s tree**. The working state becomes Aug 2's state; everything since stays in history and is recoverable.

## Steps as executed

1. **Safety net first.** Committed the 3 dirty files on `overnight-blitz-2026-08-09` as `3ce1ebe` ("Pre-revert snapshot"), tagged the tip **`pre-revert-2026-08-09`**, pushed branch + tag.
2. **Built the revert state** on branch `revert-to-2026-08-02`:
   ```
   git checkout -b revert-to-2026-08-02
   git rm -rq --cached .
   git checkout 6ba51d3 -- .
   ```
   Then deleted from disk the files that existed only in HEAD (237 staged deletes, plus 4 more that git reported as *renames* rather than deletes and so escaped the first sweep — `resources/self-authoring-rules.md` and three `resources/testing/` files whose Aug-2 home was `resources/captures/`). Committed as `19ff11b`.
3. **Verified** before merging: `git diff --cached 6ba51d3` empty, then `git diff 6ba51d3 HEAD` empty.
4. **Merged to main and pushed** (`ffab488..19ff11b`).
5. **Reinstalled the host**: pruned `__pycache__` and old cache builds, bumped the version, `claude plugin update sovereign-implementer@flintcraft` via the CLI's full path, then a full app restart.

### Gotchas worth remembering

- **`git rm --cached` + `checkout` leaves orphans on disk.** Files tracked only in HEAD stay on disk as untracked after the index is rewritten. They must be deleted explicitly, and **rename-detected pairs don't appear in the `D ` list** — check the `R ` lines too, or the tree won't match.
- **The CLI won't install backwards.** The installed host was `1.19.0-test6`; the reverted `plugin.json` said `1.16.0-test2`. `plugin install` answered "already installed" and re-snapshotted nothing. Fixed by bumping to a version *higher* than the installed one — `1.20.0-test1` — after which `plugin update` took. Any future revert that moves the version backwards hits this.
- **`claude` is not on PATH** in the desktop app's shell tools. Invoke `~/.local/bin/claude.exe` by full path.

## What survives / what's lost

- **Survives in history**: every commit from 2026-08-03 through 2026-08-09, reachable via the tag **`pre-revert-2026-08-09`** and branches `overnight-blitz-2026-08-09` / `revert-to-2026-08-02`. Individual pieces are cherry-pickable; individual files are recoverable with `git checkout pre-revert-2026-08-09 -- <path>`.
- **Lost from the working state**: the docset-A retirement (`docs/` returns; CLAUDE.md reverts to the two-docset world), cycle/queue machinery, the glossary, all doc growth, ~50 LOG entries, the whole hook test suite (`resources/testing/hook_schema_check.py`, `test_pre_tool_use_shell_writes.py`, `test_reorder_queue.py`), and the research notes written since Aug 2.
- **Known staleness**: the reverted CLAUDE.md and QUEUE describe an Aug-2 world (docset A live, the substitution directive, etc.). Internally consistent, but out of date about its own history. Expect early sessions to read slightly stale-forward.

## Verification (all passed)

- `git diff 6ba51d3 HEAD` — empty, on both the revert branch and main.
- `wc -w plugin/si-plugin/docs-b/plugin-behaviour.md` → **6162**.
- Target vs installed content stamp: **`00f5a1badf57`** on both — the installed host carries the reverted files.
- Post-restart hook run: `session_start.py` emits real context (red-flag surfacing, project-setup state, FAQ index) and — the point of the exercise — **no 21,000-word behaviour-rules directive**.

The hook *schema* checks named in the original plan could not be run: those test scripts were written after Aug 2 and do not exist at this state.
