# [HASH] — plan — the bot gains a read-only permissions command, and the audit that runs the user's review is filed beside it

The hanging question from 2026-08-29 — a member accidentally edited a forum's guidelines and nothing here could review the server's permissions — becomes answerable: `discord_post.py` gains a `permissions` subcommand printing the guild's roles and each channel's overwrites, a pure read, live the moment it is written since dev scripts run directly. The tool-then-audit rule fired at the keep: [discord-permissions-review] is the `[audit]` that runs the review, placed immediately after its tool by the placement exception, reporting what `@everyone` and `@Throughliner expert` can actually do and filing one capture per surprise; any permission change stays the user's, in Discord.

**Queue changes:** [bot-cannot-read-permissions] kept and cleared; [discord-permissions-review] filed and cleared immediately after it.
**Work processed:** kept — both.
