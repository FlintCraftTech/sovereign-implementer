# `#beta` install smoke test — resumed 2026-08-27

`[user]` item [beta-install-smoke-and-post-edit], resumed in the 2026-08-27
/next run. Second record under this slug; the first is
`LOG/2026-08-26-beta-install-smoke-and-post-edit.md`, which deferred at step 1.

## Resume point read off the record

The 2026-08-26 entry records step 1 handed over and **deferred by the user**,
with nothing run. So the resume point is step 1, unchanged, and no step is
skipped as already done.

## What this session could check that the last one could not

The earlier record states plainly that "this project has no view of Discord to
tell which" — whether the pinned "How to install" post already names `#beta`.
That is no longer true: the posting bot built earlier in this same run reads the
channels it has been granted, including the how-to forum.

**Checked, not assumed. The post does NOT name `#beta`.** Its install ask, read
back through the bot from thread `1541661928554758184`, says:

> Please add the plugin marketplace `FlintcraftTech/throughliner` and then
> install the `throughliner@flintcraft` plugin from it.

No ref, pinned or otherwise. So:

- **step 4 is genuinely outstanding** rather than possibly already done;
- the two claims posted to Discord on 2026-08-26 — the beta announcement calling
  the pinned post "the tested route", and the channel pin calling the beta
  release "the safe route — pinned in the how-to forum" — are **false as things
  stand**, in exactly the way the earlier record feared. Both are recorded
  against their lines in `INBOX/sent.md`.

`git ls-remote --heads origin beta` still resolves to `2a96ce4`, so the ref the
install route names continues to exist.

## What remains genuine user work

Steps 1 and 2 run on a second machine. No tool on this machine installs onto
another one, so the capability check returns the same answer it did on
2026-08-26: user work, not work Claude is merely blocked from running.

Step 4 edits a post authored by the user. A bot can only edit messages it
authored itself, so the bot route built this run does not reach it — this is
the migration [howto-posts-bot-authorship] is for.

## Progress this session

**Step 1 — PASSED**, 2026-08-27, evidenced by the second machine's session
transcript pasted into this run.

- `claude plugin marketplace add FlintcraftTech/throughliner#beta` succeeded:
  cloned over HTTPS (SSH not configured on that machine), ref `beta` resolved,
  marketplace validated, registered as `flintcraft` in user settings.
- `claude plugin install throughliner@flintcraft` succeeded at user scope.
- **No unknown-ref error**, which is the observation the step names. The pinned
  route's ref is therefore proven against a real second machine, which is what
  the item existed to establish.

Two facts fell out of the transcript that the step did not ask for:

- **The `claude` CLI is not on that machine's PATH.** The session found it at
  `~\.local\bin\claude.exe` after `Get-Command` returned nothing, having first
  failed with "claude: command not found". A walkthrough that assumes a bare
  `claude` command will fail on that machine.
- **The marketplace registered under the name `flintcraft`** — the same name the
  local directory marketplace uses on the development machine. Harmless here only
  if the second machine has no local directory marketplace of that name, because
  the CLI overwrites a same-name registration silently and says nothing
  (anthropics/claude-code#44042, guarded in `CLAUDE.md` earlier in this same
  run). Not checked from this side; flagged rather than assumed.

**Step 2 — PASSED.** After a full quit and reopen on the second machine, `/setup`
appears in the command menu in an empty folder. The user notes it appeared **only
after the restart**, which is what the step requires rather than a defect, and
that she had updated Claude Code before any of this — so the install was made
against a current CLI.

**Step 3 — not taken.** It is the failure branch, and neither step 1 nor step 2
failed.

**Step 4 — DONE.** The user edited the pinned "How to install" post. Read back
live through the bot after the edit rather than assumed, the first quote now
reads:

> Please add the plugin marketplace `FlintcraftTech/throughliner#beta` and then
> install the `throughliner@flintcraft` plugin from it.

The second quote block — the browser route pointing at claude.ai and
`INSTALL.md` — is untouched, as intended. Nothing else in the post changed.

**A wording defect in this session's own hand-over, recorded because it is
exactly what the walkthrough rules exist to prevent.** The step as first given
said "the quoted install line", and the post contains two quote blocks. The user
had to ask which one and whether the right thread was even meant. The shipped
rule requires a walkthrough involving more than one stored text to name where
each one lives; this hand-over failed it, in the same run that widened the
hand-over checkpoint. Filed as [handover-named-neither-of-two-quotes].

**Step 5 — DONE.** The `INBOX/sent.md` line for the install post is updated with
the corrected claim.

## Outcome

**done** — walked to its end this session. Both posted claims that depend on it
are now true: the beta announcement's "the tested route" and the channel pin's
"the safe route — pinned in the how-to forum" both rest on the pinned post
naming the tested ref, and it now does.
