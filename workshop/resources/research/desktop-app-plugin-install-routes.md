# Installing a plugin from a third-party marketplace in the Claude Code desktop app — the CLI commands do not exist there, the app has its own Add marketplace option

Filed 2026-09-02, from a web search and the user's own screenshot while processing [install-route-assumes-cli-present].

## What was found

- The `/plugin` slash command, and with it `claude plugin marketplace add` and `claude plugin install`, exist only in the terminal CLI. The desktop app does not register `/plugin` (anthropics/claude-code#42142, where Claude is reported to hallucinate about this).
- The desktop app has its own plugin surface. Seen by the user on 2026-09-02 under Settings → Customise → Plugins → the Add button at the top right: **Add marketplace**, **Upload plugin**, and **Create with Claude**. So a marketplace can be added from the app without any CLI.
- When Claude Code is installed, the official Anthropic marketplace is present by default; third-party marketplaces are added by the user.
- Not yet read: what the Add marketplace field accepts (`owner/repo#branch` as the CLI takes, or a URL) and what the app shows after adding — [desktop-add-marketplace-verified] makes that read on a second machine, because this machine's local marketplace shares the name the published one would take and the CLI is known to overwrite a same-name registration silently (`marketplace-name-collision.md`).

## What it settles

The install guide's plugin branch, which has Claude Code run the two CLI commands, rests on a false premise for a desktop-only beginner. The route is the app's own Add marketplace option, with the CLI commands as the fallback for people who have the CLI. It also falsifies this project's CLAUDE.md sentence that the desktop app's in-app plugin upload is gone.

## Frame assessment

- **Time range:** current as of the search and the screenshot; the desktop app's plugin surface is new and moving.
- **People:** applies to every desktop-app consumer, which is the audience the install guide is written for.
- **Freshness:** amended on the desktop app's release cadence; re-check the menu path before quoting it in a post.
- **Risk if wrong:** a guide naming a menu that has moved sends a beginner looking for something that is not there — the invented-affordance failure; the second-machine read is what guards it.
- **Alternatives:** Upload plugin (a zip) exists on the same menu and was not evaluated as an install route; the nerds-channel zips could use it.

Sources: [Discover and install plugins](https://code.claude.com/docs/en/discover-plugins), [issue #42142](https://github.com/anthropics/claude-code/issues/42142), [issue #52147](https://github.com/anthropics/claude-code/issues/52147); the user's screenshot of the Add menu, 2026-09-02.
