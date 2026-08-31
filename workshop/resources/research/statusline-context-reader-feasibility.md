# status-line context-% reader — feasibility of the mechanism

Researched 2026-07-31 (web + official Claude Code docs) for [statusline-context-reader]: can a status-line command surface context-% to a file that /next reads?

## Confirmed — the mechanism exists in Claude Code

- Claude Code supports a **custom status-line command** (`statusLine` in settings.json, or the `/statusline` guided setup). Claude Code pipes a JSON object to the script via stdin on every status-bar update.
- That JSON carries a **`context_window`** object with `total_input_tokens`, `total_output_tokens`, `context_window_size`, **`used_percentage`**, **`remaining_percentage`**, `current_usage`. Anthropic announced context-window info in the status line directly. So the field the item needs is real and documented.
- The script can output any string it computes — and, as a side effect, could write the % to a file for /next to read. The status line updates "every time the conversation changes."

## Two serious caveats

**1. `used_percentage` understates real usage — and worst for SI.** Per anthropics/claude-code issue #17959, `used_percentage` / `remaining_percentage` exclude system overhead: **tool definitions, CLAUDE.md files, MCP server configs, and the system prompt.** So the reported % reads *lower* than Claude Code's own "Context low" warning. This matters acutely here: SI loads a large plugin-behaviour.md (~15k tokens) + CLAUDE.md + tool defs that this field ignores — so a naive "wrap at 40% used_percentage" would fire far later than real context pressure. Any threshold must offset for the excluded overhead, or the sizing is systematically too loose.
- Also: `used_percentage` may be **null early in the session** (handle with a fallback).

**2. The desktop-app gate is NOT resolved by search.** All documented usage is the Claude Code CLI. Whether the **desktop app** (Alex's environment) runs a custom `statusLine` command at all — and if so, what shell runs it on Windows and whether the file-write side effect lands with usable freshness — is not answerable from public sources. The desktop app is known to differ from the CLI (no `--plugin-dir`, no `/plugin` CLI commands). This is the true remaining gate and is resolvable only by a **live test**: set a `statusLine` command in settings.json and observe whether the desktop app renders/runs it, then whether the file gets written.

## Bottom line for the decision

Not deletable — the mechanism is real and is the sole context-% surface (hooks stay blind). Not yet buildable — gated on (a) a live desktop-app test that the statusLine command runs and writes a file on Windows, and (b) a threshold design that offsets the used_percentage undercount. Both must clear before the reader is built.

## Sources
- Status line + context_window fields: Claude Code docs "Customize your status line" (code.claude.com/docs/en/statusline); Anthropic status-line context-window announcement.
- used_percentage excludes system overhead / mismatch with internal warning: anthropics/claude-code issue #17959.
