# [HASH] — [audit] Discord permissions review: five findings, one red-flagged

The review the user asked for on 2026-08-29, after a member accidentally edited a forum's guidelines and nothing in this project could answer how. Filed alongside the tool that makes it possible, per the tool-then-audit rule: the tool is the build, reading its output is the audit.

**The question that started it has an answer, and it is the red-flagged finding.** The `Throughliner Expert` role holds `ADMINISTRATOR` at the guild level, alongside `MANAGE_CHANNELS`, `MANAGE_GUILD` and `MANAGE_ROLES`. Editing a forum's guidelines is a channel-settings change, and this role can do that plus rename or delete any channel. Discord documents `ADMINISTRATOR` as bypassing every channel overwrite, which means the how-to forum's careful narrow grant to that same role restrains nobody holding it — a grant that reads as a restriction and is not one. That bypass is Discord's documented behaviour and was **not** tested against this server, which is the one claim in the finding a reader should not take as measured.

The other four: `@everyone` holds `MENTION_EVERYONE` server-wide with only some channels taking it back, so a channel created later is pingable by default; a bot role belonging to another project holds `MANAGE_CHANNELS` across the whole server while being granted a single view permission anywhere specific; the port-showcase forum is the one channel that *allows* `MENTION_EVERYONE` where every other denies it; and the forum topic order reads newest-activity-first, which corroborates an open question in two other items without settling it.

The last is outside the permissions question and was filed anyway, because the actionable filter came out of the audit procedure earlier in this same run — worth-doing is the user's call at /plan, and a silent step before her can only drop things.

Reads only. Nothing on the server changed. Any permission change is hers to make in Discord and would file as its own `[user]` item.

**Scrub applied at filing:** one role is named after an individual and is referred to by what it is rather than by that name, and member overwrites are cited by id only.

**Depth:** full — reasoning contested.
**Findings routing:** 5 filed as captures, none dropped on re-reading. One carries `Red flag · State: uncleared` — [expert-role-holds-administrator].
**Files touched:** none — the audit read the tool's output and the record.
**Routed to Captures:** [expert-role-holds-administrator], [everyone-holds-mention-everyone], [second-bot-role-holds-manage-channels], [port-showcase-allows-mention-everyone], [forum-order-is-by-latest-activity].
