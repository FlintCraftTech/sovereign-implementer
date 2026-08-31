# Claude Code plugin install mechanisms (CLI / desktop / agent)

Filed 2026-06-14, during the /plan discussion of a "let Claude Code install the plugin for you" INSTALL.md/README pathway.

## Question

For repo visitors who already have Claude Code, can Claude Code install the SI plugin itself via the terminal — and does that work in the desktop app, not only the CLI?

## Findings (from code.claude.com/docs)

**The desktop app is Claude Code with an integrated terminal.** The desktop app's "Code" tab is Claude Code. The app ships an integrated terminal and file editor, and CLI/desktop have plugin parity — a plugin installed one way works the other. So a desktop user does have terminal access to Claude Code, and the agent can run shell commands. This confirms the user's "the desktop app is an approachable surface over what is basically a CLI tool" model.
Source: https://code.claude.com/docs/en/desktop

**Interactive vs non-interactive surfaces.**
- The interactive `/plugin` slash menu is CLI-only — it is not available in the desktop app. (Matches the existing project note in CLAUDE.md.)
- But non-interactive CLI subcommands exist and are agent/script runnable:
  - `claude plugin install <name>@<marketplace> [--scope user|project|local]`
  - `claude plugin uninstall ...`, `claude plugin details`, `claude plugin list`
  - marketplace management: `/plugin marketplace add owner/repo` with CLI equivalents
- settings.json path: register a marketplace via `extraKnownMarketplaces` and enable plugins via `enabledPlugins` in `.claude/settings.json`. Agent-editable. Example:
  ```json
  {
    "extraKnownMarketplaces": {
      "my-team-tools": { "source": { "source": "github", "repo": "your-org/claude-plugins" } }
    }
  }
  ```

**The clean agent path needs a marketplace.** `claude plugin install` installs FROM a registered marketplace. A marketplace is a git repo (or local path / URL) containing `.claude-plugin/marketplace.json`. The sequence:
1. `claude plugin marketplace add FlintCraftTech/sovereign-implementer` (requires a marketplace.json in that repo)
2. `claude plugin install <plugin-name>@<marketplace-name>`
3. `/reload-plugins` (or restart) to activate
Source: https://code.claude.com/docs/en/discover-plugins

**Prerequisite gap for SI:** the SI repo has NO marketplace manifest. Local check on 2026-06-14: only `plugin/si-plugin/.claude-plugin/plugin.json` exists; no `marketplace.json` anywhere. The desktop GUI upload works because the app synthesizes a local marketplace wrapper around the uploaded zip — visible in the installed host path `.../plugins/marketplaces/local-desktop-app-uploads/sovereign-implementer/`. For the CLI/agent path to work cleanly, the repo must publish a `.claude-plugin/marketplace.json` pointing at si-plugin.

**Local (non-marketplace) install from a raw zip is the flaky path.** Installing a plugin from a downloaded local zip/folder in the desktop app is an open feature request (anthropics/claude-code Issue #52147). So "point the agent at the downloaded zip" is not reliable; "add a marketplace manifest and install from it" is the robust route.

## Design implication

The user's reframing is right: the axis is "who does the installing," not "which app they use."
- Human + desktop GUI: already documented (Customise → Create a plugin → upload zip).
- Claude Code (agent) via terminal: works in the CLI and in the desktop app's integrated terminal — BUT requires a published marketplace manifest first. That is a prerequisite build before the self-install pathway can be written, and it is arguably an upgrade to the whole install story (standard `marketplace add` + `install`, instead of the GUI zip-upload dance the current INSTALL.md batches are wrestling with).

## Sources
- https://code.claude.com/docs/en/discover-plugins
- https://code.claude.com/docs/en/desktop
- https://github.com/anthropics/claude-code/issues/52147
