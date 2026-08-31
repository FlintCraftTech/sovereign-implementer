# Rezip and Release — the reference companion

**The steps moved.** Both rituals now live as definitions in `CYCLES.md`, at the
project root: **Rezip [rezip]** and **Release [release]**, each with its firing
word and its `Writes:` field. Read them there — this file no longer carries a
step list, and a step list kept in two places is a step list that drifts.

What stays here is the what-if material: procedures that are not steps of a turn
but are needed when something specific has gone wrong.

**Push is in neither place.** It runs after every /next and at any /done — a
standing condition Claude has to notice, not a word the user says — so it stays
in `CLAUDE.md` where it is always loaded. The three-way framing (rezip vs push
vs release) and the on-request rule stay there too, because knowing *which*
action is being asked for has to happen before either definition is opened.

## Recovering from a project-folder move

Moving this project folder breaks two path-based links that both hold absolute
paths and don't self-heal — fix both, then fully restart the app:

1. **Local-directory marketplace.** The desktop app's marketplace registration
   keeps pointing at the old path: slash commands stop autocompleting and get
   flagged "invalid" (the cached snapshot still runs when forced). Re-point it in
   place — `claude plugin marketplace add "<new project path>"` (re-registers the
   path; no `remove` needed) — then
   `claude plugin install throughliner@flintcraft`.

   **Give it the new project path and never the GitHub repository.** The CLI
   silently overwrites a same-name registration, so pointing `flintcraft` at the
   remote would repoint the local marketplace and make every later rezip install
   the *published* plugin while reporting success. The full guard, with its
   evidence, is in `CLAUDE.md`'s Rezip bullet and in
   `workshop/resources/research/marketplace-name-collision.md`.
2. **Git worktree, if this checkout is one.** A move severs the worktree link both
   ways and git reports "not a repository" until both sides are repointed: this
   worktree's `.git` file (the `gitdir:` pointer) and the main repo's
   `worktrees/<name>/gitdir` back-reference. Check whether this checkout is a
   worktree before assuming it is — the `queue-redesign` worktree this note was
   written for has since been merged away.

Consumers are unaffected — they install from the GitHub marketplace, which has no
local path to break.
