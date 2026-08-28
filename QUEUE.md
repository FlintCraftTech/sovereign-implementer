# QUEUE

Two sections. **Processed** — agreed work, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** — captured, not yet processed; the next /plan weighs each item. Every entry in either section is a `#### ` heading (its description) with a `[slug]` at the end of that line and its rationale beneath; an entry in Unprocessed is a **capture**, and it becomes a **work item** when /plan keeps it into Processed. A leading `[audit]` / `[user]` tag names how it's executed; no tag means a build. An item carrying a security or privacy risk gets a `Red flag · State: …` marker — the flag rides the work.

**Authoring a rule for the method's own text? The rule gate is in `CLAUDE.md`, always loaded — run it before you write.**

## Processed

#### [user] Re-home the how-to forum posts under the bot's authorship [howto-posts-bot-authorship]
Filed 2026-08-27 with [posting-rule-two-kinds-and-tip-pipeline], from your instruction that the how-to topics be editable and maintainable by the bot. The constraint that makes this an item at all (recorded in `TOOLS.md`): a bot can only edit messages it authored itself, and the existing how-to posts are yours — so bot maintainability requires each one re-posted by the bot once, after which every later tweak is a bot edit under the approval rule.

**Walkthrough.**
1. Once the posting script exists, Claude fetches each how-to post's current text through the bot and shows it to you unchanged. Look for: the text matching what the forum shows.
2. On your yes per post, the bot posts the replacement in the same topic. Look for: the new post appearing under the bot's name.
3. You delete your original post of each (only you can — the bot cannot delete or edit your messages in a forum topic it doesn't manage, and your authorship is the thing being replaced). Look for: the topic showing only the bot's copy.
4. The register line for each how-to post is updated to point at the bot's copy, with the channel named; this item closes when every how-to topic's live text is bot-authored.
**Blocker re-pointed 2026-08-27, not lifted.** [discord-posting-bot] shipped and was verified live — the bot posted to #tips and read the message back byte-identical — so the thing this waited on exists. But the same run measured the bot's per-channel permissions and found it **cannot post in the how-to forum**, which is where step 1 of this walkthrough goes. Lifting it now would clear work that stops at its first step. The hold moved to [bot-needs-howto-send-permission], which was the grant that had to happen first.
**Lifted 2026-08-28.** The user granted the permission and it was confirmed from the API rather than on report — view, create posts and send in threads all true in the how-to forum — so the hold is dropped.

#### [user] Write the law-prose article for the site [law-prose-article]
**Kept 2026-08-28, cleared with no hold** — unlike the two held articles, its material is the law-prose record itself, already rich on file, and the article is publicly promised "in the coming weeks". Your observation at the keep: this walkthrough is the first clear representation of **co-writing** — interleaved Claude-drafting and your-writing steps rather than a Claude work item you end up writing into.

**Walkthrough.**
1. Claude re-reads the source records — the restyle passes, the gate amendments, the rationale-split post-mortem — and lists the article's claims including the honest limits (targets found by grep; ~151 mid-sentence prohibitions knowingly left, most legitimate). You see the list before drafting starts.
2. Claude drafts the article for flintcraft.tech, first person, opening on your arc — massive prose rule sets with no system, then pseudocode, then law prose — with the why-clauses reasoning inside it, under the recorded guardrail: the story is how models follow rules, never internal reorganisation dressed as user benefit.
3. Claude drafts the giveaway — the platform-agnostic self-authoring prompt — generalised from [setup-self-hosting-seed]'s templates, which build first.
4. You read both and say what to change; repeat until you're satisfied.
5. You decide delivery to the site project: an INBOX message (you see the exact text first) or you carry the files across yourself.
6. You publish — Claude has no route to the site. The Discord announcement is separate and carries the why-story: [law-prose-article-announcement-carries-the-why] returns to the queue by itself when this closes.
7. You confirm it's live; the send is registered in `INBOX/sent.md`, and this line closes.

Filed 2026-08-28 while processing [law-prose-article-announcement-carries-the-why], which is held on this. The article is real committed work with a public claim behind it: the user's 2026-08-26 beta announcement on Discord said the law prose findings "deserve a full article on my website... in the coming weeks" (register line in `INBOX/sent.md`). Content, venue and walkthrough are questions for this capture's own processing turn — the default shape is the flintcraft.tech article chain the two held articles already follow (Claude drafts, the user reviews and publishes, the send is registered). The announcement that accompanies it carries the why-clauses story per the held capture.

**What exists at filing — surveyed 2026-08-28, and there is no draft anywhere; this is the source-material map:**
- The findings corpus, in the LOG from 2026-08-10 onward: the rule-gate amendments (subordination, placement), the prohibition-and-subordination audit, the restyle passes converting prohibitions to stated actions, the rationale split moving why-clauses out of operative rules, and the honest blind-spot record (the restyle found targets by grep, caught thirteen sentence-leading prohibitions, knowingly left ~151 mid-sentence ones, most legitimate).
- The guardrails: `LOG/2026-08-27-announcement-rationale-split-correction.md` — what a piece on this subject must not do (internal reorganisation dressed as user benefit).

**Your narrative arc, given 2026-08-28: the story opens with what failed before.** First, massive prose rule sets written with no existing system; then pseudocode; then the law-prose style. The why-clauses reasoning (a rule with its justification attached is longer, a model follows fewer instructions reliably as they lengthen, and near-identical rules degrade one another) lands inside that arc.

**Your giveaway idea, 2026-08-28: the self-authoring rules ship with the article as a free resource** — a platform-agnostic prompt anyone can use to implement law-prose rule writing in their own system, whatever the tool. Related to [setup-self-hosting-seed], which generalises the same host sources for Throughliner consumers; this is the wider, tool-agnostic form distributed with the article. Whether it is part of this item or splits out is a question for the processing turn.

--- Cleared to run above this line ---

#### [user] Write the article comparing Throughliner to memory-system approaches, finishing with what shipped [competition-comparison-article]
**Captured by you 2026-08-15**, from a discussion prompted by Discord talk about "Obsidian memory systems" and "dreaming". **Your framing and your decision: the analysis reads as an article starter for the Throughliner site, and rather than sending it now it should be captured and finished with our shipped solutions, with the announcement doubling as a Discord post.**

**This is your own shipped-only rule applied correctly, and you reached it independently.** `CLAUDE.md` says a post announces only what has shipped, and that where a post describes work designed but not built, it waits for the build and is filed as a queue item naming what it waits on. That is exactly this.

**Your stance on the article's framing, recorded 2026-08-17 and NOT generalised into a rule.** Claude proposed turning it into a standing rule about all writing describing Throughliner, and you refused: it *truly depends what we are writing, and the tone required*. Claude had also flattened the position itself — writing "no stake in persuading anyone that one approach beats another" where **your actual position is that you have a stake, just not in being seen as the best thing since sliced bread.**

**Your assessment of the draft, which is the live problem with this item.** It swung from hard marketing to substantially explaining why the competition is better. You sent it to the other project for polishing rather than continuing here, because you wanted to move on — so the draft is out of this project's hands and the item covers what comes back.

**The queue-read weakness is NOT answered, corrected 2026-08-19, and this must be right before the article goes out.** It once read that the article's weak points — manual curation and a 56,000-token queue read — were answered by [digest-reports-computed-fields-not-summaries]. That became false on 2026-08-17, when the digest was expressly stopped from replacing the read: a planning session now runs the digest **and** reads the whole file, because the digest computes facts and the file carries the reasoning. So the full read is still paid, deliberately.

**What actually addresses it is unbuilt.** [split-the-cleared-region-for-concurrent-sessions] gives a build a derived view and stops it reading the queue at all. **Under the shipped-only rule the article cannot claim that until it ships**, and the honest line if it goes out sooner is that planning still reads everything and the reason is that reasoning across items is what planning is for.

**Read this paragraph before drafting.** A `[user]` item sitting cleared to run, producing public text, is exactly how [discord-post-context-adjacency] was nearly posted about a mechanism that no longer existed.

**The substance, drafted in discussion and to be rewritten rather than pasted.** *Stronger:* typed documents with defined roles versus an undifferentiated note graph, so product truth, pending work and history each have a home; memory coupled to execution, since /next builds from the queue rather than merely reading it; the throughline carrying *why* rather than only what; deletion as a user-approved fate decision rather than an automatic prune; and everything as plain markdown in git, reversible and auditable. *Weaker:* curation is manual, which is dreaming's entire job — sixty unprocessed items with duplicates accumulated over weeks, seven merges by hand, six items found behind already-shipped blockers; scale, where graph retrieval never needs to read everything; and one-way links, where backlinks are derived for free.

**The verification step runs BEFORE drafting, and is not optional.** `resources/research/auto-memory-staleness.md` is dated 2026-06-09 and names AutoDream as Anthropic's own consolidation sub-agent — two months old, and what the Discord means by "Obsidian memory systems" may be a specific community project rather than the general vault-as-memory pattern. **Publishing a wrong description of someone else's system under your name is worse than publishing nothing**, and unlike everything else this project writes, it is a claim about a third party. Search first, update the research file, then draft.

**Two artifacts, not one text, settled at capture.** The article is the full piece and may be long, may discuss competitors, and may say where Throughliner is weaker. The Discord post is capped at 2,000 characters, takes the shipped fix as its subject with the comparison only as framing, and points at the article. One text serving both would either saddle the announcement with a comparison it doesn't need or truncate the article into a changelog.

**The Discord post is this item's final step rather than a separate item — the user's decision.** Order: verify, draft the article, ship the digest work, finish the article with what actually shipped, then write the post. **Nothing is published without the user seeing the exact text and giving an explicit yes.** The Discord post goes through the bot on that yes (route corrected 2026-08-28); Claude genuinely has no route to the flintcraft.tech site, so the user publishes the article.

**One thing to resolve at drafting.** The site is another project, so the article is drafted here and delivered rather than written into that repository. Whether that delivery is an INBOX message or the user carrying it across is a question for the moment it is ready.

**The blocker has shipped and the `Blocked by:` line is dropped, 2026-08-15.** [digest-reports-computed-fields-not-summaries] has a LOG entry, so the digest work the article was waiting to describe now exists.

**Verification done 2026-08-15, in the /plan session that processed this — and it changed the argument rather than confirming it.** `resources/research/auto-memory-staleness.md` was re-checked and partly corrected; its index line carries the correction too. Two material findings:

- **AutoDream is live.** It consolidates memory between sessions — merging facts, deleting contradicted notes, converting relative dates to absolute, trimming the index — triggering automatically after roughly 24 hours plus five sessions, and **a manual `/dream` command is available to everyone** regardless of rollout state. The research file's claim that it is not running was two months stale. **This sharpens the weakness the draft already admits:** automatic curation is no longer something only competitors have, it is in the base tool this plugin runs on. An article treating manual curation as a fair trade must say so, and the honest framing is why typed documents and user-approved deletion are worth the manual cost — not that the alternative is unavailable.
- **"Obsidian memory systems" is a category, not a project.** Several independent implementations exist, some with semantic search, self-rewriting notes and scheduled maintenance agents, plus Obsidian's own official Agent Skills for Claude Code from January 2026. So the article names the specific project it compares against, or says plainly it is describing the general vault-as-memory pattern. Describing "the Obsidian memory system" as one thing is the wrong-about-a-third-party failure this item was right to guard against.

**Tagged `[user]` at processing 2026-08-15**, matching the other post items rather than inventing a shape: Claude drafts the article and the post, the user publishes both.

**The one-a-day pacing this paragraph used to defer to was repealed 2026-08-28** ([one-post-a-day-is-per-channel]) — the post goes out when it is ready, on your yes to the exact text, and the article can be drafted whenever.

**Walkthrough.** Authored 2026-08-22 at processing, closing [article-walkthrough-missing].
1. Claude re-checks the two 2026-08-15 findings still hold before drafting — AutoDream's status, and whether "Obsidian memory systems" now names a specific project — offering a fresh web search; anything changed is corrected in `resources/research/auto-memory-staleness.md` first. You'll see what the check found before the draft starts.
2. Claude drafts the full article: names the specific system it compares against or says plainly it describes the general vault-as-memory pattern, and is honest that automatic curation now ships in the base tool — the case made is why typed documents and user-approved deletion are worth the manual cost.
3. You read it and say what to change; repeat until you're satisfied.
4. You decide delivery: an INBOX message to the site project (you see the exact text first) or you carry the file across yourself. Claude does whichever you pick that it can.
5. Claude drafts the Discord post — under 2,000 characters, the shipped fix as its subject, pointing at the article.
6. You publish the article — Claude has no route to the site. The Discord post goes through the bot on your explicit yes to the exact text (route corrected 2026-08-28; pacing repealed the same day).
7. You confirm both are up; the send is recorded in `INBOX/sent.md` and this line closes.

**Held 2026-08-24 on your decision, made during this item's walk-through.** Drafting stalled because Claude didn't have enough how-Throughliner-works material to draw on, and the thinking fell to you. The announcement-driven FAQ shipped 2026-08-24 and fills as announcements are posted, so the material accumulates over time; `ANNOUNCEMENT-IDEAS.md` also now carries the retired FAQ's entries — exactly the material the drafting lacked. The recovered draft did not satisfy you, so this is a redraft when it resumes, not a patch. No single queue item completes as the blocker, so the hold is a date: when it passes, the lift judgment is whether the FAQ actually has enough on the relevant features — not automatic.
Not before: 2026-09-21

**Files:** none in this project — the artifacts are an article for the Throughliner site and a Discord post. Relates to [digest-reports-computed-fields-not-summaries] (shipped) and `resources/research/auto-memory-staleness.md` (verified and corrected). [comparison-article-post-needs-rewrite] follows this item — the post's rewrite runs against the final article, so it is held on this slug.

#### [user] Article: Throughliner as a memory prosthetic — built by someone with bad recall, for a brain that avoids looking back [adhd-memory-prosthetic-article]
**Your idea, 2026-08-22, seeded from a grab bag of paragraphs from a conversation you had with Gemini** — processed the same session. Your own caveats set the editing brief: the parallels it draws between AI and human memory, and between the method's docs and memory types, are not all trusted; the 15-year-project storytelling is under-developed; there is a lot of lecturing and probable doubling-up.

**The core story, which is the article's force.** Throughliner is your coping mechanism for ADHD — advertised as a memory system for Claude, built by a person with bad recall. Friends encouraged you back into a project based on an interest you feel you have failed to build anything from in 15 years; on opening it, Claude immediately picked up audits and research planned six weeks earlier that you had completely forgotten — "a pleasant slap in the face. My memory system has got my back." The difference is invisible in projects you are continuously in; the long gap is what made it visible.

**Venue chain, your decision:** flintcraft.tech first, then a YouTube version, then potentially LinkedIn. This item covers the site article; YouTube and LinkedIn adaptations are follow-on work to file once the article exists.

**Disclosure settled, 2026-08-22: you are comfortable with the personal content everywhere it goes.** The photos-and-childhood-trauma element is on the chopping block for FOCUS, not privacy — your reason: its only connection is that you couldn't look back at your project much as you reflexively avoid your photo roll, and the rest may detract from the Throughliner selling points. The aversion analogy can survive as a sentence; decide the final cut at drafting.

**Science route, your decision: verify, keep only what fits.** The seed asserts amygdala-heavy encoding, dopamine deficits, episodic/autobiographical memory impairment in ADHD, trauma generalising recall into a threat, and a docs-to-memory-types mapping (LOG as episodic, FAQ as semantic, QUEUE unmapped). Before drafting, web-search each claim; file what holds in `resources/research/` with its index line; anything unsupported is cut or reframed as your first-person experience. The docs mapping is an analogy at best and is presented as one if kept.

**Known defects in the seed, to fix at drafting:** it names doc files Throughliner doesn't have (BACKLOG.md, UX.md, claude.md as the method's docs) — use the real four; the lecturing register and the repetition go; "brilliant" self-praise inherited from Gemini's voice goes.

**Walkthrough.**
1. Claude interviews you for the story — the project and interest (as much as you want public), what your friends said, the /plan moment and what it surfaced — and folds your answers into the draft material. Your choice, made at processing: interview at drafting rather than telling it now.
2. Claude verifies the science claims by web search, files the findings under `resources/research/` (index line in the same move), and lists which claims survived and which are cut. You see the list before drafting starts.
3. Claude drafts the article for flintcraft.tech, first-person throughout, with the photos/trauma element trimmed or kept per your call on reading the draft.
4. You read it and say what to change; repeat until you're satisfied.
5. You decide delivery to the site project: an INBOX message (you see the exact text first) or you carry the file across yourself.
6. You publish — Claude has no route to the site.
7. You confirm it's live; the send is recorded in `INBOX/sent.md`, follow-on captures for the YouTube and LinkedIn versions are filed, and this line closes.

**Held 2026-08-24 with the comparison article, same reason recorded there:** articles wait until the announcement-driven FAQ has material for Claude to draw on. Re-offered when the date passes; the lift judgment is whether the material is there.
Not before: 2026-09-21

**Files:** none in this project except the research file step 2 creates under `resources/research/`. The artifact is an article for flintcraft.tech. Relates to [competition-comparison-article] — a separate piece, no dependency either way.

#### [user] Post the beta-channel launch announcement on the Throughliner Discord [beta-launch-announcement]
Filed 2026-08-22 with the keep of [beta-tester-pathway], which drafts the announcement text into this walkthrough as part of its build. The offer is framed honestly early — a testing invitation, not a product launch (the one-a-day pacing was repealed 2026-08-28). Launches alongside the community listing per your sequencing recorded on [beta-tester-pathway] and [marketplace-submission].
**Walkthrough.**
1. Once [beta-tester-pathway] builds, the announcement template lives with the release-cycle materials (your direction 2026-08-28: a cycle template, not a one-off draft in this item); Claude fills it in, shows the exact text, and walks you through any final edits.
2. Before posting, the tester install walkthrough must have been smoke-tested on a second machine — confirm that happened; do not post an install route nobody has run.
3. The bot posts it to Discord on your explicit yes to the exact text (route corrected 2026-08-28 — the posting bot exists; pacing repealed the same day).
4. You confirm; the send is recorded in `INBOX/sent.md` with what it claimed, and this line closes.
Blocked by: [beta-tester-pathway]
**Files:** none — the artifact is a Discord post.

#### [user] Approved Discord post about the comparison article now describes a superseded draft [comparison-article-post-needs-rewrite]
Found by Claude 2026-08-23 while walking the comparison-article item. A Discord post was drafted and approved on 2026-08-22 and has not gone out — it is recorded on `INBOX/sent.md` as approved and not yet posted, with its text verbatim in `LOG/2026-08-22-competition-comparison-article.md`. Its second paragraph announces the article and describes it as closing "on the coherence-over-scale trade", which was true of the 2026-08-22 draft.

That draft is superseded. The 2026-08-23 rewrite names a specific project rather than a category, adds a section on Papi as the nearest comparable tool, and ends on a shipped mechanism instead of a general trade-off — roughly 1,400 words against 900. A hold-note has already gone to the site project asking that the old one not be published.

**So the post cannot go out as approved.** Its first paragraph, about builds reading a generated view rather than the queue, was still true when this was filed and is falsified as of 2026-08-27: [builds-read-the-queue-again] retires the view, so both paragraphs now need rewriting at step 2 — the first against the shipped read-the-queue model, the second against the final article. The claim was approved but never posted (`INBOX/sent.md`), so no public correction is owed. The rewrite runs after the article settles — it is currently out for review with the maker of one of the tools it names, and that review may change what the article ends on.

**Walkthrough.** 1. The article settles (external review back, revised text final). 2. Claude rewrites the post's second paragraph against the final article and shows the whole post. 3. You say what to change. 4. The bot posts it, with the live article URL folded in, on your explicit yes to the exact text (route corrected 2026-08-28). 5. The bot reads the message back, `INBOX/sent.md` is updated from approved-not-posted to posted, and this line closes.

**This is the repeal-falsifies-an-announcement case caught before it fired**, rather than after: the claim was recorded on the sent register, and the register is what made the collision findable when the article changed. It is also why the register records what a post claimed rather than merely that one exists.

**Kept 2026-08-24, held below the line on Claude's recommendation and your agreement.** As a capture this carried its ordering in prose because captures have no `Blocked by:`; as a held work item it carries the field, so it lifts by itself when the article item closes instead of being re-offered every session while the external review is out. The same ordering sentence is written on the article item per the known-ordering rule.
Blocked by: [competition-comparison-article]

#### Nerds-channel welcome becomes a bot-authored sticky, re-bumped at each entry post [nerds-welcome-sticky-rebump]
**Raised by you, 2026-08-28:** channels open at the bottom, so a pin at the top makes the pin feel pointless — you asked whether pins can stick to the bottom. Research (2026-08-28, in-session): Discord has no native bottom-pin; the universal pattern is a sticky message a bot re-posts as the newest message. Our bot has no always-running process, so it cannot react to other people's messages — but test-rezips traffic is mostly the bot's own, so re-bumping at each entry post keeps the welcome at the bottom exactly when people look.

Changes: the welcome text moves to a source file in the repo (`resources/nerds-welcome.md`), bot-authored on its first sticky post — the same bot-maintainability reasoning as [howto-posts-bot-authorship]; `resources/discord_post.py`'s entry-posting step gains the re-bump: after posting an entry to test-rezips, delete the bot's previous welcome message and repost the source file's text as the newest message. The user's yes to posting the entry covers re-bumping the unchanged welcome bytes; any change to the welcome text needs its own explicit yes, under the standing send gate.
Observable: after an entry post, the channel's newest message is the bot-authored welcome, byte-identical to the source file.
Refused: a third-party sticky bot — nothing currently needs a bottom-sticky in a human-traffic channel, and adding an outside bot is a decision for when something does; a gateway/daemon listener for our own bot — the script-driven architecture stands.
Blocked by: [rezip-archive-mirrors-nerds-channel]
The blocker is real, not conceptual: that item is rewriting the same posting step this extends, and two builds editing it must not interleave.

#### [user] Retire the old nerds-channel pin once the bot's sticky welcome is live [nerds-old-pin-retired]
Filed 2026-08-28 with [nerds-welcome-sticky-rebump]. Once the welcome is bot-authored and re-bumping, your pinned copy is a second stored text saying the same thing, and only you can remove it — the bot cannot delete or unpin your message.

**Walkthrough.**
1. Confirm the bot's welcome is live: open 🤓test-rezips-for-nerds and look for the welcome text as a recent message under the bot's name (it re-bumps at each entry post).
2. Hover your old pinned welcome message, open the ⋯ menu, choose **Unpin Message**, then delete the message. Look for: the pins flyout no longer listing it, and the channel holding only the bot's copy.
3. Tell this project; the register line for the pin is re-pointed at the bot's copy and this item closes.
Blocked by: [nerds-welcome-sticky-rebump]

## Unprocessed

#### Last session advises processing the run's aftermath at /plan next [forward-advisory]
Filed at the 2026-08-28 build close. The 30-item run emptied the cleared region down to two `[user]` items, and both need reshaping rather than driving: the how-to re-homing halted on two unverified questions about Discord forums (its record names them and a safe bot-side test), and the law-prose article is mid-processing — claims 1–6 settled, claim 7's recommendation recorded unanswered, 8–14 fresh. A /next run would halt on the first of these, so planning comes first. Unprocessed holds roughly two dozen new captures from the run, the rescan and the mail — among them [compliance-audit-lag] (the rule checks' own finding), a red-flagged [sent-register-untracked], the co-writing flavour question the law-prose processing is waiting on, and five tip recycles. Overlap worth knowing at ranking: [co-writing-flavour] bears directly on how the law-prose item resumes, so processing it first shapes that resume.

#### Show-first approval moments produce their text twice [approval-flow-token-doubling-simplification]
Captured by you (2026-08-01) while reviewing your Claude Code feature request anthropics/claude-code#77134. Rescoped at your direction 2026-08-13 from a larger item about approval-time doubling generally.
**The cost, narrowed to where it still exists.** Showing text in chat and writing it to a file are both the model producing those tokens, so text doing both is produced twice. That used to hit every approval moment; it no longer does — write-first shipped, and the post-write report is one line naming what landed, never a re-paste.
**What remains is the show-first set only** — the moments write-first deliberately keeps showing first, because the previous version isn't recoverable without the user: a commit message, anything leaving the machine, a wholesale conversion of a document the user already owns. There the text is composed in chat, approved, then produced again to be used.
**Why it is not buildable yet.** The saving needs the harness to surface an already-produced Write's content verbatim with no second model pass — issue #77134, which hasn't landed. Until it does there's no build to describe. Re-examine when the issue ships.
**Two things settled, not to be re-opened here.** The write-first ordering flip is decided and shipped. The convergence note about view-in-doc machinery is spent — working-mode field, Editor field and line-anchored-link promise all retired 2026-08-09.
External dependency: anthropics/claude-code#77134.

**Checked 2026-08-19 and still open** — filed 2026-07-13, labelled `enhancement`, `area:cost`, `area:tools`, `area:core`, no maintainer response and no close date. The disposition is unchanged: nothing to build, re-examine when it ships. **What the check buys is that the next session reads a date rather than re-running the lookup**, which is the whole reason it is written here.

**Two things in the discussion are worth having when this does become buildable.** A comment dated 2026-08-01 sets out the mirror direction — author-in-chat, approve, then write — and argues it needs no second primitive, because a workflow that can show a Write's content verbatim can adopt write-first ordering and get the same saving so long as rejection reverts. That is this project's shipped model described from the outside. **It looks like yours, on the date and the reasoning, but nothing in the record here says so — worth confirming rather than assuming.** A later comment proposes generalising the primitive to `show_file(path, range?)`, which would also let Claude surface parts of *existing* files without re-emitting them — that reaches the view-in-doc pointer and the inline-text offer, not just the three show-first cases, so it would widen this item rather than merely unblocking it.

**Surfaced 2026-08-19 by the decay rung, on its first firing since the interleave was adopted.** It had been the oldest entry in the queue at 17 days and nothing in the ladder had ever reached it.

**Dated 2026-08-21 with your approval — the field's first use, as this item predicted.** It waits on `anthropics/claude-code#77134`, which nothing in this queue can resolve; five weeks open with no maintainer movement, so a month out is when there is plausibly news. Not offered again before then.
Not before: 2026-09-21

**Skipped again 2026-08-19, and it is the item that produced the fix for its own condition.** Presented, found unchanged, and in being presented it made the pattern visible: three entries in one session waiting on something outside this project, none able to name a blocker, all re-offered every session. That is [not-before-reaches-unprocessed], kept and cleared in the same session. **This is its first candidate** — once `anthropics/claude-code#77134` ships, or a date is worth guessing at, the field goes here and the re-offering stops. Until the field is built there is nothing to write, so the skip stands.

#### A personal bridge pushing `[user]` items into Taskflow as tasks, and reading completions back [taskflow-personal-bridge]
**Raised by you 2026-08-19**, from executing in another of your projects where the work is mostly `[user]` items. Your framing: Throughliner becomes an executive layer over projects Claude only half-implements, and sometimes you do not want to complete things in conversation — you want the to-do list. **The mapping is yours: a `[user]` item is a task, and its steps are subtasks.** The assessment below and the decomposition are Claude's.

**Your mapping is Taskflow's own model rather than an approximation, which is what makes the completion half work.** Taskflow's subtasks inherit their parent's Project, date and placement, and a parent has no checkmark of its own — it is complete only when every subtask is, and un-checking any child pulls the parent back out of the completed tray. So completion arrives as one derived signal per item, and a half-done item cannot read as done.

**Two decisions of yours, in your own words.** Route: *"design this against the file-based route now, with MCP as the later transport."* Scope: *"agreed, personal bridge to start."* So this is host-only tooling in this project, assuming your own Drive setup, and it ships nothing to consumers; promoting it to a shipped feature is a later decision this does not pre-empt.

**Why file-first rather than MCP.** Taskflow's paid tier already designs the channel — Claude reaching Taskflow through a remote MCP server — so Throughliner would be a client of a route Taskflow intends rather than an integration Taskflow's local-first principle forbids. But `[0020-remote-mcp-server]` and `[0019-ai-choice-flow-and-mcp-setup]` are unbuilt over there and cloud sync is their precondition. The same reasoning is already on their queue in `[strategy-doc-preview]`, in your words there: *"We're just here, so we don't need the MCP."*

**Two hazards found by reading their SPEC rather than assumed.** Taskflow runs on the phone against a local Room database, so a file route means producing a file that is carried onto the device, not writing where Taskflow reads. And their existing `[0014-json-export-and-import]` is a whole-database export and restore — pushing tasks through it would replace every other task in the app. What this needs is an **additive** import, which Taskflow has neither built nor designed.

**Taskflow's answers arrived 2026-08-26** (their mail read and archived here; the standalone capture [taskflow-bridge-asks-answered] was merged into this item and deleted). All three asks are settled on their side. The bridge is not a breach of their no-external-task-app rule — that rule is about data living in two places with neither being the truth, not about who may put work in, and they have added a SPEC sentence drawing the line. They have designed a separately named **additive** import that inserts rather than restores, creating a named Project where one is missing and leaving everything present untouched — deliberately a separate action rather than a mode on the replacing import, because one destroys data and the other does not. And every exported task will carry its completion state and date, with a parent's state as the derived roll-up — the two-way half. Two of their choices travel into our design rather than being rediscovered: additive stays separately named, and incoming tasks are deliberately not de-duplicated, on their view that a visible duplicate is a smaller harm than a task that silently never arrives.

**The status qualifier is load-bearing: all of this is settled and unbuilt on their side** — product decisions, not shipped capabilities. So the design here can now be written at the keep-step, but anything depending on the file format depends on a design rather than a thing that exists, and the item stays unbuildable until their export and additive import ship.

**A second question rides this item's keep, merged 2026-08-26 from the deleted capture [multipart-user-handoff-queue-side]: the queue-side bookkeeping Taskflow declined to design.** What this queue does with a `[user]` item whose parts have moved onto a to-do list. Their side is settled and small — an arriving task is an ordinary task with no origin marker (their trust-at-a-glance reasoning, now in their SPEC), so a handoff sends only a title, an optional Project and an optional date. The candidate design here is existing machinery rather than new state: a handoff is an outbound send, so the sent register's intent field carries the bookkeeping — *for completion* can clear the item, with completion read back through the bridge's export or your mention; *for continuation* leaves the line in place carrying a note of what moved. Their one flag is the constraint the design must survive: the handoff most likely fires **mid-walkthrough**, when the item's true size becomes visible and the user is least able to reorganise — so the run records which steps moved and stops walking them.

**Scrub settled 2026-08-28 at processing:** a pushed task is text leaving this project's records, so it passes the same scrub checklist as any capture before it crosses the boundary — personal names, case details, third-party data rewritten at the boundary at the same level of usefulness — with the standing limit stated: the check catches credential shapes and what Claude's own read spots, and nothing can tell whether a sentence quietly identifies a real person.

**Re-dated 2026-09-28 with your approval, 2026-08-28.** The 2026-08-21 date passed and the item was taken up on its merits: it cannot pass the buildability check while the file format it writes depends on Taskflow's designed-but-unbuilt export and additive import — scoping against another project's unshipped design would be guessing. Lift judgment when the date passes: read Taskflowapp's own LOG index (this project may read it freely) for the export and additive import having shipped, rather than asking the user.
Not before: 2026-09-28

#### Submit Throughliner to Anthropic's community marketplace, as step one toward in-app browsability [marketplace-submission]
**Your goal, 2026-08-22: actual release to the Claude marketplace so people can browse for it inside the desktop app.** The research (`resources/research/claude-marketplace-listing-paths.md`) found two routes: the official marketplace is the only one browsable in-app by default, is curated at Anthropic's discretion, and has no self-serve path — the submission form feeds the community marketplace instead. So the realistic sequence is community first: submission via the clau.de/plugin-directory-submission form, automated security scanning plus human review, a public listing at claude.com/plugins pinned to a commit SHA; then official at Anthropic's discretion.
What a keep must settle: ending the pre-release posture CLAUDE.md declares ("in active testing, not ready for the Claude marketplace") — the user's decision; version-consistency discipline (plugin.json, changelog, git tags — the commonest reported rejection cause; the weekly release cycle [weekly-release-cycle] supplies the cadence for it, and a changelog does not yet exist); and confirming the name is final, since a marketplace slug is immutable once published and a rename breaks every install. The submission itself is a `[user]` step — a web form Claude cannot submit.
Runs behind [weekly-release-cycle] in spirit — a regular release rhythm is what makes the version discipline real — carried as this sentence rather than a blocker, since the submission decision is independently the user's.
**Reframed 2026-08-22, same session: the listing is the stable channel of the three-channel model settled on [beta-tester-pathway].** The research question this paragraph used to flag is answered — see below.
**Your sequencing, 2026-08-22, revised the same day: the listing launches alongside the beta channel rather than after it** — your first thought was beta testers before any listing, revised when it emerged the listing may be the only realistic way testers arrive; the listing is framed honestly as early instead. YouTube videos come after both, on your reasoning that videos without a listing would look bad to viewers while YouTube may bring the very first users. Written on both items per the known-ordering rule.
**Update-cadence research answered, 2026-08-22** (`resources/research/claude-marketplace-listing-paths.md`, listing-updates section): the listing's commit pin updates **only after re-review**, and no turnaround is documented anywhere — so the Wednesday stable promotion cannot push to the listing. The realistic shape: the weekly stable channel lives on this repo, and the listing is updated on a slower submit-and-wait rhythm — monthly, or when something worth announcing lands — worded as "submit the update".
**Your decision, 2026-08-22: the not-ready-for-the-marketplace posture ends.** You are ready to remove it; the one thing genuinely holding the submission is company registration, which is [abr-identity-and-address] on the flintcraft.tech project's queue — designed there with its research done. A dependency note was sent to that project's INBOX the same day (recorded in `INBOX/sent.md`); it asks no new work, only flags that a second project now waits. Whether the submission form itself actually requires registered-business details is unverified — check at keeping.
**Dated 2026-08-22 with your approval.** It waits on the ABR work in another project, which nothing in this queue can build; a month out is when there is plausibly news. Not offered again before then. Still to settle at the eventual keep: the changelog, and confirming the Throughliner name is final (the slug is immutable).
**Understudy ordering, your decision 2026-08-22: the launch does not wait for it.** Understudy debuts as the standard companion app with the YouTube videos (already last in the chain); the listing stays silent on it until it is real. Until a companion app honouring the editing-state contract is out, launch materials carry one honest line: don't edit the project docs while a run is writing them. A dependency note went to Understudy's own project INBOX the same day (recorded in `INBOX/sent.md`). Written on both this item and the beta-channel item per the known-ordering rule.
Not before: 2026-09-22

#### [user] Discord post draft: subprojects [discord-post-subprojects]
Drafted 2026-08-25 at the planning close under the close-sweep design; approved as a candidate by you, with your addition of the start-big benefit. Waits on [subprojects-pop-out] shipping; verify against the shipped build before posting (one-a-day pacing repealed 2026-08-28). FAQ potential noted for posting time, per the announcement-time FAQ rule.
Not before: 2026-08-29
**Draft (under 2,000 characters):**
> **Subprojects: start big, split later.** When one part of your project outgrows the rest — the software inside a business plan, the contracts inside a venture — you can now pop that subfolder out into its own full Throughliner project. Run setup inside the subfolder: it reads the parent project's spec, works out which part this is, checks with you, and tells the parent it's moved out. From then on it's an ordinary project with its own clear queue.
>
> The quiet benefit: you don't have to understand your project's final shape at the start. If the idea is nebulous and multi-parted, start it as one big project, rest assured that any part which grows a life of its own can be popped out later.
>
> The link back is deliberately simple: work in a subproject can hold up work in the parent — never the other way round — so the popped-out piece marches forward on its own terms, and anything crossing between them travels as mail you approve, never as one project silently editing another. One thing to know going in: there's no scripted way to pop a subproject back in, so it's for parts that have genuinely outgrown the nest.

#### [user] Discord post draft: multi-person sessions [discord-post-multi-person]
Drafted 2026-08-25 at the planning close under the close-sweep design; approved as a candidate by you, with your additions: name Chagora — your new app by its-coughfee, designed to work with Throughliner but not dependent on it — and credit zebbern. Both names are published GitHub identities, which is what the scrub rule permits. Explanatory register. Waits on [multi-user-identity-layer] shipping; verify against the shipped build before posting (one-a-day pacing repealed 2026-08-28).
Not before: 2026-08-30
**Draft (under 2,000 characters):**
> **Several people, one session — and everyone's ideas stay theirs.** Throughliner now understands a session with more than one person in it. Anyone present can drop ideas into the queue; the decisions — what gets kept, built, or published — stay with the one person holding the reins. Credit follows whoever's message raised an idea, under the same fairness rules as ever: agreeing to a suggestion doesn't make it yours, and Claude's own proposals stay Claude's.
>
> Identity can be as solid as you want it. Where people join through a Discord server, Discord's own account-linking can stamp members with a verified GitHub login — no custom bot — so contributions arrive under an identity someone actually proved. And contributors get real credit where it counts: commits carry co-author lines, so their work shows on GitHub itself, using only details they've chosen to share.
>
> This grew out of real use: **Chagora**, a new app by its-coughfee, is built to work with Throughliner (though it doesn't depend on it) and runs exactly this shape — a team prompting one session from a shared channel. Credit also to zebbern for the upstream groundwork.

#### [user] Discord post draft: session-flow smoothings [discord-post-session-smoothings]
Drafted 2026-08-25 at the planning close under the close-sweep design; approved by you as an announcement for now, with the note that it carries the makings of several FAQ entries — authored at posting time per the announcement-time FAQ rule, as may the other four drafts each in their own right. Waits on [build-refuses-user-queue-move], [end-of-queue-gate-refill-and-standing-intent] and [build-view-delete-ask-at-close] shipping; verify against the shipped builds before posting (one-a-day pacing repealed 2026-08-28).
Not before: 2026-08-31
**Draft (under 2,000 characters):**
> **A round of session-flow smoothings.** Small changes, each removing a moment of friction:
>
> **Your word carries mid-build.** Tell a build run to move a queue item — skip this, shelve that — and it does it, says so in one line, and carries on. The run still never rearranges your queue on its own initiative; what changed is that your explicit instruction goes through instead of being deferred to a later session.
>
> **The wrap-up question behaves.** The end-of-session ask returns when new ideas refill the queue and it empties again — and if you tell a session you're keeping it open as a drop-box for ideas while you work elsewhere, it stops offering to wrap up for the rest of that chat.
>
> **Housekeeping goes quiet.** The temporary file a build run reads from is cleaned up silently at the close and kept out of your repository — no more being asked about a file you never created.

#### Should cycles get mermaid diagrams? [cycles-mermaid-diagrams]
Captured by you, 2026-08-24, mid-planning — your framing: seems reasonable. Filed at your direction without discussion, so the idea is unshaped: what a diagram would show (a cycle's steps? the turn's two events? due-ness over time?), where it would live (in CYCLES.md beside the definition, or generated), and who reads it are all open for the keep-step. Context worth having there: the desktop app renders mermaid in its markdown viewer, and the cycles doc is user-facing by design.
Skipped 2026-08-26 on Claude's recommendation and your agreement: what settles it is a build that must ship first — [weekly-release-cycle] creating this project's first real cycles doc, with the due-ness check working ([cycles-check-fires-nowhere]'s fix). A diagram designed before any real cycles doc exists would be guessing at a document nobody has seen; take it up once there is one to draw.
Held 2026-08-27 with the capture bow-out field; that blocker built ([weekly-release-cycle] shipped, CYCLES.md exists) and the capture returned 2026-08-28.

**Re-held 2026-08-28 on Claude's recommendation and your agreement, behind the rituals build.** Two grounds, both to be answered by the eventual design: a diagram is a second copy of the steps that nothing checks — the parser reads fields, so a stale diagram misleads silently, and the likely answer is that the diagram is authored and updated only by whichever build amends the definition; and the doc's shape is changing under it — [ritual-definitions-and-offers] adds ritual definitions to the same doc, so a diagram drawn now is drawn on a moving target. Not deleted: once the doc carries several definitions and rituals, a rendered diagram is cheap to read (the desktop app renders mermaid) and genuinely orienting.
Blocked by: [ritual-definitions-and-offers]

#### Tip candidate: the readiness line, and the two things that stop a build run [tip-readiness-line]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.

Observed: the "Running /next" how-to post claims several ready items build back-to-back, but never explains the line in the queue that decides which ones — `--- Cleared to run above this line ---`, positioned at a planning close, with Claude narrating where it sits whenever it moves. Nor does anything cover `Runs alone`, the one other bound, which stops a run before work that must not share it because a rename or folder move would make another item's paths stale mid-build.

Why it matters: a user reading the queue sees that line and has no way to learn what it is. It is also the feature that makes an unattended run safe — the run stops at a boundary the user set while planning, rather than running on into work nobody has vetted. Both bounds belong in one tip: what the line is, that you set it, and what makes a run stop early.

#### Tip candidate: how work gets held, and how it lets itself go again [tip-holding-work]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.

Observed: SPEC describes work sitting below the readiness line for exactly two reasons written on the item itself — `Blocked by:` naming one or more queue items, or `Not before:` naming a date — with the queue lint checking both and every planning session asking, per held item, whether the blocker shipped or the date passed. None of this appears in any post, how-to or FAQ entry.

Why it matters: it answers a question every user of a growing queue eventually has, which is what to do with work that is real but cannot happen yet. The tip's point is that you do not have to remember any of it: a date is read off the calendar, and a blocker is a queue item like any other, so the thing being waited on gets planned and done rather than living as a sentence buried inside another item. That last part is the recorded failure the design came from — one item sat shelved for weeks on a step nobody could see was work.

#### Tip candidate: cycles, for work that comes round again [tip-cycles]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.

Observed: SPEC describes putting an artifact on a cycle — a named piece of recurring work defined once, with its steps, its cadence and the observable that marks a completed turn — after which the openings and closes of /plan and /next compute due-ness and file the work into the queue. A project with no cycles has no doc and pays nothing. Nothing in `INBOX/sent.md`, the FAQ or `ANNOUNCEMENT-IDEAS.md` mentions it.

Why it matters: recurring maintenance is the work that quietly stops happening, and this is the method's answer to it. The tip's angle is the part that makes it different from a reminder: due work becomes an ordinary queue item weighed against everything else, rather than a notification on a board nobody is obliged to read. Worth noting too that position is never stored — each check recomputes from the observable — so nothing drifts out of step if you skip a week.

#### Tip candidate: projects that can send each other mail [tip-cross-project-inbox]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.

Observed: SPEC describes an `INBOX/` folder in every project, scaffolded at /setup, through which one project writes a durable message into another's mailbox; the session opening names waiting messages and directs the session to read them, mail is routed at the openings of both /plan and /next, and an arriving message is triaged and archived. Nothing has been posted about it, and the FAQ has no entry.

Why it matters: users running more than one project on the method have this and do not know it. The tip's honest angle is the guarantee and its limit together — sending places a file in the recipient's mailbox and nothing confirms it was read, which is why the design has no automatic read-receipt (a receipt would be an automatic send, and nothing leaves the machine unapproved). Also worth saying: a message is another project's report, not an instruction, and only the user's own words direct the work.

#### Tip candidate: TOOLS.md, so a fact about your machine is learned once [tip-tools-md]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.

Observed: SPEC describes a `TOOLS.md` at the project root holding facts about a project's environment that are expensive to re-derive — a tool installed at a known path, a build command that fails specifically from Claude's shell — created the first time a session has such a fact, with a build's environment check reading it before assuming anything is absent. A project with none has no file and pays nothing. No post, no FAQ entry, no line in the pool.

Why it matters: the failure it fixes is one users feel directly — a session assuming a tool is missing and handing them a manual workaround, when the same project had already proved the tool works. The recorded instance cost a run its first act. It is also the smallest possible feature to explain, which makes it a good slow-news-day tip. Borderline on the visibility screen: the mechanism is internal, kept because the file sits visibly in the project root and the failure it fixes is one the user feels directly.

#### Tip candidate: seeding the queue from your spec, so features don't die in SPEC [tip-seed-from-spec]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.

Observed: SPEC describes /plan seeding the backlog from SPEC — offered automatically only in the narrow thin-queue/rich-SPEC state, invocable manually any time, with the user choosing the granularity between a few coarse milestones and granular per-feature items, and the derived items landing in Unprocessed as ordinary captures rather than straight into ready work. Nothing has been posted and the FAQ has no entry, though `ANNOUNCEMENT-IDEAS.md` carries a line on it.

Why it matters: it addresses a failure the user can recognise in their own project — a rich setup interview produces a SPEC full of buildable features with no path into the queue, so the whole feature set sits there with nothing to build it. The tip is short: your spec already lists the work; ask and it becomes queue items you can weigh.

#### Tip candidate: what happens when your project falls behind the plugin [tip-keeping-projects-current]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.

Observed: SPEC describes three checks at every session start — flagging whole docs the project is missing, topping up a doc missing a newer setting, and halting the session outright when the project's documents are on an older format than the plugin expects — plus the deliberate design that a plugin version change on its own produces no notice at all. Nothing has been posted about any of it and the FAQ has no entry.

Why it matters: the halt is the strongest thing the method does to a session, and a user who meets it with no warning will read it as a fault. It also carries a reassurance worth stating: the migration edits documents rather than replacing them, the top-up never overwrites anything the user wrote, and the format number is deliberately not the version number so it cannot cry wolf at every release.

#### Tip candidate: why Claude writes first and reports, and how to ask for the opposite [tip-write-first-and-show-first]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.

Observed: SPEC describes write-first approval settled by one test — is the previous version recoverable without the user's help? — with queue items, captures, LOG entries, SPEC edits and ordinary build edits written first and reported, while a commit message, anything leaving the machine, and a wholesale conversion of an untracked document are shown first. It also describes the user being able to ask for show-first at any time, for the rest of that session, with the switch moving only toward more showing. No post, no FAQ entry.

Why it matters: this is the single most visible behaviour difference a new user notices, and without the explanation it reads as Claude changing their files without asking. The tip's honest half is the trade the design accepts: a file briefly holds content the user has not agreed to, which is cheap in a git repository, and the real risk is not rejection but the user not noticing — which is why the report has to name its artifact precisely enough to open. Pairs naturally with the queued [discord-post-plain-english-consent] draft; whether they are one post or two is a decision for processing.

#### Tip candidate: the freeform tag, for work a build run must not touch [tip-freeform-flavor]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.

Observed: the "Running /next" how-to post names `[audit]` and `[user]` and stops there. `[freeform]` — work done by hand rather than by /next, because it is large or because it characteristically cannot run inside a run — is never mentioned in any post or FAQ entry, though it is one of the four flavors and the one /next halts on outright rather than skipping.

Why it matters: a user meeting an unexplained halt has no way to tell a deliberate stop from a fault. The tip also carries the clearest example the method has of why the flavor exists: a repair to the machinery /next itself depends on cannot run inside a run, because running the broken mechanism to build past it is the failure. Worth stating that most freeform work never passes through the queue at all — it is just you and Claude working by hand, and the close reads the edits as expected work.

#### Tip candidate: what the scrub gate does, and what it will never promise [tip-scrub-gate-limit]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.

Observed: SPEC describes a hook scanning QUEUE.md, SPEC.md and LOG entries for credential shapes, alongside Claude reading its own writing against a checklist — personal names, case details, third-party data, identifying paths — at the three moments text enters a committed doc. It also states the limit that must never be softened: no pattern can tell whether a sentence quietly identifies a real person, so the method never tells a user their artifacts are scrubbed or safe to publish. Nothing has been posted and the FAQ has no entry.

Why it matters: this is the one place the project deliberately under-claims, and saying so publicly is worth more than the feature. A user deciding whether to make a repository public needs the honest answer — that not publishing these artifacts is the only complete protection — and they will not get it from a tool that markets the gate. Post it as the limit first and the mechanism second. Borderline on the visibility screen: the gate itself is invisible, kept because the tip answers a question users actually ask — whether their repo is safe to publish.

Note for processing: this is a tip about a safeguard, not an announcement of a change, so it fits the tips test ("explains one Throughliner feature") rather than the news test.

#### Tip candidate: the advisory note a close leaves for the next planning session [tip-forward-advisory]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.

Observed: SPEC describes /done filing a "Last session advises…" note at the top of Unprocessed when it closes with a concrete recommendation, which the next /plan reads and deletes in the same breath — surfacing it is what consumes it. It never moves into Processed and is never treated as real work. The close also records whether it filed one or judged it unnecessary, and cannot complete until it has. Nothing has been posted, and the FAQ has no entry.

Why it matters: users see this note in their queue and have no way to know it is transient rather than work. The tip explains the one thing that makes it safe — it is advice, not a command, and it clears itself — and carries a nice detail about why the clearing moved to the read: a build run passing between two planning runs used to leave a consumed note behind, so the next planning session opened on advice about work that had already shipped.

#### Law-prose article announcement carries the why behind removing the why-clauses [law-prose-article-announcement-carries-the-why]
Raised by you 2026-08-27, while rejecting the rationale-split draft — the one constructive note in that rejection, filed rather than acted on because you set it aside for now ("that's neither here nor there").

Your point: the draft was worthless because it described where the reasoning went, when the interesting story is **why the why-clauses were removed at all**. That reasoning — a rule with its justification attached is a longer rule, a model follows fewer instructions reliably as they lengthen, and an irrelevant or same-sounding rule degrades the ones around it — is a real finding about how these tools behave, and it is the sort of thing worth reading even if you never touch Throughliner.

Your placement for it: not a standalone post, but part of a larger announcement alongside the **upcoming law-prose article**. That gives it the length it needs and an occasion, which a tip about an internal reorganisation never had.

Bears on the deleted [announcement-rationale-split-correction], whose record (`LOG/2026-08-27-announcement-rationale-split-correction.md`) carries the full critique of what a post on this subject must not do.

Note for processing: this waits on the law-prose article existing, which was not a queue item when this was filed.
**Wired 2026-08-28:** the blocker is now filed as [law-prose-article] — real committed work, publicly promised in the user's 2026-08-26 beta announcement ("a website article coming") — and this capture bows out until it resolves, returning by itself when the article item is processed or built.
Blocked by: [law-prose-article]

#### Migrate this project's rezip, push and release prose into ritual definitions [host-rituals-migration]
Filed 2026-08-28 with the keep of [ritual-definitions-and-offers], from your framing that the release and rezip rituals are subparts of cycles. Host-only: move the step lists in `resources/release-ritual.md` (and CLAUDE.md's push section, if it fits the shape) into ritual definitions in `CYCLES.md`, with the weekly-release cycle naming the release ritual as its turn's steps rather than restating them. Not designed yet — what stays prose (the recovery procedures, the marketplace-collision guard) and what becomes definition is the keep-step question.
Blocked by: [ritual-definitions-and-offers], [rezip-archive-mirrors-nerds-channel]
The second blocker is ordering, not just concept: that item is rewriting the same ritual text right now, and two items editing `resources/release-ritual.md` must not interleave.

#### Demo-session guide for the legal-case YouTube video [legal-demo-video-guide]
**Your idea, 2026-08-28, processed at raising.** One of the first YouTube videos: an essentially unscripted demo where you set up a fresh legal-case-shaped project with Throughliner on camera, phrasing your questions as though you don't know what Claude will suggest, and steering toward a structure similar to one you already proved — a family-law source-of-truth template and method in your legal project (located 2026-08-28; the path and matter names are deliberately not recorded here, per the scrub rule on identifying paths). You never show or use the template; the guide's job is knowing the destination so your naive-sounding questions reliably arrive there. Your virality read: a legal case is a very weird project type to run inside Claude Code, which is exactly why it travels.

How it gets made: hand-work with you in a dedicated session — the drafting reads the legal project's sensitive files, so it is done deliberately with you present, not inside a build run. Output lands in `YouTube/` (gitignored once [youtube-folder-gitignored] ships), which keeps the guide and any matter-adjacent notes out of this public repository. This capture holds the intent; the dedicated session does the work, and the close there records it.
Blocked by: [youtube-folder-gitignored]
The hold is real: the guide must not be written into a tracked folder, so the ignore line lands first.

#### Pop the YouTube folder out into its own project [youtube-subproject-popout]
Your direction, 2026-08-28: the `YouTube/` subfolder starts life inside this project and pops out as its own full Throughliner project later — your timeframe, "maybe in a month or something", written as the date below and adjustable on your word. The pop-out is the shipped subprojects flow: /setup run inside the subfolder reads this project's product truth, confirms which part it covers with you, and tells the parent it moved out. Until then the folder is gitignored working space ([youtube-folder-gitignored]).
Not before: 2026-09-28

#### Slides-to-video route for the Throughliner introductory video [slides-transform-intro-video]
**Your idea, 2026-08-28, filed at your direction as a deliberately vague concept to ripen.** The slide deck from your 2026-08-27 Throughliner presentation becomes the introductory video — possibly the channel's featured video — via the Slides-to-video transform you discovered. The transform has no automation route, so the conversion itself is your work; this session's Google Drive connection can read the deck's content at design time to script narration or plan the video around it. The deck's share link is on file in `INBOX/` (gitignored — the link carries your account id, so it stays out of this committed file). Design belongs with the other YouTube work: [legal-demo-video-guide], the `YouTube/` folder, and the eventual pop-out.

#### Lesson video: deterministic versus probabilistic output, taught through Throughliner's tool-finding [determinism-lesson-video]
**Your idea, 2026-08-28, filed at your direction; the arc and the heuristic are yours.** A different video type from the legal-case demo — a lesson, not a case study, though it carries case-study elements rather than being example-free (your framing).

The arc: first show what Throughliner does when it finds tools for you — accomplishing things it is not necessary to use AI for. Then identify what is different about those tasks: beyond not needing the AI directly, their output is **deterministic**. The teachable heuristic, in your words: *a good way to recognise when an output is deterministic is when you can imagine a tool that might accomplish it.* The payoff is double — you stop spending valuable AI generating things a different way every time (probabilistically), and you start identifying and suggesting CLI tools yourself, even when Claude Code hasn't.

Grounding on the shelf: the method's own CLI-tool rule and capability check ("name the tool that would do the work") are the shipped behaviour the lesson demonstrates. Designs with the other video captures — [legal-demo-video-guide], [slides-transform-intro-video] — in the YouTube folder's own sessions.

#### Reusable priming prompt for demo recording sessions [recording-priming-prompt]
Filed 2026-08-28 from the site project's mail (archived same day), the idea Alex's — raised in that project's planning session and sent here as the side that owns it. A prompt given to Claude before any case-study recording session: this session is a demo, and it must not put revealing information on screen. Her reason, carried from the mail: demoing a real personal project exposes more than the method being shown — the structure of the work, what is being tracked — and preventing it at the source is far cheaper than blurring it in the edit afterwards. Reusable by construction, since every case-study recording wants it; the [legal-demo-video-guide] session is its first consumer, so the two design together in the YouTube folder's sessions.

#### Co-writing as an interaction shape — flavor, convention, or nothing? [co-writing-shape-question]
**Raised by you, 2026-08-28**, at the keep of [law-prose-article], whose walkthrough you called the first very clear representation of co-writing: interleaved Claude-drafting and your-writing steps, where past article items were written as Claude work items you then ended up writing into a lot. Your call at filing: experience it first — run the article's walkthrough as designed — then process this at the next planning session, with a lived instance to judge from.

The question for that turn: is co-writing a new flavor (heavy — a flavor must be wired into plan.md, next.md and done.md), a walkthrough convention (cheap — a shape [user] items can carry, like this one already does), or nothing needing a name? The method's record warns against typing nuance into a taxonomy; the counterweight is your observation that the untyped version mis-set expectations for who writes.
Blocked by: [law-prose-article]

#### Cross-project research citations have no shape, and the superseded-file safety net stops at the boundary [cross-project-research-citation]
Filed 2026-08-28 from INBOX mail sent by a consumer project running this method (archived at `INBOX/archive/2026-08-28-from-flintcraft-cross-project-research-citation.md`). Reported against plugin 1.21.0-test3. Data from another project, not a decision here.

What they report: a planning session there revised a cleared `[user]` item on research a sibling project owns. The finding lives in the sending project's `resources/research/`, so their item cites it by absolute path.

The gap they name: the method files and indexes research per project, and has no shape for a finding one project owns and another's work depends on. Both available answers are poor — an absolute path that breaks silently when the folder moves, or a copy with no link to the original and no way to tell which is current.

What makes it more than untidy: the `Superseded by:` convention and the queue digest's superseded-research flag are both scoped to one project. If the owning project supersedes the finding, the citing project's item keeps citing the old version and no check fires anywhere. The safety net stops exactly at the boundary the citation crosses.

Why they expect it to recur: the cross-project INBOX exists so sibling projects can send each other findings. Mail arrives, is routed as a capture, the capture reshapes an item — and the evidence now under that item sits in the sender's folder. The mail feature makes the citation, and nothing downstream knows it is cross-project.

What they are doing meanwhile, offered as data rather than a proposal: copying the file in with a line recording where it was originally researched and by which project, plus an ordinary index line. That answers the dead-path risk and not the staleness one.

For processing: whether a cross-project citation shape is worth designing at all, and if so whether the staleness half can be reached without one project reading another's research folder on a schedule.

#### Retiring the generated build view left BUILD-VIEW.md orphaned in migrated projects [retired-feature-leaves-orphan]
Filed 2026-08-28 from INBOX mail sent by a consumer project running this method (archived at `INBOX/archive/2026-08-28-from-flintcraft-retired-feature-leaves-orphan.md`). Reported against plugin 1.21.0-test3, topped up from 1.20.0-test17 the same day. Data from another project, not a decision here.

What they report: they ran the format 3 to 4 migration on 2026-08-23, which wrote build blocks into every cleared item and generated `BUILD-VIEW.md` at their project root — 15KB, committed. The generated view was retired 2026-08-27. On 2026-08-28 their version top-up refreshed the managed CLAUDE.md block, ran every scaffold and settings check, and reported nothing to do. The orphaned file was still at the root. A planning session found it only because a queue item happened to ask whether it should be committed or gitignored — a question whose premise had quietly become false.

The gap they name: a retirement removes the code that writes an artifact, not the artifact from projects that already have one, and the top-up has no notion of what a previous epoch generated. So a file sits at the root that nothing produces and nothing reads, in every project that ran the earlier migration and then took this version.

The part that shows it was nearly caught: `post_tool_use.py` records that the `--- Build block ---` delimiters were deliberately left alone, because they read as ordinary text now and rewriting them would edit records to match a vocabulary they predate. That reasoning covers the text inside the queue; the retirement also had a file outside it, which no note mentions.

Why they call it worth more than one deletion: the orphan explains itself to nobody — a user opening the folder finds a large unowned file at the root, and the honest answer takes reading the plugin source. Theirs is deleted; every other migrated project still has one.

For processing: this bears on this project's own eviction rule, which already requires that retiring a step retires the artifacts that step produced. The rule fired for the in-queue half and not for the generated file, and nothing sweeps artifacts already sitting in consumer projects — so the question is whether the top-up gains a retired-artifact sweep, or whether the eviction rule gains a limb about artifacts already distributed.

#### [audit] Rule changes since the last compliance audit are uncovered [compliance-audit-lag]
Filed 2026-08-28 by `resources/rule_signals.py`'s audit-lag check, under the slug it prints. Nothing had filed it and the slug was open in neither section.

The check reports rule-bearing commits since `2026-08-27-compliance-audit-lag.md` that no compliance audit has covered. The count will have grown by the time this is processed: the run filing it is itself editing most of the files below.

**Delta scope — the files the uncovered commits changed:** `CLAUDE.md`, `plugin/throughliner/docs/done.md`, `feedback-and-inbox.md`, `next.md`, `plan.md`, `rescan.md`, `setup.md`, `skill-nonspecific-rules.md`. Re-run the check at processing rather than trusting this list — it is a snapshot, and the audit should be scoped to what the check reports on the day.

The standing criteria are in `resources/method-compliance-audit-checklist.md`: four lenses — self-authoring compliance, response-shape tag placement, narration drift, and decision history in operative text. Reads only; findings go straight to Unprocessed as captures.

#### [user] Tip: your projects can send each other mail [tip-recycle-cross-project-inbox]
**Recycle from the #announcements post of 2026-08-12, "Your projects can now talk to each other"** (message id 1537247086179786772). Found by the announcement-history sweep of 2026-08-28, which mined the channel's full history — the early posts predate the sent register, so nothing had looked at them for tip material.

Passes the tip test: it explains one feature. Passes visibility: a user running two projects sees the waiting-mail line at a session opening and the INBOX folder in their own project.

What a tip would walk through, rather than merely reporting the capability exists: where the folder is, what a session opening says when mail waits, that a planning session opens it and files what it contains, that nothing is sent without seeing the exact wording, and that the folder is gitignored.

**Drift check before drafting — the original is 16 days old and the feature has grown since.** Build runs now open mail too, not only planning sessions; an address book records a correspondent's path on first use; `INBOX/sent.md` records what went out. The original post lists the first two as "coming next". Re-verify every claim against the installed build at drafting.

#### [user] Tip: what /next does with your spec while it builds [tip-recycle-spec-read-at-build]
**Recycle from the #announcements post of 2026-08-14, "Spec-driven development, finally the right way round"** (message id 1537631817849380925). Filed by the announcement-history sweep of 2026-08-28.

Passes the tip test: one feature — SPEC.md read at the start of a build run, each item checked against it, and a halt naming the sentence it contradicts. Passes visibility: the user sees the halt, in their own words, in a run they are sitting in.

**Drift is material here and the recycle must not reuse the wording.** The original's last bullet says a build establishing new product truth "asks first, adds SPEC.md to its own file list, and edits it in the same commit". That is repealed: a build now files the sentence it thinks SPEC owes as a capture and never writes SPEC, because the session that made a choice is not the session that certifies it. A recycle that reuses the old bullet would announce behaviour the plugin no longer has.

#### [user] Tip: the work cycle, and the two ways work comes back to the start [tip-recycle-work-cycle-loop]
**Recycle from the #announcements post of 2026-08-21, "Claude can now tell you how its own work cycle fits together"** (message id 1540223708210270219). Filed by the announcement-history sweep of 2026-08-28.

Passes the tip test: it explains one thing the plugin has — the loop the four commands sit in. Passes visibility, though it is the weaker of the two limbs: the user does not see the rules file, but they do live the loop, and "which command do I run now?" is a question they actually ask.

A tip here is the walk-through the original was not: capture, plan, next, done, fresh session — plus the return edges, which are the part a flat list misses. An audit files findings back into the queue; a build that discovers something files it and carries on; a step that is yours leaves the loop only when you have done it.

Borderline on visibility, and recorded as such: the original's subject was partly the internal fix (a section added to the rules). The tip has to be about the loop the reader is in, never about the section that was added.

#### [user] Tip: why your old queue items stop getting skipped [tip-recycle-ordering-ladder]
**Recycle from the #announcements post of 2026-08-23, "your old queue items stop getting skipped"** (message id 1540901808090783824). Filed by the announcement-history sweep of 2026-08-28.

Passes the tip test: one feature — the order a planning session works through unprocessed captures. Passes visibility strongly: the user watches items being presented in that order, and the complaint it answers ("why does the same item keep coming up?") is one they actually voice.

The original already reads close to a tip. What a recycle adds is the how-to half: what to look for in the one-line narration naming the order used, and that naming a few items to start with sets the order rather than the length of the run.

**Drift check:** the ladder's rungs are described in SPEC as they now stand — re-read that before drafting rather than trusting the post's four-line list, which was written to an earlier shape.

#### [user] Tip: what the planning close does to your queue, and what it deliberately leaves alone [tip-recycle-close-reorder-restraint]
**Recycle from the #announcements post of 2026-08-10, "Token savings, and most of them are things we're going to stop doing"** (message id 1536412983499165746). Filed by the announcement-history sweep of 2026-08-28.

Passes the tip test: one feature — the single pass the planning close makes over Processed, batching the steps that need you to the end. Passes visibility: the user can open QUEUE.md and see that their items sit in the order things landed, with the human stops grouped at the bottom.

The angle that makes it a tip rather than a changelog: file order records *when things landed*, and that is more useful than a ranking that goes stale. Three other reorders were removed to keep it that way.

**Drift check:** the post's framing is a savings announcement, which is the internal-arrangement shape the visibility rule now excludes. The recycle keeps only the user-facing half — what your queue looks like and why — and drops the token-saving story entirely.

#### Announcement-history sweep: subjects considered and passed over [tip-recycle-sweep-coverage-note]
Filed by the announcement-history sweep of 2026-08-28 so its coverage is checkable rather than only its output. Not work — a record of what the sweep looked at. Delete it once read, or keep it as the sweep's own coverage note.

All 22 posts in #announcements were read, back to the channel's first message (2026-07-30). Five reshape into tips and are filed above. The rest were passed over, with grounds:

- **2026-07-30 forum topics; 2026-07-31 the Sovereign Implementer rename; 2026-08-25 the Fable graduation and support channels; 2026-08-26 the first beta and nerd role; 2026-08-27 v1.21.1** — project news, not a feature explained. Two of them are already covered by shipped FAQ entries.
- **2026-07-31 terse docs; the five 2026-08-03 posts on the terse-docs experiment, the pseudocode research, the measurement harness and the doc-size defence; 2026-08-09's three rollback and law-prose posts; 2026-08-10's `plugin-behaviour.md` retirement** — every one fails the visibility test. They describe how the method's own text is arranged, which is the exact class the posting brief now excludes. Their proper home is the law-prose article, which [law-prose-article] already owns.
- **2026-08-08 learning mode** — a feature that was never built. The shipped-only rule bars it.
- **2026-08-22 "builds no longer read your queue"** — the claim is FALSIFIED. The generated build view was retired on 2026-08-27 and builds read the queue again. This must not be recycled, and it is the one post in the channel whose subject is actively wrong; whether a correction is owed is a question for processing, noting that the post's other half (the comparison article) is separately owned by [comparison-article-post-needs-rewrite].

#### Co-writing as a work flavour, with each claim processed like a capture [co-writing-flavour]
**Raised by you, 2026-08-28**, mid-walk-through of [law-prose-article], looking at that item's step 1 — the fourteen-claim list produced before drafting. Your idea: process each claim the way /plan processes a capture, one at a time with a disposition, rather than showing the set and asking for changes by number. Your second thought in the same breath: this might inform a new co-writing work flavour.

**Why it lands where it does.** [law-prose-article]'s own keep already records that its walkthrough is the first clear representation of **co-writing** — interleaved Claude-drafting and user-writing steps, rather than a Claude work item the user ends up writing into. This is the next question that observation raises: whether co-writing is a shape the method should name and execute, or a walkthrough pattern that happens to recur.

**What the claims list exposed, which is the concrete evidence.** The set was shown as one numbered message and the ask was "anything missing, anything to cut, or shall I draft?" That is the candidate-set inversion — deliberate for a deterministic result set under approved criteria. But a claims list is not that: each claim is a separate editorial decision with its own weight, its own honest limit, and its own reason to survive or go. Two of the fourteen needed a marginal flag precisely because a flat set could not carry a per-item verdict. Processing them one at a time would have produced fourteen recorded dispositions instead of one bulk approval.

**Against it, so the design question is real rather than rhetorical.** Fourteen sequential turns is the over-asking this method has spent months removing, and the inversion exists because a set the user reads at once is cheaper for them. The question worth settling is what distinguishes a set that inverts from a set that must go one at a time — the candidate answer being whether each item carries a decision of its own, or the criteria were agreed in advance and the items merely satisfy them.

**If a flavour is admitted it is not a small change.** The standing rule: a new work-item flavour must be wired everywhere it is read — `plan.md` (how it is marked and placed at the decision step), `next.md` (execution routing), `done.md` (close routing and whether the close announces it). The queue lint holds no list of valid flavors, so it needs nothing. A flavour also needs the rule gate run at the decision step, with its disposition written onto the item there.

**An outbound message about this is wanted and is deliberately NOT sent yet — your instruction, 2026-08-28.** You asked to hold it so it does not muddy a test running in a parallel session at the time this was filed. You will say when that test is done. Nothing has been drafted or sent. Whoever picks this up: do not send on the strength of this paragraph — the send needs your explicit yes to the exact text, like every outbound artifact.

**A note for whoever processes this, about the session it was filed in.** A parallel session was running on the user's machine while this was captured. This project's rules say to work on a project from one chat at a time, because a capture filed in one chat is invisible to the other; whether that parallel session was on this project or on a consumer project was not established at filing.

#### Self-scoping derives Files from Changes and misses what the observable needs [self-scoping-misses-observable-files]
Found live 2026-08-28, twice in one /next run, and filed by /rescan at that run's end.

/next's self-scoping step reads each item whole and lists the files its instructions name. In practice it reads the **Changes** line, because that is where files are named. An item's **Observable** line routinely names others — the suite that must pass, the sibling doc the acceptance test greps — and those went missing from the Files list both times.

- [cycles-fields-are-single-line] named `session_start.py` in Changes and required "the suites under `resources/testing/` pass, with a case covering a wrapped field" in its observable. Writing that case needed a file the lock denied.
- [ca-commit-steps-untagged] named two close docs in Changes and set its observable as "no untagged commit step remains in the done family" — which `done-audit.md` violated, a third file the finding never noticed.

Both were added to the run's Files list before editing and recorded at the tick, so nothing was built outside an agreed scope. The cost was two interruptions in a run that is meant not to need them.

**Worth weighing at processing: the fix may belong at /plan rather than /next.** The decision step already requires an item to state what changes inside the files it names; it does not require the Files line to cover the files the observable reaches. A scoping step that read both lines would catch it, and so would a decision-step limb requiring the observable's files to appear in Files. The second is cheaper and fires with the user present.

Related: the repeal-grep limb already makes the decision step trace a change's ripple by grep. This is the same shape one field over.

#### A [user] walkthrough can assert unchecked facts about an outside surface [walkthrough-asserts-unchecked-surface]
Found live 2026-08-28, when [howto-posts-bot-authorship] was driven and halted at its own step 3.

Its walkthrough assumed two things about Discord that nobody had checked, and both are load-bearing: that each how-to topic is a single post, and that the user can delete her opening post so the bot's replacement stands in its place.

Reading the live forum found six topics each holding between two and five further messages of hers plus an attachment — so re-homing "the post" leaves those under her name in a topic the bot would present as its own. And a forum topic's opening message shares its id with the topic, which raises the question of whether deleting it destroys the topic and the bot's replacement with it. A search was run on the user's go and did not settle it: one Discord support thread implies the topic survives with its subtitle reading "Original message was deleted", another was summarised as the opposite, and the developer documentation is clear only about the different case of a thread started from an existing message in a text channel.

**The general shape, which is what makes this worth processing rather than only fixing the one walkthrough.** The rule built earlier the same day covers a doc sentence asserting what a *tool* can do: run the read that would verify it, or write it as intended rather than as fact. A walkthrough step asserting what an outside *surface* permits is the identical failure at a site that rule does not reach — and it is worse there, because a walkthrough is handed to a non-coder to perform with nobody to ask.

Weigh against the project's ban on speculative rules: this is one recorded instance, which the gate accepts as a pointable failure. The candidate fix is an amendment to the same what-would-answer-this rule rather than anything freestanding.

**A safe test exists for the specific question and was not run:** the bot can create its own throwaway topic in the forum and delete its own opening message, which settles it with nothing of the user's at risk. Not run because it posts to a public onboarding forum and needs her say-so.

#### View-in-doc pointing fails a reader who cannot open the file [rendering-for-a-reader-away-from-the-files]
**Raised by you, 2026-08-28**, in the middle of a `[user]` walk-through: *"sorry can you please give it to me as a card? I'm on remote control"*. Filed by /rescan at the run's end.

The always-loaded render rule is unconditional and deliberately so: text already living in a project doc is surfaced as a one-line pointer plus a link, never re-pasted, with no user override and no stored setting. The reasoning behind removing the override still stands — the reader away from the file is served by the plain-English summary that opens each item's discussion.

That reasoning assumes the reader *could* open the file if they wanted to. On remote control there is no filesystem to open, so the pointer resolves to nothing and the summary is all there is — which is fine for one queue item and not fine for a fourteen-part deliverable the user is being asked to approve item by item.

What this session did instead, offered as data rather than as the proposal: published the list as an artifact and gave her the link. That worked, and it is not in any rule.

**Worth weighing at processing.** The rules already know about being driven remotely — the show-first section names it and refuses to make it a separate trigger, on the ground that no detection is built to reach an outcome that asking reaches. The same answer may serve here: the user asks, and nothing detects. What is missing is not detection but the *option* — nothing tells a session that rendering a long deliverable as a page is available, so it is reached for by improvisation rather than by rule. **Consider also whether this is one instance or a class**, since the same gap would appear for any long approval set put to a user who is not at the machine.

#### The Cowork origin month lives in one article's walk-through record and nowhere else [cowork-origin-month-unrecorded]
**Your account, 2026-08-28**, given while settling the law-prose article's opening claim: the method was originally developed inside Cowork, for roughly a month, because you were too scared to use Claude Code. That is what reconciles your "about four months old" with this repository's first commit of 2026-06-01.

It is written into `LOG/2026-08-28-law-prose-article-2.md` as part of claim 1's disposition, because that is where it was said. That is a poor home for it: a session wanting the project's origin story would look at `CLAUDE.md`'s plugin-history section, which currently begins at the 2026-06-01 rebuild and says nothing about what came before.

The change is one or two sentences added to that section, naming the Cowork period and why the repository starts where it does. Small, and it is the kind of fact that is unrecoverable once the person holding it stops being asked.

#### Compaction leaves a detectable tell, so /rescan's "undetectable" claim is too strong [compaction-has-a-designable-tell]
**Raised by you, 2026-08-28**, on hearing /rescan say its limit sentence out loud. Your words: *"isn't it pretty easy to tell? You wouldn't see the normal artifacts left over from /next running if compaction had occurred. This is an easy tell we can design"*.

**What the method currently says, and why it is now in question.** `rescan.md` states that where the conversation has been summarised the memory of it is gone, "and that is undetectable from the inside, exactly as a compaction is". The required limit sentence follows from that: *I can't tell whether any of our earlier conversation has dropped out of view*. The whole design of the stopping point — held in the conversation, no durable marker, refused as a new artifact — rests on the undetectability claim.

**Your observation is right and the claim is too absolute.** A /next run leaves structurally recognisable traces: the session-opening block, the run presented at the off-ramp, and one tool exchange per item ticked. A session that can still see those has not had them summarised away.

**The stronger version, which is what makes it mechanical rather than introspective: cross-check the conversation against durable artifacts on disk.** The build working file records exactly which items were ticked. If it lists thirty and the conversation shows the work of six, the difference is not a judgement about memory — it is two counts that disagree. The same holds for `LOG/` entries this chat wrote, and for captures already in the queue. The filesystem remembers what the conversation may not.

**The asymmetry is the important part, and a check that ignores it would be worse than the honest disclaimer.** Compaction takes the *earliest* material first. So:

```
expected artifacts ABSENT   ->  positive evidence something dropped out.
                                Reliable, and worth saying out loud.
expected artifacts PRESENT  ->  proves the recent window is intact and
                                NOTHING about the earliest stretch —
                                which is exactly what /rescan reaches for.
```

**So the finding admits a warning, never an all-clear.** A check reporting "I can see the artifacts, so nothing was lost" would hand the user a false guarantee at the one moment they are relying on the scan to be complete. The current sentence over-claims ignorance; the naive fix would over-claim knowledge.

**Candidate shape at processing, not chosen here:** keep the limit sentence as the default, and add a second, louder statement for the case where the cross-check *fails* — where the conversation cannot account for work the files record. That is new information the user does not otherwise get, and it fires only when it has something to say, which is the shape this project's checks already take.

**Worth settling alongside it:** whether this reaches `done.md`'s wind-down re-scan too, which looks back over the same conversation for the same reason and inherits the same blind spot.

#### Augmentatism article: where Throughliner fits the philosophy and where it fails its central claim [augmentatism-article-material]
Filed 2026-08-28 from INBOX mail sent by the flintcraft.tech site project (archived at `INBOX/archive/2026-08-28-from-flintcraft-augmentatism-article-idea.md`).

**Provenance is unusual and binding: the analysis in the mail is Claude's reading, not the user's.** She raised the idea and named its centre — an article on all the ways Throughliner is so augmentatist, and so not, especially the Law of Creative Latency, which she calls Throughliner's strong suit — then deliberately stopped before reading the analysis, so as not to prime herself. She is writing her own commentary on the manifesto and intends to cross-pollinate the two. Nothing in the mail's reading may be presented back to her as her position.

The source is `https://augmentatism.com/`, a manifesto by Manolo Remiddi. The mail's summary of it is a fetch from 2026-08-28 and is to be re-verified before drafting. The mail's candidate shape: Throughliner satisfies the philosophy's principles almost point for point — Creative Latency most of all, since the method's whole shape is friction placed on purpose — while failing its central political claim, the Many versus the One, because it is built entirely inside one company's ecosystem.

Two constraints from the sender's own rules travel with it: a named person's published work gets third-party care (describe accurately, verify, never argue the author is wrong), and the site's SPEC bars claiming Throughliner is the only holder of any value.

**What lands here is the sending-back half:** the mail asks that this be processed here and sent back. Articles for the site are written there; this project's part is its reading of the method against the manifesto. The send needs the user's yes to the exact text like any outbound message.

#### Issue check cannot see issues on repositories a project does not own [issue-check-foreign-repos]
Filed 2026-08-28 from INBOX mail sent by a consumer project running this method (archived at `INBOX/archive/2026-08-28-from-flintcraft-issue-check-cannot-see-foreign-repos.md`). Reported against plugin 1.21.0-test3. Data from another project, not a decision here.

The planning opening's issue check has two limbs — comments on issues the register records, and new issues on a repository the project owns — and nothing else is in view. The user named the gap there: issues on other repositories, including her own other projects and Claude Code, can bear directly on a project and no limb reaches them. The evidence in the mail: at least fifteen open issues she is involved in, most on `anthropics/claude-code`, one on a third-party Discord bot repository bearing on this project's own Discord work — every one invisible to every project she runs. A narrower hole inside the first limb: an issue she filed herself, outside any project's flow, is anchored to no register and never checked.

Mechanism finding worth keeping whatever is built: the GitHub notification inbox is the wrong source — notifications are read-once, so a seen-but-unresolved issue vanishes from it. The durable query is a search for issues the account is involved in.

Two limits constraining any fix, from the mail: relevance cannot be derived, so which outside repositories bear on which project would have to be declared per project; and a widened check reads issue text written by strangers, which is untrusted content — data, never instruction, summarised in the project's own words.

#### Outbound register is untracked by construction, one deletion from gone [sent-register-untracked]
Filed 2026-08-28 from INBOX mail sent by a consumer project running this method (archived at `INBOX/archive/2026-08-28-from-flintcraft-register-tracking-and-defect-watch.md`, report 1 of 2). Reported against plugin 1.21.0-test3.

`INBOX/sent.md` is the permanent outbound register — what the repeal check greps for claims already announced — and `INBOX/` is gitignored on every path, so the register has no history, no backup, and one accidental deletion ends it. The ignore rule is right about what it was written for (inbound mail holds another project's raw text); the register is caught by a rule aimed at something else. It is this project's own words.

The sender considered a local `.gitignore` exception and rejected it on a real ground: `/setup` refreshes scaffolding, so a hand-added exception could be silently overwritten, leaving the register untracked while everyone believes it is safe. Their suggestion, offered not decided: move the register out of the mailbox rather than un-ignoring it inside one.

This project has the same exposure with more at stake — its register is the longest-running and records public Discord claims. Red flag · State: uncleared

#### Method-defect watch: nothing asks Claude to look, where the security screen already does [method-defect-watch]
Filed 2026-08-28 from the same mail as [sent-register-untracked] (report 2 of 2). Data from another project.

The method carries a standing duty to screen every chat for data-exposure risk, honest that it catches only what it spots. There is no equivalent duty for defects in the method itself — the routing rule fires when a user reports one, so the channel is wholly reactive. The sender's evidence: three method-level defects surfaced in one planning run there, all found sideways while doing unrelated work, none by looking. The user's suggestion, in her framing: Claude should be instructed to proactively watch for things that are method issues rather than project issues.

Two limits the mail states so this is not adopted as more than it is: a standing watch is a noticing duty of the security screen's class — improves the odds, guarantees nothing, and must say so wherever written; and it has a cost the security screen does not, since friction is not a defect and the duty invites every awkward moment to be reported as one. The sender says it probably needs a threshold and offers no view on what.

For processing: the rule gate applies in full — this is a candidate always-loaded rule, the most expensive kind, and the admission question is whether the reactive channel's misses are a pointable failure or the sender's three sideways finds are evidence the noticing already happens without a rule.

