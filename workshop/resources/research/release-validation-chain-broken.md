# The release chain cannot deliver a validated build — findings from 2026-08-27

**Dispositions written 2026-08-28:** findings 1, 2 and 4 → [rezip-archive-mirrors-nerds-channel] (the rezip builds and archives its own zip, the release packages the archived build); finding 3 → [content-stamp-normalises-line-endings]. The findings stand as written until those items ship.

Written at the end of the 2026-08-27 build session, when a request to release the
build that had just been validated could not be carried out. This is a defect
report for the next planning session, not a research finding about the outside
world.

**The short version.** Three separate mechanisms each look correct on their own,
and together they make "release the build we tested" impossible to execute and
impossible to verify. Two of the three were designed or amended earlier the same
day, on the strength of yesterday's mixup — so the fix that was supposed to
prevent this reproduced it.

---

## Finding 1 — Validation always happens on a build the tree has already moved past

**This is the root cause. The other findings are consequences or symptoms.**

The sequence the method now prescribes:

1. a rezip installs `<version>-testN` from the working tree;
2. a full `/plan` session and a full `/next` session run **on that installed
   build** — this is what "validated" means, and it is the readiness test
   [rezip-posts-its-entry] shipped today;
3. the build is then considered ready to release.

The problem is step 2. **The sessions that validate a build are the same sessions
that change it.** A `/plan` run rewrites the queue; a `/next` run builds items,
which on this project overwhelmingly means editing `plugin/throughliner/`. By the
moment a build has been exercised enough to release, the working tree is no
longer that build.

Today's numbers, as a concrete instance:

| thing | content stamp |
|---|---|
| installed `1.21.0-test2` — the validated build | `b01cd48a05bd` |
| working tree after this session's 13 built items | `c592cd7d1058` |

The release ritual packages `plugin/throughliner/` **as it stands in the working
tree**. So running it delivers `c592cd7d1058` — code that no session has
exercised — while the artifact anyone actually tested was `b01cd48a05bd`.

**Nothing in the ritual notices this.** There is no step that asks which commit
the validated build came from, and no step that packages anything other than the
current tree. A release therefore always ships the *least* tested state of the
plugin: whatever was written since the last rezip.

**This is what went wrong yesterday**, and the corrective work done today did not
touch it, because the day's design attention went to *when* an entry is posted
and *which* rezip is picked — never to *what gets packaged*.

## Finding 2 — The test-rezips entry lifecycle shipped today has the same flaw

[rezip-posts-its-entry] built this today: at a close, once one `/plan` and one
`/next` have run on the installed build, post an entry describing it and **attach
a zip of `plugin/throughliner/` as it stands**.

"As it stands" is the working tree, at a close — which by Finding 1 is precisely
when the tree no longer matches the build being described. So the entry's prose
would describe the exercised build while its attachment contained something else,
and the `Commit:` line would name the commit the *close* produces rather than the
one the build came from.

The design intent is stated in that item's own record: "every entry carries the
exact build it describes". The implementation cannot do that. `build_plugin_zip()`
in `resources/discord_post.py` zips a directory path, and the only path it is
given is the live folder.

**Nobody has posted an entry this way yet**, so nothing false is published. The
defect is in shipped instructions, not in an artifact.

## Finding 3 — The content stamp cannot compare a git object to an installed build

`content_stamp()` hashes each file's **raw bytes**. This repository has
`core.autocrlf = true` and **no `.gitattributes`**, so:

- committed blobs store **LF**;
- the working tree and anything the CLI snapshots from it hold **CRLF**.

Therefore a stamp computed over `git archive <commit>` output can never equal a
stamp computed over an installed build, even when the two are the same code.
Measured today: `d31b553`'s plugin archived out stamps `4000b750899f`, while the
installed `1.21.0-test2` it produced stamps `b01cd48a05bd`. A file-by-file diff
with `--strip-trailing-cr` showed **every** differing file was identical apart
from line endings.

**Why this matters beyond tidiness.** The stamp is the method's one mechanical
answer to "is this build the build I think it is". It works for the comparison it
was written for — source tree against installed snapshot, both CRLF, which is
step 6 of the rezip. It silently fails for the comparison Finding 1 forces anyone
to make: *a commit* against *an installed build*. So the moment you try to verify
that a release matches a validated build, the only available tool returns a
mismatch that means nothing.

A smaller related gap: the exclusion list covers `__pycache__`, `.pyc` and
`.in_use`, but **not `.orphaned_at`**, which the CLI also writes into cached
builds. Any stamp taken over an orphaned cache entry is perturbed by it.

## Finding 4 — The weekly cycle's selector has no mechanism behind it

[weekly-release-cycle], written today, says the Wednesday pick is "the most
recent rezip labelled stable on the nerds list". Two gaps:

- **Label to commit.** The mapping exists only through the `Commit:` line in a
  channel post, introduced days ago, and only for entries posted since. Nothing
  reads it back. Selecting a build means a human reading Discord and typing a
  hash.
- **Commit to release.** Even given the right commit, the ritual has no step that
  releases *from* a commit. See Finding 1.

So the cycle's steps are executable only in the sense that a person could improvise
them.

---

## What was actually done today, so the next session starts from facts

- **No release was made.** The ritual was not run past its read-only steps.
- **The rezip completed**: version bumped to `1.21.0-test3`, bytecode cleared, all
  27 suites passed, cache pruned to four builds, host re-snapshotted, and source
  and installed stamps matched at `c592cd7d1058`. The full app restart had not
  been done when this was written.
- **`1.21.0` remains the latest published release** (pre-release, 2026-08-26).
- The commit corresponding to the validated `-test2` build is **`d31b553`**;
  this session's commit is **`beac9d2`**.

## Directions a fix might take — none of these are decided

Recorded so the next session has starting material rather than a blank page.

1. **Release from a commit, not from the tree.** Add a parameter to the release
   ritual naming the commit to package, defaulting to the one the validated build
   came from. Requires knowing that commit — see 3.
2. **Normalise line endings** with a `.gitattributes`, or make `content_stamp()`
   normalise before hashing. The second is smaller and does not rewrite the
   working tree, but changes every stamp once, which needs saying out loud rather
   than discovering.
3. **Record the commit at rezip time**, in a file rather than only in a Discord
   post — the rezip already knows it. That single fact makes 1 and Finding 4 both
   tractable.
4. **Or accept that a release ships the tip and drop the validated-build framing
   entirely**, which is honest and much simpler, but abandons what today's work
   was for. Worth weighing rather than dismissing.

## The part worth being blunt about

Two of the four findings are defects in work shipped today, by the session
writing this report, hours after the design discussion that was supposed to
prevent exactly this class of problem. The design discussion asked *when* to post
and *which* build to pick. It never asked *what bytes get packaged*, and no check
in the method asks that either — which is why a full day of careful work on the
release story left the release itself unable to do the one thing it was being
redesigned to do.
