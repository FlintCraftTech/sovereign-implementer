# [HASH] — Posting bot gains a read-only permissions command

Filed by /rescan at the end of the 2026-08-29 planning session, where it came up and was left hanging: the user asked for a review of the server's permissions after a member accidentally edited a forum's guidelines, and nothing in this project could answer it. Everything said about Discord permissions that day came from Discord's documentation rather than from her server.

The script already sent, edited, listed, pruned, read replies and set an avatar, and held a token that would permit a read-only query of roles and channel overwrites. It had no command for either.

Two things it buys, and the second is the general one. A permission question becomes answerable instead of being handed back as a GUI walk-through, which the always-loaded CLI-tool rule says to reach for a tool before doing. And a capability claim about a channel becomes checkable *before* acting on it rather than after — the same session had posted to a forum to discover the bot could not, and read a channel to discover it was empty.

Two choices inside the build worth recording. The notable permission bits are named and the raw bitfield printed alongside, so a flag outside the named set is still visible as a number rather than hidden by the summary. And **a member-specific overwrite is reported by id only**: resolving it to a person would put a name into output this project commits, which the scrub checklist bars.

The output also states what it cannot do, because a listing invites over-reading: it reports what is granted and denied, and does not compute any member's effective permissions.

**Observable met:** the subcommand returns the server's roles and per-channel overwrites; nothing on the server changed. Live, since dev-side scripts run directly.

**Depth:** short.
**Files touched:** `resources/discord_post.py`.
**Routed to Captures:** none from this item — the findings belong to the audit that read its output.
