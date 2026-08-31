# Claude Code MCP registration — how a local server attaches, and the desktop app's support

**Read 2026-08-31 from the official docs (code.claude.com/docs/en/mcp), for the MCP umbrella's first slice ([mcp-server-standing-intent]).** Read, not tested — nothing has been run against this yet.

## What it settles

- **A project registers a local stdio server in `.mcp.json` at the project root** — shape: `{"mcpServers": {"name": {"command": "...", "args": [...]}}}`. Absolute command path recommended.
- **The desktop app supports project-scoped `.mcp.json`.** One caveat: a same-named server at user scope (`~/.claude.json`) wins over the project file in the Code tab.
- **First use shows a trust dialog.** Until accepted, the server sits at "Pending approval" — so switching the server on needs one human acceptance, once, in an interactive session.
- **A plugin can bundle an MCP server** — either an `.mcp.json` at the plugin root or an `mcpServers` block inline in `plugin.json`, with `${CLAUDE_PLUGIN_ROOT}` resolving paths. Bundled servers connect at session startup and disconnect when the plugin is disabled. Tool names arrive scoped: `mcp__plugin_<plugin>_<server>__<tool>`.
- **Consequence for dogfood-first:** a project `.mcp.json` in this repository reaches this project only — it is not part of the plugin package — so the server can be dogfooded here and promoted later by adding the `mcpServers` block to `plugin.json`, with no change to the server itself.

## Frame assessment

- TIME RANGE: not applicable — current docs describing current behaviour, read the day of use.
- PEOPLE: applies to this project's dogfood directly; consumer behaviour (trust dialog per project) matters at promotion and is covered by the same page.
- FRESHNESS: Claude Code moves fast; re-read at promotion time rather than trusting this file.
- RISK IF WRONG: the first build's observable fails visibly (tools never appear) — cheap to detect, no data risk.
- ALTERNATIVES: user-scope registration (`~/.claude.json`) noted and not chosen — it is per-machine, invisible to the repo, and its same-name precedence over the project file is a footgun; plugin-bundled registration deferred to promotion deliberately.
