# Discord message limits: bots are capped at 2,000 characters, and no paid plan lifts it

Filed 2026-09-02, from a web search made while processing [rezip-backfill-has-no-room], where the user asked whether a paid Discord plan would raise the limit the rezip-entry backfill keeps hitting.

## What was found

- A free Discord account sends up to 2,000 characters per message; a full Nitro subscriber sends up to 4,000.
- **The 4,000 does not reach bots.** The API's content field is capped at 2,000 characters on every endpoint that sends or edits a message — channel messages, webhooks, interaction responses — whatever the owner's subscription. A bot cannot benefit from Nitro.
- Nitro Basic does not raise the limit at all; only full Nitro does, and only for the human account that holds it.
- Pricing at the time of the search: Nitro about $9.99 a month or $99.99 a year; Nitro Basic about $2.99 a month or $29.99 a year.

## What it settles

Every post this project makes goes out through the bot, so the 2,000-character ceiling is a hard one for the rezip entry, its backfill, the tips and the announcements alike. Paying does not move it. Room for a backfill has to come from structure — a threaded reply under the entry — not from a plan.

## Frame assessment

- **Time range:** current as of the search date; the limit has been 2,000 for bots for years and nothing suggests a change.
- **People:** applies to the bot account this project posts through, which is the only sender here.
- **Freshness:** Discord changes plan features occasionally; the bot ceiling is an API constant and is the stable part. Re-check the prices before quoting them anywhere.
- **Risk if wrong:** low — if a paid plan ever lifted the bot limit, the threaded-reply design still works and merely stops being necessary.
- **Alternatives:** webhooks and interaction responses were covered by the same finding; none escapes the cap. Splitting a message into several was not researched as it is the same structural answer as a reply.

Sources: [TypeCount on Discord limits](https://typecount.com/blog/discord-character-limit), [DigiToolVault field list](https://www.digitoolvault.com/post/discord-character-limit), [Discord pricing breakdown](https://pumble.com/discord-pricing), [eesel on Nitro tiers](https://www.eesel.ai/blog/discord-pricing).
