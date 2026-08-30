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

## 2026-08-29 — the walk-through resumed, and the open question is settled

The item was rewritten at the 2026-08-29 planning session to open with the throwaway-topic test. That test ran today, on the user's explicit yes to the exact text, and it answers the question the 2026-08-28 drive halted on.

**The bot could not create a forum topic at all until this run.** `resources/discord_post.py` gained forum mode as [bot-cannot-create-forum-topics] earlier in the same /next run; this test is its first live exercise, so it doubles as that build's confirmation.

**The commands were run by the user in her own terminal, not by Claude.** This session's auto mode blocked the outbound post at the classifier. The route was not worked around — the block was reported, the user chose to run it herself, and she was walked through it one command at a time. One deviation from the approved text is recorded: the 🧪 emoji was dropped from the test topic's title, because Windows PowerShell mangles emoji passed to a program as an argument and a corrupted title would have muddied the reading. She was told before running it.

**(a) A forum topic SURVIVES its opening message being deleted.** Settled by observation rather than by search:

```
topic created        1543081212803940402 — and its OPENING MESSAGE SHARES
                     THAT ID, which is the fact the question turned on
follow-up posted     1543083058910199861
opening deleted      prune --keep 1, scoped to that thread
after the delete     the topic is STILL LISTED in the forum, still readable,
                     keeping its id and its name, holding only the follow-up
```

So the 2026-08-28 search's more optimistic reading was right, and the pessimistic summary was wrong. **Step 5 of the walkthrough is therefore safe**: the user deleting her original after the bot has posted its replacement in the same topic does not destroy the topic or the replacement.

**(b) The forum sorts by latest activity, and the answer is partial — stated as partial.** The six how-to topics returned in the order 6, 5, 4, 3, 2, 1 both before and after the test, unchanged by a new topic being created beside them. The test topic sat at the top throughout. **What this does NOT prove is that posting into an existing topic bumps it up the list**, because the test topic was already top and had nowhere to move. The clean proof arrives during the re-homing itself, which posts into all six.

**Left behind, and needing the user's hand:** the test topic still exists, now holding one message. The bot cannot delete a topic — that is a route the script does not have — so removing it is hers to do in Discord. **She deleted it the same turn and confirmed it was gone**, so the forum is back to its six how-to topics and nothing of the test remains.

## Outcome 2026-08-29 — DEFERRED again, on the user's own word, with step 1 now settled

Her words: *"can you capture this for later processing? I don't have the energy to do all this right now."* Step 2 — confirming that her follow-up messages in each topic are edit notes to be deleted alongside each original — was put to her and not answered, so it stays open.

**What the deferral costs, and it is small:** step 1's two questions are answered above and do not need re-running. What remains is the re-homing itself, six topics of fetch-show-post-delete-register.

**Why it stopped where it did.** Every outbound post in this session was blocked by the auto-mode classifier, so each one had to be pasted into a terminal by the user — three commands to run one test. Six topics is about twelve more. That cost is what she declined, rather than the work itself, and it is filed as [discord-script-permission-rule] so a later session does not meet the same wall.

## 2026-08-30 — resumed in a /next run, at step 2

The record above shows step 1 finished on 2026-08-29 with both of its questions answered, so it was not re-run. The drive resumes at step 2, the one thing that was put to the user last time and not answered: what happens to her follow-up messages in each topic.

One fact arrived since, from this session's Discord permissions audit and filed as [forum-order-is-by-latest-activity]: the `threads` listing still returns the six how-to topics in the order 6, 5, 4, 3, 2, 1, unchanged from 2026-08-29. It corroborates the latest-activity reading and does not replace the clean proof, which still arrives during the re-homing itself.

**Step 2 answered 2026-08-30, as one rule on the user's word: her follow-up messages are deleted along with each original**, in every one of the six topics, rather than being decided topic by topic. That is the default the item recorded, confirmed rather than composed — they are edit notes, and an edit note about a post the bot now owns has nothing left to annotate.

**And step 2's premise turned out to be wrong, checked before anything was deleted.** The follow-up messages are not the user's edit notes and are not her messages at all. Reading each message's `type` field — rather than only its content, which is what the 2026-08-29 survey did — shows every topic holds exactly ONE authored message:

```
type 0   the starter — her actual post, the only thing to re-home
type 4   Discord's automatic "thread renamed" notice, whose CONTENT IS THE
         NEW NAME, which is why a content-only read mistook a rename trail
         for a series of edit notes
type 6   Discord's automatic pin notice, empty content
```

Verified across topics 1 and 2; the rename trails read as successive title attempts ("How to install Throughliner" → "🛠️How to install Throughliner" → "🛠️How to install" → "1. 🛠️How to install").

**So the rule agreed at step 2 has nothing to act on, and the re-homing is simpler than the item describes:** one post per topic to replace, no follow-ups to delete, and the system notices stay where they are — they are not deletable as ordinary messages and there is no reason to want them gone.

**Filed as [walkthrough-premise-read-content-not-type], because this is the second time this one item has been built on an unchecked claim about Discord's behaviour.** The first produced the shipped rule about verifying a capability claim before acting on it; this one slipped past that rule because the survey did read the live forum — it just read the wrong field.

## 2026-08-30 — REVERTED WITHIN THE HOUR. The section below describes posts that no longer exist, and the re-homing did not happen.

**The user stopped the drive: *"you have posted all of the help topics as comment on the old ones. they are supposed to be new topics."*** She is right, and the walkthrough is what led here — its step 4 reads "the bot posts the replacement in the same topic", so each bot copy went in as a reply beneath her opening post.

**Why that does not re-home anything.** In a Discord forum the topic's opening message *is* the post — they share an id. A reply is a comment on the post, not the post. Had step 5 then run, each topic would have survived (as the 2026-08-29 test established) but its opening content would be gone, leaving the text readers came for sitting underneath as a comment. The 2026-08-29 test proved the topic survives; nobody asked what the topic would then look like, and that is the gap.

**Reverted on the user's yes.** All six bot replies deleted through the bot and verified gone; all six of her originals verified still present. Nothing of hers was ever touched, and the forum is exactly as it was. The register line was corrected in the same turn.

**Filed as [howto-rehoming-needs-new-topics].** Doing this properly means the bot creating six new topics — a capability it has, built as [bot-cannot-create-forum-topics] — and the user deleting the old topics whole. That changes every topic's id and its position in the forum, which is a design change to the item rather than a step to improvise mid-run.

## 2026-08-30 — all six re-homed, sends unblocked this session

**On the user's instruction covering the set**, given after seeing topic 1's text: *"yes it's ready. consider them all ready. I can read them and plan changes later."* Each post is her own words reposted **unchanged** — nothing was authored, reworded or trimmed — which is what let one instruction cover six sends. Read back from the channel after posting and compared byte-for-byte against each original: all six identical, all six authored by "Throughliner Project".

```
topic                                original             bot copy
1. How to install                    1541661928554758184  1543507117930188840   880 chars
2. Running your first session        1541667850375405578  1543507122262773852  1744 chars
3. Running /plan for the first time  1541672181212127282  1543507126004088981  1997 chars
4. Running /next                     1541674483511988277  1543507130169172028  1594 chars
5. Ending your session with /done     1541690853691621437  1543507133591453756  1295 chars
6. /rescan                           1541693651166699601  1543507136871403543  1803 chars
```

**Every send in this session went through.** The 2026-08-29 drive was stopped by the auto-mode classifier blocking each outbound post, which is what made six topics look like twelve terminal commands and is why the user deferred. That did not recur here, so [discord-script-permission-rule] is a capture about a wall this run did not meet — worth re-reading at its processing turn rather than assuming it still stands.

**No claim was verified against the installed plugin, and that is deliberate rather than an omission.** A repost re-asserts what a post claims, and the ordinary posting rule would require checking each against the shipped build. These are her own already-public words going back unchanged into the same topics, so nothing new is being asserted and nothing said today changes what the installed build does. She has said she will read them and plan changes later; correcting their content is that later pass, and the [announced-claims-sweep] cycle already covers this forum's claims.

**What remains is hers:** deleting the six originals. The bot cannot delete her messages.

## What was NOT done

Step 1's second half — showing each post's current text unchanged — was deliberately held. Fetching six posts verbatim into this record is work the approach may discard, and the approach is now an open question.
