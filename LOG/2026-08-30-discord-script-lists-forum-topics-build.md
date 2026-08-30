# [HASH] — Posting bot gains a `threads` command listing open forum topics

Filed on 2026-08-29 by /next while building forum-topic creation, as adjacent work rather than part of it. `active_threads()` existed inside the script and worked live — it had returned the server's eight open topics — but nothing exposed it on the command line, so a session needing the list wrote a throwaway `python -c` against the module, which is the shape this project's tooling rules push work away from.

Two pieces of standing work need exactly that list: the announced-claims sweep reads each forum's topic order every turn and reports where it no longer matches the numbers in the titles, and the how-to re-homing reads where a topic sits after each post.

Exposure of an existing working function rather than new capability, so it is live the moment it is written. Grouped by parent forum in the output, which the underlying function does not do — a flat list of topic ids answers neither of the two consumers without further work.

**Observable met:** the subcommand prints each open topic's id and name grouped by forum, returning the six how-to topics plus the announcements thread and the port-showcase topic.

It was used twice within the hour — by the permissions audit, and by the how-to walk-through.

**Depth:** short.
**Files touched:** `resources/discord_post.py` — shared with [bot-cannot-read-permissions] and built adjacently, each reading the file as it found it.
**Routed to Captures:** none from this item.
