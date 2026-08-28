# [user] Re-home the how-to forum posts under the bot's authorship [howto-posts-bot-authorship]

Walk-through started 2026-08-28 during a /next run. Written as the drive went, so a crash leaves a record of exactly what was done.

## Step 1 — survey of the six how-to topics, read live through the bot

The bot's send permission in ❓how-to-throughliner was confirmed from the API earlier (view, create posts, send in threads), so the read half of step 1 ran without trouble. Forum channel id `1541659900705378355`. Six topics, none archived:

```
1541661928554758184  1. 🛠️How to install                    starter 880 chars   + 5 later messages
1541667850375405578  2. ⚙️Running your first session         starter 1744 chars  + 5 later messages
1541672181212127282  3. 📋Running /plan for the first time   starter 1997 chars  + 3 later messages
1541674483511988277  4. 🏗️Running /next — start building     starter 1594 chars  + 2 later messages
1541690853691621437  5. 📓Ending your session with /done      starter 1295 chars  + 2 later messages
1541693651166699601  6.🔭/rescan — catching what you missed   starter 1803 chars  + 2 later messages
```

Every message in every thread is authored by the user, none by a bot — which is the condition this item exists to change.

## The walk-through halted at step 3, before anything was posted or deleted

Two things the walkthrough did not anticipate, both found by reading the live forum rather than by reasoning:

**1. A forum topic's opening post is not an ordinary message.** In a Discord forum, the thread and its starter message share an id, and the topic exists because that message does. The walkthrough's step 3 has the user delete each original after the bot has posted its replacement in the same topic — but if deleting the starter deletes the whole topic, that step destroys the bot's replacement along with it, and the topic's name, position and any links pointing at it.

**This is stated as the thing to check, not as a fact.** It is a claim about how Discord behaves, and the rule this project shipped today says a capability claim gets the read that would verify it before anyone acts on it. Nothing here has verified it.

**2. Each topic holds more than one message.** Between two and five follow-ups sit under each starter, all the user's, plus one empty-content message per topic that is almost certainly an attachment. The walkthrough treats each topic as a single post. Re-homing "the post" leaves those follow-ups where they are, under the user's name, in a topic the bot would then be presenting as its own.

Nothing was posted, edited or deleted. The item stays in the queue.

## The search ran, on the user's go, and did not settle it

Two searches, and the evidence points both ways:

- A Discord support feature request, "Forums: Display first UNDELETED post as subtitle", exists only if a forum post *survives* its first message being deleted — it asks for the subtitle to fall through to the next message instead of reading "Original message was deleted". Its own page returned HTTP 403 to a direct fetch, so this rests on the search result's summary rather than on the page read.
- Another support thread in the same result set was summarised as the opposite: deleting the original message deletes the whole post.
- The developer documentation is clear only about the *other* case — a thread created from an existing message in a text channel, which is orphaned rather than deleted when its source message goes. A forum post's starter is not that: it is created with the thread and shares its id, so the documented behaviour does not transfer.

**So the question is open.** Recorded rather than resolved, and the walk-through is not resumed on a guess.

There is a safe empirical test available and not taken: the bot could create its own throwaway topic in the forum and delete its own starter message, which settles it with nothing of the user's at risk. It was not run because it posts to a public onboarding forum and needs her say-so.

## Outcome — DEFERRED, on the user's own word

She offered the deferral herself — *"go ahead or we can defer this to plan and transform into a user line"* — and after the search failed to settle the deletion question, accepted the defer-to-plan recommendation and moved to the next item. The item stays in the queue for /plan to reshape; the two design questions it must answer (whether deleting a forum starter deletes the topic, and what happens to the follow-up messages) are recorded above, along with the safe bot-side test not yet run.

## What was NOT done

Step 1's second half — showing each post's current text unchanged — was deliberately held. Fetching six posts verbatim into this record is work the approach may discard, and the approach is now an open question.
