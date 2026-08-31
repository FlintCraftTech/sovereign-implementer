# Worktree isolation, desktop parallel sessions, and what this machine actually does

Researched 2026-08-11, inline (no subagent), while processing [concurrent-session-support].
Sources: https://code.claude.com/docs/en/worktrees and https://code.claude.com/docs/en/desktop
Claude Code version on this machine at the time: 2.1.222.

## 1. What a worktree is for, in the documentation's own words

> "Running each Claude Code session in its own worktree means edits in one session
> never touch files in another, so one session can build a feature while a second
> fixes a bug."

So the fork a remote or parallel session performs is a deliberate isolation
mechanism, not an accident of how sessions start.

## 2. The isolation is enforced, not advisory

While a session is isolated in a worktree, Claude Code **blocks**:

- an `Edit`, `Write` or `NotebookEdit` targeting a path in the main checkout;
- a Bash/PowerShell/Monitor command whose working directory resolves to the main
  checkout, or that it cannot verify stays outside it;
- a Bash or Monitor command redirecting git into the main checkout (`git -C`,
  `--git-dir`, `GIT_DIR`, `GIT_WORK_TREE`, or a `cd` first).

The same enforcement covers every subagent spawned from an isolated session.

## 3. This probably kills [worktree-override-hook] as designed

That item's design is a `WorktreeCreate` hook returning the *existing* tree so a
new session does not fork. The documentation now describes a check that refuses
exactly that shape:

> `Refusing to use <path> as an isolation worktree`

raised when the directory's git metadata resolves into the main checkout, or when
the directory *contains* the protected checkout. Returning the main tree is the
case the check exists to catch.

**Not conclusively settled**: the docs say a worktree created by a
`WorktreeCreate` hook, lacking git metadata, *can* pass the resume check — so
whether a hook-returned main-tree path is refused at creation time is inference
from the refusal's stated conditions, not a quoted statement about hooks. Verify
before deleting that item.

## 4. Desktop parallel sessions

> "Click **+ New session** in the sidebar ... For Git repositories, each session
> gets its own isolated copy of your project using Git worktrees, so changes in
> one session don't affect other sessions until you commit them."

Worktrees live in `<project-root>/.claude/worktrees/` by default; the location and
a branch prefix are configurable in Settings → Claude Code. A session is retired
with the sidebar's archive icon, optionally automatically after its PR merges.

## 5. What this machine actually does — and it does not match

Checked directly on 2026-08-11, in a session the user confirms was opened with
**+ New session**:

```
cwd / toplevel : <project root>          (the main checkout, not a worktree)
branch         : main
git worktree list : the main checkout, plus one unrelated hand-made worktree
                    for the shelved Codex port
.claude/worktrees/ : does not exist
```

No `worktree` key appears in the project's `.claude/settings.local.json` or the
user's `~/.claude/settings.json`, and the desktop app's own configuration under
`AppData/Roaming/Claude` holds only binaries and caches — nothing readable.

So the documented default is not in force here, and the reason is not visible from
the filesystem. It is a GUI setting or an app-level condition, which makes it a
user-observable question rather than one Claude can settle.

## 5a. Reported upstream, 2026-08-11

Filed as https://github.com/anthropics/claude-code/issues/85560 — the docs describe
automatic worktree creation as unconditional while this machine creates none.

Context found while searching first: three issues asked for an option to disable
automatic creation — #31896 (closed as duplicate), #27971, and #57484 (closed,
reading as resolved) — all about the desktop app's **local** sessions, not remote
or cloud ones. Yet the settings reference documents no opt-out; `worktree.baseRef`
(`"fresh"` / `"head"`) is the only worktree key listed, and the worktrees page puts
the location and branch prefix in a GUI panel rather than a config key. So either
an undocumented toggle shipped, or creation is failing silently here.

A future session should check that issue for a reply before re-opening the
question.

## 6. The consequence for the method, which holds either way

**The method cannot assume an isolation model.** It must be safe when sessions
share one working tree — this machine's case, and the dangerous one, since two
sessions then write the same QUEUE.md — and correct when they do not, where each
session edits its own copy and a capture filed in one does not reach the other
until a merge. The shipped "parallel sessions are allowed" rule was written for
the shared-tree case and does not know about the other.

## 6a. The reused-session hypothesis, tested and REFUTED (2026-08-14)

The leading explanation for the contradiction in §5 was that Claude Code
allocates a worktree at session *creation* rather than at `/clear`, and that a
workflow built on pre-made, cleared sessions would therefore never see one.

**Tested directly and it does not hold.** A genuinely new desktop session (+ New
session, not `/clear`) was started on this project and asked to report both git
paths. Both printed `.git` — identical, which means a main working tree.
`.claude/worktrees/` still did not exist afterwards, and `git worktree list`
still showed only the main checkout and the Codex port.

So the documented behaviour does not happen on this machine under any
session-creation route tested, and the "Worktree location" setting was already
confirmed at its default, so nothing is redirecting worktrees elsewhere either.
**This removes the leading explanation without supplying one** — §5's
contradiction stands and is now harder to explain, not easier.

**It strengthens the filed issue rather than dissolving it.** What might have
been a workflow artefact on this machine is shown not to be, so
`anthropics/claude-code#85560` describes the app's behaviour rather than how
sessions were being started. Record: `LOG/2026-08-14-cleared-sessions-may-never-get-a-worktree.md`.

**One consequence is now established rather than suspected:** the isolated path
is never exercised by this project's own testing, because isolation is absent
here under every route tried.

## 7. Worktrees are not the only isolation mechanism — the cloud clone (added 2026-08-14)

This file read as though a worktree were the only way a session could be
isolated. It is not.

**A Claude Code cloud session runs on a clone inside a container.** Its own
startup steps, from a screenshot of a live session: set up a cloud container,
**cloned repository**, run setup script, started Claude Code. No worktree is
involved. Work reaches the user's machine only as a pushed branch.

**Why that broke the isolation check.** `session_start` decided between two
cases by comparing `git rev-parse --git-dir` against `--git-common-dir`: they
differ in a linked worktree and match in a main checkout. **In a clone they also
match, because a clone is a main checkout.** So a cloud session was classified
as a shared tree and told that two appends to different parts of QUEUE.md do not
collide and the file-modified warning will catch them if they do. Both halves
are false there, and this is worse than the worktree case rather than equivalent:
the worktree branch of the advice at least describes isolation, while the clone
got the one branch that actively misleads.

**The discriminator, measured on a live cloud session rather than guessed.** Both
git paths resolved to the same `.git`, confirming an ordinary clone. The
environment carries the signal:

```
CLAUDE_CODE_REMOTE_ENVIRONMENT_TYPE=cloud_def…   # the one to key on
CLAUDE_CODE_ENTRYPOINT=remote_mobile
IS_SANDBOX=yes                                    # broader; other sandboxes may set it
```

`IS_SANDBOX` was rejected as the signal: it describes sandboxing generally, and a
false positive would hand an ordinary session the wrong branch of the advice.

**Absence means "not cloud", deliberately.** These variable names are
undocumented, so a rename is a live risk. Written this way a rename loses the
improvement; written the other way it would produce a confident wrong answer.

Container observed: `sandbox-ccr-default`, running Claude Code 2.1.42, entered
from mobile.

## 8. What a deliberate long-lived worktree looks like (recorded 2026-08-14)

Recorded here because the only live specimen on this machine is scheduled for
deletion, and the example would otherwise vanish with it.

**The specimen.** The shelved Codex port: branch `codex/si-port`, checked out in
a worktree at a **sibling folder outside the project** (`../Sovereign
Implementer - Codex port`), dormant since 2026-07-28, 31 commits ahead of the
main checkout. `CLAUDE.md` describes it as read-only history with no live
relationship to maintain.

**What marks it as an archive rather than session work.** Not its name, and not
its commit count — a stranded session branch looks identical on both. It is the
**location**: it sits outside the project entirely, whereas Claude Code allocates
a session's worktree inside `<project-root>/.claude/worktrees/` by default, and
the desktop setting offers only that default or a custom folder, with no option
that disables worktrees. Sources: [Run parallel sessions with
worktrees](https://code.claude.com/docs/en/worktrees) and the Settings → Claude
Code → "Worktree location" control.

**Which way the path test fails.** Where a user has set a custom worktree
location, their session worktrees classify as deliberate and go unoffered — a
missed merge offer. It never does the opposite, because an archive is never
inside `.claude/worktrees/`. That asymmetry is why the path test was chosen over
a naming test, which fails in both directions.

## 9. Adjacent finding, noted rather than pursued

The desktop app has **native cross-session messaging**: Claude can list the other
Code-tab sessions, read what they have been doing, and send messages between them,
with incoming messages shown as attributed cards. This is adjacent to the
cross-project INBOX design and worth reading before that thread goes further. It
covers sessions the desktop app runs itself — not cloud sessions, terminal CLI
sessions, or VS Code extension sessions.
