# Output styles: plugin shipping and force-for-plugin (verified 2026-08-22)

**Superseded by: the 2026-08-26 repeal of the style-dedup policy (SPEC's output-style paragraph)** — only the "Informs" line's parent-axis-deduplication reasoning falls: it holds for a layer that always applies and fails for a consent-gated style, where evicting a rule from the docs ungoverns every project that declined the style. The factual findings above all still stand.

Source: https://code.claude.com/docs/en/output-styles (official Claude Code docs, fetched 2026-08-22). Verifies the claims in the 2026-08-21 INBOX message from another of the user's projects; all held.

- Plugins can ship output styles in an `output-styles/` directory.
- Frontmatter `force-for-plugin: true` (plugin styles only) applies the style automatically whenever the plugin is enabled, without the user selecting it, **overriding the user's `outputStyle` setting**. If multiple enabled plugins set it, the first plugin loaded wins.
- `keep-coding-instructions: true` keeps Claude Code's built-in software-engineering instructions; default is `false` (they are dropped).
- Styles modify the system prompt directly and trigger in-conversation adherence reminders. They apply to the **main conversation only** — subagents run their own system prompt (a conversation fork is the exception).
- Changes take effect only after `/clear` or a new session; the system prompt is read once at session start.
- A built-in **Concise** style exists (Claude Code v2.1.237+): leads with the result, keeps responses short by default, keeps error reports and destructive-action confirmations in full.
- Precedence context: output styles modify the system prompt and therefore outrank CLAUDE.md content, which arrives as a user message after the system prompt.

Informs: [ship-brevity-output-style] and its follow-up dedup audit — a rule carried at style level sits above the always-loaded rules, so evicting the same rule from the docs below is parent-axis deduplication.
