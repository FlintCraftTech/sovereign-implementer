# Discord Connections + Linked Roles as a GitHub identity handshake

Researched 2026-08-25, during the multi-user identity design ([multi-user-identity-layer]): Alex wanted identity "harder than people saying who they are" for a remote participant prompting a session through a Discord channel, and suspected a GitHub handshake would have to happen on the consumer-project (Chagora) side.

## Finding

No custom bot is needed. Discord natively supports **Connections** (a member links their GitHub account inside Discord via an OAuth authorisation GitHub itself confirms) and **Linked Roles** (a server grants a role only to members whose linked connection meets set criteria — GitHub is a supported platform). So a server can stamp a member with a verified role that attests to a real GitHub login, and anything a bot relays from that member carries a Discord identity backed by it.

- Feature coverage: Discord linked accounts / role verification — https://www.engadget.com/discord-connections-server-roles-170028296.html
- Working example implementation: https://github.com/JustinBeckwith/linked-role-bot

## What it means for the design

- The handshake lives on the consumer side (server setup), not in the method.
- The method's side needs only: identity is the authenticated identity the channel supplies, where one exists.
- GitHub-side credit is separate and simpler: commit **co-author trailers** (`Co-authored-by: Name <email>`) — GitHub attributes the commit to the named person; no branches or separate sessions needed. The person supplies their name/email pair once, by consent.

## Limit

Not verified: exactly what connection metadata a bot can read programmatically versus merely gate a role on. The design leans only on the role's existence, which is safe.
