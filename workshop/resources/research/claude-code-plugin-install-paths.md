# Installing a custom/local plugin in Claude Code (desktop app), 2026-06-30

Research prompted by: Alex couldn't find how to add a custom plugin in the desktop app — the pathway had changed and the local-zip upload she used for SI's rezip→reinstall loop appeared gone. This file records what changed, what still works, and the supported path going forward.

## Headline

The desktop app's **in-app local/custom plugin install has been removed**. The supported way to install a non-marketplace plugin is now the **`claude` CLI** (`plugin marketplace add` + `plugin install`), or hosting the plugin as a **GitHub marketplace** and adding that. The capability isn't gone — it moved from a GUI button to the CLI/marketplace model.

## What was confirmed on Alex's build (desktop app)

- The Plugins area's **"+"** (next to "Personal plugins") opens a curated **Directory** with three tabs — **Anthropic / Partners / Code** — that is browse-and-install only. No "upload a file" and no "add marketplace" affordance anywhere in that UI.
- There is **no `/plugin` command** in the desktop app: typing `/plugin` only fuzzy-matches skill names (e.g. `cowork-plugin-customizer`), not a plugin manager.
- Fossils of the old flow remain in `~/.claude/plugins/known_marketplaces.json`:
  - `local-desktop-app-uploads` — the staging marketplace the removed "upload plugin" button used (lastUpdated 2026-05-24).
  - `sovereign-implementer` — a `directory`-source marketplace pointing at `C:\Users\Alex\Desktop\Taskflow Planning\No code method\sovereign-implementer`, a folder that **no longer exists** (the plugin actually lives at `plugin\si-plugin`). Stale/broken.
- `installed_plugins.json` holds only the six official plugins (pyright-lsp, code-review, claude-md-management, feature-dev, code-simplifier, commit-commands), all `@claude-plugins-official`. SI is not currently installed.

## What still works (the path forward)

- The **`claude` CLI is installed**: `C:\Users\Alex\.local\bin\claude.exe`. Relevant commands (from `claude plugin --help` on this build):
  - `claude plugin marketplace add <source>` — source is a URL, local path, or GitHub `owner/repo`.
  - `claude plugin install <plugin>` (or `<plugin>@<marketplace>`), `uninstall`, `update`, `list`, `enable`, `disable`, `validate <path>`.
  - `claude plugin marketplace list | remove | update`.
- The CLI writes to the same `~/.claude/plugins/` config the **desktop app reads**, so a CLI install surfaces in the desktop app's Personal plugins **after a full app restart**. (Plugin components register at launch, not per session.)
- A **local-folder marketplace** requires a `marketplace.json` catalogue (schema `https://anthropic.com/claude-code/marketplace.schema.json`): top-level `name`, `owner`, `plugins[]`, each plugin a `name` + `source` (a relative path like `./si-plugin` for a local plugin, or a git source for a remote one). **Correction (2026-06-30): the SI repo DOES already have a committed `marketplace.json` at the repo root (`.claude-plugin/marketplace.json`)** — marketplace `flintcraft`, owner `FlintCraftTech`, one plugin `sovereign-implementer` with `source: ./plugin/si-plugin`. The earlier "no marketplace.json yet" note was wrong; the install path was ready to use without any new build.
- `claude --plugin-dir <dir|zip>` loads a plugin for one **CLI** session only (zip needs v2.1.128+); `--plugin-url <zip-url>` likewise. These are CLI-session-scoped, not desktop installs.

## Implication for SI's two install needs

- **Local test loop (rezip dogfooding):** point a local-folder marketplace at the working tree's `plugin/si-plugin` (via a `marketplace.json`), `marketplace add` + `install` through the CLI, restart the app. Claude can drive the CLI so the user types nothing. **Confirmed 2026-06-30: install SNAPSHOTS the plugin into `~/.claude/plugins/cache/<marketplace>/<plugin>/<version>` (with a `gitCommitSha`), it does NOT read the live working tree.** So the cache is frozen at install time — after each rezip you must re-run `claude plugin install` (or `update`) to refresh the snapshot, then restart the app. A bare working-tree edit alone changes nothing the host sees.
- **Released install (consumers):** host the marketplace.json in the GitHub repo so `claude plugin marketplace add FlintCraftTech/sovereign-implementer` + `install` works. This is the [publish-marketplace-manifest] deferred item. Note consumers on the desktop app face the same no-GUI-install constraint, so INSTALL.md must teach the CLI/marketplace path, not the old upload button.

## Not targeted, despite how it feels

The removal reads as a platform consolidating distribution around curated marketplaces (curation, security, support load), and pulling a GUI that uploads arbitrary code is a routine safety move. The CLI path and self-publishing via a personal GitHub marketplace remain fully open — the opposite of locking self-distributors out. The real cost is a relied-on workflow removed without warning, which lands hardest on non-coders.

## Sources

- [Use plugins in Claude — Anthropic Help Center](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)
- [Discover and install plugins — Claude Code Docs](https://code.claude.com/docs/en/discover-plugins)
- [Create plugins — Claude Code Docs](https://code.claude.com/docs/en/plugins)
- [Create and distribute a plugin marketplace — Claude Code Docs](https://code.claude.com/docs/en/plugin-marketplaces)
- [Issue #52147 — local plugin installation in the desktop app (April 2026, since outdated)](https://github.com/anthropics/claude-code/issues/52147)
- Local evidence: `~/.claude/plugins/known_marketplaces.json`, `installed_plugins.json`, and `claude plugin --help` on Alex's build (2026-06-30).
