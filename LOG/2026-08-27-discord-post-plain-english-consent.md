# Plain-English consent post — posted to #tips through the bot

`[user]` item [discord-post-plain-english-consent], walked through and completed
in the 2026-08-27 /next run. **The first post this project has made to Discord
through the bot rather than by hand.**

## Verification before posting, as the item required

All three of the draft's claims were checked against the **installed** build —
not the working tree, which this same run had already edited, so the target and
installed content stamps differ (`c592cd7d1058` against `f5e65732596c`) and only
the installed one can make a post true at the moment it goes up.

- "each one opens with a plain-English summary … before any analysis" — present
  in the installed `plan.md`.
- the recommendation states in plain words what would change and asks agreement
  in those words — present in the installed `plan.md`.
- records bounded by the project's own measured norms — present in the installed
  `skill-nonspecific-rules.md`.
- `"the ready list"`, the retired phrase the item warned the draft quoted,
  appears **nowhere** in either installed doc, so no rewording was owed.

One wording change was made and accepted: the draft said each item "**now**
opens with" a summary, which asserts a before-and-after no current reader lived
through. The word was dropped so the sentence describes what happens rather than
what changed.

## The channel, and why it is tips rather than announcements

Under the two-kinds posting rule built earlier in this same run, this explains
one feature with no release or event behind it, which is the tip test rather
than the news test.

## The permission gap this uncovered

The first send failed: **HTTP 403 "Missing Permissions" (code 50013)** on tips.
Nothing was sent, so there was no partial state to unwind.

Rather than discovering the rest one failed send at a time, the bot's effective
permissions were computed for every channel from the guild roles plus each
channel's overwrites — a read, never a test post. Result: it could post to
test-rezips-for-nerds, general-chat and give-and-get-support, and was blocked
from tips, announcements and the how-to forum. **Reading those three worked**,
which is exactly why the gap stayed invisible until a send was attempted.

The user granted Send Messages on tips and announcements, and the post then
succeeded. Recorded in `TOOLS.md`.

**A sentence written into `CLAUDE.md` earlier in this same run is falsified by
this** — it states the bot may post in tips, announcements and
test-rezips-for-nerds, which was untrue of the live server when written. It is
true now, but it was asserted rather than checked. Filed as
[claude-md-asserted-bot-posting-channels-unchecked].

## The posted text, verbatim

Read back from the live message through the bot after posting, not reproduced
from the draft:

> **Plain-English approvals.** When you and Claude go through your captured ideas in a planning session, each one opens with a plain-English summary of what the idea says — right there in the chat, before any analysis. And when Claude recommends what to do with it, it says in plain words what would actually change ("this would move into Processed, cleared to run — the part of the queue the build command works from") and asks whether you agree, in those words. No procedure jargon, no needing to open the queue file to know what you're saying yes to: you approve what's in front of you.
>
> The files themselves stay tidy through a companion rule: everything written into your project's documents is bounded by the project's own measured norms, so records stay terse enough to actually read when you do open them. The summary serves the moment; the documents serve the return visit.

Channel `💡tips`, message id `1542432408320606338`, author "Throughliner Project"
(the bot).

## What this confirms about the posting bot, and what it does not

**Confirmed live:** authentication, channel-name resolution across emoji-prefixed
names, and `send`. This is the acceptance test [discord-posting-bot] was waiting
on, met in a real channel with the user's explicit yes to the exact text.

**Still unconfirmed:** `edit`. Editing this post purely to prove the code path
would alter a published post for no reason, so it is left to the first genuine
edit. Said plainly rather than recorded as passed.

## The one-a-day rule, and the amendment it prompted

A Throughliner post had already gone out on 2026-08-27, so the standing one-a-day
pacing would have held this back. That was put to the user as its own turn, and
she directed it up anyway.

She then amended the rule: **one post a day per channel**, her reasoning being
that the rule dates from when announcements was the only channel in use and
everything went there. Not written into `CLAUDE.md` by this run — the rule gate
reserves rule admission for a planning session — so it is filed as
[one-post-a-day-is-per-channel]. On her reading there was no collision here at
all, since today's earlier post and this one are in different channels.

## Outcome

**done** — walked to its end this session.
