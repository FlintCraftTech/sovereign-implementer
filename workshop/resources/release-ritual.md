# Rezip and Release — the two rituals that fire on an explicit word

Fetched on demand. Read this when Alex says **"rezip"** or **"release"**, and at no
other time. Neither ritual has an unprompted trigger, which is precisely why they
live here instead of in the always-loaded `CLAUDE.md`: about twenty-five standing
instructions, none of which ever fires on a condition Claude has to notice.

**Push is not here.** It runs after every /next and at any /done — a standing
condition, not an explicit word — so it stays in `CLAUDE.md` where it is always
loaded. The three-way framing (rezip vs push vs release) and the on-request rule
stay there too, because knowing *which* action is being asked for has to happen
before this file is opened.

## Recovering from a project-folder move

Moving this project folder breaks two path-based links that both hold absolute
paths and don't self-heal — fix both, then fully restart the app:

1. **Local-directory marketplace.** The desktop app's marketplace registration
   keeps pointing at the old path: slash commands stop autocompleting and get
   flagged "invalid" (the cached snapshot still runs when forced). Re-point it in
   place — `claude plugin marketplace add "<new project path>"` (re-registers the
   path; no `remove` needed) — then
   `claude plugin install throughliner@flintcraft`.
2. **Git worktree, if this checkout is one.** A move severs the worktree link both
   ways and git reports "not a repository" until both sides are repointed: this
   worktree's `.git` file (the `gitdir:` pointer) and the main repo's
   `worktrees/<name>/gitdir` back-reference. Check whether this checkout is a
   worktree before assuming it is — the `queue-redesign` worktree this note was
   written for has since been merged away.

Consumers are unaffected — they install from the GitHub marketplace, which has no
local path to break.

## Rezip (local testing)

When Alex says "rezip" (or asks for a fresh local build to test), run this — no
release version bump, no archive, no GitHub Release. It comes *before* a push, not
after one: the test build that was actually exercised is then the build the push
carries.

**The `-testN` test-build scheme.** A rezip refreshes the installed host without a
release bump, because bumping the release version on every private test build would
nag Alex's own projects to re-run /setup each time. But test builds still need to be
distinct and unmistakably-test, so each carries a `<base>-testN` version — the
release-line base plus `-test` and a number incremented each rezip-for-testing (e.g.
`1.12.0-test1`, then `-test2`). Honest framing: the suffix is not what makes a
reinstalled host load — the full app restart is. `-testN`'s job is to keep each test
build a distinct, clearly-labeled version never mistaken for a release, and to force
the CLI to re-snapshot (see the bump rule below). **The suffix is committed and
does reach the remote**, where it sits between releases; the release bump is what
strips it, so it never reaches a published release. The push's version-clean step
was repealed on 2026-08-19 — the owner of the repository judged a suffixed version
on the remote untidy rather than harmful, and the clean was running at every rezip
to prevent it.

**The bump rule — the one sentence whose absence caused a whole session to run on
the wrong plugin.** `claude plugin update` matches on the **version string**.
Re-running it against an unchanged version reports "already at the latest version",
re-snapshots nothing, and reports success — however far the source has moved since.
So **any source change made after a rezip needs a fresh `-testN` bump before another
update will take.** "I already rezipped today" is not sufficient and never was. On
2026-08-09 a rezip installed `-test1` while the source was still two commits behind;
every later update was a silent no-op, and a /plan session ran half its length
loading procedure docs from a docset that had already been retired. Bumping to
`-test2` fixed it instantly.

1. Bump the test suffix in `plugin/throughliner/.claude-plugin/plugin.json`. **Read
   the next number from the installed builds in the plugin cache — take the
   highest `-testN` present on this release line and add one** — not from
   `plugin.json`. List the cache directory to see them:
   `Get-ChildItem "$env:USERPROFILE\.claude\plugins\cache\flintcraft\throughliner"`.
   Bump on every rezip, whatever the reason for it.

   **The cache is the authority because it is what the CLI matches against.**
   `claude plugin update` keys on the version string, so re-installing a string
   the CLI has already seen reports success, re-snapshots nothing, and leaves the
   session believing it runs new code — the silent no-op this bump exists to
   prevent, which cost most of a session on 2026-08-09.

   **`plugin.json` cannot answer this**, and the branch that read it is deleted
   rather than left standing: the push strips the suffix, so the committed
   version always carries none, and every rezip following a push therefore read a
   bare version and named `-test1` — a build that already existed. That misfired
   twice, on 2026-08-14 and 2026-08-15, and both times was saved only by someone
   listing the cache, which nothing asked for. This writes that habit in.

   A release bump starts a new release line, which genuinely has no prior test
   builds, so the first rezip after one finds nothing in the cache for that line
   and starts at `-test1`.
2. Delete all `__pycache__` folders under `plugin/throughliner/` so compiled Python
   bytecode never gets snapshotted into the installed host (disposable — Python
   regenerates them as needed):
   `Get-ChildItem "plugin\throughliner" -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force`.
   **This is belt-and-braces for the install only.** It cannot keep bytecode out
   of the zip, because step 3's suites import the hooks and regenerate the
   folders it just deleted; the zip is protected by its own exclusion at step 7.
   (The install itself uses no zip — the local marketplace sources the plugin from
   the `plugin/throughliner` folder, and the CLI snapshots that folder directly.
   The zip step 7 archives is for the channel and for the release to package, not
   for this install.)
3. **Run the test suites and stop if any fails.** They exist, they pass,
   and for a period nothing ran them — which is how a `session_start.py` emitting a
   rejected payload shape stayed dead and invisible, sessions compensating by
   reading CLAUDE.md and the queue directly. The runner discovers every suite in
   the folder, so nothing here names one:

   ```bash
   py resources/testing/run_all.py
   ```

   **The honest limit, which travels with them and must never be dropped: the
   schema check asserts output *shape*, not *delivery*.** A correctly-shaped hook
   can still be discarded before it reaches a session. These suites do not replace
   the liveness proof after the restart; they are the half a machine can do.
4. **Prune the plugin cache** at
   `~/.claude/plugins/cache/flintcraft/throughliner/`, keeping the build
   about to be installed and the three most recent. Nothing else ever removes these,
   so every test build accumulates — ten by 2026-08-04, six again by 2026-08-09 —
   and the pile is what makes "which host is actually live?" hard to answer.
5. Refresh the installed host from the local-folder marketplace via the `claude`
   CLI. The desktop app has no in-app plugin upload, and a working-tree edit alone
   changes nothing the installed host sees — the host runs a frozen snapshot the CLI
   copied into `~/.claude/plugins/cache/...` at install time, not the live files.
   Claude runs these commands; Alex types nothing in a terminal.

   **`claude` is NOT on PATH in the desktop app's Bash/PowerShell tools — invoke it
   by full path.** A bare `claude plugin …` fails with "command not found"; this is
   the single reason the reinstall has repeatedly been handed to Alex instead of run
   by Claude. The executable is at `~/.local/bin/claude.exe` (equivalently
   `C:\Users\<you>\.local\bin\claude.exe`); if it isn't there, it's under
   `AppData/Roaming/Claude/claude-code/<version>/claude.exe`. Run every CLI step in
   this ritual by full path, e.g.
   `"/c/Users/<you>/.local/bin/claude.exe" plugin update throughliner@flintcraft`.
   Locating and running it is Claude's job — don't hand the reinstall to Alex just
   because a bare `claude` failed.
   - First time only — register the local marketplace (the committed
     `.claude-plugin/marketplace.json`, marketplace `flintcraft`, which points at
     `plugin/throughliner`): `claude plugin marketplace add "<PROJECT_ROOT>"` —
     substitute `<PROJECT_ROOT>` with the absolute path to this project's folder on
     your machine.
   - Each rezip after — re-snapshot the current build:
     `claude plugin update throughliner@flintcraft` (or
     `claude plugin install throughliner@flintcraft`).
6. **Compare the content stamps immediately after installing — before saying
   anything to Alex about restarting.** Run `content_stamp()` (from
   `plugin/throughliner/hooks/session_start.py`) over `plugin/throughliner`, and again
   over the cache directory for the version just installed. No edits happened in
   between, so the two must be **identical**. A difference is unambiguous rather
   than a judgement call: either the snapshot didn't take or the stamp function is
   wrong, and both are worth stopping for. This is the step that catches the
   silent-no-op failure the bump rule describes, and it caught a real shipped bug
   the day it was first written down. Its honest limit: it proves the installed copy
   matches the source, and cannot prove the stamp function computes the right thing.

   **The stamp hashes `plugin.json` with its `version` key dropped**, so the
   `-testN` suffix the rezip just set does not itself move it. That is what makes
   the comparison meaningful across the rezip-then-push sequence: without the
   exclusion the push's version-clean moved the source stamp on its own, and the
   host read as stale in exactly the sessions most likely to be checking. It also
   means a pure release bump leaves the stamp where it is.
7. **Archive this build's zip and its readme.** The stamps have just been proved
   equal, so the folder on disk *is* the installed build — which is the one moment
   the bytes are known good. Build the zip from `plugin/throughliner/` and write it
   plus a readme into `plugin/rezip-archive/`:

   Build it with Python's `zipfile`, through the Bash tool, substituting the
   version into both the filename and nothing else:

   ```bash
   py - <<'PY'
   import os, zipfile
   VERSION = "<VERSION>"
   src = "plugin/throughliner"
   dest = f"plugin/rezip-archive/throughliner-v{VERSION}.zip"
   with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
       for root, dirs, files in os.walk(src):
           dirs[:] = [d for d in dirs if d != "__pycache__"]
           for name in files:
               full = os.path.join(root, name)
               # Entry names are relative to plugin/, so every path starts
               # `throughliner/`, and forward slashes are written explicitly:
               # the zip format specifies them, and a backslash entry unzips
               # on macOS and Linux as one flat file literally named
               # `throughliner\skills\next.md` rather than as a folder tree.
               arc = os.path.relpath(full, "plugin").replace(os.sep, "/")
               z.write(full, arc)
   print(dest)
   PY
   ```

   **Python and not `Compress-Archive`.** PowerShell 5.1's cmdlet writes the
   platform separator into the entry names, so every zip this project has ever
   shipped — the archived ones and the one attached to each GitHub Release —
   stores backslashes the format does not allow. Windows tools tolerate them,
   which is why nothing here ever saw it. Python writes conformant paths, is
   what everything else in this project runs on, and removes a PowerShell
   dependency from the ritual.

   **The `__pycache__` exclusion lives here, at zip time, and that ordering is
   the fix rather than a duplication.** Step 2's sweep runs before the test
   suites in step 3, and those suites import the hooks and regenerate exactly
   the folders the sweep deleted — so bytecode reached the zip anyway, observed
   live. Excluding at the moment of writing cannot be outrun by a later step.

   (Zip the folder, not its contents — internal paths must start with
   `throughliner/`. Verify by listing the zip's entries.)

   The readme sits beside it as `throughliner-v<VERSION>.md` and carries **exactly
   what the channel post for this build says** — its label, its `Commit:` line, and
   its version. That equality is the point: the archive is a local mirror of the
   test-rezips-for-nerds channel, one entry per build, so the label a release picks
   by is read from a file here rather than from a person reading Discord.

   **Prune to the newest 15**, mirroring what the channel shows. The folder is
   gitignored — every build is rebuildable byte-for-byte from its `Commit:` line, so
   committing the zips would store what git already holds.
8. **Check the CLI's version against the app's.** The `claude` CLI and the desktop
   app can be on different builds, and a plugin behaviour that depends on a recent
   Claude Code version will then work in one and not the other. Note the mismatch
   plainly if there is one rather than debugging past it.
9. Tell Alex to do a **full app restart, not just a new session** — plugin skills
   register at app launch, and on Windows a normal quit can leave the app running,
   so she must fully quit (confirming the process has exited, via Task Manager if
   needed) and relaunch. Say: "Host refreshed via the CLI — nothing has been
   published. Fully restart the app to load it for private testing."
10. **Prove the hooks are alive after the restart** — the delivery half that
   step 3 cannot give. A hook that is well-formed, installed, and silently
   dropped looks exactly like a working one from this side.

   **The primary proof is the re-fired `[Throughliner]` session-start payload
   arriving in the rezip chat itself after the full restart.** The restart
   re-fires session start into the chat that is already open, so read the
   block there — no fresh chat needed. (Observed working on the
   -test13/-test14 rezips of 2026-08-21: the payload arrived in-chat carrying
   the new build stamp, and the stamp matched the source.)

   **Where no payload re-fires in-chat, the fallback is a fresh session in a
   project whose state reproduces the check** — version marker stale, epoch
   current, nothing missing. Paste this block verbatim into that fresh
   session — it is fixed text, not a template to adapt; fresh composition is
   the recorded failure and fixed is also cheaper:

   ```
   Quote the [Throughliner] block from your session start verbatim. If no
   such block arrived, say so plainly rather than reconstructing what it
   would have said. If you can only paraphrase, answer these four instead:
   (1) What plugin version did it report? (2) What build stamp? (3) Did it
   halt you, or let the session proceed? (4) What did it say about waiting
   mail?
   ```

   **How to read the answer:**
   - the block quoted, with the new `-testN` version and a build stamp
     matching the source's -> the fix landed; done.
   - a halt about the document format or a missing doc -> a real halt, not a
     delivery failure — the project's state, not the rezip, is what is
     speaking.
   - the old version number, or no block at all -> the restart was
     incomplete (the process never exited) or the update was the silent
     no-op the bump rule describes — re-check the cache and the stamp before
     touching anything else.

   **Known false positive, not a finding:** the returned block currently
   reports `INBOX/sent.md` as waiting mail. Already known — do not file it.

### No entry is posted here

**The test-rezips entry does not post at the rezip.** It posts at a later close,
once at least one full /plan and one full /next have run on the build this rezip
just installed — an entry describes a build that has been exercised. The check
and the entry's two-step lifecycle are in `CLAUDE.md`'s Discord posts section.

### Tip-candidate check

The rezip is the moment a feature lands in the installed build, which makes it
the moment a tip about that feature becomes noticeable. Read what this rezip
carries — the commits since the last one — and file a capture in Unprocessed for
each feature a tip could explain, screened first against the posting brief's
visibility test. A candidate is not postable until a release clears it, which is
the release step below.

**Captures, not a pool file.** The queue is the one file every session may write
whatever it is doing; a rezip runs after a close, so the session has no build
working file and the scope-lock treats it as a planning session — which refused
the write to `ANNOUNCEMENT-IDEAS.md` outright the first time this step ran.

Nothing is posted here, and a rezip carrying no user-facing feature files
nothing. Say in one line what was captured, or that nothing was.

## Release (on request)

Run this when Alex asks for a release, and only then. Once she has asked, run the
whole ritual through without further confirmation per step — the asking already
happened. Every step that says "push" here means the ordinary `git push` in
`CLAUDE.md`.

The last-release tag is read from `gh release list` after `git fetch --tags`, never
from `git describe --tags`. Both halves were verified rather than assumed: release
tags are created by `gh release create` on the remote and are not in the local clone
until fetched, and this repo carries ~135 unrelated local tags (`v95`, `v103`, …)
from an older history, none of them ancestors of HEAD, so `git describe` fails
outright here.

1. **Open the queue item that scheduled or constrains this release, and run
   against what it says.** Search QUEUE.md for an entry about this release — a
   release cycle, a version this one has to carry, a post that waits on it — and
   where one exists, read it in full before touching anything else. A release
   that ignores the item scheduling it is a release nobody can check afterwards,
   and the item is where the constraints were written down.

   ```
   a scheduling item exists   ->  read it whole; its constraints govern the
                                  steps below, and its slug names the record
                                  written at the end
   no scheduling item         ->  proceed; the record at the end is written as
                                  a plain release entry under its own slug
   ```
2. Backfill any unfilled commit-hash placeholders anywhere in `LOG/` before
   proceeding. The session-start hook only fires at session start, so a /done that
   ran earlier in this same session leaves its placeholder unfilled at push time —
   this step catches it. Same rules as the hook: replace the token only in hash
   position (an entry heading line or the start of an index line), never in body
   prose, which may mention the token literally; resolve each to the **oldest**
   `git log -S "<entry title>"` match, never the newest commit touching the file.
3. Bump version in `plugin/throughliner/.claude-plugin/plugin.json` to a clean
   patch/minor — patch for fixes/incremental, minor for new capabilities (`1.20.0` →
   `1.20.1` or `1.21.0`). **Strip any `-testN` suffix as part of this bump —
   expect one to be present rather than treating it as a sign something was
   skipped.** The push commits the suffix as it stands (the version-clean step
   there was repealed 2026-08-19), so the committed version between releases
   normally carries one. This is the only place it comes off, which is what
   keeps a test suffix out of every published release. The release bump lives here, not in rezip — rezip
   only ever touches the `-testN` test suffix, never the release line, because
   bumping the release version on every private test build would make Alex's own
   projects nag "version changed, re-run /setup" each time she tests.
4. Pre-release consistency sweep — two passes, run in order:

   **Pass A — Gather the feed:** List the commits since the last release, using the
   tag lookup described above (fetch tags first; read the tag from
   `gh release list`, never `git describe`):

   ```bash
   git fetch --tags && git log --oneline "$(gh release list --limit 1 --json tagName -q '.[0].tagName')"..HEAD
   ```

   Read their LOG entries (each session's own file under LOG/) to understand what
   changed (files touched, features added/removed/renamed, concepts that shifted).
   **The range is since-the-last-release-tag, not `origin/main..HEAD`** — that older
   range meant "unpushed," which under routine pushing is usually empty, so the
   sweep would silently read nothing and pass. The release span is what this sweep
   is about, and Pass A's output is also the feed the release notes are written from
   in the GitHub Release step.

   **Pass B — Check for staleness against those changes:**
   - **Target internal consistency:** Do templates match the procedure docs they
     ship alongside? Compare FAQ templates and CLAUDE-TEMPLATE.md against current
     procedure docs (field names, doc structure, workflow descriptions). Update any
     that fell behind.
   - **Project docs:** Check QUEUE.md, SPEC.md, and LOG/ for references to removed
     features, renamed fields, or old formats that the release span's commits
     changed. Fix any found.
   - **CLAUDE.md:** Check its descriptions (Architecture, Method docs, Rules)
     against current target state. Update any stale references.
   - **The install path:** re-read README.md's Install section and INSTALL.md
     against the way the plugin is actually installed today — the commands, the
     marketplace name, the minimum Claude Code version. This one earns its own
     clause because nobody who already has the plugin ever exercises it, so it can
     break completely and stay broken; the only person who would notice is a
     brand-new user who by definition can't diagnose it. Every other doc gets read
     by someone eventually. This one doesn't, so the release sweep is where it gets
     read.
5. **Identify the build being released, from the rezip archive.** The pick is a
   file read, not a judgment: open `plugin/rezip-archive/` and take the entry the
   release is for — its readme carries the label, the version and the `Commit:`
   line. That commit is the build going out. Say the version and the commit in one
   line before continuing.

   **Nothing is picked from the working tree.** The archived zip was built at the
   moment its build was installed and proved equal to the source, so it holds the
   bytes that were actually tested; the tree has moved since, and packaging it
   would ship a build nobody ran.
6. **Run the test suites and stop if any fails**, the same runner the rezip uses:

   ```bash
   py resources/testing/run_all.py
   ```

   The rezip already ran them, but a release can be asked for days later with
   commits landed since — and this is the last moment before something is
   published under a version number.
7. **Check the archived zip against the commit its readme names, and stop if they
   differ.** Run `content_stamp()` (from
   `plugin/throughliner/hooks/session_start.py`) over the archived zip's extracted
   contents, and over `git archive <the readme's commit>` — the same commit step 5
   read.

   ```
   stamps match     ->  the zip holds the build its readme claims. Carry on.
   stamps differ    ->  ONE standalone turn: say plainly that the archived zip and
                        the commit recorded beside it are not the same build, name
                        which entry it is, and stop there. Proceed only on Alex's
                        next word.
   ```

   **A release releases a tested rezip.** That is the invariant this step guards,
   and it is what makes a release safe to publish without re-testing everything.
   Under the archive model the invariant holds by construction — the zip *is* the
   tested build — so this step is checking that the archive's own bookkeeping is
   intact, not that the working tree has stayed still.

   **The working tree is not consulted at all**, which is the whole point of the
   change: an edit landed since the tested rezip belongs to a current or future
   rezip, and can no longer reach a release by accident.

   The warning stops nothing on its own: warn-don't-enforce governs, and Alex may
   knowingly release anyway.
8. Repackage — **copy, do not build**:
   `cp plugin/rezip-archive/throughliner-v<PICKED_VERSION>.zip plugin/throughliner.zip`
   The archived zip already has the right internal paths (`throughliner/…`) and
   already passed the separator and `__pycache__` checks when it was built.
   Verify anyway — list the entries and confirm every path uses forward slashes
   and none contains `__pycache__`:

   ```bash
   py -c "import zipfile;n=zipfile.ZipFile('plugin/throughliner.zip').namelist();print(sum('\\\\' in x for x in n),'backslash;',sum('__pycache__' in x for x in n),'pycache;',len(n),'entries')"
   ```

   Both counts must be zero. A zip predating the Python zip step will fail the
   first — stop and rebuild it from its `Commit:` line rather than shipping it.
9. Stage every dirty path in `plugin/throughliner/` (run
   `git status --porcelain plugin/throughliner/` and stage each listed path — catches
   any sweep edits from the consistency sweep), plus the zip in `plugin/`,
   plugin.json, and the LOG/ changes (including the hash-backfill edits). Commit:
   "Bump to v<VERSION> and repackage". Nothing from `plugin/rezip-archive/` is
   staged — it is gitignored.
10. `git push`.
11. Publish a GitHub Release for the new version, so users who subscribed via Watch
    → Releases get notified — a plain `git push` does not fire that notification;
    only a published Release does. Use `gh`:
    - Tag and title = the new version (e.g. `v1.13.0`).
    - **Always `--prerelease`.** The plugin is in active testing and is not
      marketplace-ready; the flag says so structurally so it never has to be
      re-decided per release. Drop it only when the project genuinely leaves
      testing, which is a deliberate decision, not a judgment made inside this
      ritual.
    - **Notes summarise everything since the previous release, and must never be the
      commit message.** Write them from the consistency sweep's Pass A feed — the LOG entries
      across the whole release span, which will usually cover several sessions. The
      commit message describes one commit; the notes describe a release. So a note
      that restates the commit message is wrong **even when the span holds a single
      commit**, because it reports what was typed at a commit rather than what
      changed for a reader. Group by theme rather than listing commits, say what
      changed and why it matters in plain English for the Discord reader, and name
      it plainly as a testing build.
    - Attach the zip: `plugin/throughliner.zip`.
    - **Generate and attach the port-facing changelog**, so a port tracking this
      project can survey what changed in the shipped package since the version it
      last ported from:

      ```
      py plugin/throughliner/scripts/port_changelog.py . \
          --from <PREVIOUS_TAG> --to v<VERSION> \
          --out <scratchpad>/port-changelog-v<VERSION>.md
      ```

      `<PREVIOUS_TAG>` is the last-release tag already read from `gh release list`
      at the top of this ritual. It writes to the session scratchpad rather than
      into the repository: every release's copy is kept as a Release asset, so a
      file per release in the tree would store what GitHub already holds. Where it
      reports that nothing shipped, attach nothing and say so in the notes — a
      release whose whole span is host-only work has nothing for a porter, and
      an empty changelog would imply otherwise.
    - Command shape:
      `gh release create v<VERSION> plugin/throughliner.zip <scratchpad>/port-changelog-v<VERSION>.md --title "v<VERSION>" --prerelease --notes "<summary>"`.
    - If `gh` isn't authenticated in this session (the command errors on auth), don't
      silently skip the Release — tell Alex how to publish it from the GitHub web UI
      instead: on the repo's **Releases** page, click **Draft a new release**, create
      the tag `v<VERSION>`, set the same title, paste the summary as the notes,
      attach `plugin/throughliner.zip`, and **Publish release**. The step never silently
      does nothing.
12. Update the installed host via the `claude` CLI, then tell Alex to fully restart
    the app. Same mechanism as the Rezip reload step — the host reads a frozen cache
    snapshot, so without a CLI update + full restart it keeps running the old build.
    The marketplace is already registered from earlier testing, so this is just:
    `claude plugin update throughliner@flintcraft`. **Invoke `claude` by
    full path — it is not on PATH in the desktop app's shell tools (see the Rezip
    reload step's PATH note); a bare `claude` fails, but running it is Claude's job,
    not a hand-off to Alex.** Then tell Alex: "Released and pushed. I've updated the
    host via the CLI so it's running the released version — fully quit and relaunch
    the app to load it."
13. **Write the release's own session record, and settle the item that scheduled
    it.** A release usually runs after the close, so nothing else will record it
    — and a release nobody recorded is the one piece of work that leaves the
    project with no trail at all.

    ```
    a scheduling item exists   ->  write the LOG entry under that item's slug,
                                   add its index line, then close the item
                                   (remove it) or update it with what this
                                   release did and what it still waits on
    no scheduling item         ->  write a plain release entry under its own
                                   slug, with its index line, naming the
                                   version and what went out
    ```

    The entry says what was released, what the release notes claimed, and
    anything that had to be decided along the way. It rides the next session's
    commit like any other post-close work.

### Clear the tip candidates this release ships

The release is what makes a tip candidate postable, so this is where the open
candidates are marked. Read the tip-candidate captures in Unprocessed against the
features this release shipped, and append one line to each that this release
clears, naming the version that cleared it.

Nothing is posted here either. Those lines are read by the next /plan, which
files the cleared candidates as dated post items — new or updated features
first, historical tips on slow news days. Say in one line which candidates were
cleared, or that none were.

**Archive accuracy.** The rezip builds every zip and the release only copies one,
so `plugin/rezip-archive/` holds the newest 15 builds as they were installed, and
`plugin/throughliner.zip` in the working tree is always the last released one. Git
history remains the authoritative record either way, since each release commits
`throughliner.zip` and every archived build is rebuildable byte-for-byte from the
`Commit:` line in its readme.

LOG entries are per-entry files — no log capping at push time. Existing `LOG/log.md`
and `LOG/log-v*.md` files stay in place untouched: index references work by hash, so
old entries remain findable.
