# Plugin/marketplace rename migration — how a Throughliner rename reaches existing consumers

Researched 2026-07-31 (web + official Claude Code docs) for [rename-to-throughliner]'s gating open question: does renaming the repo/slug orphan already-adopted consumers, and is big-bang vs. a transition path the right call?

## Two independent rename surfaces

**1. The GitHub repo rename** (`FlintCraftTech/sovereign-implementer` → `.../throughliner`).
- GitHub 301-redirects the old repo URL, and `git clone` / `fetch` / `push` continue to work through the redirect. So an existing consumer's `marketplace add FlintCraftTech/sovereign-implementer` registration keeps resolving after the rename — the underlying clone follows the redirect.
- **Caveat:** never create a *new* repo reusing the old name, or the redirect breaks. (Also: GitHub does not redirect Actions calls — irrelevant here, no Actions in the install path.)

**2. The plugin `name`/slug rename** (`sovereign-implementer` → `throughliner`), inside `marketplace.json`.
- Official mechanism: a top-level **`renames`** map in `marketplace.json` — maps a former plugin `name` to its current name (or `null` if removed). **Requires Claude Code v2.1.193+.**
- On next session with the old name in settings, Claude Code follows the map, loads the plugin under its new name, shows a one-line notice ("Renamed to …"), and **auto-rewrites** the old key → new key in user/project/local settings (`enabledPlugins`, `pluginConfigs`). Notice appears once.
- **BUT for a `github` remote source, Claude reports `plugin-cache-miss` after the rename, and the user must run `/plugin install` once** to fetch under the new name. So it is NOT zero-touch — one reinstall per consumer.
- `renames` is **append-only history**: keep old entries forever; Claude follows chains across successive renames.
- **Limits:** Claude Code < 2.1.193 ignores `renames` and reports `plugin-not-found`. Managed/policy-enabled settings are read-only, so the auto-rewrite can't fire there — the notice recurs until an admin updates the managed settings.

## Bottom line for the decision

Big-bang rename is feasible and reasonably soft, using both mechanisms together:
- Repo rename → GitHub redirect keeps old marketplace registrations resolving.
- Slug rename → `renames` map auto-migrates settings; each consumer runs `/plugin install` **once** (github remote → cache-miss).

Net consumer cost: one `/plugin install`, on Claude Code ≥ 2.1.193. Not an orphaning event, not a prolonged transition apparatus. This argues **big-bang + `renames` map**, not a hand-rolled transition path.

## Sources
- GitHub repo-rename redirect behavior (git operations continue through redirect; don't reuse old name): GitHub Docs "Renaming a repository"; GitHub Blog "Repository redirects are here!"
- `renames` map, `plugin-cache-miss`, append-only chains, v2.1.193 requirement, managed-settings caveat: Claude Code docs, "Create and distribute a plugin marketplace" → "Rename or remove a plugin" (code.claude.com/docs/en/plugin-marketplaces).
