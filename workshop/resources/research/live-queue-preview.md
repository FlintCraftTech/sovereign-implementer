# Live preview of QUEUE.md (and other project docs)

**Superseded in part by Understudy** — the user reported on 2026-08-15 that Understudy now live-renders a file as it changes on disk. What falls is this file's *conclusion*: that no live preview is available and the want is unmet pending an Anthropic fix. What still stands is the finding itself — the desktop app's own Files panel does not auto-refresh, which is untouched by anything outside the app. **Do not cite this file as evidence that live rendering is unavailable.**

Researched 2026-06-03. Context: Alex wants a live or near-live rendered preview of QUEUE.md while working in the Claude Code desktop app. The app's Files panel shows a preview when you click a file, but it does not auto-refresh — you have to click away and click back (or re-open the file) to see changes.

## Root cause: this is a known, unfixed limitation

The desktop app's Files panel renders a file when clicked but does **not** live-update as the file changes on disk. This is filed as a feature request, not a bug with a workaround inside the app:

- **GitHub issue #60432** — "[FEATURE] Desktop App: Add live Markdown preview in Files panel" (opened 2026-05-19). Requests that the Files panel render .md as formatted HTML and update in real-time on file save/change, ideally with a raw/rendered toggle. As of this research it is an open enhancement request, not shipped.

So there is no in-app setting that makes the preview auto-refresh. The click-away-click-back dance is currently the only native way to force a refresh.

## Workaround options (ranked for a non-coder on Windows)

### 1. mdserve — most workflow-native
A Markdown preview server built for AI coding agents. Launches a local web server that renders markdown to auto-updating HTML in the browser, with real-time updates as the file changes, Mermaid diagram support, and a directory mode that serves all .md files with a navigation sidebar (so QUEUE.md, SPEC.md, REGISTRY.md, LOG/ could all be live in one browser tab).

- Ships as a **Claude Code plugin** with a `/mdserve` skill — once installed, Claude Code knows when to serve markdown and when not to.
- Usage: `mdserve QUEUE.md` (single file) or `mdserve .` (whole project, with sidebar).
- **Windows install caveat:** documented installs are `brew` (macOS), a `curl` script (Linux), and `cargo install mdserve` (cross-platform but requires the Rust toolchain). Prebuilt binaries are published on the GitHub releases page — a Windows binary is *likely* available there but was not confirmed in this research. **Verify on the releases page before committing.** If there's a Windows `.exe`, that's the no-toolchain path; if not, it needs Rust installed (friction for a non-coder).
- Source: https://github.com/jfernandez/mdserve  ·  releases: https://github.com/jfernandez/mdserve/releases

### 2. A standalone live-preview server
`ComotionLabs/markdown-live-preview` — a live markdown preview server with auto-reload and real-time rendering. Same idea as mdserve (browser tab that auto-refreshes), without the Claude Code plugin integration.

### 3. VS Code's built-in preview
Open the file in VS Code and use the Markdown preview (Ctrl+Shift+V). It auto-refreshes via a file-change subscription. **Caveat:** on Windows, some external writes don't always trigger VS Code's file watcher, so it can occasionally go stale the same way — though far less often than the desktop app. Only worth it if VS Code is already in the workflow. Extensions like "Markdown & HTML Live Preview" and "Instant Markdown" preview in a browser with auto-reload.

### 4. A watching editor (Typora)
Cross-platform markdown editor for Windows. Reloads on external change, but behavior varies and it's an editor (risk of accidental edits to a file Claude owns). Marked 2 is mentioned in the community but is macOS-only — not relevant here.

## Recommendation

For Alex's setup (non-coder, Windows, desktop app), the best fit is **mdserve in directory mode** — one browser tab showing all project docs, auto-updating as Claude writes them — *if* a Windows binary exists on the releases page (no Rust toolchain needed). If it doesn't, the simplest fallback is VS Code's preview, accepting its occasional Windows file-watcher staleness. Either way, the desktop app's own Files panel will not auto-refresh until issue #60432 ships.

## Sources

- [Issue #60432 — Live Markdown preview in Files panel](https://github.com/anthropics/claude-code/issues/60432)
- [mdserve on GitHub](https://github.com/jfernandez/mdserve)
- [Markdown Live Preview skill (mdserve) — MCP Market](https://mcpmarket.com/tools/skills/markdown-live-preview)
- [ComotionLabs/markdown-live-preview](https://github.com/ComotionLabs/markdown-live-preview)
- [Markdown and Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown)
