# beac9d2 — The posting bot prunes its own old test-rezips entries, under four bounds that make the pin and other members' posts unreachable

Pruning the nerds list was a by-hand job. It now runs in the same pass as each new entry. The route and its reasoning are in this session's entry for [discord-posting-bot]; this records only what the prune adds.

**Four bounds, all of them settled at planning and transcribed here rather than designed.**

- Keep the newest **15** entries — the user's figure, given at processing.
- Delete only messages **the bot itself authored**, checked per message against the author id.
- Skip **pinned** messages explicitly.
- On any error partway, **stop and report, with no retries.**

**The author check and the pin check overlap deliberately, and that is the point.** Either alone would protect the pin; together the pin survives even if the other is later changed. The author bound is what makes the user's posts and other members' posts unreachable **by construction rather than by ordering luck** — the refused alternative was pruning by position or count with no author check, which is precisely what could reach them.

**The author bound costs the workflow nothing**, because nobody can edit anyone else's Discord message anyway: a pre-post edit happens in the draft file, and a post-post correction is the bot editing its own message. **One cost is real and stated:** entries posted by hand before the bot existed can never be pruned or edited by it, and get cleaned up by hand once.

**Stop-on-error needs no recovery path**, which is why it has none: leftover old entries are simply picked up by the next post's prune.

**Verified against the live channel without deleting anything.** `prune --dry-run` on test-rezips-for-nerds reported zero candidates — correct, because all three entries there are the user's own. A zero that proves the author bound is working is a better first test than one that deletes something.

Bulk delete was refused on a fact read from Discord's documentation rather than assumed: the route rejects anything older than two weeks, and entries this prunes are older than that by definition.

**Files:** `resources/discord_post.py`.

**Red flag:** carried one, **cleared** at planning — designed out by the four bounds above. The residue recorded there and repeated here: `Manage Messages` stays granted to the bot, which the user consented to on [discord-bot-server-setup].

Rule gate: not needed — a script addition under bounds settled at planning; no rule authored, amended or repealed.
