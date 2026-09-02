# How Claude Code runs hook commands on Windows — in flux, so no interpreter fallback yet

Filed 2026-09-02, from a web search made while processing [hooks-silent-under-python-stub], to decide whether the hook command lines could try `py` before `python`.

## What was found

- A `command` hook runs a shell command and talks JSON over stdin/stdout with an exit code; hooks carry an optional timeout.
- On Windows, Claude Code has run hook commands through Git Bash; a PowerShell backend for command execution on Windows has been introduced as a new default for Windows users. Which one a given install uses for hooks is therefore not stable across versions.
- Cross-platform advice from the community is to invoke hooks with `node`, which Claude Code requires on every platform, rather than with a shell-specific line; shell-specific commands (bash, cmd, powershell, sh) break on other platforms.
- Two Windows-specific silent-failure causes are reported: `.sh` hook scripts opening in an editor instead of executing (anthropics/claude-code#21847), and CRLF line endings in hook scripts.

## What it settles

A fallback of the shape "try `py`, then `python`" depends on shell syntax (`||` in bash, different in PowerShell), so a line that works in one shell and not the other would reproduce the silent failure it is meant to remove. The change waits on reading, at build time, which shell the current Claude Code invokes hooks with on Windows, and on a run on a second Windows machine — recorded on [hook-interpreter-fallback-on-windows].

## Frame assessment

- **Time range:** current as of the search date; the PowerShell backend is recent and the situation is expected to change.
- **People:** applies to every Windows consumer of the plugin; Mac and Linux are unaffected.
- **Freshness:** amended on Claude Code's release cadence — re-read the hooks docs before any change to the command lines.
- **Risk if wrong:** a wrong fallback line silently kills all four hooks on some Windows installs, the exact failure the tester hit; that is why nothing is changed on this finding alone.
- **Alternatives:** a `node` launcher that picks the interpreter was seen in the community advice and not evaluated; it would add a runtime the hooks do not currently use.

Sources: [Claude Code hooks guide](https://code.claude.com/docs/en/hooks-guide), [Cross-platform hooks](https://claudefa.st/blog/tools/hooks/cross-platform-hooks), [PowerShell tool on Windows](https://claudcod.com/blog/claude-code-windows-powershell/), [issue #21847](https://github.com/anthropics/claude-code/issues/21847).
