# [HASH] — The posting script can create forum topics, and can address an existing one by name

A forum channel holds threads rather than messages, so posting to its `/messages` route returned HTTP 400 code 50008 — found by trying, on 2026-08-29, while attempting to post the showcase guidelines. Creating a topic is a different call that carries a title, and the script had no parameter for one. `send` gained `--title`, which routes to `POST /channels/{id}/threads` with the body as the topic's opening message.

The item's second half asked whether posting *into* an existing topic works through the current `send`. It does, and needs no new route at all: a thread's own id is a channel id. What was actually missing was a way to name one, since the guild channel listing does not include threads — so channel resolution now falls back to the guild's open threads, searched only when no channel matches, which keeps a topic from shadowing a channel of the same name. Archived threads are deliberately not fetched: that is a per-channel route rather than a per-guild one, so reaching it would cost a call per channel on every name lookup, and a quiet topic is addressed by its id instead.

Tick: done, UNCONFIRMED: the topic-creation POST has not run live, because posting to the forum is a send and needs the user's explicit yes to the exact text. Thread resolution IS confirmed live — `active_threads()` returned the server's eight open topics.

**Confirmed later the same session, after this tick was written.** The walk-through of [howto-posts-bot-authorship] created a real topic through this route — id `1543081212803940402` — so the unconfirmed half is now confirmed. The tick is transcribed as it stood and the correction recorded beside it rather than rewritten, since the tick records what was true when the item completed.

Depth: short.

**Files touched:** `resources/discord_post.py`.

**Routed to Captures:** [discord-script-lists-forum-topics] — `active_threads()` now exists and works, and nothing exposes it on the command line, which two pieces of standing work need.
