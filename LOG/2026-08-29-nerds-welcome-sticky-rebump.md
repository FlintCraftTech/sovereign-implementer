# 819f7f1 — The nerds-channel welcome becomes a source file the bot re-bumps to the bottom

Discord opens a channel at the bottom, so a pinned welcome sits where it is least likely to be read. There is no native bottom-pin; the universal pattern is a sticky message a bot re-posts as the newest message. This bot has no always-running process and cannot react to other people's messages — but that channel's traffic is almost entirely the bot's own, so re-bumping at each entry post keeps the welcome at the bottom exactly when anyone looks.

The welcome text was **read off the live channel rather than retyped**, so the source file carries the user's own wording byte for byte rather than a paraphrase of it. The re-bump deletes the bot's own previous copy first and posts after, so the channel never briefly shows two, and it matches on author id *and* content — the existing pin, her posts and every entry are untouchable by construction rather than by ordering luck, which is the guard the prune already takes.

It runs last in the posting step, after any prune, so the welcome ends up newest whatever else that run did. The two need no coordination: a prune that removed an older copy simply leaves nothing for the re-bump to delete.

The consent boundary is recorded in the script itself, since a script cannot enforce it: the user's yes to posting an entry covers re-bumping the welcome's unchanged bytes, and any change to the welcome text is a new send needing its own explicit yes.

Tick: done, UNCONFIRMED: the observable — that after an entry post the channel's newest message is the bot-authored welcome, byte-identical to the source file — cannot be checked until an entry is posted, which is a send needing the user's yes. The route is built and its command line verified.

Depth: short.

**Files touched:** `resources/nerds-welcome.md` (created), `resources/discord_post.py`.

**Routed to Captures:** none. [nerds-old-pin-retired] is held on this item and its blocker has now shipped; lifting is planning work and nothing was changed here.
