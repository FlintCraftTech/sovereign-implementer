# Discord forum posts and notifications — what an admin can and cannot switch off

Researched 2026-09-02, prompted by the user's question before the first
`#👷‍♂️how-ports-work` post went out: are we spamming people with notifications,
and can that be switched off for the two forums?

## The finding

**There is no per-channel notification default an admin can set.** The lever a
server owner has is the **server-wide** default — Server Settings →
Notifications → All Messages / Only @mentions — and it applies only to members
who have never changed their own notification settings. Per-channel control
(Discord calls it a Notification Override) is a **per-member** setting each
person applies for themselves; it cannot be imposed on a channel from the
server side.

**The evidence that the admin-side version does not exist is the feature
requests for it.** Discord's own support-community boards carry open requests
for exactly this — "default notification settings for channels", "[Server
Setting] Channel Notification", and, specifically for forums, "Allow for 'New
Posts' default notification for Forums without the global 'all messages'
enabled". A standing request is not proof of absence, but three of them, one
naming the forum case precisely, is the strongest signal available short of
testing.

**So for these two forums specifically, nothing can be switched off from our
side.** What decides whether a new post pings a member is (a) their own
notification level for the server or that channel, and (b) whether the post
mentions them. Our posts mention nobody and use no `@everyone` — and
`MENTION_EVERYONE` is being taken out of the baseline role anyway
([everyone-holds-mention-everyone]) — so a member on "Only @mentions" is not
notified by them at all.

**One thing to check rather than assume: what this server's own default is.**
If it is "All Messages", members who have never customised do get pinged by
every new post; if it is "Only @mentions", they do not. That is one look in
Server Settings, and it is the whole of what is controllable here.

## What this does not answer

Whether a member who has explicitly **followed** a forum gets notified
regardless of the server default. Discord's Forum Channels FAQ is the page that
would settle it and it returned 403 to an automated fetch, so it was not read.
The search summary of it says members "can continue receiving notifications if
they're following a specific forum post", which suggests following is
opt-in per post rather than automatic — untested, and stated here as unresolved
rather than folded into the finding.

## Frame assessment

- **Time range** — not applicable in the usual sense; the question is about a
  product's current behaviour. The risk is that Discord ships the requested
  feature and this finding goes stale, which the freshness line covers.
- **People** — applies to the server's members, who are the people a post would
  notify. The user's own concern is about them rather than about herself.
- **Freshness** — the subject changes on Discord's release cycle, not ours. The
  three open feature requests are the thing most likely to change; re-check
  before relying on "no admin-side per-channel default" more than a few months
  from now.
- **Risk if wrong** — low and self-correcting. If an admin-side default does
  exist and was missed, the cost is that a setting nobody changed stayed
  unchanged; nothing is published on the strength of this and no claim about
  Discord goes into any post.
- **Alternatives** — the alternative approach not taken is testing it live:
  changing the server default and observing what a second account receives.
  That is the only way to settle the following question above, and it needs a
  second account and the user's hands, so it was not attempted here.
