# CYCLES

Recurring work this project has put on a cycle. Each definition names the
artifact, the steps of one turn, the cadence, and **the observable that marks a
completed turn** — position is never stored, so every check recomputes due-ness
from the observable. The openings and closes of /plan and /next read this file
and file one capture per due turn.

## Weekly release [weekly-release]

**Artifact:** the GitHub release of the Throughliner plugin.

**Cadence:** weekly on Wednesday, declared by the user 2026-08-22.

**Observable:** the published date of the latest GitHub release (`gh release list`).

Declared rather than derived from the record — the definition says which, and
this one is the user's decision. A turn is due when that published date falls
before the current Wednesday; the rezip list supplies the candidate build.

**One turn produces two events, in this order.** The week's pick becomes the new
**beta**, and last week's beta — which has now had its week of soak — promotes to
**stable** and is released. So a build is never released in the same turn that
selects it: the soak sits between the two events, and it is the whole reason the
turn has two halves rather than one.

**Steps of one turn.**
1. Check the branch is `main` — a release never runs from anywhere else.
2. **Promote last week's beta to stable.** The `beta` branch tip as it stands
   *before* this turn touches it is the build being released — it has had its
   week. Read its commit; that is what the release ships.
3. Run the release ritual in `resources/release-ritual.md` end to end against
   that commit — the version bump, the consistency sweep, the repackage, the
   GitHub pre-release, the host reinstall.
4. **Pick this week's beta: the most recent rezip labelled stable on the
   test-rezips-for-nerds list.** The pick is mechanical and takes no judgment on
   the day — the label was applied when that rezip was posted, describing a
   build that already existed, so the turn reads a recorded state rather than
   asking "is this good enough?" That prospective readiness question stays
   banned, which is what the 2026-08-09 decision was protecting.
5. **Fast-forward the `beta` branch to that rezip's commit**, read from its entry
   in the rezip archive. Testers installing from `FlintcraftTech/throughliner#beta`
   pick it up on their next update. Where the pick is not a descendant of the
   current beta tip, stop and say so rather than forcing the branch.
6. Offer the beta announcement, filled in from
   `resources/beta-offer-announcement-template.md`. It goes out through the bot
   on the user's explicit yes to the exact text, and gets its line in
   `INBOX/sent.md` in the same turn.
7. Record the turn in `LOG/` under this cycle's slug — both events, with the two
   commits named.

**Refused, and recorded so it is not re-proposed:** choosing among candidate
rezips each Wednesday on the day's judgment. The selector is mechanical — most
recent stable label wins. Also refused: a separate beta cycle with its own
cadence — one cycle, beta as a step inside its turn, the user's call 2026-08-22.

**Superseded selector, kept because the reasoning is cited elsewhere:** the
original pick rule was "newest rezip at least a week old". Its week-old property
now lives in the promotion step above rather than in the pick — step 2 releases a
build that has had exactly that week, so the property is enforced by the turn's
shape instead of by the selector reading a date.

## Tips posting [tips-posting]

**Artifact:** the 💡tips channel on the Throughliner Discord.

**Cadence:** every three days, declared by the user 2026-08-29.

**Observable:** the date of the most recent tips line in `INBOX/sent.md`, which
records the channel per post.

Declared rather than derived — the definition says which, and this one is the
user's. The record could not have supplied it: one tip had gone out at the time
this was written.

**Material.** Every capture in QUEUE.md's Unprocessed section carrying the line
`Cycle: [tips-posting]` — the field is what claims it, so the planning ladder
passes over it rather than presenting it as a pending decision, and a turn draws
from that pool rather than inventing a subject. Candidates are filed at rezips as
features land, recycled from old announcements, or noticed any other way, and
**the filing writes the field**, so a new candidate arrives claimed. New or
updated features first; recycled and historical tips on slow news days.

Deleting this definition releases the whole pool by itself: a `Cycle:` naming a
cycle that no longer exists ranks normally again, with nothing to unwind.

**Steps of one turn.**
1. Pick a candidate. Prefer one whose capture carries a release's version line,
   which is what marks a feature as shipped and so postable. Where none is
   marked, take a recycled tip — those describe features that shipped long ago,
   so they need a drift check rather than a release.
2. Verify every claim against the **installed** plugin, at post time rather than
   draft time. Where a claim has drifted, rewrite it or hold the post.
3. Read the how-to topics' lines in `INBOX/sent.md` for claims this post
   touches. A needed tweak is the bot editing its own how-to post, under the
   approval rule like any send.
4. Draft it. The post walks the reader through the how-to — what to type, where
   to look, what tells them it worked — rather than reporting that a capability
   exists, and stays under 2,000 characters.
5. The bot posts it to 💡tips on the user's explicit yes to the exact text, then
   reads the message back.
6. Write the register line in `INBOX/sent.md` in that same turn — date, channel,
   intent, what it claimed, and a pointer to the text. **Read the claim off the
   approved text as it stands, never from what the session settled.**
7. Author the FAQ entry the post teaches, into
   `plugin/throughliner/templates/faq-template.md` with its index line, then
   re-copy both into `FAQ/`.
8. Delete the spent candidate's capture from QUEUE.md.

**No writable-paths declaration is needed, checked rather than assumed:** every
path a turn writes — `INBOX/`, the two FAQ templates, `FAQ/`, `QUEUE.md` and a
scratch draft file — is already permitted to a planning session. If a later step
ever needs somewhere outside that, this definition gains the field that
[ritual-declares-writable-paths] builds.

**Not capped by anything else:** the one-post-a-day pacing was repealed
2026-08-28, so this cadence is the only rhythm governing the channel.

## Announced-claims sweep [announced-claims-sweep]

**Artifact:** the claims recorded in `INBOX/sent.md` for channels that retire
their old posts rather than recycling them — 📣announcements above all.

**Cadence:** weekly, declared by the user 2026-08-29, matching the release
cycle.

**Observable:** the date of the most recent `LOG/` entry under this cycle's slug
**whose opening line says it records a completed turn of this cycle**. Each
turn's record must open with that sentence, and a record that does not carry it
is not a turn — which is what keeps the planning records written under this same
slug, including the one that authored this definition, out of the count.

Declared rather than derived, and the reason is the derivation the user chose:
a release is the thing most likely to falsify a public claim, so the sweep runs
at the rhythm of the thing that breaks its subject.

**Why it exists, and what it does NOT cover.** Channels flagged to *return*
their pruned posts re-check themselves — a pruned post comes back as a capture
and its claims are verified before it is reposted ([channel-depth-and-recycling]).
Channels flagged to *retire* get no such pass, so a claim there is checked only
if some later change happens to repeal its exact wording and the grep over
`INBOX/sent.md` happens to match. That gap is not hypothetical: the 2026-08-22
announcement was falsified on 2026-08-27 and nothing fired for a week.

**Steps of one turn.**
1. Read `INBOX/sent.md` and take every claim line whose channel retires.
2. Re-read each claim against the **installed** plugin, not the source tree.
3. Where a claim no longer holds, file one capture naming the post, its message
   id and what is now false. Satisfied while an open capture already carries
   that post's id.
4. Where every claim still holds, say so in one line. A sweep that ran and found
   nothing must be distinguishable from one that never ran.
5. Record the turn in `LOG/` under this cycle's slug, **opening the record with
   a line saying it records a completed turn of this cycle** — that sentence is
   what the observable counts.

**Two limits, stated because this cycle is easy to over-read.** Its observable is
written by the same session that runs the turn, so it records that a sweep
happened and not that it was thorough — unlike the release cycle, whose
observable is an external publication date. And its cost grows with the register:
every turn re-reads every retained claim, so a long-lived channel makes a longer
sweep.

**Scope until [channel-depth-and-recycling] ships:** no channel carries a
retire-or-return flag yet, so the sweep's scope is 📣announcements by name, plus
the forums below.

**The forums are in scope too, on the user's instruction 2026-08-29, and they
need a second check the channels do not.** The ❓how-to-throughliner forum and
the "how ports work" forum ([ports-forum]) both hold standing instructional
posts whose claims go stale exactly as an announcement's do — and their lines are
already in `INBOX/sent.md`, so step 1 reaches them with no change. A fourth cycle
was considered and refused: one definition covering every published claim beats
two that can drift apart.

**The extra check is ordering.** A forum lists its topics by latest activity, so
posting or commenting shuffles them out of their numbered sequence — observed
2026-08-29 with the how-to topics displaying 3, 6, 5, 4, 2. So each turn also
reads the forum's topic order and reports where it no longer matches the numbers
in the titles. **Report only: re-ordering a forum is the user's to do, and
whether it can be done at all is one of the questions
[howto-posts-bot-authorship]'s first step settles.**
