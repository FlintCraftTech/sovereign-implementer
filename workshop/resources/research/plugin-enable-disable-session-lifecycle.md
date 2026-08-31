# Claude Code plugin enable/disable — when does it take effect?

**Question:** When you toggle a Claude Code plugin on or off, does it take effect in the running session, or only in a new one? (Raised 2026-06-19 from the goal-session-ran-with-plugin-active observation.)

**Finding (web search, 2026-06-19):** Plugin component changes — `hooks/`, `.mcp.json`, `agents/`, `output-styles/` — do **not** take effect immediately within a running session. To apply them you must run `/reload-plugins` or restart Claude Code. In cloud sessions `/reload-plugins` is disabled, so you must end the session and open a new one for everything (including hooks) to apply. An open bug ([#35713](https://github.com/anthropics/claude-code/issues/35713)) reports that *disabled* plugins still inject context via SessionStart / UserPromptSubmit hooks — direct corroboration that disabling a plugin does not immediately stop its hooks.

**The mirror holds.** Just as enabling a plugin mid-session doesn't activate it until a fresh session, **disabling it doesn't deactivate its hooks until a `/reload-plugins` or a restart / new session.** Disabling alone, mid-session, leaves the hooks firing — exactly what the 2026-06-18 goal session observed (the post_tool_use lint kept firing despite the run being intended as "plugin off").

**Implication for SI's goal-session model.** To run a goal session "with the plugin off," the user must disable the plugin **and start a fresh session** — not just disable it mid-session. On the desktop app the reliable path is a **full app restart** (fully quit and relaunch), because `/reload-plugins` is a TUI/CLI command the desktop app doesn't expose, and on Windows a normal quit can leave the app running (same caveat as the reinstall step in CLAUDE.md).

**Sources:**
- [Plugins reference — Claude Code Docs](https://code.claude.com/docs/en/plugins-reference)
- [Issue #35713 — Disabled plugins still inject context via SessionStart and UserPromptSubmit hooks](https://github.com/anthropics/claude-code/issues/35713)
- [Issue #63028 — declared plugins inactive on first session, require restart to fully load](https://github.com/anthropics/claude-code/issues/63028)
