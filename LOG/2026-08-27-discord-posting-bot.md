# [HASH] — Claude gains a route to Discord: a standard-library bot client, and CLAUDE.md's no-route sentences replaced by the route plus its approval gate

Every Discord post this project has made was copied across by hand. This builds the route: `resources/discord_post.py`, a standard-library client that sends, edits, deletes, lists, attaches files and sets the bot's own avatar against Discord API v10, reading its token from `INBOX/.discord-bot-token.txt`.

**The route is all that changed, and the wording had to make that unmistakable.** The sentences this replaces said Claude has no route to Discord — a statement of fact that was quietly doing a second job as a safeguard, because "cannot" reads like "will not". Only the fact was false. So the replacement states the two separately: the bot reads the channels it has been granted, and **every send is gated by the approval rule — the exact text is shown and needs an explicit yes before anything leaves the machine, and an automated edit is still a send.** A script cannot ask for consent, so the script does not pretend to: it takes a file a human has already approved and sends its exact bytes.

The draft-edit flow is recorded alongside it, from the user's design: a draft goes to a `.txt` file opened in Notepad, she edits and saves, and the script posts that file's exact content on her yes. Her reason, in Claude's words: editing the file directly beats negotiating wording change-by-change in chat.

**Routes were verified against Discord's current documentation before any code was written**, as the item required, and the doc read changed one decision — bulk delete refuses anything older than two weeks, which is exactly the age of the entries the prune exists to remove, so the prune deletes one message at a time instead.

**Two things the design refused.** A hosted always-on bot: nothing here needs to listen, only to send. And any suggestion that per-post manual copying goes away — it stays available whenever the user prefers it.

**One thing built that the item did not name, and one it named that could not be built.** An emoji-tolerant channel resolver was necessary rather than a nicety: every channel on this server is named with a leading emoji, so an exact match on a typed name found nothing, and the alternative was making a human paste emoji into a command line. Against that, the item's instruction to reword queue items still saying "you post" was refused by the scope-lock — correctly, since rewording a queue item's prose is work on the queue's contents, which is planning. Filed as [queue-walkthroughs-say-claude-cannot-post].

**Acceptance was met in a real channel, not a fixture.** During the same session's walk-through pass the bot posted the plain-English consent tip to #tips on the user's explicit yes to the exact text, read back byte-identical and authored by the bot. Auth, channel resolution, reading and `set-avatar` are confirmed live.

**`edit` is unconfirmed and is recorded as unconfirmed.** Exercising it would mean altering a published post purely to prove a code path, which is the same shape as verifying a guard by performing the guarded action for real. It is proven at the first genuine edit, tracked by [bot-edit-path-unproven].

**Files:** `resources/discord_post.py` (created), `CLAUDE.md`.

**Red flag:** none on this item. The token risk was cleared on [discord-bot-server-setup] at an earlier planning session; this build never prints, echoes or commits the token, and the file it reads is outside git.

Rule gate: run — amendment to CLAUDE.md's Discord section (the no-route sentences replaced by the route-plus-approval statement); no new freestanding rule, the send-approval rule unchanged and cited.

Routed to Captures: [queue-walkthroughs-say-claude-cannot-post], [bot-edit-path-unproven], [claude-md-asserted-bot-posting-channels-unchecked]
