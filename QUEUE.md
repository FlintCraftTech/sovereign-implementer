# QUEUE

Two sections. **Processed** — agreed work, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** — captured, not yet processed; the next /plan weighs each item. Every entry in either section is a `#### ` heading (its description) with a `[slug]` at the end of that line and its rationale beneath; an entry in Unprocessed is a **capture**, and it becomes a **work item** when /plan keeps it into Processed. A leading `[audit]` / `[user]` tag names how it's executed; no tag means a build. An item carrying a security or privacy risk gets a `Red flag · State: …` marker — the flag rides the work.

**Authoring a rule for the method's own text? The rule gate is in `CLAUDE.md`, always loaded — run it before you write.**

## Processed

#### The beta channel: each Wednesday's pick offered via Discord and a GitHub pre-release [beta-tester-pathway]
**Your idea, 2026-08-22, designed in the same session into a three-channel model — the standard release-channel shape (Chrome/Firefox), adopted on your terminology question.** Your day-to-day rezips are dev builds, yours alone and unchanged by this. Each Wednesday's pick becomes the **beta**: announced on the Throughliner Discord, hosted as a GitHub pre-release (Discord cannot host an install; the release ritual already builds and attaches zips), and offered to willing testers while it soaks for a week — you as the only tester at first, which is better than nothing and still a beta channel. After its week it promotes to **stable** and goes to the community listing ([marketplace-submission]). This superseded the earlier two-route question (repo-at-HEAD versus per-rezip artifacts): the weekly-pick artifact route won because it gives testers your chosen moments rather than every commit, and it reuses release machinery rather than adding a publish step to every rezip.
**Your sequencing, 2026-08-22, revised the same day: the channels launch together rather than beta-then-listing** — the community listing is itself part of how testers arrive, so the chain is beta channel + community listing (honestly framed as early), then YouTube videos pointing at them. Written on both items per the known-ordering rule.

**Kept 2026-08-22, held behind [weekly-release-cycle].** The three things the capture left open are settled. **Install route: a ref-pinned marketplace add** — research done at processing (`resources/research/claude-marketplace-listing-paths.md`, beta-channel section): a marketplace-add pins to a branch via `#ref`, so a `beta` branch fast-forwarded to each Wednesday's pick serves testers through the README's existing ask-Claude install shape, and no tester touches a zip; the pre-release zip stays as the release artifact. The research caveat travels: some ref-handling behaviour is covered by open feature requests, so the walkthrough is smoke-tested on a real second machine before any tester gets it. **Naming, your decision at processing: one cycle, called the release cycle** — beta is a step inside the Wednesday turn, not a sibling cycle; this build amends the one definition rather than adding another. **Offer wording:** drafted in the build, honestly-early testing framing; the launch announcement is the `[user]` line [beta-launch-announcement], filed with this keep.

--- Build block ---
Changes: amend the release-cycle definition in the cycles doc so one Wednesday turn carries both events — fast-forward the `beta` branch to the newest week-old rezip's commit, and promote last week's beta to the stable release; create the `beta` branch. `README.md` — add a beta-channel section: what beta means (honestly early), the tester install walkthrough (ask Claude to add the marketplace `FlintcraftTech/throughliner#beta` and install), and how updates arrive. Draft the Discord beta-offer announcement text into [beta-launch-announcement]'s walkthrough.
Acceptance: the cycles doc still parses under the shipped check with the two-event turn; the `beta` branch exists; README's beta section reads for a non-coder and matches the walkthrough smoke-test caveat (not offered to testers until smoke-tested); the announcement draft is under 2,000 characters.
Refused: a separate beta cycle with its own cadence — one cycle, beta as a step (the user's call); zip-download installs for testers — the ref-pinned marketplace add replaces it; a separate beta repo — a branch suffices.
--- End build block ---
**Understudy ordering, your decision 2026-08-22: the beta launch does not wait for it** — Understudy debuts as the standard companion app with the YouTube videos, after this channel and the listing; until then the beta materials carry the one-line caution against editing project docs while a run writes. Written on both this item and the marketplace item per the known-ordering rule.
**Read [expedite-first-beta-release] before building this, 2026-08-26.** Alex's labelled test-rezip list would give the Wednesday pick a defined candidate set, which this item never had. It does not collide with the ref-pinned install decided here — the list is zips for people who want raw dev builds, testers still install from the `beta` branch — but it changes what the pick selects from, so the two are designed together or not at all.
**Selector settled 2026-08-26, your decision, recorded in full on [weekly-release-cycle]:** the Wednesday beta pick is the most recent stable-labelled rezip from the nerds list; the stable release is last week's beta promoted after its soak. This item's two-event turn is unchanged in shape — only what the pick selects from changed.
**Install half advanced 2026-08-26:** [beta-branch-install-pin] creates the `beta` branch at today's expedited release and points README/INSTALL at `#beta`, with the second-machine smoke test as [beta-install-smoke-and-post-edit]. What remains here is the cycle wiring — the two-event Wednesday turn — and the announcement draft; this item's build reconciles its block against what those two already shipped.
**Lifted 2026-08-27.** [weekly-release-cycle] shipped and was verified in the same run — `CYCLES.md` now exists with the weekly Wednesday definition, checked by running the installed parser against it rather than by reading the file. So the definition this item amends is there to amend, and the hold is dropped.
**Files:** the cycles doc, `README.md`, QUEUE.md (the announcement item's walkthrough). The dependency is real, not just conceptual: the definition this amends is created by [weekly-release-cycle]'s build.

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

**The Discord post is this item's final step rather than a separate item — the user's decision.** Order: verify, draft the article, ship the digest work, finish the article with what actually shipped, then write the post. **Nothing is published without the user seeing the exact text and giving an explicit yes**, and Claude has no route to Discord or to the site — the user posts both.

**One thing to resolve at drafting.** The site is another project, so the article is drafted here and delivered rather than written into that repository. Whether that delivery is an INBOX message or the user carrying it across is a question for the moment it is ready.

**The blocker has shipped and the `Blocked by:` line is dropped, 2026-08-15.** [digest-reports-computed-fields-not-summaries] has a LOG entry, so the digest work the article was waiting to describe now exists.

**Verification done 2026-08-15, in the /plan session that processed this — and it changed the argument rather than confirming it.** `resources/research/auto-memory-staleness.md` was re-checked and partly corrected; its index line carries the correction too. Two material findings:

- **AutoDream is live.** It consolidates memory between sessions — merging facts, deleting contradicted notes, converting relative dates to absolute, trimming the index — triggering automatically after roughly 24 hours plus five sessions, and **a manual `/dream` command is available to everyone** regardless of rollout state. The research file's claim that it is not running was two months stale. **This sharpens the weakness the draft already admits:** automatic curation is no longer something only competitors have, it is in the base tool this plugin runs on. An article treating manual curation as a fair trade must say so, and the honest framing is why typed documents and user-approved deletion are worth the manual cost — not that the alternative is unavailable.
- **"Obsidian memory systems" is a category, not a project.** Several independent implementations exist, some with semantic search, self-rewriting notes and scheduled maintenance agents, plus Obsidian's own official Agent Skills for Claude Code from January 2026. So the article names the specific project it compares against, or says plainly it is describing the general vault-as-memory pattern. Describing "the Obsidian memory system" as one thing is the wrong-about-a-third-party failure this item was right to guard against.

**Tagged `[user]` at processing 2026-08-15**, matching the other post items rather than inventing a shape: Claude drafts the article and the post, the user publishes both.

**Only the final step yields to the one-a-day chain.** Three posts are queued ahead of it, and the pacing rule applies to the post rather than to the writing — so the item is cleared and the article can be drafted whenever. Carried as prose today because there is no way to write a date; once [not-before-date-field] ships, this becomes a `Not before:` line.

**Walkthrough.** Authored 2026-08-22 at processing, closing [article-walkthrough-missing].
1. Claude re-checks the two 2026-08-15 findings still hold before drafting — AutoDream's status, and whether "Obsidian memory systems" now names a specific project — offering a fresh web search; anything changed is corrected in `resources/research/auto-memory-staleness.md` first. You'll see what the check found before the draft starts.
2. Claude drafts the full article: names the specific system it compares against or says plainly it describes the general vault-as-memory pattern, and is honest that automatic curation now ships in the base tool — the case made is why typed documents and user-approved deletion are worth the manual cost.
3. You read it and say what to change; repeat until you're satisfied.
4. You decide delivery: an INBOX message to the site project (you see the exact text first) or you carry the file across yourself. Claude does whichever you pick that it can.
5. Claude drafts the Discord post — under 2,000 characters, the shipped fix as its subject, pointing at the article.
6. You publish both — Claude has no route to either. The post yields to the one-a-day chain: it goes out on a day no other Throughliner post does.
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
Filed 2026-08-22 with the keep of [beta-tester-pathway], which drafts the announcement text into this walkthrough as part of its build. The offer is framed honestly early — a testing invitation, not a product launch — and yields to the one-a-day posting chain like every other post. Launches alongside the community listing per your sequencing recorded on [beta-tester-pathway] and [marketplace-submission].
**Walkthrough.**
1. The draft is in this item once [beta-tester-pathway] builds; Claude walks you through any final edits.
2. Before posting, the tester install walkthrough must have been smoke-tested on a second machine — confirm that happened; do not post an install route nobody has run.
3. You post it on Discord, on a day no other Throughliner post goes out — Claude has no route to Discord.
4. You confirm; the send is recorded in `INBOX/sent.md` with what it claimed, and this line closes.
Blocked by: [beta-tester-pathway]
**Files:** none — the artifact is a Discord post.

#### [user] Approved Discord post about the comparison article now describes a superseded draft [comparison-article-post-needs-rewrite]
Found by Claude 2026-08-23 while walking the comparison-article item. A Discord post was drafted and approved on 2026-08-22 and has not gone out — it is recorded on `INBOX/sent.md` as approved and not yet posted, with its text verbatim in `LOG/2026-08-22-competition-comparison-article.md`. Its second paragraph announces the article and describes it as closing "on the coherence-over-scale trade", which was true of the 2026-08-22 draft.

That draft is superseded. The 2026-08-23 rewrite names a specific project rather than a category, adds a section on Papi as the nearest comparable tool, and ends on a shipped mechanism instead of a general trade-off — roughly 1,400 words against 900. A hold-note has already gone to the site project asking that the old one not be published.

**So the post cannot go out as approved.** Its first paragraph, about builds reading a generated view rather than the queue, was still true when this was filed and is falsified as of 2026-08-27: [builds-read-the-queue-again] retires the view, so both paragraphs now need rewriting at step 2 — the first against the shipped read-the-queue model, the second against the final article. The claim was approved but never posted (`INBOX/sent.md`), so no public correction is owed. The rewrite runs after the article settles — it is currently out for review with the maker of one of the tools it names, and that review may change what the article ends on.

**Walkthrough.** 1. The article settles (external review back, revised text final). 2. Claude rewrites the post's second paragraph against the final article and shows the whole post. 3. You say what to change. 4. You post it, with the live article URL pasted in — Claude has no route to Discord. 5. You confirm, `INBOX/sent.md` is updated from approved-not-posted to posted, and this line closes.

**This is the repeal-falsifies-an-announcement case caught before it fired**, rather than after: the claim was recorded on the sent register, and the register is what made the collision findable when the article changed. It is also why the register records what a post claimed rather than merely that one exists.

**Kept 2026-08-24, held below the line on Claude's recommendation and your agreement.** As a capture this carried its ordering in prose because captures have no `Blocked by:`; as a held work item it carries the field, so it lifts by itself when the article item closes instead of being re-offered every session while the external review is out. The same ordering sentence is written on the article item per the known-ordering rule.
Blocked by: [competition-comparison-article]

#### [user] Re-home the how-to forum posts under the bot's authorship [howto-posts-bot-authorship]
Filed 2026-08-27 with [posting-rule-two-kinds-and-tip-pipeline], from your instruction that the how-to topics be editable and maintainable by the bot. The constraint that makes this an item at all (recorded in `TOOLS.md`): a bot can only edit messages it authored itself, and the existing how-to posts are yours — so bot maintainability requires each one re-posted by the bot once, after which every later tweak is a bot edit under the approval rule.

**Walkthrough.**
1. Once the posting script exists, Claude fetches each how-to post's current text through the bot and shows it to you unchanged. Look for: the text matching what the forum shows.
2. On your yes per post, the bot posts the replacement in the same topic. Look for: the new post appearing under the bot's name.
3. You delete your original post of each (only you can — the bot cannot delete or edit your messages in a forum topic it doesn't manage, and your authorship is the thing being replaced). Look for: the topic showing only the bot's copy.
4. The register line for each how-to post is updated to point at the bot's copy, with the channel named; this item closes when every how-to topic's live text is bot-authored.
**Blocker re-pointed 2026-08-27, not lifted.** [discord-posting-bot] shipped and was verified live — the bot posted to #tips and read the message back byte-identical — so the thing this waited on exists. But the same run measured the bot's per-channel permissions and found it **cannot post in the how-to forum**, which is where step 1 of this walkthrough goes. Lifting it now would clear work that stops at its first step. The hold moves to [bot-needs-howto-send-permission], which is the grant that has to happen first.
Blocked by: [bot-needs-howto-send-permission]

## Unprocessed

#### Last session advises processing release-validation-chain-findings next [forward-advisory]
Advice from the third 2026-08-27 session's close, not work. The next planning session reads this and deletes it in the same breath. It replaces the spent advisory that session cleared at its opening.

**Why this one first.** That capture points at `resources/research/release-validation-chain-broken.md`, whose root finding — validation always runs on a build the working tree has already moved past — cost this session its planning time: the close had to re-derive by hand which commit the tested build was before the user's off-cycle release could run. Until the chain is fixed, every release request repeats that derivation. Overlap check: nothing in the 38 waiting captures contradicts it, and two ([beta-tester-pathway-files-line-names-queue], the tip screen) are independent of it.

**Condition:** this stops being the right first item once the four findings in that file have dispositions, whatever they are.

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

**Dated 2026-08-21 with your approval; the date stands.** The reply it waited on has arrived, so when the date passes this is taken up on its merits rather than re-dated.
Not before: 2026-08-28

**One thing to settle at processing regardless of their answer:** a `[user]` item's text can name real people or client details, so what crosses the boundary needs the scrub the queue already gets, and a pushed task is leaving this project's records.

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

#### [user] Discord post draft: issue-first problem reporting [discord-post-issue-first-reporting]
Drafted 2026-08-25 at the planning close under the close-sweep design; approved as a candidate by you, with your addition of the GitHub-CLI-recommended mention. Waits on [method-feedback-issue-first] and [plan-open-github-issue-check] shipping; verify against the shipped builds before posting; one-a-day chain applies.
Not before: 2026-08-28
**Draft (under 2,000 characters):**
> **Report a problem, get the answer back automatically.** When something in Throughliner misbehaves, Claude now offers to file it as a GitHub issue on the Throughliner repository for you — drafted, shown to you word for word, and posted only on your yes. (An issue is public under your GitHub account; if you'd rather stay private, the report form is still there.)
>
> The reason issues are worth it: they're two-way. Your planning sessions now scan your correspondence at their opening — waiting mail, answers on issues your project filed, and new issues arriving on your own repository — so a reply reaches you without you checking anywhere or remembering to. And if you want a follow-up on a report, say so when it's sent: a dated reminder lands in your queue and surfaces on its day, with the checking method already agreed.
>
> For all of this, the GitHub command line tool (`gh`) is a highly recommended companion to Throughliner — everything degrades gracefully without it, but the two-way channel is what you'd be missing.

#### [user] Discord post draft: subprojects [discord-post-subprojects]
Drafted 2026-08-25 at the planning close under the close-sweep design; approved as a candidate by you, with your addition of the start-big benefit. Waits on [subprojects-pop-out] shipping; verify against the shipped build before posting; one-a-day chain applies. FAQ potential noted for posting time, per the announcement-time FAQ rule.
Not before: 2026-08-29
**Draft (under 2,000 characters):**
> **Subprojects: start big, split later.** When one part of your project outgrows the rest — the software inside a business plan, the contracts inside a venture — you can now pop that subfolder out into its own full Throughliner project. Run setup inside the subfolder: it reads the parent project's spec, works out which part this is, checks with you, and tells the parent it's moved out. From then on it's an ordinary project with its own clear queue.
>
> The quiet benefit: you don't have to understand your project's final shape at the start. If the idea is nebulous and multi-parted, start it as one big project, rest assured that any part which grows a life of its own can be popped out later.
>
> The link back is deliberately simple: work in a subproject can hold up work in the parent — never the other way round — so the popped-out piece marches forward on its own terms, and anything crossing between them travels as mail you approve, never as one project silently editing another. One thing to know going in: there's no scripted way to pop a subproject back in, so it's for parts that have genuinely outgrown the nest.

#### [user] Discord post draft: multi-person sessions [discord-post-multi-person]
Drafted 2026-08-25 at the planning close under the close-sweep design; approved as a candidate by you, with your additions: name Chagora — your new app by its-coughfee, designed to work with Throughliner but not dependent on it — and credit zebbern. Both names are published GitHub identities, which is what the scrub rule permits. Explanatory register. Waits on [multi-user-identity-layer] shipping; verify against the shipped build before posting; one-a-day chain applies.
Not before: 2026-08-30
**Draft (under 2,000 characters):**
> **Several people, one session — and everyone's ideas stay theirs.** Throughliner now understands a session with more than one person in it. Anyone present can drop ideas into the queue; the decisions — what gets kept, built, or published — stay with the one person holding the reins. Credit follows whoever's message raised an idea, under the same fairness rules as ever: agreeing to a suggestion doesn't make it yours, and Claude's own proposals stay Claude's.
>
> Identity can be as solid as you want it. Where people join through a Discord server, Discord's own account-linking can stamp members with a verified GitHub login — no custom bot — so contributions arrive under an identity someone actually proved. And contributors get real credit where it counts: commits carry co-author lines, so their work shows on GitHub itself, using only details they've chosen to share.
>
> This grew out of real use: **Chagora**, a new app by its-coughfee, is built to work with Throughliner (though it doesn't depend on it) and runs exactly this shape — a team prompting one session from a shared channel. Credit also to zebbern for the upstream groundwork.

#### [user] Discord post draft: session-flow smoothings [discord-post-session-smoothings]
Drafted 2026-08-25 at the planning close under the close-sweep design; approved by you as an announcement for now, with the note that it carries the makings of several FAQ entries — authored at posting time per the announcement-time FAQ rule, as may the other four drafts each in their own right. Waits on [build-refuses-user-queue-move], [end-of-queue-gate-refill-and-standing-intent] and [build-view-delete-ask-at-close] shipping; verify against the shipped builds before posting; one-a-day chain applies.
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
Held 2026-08-27 with the new capture bow-out field, so it stops being re-offered while the wait runs: the blocker is now cleared to run, and this returns by itself once it is built.
Blocked by: [weekly-release-cycle]

#### Three queue items still tell the user to post to Discord by hand [queue-walkthroughs-say-claude-cannot-post]
Noticed by Claude during the 2026-08-27 build of [discord-posting-bot], filed rather than done: the build tried to correct the wording and the scope-lock refused it, correctly — rewording a queue item's prose is work on the queue's contents, which is planning. The build's own Changes line had listed it, so this is the part of that item that could not be built where it was written.

Three walkthroughs claim Claude has no route to Discord, which the bot falsifies: [beta-launch-announcement] step 3, [comparison-article-post-needs-rewrite] step 4, and [competition-comparison-article] step 6 — that last one only in its Discord half, since Claude genuinely has no route to the flintcraft.tech site and the user does publish the article. Each should read that Claude posts through the bot on the user's explicit yes to the exact text; the one-a-day pacing and the approval gate are unchanged either way.

Left standing costs a walk-through: a session driving one of these hands the user a manual step the tool can now do, which is the over-tagging the capability check exists to catch.

#### [user] Describe the install-from-zip route once, in the test-rezips pin or a how-to post [install-from-zip-route-described]
Split out of [rezip-posts-its-entry] during its 2026-08-27 build. That item scoped the description as part of the build; it cannot be built, because the pin in test-rezips-for-nerds was posted by the user and a bot can only edit messages it authored itself (TOOLS.md). So the writing is Claude's and the posting is the user's — the ordinary shape for anything leaving the machine.

Now that every test-rezips entry carries a zip of the exact build it describes, a nerd downloading one needs to be told what to do with it: extract it, then add the extracted folder as a local marketplace. Nothing on the channel says this, so the attachment currently arrives with no instructions.

Framed honestly as bleeding-edge work, per the pin's existing register. Whether it belongs in the pin or in its own how-to topic is a judgment for processing — the how-to set's number stays small and a new topic is the user's call, so the pin is the cheaper default.

**Walkthrough.**
1. Claude drafts the paragraph and shows the exact text.
2. You say what to change; repeat until you are satisfied.
3. Claude posts or edits it where it can — a bot-authored how-to post is a bot edit; the existing pin is yours to paste, since nobody can edit anyone else's Discord message.
4. You confirm it is live. Look for: the channel's pin or how-to naming the extract-then-add-local-marketplace route.
5. The send is recorded in `INBOX/sent.md` with its channel and what it claimed, and this line closes.

#### Audit-only runs never hear the rescan recommendation at their close [audit-close-missing-rescan-clause]
Noticed by Claude while building [rescan-before-done], 2026-08-27, and captured rather than folded in: that item scoped itself to two named sites — the end-of-queue gate in plan.md and the close hand-off in next.md — plus done.md's wind-down arm. It named next-audit.md nowhere, so extending to it would have been scope the user never agreed.

`next-audit.md`'s close step says: when the whole run is done, tell the user how many findings were filed, and say "Run /done to record this and commit, or keep reviewing." That is a close-naming sentence at the end of a run, which is exactly the moment [rescan-before-done] decided the rescan should be recommended — closing is on the table and the session is not mid-work. A run of only audit items therefore reaches its end and never hears the suggestion, while a run with a build item does.

The fix is the same one clause the other three sites now carry. `next-build.md`'s abort path is deliberately NOT included: it names /done after a failed item, which is a different moment.

#### Tip candidate: red-flag screening, which has never been posted about [tip-red-flags]
From the features-needing-tips audit, not yet reviewed.

Observed: SPEC describes screening every chat for anything that could expose the user's data or their users' data, surfacing it in plain English, and tagging the queue entry that carries it with a `Red flag · State:` marker — with a flag only clearing when the risk is designed out or the user consciously accepts it after being told plainly. Nothing in `INBOX/sent.md`, the FAQ index or `ANNOUNCEMENT-IDEAS.md` covers it. No announcement, no how-to line, no FAQ entry.

Why it matters: this is one of the method's five stated principles and one of the few things it does that a user would not think to ask for. It is also the feature most likely to reassure someone deciding whether to trust the tool with a real project. A tip would explain what gets flagged, that flagging is not fixing, and — honestly — that it catches what Claude spots rather than every risk that exists.

#### Tip candidate: the readiness line, and the two things that stop a build run [tip-readiness-line]
From the features-needing-tips audit, not yet reviewed.

Observed: the "Running /next" how-to post claims several ready items build back-to-back, but never explains the line in the queue that decides which ones — `--- Cleared to run above this line ---`, positioned at a planning close, with Claude narrating where it sits whenever it moves. Nor does anything cover `Runs alone`, the one other bound, which stops a run before work that must not share it because a rename or folder move would make another item's paths stale mid-build.

Why it matters: a user reading the queue sees that line and has no way to learn what it is. It is also the feature that makes an unattended run safe — the run stops at a boundary the user set while planning, rather than running on into work nobody has vetted. Both bounds belong in one tip: what the line is, that you set it, and what makes a run stop early.

#### Tip candidate: how work gets held, and how it lets itself go again [tip-holding-work]
From the features-needing-tips audit, not yet reviewed.

Observed: SPEC describes work sitting below the readiness line for exactly two reasons written on the item itself — `Blocked by:` naming one or more queue items, or `Not before:` naming a date — with the queue lint checking both and every planning session asking, per held item, whether the blocker shipped or the date passed. None of this appears in any post, how-to or FAQ entry.

Why it matters: it answers a question every user of a growing queue eventually has, which is what to do with work that is real but cannot happen yet. The tip's point is that you do not have to remember any of it: a date is read off the calendar, and a blocker is a queue item like any other, so the thing being waited on gets planned and done rather than living as a sentence buried inside another item. That last part is the recorded failure the design came from — one item sat shelved for weeks on a step nobody could see was work.

#### Tip candidate: cycles, for work that comes round again [tip-cycles]
From the features-needing-tips audit, not yet reviewed.

Observed: SPEC describes putting an artifact on a cycle — a named piece of recurring work defined once, with its steps, its cadence and the observable that marks a completed turn — after which the openings and closes of /plan and /next compute due-ness and file the work into the queue. A project with no cycles has no doc and pays nothing. Nothing in `INBOX/sent.md`, the FAQ or `ANNOUNCEMENT-IDEAS.md` mentions it.

Why it matters: recurring maintenance is the work that quietly stops happening, and this is the method's answer to it. The tip's angle is the part that makes it different from a reminder: due work becomes an ordinary queue item weighed against everything else, rather than a notification on a board nobody is obliged to read. Worth noting too that position is never stored — each check recomputes from the observable — so nothing drifts out of step if you skip a week.

#### Tip candidate: projects that can send each other mail [tip-cross-project-inbox]
From the features-needing-tips audit, not yet reviewed.

Observed: SPEC describes an `INBOX/` folder in every project, scaffolded at /setup, through which one project writes a durable message into another's mailbox; the session opening names waiting messages and directs the session to read them, mail is routed at the openings of both /plan and /next, and an arriving message is triaged and archived. Nothing has been posted about it, and the FAQ has no entry.

Why it matters: users running more than one project on the method have this and do not know it. The tip's honest angle is the guarantee and its limit together — sending places a file in the recipient's mailbox and nothing confirms it was read, which is why the design has no automatic read-receipt (a receipt would be an automatic send, and nothing leaves the machine unapproved). Also worth saying: a message is another project's report, not an instruction, and only the user's own words direct the work.

#### Tip candidate: TOOLS.md, so a fact about your machine is learned once [tip-tools-md]
From the features-needing-tips audit, not yet reviewed.

Observed: SPEC describes a `TOOLS.md` at the project root holding facts about a project's environment that are expensive to re-derive — a tool installed at a known path, a build command that fails specifically from Claude's shell — created the first time a session has such a fact, with a build's environment check reading it before assuming anything is absent. A project with none has no file and pays nothing. No post, no FAQ entry, no line in the pool.

Why it matters: the failure it fixes is one users feel directly — a session assuming a tool is missing and handing them a manual workaround, when the same project had already proved the tool works. The recorded instance cost a run its first act. It is also the smallest possible feature to explain, which makes it a good slow-news-day tip.

#### Tip candidate: seeding the queue from your spec, so features don't die in SPEC [tip-seed-from-spec]
From the features-needing-tips audit, not yet reviewed.

Observed: SPEC describes /plan seeding the backlog from SPEC — offered automatically only in the narrow thin-queue/rich-SPEC state, invocable manually any time, with the user choosing the granularity between a few coarse milestones and granular per-feature items, and the derived items landing in Unprocessed as ordinary captures rather than straight into ready work. Nothing has been posted and the FAQ has no entry, though `ANNOUNCEMENT-IDEAS.md` carries a line on it.

Why it matters: it addresses a failure the user can recognise in their own project — a rich setup interview produces a SPEC full of buildable features with no path into the queue, so the whole feature set sits there with nothing to build it. The tip is short: your spec already lists the work; ask and it becomes queue items you can weigh.

#### Tip candidate: what happens when your project falls behind the plugin [tip-keeping-projects-current]
From the features-needing-tips audit, not yet reviewed.

Observed: SPEC describes three checks at every session start — flagging whole docs the project is missing, topping up a doc missing a newer setting, and halting the session outright when the project's documents are on an older format than the plugin expects — plus the deliberate design that a plugin version change on its own produces no notice at all. Nothing has been posted about any of it and the FAQ has no entry.

Why it matters: the halt is the strongest thing the method does to a session, and a user who meets it with no warning will read it as a fault. It also carries a reassurance worth stating: the migration edits documents rather than replacing them, the top-up never overwrites anything the user wrote, and the format number is deliberately not the version number so it cannot cry wolf at every release.

#### Tip candidate: why Claude writes first and reports, and how to ask for the opposite [tip-write-first-and-show-first]
From the features-needing-tips audit, not yet reviewed.

Observed: SPEC describes write-first approval settled by one test — is the previous version recoverable without the user's help? — with queue items, captures, LOG entries, SPEC edits and ordinary build edits written first and reported, while a commit message, anything leaving the machine, and a wholesale conversion of an untracked document are shown first. It also describes the user being able to ask for show-first at any time, for the rest of that session, with the switch moving only toward more showing. No post, no FAQ entry.

Why it matters: this is the single most visible behaviour difference a new user notices, and without the explanation it reads as Claude changing their files without asking. The tip's honest half is the trade the design accepts: a file briefly holds content the user has not agreed to, which is cheap in a git repository, and the real risk is not rejection but the user not noticing — which is why the report has to name its artifact precisely enough to open. Pairs naturally with the queued [discord-post-plain-english-consent] draft; whether they are one post or two is a decision for processing.

#### Tip candidate: the freeform tag, for work a build run must not touch [tip-freeform-flavor]
From the features-needing-tips audit, not yet reviewed.

Observed: the "Running /next" how-to post names `[audit]` and `[user]` and stops there. `[freeform]` — work done by hand rather than by /next, because it is large or because it characteristically cannot run inside a run — is never mentioned in any post or FAQ entry, though it is one of the four flavors and the one /next halts on outright rather than skipping.

Why it matters: a user meeting an unexplained halt has no way to tell a deliberate stop from a fault. The tip also carries the clearest example the method has of why the flavor exists: a repair to the machinery /next itself depends on cannot run inside a run, because running the broken mechanism to build past it is the failure. Worth stating that most freeform work never passes through the queue at all — it is just you and Claude working by hand, and the close reads the edits as expected work.

#### Tip candidate: what the scrub gate does, and what it will never promise [tip-scrub-gate-limit]
From the features-needing-tips audit, not yet reviewed.

Observed: SPEC describes a hook scanning QUEUE.md, SPEC.md and LOG entries for credential shapes, alongside Claude reading its own writing against a checklist — personal names, case details, third-party data, identifying paths — at the three moments text enters a committed doc. It also states the limit that must never be softened: no pattern can tell whether a sentence quietly identifies a real person, so the method never tells a user their artifacts are scrubbed or safe to publish. Nothing has been posted and the FAQ has no entry.

Why it matters: this is the one place the project deliberately under-claims, and saying so publicly is worth more than the feature. A user deciding whether to make a repository public needs the honest answer — that not publishing these artifacts is the only complete protection — and they will not get it from a tool that markets the gate. Post it as the limit first and the mechanism second.

Note for processing: this is a tip about a safeguard, not an announcement of a change, so it fits the tips test ("explains one Throughliner feature") rather than the news test.

#### Tip candidate: the advisory note a close leaves for the next planning session [tip-forward-advisory]
From the features-needing-tips audit, not yet reviewed.

Observed: SPEC describes /done filing a "Last session advises…" note at the top of Unprocessed when it closes with a concrete recommendation, which the next /plan reads and deletes in the same breath — surfacing it is what consumes it. It never moves into Processed and is never treated as real work. The close also records whether it filed one or judged it unnecessary, and cannot complete until it has. Nothing has been posted, and the FAQ has no entry.

Why it matters: users see this note in their queue and have no way to know it is transient rather than work. The tip explains the one thing that makes it safe — it is advice, not a command, and it clears itself — and carries a nice detail about why the clearing moved to the read: a build run passing between two planning runs used to leave a consumed note behind, so the next planning session opened on advice about work that had already shipped.

#### Commit steps in both child close docs carry no response-shape tag [ca-commit-steps-untagged]
From the compliance audit of 2026-08-27 (delta scope), lens 2 — tag placement. Not yet reviewed.

Observed: `done-build.md`'s `### 2.4 Commit` and `done-plan.md`'s `## 2. Commit` both carry no tag. Their parent, `done.md`'s `## Commit core`, carries `[BRIEF, PROMPT]`. The inconsistency is inside `done-build.md` itself: its neighbouring `### 2.2 Staleness sweep` is also a bare pointer at a parent section and it *does* repeat the parent's tag — so the doc tags one pointer step and not the other.

Where each site fires: 2.4 fires at the end of a build close, immediately before the commit; done-plan's fires at the same point in a planning close; done.md's Commit core fires when either of them hands off to it.

Why it matters: the commit message is one of the few things the method always shows before it happens and waits on, so a missing `[PROMPT]` on the step that performs it leaves the wait to chance. A reader arriving at 2.4 sees an untagged step next to a tagged one and has no signal that this is a stopping point.

#### feedback-and-inbox.md carries no response-shape tags anywhere, though it drives approval-gated sends [ca-feedback-doc-untagged]
From the compliance audit of 2026-08-27 (delta scope), lens 2 — tag placement. Not yet reviewed.

Observed: the doc has four sections — Method problem reports, the method report route, the Claude Code report route, and Cross-project INBOX — and not one carries a tag. Every other procedure doc in scope tags its steps.

Where it fires: whenever a user reports a problem with the method or with Claude Code, and whenever mail is sent or triaged. These are the moments the doc exists for, and each of them ends in something leaving the machine on an explicit yes.

Why it matters: a send is the strongest `[PROMPT]` case the method has — the exact text is shown and the session stops — and the doc encodes that in prose rather than in the tag that exists for it. Lens 2 names this failure mode directly: prose where a tag belongs, with the tag being the mechanism the prose substitutes for. The doc is fetched rather than always-loaded, so a session arrives at it mid-task with only its own words to go on.

#### done-plan.md's repeal block is host history sitting in a doc consumers load [ca-repeal-block-in-shipped-doc]
From the compliance audit of 2026-08-27 (delta scope), lens 4 — decision history in operative text. Not yet reviewed.

Observed, at `done-plan.md` around line 96: after the operative rule — one pass over Processed, putting `[user]` and `[audit]` lines at the end — comes "Everything else the close used to reorder is repealed", followed by a fenced block headed "repealed — do not reinstate:".

The delete-and-read test cuts both ways here, which is why this is filed rather than asserted. Delete the sentence and the rule above it is complete, so by the strict test it is history. But the fenced block is addressed to a future author considering reinstating the behaviour, which is an instruction of a kind — and that author is never a consumer, because consumers do not author the method's steps.

Where it fires: at every planning close, in a doc that ships in the plugin package and is read by every consumer running /done after /plan.

Why it matters: whichever way the test lands, the audience is wrong. If it is history, it belongs in the LOG entry; if it is a do-not-reinstate instruction, it belongs in the host project's own files alongside the other host-only rules. Either disposition removes it from what consumers load. Worth deciding rather than leaving, since it is the clearest case in scope of a host concern shipped to people it can never apply to.

#### next-audit.md restates the empty-Files-list rule its parent already carries [ca-audit-restates-files-rule]
From the compliance audit of 2026-08-27 (delta scope), lens 1 — self-authoring compliance, eviction debt. Not yet reviewed.

Observed on the parent axis, `next-audit.md` against `next.md`. The child says an audit item names no files to edit, contributes nothing to the run's Files list, and that a run of only audit items has an empty list holding the session to the method docs. The parent's self-scoping step already says audit items name no files because an audit reads and reports, so a run of only audit items gets an empty Files list locking the session to the method docs.

Where each site fires: the parent's fires once at scope-lock, before any item is executed, when the Files list is being derived. The child's fires later, when the run routes to a particular audit item — by which point the list is already locked and cannot change. So this is not two plugs in two holes: the child's statement fires at a moment where it can no longer affect anything, and the session that reaches it has already read the parent.

Why it matters: this is the eviction-debt signature the lens looks for — a restatement that never repealed its prior. The disposition is likely consolidate-and-repeal with the parent keeping the rule, but the child may want a one-clause pointer so a reader arriving mid-run still knows why the list is empty. That call belongs at processing.

#### feedback-and-inbox.md narrates its own superseded earlier version inside the shipped doc [ca-superseded-version-narrated]
From the compliance audit of 2026-08-27 (delta scope), lens 4 — decision history in operative text. Not yet reviewed.

Observed, at `feedback-and-inbox.md` around line 328: "An earlier version of this doc rejected the return path outright, on the ground that it writes a path from this machine into another project's repository where it may be committed. That is superseded: the send now refuses unless the recipient's `INBOX/` is gitignored, so the file is never committed, and the refusal was costing real replies."

The delete-and-read test: remove the whole passage and what remains is a complete instruction — the send refuses unless the recipient's `INBOX/` is gitignored. So what was deleted was history, and it belongs in the LOG entry that decided it.

Where it fires: when a session is about to write into another project's mailbox — a moment where the operative rule is the refusal condition and nothing else.

A second, milder instance in the same doc, around line 302: "every reply used to be a fresh lookup the user performed by hand, however long the correspondence had run." Delete it and "Write an entry the first time the user supplies a path" still stands. Worth weighing separately — it reads closer to a purpose clause than the first one does, and lens 3 warns explicitly against evicting those.

Why it matters: this doc ships to consumers, who have no interest in which version of it rejected what. It is also the founding shape lens 4 was written to catch — history wearing rule syntax, with no "because" to give it away.

#### Reorder narration specimen shows the user bare slugs and nothing else [ca-reorder-specimen-bare-slugs]
From the compliance audit of 2026-08-27 (delta scope), lens 3 — narration drift. Not yet reviewed.

Observed, at `done-plan.md` around line 158, the specimen a session copies when it narrates a reorder: "Moved [slug-a] above [slug-b] so it builds first — say if not."

That contradicts two always-loaded rules at once. The Vocabulary section lists "slug" among the terms that name nothing in the user's own files, to be translated or omitted; and its queue-item arm requires that an item named in output leads with its heading's opening words, with the slug after them, plus what the item is for on first mention in each message.

Where it fires: at a planning close, in the one line the user reads about an ordering decision Claude made on their behalf — so it is precisely the moment the rule was written for, since a reorder they cannot parse is a reorder they cannot object to.

Why it matters: a specimen is stronger than a rule, because it is what gets copied. This one models the exact output the vocabulary rule forbids, in a doc that ships. The fix is a specimen naming both items by their opening words.

#### Audit-halt specimen offers a flat menu where the doc has a clear preference [ca-audit-halt-offers-menu]
From the compliance audit of 2026-08-27 (delta scope), lens 3 — narration drift. Not yet reviewed.

Observed, at `next-audit.md` around line 37, the specimen for halting when an audit item directs a write into a document: it ends "Want me to file them as captures, or run this as a build that writes review-notes.md directly?"

Two options, evenly weighted. But the same doc opens by stating the output contract — findings route to Unprocessed, no direct edits to what the audit reads — and calls an item pointed at a doc-write "a planning slip". So the doc has a preference and the specimen hides it. Lens 3 names this failure mode as a menu where a recommendation was due.

Where it fires: at the start of an audit item, before any reading, with the user present and deciding — which is exactly where the dependency-ownership rule says to lead with the recommendation and offer the alternative as the fallback.

Why it matters: the user is being asked to arbitrate between the contract and a slip, with nothing telling them which is which. The fix is one sentence of reordering, not a new rule: recommend filing to the queue, name the doc-write as the escape.

#### Hand-over step named "the quoted install line" where the post held two quotes [handover-named-neither-of-two-quotes]
Found live 2026-08-27, raised by the user mid-walk-through of [beta-install-smoke-and-post-edit]. Her words: *"there are two quonte looking things in there. are you talking about the how to install post in how to throughliner"* — two questions in one, because the step was ambiguous about which quote AND had not made the thread unmistakable.

The step handed over said to edit "the quoted install line". The pinned "How to install" post contains two indented quote blocks: the install ask under "If you already have Claude Code", and a browser-route prompt under "If you're new to Claude Code". Only the first was meant. The second points at claude.ai and INSTALL.md and would have been wrong to touch.

**The shipped rule that should have caught it already exists** and is stated in the `[user]` walkthrough rules: where a walkthrough involves more than one stored text — a pinned message, a forum post, a register line — it names where each one lives, since a step saying "update the text" is unfollowable once there are two of them. This is that failure exactly, with "the quoted line" standing in for "the text".

**What sharpens it into a finding rather than a one-off slip:** it happened in the same run that built [handover-composition-checkpoint], which widened the pre-send read-back into three questions — the first of which asks whether each step names the thing to click and the thing to look for. The checkpoint was authored and then not run on the very next hand-over composed after it. That is the second recorded instance of this project breaking a hand-over rule within an hour of writing it (the first is on [handover-composition-checkpoint]'s own evidence).

Worth weighing at processing: whether the checkpoint's question 1 needs the two-stored-texts limb stated inside it rather than cross-referenced, since the cross-reference is what did not fire.

#### Law-prose article announcement carries the why behind removing the why-clauses [law-prose-article-announcement-carries-the-why]
Raised by you 2026-08-27, while rejecting the rationale-split draft — the one constructive note in that rejection, filed rather than acted on because you set it aside for now ("that's neither here nor there").

Your point: the draft was worthless because it described where the reasoning went, when the interesting story is **why the why-clauses were removed at all**. That reasoning — a rule with its justification attached is a longer rule, a model follows fewer instructions reliably as they lengthen, and an irrelevant or same-sounding rule degrades the ones around it — is a real finding about how these tools behave, and it is the sort of thing worth reading even if you never touch Throughliner.

Your placement for it: not a standalone post, but part of a larger announcement alongside the **upcoming law-prose article**. That gives it the length it needs and an occasion, which a tip about an internal reorganisation never had.

Bears on the deleted [announcement-rationale-split-correction], whose record (`LOG/2026-08-27-announcement-rationale-split-correction.md`) carries the full critique of what a post on this subject must not do.

Note for processing: this waits on the law-prose article existing, which is not yet a queue item as far as this capture's author could see. If it is not filed, filing it is the blocker this needs.

#### One post a day is per channel, not across the whole server [one-post-a-day-is-per-channel]
Your decision, 2026-08-27, given while directing the plain-English consent tip to go up on a day another Throughliner post had already gone out. Your reasoning, in your own words: *"I think that should be one post a day per channel. That rule is from when i was only using the announcements channel and everything was going in there."*

Filed rather than written. The rule gate reserves admission of a rule into the method's own text for a planning session, so a build run transcribes dispositions and does not author them — this needs a disposition it does not have.

What changes if it is admitted: the pacing rule currently reads as one Throughliner post per day full stop, which is what held this tip back and prompted a warning turn. Per-channel, there was no collision at all — the earlier post that day went to a different channel from the tip. It also stops the new tips channel from competing with announcements for the same daily slot, which the channel restructure of 2026-08-27 ([posting-rule-two-kinds-and-tip-pipeline]) makes a live problem: two kinds of post now exist with their own channels, and one shared daily slot would starve one of them.

The premise to check at processing is your own: that the original rule was written when announcements was the only channel in use. Worth confirming against the record before the amendment rests on it.

Site: the Discord posts section of `CLAUDE.md`, where the one-a-day pacing is stated. Host-only, like the rest of that section.

#### CLAUDE.md asserts which channels the bot may post in, and nobody checked [claude-md-asserted-bot-posting-channels-unchecked]
Found live 2026-08-27, during the walk-through of [discord-post-plain-english-consent], and filed by Claude.

Earlier in that same run, [posting-rule-two-kinds-and-tip-pipeline] wrote into `CLAUDE.md`'s Discord section that the bot may post in tips, announcements and test-rezips-for-nerds. That sentence came from the design discussion. It was untrue of the live server at the moment it was written: the bot could post only to test-rezips-for-nerds, and the first send to tips failed with HTTP 403 "Missing Permissions". The user has since granted both, so the sentence is true now — but it was true by repair, not by having been checked.

**Why reading proved nothing.** The bot could already READ tips and announcements, so every check short of an actual send returned success. Reading a channel and posting to it are separate grants in Discord, and TOOLS.md now records that along with the measured per-channel picture.

**The general shape, which is what makes this worth processing rather than just fixing.** A doc sentence stating what a tool CAN do is a claim about the world, and this project already has a rule for that class — the capability check that must name the tool and confirm it is absent or unauthenticated before work is tagged `[user]`. Nothing runs the same check in the other direction, when a doc asserts a capability exists. The cheap version here would have been one permissions read before writing the sentence, which is exactly what was eventually done to diagnose the 403.

Worth weighing against the project's ban on speculative rules: this is one recorded instance, and the admission gate asks for a failure you can point to. This is that pointer, filed so a second instance has something to join.

#### Screen the twelve tip candidates against the is-this-visible-to-a-user test [tip-candidates-need-visibility-screen]
Filed by /rescan, 2026-08-27, joining two things that happened in the same chat and were never connected.

The features-needing-tips audit filed twelve tip candidates into Unprocessed earlier in this run, each naming a feature with no post coverage. Later in the same run you rejected a drafted post outright, and your reasons were not about its wording — they were that the thing it described is invisible from where the user stands. Your five objections, in your own words: users "do not read throughliner rules"; there are "no current users so no one there to feel the difference"; the FAQ "was always supposed to be" where the user looks so nothing changed for them; and twice, "why would anyone care about this?"

**The two existing tests both pass a post like that.** The posting brief asks how a claim is worded — benefit first, plain words, no decision history. The two-kinds rule added the same day asks whether a post explains one Throughliner feature. Neither asks whether the feature is one the user can see, and the rejected draft satisfied both.

So the twelve candidates were written before that test existed, against criteria that do not contain it. Several plausibly fail it — the ones describing where something is filed, or how the method organises its own text, rather than something that shows up in a session the user is sitting in.

The work: at processing, run each of the twelve against the visibility question before any is drafted, and drop the ones that only describe internal arrangement. Whether the test also belongs in the posting brief as a third criterion is a separate question, and it is a rule change — so it goes through the gate rather than being assumed here.

Bears on [posting-rule-two-kinds-and-tip-pipeline] (shipped) and on the deleted [announcement-rationale-split-correction], whose record `LOG/2026-08-27-announcement-rationale-split-correction.md` carries the full critique.

#### Bot's edit path is unproven, and the item that owned that acceptance has left the queue [bot-edit-path-unproven]
Filed by /rescan, 2026-08-27.

[discord-posting-bot]'s acceptance read: a test post appears in the channel "and is then edited by the script". The post half was met in a real channel during this run — the plain-English consent tip went up in #tips on your explicit yes, read back byte-identical. The **edit** half was not, and the item has since been removed from Processed as built.

**Why it was left unproven rather than exercised.** Editing a published post purely to demonstrate that the code path works changes something real in the server for no reason anyone reading it would want. The same reasoning the method already applies to hook changes — never verify a guard by performing the guarded action for real — points the same way here.

**Why that needs a line rather than a note.** With the item gone, the only record that `edit` is unverified sits inside this run's session records, which nothing routinely re-reads. A capability recorded as working in `TOOLS.md` and never actually run is exactly the shape that gets discovered at the worst moment — the first time a posted claim needs correcting under time pressure.

The work is small: at the first genuine edit — a correction to a post, or the test-rezips entry lifecycle where posting a new entry unlocks editing the previous one — confirm the edit landed by reading the message back, and record that `edit` is now proven. No separate test post is wanted.

#### [user] Grant the bot send permission in the how-to forum before the re-homing runs [bot-needs-howto-send-permission]
Filed by /rescan, 2026-08-27.

[howto-posts-bot-authorship] plans to re-home the how-to forum posts under the bot's authorship, because a bot can only edit messages it authored itself and the how-to posts are currently yours. That item will stop at its first step: the bot **cannot post in the how-to forum**.

Measured this run rather than assumed, by computing effective permissions from the guild roles plus each channel's overwrites (a read, never a test post): the bot can post to test-rezips-for-nerds, general-chat and give-and-get-support, and is blocked from the how-to forum. You granted tips and announcements during this session, which fixed those two and left this one.

**The trap worth naming, because it is why nobody spotted this earlier:** reading a channel and posting to it are separate grants. The bot can already read the how-to forum — it read the install post back from there twice during this run — so every check short of an actual send comes back clean. Recorded in `TOOLS.md`.

Written into both entries by slug, so opening either one surfaces the other.

**Walkthrough.**
1. In Discord, right-click the **❓how-to-throughliner** channel, choose **Edit Channel**, then **Permissions**. Look for: the permissions list for that channel specifically, not the server-wide settings.
2. Add the bot (or the role it holds) and turn **Send Messages** on. Forum channels also need **Create Posts** to start a new topic — turn that on too if the re-homing will create posts rather than only reply. Look for: the bot listed with both enabled.
3. Tell this project. It will re-run the permissions read and confirm from the API rather than taking the report on trust, exactly as it did for tips.

#### Cycles parser reads only the first line of Cadence and Observable, and nothing says so [cycles-fields-are-single-line]
Filed by /rescan, 2026-08-27, from writing this project's own `CYCLES.md` earlier in the same run.

`session_start.py`'s `cycles_facts()` matches `Cadence:` and `Observable:` with a single-line regex, so a field wrapped across two lines is silently truncated at the line break. The first draft of the weekly-release definition wrapped both, and the session-opening line would have reported the cadence as "weekly, Wednesday — declared by the user (decision of 2026-08-22)," — cut mid-sentence, with the trailing comma. Caught only because the parser was run directly against the new file before moving on; reading the doc would not have shown it.

**Nothing a cycle author reads mentions this.** plan.md's cycle-authoring rule names the four things a definition must carry and says nothing about their shape. `CYCLES.md` files carry no format note. So the next author — in this project or a consumer's — writes a naturally wrapped line and gets a truncated fact in every session opening, with no error anywhere.

Two candidate fixes, not chosen here:
- state the constraint where definitions are authored, so the author keeps both fields on one line;
- or make the parser continue across wrapped lines, which removes the constraint instead of documenting it, and is the better fix if it is cheap.

The second is a hook change and would trigger the test suites at its close. Which one to take is a decision for processing.

Worth noting the failure mode is silent and cosmetic-looking: a truncated cadence still reads like a cadence, so nobody downstream can tell it was cut.

#### Two live rules still name retired mechanisms [live-rules-name-retired-terms]
Filed at the 2026-08-27 build close, under the slug `resources/rule_signals.py` prints. The check found it during the close's required run; nothing had filed it, and the slug was not open in either section.

Two live references, both in hook code rather than in prose:

- `plugin/throughliner/hooks/pre_tool_use.py:866` names `keep-step`
- `plugin/throughliner/hooks/session_start.py:54` names `--- Build block ---`

Both mechanisms are on `resources/retired-terms.md`. A live rule naming a mechanism that no longer exists either instructs a session to look for something absent, or — worse in hook code — keys behaviour on a marker nothing writes any more, which fails silently rather than erroring.

Worth checking at processing whether each is genuinely live or is a comment describing history. The check matches the term wherever it appears in a file it treats as carrying rules, and cannot tell an operative line from a comment. That distinction decides whether this is a code fix or a comment reword.

**A close-time correction, recorded because it nearly went unfiled.** The check's output was read earlier in this same session as saying the slug was already open and therefore satisfied. It was not open. The check prints its slugs under a heading saying a capture should be filed under each; the misreading turned a finding into a no-op. Nothing mechanical would have caught that — the check goes quiet once an item carries its slug, so a session that wrongly believes one exists gets the same silence as a session that filed one.

Since a hook file changes here, the build that fixes it runs the suites under `resources/testing/` before committing.

#### SPEC owes a sentence: the method recommends the rescan wherever it names the close as next [spec-owes-rescan-recommendation]
Filed at the 2026-08-27 build close by the build itself, which records the sentence it thinks SPEC owes and does not write it. A build never writes product truth — the session that made a choice is not the session that certifies it — so SPEC lags this one sentence, visibly, until the next planning run writes it.

[rescan-before-done] shipped this run and changed what the method **says to the user**: the end-of-queue gate in a planning session and /next's close hand-off both now recommend running the rescan first, to catch anything decided but never written down, before closing. That is user-facing behaviour, not internal arrangement — it appears in the chat, at the moment the user is deciding whether to stop.

SPEC's `/rescan` paragraph currently describes the command as user-invoked and never positional, and describes the close's shrunken scan. It does not say the method now offers the rescan at the points where closing comes up. A reader of SPEC would conclude the user has to think of it themselves, which was true before this run and is not true now.

The sentence SPEC owes, as the build would put it — to be re-authored by whoever writes it rather than pasted:

> Where the method names the close as the next step, it recommends running /rescan first, so anything decided but never written down is caught before the session ends.

The second half of that item — the close's scan standing down when a rescan just ran, with a required line saying so — needs no SPEC sentence: SPEC already says a chat that invokes /rescan pays a line at the close, which is exactly that outcome.

#### Rezip's tip-candidate step writes to a file the scope-lock refuses at rezip time [tip-pooling-step-blocked-by-scope-lock]
Found live 2026-08-27, at the first rezip after the step was built in the same run. Filed by Claude.

[posting-rule-two-kinds-and-tip-pipeline] added a step to the rezip ritual: notice tip candidates as features land in the installed build, and pool them in `ANNOUNCEMENT-IDEAS.md`. The step cannot run.

**Why.** A rezip happens after a close, when the build working file has been deleted, so the scope-lock treats the session as a planning session. Its standing writable list is QUEUE.md, SPEC.md, CYCLES.md, TOOLS.md, `LOG/`, research notes and scratch files. `ANNOUNCEMENT-IDEAS.md` is on none of them, and the write was refused outright — correctly, by the rule as it stands.

**The design fault is the siting, not the lock.** The pooling step was written into the ritual without checking what the session running that ritual is permitted to write. The rezip is the one moment the step is meant to fire, and it is exactly the moment the file is unwritable.

Three candidate fixes, none chosen here:
- add `ANNOUNCEMENT-IDEAS.md` to the planning session's standing list, which is the smallest change but widens a list deliberately kept narrow;
- move the pool into a file already on the list — the queue itself, as captures, which is where cleared candidates end up anyway;
- move the pooling to a moment that has a build working file, though the rezip is where the information is freshest, which is why it was sited there.

**Worth weighing at processing: whether pooling is needed at all**, given the audit that just filed twelve tip candidates straight into Unprocessed with no pool involved. That path was not blocked by anything.

**What this session did instead**, so the work is not lost: the two candidates it would have pooled are recorded in the rezip's own account in this session's tail — the rescan-before-close recommendation, and /rescan's process-now arm no longer writing a throwaway capture. Both were screened against the user's visibility test and the other three of the build's rule changes were deliberately not pooled, being internal.

#### Process the release-chain findings in resources/research/release-validation-chain-broken.md [release-validation-chain-findings]
Filed at the third 2026-08-27 session's planning close. The file was written as the build session's post-close tail — a defect report addressed to the next planning session — and that session (this one) never saw it, because a tail file is invisible until the close stages it. This line is what puts it in front of a planning run.

Four findings, per its own index line: validation always runs on a build the tree has already moved past, so the ritual packages the least-tested state; the test-rezips entry lifecycle attaches a zip with the same flaw; `content_stamp()` hashes raw bytes under `core.autocrlf=true` with no `.gitattributes`, so a commit can never be compared to an installed build; and the weekly cycle's stable-label selector has no label-to-commit mechanism behind it. Fix directions are listed in the file, none chosen.

Live evidence from this session: this close had to re-derive by hand that test2 = d31b553 before the off-cycle release of the tested build could be planned — the exact lookup the broken chain fails to provide.

#### Beta-channel item's file list names QUEUE.md, which a build run cannot write [beta-tester-pathway-files-line-names-queue]
Filed at the third 2026-08-27 session's planning close; the queue lint flagged it when [beta-tester-pathway] was lifted, and the user approved capturing it. The item's Files line includes "QUEUE.md (the announcement item's walkthrough)" — its build is meant to draft the Discord beta-offer text into [beta-launch-announcement]'s walkthrough, which lives in the queue. A run cannot reach the queue: queue content is planning work, and the scope-lock refused exactly this shape once already ([queue-walkthroughs-say-claude-cannot-post]).

The collision was named at the close: [beta-tester-pathway] is cleared and runs before the next planning session unless amended first. The likely fix is small — the announcement draft is authored at a planning session instead, or the build writes it somewhere a run may write and a planning session carries it across — but choosing is processing, not filing.

#### "Contest by number or say go" close ask never says what go does [contest-by-number-ask-unexplained]
Captured by you, 2026-08-27, at this close's own candidate-set ask: the phrasing is confusing because it does not explain what happens on "go". A reader is asked to choose between two words with only one of them defined — contesting is explained by the numbering, while "go" silently means "write all of these as captures". The fix is wording at the ask's site(s): the candidate-set specimen should state the effect in the sentence, e.g. "say go to file them all, or contest by number." Sites to grep at processing: the wind-down re-scan in done.md, and the /rescan candidate-set ask if it shares the phrasing.

