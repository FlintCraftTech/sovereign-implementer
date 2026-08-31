# Claude Code plugin install/update mechanism (checked 2026-07-01)

Question: after recent Claude Code updates, do plugins run live from GitHub, or is the reinstall-and-restart loop still needed?

## Finding: still a cached snapshot, not live

- On install, Claude Code copies the plugin into the local cache (`~/.claude/plugins/cache/...`) and runs that copy. It does **not** re-fetch from source each session. Republishing the plugin does not change what's running — the cache is a snapshot written at install time.
- Each installed version is its own directory in the cache. On update/uninstall, the previous version directory is marked orphaned and auto-removed ~7 days later (grace period so concurrent sessions that loaded the old version keep working).
- Version is the cache key: resolved from the plugin source's git commit SHA (for github / url / git-subdir / relative-path sources in a git-hosted marketplace); "unknown" for npm sources or local directories not inside a git repo. An update is skipped if the computed version matches what's installed.

## What is new (the "runs from GitHub" impression)

- Claude Code now runs a lightweight update **check**: it compares each installed plugin's gitCommitSha (from installed_plugins.json) against the remote HEAD of its marketplace repo, caching the last-check timestamp to avoid a network call every session start. There is an auto-update path for GitHub-sourced marketplace plugins.
- This is a check-and-fetch, not live execution: the code that runs is still the cached snapshot after an update is pulled.

## Implications for this project

1. Local dogfooding (Rezip) uses a **local-folder** marketplace (`flintcraft`), not the GitHub repo. The remote-check/auto-update only applies to GitHub-sourced installs, so the local Rezip → reinstall → full restart loop is unchanged and still required to test a build.
2. Full app restart still required after an update lands: skills register at app launch, so a cache update alone does not load them.
3. The Rezip/Push rituals in CLAUDE.md remain valid. Candidate future simplification: the Push ritual's manual "update the host" step for the *published* GitHub version might be able to lean on auto-update — a design question, not decided.

## Sources
- https://code.claude.com/docs/en/plugins-reference
- https://github.com/anthropics/claude-code/issues/15642
- https://github.com/anthropics/claude-code/issues/31462
