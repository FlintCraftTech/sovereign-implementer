# QUEUE

Two sections. **Processed** — agreed work, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** — captured, not yet processed; the next /plan weighs each item. Every entry in either section is a `#### ` heading (its description) with a `[slug]` at the end of that line and its rationale beneath; an entry in Unprocessed is a **capture**, and it becomes a **work item** when /plan keeps it into Processed. A leading `[audit]` / `[user]` tag names how it's executed; no tag means a build. An item carrying a security or privacy risk gets a `Red flag · State: …` marker — the flag rides the work.

**Authoring a rule for the method's own text? The rule gate is in `CLAUDE.md`, always loaded — run it before you write.**

## Processed

#### `workshop/` becomes a method folder, with `resources/` inside it [workshop-becomes-a-method-folder]
**Your design, 2026-08-29**, reached while settling what a visitor to the repository sees first. Working material that is not the product lives in one folder every project gets, and `resources/` — research findings and re-read-later testing evidence — sits inside it as `workshop/resources/`.

**Your reason, in your own framing:** only what is part of Throughliner stays in view, so someone shopping online for a method sees the method rather than the workshop. The method's own documents stay visible because they demonstrate it; everything they merely refer to does not.

**Claude's objection was wrong and is recorded so it is not re-raised:** that `resources/` is a shipped concept and therefore not renameable here. This is the project that authors the method, and /setup's migration is what carries other projects across.

**Rule gate: run — admitted as an amendment, costing no slot.** It renames and re-homes the subject of an existing rule rather than adding one. Parent: the two-kinds rule for `resources/` in `docs/skill-nonspecific-rules.md`.

**Files, derived from a grep for `resources/` rather than from the discussion.**
- `plugin/throughliner/docs/skill-nonspecific-rules.md` — the two-kinds rule, the three-way triage and the temp-files block reworded to `workshop/resources/`.
- `plugin/throughliner/docs/plan.md` — the planning scope-lock's writable list.
- `plugin/throughliner/docs/setup.md` — scaffolding creates `workshop/`.
- `plugin/throughliner/docs/migrate-checklist.md` — gains the step that creates `workshop/` and moves an existing `resources/` inside it. This is the step that does the work in every project, including this one.
- `plugin/throughliner/docs/next.md`, `done-build.md`, `rescan.md`, `feedback-and-inbox.md` — each names a `resources/` path.
- `plugin/throughliner/hooks/pre_tool_use.py` — the planning session's writable path.
- `plugin/throughliner/hooks/session_start.py` — `FORMAT_EPOCH` bumped, with a line in the epoch history saying what the new number means.
- `plugin/throughliner/hooks/post_tool_use.py`, `stop.py`, `scripts/queue_digest.py`, `scripts/measure_written_shape_length.py` — changed only where the grep shows a path named.
- `README.md` — the feature list, per the README-sync trigger.

**Reads but does not change:** this project's own files under `resources/`. They move when /setup runs, at [workshop-migration-setup-run], not here.

Observable: a grep for `resources/` across `plugin/throughliner/` returns only paths written as `workshop/resources/`, and the hook suites pass.
**The observation reaches `resources/testing/`**, named among the files above because the suites are what the close must run before committing a hook change.

**Refused: renaming `resources/` to `workshop/` outright.** That leaves one folder holding three kinds of thing, which is the defect that made the name feel wrong to begin with. The two-kinds rule survives, one level down.

**Refused: nesting the other way as `resources/workshop/`.** Same objection, and it puts a host-shaped folder inside a method-shaped one.

**The epoch bump halts every existing project at its next session until /setup migrates it.** That is the mechanism working rather than a cost to avoid, and it is how the user's other projects get carried across.

**No `Runs alone` marker, checked rather than assumed:** this item edits files inside the package and moves no path, so nothing another item names goes stale while it builds. The folder move happens at [workshop-migration-setup-run], and the marker rides [repo-cleanup-product-forward], which is the build that moves paths.

#### Audit findings always route to the queue, and the actionable filter comes out [audit-findings-always-queue]
**Your ruling, 2026-08-29**, after the live instance the same day: Claude read the always-loaded triage's middle arm ("a finding -> the observing chat's LOG entry") over the audit procedure's "findings route to Unprocessed", and recommended routing the repository inventory out of the queue. Your words: findings of audits always belong in the queue — it's WORK (planned writing) that doesn't.

**Two rewordings, one item.**
- `plugin/throughliner/docs/skill-nonspecific-rules.md` — the three-way triage's middle arm gains the exclusion: it never covers an `[audit]` run's output, which goes to Unprocessed whatever it proposes. The reason, carried as operative text because the rule cannot be applied correctly without it: findings are filed for the user to weigh, and nobody processes a session record, so a finding parked there is one the user never meets.
- `plugin/throughliner/docs/next-audit.md` — the compile step's "one finding per actionable change" becomes one finding per discrete observation. **Your ruling on the second half, distinct from the first:** Claude does not decide whether a finding is actionable — it already exercises enough discretion on what counts as a finding within the audit's parameters. Worth-doing is settled at /plan, with the user present. A filter running in a `[SILENT]` step before the work reaches the user can only drop things, never surface them.

**Kept, on Claude's recommendation and your non-objection:** next-audit.md's `dropped` route for a finding Claude re-reads and finds factually wrong before filing — a correctness check, already fenced by that doc's own text from being a worth-it judgment or a user-rejection route.

Rule gate: run — admitted as an amendment, costing no slot. Two existing statements reworded; parents are the three-way triage and the compile step's own sentence, and the old wordings are what the new ones evict.

Observable: a grep for "actionable" in next-audit.md's compile step returns nothing, and the triage's middle arm names the audit exclusion.
**Files:** `plugin/throughliner/docs/skill-nonspecific-rules.md`, `plugin/throughliner/docs/next-audit.md`.
No SPEC sentence is owed, checked rather than assumed: SPEC describes audits as reporting findings for later review and never names where they land.

#### Reusable priming prompt for demo recording sessions [recording-priming-prompt]
**Your idea, raised in the site project's planning session and mailed here 2026-08-28** as the side that owns it; processed 2026-08-29. A prompt pasted at the start of any session being recorded: this is a demo, keep revealing information off the screen. Your reason, carried from the mail: a recording exposes more than the method being shown — the structure of the work, what is being tracked — and preventing it at the source is far cheaper than blurring it in the edit afterwards.

**Both videos went scripted at processing, which shrinks this prompt's job without removing it:** the risks live in the margins a script does not cover — a session opening listing other projects' names, a file path carrying the username, an INBOX line naming a correspondent, an autocomplete showing real folders. Those appear uninvited, which is what a standing prompt is for.

**The build:** write `YouTube/recording-priming-prompt.txt`, a paste-ready prompt instructing the recorded session to: never open or quote anything outside the demo project itself; never echo absolute paths, which carry the username; never touch `INBOX/`, the address book or the sent register on camera; use invented names and data only; and where a step would surface something real, say so and stop rather than showing it.

Observable: the file exists and a read shows each named exposure covered. Its folder is gitignored, so the user can tune the wording by hand at any time after it exists.

**Files:** `YouTube/recording-priming-prompt.txt` (created).

Reusable by construction — every case-study recording wants it. The scripted-video sessions ([legal-demo-video-guide], [determinism-lesson-video]) are its first consumers.

#### Every zip this project ships stores Windows path separators, which the zip format does not allow [zip-entries-use-backslash-separators]
Found live 2026-08-29 during the 1.21.1-test2 rezip, and confirmed against the committed release zip. Filed by Claude.

**What was observed.** Entries in the archive zip read `throughliner\skills\`, `throughliner\.claude-plugin\plugin.json`. The committed `plugin/throughliner.zip` — the artifact attached to every GitHub Release so far — has the identical shape.

**Why it is a defect rather than a cosmetic detail.** The zip format specifies forward slashes as the path separator. Windows tools tolerate backslashes, which is why nobody here has ever seen a problem: the rezips are built, installed and tested on one Windows machine. A macOS or Linux tester unzipping the release plausibly gets flat files literally named `throughliner\skills\next.md` rather than a folder tree — and the install route in the pinned how-to post tells them to unzip it and add the extracted folder as a local marketplace.

**The cause is `Compress-Archive` on Windows PowerShell 5.1**, which is what the ritual specifies.

**Unverified, and it decides how urgent this is:** whether any tester has actually installed from the zip on a non-Windows machine. Nobody here can answer that by reading; it is a question for the testers, or for someone with a Mac to hand. **Do not treat the defect as proven harmful until that is known** — what is proven is that the bytes are non-conformant, not that anyone has been broken by them.

**The fix, chosen at processing 2026-08-29 on Claude's recommendation and the user's agreement: rebuild the ritual's zip step in Python's `zipfile`.** Python writes conformant forward-slash paths, is already what everything else in this project runs on, and removes a PowerShell dependency from the ritual. Post-processing the entries was the alternative and lost as the more fragile half-measure.

**Merged in at that processing: [pycache-sweep-runs-before-the-suites], deleted with its facts carried here.** Found in the same rezip: the ritual's bytecode sweep (step 2) runs before the test suites (step 3), which import the hooks and regenerate exactly the `__pycache__` folders the sweep deleted, so the zip (step 7) catches them — observed live, five bytecode entries in the first archive zip of the day. The Python zip step closes this permanently by excluding `__pycache__` at zip time, ending the sweep-ordering fragility instead of re-ordering around it. That item's open check was run and found unanswerable, recorded so it is not re-run: the installed cache does hold bytecode folders, but the hooks run from that cache and regenerate them at runtime, so the check cannot tell what the snapshot carried — the provable harm is confined to the zips.

**Files:** `resources/release-ritual.md` — the zip step rewritten to a `py` one-liner (or small script) using `zipfile`, excluding `__pycache__`; the step-2 sweep may then be simplified or noted as belt-and-braces, the build's call. The release ritual's repackage step reads the archived zip, so fixing the rezip fixes both.
Observable: a zip built by following the ritual end to end, its entries listed rather than trusted — every path uses forward slashes and no entry names `__pycache__`.

**Ordering, in prose:** [host-rituals-migration] (held) will later move this ritual's steps into `CYCLES.md` definitions — whichever builds second reads the other's change rather than assuming the file's shape.

#### [user] Re-home the how-to forum posts under the bot's authorship [howto-posts-bot-authorship]
Filed 2026-08-27 with [posting-rule-two-kinds-and-tip-pipeline], from your instruction that the how-to topics be editable and maintainable by the bot. The constraint that makes this an item at all (recorded in `TOOLS.md`): a bot can only edit messages it authored itself, and the existing how-to posts are yours — so bot maintainability requires each one re-posted by the bot once, after which every later tweak is a bot edit under the approval rule.

**Walkthrough. Rewritten 2026-08-29** to open with the test that settles its own unverified assumption — see [walkthrough-asserts-unchecked-surface], which found this halting at old step 3 on two facts about Discord nobody had checked.
1. **Settle two things with one throwaway topic.** The bot creates its own topic in the how-to forum, posts a second message into it, then deletes its own opening message; nothing of yours is at risk. Claude shows you the exact text before anything is posted and needs your explicit yes. Look for **(a)** after the delete, either the topic is gone from the forum list, or it survives with its subtitle reading that the original message was deleted — a search on 2026-08-28 found Discord support threads pointing both ways, so this is not answerable by reading; and **(b)** where the topic sits in the list after each post, which settles whether posting into a topic re-orders the forum.

   **(b) is on the list because of what you saw on 2026-08-29:** the topics display out of numeric order — 3, 6, 5, 4, 2 — all showing recent activity. The likely cause is that the forum sorts by latest activity rather than creation, so your edit notes have been shuffling them. **That is a guess about someone else's surface and must not be built on** — which is the rule this very item produced. The test above settles it, and re-homing will post into every topic, so the answer is needed *before* the sweep rather than discovered during it. **Lower stakes than it looks:** the sequence numbers live in the topic titles, so a reader can follow the order even when the list is shuffled.
2. **Decide what happens to your other messages in each topic.** Reading the live forum on 2026-08-28 found six topics each holding between two and five further messages of yours, plus an attachment. **What they are was settled 2026-08-29 from your own view of the forum: they are your edit notes**, which makes this easier than it looked — the default is to delete them with the original rather than repost them, since an edit note about a post the bot now owns has nothing left to annotate. Confirm that per topic or as one rule.
3. Claude fetches each how-to post's current text through the bot and shows it to you unchanged. Look for: the text matching what the forum shows.
4. On your yes per post, the bot posts the replacement in the same topic. Look for: the new post appearing under the bot's name.
5. You delete your original post of each (only you can — the bot cannot delete or edit your messages in a forum topic it doesn't manage, and your authorship is the thing being replaced). Look for: the topic showing only the bot's copy.
6. The register line for each how-to post is updated to point at the bot's copy, with the channel named; this item closes when every how-to topic's live text is bot-authored.
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

#### [user] Post the beta-channel launch announcement on the Throughliner Discord [beta-launch-announcement]
Filed 2026-08-22 with the keep of [beta-tester-pathway], which drafts the announcement text into this walkthrough as part of its build. The offer is framed honestly early — a testing invitation, not a product launch (the one-a-day pacing was repealed 2026-08-28). Launches alongside the community listing per your sequencing recorded on [beta-tester-pathway] and [marketplace-submission].
**Walkthrough.**
1. Once [beta-tester-pathway] builds, the announcement template lives with the release-cycle materials (your direction 2026-08-28: a cycle template, not a one-off draft in this item); Claude fills it in, shows the exact text, and walks you through any final edits.
2. Before posting, the tester install walkthrough must have been smoke-tested on a second machine — confirm that happened; do not post an install route nobody has run.
3. The bot posts it to Discord on your explicit yes to the exact text (route corrected 2026-08-28 — the posting bot exists; pacing repealed the same day).
4. You confirm; the send is recorded in `INBOX/sent.md` with what it claimed, and this line closes.
**Lifted 2026-08-28.** [beta-tester-pathway] shipped in the 2026-08-28 run and its tick is confirmed (`LOG/2026-08-28-beta-tester-pathway.md`): the announcement now exists as `resources/beta-offer-announcement-template.md`, the `beta` branch exists, and the record notes the tester install smoke test ran 2026-08-27 — which is step 2's condition, so that step is a confirmation rather than a wait.
**Files:** none — the artifact is a Discord post.

#### [user] Re-home the announcements back catalogue under the bot, correcting claims as it goes [announcement-back-catalogue-rehomed]
**Your decision, 2026-08-29**, given while processing [tip-recycle-sweep-coverage-note]: you are happy for your own posts to be deleted and replaced with Throughliner-project posts, so they stay editable as further falsifications occur. The back catalogue is short, so it is done once, and after that as corrections arise.

**Why it is worth doing as a sweep rather than post by post.** A post cannot be re-posted without every claim in it being true of the shipped plugin at that moment — that is the existing posting rule. So re-homing all of them **is** a full verification pass over everything the channel has ever claimed, obtained as a side effect rather than as separate work.

**The occasion that forced it.** `#announcements` message id `1540531465115410553` (2026-08-22, "builds no longer read your queue — and an honest comparison") is public and both its claims are false: the generated build view was retired 2026-08-27, and the article it announces was superseded 2026-08-23. `INBOX/sent.md` recorded that post as "approved, not yet posted", which is why no repeal-grep ever fired on it. That register line is corrected; this item makes the public correction.

**Verified, not assumed:** the bot can post to `#announcements` — the v1.21.1 announcement there is already under its name. It cannot delete or edit the user's messages, which is why each step needs her.

**Every repost carries a dateline naming when it was originally posted.** Without it, twenty-odd reposts read as twenty-odd fresh announcements, which is the cost that made a back-catalogue sweep look wrong in the first place. The dateline is what turns it into a visible archive rebuild.

**Walkthrough.**
1. Claude lists the channel through the bot and shows you every post with its id and date, oldest first. Look for: the count matching what you see in Discord.
2. Working **oldest first**, so the rebuilt channel keeps its original order: Claude reads a post's text, checks each claim against the installed plugin, and shows you the text with any claim that no longer holds marked, plus the dateline it will carry. Look for: the marked claims, and whether you agree they are wrong.
3. On your yes to the exact text, the bot posts it to 📣announcements. Look for: the new post appearing under "Throughliner Project".
4. You delete your original: hover it, open the ⋯ menu, choose **Delete Message**. Only you can — the bot cannot delete your messages. Look for: only the bot's copy remaining in that position.
5. That post's line in `INBOX/sent.md` is updated in the same turn — the bot's message id, the changed author, and what it claims read off the text as posted rather than from what was decided.
6. Repeat to the newest post. This closes when every message in the channel is bot-authored.

Observable: every message in `#announcements` is authored by the bot, and every announcements line in `INBOX/sent.md` carries a bot message id.
**Files:** `INBOX/sent.md` only — the artifacts are Discord posts.

#### [user] "How ports work" forum, with four informational posts [ports-forum]
**Your direction, 2026-08-29**, with the forum name and all four subjects yours. Two people are porting Throughliner to other harnesses, one of them making several, and there is nowhere that tells anyone how.

**The four posts, as you named them.**
1. Starting your own port **from outside Throughliner**, with example prompts.
2. Starting your own port **from inside Throughliner**, with example prompts — this is where [setup-self-hosting-seed] gets its first audience: setup already seeds the rule gate, the disposition pattern, the host-versus-target framing and the template files for anyone building a method or port of their own, and nobody porting knows it exists.
3. **Pulling changes into your own port**, and where the relevant ones are found — describing what [port-facing-changelog] produces, including the part a porter most needs: that host-only changes are marked and must not be ported.
4. **Communicating your port flavour**, so it is legible — using the two names from [port-flavours-named].

**Walkthrough.**
1. You create the forum in the Throughliner Discord and tell Claude its name. Only you can — the bot cannot create channels. Look for: the forum appearing in the channel list.
2. Claude drafts each post in turn, verifying every claim against the installed plugin at drafting rather than from the design discussion, and shows you the text. Look for: claims about what setup seeds and what the changelog contains matching what the shipped build actually does.
3. On your yes to the exact text, the bot posts it. **Bot-authored from the start** — the how-to forum is being re-homed under the bot for exactly this reason ([howto-posts-bot-authorship]), so a new forum should not repeat the mistake.
4. Each post gets its line in `INBOX/sent.md` in the same turn, naming the forum, what it claimed, and a pointer to the text.
5. Closes when all four are posted and registered.

Observable: four bot-authored posts in the forum, and four lines in `INBOX/sent.md` naming it.
**Files:** `INBOX/sent.md` only — the artifacts are Discord posts.

**Maintenance is not part of this item, on your instruction:** the forum's ordering and the factualness of its content are maintained on a cycle, the same way the how-to forum's claims are. [announced-claims-sweep] was widened to cover both rather than a fourth cycle being created.

**Ordering:** last of the four port items. Posts 3 and 4 describe artifacts that [port-facing-changelog] and [port-flavours-named] create, so drafting them first would mean writing about things that do not exist. Carried by placement and this sentence rather than by a `Blocked by:` line, which would push it below the readiness line and out of the priority position you set.

#### [user] Legal case run in Throughliner, scripted as a hypothetical — a YouTube video [legal-demo-video-guide]
**Your idea, 2026-08-28; reshaped 2026-08-29 on your decision.** A video about running a family-law matter in Throughliner. Your virality read, unchanged: a legal case is a very weird project type to run inside Claude Code, which is exactly why it travels.

**The unscripted demo is refused, in your words: "This is too hard."** That version had you setting up a legal-case-shaped project on camera, asking questions as though you did not know what Claude would suggest, while steering toward a structure you had already proved. It needed a steering guide written from your real case files so the naive-sounding questions would reliably arrive somewhere good. The guide, the destination structure and the naive-question device all go with it.

**What replaces it: a script.** You describe your project's structure in detail with all identifiers removed, and the video presents it as a hypothetical case rather than one you ran. The structure is the real one that worked, which is what makes it worth watching; nothing ties it to a person or a matter.

**Nothing sensitive is opened from this session.** The abstraction happens before the description reaches Claude, so no file of your legal project is read from here — the path and matter names stay unrecorded, per the scrub rule on identifying paths. A script is also reviewable cold before recording, which the unscripted version could never be.

Output lands in `YouTube/`, gitignored (confirmed 2026-08-29 at `.gitignore` line 9, so the earlier hold on [youtube-folder-gitignored] is spent). [recording-priming-prompt] still applies, now for screen contents during recording rather than for what is said. [project-types-listicle-video] was raised as this item's replacement and kept as separate work instead. The slug is kept through the rename per the stable-slug rule, and no longer describes a demo.

**This item stops at an approved script; recording and publishing are filed separately once it exists.** Two reasons, recorded so the cut is not re-argued: the script is the half Claude contributes to and the half carrying the identifier-stripping work, and a walkthrough that runs on past the thing it was proving has no point anyone can check it against. It also lets the item finish in one sitting rather than waiting on a camera.

**Walkthrough.**
1. You describe your legal project's structure in detail, identifiers already removed — what the source-of-truth document held, how the matter was broken into work, what the queue looked like. Claude asks follow-ups where the picture has gaps. Look for: a description you would be comfortable reading aloud on camera.
2. Claude drafts the script into `YouTube/legal-case-script.txt`. You open that file in the desktop side panel, edit it directly, and save; say when you are done, and Claude reads it back and asks whether there is anything else, repeating until you say you are finished. Look for: your own edits present in the text Claude quotes back.
3. You read the finished script once cold, hunting for anything that narrows it toward a real matter — a date, a sequence of events, an unusual detail. Look for: nothing that would identify the case to someone who already knew it.
4. Tell this project it is signed off; the recording and publishing item is filed then.

Observable: `YouTube/legal-case-script.txt` exists and you have said it is finished.
**Files:** `YouTube/legal-case-script.txt` — gitignored working space, so this item publishes nothing.

#### [user] Determinism lesson video — script drafted together, from the four-quadrant example bank [determinism-lesson-video]
**Your idea, 2026-08-28; the arc, the heuristic and the quadrant requirement are yours. Processed 2026-08-29.** A lesson video: show Throughliner finding tools — doing things that never needed AI — then name what those tasks share: deterministic output. Your heuristic is the teachable core: *a good way to recognise when an output is deterministic is when you can imagine a tool that might accomplish it.* What the video is for, in your framing: helping people identify how to ask and what to ask for — more tools, or more AI — because the big waste is spending AI on work that does not need it.

**Your addition at processing, which reshaped the item:** the video must dispel the equation most viewers hold — probabilistic = AI, deterministic = not AI — by showing the two off-diagonal cases: outputs that are probabilistic without AI, and deterministic work done with AI. Every example is classified as good or bad practice, which is what turns the taxonomy into advice. Your example: OCR — magic that reads an image without a chatbot; show a good use, then a bad one where AI does the same job dearer.

**The example bank exists** — `resources/research/determinism-lesson-examples.md`, compiled at processing on your direction, covering all four quadrants with the good/bad call proposed on each and two claims flagged for re-verify at drafting. The bridge example in it is the lesson's strongest good-practice move: AI builds the deterministic tool once, then the tool runs free forever.

**The knowledge hole is named and the walkthrough is built around it — your own words at processing: the hole in this is my knowledge.** So drafting starts with you working the examples, not with a script.

**This item stops at an approved script, like [legal-demo-video-guide]** — recording and publishing file separately when it exists, and publishing waits behind the marketplace listing per your 2026-08-22 sequencing on [marketplace-submission].

**Walkthrough.**
1. Claude presents the example bank quadrant by quadrant, with its proposed good-or-bad call on each; you agree, overrule or add, until the distinction sits solidly with you — you cannot present a heuristic you are unsure of. Look for: your own verdict written against every example.
2. Claude re-verifies the two flagged claims (Tesseract free/local/deterministic; LanguageTool's core rule-based) and drafts the script into `YouTube/determinism-lesson-script.txt`: your arc, the surviving examples, the heuristic, the bridge as the closing advice.
3. You open that file in the desktop side panel, edit it directly, save, and say when you are done; Claude reads it back and asks whether there is anything else, repeating until you say you are finished.
4. Tell this project it is signed off; the recording item is filed then.

Observable: `YouTube/determinism-lesson-script.txt` exists and you have said it is finished.
**Files:** `YouTube/determinism-lesson-script.txt` — gitignored working space, publishes nothing.

**Ordering, in prose rather than a blocker:** the legal-case script ([legal-demo-video-guide]) goes first — the two design together in the YouTube folder's sessions, and [recording-priming-prompt] rides whichever records first, so one settled script shapes the second. (The intro-video capture once named here was deleted 2026-08-29 — you are exploring that concept outside the queue.)

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

#### Channel depth and recycling: pruned posts come back to be corrected [channel-depth-and-recycling]
**Your design, 2026-08-29.** A channel is only so many posts deep; old posts are pruned; and a pruned post **returns here as a capture** for correction and reposting. Your reason, and it answers a hole you spotted in the same breath: correcting posts only "as they arise" never reaches the ones nothing happens to, so they rot unchecked. Pruning is what makes every post eventually arise.

**Two dials per channel, not one — Claude's addition on your per-channel point, agreed.** Depth alone gives the wrong answer in two of three channels:

```
tips           depth 50, RETURN    evergreen how-tos; a five-month-old tip is
                                   still useful and comes back corrected
announcements  RETIRE, no return   dated news; an old release note reposted
                                   reads as a new release
test-rezips    depth 15, RETIRE    build-specific entries; returning one would
                                   repost a dead build. Already prunes to 15
```

**The depth is derived, not picked: depth × cadence = how long before a post comes back to be re-checked.** Tips at 50 with the three-day cadence is a re-check roughly every five months. **The figure of 50 is yours**; what makes it admissible is that it is stated as a re-check interval rather than a bare number, and it moves by itself if the cadence changes.

**Changes.** `resources/discord_post.py` — the existing `prune` subcommand reads its depth and its return-or-retire flag per channel instead of taking a fixed count, and where a channel returns, each pruned post is written back into QUEUE.md's Unprocessed as a capture carrying its original text, its original date and its message id. `CYCLES.md` — the per-channel settings live with the [tips-posting] definition, since the depth is derived from that cadence and belongs beside it.
Observable: pruning a return-flagged channel leaves a capture per pruned post carrying its text and original date; pruning a retire-flagged channel leaves none; a channel with no settings is not pruned at all.

**Blocked, and the dependency is mechanical rather than conceptual:** the bot can only delete its own messages, so pruning does nothing at all until the channel is bot-authored.

**A returning post is material, not an instruction to repost.** It arrives as a capture and is weighed like any other work — its claims may have been overtaken entirely, in which case the right outcome is deletion rather than a corrected repost.
Blocked by: [announcement-back-catalogue-rehomed]

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

#### [user] Approved Discord post about the comparison article now describes a superseded draft [comparison-article-post-needs-rewrite]
Found by Claude 2026-08-23 while walking the comparison-article item. A Discord post was drafted and approved on 2026-08-22 and has not gone out — it is recorded on `INBOX/sent.md` as approved and not yet posted, with its text verbatim in `LOG/2026-08-22-competition-comparison-article.md`. Its second paragraph announces the article and describes it as closing "on the coherence-over-scale trade", which was true of the 2026-08-22 draft.

That draft is superseded. The 2026-08-23 rewrite names a specific project rather than a category, adds a section on Papi as the nearest comparable tool, and ends on a shipped mechanism instead of a general trade-off — roughly 1,400 words against 900. A hold-note has already gone to the site project asking that the old one not be published.

**So the post cannot go out as approved.** Its first paragraph, about builds reading a generated view rather than the queue, was still true when this was filed and is falsified as of 2026-08-27: [builds-read-the-queue-again] retires the view, so both paragraphs now need rewriting at step 2 — the first against the shipped read-the-queue model, the second against the final article. **That sentence was wrong and is corrected 2026-08-29.** It read that the claim was approved but never posted, on the strength of `INBOX/sent.md`. Reading `#announcements` through the bot at processing found the post live — message id `1540531465115410553`, under the user's own account, in its 2026-08-22 position. The register's status line was false from the day it was written, which is why the repeal-grep never fired on a claim that had been public and wrong for a week. **A public correction is owed**, and it is being made by re-homing the post under the bot's authorship with corrected text — see [announcement-back-catalogue-rehomed], which does that for the whole channel. The rewrite runs after the article settles — it is currently out for review with the maker of one of the tools it names, and that review may change what the article ends on.

**Walkthrough.** 1. The article settles (external review back, revised text final). 2. Claude rewrites the post's second paragraph against the final article and shows the whole post. 3. You say what to change. 4. The bot posts it, with the live article URL folded in, on your explicit yes to the exact text (route corrected 2026-08-28). 5. The bot reads the message back, `INBOX/sent.md` is updated from approved-not-posted to posted, and this line closes.

**This is the repeal-falsifies-an-announcement case caught before it fired**, rather than after: the claim was recorded on the sent register, and the register is what made the collision findable when the article changed. It is also why the register records what a post claimed rather than merely that one exists.

**Kept 2026-08-24, held below the line on Claude's recommendation and your agreement.** As a capture this carried its ordering in prose because captures have no `Blocked by:`; as a held work item it carries the field, so it lifts by itself when the article item closes instead of being re-offered every session while the external review is out. The same ordering sentence is written on the article item per the known-ordering rule.
Blocked by: [competition-comparison-article]

#### [user] Retire the old nerds-channel pin once the bot's sticky welcome is live [nerds-old-pin-retired]
Filed 2026-08-28 with [nerds-welcome-sticky-rebump]. Once the welcome is bot-authored and re-bumping, your pinned copy is a second stored text saying the same thing, and only you can remove it — the bot cannot delete or unpin your message.

**Walkthrough.**
1. Confirm the bot's welcome is live: open 🤓test-rezips-for-nerds and look for the welcome text as a recent message under the bot's name (it re-bumps at each entry post).
2. Hover your old pinned welcome message, open the ⋯ menu, choose **Unpin Message**, then delete the message. Look for: the pins flyout no longer listing it, and the channel holding only the bot's copy.
3. Tell this project; the register line for the pin is re-pointed at the bot's copy and this item closes.
Blocked by: [nerds-welcome-sticky-rebump]

#### [user] Rezip, restart, then run /setup so this project gets the workshop folder [workshop-migration-setup-run]
**Your sequencing, 2026-08-29:** the migration does the move, rather than a bespoke build doing it and the migration recipe being written separately. This project's own folders get carried across by the shipped machinery, which is the strongest test that machinery can have.

**The dependency is host-side and does not resolve in the session that builds [workshop-becomes-a-method-folder].** /setup runs from the installed plugin, not from the source in this repository, so the build has to be rezipped and the app fully restarted first — otherwise /setup migrates to the old shape and reports success.

**Walkthrough.**
1. Ask for a rezip once [workshop-becomes-a-method-folder] has been built and committed. Look for: the rezip reporting the installed stamp equal to the target's.
2. Quit the desktop app completely and reopen it — plugins load at launch, so a reopened window is not enough. Look for: the session opening reporting the new version.
3. Type /setup in this project. Look for: it reporting that the project's documents are on an older format and offering to migrate, rather than saying everything is current.
4. Let the migration run. Look for: a `workshop/` folder at the project root with `resources/` inside it, and `research/` and `testing/` still sitting inside that.

Observable: `workshop/resources/research/` and `workshop/resources/testing/` exist, and no `resources/` folder remains at the project root.

**References break between this step and the cleanup, and the window is minutes rather than days.** Six root documents name `resources/` paths — `CLAUDE.md`, `SPEC.md`, `README.md`, `QUEUE.md`, `CYCLES.md`, `TOOLS.md` — and they are repaired by [repo-cleanup-product-forward], which runs in the same sitting once this finishes.
Blocked by: [workshop-becomes-a-method-folder]

#### Repo cleanup: foreground the product, and treat everything peripheral [repo-cleanup-product-forward]
**Raised by you, 2026-08-29.** Your framing: you have no idea what half the files littering the repository are for, many may have outstayed their welcome, others need better organising or gitignoring — and you want the repository more product-forward, foregrounding what Throughliner is, with anything peripheral to the product itself treated by delete, reorganise, or gitignore.

Filed at the moment you raised it so the reference from [post-drafts-leave-the-queue] resolves; processed in the same session, and split there into three pieces on your agreement. [repo-debris-proven-fixes] took what was already provable; [repo-inventory-audit] answers what each file is; this item keeps the presentation question, which is the one that needs your taste rather than a finding.

**The question this owns: what a visitor to the repository sees first.** The root held seventeen tracked files with no separation between the product and the workshop. **Designed 2026-08-29 with the inventory in front of us**, so it is no longer held on the audit.

**The principle you settled, which governs every call below:** tracked means part of Throughliner, and anything the project merely refers to is either moved into `workshop/` or gitignored. Your reason: someone shopping online for a method should see the method, not the workshop.

**Stays at the root:** `README.md`, `INSTALL.md`, `LICENSE`, `plugin/`, `.claude-plugin/` and the dot-files — plus the method's own documents, which stay because they demonstrate it: `SPEC.md`, `CLAUDE.md`, `QUEUE.md`, `LOG/`, `FAQ/`, `CYCLES.md`, `TOOLS.md`. `EDITING-STATE-CONTRACT.md` stays because another application is built against it and needs a home a stranger can find. `self-authoring-rules.md` comes up to the root — your call, on the ground that it is one of the more interesting artifacts here and currently sits three levels down.

**Moves into `workshop/`**, which exists by then, created by [workshop-migration-setup-run]: `ANNOUNCEMENT-IDEAS.md`, `FABLE-BRIEF.md`, the three image files, and the loose top level of `workshop/resources/` — `release-ritual.md`, `rule_signals.py`, `discord_post.py`, `rule-maintenance.md`, `method-compliance-audit-checklist.md`, `retired-terms.md`, `method-map.md`, `beta-offer-announcement-template.md`, `nerds-welcome.md`, `plugin-behaviour-retired.md`, `2026-08-09-emergency-revert-plan.md`, `queue-two-section-migration-recipe.md`. That leaves `workshop/resources/` holding `research/` and `testing/` only, which is what its own rule says it holds.

**Moved rather than gitignored, on Claude's recommendation and your agreement.** Much of it is machinery rather than reference — the bot script posts to the Discord, and the rule checks and test suites are what a close is required to run. Ignoring them would leave them on one machine with no history behind them, which is the exposure a hook was built to guard against on the outbound register.

**Gitignored:** the Discord post drafts folder, which is [post-drafts-leave-the-queue]'s destination. `YouTube/` and `INBOX/` already are.

**One fact that bounds the ambition.** `Throughliner-icon.png` is 4.5MB, roughly 40% of the working tree, and deleting it reclaims nothing: the blob stays in history, and this project refuses history rewrites because its records are full of commit hashes. Placement only.

**Files.**
- `.gitignore` — the drafts folder added.
- `CLAUDE.md`, `SPEC.md`, `README.md`, `QUEUE.md`, `CYCLES.md`, `TOOLS.md` — every `resources/` path repaired to `workshop/resources/`, derived from a grep for the literal string rather than from the design discussion.
- the moves themselves, by `git mv` so history follows the file.

Observable: a grep for `resources/` in a tracked file outside `workshop/` returns nothing, and the root's tracked entries are the list above and no others.

**The bot gets its own folder inside the workshop — your direction, 2026-08-29, answering half of [unreferenced-brand-files-and-brief]:** `throughlinerprojectboticon.svg` is the bot's live Discord avatar, so `workshop/bot/` holds everything that is the bot — `discord_post.py`, `nerds-welcome.md` and the avatar — healthily separate from the project and the posts it handles. Your words on its status: it is a folder, and it is not being popped out. Moving the file changes nothing live; Discord holds its own copy of the avatar.

**One consequence the build must surface as a `[user]` step:** the permission rule added 2026-08-29 names the script's path literally — `Bash(py resources/discord_post.py *)` in `.claude/settings.local.json` — and CYCLES.md's step commands name it too. The CYCLES.md repairs are the build's; the settings line only the user can edit, so the build stops and hands that one over when the move lands.

**`FABLE-BRIEF.md` is deleted — your call, 2026-08-29: it has done its job.** The build removes it with `git rm`, so history keeps it and the delete is revertible. It comes off the moves list.

**The badge becomes the repo's face — settled 2026-08-29 with [unreferenced-brand-files-and-brief].** Your account of `throughliner-icon-badge.png`: used on Discord only so far, possibly created to meet its size limits. The build embeds it at the top of `README.md` as the project's logo — it stops being unreferenced by being used, it serves the product-forward goal directly, and at 188K it is embeddable where the 4.5MB original is not. The original still moves to `workshop/`; history keeps it either way.
Runs alone
Blocked by: [workshop-migration-setup-run]

#### Migrate this project's rezip, push and release prose into ritual definitions [host-rituals-migration]
Filed 2026-08-28 with the keep of [ritual-definitions-and-offers], from your framing that the release and rezip rituals are subparts of cycles. Host-only. **Designed 2026-08-29 at processing; both original blockers had built and are dropped.**

**The move:** the rezip's numbered steps and the release's numbered steps leave `resources/release-ritual.md` and become two ritual definitions in `CYCLES.md` — firing words "rezip" and "release", each with its `Writes:` field (the rezip declares `plugin/rezip-archive/`). The weekly-release cycle's step 3 points at the release definition instead of at the old document, so the steps live once. Nothing about how the user fires either changes.

**What stays, each for a recorded reason.** `release-ritual.md` survives as the reference companion holding the recovery procedures and the marketplace-collision guard — what-if material, not steps of a turn; its step lists are replaced by pointers to the definitions. CLAUDE.md's push section is untouched: push fires on a standing condition Claude must notice unprompted, not on a word, so it does not fit the ritual shape — the record already settled that a rule that must fire unprompted cannot be fetched.

**Files:** `CYCLES.md` (two definitions with `Writes:` fields), `resources/release-ritual.md` (step lists out, pointers in, recovery and guard kept), `CLAUDE.md` (the fetched-doc section repointed at the definitions).
Observable: a grep finds the rezip and release step lists in `CYCLES.md` and not in `release-ritual.md`, and CLAUDE.md's pointer resolves to the definitions.
Rule gate: run — an amendment relocating existing rules; nothing new admitted, no slot spent.

**Held on the zip fix, and the blocker is real:** [zip-entries-use-backslash-separators] rewrites the zip step in the same document, two items editing one file must not interleave, and the migrated definition should carry the new Python zip step rather than the PowerShell one it replaces.
Blocked by: [zip-entries-use-backslash-separators]
**Ordering, written on both items per the known-ordering rule (2026-08-29):** [ritual-declares-writable-paths] shipped 2026-08-29, so the definitions this migration writes carry the writable-paths field from the start.

## Unprocessed

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
**Verified 2026-08-29 against the installed build's setup procedure — all five claims hold**: the parent-spec read, the confirm-with-you step, the mail to the parent, upward-only dependencies, no scripted way back in. **Destination is #tips by the two-kinds tie-break** — it reports a change and walks through the how, and where both tests pass the tip test wins. **Posting waits for the next session on your decision's practical ground**: the send-permission rule ([discord-script-permission-rule]) was added 2026-08-29 and takes effect only in a fresh session, so this becomes the first terminal-free post rather than one more walkthrough. A re-verify at post time is not owed twice — the claims were checked today against the same installed build.
Not before: 2026-08-29
**Draft (under 2,000 characters):**
> **Subprojects: start big, split later.** When one part of your project outgrows the rest — the software inside a business plan, the contracts inside a venture — you can now pop that subfolder out into its own full Throughliner project. Run setup inside the subfolder: it reads the parent project's spec, works out which part this is, checks with you, and tells the parent it's moved out. From then on it's an ordinary project with its own clear queue.
>
> The quiet benefit: you don't have to understand your project's final shape at the start. If the idea is nebulous and multi-parted, start it as one big project, rest assured that any part which grows a life of its own can be popped out later.
>
> The link back is deliberately simple: work in a subproject can hold up work in the parent — never the other way round — so the popped-out piece marches forward on its own terms, and anything crossing between them travels as mail you approve, never as one project silently editing another. One thing to know going in: there's no scripted way to pop a subproject back in, so it's for parts that have genuinely outgrown the nest.

#### [user] Discord post draft: multi-person sessions [discord-post-multi-person]
Drafted 2026-08-25 at the planning close under the close-sweep design; approved as a candidate by you, with your additions: name Chagora — your new app by its-coughfee, designed to work with Throughliner but not dependent on it — and credit zebbern. Both names are published GitHub identities, which is what the scrub rule permits. Explanatory register. Waits on [multi-user-identity-layer] shipping; verify against the shipped build before posting (one-a-day pacing repealed 2026-08-28).
**Date passed 2026-08-30; posting waits for the next session on your agreement, same ground as [discord-post-subprojects]:** the send-permission rule takes effect only in a fresh session, so it posts terminal-free there, after the subprojects post. Claims are verified against the installed build at posting — unlike its sibling, this one has not been verified yet. Pacing between the two is the posting session's call.
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

#### Pop the YouTube folder out into its own project [youtube-subproject-popout]
Your direction, 2026-08-28: the `YouTube/` subfolder starts life inside this project and pops out as its own full Throughliner project later — your timeframe, "maybe in a month or something", written as the date below and adjustable on your word. The pop-out is the shipped subprojects flow: /setup run inside the subfolder reads this project's product truth, confirms which part it covers with you, and tells the parent it moved out. Until then the folder is gitignored working space ([youtube-folder-gitignored]).
Not before: 2026-09-28

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

**Settled 2026-08-29.** It is a finding, not work: nothing changes in any file because of it, so under the three-way triage its home is this session's record rather than the queue. **The close carries the coverage record below into that entry and then deletes this item** — deleting it now would rely on a later write that has not happened yet.

**Re-confirmed at the second 2026-08-29 planning session, which is executing it.** The close that was meant to carry this out missed it — caught only because the ladder re-presented the item, which is the queue doing its job. Checked against the same day's ruling that audit findings always belong in the queue: that ruling protects findings nobody has weighed yet, and this one has been weighed to completion, so the settled fate stands. This session's close copies the coverage list below into its record and deletes the item.

**Its one live finding is fully handled and has left this item.** The 2026-08-22 post's claim is not merely falsified — reading `#announcements` through the bot proved the post is **live** (`1540531465115410553`), while `INBOX/sent.md` had recorded it as "approved, not yet posted" since the day it was written. That wrong status is why no repeal-grep ever fired on it. The register line is corrected, the false sentence on [comparison-article-post-needs-rewrite] is corrected, and the public correction runs through [announcement-back-catalogue-rehomed].

**The sweep's own accuracy is worth recording alongside its coverage:** it listed that post among "all 22 posts in #announcements", which was right about the channel and inconsistent with the register it did not check. Neither artifact was compared against the other until now.

All 22 posts in #announcements were read, back to the channel's first message (2026-07-30). Five reshape into tips and are filed above. The rest were passed over, with grounds:

- **2026-07-30 forum topics; 2026-07-31 the Sovereign Implementer rename; 2026-08-25 the Fable graduation and support channels; 2026-08-26 the first beta and nerd role; 2026-08-27 v1.21.1** — project news, not a feature explained. Two of them are already covered by shipped FAQ entries.
- **2026-07-31 terse docs; the five 2026-08-03 posts on the terse-docs experiment, the pseudocode research, the measurement harness and the doc-size defence; 2026-08-09's three rollback and law-prose posts; 2026-08-10's `plugin-behaviour.md` retirement** — every one fails the visibility test. They describe how the method's own text is arranged, which is the exact class the posting brief now excludes. Their proper home is the law-prose article, which [law-prose-article] already owns.
- **2026-08-08 learning mode** — a feature that was never built. The shipped-only rule bars it.
- **2026-08-22 "builds no longer read your queue"** — the claim is FALSIFIED. The generated build view was retired on 2026-08-27 and builds read the queue again. This must not be recycled, and it is the one post in the channel whose subject is actively wrong; whether a correction is owed is a question for processing, noting that the post's other half (the comparison article) is separately owned by [comparison-article-post-needs-rewrite].

#### Planning work surfacing inside a `[user]` walkthrough has nowhere to go [co-writing-flavour]
**Raised by you, 2026-08-28**, mid-walk-through of [law-prose-article], and reshaped at processing the same day when you named the underlying cause. **Your framing, which is the item:** co-authoring is both your work and Claude's, it "works slightly different each time", and "we always have to just kind of shove it in there somehow". The concrete instance: evaluating that item's fourteen-claim list was *planning* work — weighing each claim on its merits — performed inside a walkthrough, where there is no room for it, so it came out as fourteen approval turns.

**Merged in at processing from the deleted [co-writing-shape-question]**, which asked the same question from the other end: is co-writing a new flavour (heavy — a flavour must be wired into `plan.md`, `next.md` and `done.md`, and pass the rule gate), a walkthrough convention (cheap — a shape `[user]` items can carry), or nothing needing a name? Your call at that filing was to experience it first and judge from a lived instance; the 2026-08-28 run supplied one, which is what makes this ripe. The record warns against typing nuance into a taxonomy; the counterweight is your observation that the untyped version mis-set expectations for who writes.

**Design progress made 2026-08-28, so the next turn starts further along.** The always-loaded inversions block already says what may be delivered as a set rather than one at a time, and it already excludes `[user]` walk-through items as "driven live, always sequential". So an amendment there is a candidate cheaper than a flavour. It is not airtight: the block names walkthrough *items*, and fourteen claims produced *by* a step are not obviously that — closing that gap may be the whole fix.

**Refused 2026-08-28, your verdict:** processing each claim the way /plan processes a capture. Your reason — the interaction was long and probably too tedious, not time-saving, and it was an experimental ask at the time. Not to be re-proposed as the answer here.

**The drafting half has left this item.** [co-authoring-txt-draft-loop] took the mechanism — a `.txt` draft you edit directly with a read-back loop — because it was specified and this is not. What stays here is the routing question that a drafting mechanism does not answer.

**An outbound message about this is wanted and is deliberately NOT sent yet — your instruction, 2026-08-28.** You asked to hold it so it does not muddy a test running in a parallel session at the time this was filed. You will say when that test is done. Nothing has been drafted or sent. Whoever picks this up: do not send on the strength of this paragraph — the send needs your explicit yes to the exact text, like every outbound artifact.

**An outbound message about this is wanted and is deliberately NOT sent yet — your instruction, 2026-08-28.** You asked to hold it so it does not muddy a test running in a parallel session at the time this was filed. You will say when that test is done. Nothing has been drafted or sent. Whoever picks this up: do not send on the strength of this paragraph — the send needs your explicit yes to the exact text, like every outbound artifact.

**A note for whoever processes this, about the session it was filed in.** A parallel session was running on the user's machine while this was captured. This project's rules say to work on a project from one chat at a time, because a capture filed in one chat is invisible to the other; whether that parallel session was on this project or on a consumer project was not established at filing.

#### Augmentatism article: where Throughliner fits the philosophy and where it fails its central claim [augmentatism-article-material]
Filed 2026-08-28 from INBOX mail sent by the flintcraft.tech site project (archived at `INBOX/archive/2026-08-28-from-flintcraft-augmentatism-article-idea.md`).

**Provenance is unusual and binding: the analysis in the mail is Claude's reading, not the user's.** She raised the idea and named its centre — an article on all the ways Throughliner is so augmentatist, and so not, especially the Law of Creative Latency, which she calls Throughliner's strong suit — then deliberately stopped before reading the analysis, so as not to prime herself. She is writing her own commentary on the manifesto and intends to cross-pollinate the two. Nothing in the mail's reading may be presented back to her as her position.

The source is `https://augmentatism.com/`, a manifesto by Manolo Remiddi. The mail's summary of it is a fetch from 2026-08-28 and is to be re-verified before drafting. The mail's candidate shape: Throughliner satisfies the philosophy's principles almost point for point — Creative Latency most of all, since the method's whole shape is friction placed on purpose — while failing its central political claim, the Many versus the One, because it is built entirely inside one company's ecosystem.

Two constraints from the sender's own rules travel with it: a named person's published work gets third-party care (describe accurately, verify, never argue the author is wrong), and the site's SPEC bars claiming Throughliner is the only holder of any value.

**What lands here is the sending-back half:** the mail asks that this be processed here and sent back. Articles for the site are written there; this project's part is its reading of the method against the manifesto. The send needs the user's yes to the exact text like any outbound message.

#### Method-defect watch: nothing asks Claude to look, where the security screen already does [method-defect-watch]
Filed 2026-08-28 from the same mail as [sent-register-untracked] (report 2 of 2). Data from another project.

The method carries a standing duty to screen every chat for data-exposure risk, honest that it catches only what it spots. There is no equivalent duty for defects in the method itself — the routing rule fires when a user reports one, so the channel is wholly reactive. The sender's evidence: three method-level defects surfaced in one planning run there, all found sideways while doing unrelated work, none by looking. The user's suggestion, in her framing: Claude should be instructed to proactively watch for things that are method issues rather than project issues.

Two limits the mail states so this is not adopted as more than it is: a standing watch is a noticing duty of the security screen's class — improves the odds, guarantees nothing, and must say so wherever written; and it has a cost the security screen does not, since friction is not a defect and the duty invites every awkward moment to be reported as one. The sender says it probably needs a threshold and offers no view on what.

For processing: the rule gate applies in full — this is a candidate always-loaded rule, the most expensive kind, and the admission question is whether the reactive channel's misses are a pointable failure or the sender's three sideways finds are evidence the noticing already happens without a rule.

#### [user] Tip candidate: rituals — a step list you fire with a word [tip-candidate-rituals]
Filed at the 1.21.1-test1 rezip, 2026-08-28, per the rezip's tip-candidate step: rituals landed in this build. Passes visibility — a user sees their rituals named at every session opening with the word that fires each, and /plan offers to write one down when it meets procedure-shaped work. A tip would walk through: asking to save a repeated procedure as a ritual, where it lives (the cycles doc), saying the word to run it, and what promotes one to a cycle. Not postable until a release clears it; the release marks this capture with the version when it does.

#### Red-flag markers fail silently when the marker is not at the start of a line [red-flag-marker-silent-shape-failure]
Found live 2026-08-29, in the planning session that processed [sent-register-untracked]. Filed by Claude on your direction to keep it apart from the digest's missing fields — one is about what ordering costs, this is about a risk nobody sees.

**The instance.** That item's marker sat at the end of a prose sentence — "…records public Discord claims. Red flag · State: uncleared". `queue_digest.py`'s `FLAG_RE` is anchored to the start of a line, so the digest never reported the flag on that entry, and neither would anything else keying on the same shape. It was found only because Claude happened to grep for the words anywhere in a line, which is looser than the tool's own pattern. **Rung 1 of the ordering ladder — an uncleared red flag outranks everything — fired by luck rather than by the machinery.** The live instance is repaired: the item's rewrite put the marker on its own line and the digest now reports it.

**Why it is worth more than one repair.** The red-flag design promises the risk is surfaced where the user cannot miss it, and the always-loaded rules say plainly that these markers fail silently against any other shape. This is that failure happening, in the one project most likely to catch it.

**It is the third instance of one family, which is the argument for fixing the class rather than the case.** `Rule gate:` written bold hid a whole session's dispositions from the board twice, and the patterns were widened to tolerate the emphasis. `Blocked by:` carries a written instruction to stay plain for the same reason. Now a red-flag marker mid-line. Each time a canonical shape existed, an ordinary Markdown instinct produced a variant, and the reader went quiet instead of complaining.

**Design progress, so the keep starts further along.** Two candidate routes. Widening the readers' patterns repeats the tolerate-at-the-reading-end move, which has already been taken twice and leaves the deviation invisible. Having the lint flag a `Red flag · State:` string that is not at the start of a line keeps one canonical shape and makes the deviation visible where it is written — the same posture the project took on the `#### ` heading. The second looks right; it is not settled here.

**Check at the keep, rather than assumed either way:** whether `Blocked by:` and `Not before:` have the identical exposure in every reader that parses them, since those two carry the held region and a wrong read there releases work early.

#### Captures a cycle claims as material are still ranked by the planning ladder [cycle-material-captures-still-ranked]
Filed 2026-08-29 at the authoring of the [tips-posting] cycle, which was created to stop eighteen near-identical tip candidates being met one at a time.

**The gap.** Those eighteen are now material a cycle's turn draws from rather than eighteen pending decisions, and the cycle definition says so. Nothing tells the planning ladder that. Next session it ranks them as ordinary captures and presents them one by one again — the exact tedium the cycle was created to end, and the user's own words for it: the interaction was long and probably too tedious.

**Neither existing field fits, checked rather than assumed.** On a capture, `Blocked by:` bows it out while a named *entry* is open, and a cycle is not a queue entry — its capture exists only while a turn is due, so the hold would lapse between turns. `Not before:` needs a date per capture and the user's approval for each, which is eighteen approvals to avoid eighteen presentations.

**Candidate fix, not chosen here:** a capture a cycle definition claims as material is drawn by that cycle's turn instead of being ranked by the ladder — a third arm alongside the two pass-over rules that already skip captures held by a date or by a blocker, which is the parent it would amend. It ships rather than being host-only, since consumers have cycles.

**The load-bearing unknown:** nothing today marks a capture as a cycle's material. The [tips-posting] definition names its pool in prose, which a person can read and a ranking pass cannot. Settling this means deciding whether the capture carries a field, or the definition names something mechanical the pass can match. Do not build the prose-matching version.

**Meanwhile the eighteen are not lost and not cleared** — they stay captures, which is what the pipeline already calls them, and the cycle's first turn draws from them.

#### Post drafts leave the queue, keeping their reasoning behind [post-drafts-leave-the-queue]
**Raised by you, 2026-08-29.** Your position, and the narrowing is yours: the captures themselves are not in dispute — what does not belong in the queue is the full post text. A finished draft is a deliverable rather than work-reasoning, and the method's own view-in-doc rule already says doc-resident text is pointed at rather than pasted.

**You ruled out the LOG, and your own doc routing agrees with you.** `LOG/` records what happened; a draft that has not gone out has not happened, so storing it there turns the record into a filing cabinet. Your words: *"log is not a place for writing to live."* Current practice is the other way — the 2026-08-22 comparison-article draft's full text sits in `LOG/2026-08-22-competition-comparison-article.md` — and that is evidence of practice, not of correctness.

**Measured at processing, and it must not be described as shortening the queue.** QUEUE.md is 772 lines / 138KB. The verbatim draft text is **10 lines**, across three items — [discord-post-subprojects], [discord-post-multi-person] and [discord-post-session-smoothings]. This is a principle fix and will not be felt as a size one. For the record of where the length actually comes from: roughly 155 of those lines arrived during the 2026-08-29 planning session itself, as settlement prose on processed items.

**Claude's position, recorded because it is the one contested point: tracked, not gitignored.** An approved-but-unposted draft carries a public claim and cannot be reconstructed — which is the exposure cleared the same morning on [sent-register-untracked]. A gitignored drafts folder recreates it.

**The destination is deliberately not chosen here.** Where it lands is a question about the repository's shape, which [repo-cleanup-product-forward] answers; deciding it here and re-deciding it in the same session would be the wrong order. That is also why this cannot yet state what it changes: the file list is one path short.

**What it will change once the destination is known:** the three items' `**Draft (under 2,000 characters):**` blocks come out and are replaced by a one-line pointer; the draft text is carried across byte-for-byte rather than retyped.
Blocked by: [repo-cleanup-product-forward]

#### Environment facts learned 2026-08-29 are not in TOOLS.md [tools-md-owes-three-facts]
Filed by /rescan at the end of the 2026-08-29 planning session. Three facts were established live and recorded nowhere durable; `TOOLS.md` is not on the planning session's writable list, so this is a capture rather than an edit.

- **The Drive connection reads a Drive-hosted `.pptx` and returns its text.** Proved by reading `Throughliner.pptx` (a PowerPoint uploaded to Drive, not a native Slides file) through `read_file_content` after `get_file_metadata` confirmed the type. Worth recording because the next session to want a deck's contents will otherwise assume it cannot and hand the user a manual workaround — the exact failure `TOOLS.md` exists to stop.
- **The Discord server's posting role is `Throughliner expert`, granted by DMing the user.** It gates the showcase forum, and any walkthrough that tells someone to post there has to say so.
- **The showcase forum is for ports of Throughliner AND for projects built with it** — the user's own definition, given when the bot could see no messages in the channel and could not tell what it was for.

Also worth a line while that file is open: the bot's known limits as of this date — it cannot create a forum topic ([bot-cannot-create-forum-topics]), cannot read roles or channel permissions, has no pin command, and cannot delete or edit anyone else's messages.

#### Bot cannot read roles or channel permissions, so no permission claim can be checked [bot-cannot-read-permissions]
Filed by /rescan at the end of the 2026-08-29 planning session, where it came up and was left hanging: you asked for a review of the @everyone and @Throughliner expert permissions after a member accidentally edited a forum's guidelines, and nothing in this project could answer it. Everything said about Discord permissions that day came from Discord's documentation, not from your server.

`resources/discord_post.py` does send, edit, list, prune, replies and avatar. It holds a token that would permit a read-only query of a guild's roles and a channel's permission overwrites, and it has no command for either.

**Two things it would buy, and the second is the general one.** A permission question like that one becomes answerable instead of being handed back as a GUI walk-through — which the always-loaded CLI-tool rule says to reach for a tool before doing. And a capability claim about a channel becomes checkable *before* acting on it rather than after: the same session posted to a forum to discover the bot could not, and read a channel to discover it was empty.

**Ordering, not blocking:** [bot-cannot-create-forum-topics] is cleared to run and edits the same file. Whichever builds second should read the other's change rather than assume the file's shape. Neither depends on the other.

**The accidental edit is the reason this is not merely tidy.** Changing a forum's guidelines is a channel-settings change, so someone held a permission that also lets them rename or delete channels. Whether that is still true is exactly what cannot currently be checked from here.

#### Ports being the top priority is recorded only by queue position [ports-priority-unrecorded]
Filed by /rescan at the end of the 2026-08-29 planning session. **Your words that day: ports are now your number one priority.** The four port items were placed at the top of the cleared region because of it, and that placement is the only trace.

**Position is the wrong carrier for it**, by this project's own reasoning: the queue is reordered on request, everything above the readiness line is built by one run so its internal order rarely matters, and the always-loaded rules say a relationship carried by placement rather than by text survives by luck. A reorder erases this with nobody noticing it was ever said.

**What it should change is not obvious, which is why this is a capture rather than an edit.** Candidates: a line in `CLAUDE.md` saying what this project is currently oriented around, which a fresh session reads at every opening; a SPEC sentence, if being a portable method is product truth rather than a current focus; or nothing in this project at all, since the ranked list of your projects lives in the Claude memory project and a per-project priority may belong beside it. Settle which at processing.

**One thing that is already true and does not depend on the answer:** [cross-platform-section-speaks-for-others] rewrites the section a fresh session reads to learn whether ports matter, and it is cleared to run. If that section says ports are supported, the immediate risk of a session dismissing them is already handled — what is missing is the ordering signal, not the fact.

#### Newly filed work can invalidate cleared work, and nothing looks [newly-filed-work-invalidates-cleared-work]
**Raised by you, 2026-08-29**, at the end of a /rescan: should there be a rule checking that what a scan files blocks nothing in the cleared region? Filed as the reworded version of that, on Claude's recommendation and your agreement.

**The rule as first put was refused, and the reason travels with it so it is not re-proposed.** A capture cannot block anything by construction: only a Processed item carrying `Blocked by:` holds work back, and /rescan files captures and nothing else. A check for that would never fire, which is worse than one that fires rarely — it would read as coverage while covering nothing.

**The real risk is invalidation rather than blocking, and there is one recorded instance, from the session that raised it.** Filing [bot-cannot-create-forum-topics] revealed that [ports-forum] — already cleared to run — could not be built as written, because the bot cannot create a forum topic at all. Nothing detected that. It was caught because the same session happened to be holding both items in view, which is exactly the condition a fresh short session does not have.

**What is already nearby, so this is weighed as an amendment before anything freestanding is considered.** The queue digest reports placement contradictions, including an item in Processed whose own text says it must not be built. That is the same family — a cleared item whose premise has gone — but it reads the item's own words, and here the falsifying fact arrived in a *different* entry that never mentions it.

**Open at the keep, and the first is load-bearing.** Whether this is detectable at all without judgement: the falsifying relationship was semantic, not textual, and nothing in the queue linked the two entries. Whether the site is /rescan's filing step, /plan's decision step, or the digest. And whether the honest answer is a prompt to look rather than a check that claims to find — which is the shape the security screen already takes, catching what it spots and promising nothing.

**Do not build a check that reports a clean pass.** If this lands as anything, it must be able to say it found something and otherwise stay silent, because a clean result here would assert that no cleared item has been invalidated — which nothing can know.

#### Forum topics resolve in the posting script but cannot be listed by it [discord-script-lists-forum-topics]
Filed 2026-08-29 by /next while building [bot-cannot-create-forum-topics], which added forum-topic creation and made channel resolution fall back to the guild's open threads. Adjacent work rather than part of that item, so captured rather than folded in.

`active_threads()` now exists inside `resources/discord_post.py` and works live — it returned the eight open topics on the server, the six how-to ones among them. Nothing exposes it on the command line, so a session that needs the list writes a throwaway `python -c` against the module, which is the shape this project's tooling rules push work away from.

**Two pieces of standing work need exactly that list.** The announced-claims sweep reads each forum's topic order every turn and reports where it no longer matches the numbers in the titles. And [howto-posts-bot-authorship]'s first step reads where a topic sits in the list after each post, to settle whether posting re-orders a forum.

The change is small: a `threads` subcommand printing each open topic's id and name, per forum. The listing route is already written and already handles a guild refusing the read.

#### SPEC's ports paragraph recognises two flavours without naming them [spec-owes-port-flavour-names]
Filed 2026-08-29 by /next while building [port-flavours-named], which named them. A build never writes product truth, so the sentence is filed for the next planning session rather than written into SPEC here.

SPEC's Ports paragraph currently says two flavours are recognised and both supported, and describes each one without a name. The build gave them names — **tracking** and **independent** — defined in the shipped `plugin/throughliner/docs/ports.md` and named in `README.md`. Until SPEC carries them, product truth describes a feature the shipped docs state one level more precisely.

The sentence SPEC owes, proposed rather than written: *The two flavours are named — **tracking**, which takes this project's changes as they come and adds nothing beyond what its own system needed to fit, and **independent**, which is its own thing and adopts only the changes it wants — because a flavour nobody can name is a promise nobody can read.*

#### Navigation is 22% of tool calls in both a build run and a planning run [navigation-share-measured-at-22-percent]
From the run-token-cost audit, not yet reviewed. This is the numerator [run-token-cost-audit] existed to count, and the figure the MCP-server proposal has to be worth.

**Measured from the raw transcripts**, classified by tool and by command after stripping the `cd "<path>" &&` prefix every command in these transcripts carries — a detail worth keeping, because a first pass that missed it put a quarter of all calls into "unclassified" and reported navigation at 5%.

```
BUILD run   2026-08-28 05:53 -> 14:10, on Opus 5
            417 tool calls — 91 navigation (22%), 271 work (65%)
            of the navigation: 71 searches and shell reads, 20 re-reads of a
            file the run had already read

PLANNING    2026-08-28 13:30 -> 2026-08-29 00:58, on Fable
run         254 tool calls — 57 navigation (22%), 159 work (63%)
            of the navigation: 53 searches and shell reads, 4 re-reads
```

**The two runs are on different models and are stated separately for that reason** — the user's instruction at this run's off-ramp. They are not interchangeable figures, and it is a coincidence rather than a finding that both land on 22%.

**Against the fixed read cost, which no transport changes.** A run loads before it navigates anything: the always-loaded rules (78KB), `next.md` plus `next-build.md` (55KB), the close docs (73KB), SPEC.md (91KB) and the cleared region of QUEUE.md (of 125KB) — around a third of a megabyte for a build run, and a planning run pays `plan.md` (86KB) instead of the run docs. An MCP server touches none of it.

**So the honest reading: the proposal's target is about a fifth of tool calls, sitting on top of a fixed cost several times larger.** That is not nothing, and it is not the picture the brief implied. Whether a fifth is worth a server is the decision this measurement exists to inform, and it is a decision rather than a conclusion the numbers make.

#### Scoping an answer beat changing its transport, on this run's own evidence [scoping-beats-transport-on-measured-evidence]
From the run-token-cost audit, not yet reviewed. It settles half of what [run-token-cost-audit] was asked to settle and leaves the other half open, which is stated rather than glossed.

**What the audit was asked:** whether MCP beats a script flag once the answer is already scoped. **What it can answer:** that scoping was worth roughly a tenth, measured. **What it cannot:** the transport comparison, because nothing here ran an MCP server.

**The scoping measurement, taken this session on this project's own queue.** [digest-answers-whats-next] shipped a `--next` mode: 1,652 characters against the full digest's 16,959. The saving came entirely from answering one question instead of printing everything, and it needed a script flag rather than a new transport.

**Why that bears on the MCP question rather than merely sitting beside it.** Half the brief's proposed tool table is already built as scripts — the digest returns the queue as structured facts in one call, and the mover does moves byte-for-byte — so the delta a server would add is script-versus-tool, not tool-versus-nothing. And the write-side tools it proposed are the exact shape `pre_tool_use` refuses: a project file written through a script rather than the editing tools.

**What a fair transport comparison would need**, if anyone wants one: the same scoped question asked both ways, counted the same way. Nothing here did that, so no claim is made either direction.

**Unverified and still to be checked before any MCP build is scoped** — carried forward from the item so it is not lost: that a plugin may define an MCP server in `.mcp.json` at its root, that Claude Code starts it automatically when the plugin is enabled, and the tool-naming shape. None of it was checked by this audit.

#### Build runs re-read files they have already read; planning runs barely do [build-runs-reread-files]
From the run-token-cost audit, not yet reviewed. A difference between the two runs that neither the item nor the MCP brief predicted, and it points somewhere else entirely.

**The counts.** The build run re-read a file it had already opened 20 times in 417 calls. The planning run did it 4 times in 254. Same project, same week, adjacent days.

**Why the asymmetry is plausible rather than noise:** a build works one item at a time across many files and comes back to a doc it edited earlier to check what it did there, while a planning run reads the queue and works within it. So this is a shape of build work rather than a defect on its face.

**What makes it worth an item anyway.** A re-read is the one navigation class where the session already had the content and fetched it again — which is a memory or working-file question, not a transport one. An MCP server would not remove a single one of them. If a fifth of a run's calls are navigation and a fifth of those are re-reads, that is the cheapest thing on the list to look at and nothing has ever looked at it.

**No fix is proposed here**, deliberately: what would help — recording in the build working file what each item touched, so a later item reads that instead of the file — is a design question for a planning session, and this audit's job was counting.

#### Audit close records the outcome of an approval step the audit procedure repealed [done-audit-records-a-repealed-approval-step]
From the compliance audit of 2026-08-29, not yet reviewed. Lens 1 (eviction debt) and lens 3, delta scope.

**The contradiction, in two shipped docs a single audit close reads together.**

```
next-audit.md, "File the findings to Unprocessed"
    "Nothing waits for approval here." Findings are appended to Unprocessed
    and the run carries on; asking the user to accept a set of findings before
    filing them makes them assess the same material twice.

done-audit.md, step 2.1's body fields
    "Approval outcomes — what happened at bulk approval — findings dropped or
    reworded, each with the user's reason; or 'all findings approved as-is'."
```

**Where each fires.** `next-audit.md`'s statement fires during the run, at the moment findings are written. `done-audit.md`'s field fires at the close, when the LOG entry for that same audit item is written — minutes later, in the same session, over the same findings. So one session reads both, which is what makes this a genuine duplication rather than two docs that happen to disagree.

**What the close is being asked to record does not exist.** There is no bulk approval in an audit run any more, so the honest value of that field is always "all findings approved as-is" — which asserts an approval that never happened. A required field whose only truthful value is a fiction is worse than no field.

**The retirement left the artifact.** This is the eviction rule's own failure mode: the step went, and the body field the step produced stayed. Same shape as the orphaned generated view, one document over.

**Not proposed here, because an audit files findings rather than fixes:** whether the field is deleted outright or replaced by something that records what the run actually did with each finding — captured, or dropped on Claude's own re-reading, which `next-audit.md` does still allow.

#### Shared mail-triage step carries no stop-and-wait arm, though its own child does [done-mail-triage-missing-prompt-arm]
From the compliance audit of 2026-08-29, not yet reviewed. Lens 2, tag placement, delta scope.

**The tags, on two steps that do the same thing.**

```
done.md, "Triage any waiting mail"
    [SILENT] when the mailbox is empty; [BRIEF] when it isn't
    — and the step goes on to require a reply drafted and the exact wording
      shown before anything is sent.

done-build.md, step 1.5 "Reply to mail the run opened"
    [SILENT] when no mail arrived; [PROMPT] when it did
```

**Where each fires.** `done.md`'s step fires at every close, of every shape, from the commit core. `done-build.md`'s fires only in a build close, before that close's own commit. A build close therefore reaches both, and the two give different instructions about the same moment: one says be brief, the other says stop and wait.

**Why the missing arm matters rather than being cosmetic.** The step it governs ends in something leaving the machine, which is the method's hardest gate. `[BRIEF]` says how much to say; it does not say to stop, and the tag is the mechanism the method uses precisely so that stopping is not left to the surrounding prose. A close that read only `done.md` — a planning close, an audit close, a completed `[user]` item — has no tag telling it to wait at all.

**The prose does carry it** ("show the exact wording before anything is sent"), which is the third failure mode in lens 2's own list: a step describing its output behaviour in a sentence instead of carrying the tag that encodes it.

#### Build close cites the parent for the three walk-through outcomes, then restates them anyway [done-build-restates-cited-outcomes]
From the compliance audit of 2026-08-29, not yet reviewed. Lens 1 on the parent axis, delta scope.

**The pattern is cite-and-restate, which is the harder half of eviction debt to see:** the child does the right thing by naming where the definitions live, and then carries them too, so the duplication reads as a courtesy.

```
done.md
    the full block: done / deferred / not reached, plus "write deferred only
    where the user's own word is on the trail" and "not reached tells the next
    session to present the item fresh".

done-build.md, step 2.1
    "Close each [user] item on one of the three outcomes — done, deferred, or
    not reached — read off the run's own trail (done.md's outcome block, and
    next.md's walk-through branch, carry the definitions). `deferred` requires
    the user's own word; an item the run never presented is `not reached`, and
    the next session presents it fresh."
```

**Where each fires.** `done.md`'s block fires at the routing step of every close, before the sub-doc runs. `done-build.md`'s fires inside the build close's entry-writing step. A build close reads both, minutes apart — which is exactly the parent-axis case, where the child is loaded *with* the parent and the reader has both.

**The citation is what makes it fixable cheaply**: the sentence already names its source, so the restatement can go and the pointer stay. The parenthesis is the whole of what the child needs.

**Not a finding: `next.md` carrying the same block.** `next.md` and `done.md` are siblings, not parent and child, and no single session reads the walk-through branch and the close's routing step for the same purpose. That is the sibling-axis trap this checklist records a worked instance of.

#### Superseded refusal is narrated inside a shipped doc's operative text [inbox-doc-narrates-a-superseded-refusal]
From the compliance audit of 2026-08-29, not yet reviewed. Lens 4, decision history in operative text, delta scope.

**The sentence, in `feedback-and-inbox.md`'s return-path rule:**

> This supersedes an earlier refusal in this doc, which held that writing a path into another project's repository risked committing it: that reasoning predates the check, and with the check in place the file is never committed.

**The delete-and-read test.** Delete it and what remains is *"The return path is safe to write because the recipient's `INBOX/` is gitignored, which the send already confirms — see the gitignore check below, which refuses to send where it is not."* That is a complete instruction. So what was deleted was history, and it belongs in the record rather than in the rule.

**Where it fires.** The doc is fetched on demand — when a user reports a method problem, or when mail is waiting — so this sentence is read by a session that is mid-task on something else entirely, and it is telling that session about a decision made in this document's own past.

**It is the founding shape lens 4 exists for**: no "because" is present in the operative half, the sentence carries a whole defeated position in rule syntax, and it survived earlier passes precisely because it does not read as a why-clause riding a rule.

**Two nearby sentences were checked and are NOT findings**, recorded so a fix does not sweep them up. `done.md`'s "Two limits, and neither may be softened" is an honest-limit statement the method requires, not rationale. And `feedback-and-inbox.md`'s rejection of an automatic read-receipt states a live prohibition — delete it and a future session builds the receipt.

#### Scrub instruction is stated twice inside one doc, three sections apart [done-md-states-the-scrub-rule-twice]
From the compliance audit of 2026-08-29, not yet reviewed. Lens 1, eviction debt, delta scope.

**Both statements are in `done.md`:**

```
"The close's checks report as one narration"
    "Run the scrub checklist before writing a LOG entry
    (skill-nonspecific-rules.md, Scrub before writing)."

"LOG entry files"
    "Run the scrub checklist before writing (skill-nonspecific-rules.md, Scrub
    before writing). A LOG entry gets committed, and a session that ran on
    someone's real situation is where a name or a case detail arrives without
    anyone noticing."
```

**Where each fires.** The first sits in a section about consolidating several checks into one narration — a section about *output shape*, which the scrub rule is not. The second sits at the top of the entry-writing section, which is the moment the rule actually applies and is where the second copy earns its place, carrying what the first does not: why, and what to do with what is found.

**So the first is the redundant one, and it is also mis-sited** — a filing rule living in a narration-shape section is how the duplication got in unnoticed.

**Small, and filed anyway because the class is what matters.** Two statements of one rule are optimal distractors for each other, which is the admission cost this project's own gate is built on. A near-identical pair inside a single document is the cheapest possible instance of it to remove.

#### Inventory of the repository root and `resources/`: what each entry is and what reads it [repo-inventory-table]
From the repository-inventory audit of 2026-08-29, not yet reviewed. This is the answer to "I have no idea what half the files in here are for". **It proposes no fates** — deciding those is separate work, and the audit deleted nothing.

**Form, stated because it departs from what the item asked for.** The item's observable was one finding per entry, which would be about thirty-five captures each ranked independently by the ladder. The inventory's value is in being read whole, so every entry gets its line and they travel in one capture; the four entries that genuinely need their own fate are filed separately alongside this. Say if you would rather have them split.

**Reference counts exclude `LOG/`**, which mentions nearly everything historically and would make every count look healthy.

**Repository root.**

```
.claude-plugin/          the marketplace manifest. Read by the CLI at install.
.gitignore               live.
.throughliner-format-epoch   this project's own format marker, read by
                         session_start at every opening.
.throughliner-version    same, for the version notice.
.throughliner/           editing-state markers, gitignored, self-clearing.
ANNOUNCEMENT-IDEAS.md    152K static seed archive of the retired FAQ's entries.
                         Read for post material; named by CLAUDE.md and the
                         release ritual. Live, and read rather than written.
CLAUDE.md                always-loaded project instructions. Live.
CYCLES.md                the three cycle definitions. Live.
EDITING-STATE-CONTRACT.md    the published field contract another app builds
                         against. Referenced by README, SPEC and its own suite.
FABLE-BRIEF.md           referenced by one queue item and nothing else. Worth
                         a line of its own — filed separately.
FAQ/                     a straight copy of the shipped FAQ templates.
                         session_start points every session at its index.
INBOX/                   mailbox, address book and the outbound register.
                         Gitignored on every path.
INSTALL.md               the install route. Referenced by the FAQ, the shipped
                         FAQ template and the outbound register.
LICENSE                  live.
LOG/                     7.5MB, 1,375 session records. The archive working as
                         designed, and explicitly out of the fate question.
                         LOG/index.md is 316KB — stated as a fact, with no
                         verdict attached.
QUEUE.md, SPEC.md        live method documents.
README.md                live.
TOOLS.md                 environment facts. Read by next-build, the
                         always-loaded rules and pre_tool_use.
Throughliner-icon.png    4.5MB. Rides [repo-cleanup-product-forward]; deleting
                         it reclaims nothing, since the blob stays in history
                         and this project refuses history rewrites.
throughliner-icon-badge.png, throughlinerprojectboticon.svg
                         tracked, and nothing in the repository references
                         either. Filed separately — a grep cannot see a file
                         used as an avatar or a badge somewhere else.
YouTube/                 empty, and gitignored.
.agents/                 empty and untracked. Filed separately.
.pytest_cache/           untracked and NOT gitignored. Filed separately.
plugin/                  the package plus the gitignored rezip archive.
resources/               below.
```

**`resources/`.**

```
research/                676K of findings, 28 references. Live.
testing/                 1.0MB of suites and re-read-later evidence, 13
                         references. Live.
discord_post.py          the bot. 5 references. Live.
rule_signals.py          the rule-corpus checks. 12 references. Live.
release-ritual.md        rezip and release. 6 references. Live.
method-compliance-audit-checklist.md    6 references. Live.
self-authoring-rules.md  the record behind the rule gate. 7 references. Live.
rule-maintenance.md      subtraction techniques. 6 references. Live.
retired-terms.md         source data for the REPEALED check. 7 references. Live.
method-map.md            where each part of the method lives. Named by
                         CLAUDE.md. Live.
beta-offer-announcement-template.md     cycle material. 2 references. Live.
nerds-welcome.md         created this run. 2 references. Live.
plugin-behaviour-retired.md    44K of retired rules kept as history, and an
                         excluded path in the retired-terms check. Live as
                         history — it is not debris.
2026-08-09-emergency-revert-plan.md     the revert's own plan. Referenced by
                         CLAUDE.md and by rule_signals' archival paths.
                         History, correctly kept.
queue-two-section-migration-recipe.md   the recipe for a migration that has
                         run. One reference. A candidate for the retired-
                         artifacts list rather than for deletion.
reader-test-workflow.js  tracked, 24K, untouched since 2026-08-13, zero
                         references. Filed separately.
__pycache__/             gitignored build output.
```

**The honest limit, and it is the item's own:** an inventory finds what it can trace. A file nothing references may still matter to a person — an icon used on a website, a brief written for a model that is not running today — which is why every fate here stays yours and this pass proposes none.

#### `reader-test-workflow.js` is tracked, untouched since August, and referenced by nothing [reader-test-workflow-unreferenced]
From the repository-inventory audit of 2026-08-29, not yet reviewed.

24K of JavaScript sitting in `resources/`, last touched 2026-08-13, with no reference anywhere in the repository outside `LOG/`. It is also the only `.js` file in a project whose scripting constraints say standard-library Python.

**It fails the folder's own rule rather than merely looking untidy.** The always-loaded rules say `resources/` holds two things: research findings under `research/`, and re-read-later testing evidence under `testing/`. A workflow script at the top level of `resources/` is neither, which is the same test that made [repo-debris-proven-fixes] debris.

**Not asserted: that it is dead.** A grep reaches references written down; it does not reach a file someone runs by hand or keeps for a tool that is not in this repository. What the name suggests — a reader test — sounds like exactly that kind of artifact. **So the question for processing is what it was for, and only you can answer it.**

Three fates, in the order this pass would guess: it belongs under `resources/testing/` as evidence, it is spent and goes, or it is live and something should say so.

#### `.pytest_cache` sits at the root, untracked and un-ignored, from a tool this project bans [pytest-cache-at-the-root]
From the repository-inventory audit of 2026-08-29, not yet reviewed.

63K at the repository root. Not tracked, and — unlike `__pycache__/`, `.claude/`, `YouTube/` and the rest — **not named in `.gitignore` either**, so it shows as untracked clutter at every `git status` and one blanket `git add` would commit it.

**What makes it more than clutter: this project's scripting constraints say the suites are invoked as plain scripts and never through `pytest`**, because `python` on this machine resolves to an application's bundled interpreter with no pytest, and its error names that application and sends a session chasing the wrong cause. A pytest cache at the root is evidence that something ran pytest here anyway.

**Both halves are worth settling, and they are different questions.** The folder is disposable and can go. Whether anything still reaches for pytest — a habit, a stale instruction, an editor integration — is the part that would recur, and deleting the folder answers only the first.

**Nothing was deleted by this pass.** An audit reads and reports.

Cheapest fix if it is simply spent: one line in `.gitignore` beside the siblings that are already there, and remove the folder.

#### [user] Allow the posting script in this project's settings, so sends stop needing the terminal [discord-script-permission-rule]
**Captured by you, 2026-08-29**, when the auto-mode classifier blocked every outbound post during [howto-posts-bot-authorship]'s walk-through and you asked to pick it up later.

**What happened, recorded because it shapes the fix.** Claude's reads of Discord went through untouched — the forum listing, the message fetches, the check that a topic survives its opening message being deleted. Only the *sends* were blocked. Claude then tried to add the permission itself and was blocked again, correctly: a session granting itself a permission it was just refused is what that block exists for. Editing the settings file by hand to get around it was refused on the same ground.

**So the rule has to be added by you, and Claude cannot do it.** That is what makes this a `[user]` item rather than a build.

**Walkthrough.**
1. Open `.claude/settings.local.json` in this project's folder. Look for: a list of permissions beginning with `"WebSearch",` near the top.
2. Add this line immediately below the `"WebSearch",` line, keeping the same indentation and the trailing comma:
   `"Bash(py resources/discord_post.py *)",`
   Look for: the new line sitting between `"WebSearch",` and the line that follows it, each ending in a comma.
3. Save the file and start a fresh session. **The change does not take effect in the session that made it** — that is why step 3 is a step rather than a note.
4. Confirm it took: in the new session, Claude posting through the bot no longer stops with "Blocked by classifier".

Observable: a send through `resources/discord_post.py` completes without a classifier block in a session started after the edit.

**What this does NOT change, stated so the grant is not read as wider than it is.** Every post still needs your explicit yes to the exact text before it goes — that is Throughliner's own rule about anything leaving the machine, and it was never what the classifier was doing. The rule also names one script and nothing else.

**Why it is worth doing rather than living with the terminal route.** Re-homing the six how-to posts is about twelve commands, and the announcements back catalogue is twenty-odd more. Each one currently costs a round trip through you copying a command into a terminal window.

#### [user] Post the 1.21.1-test1 entry to the nerds channel, with its archived zip [test-rezip-entry-1-21-1-test1]
**Your direction, 2026-08-29**, when you asked why the previous rezip had not been posted — it should have been, and the close missed the check. Folded to the next session on your instruction, with the zip back-filled first, which is done.

**Ready now, and both halves of the readiness test are confirmed rather than assumed:** a full planning session ran on 1.21.1-test1 (2026-08-29, confirmed from that session's own start block) and a full build run ran on it (2026-08-29). The archive holds its zip and readme, rebuilt from commit `4efdcff` and verified by content stamp `8c874952044d` — identical to the stamp proved equal when the build was installed, so the attached bytes are the tested bytes.

**Walkthrough.**
1. Draft the entry from `plugin/rezip-archive/throughliner-v1.21.1-test1.md`, whose text the archive and the channel post are required to share. Look for: the label, the `Commit:` line and the version matching the readme exactly.
2. The bot posts it to 💡test-rezips-for-nerds with the archived zip attached, on your explicit yes to the exact text:
   `py resources/discord_post.py send --channel test-rezips-for-nerds --body <draft> --attach-archived-zip 1.21.1-test1 --prune-to 15 --rebump-welcome resources/nerds-welcome.md`
   Look for: `Posted to #test-rezips-for-nerds — message id`, then a line saying the welcome was re-bumped.
3. Write the register line in `INBOX/sent.md` in that same turn, naming the channel and reading the claim off the posted text.
4. **Posting this entry unlocks editing the one before it** — the v1.21.0 post — to add a testing-outcomes summary and your rating out of 5. That entry is your own post rather than the bot's, so under the first-iteration note the backfill is yours to paste once.

Observable: the entry appears in the channel under the bot's name with the zip attached, and `INBOX/sent.md` carries its line.

**Blocked in practice, not in principle:** every send in the 2026-08-29 session was refused by the auto-mode classifier, so this needs [discord-script-permission-rule] done first or it goes through your terminal again.

#### Nothing proves the test-rezips readiness check ran at a close, so it can be skipped invisibly [rezip-entry-check-has-no-artifact]
Found live 2026-08-29: the close of a 23-item run did not run the check, and nobody would have known if the user had not asked why the previous rezip was unposted.

**The check as it stands.** `CLAUDE.md` says that at a close, read the `LOG/` records dated after the installed build's install date and see whether at least one full /plan and one full /next have run on it; where both have, the new entry is ready to draft.

**Why it was missed rather than refused.** The close works through `done.md` and its flavor sub-doc, and this check lives in `CLAUDE.md` outside that sequence. A close can complete every step its own procedure names and never touch it. That is not a discipline failure to be told off for — it is a step with no site.

**And it leaves no trace either way**, which is the part that makes it recur. A clean run and a run that never happened look identical afterwards. This project has solved that shape three times already — the rule-gate disposition, the forward-advisory disposition, the FAQ disposition — each by requiring a recorded line in the session record rather than by hoping.

**Changes.** `CLAUDE.md` — the test-rezips check gains a required line in the close's session record, in the disposition shape the neighbouring obligations already use:

```
Rezip entry: ready — <version>, one /plan and one /next since <date>
Rezip entry: not yet — <version>, <which half is missing>
Rezip entry: none — no rezip since the last entry was posted
```

Observable: a close whose commit follows a rezip carries one of those three lines in its session record, and a grep for `Rezip entry:` across `LOG/` finds one per such close.

**Weigh at processing whether it belongs in `done.md` instead.** It is host-only — consumers have no channel — which is the argument for leaving it in `CLAUDE.md` where the other host-only close obligations live. The counter-argument is that a step in `CLAUDE.md` is exactly what just got skipped. Both readings are real and this item does not settle them.

#### Third steering layer is live in this project, and the compliance checklist says there are two [doubled-rules-table-misses-the-brevity-style]
Found live 2026-08-29 while rebuilding an old build from its commit — `plugin/throughliner/output-styles/` was in it, which a retirement was supposed to have emptied.

**The retirement is real and this is not it.** `concise-throughliner.md` — auto-applied at system-prompt priority — was deleted 2026-08-14. What ships today is a different file, `brevity.md`, named **Throughliner Brevity**, offered at /setup and enabled per project with the user's consent. SPEC describes it correctly.

**But the compliance checklist reasons as though nothing shipped.** Its doubled-rules section says "**Two layers now, not three, and the change is recent**", lists (G) the user's global CLAUDE.md and (M) the method's own always-loaded rules, and builds a twelve-row table on that pair — concluding that eight rows are unattributable and that three M-only rows are "M working alone".

**In this project the third layer is switched on.** `.claude/settings.local.json` carries `"outputStyle": "Throughliner Brevity"`, and that style asserts the method's communication shape at system-prompt level — leading with the decision, one item at a time, plain English for non-coders. So several of the table's M-only rows are not M working alone here, and the table currently overstates what this project's narration tests.

**Why it matters beyond tidiness.** That section exists precisely to stop this project's own good behaviour being read as evidence the shipped rules work. A table that undercounts the layers does the opposite of its job — it makes the evidence look cleaner than it is. The 2026-08-29 compliance audit used this section and inherited the error.

**Changes.** `resources/method-compliance-audit-checklist.md` — the doubled-rules section restated for three layers, with the brevity style's rows marked, and the deletion of `concise-throughliner.md` kept as the history it is rather than as the current state. Whether the style's rows are marked per-project (it is opt-in, so a consumer may not have it) is the judgement the rewrite has to make.
Observable: the section names three layers, the table has a column for the shipped style, and a grep for "Two layers now, not three" returns nothing.

#### Project types nobody expects to run in Throughliner — a listicle video [project-types-listicle-video]
**Raised by you, 2026-08-29**, while reshaping [legal-demo-video-guide], and kept as work of its own on your decision rather than as a variant of that item.

One video running through several unexpected project types, each getting the length of a bullet rather than a whole video. A legal matter is one of them. The reason it works is the same one that makes the legal case worth filming at all: these are not what anyone expects a coding tool to be pointed at.

Undesigned: which project types, how many, how long each gets, and whether the material comes from projects you have actually run or from invented examples. Designs alongside [legal-demo-video-guide] and [determinism-lesson-video], which share the same YouTube-folder sessions.

#### Planned writing never lives in the queue — a rule the co-writing flavour must carry [planned-writing-lives-outside-the-queue]
**Your ruling, 2026-08-29**, given while overruling a misrouting of the repository inventory: captures ABOUT writing pieces belong in the queue, and the larger writing or writing plans they point to do not. Your words at the time: the posts need their own home, and then captures that reference them — and this needs a larger rule as part of the overall development of co-writing as a work flavour.

**The specific instance is already settled elsewhere:** [post-drafts-leave-the-queue] moves the three post drafts' text out, and its destination — a gitignored Discord-posts folder — was fixed on [repo-cleanup-product-forward] the same day. What this capture holds is the general rule, which reaches the article items too ([competition-comparison-article] carries its draft substance inline) and any future writing work.

**Where it lands is the open question, and it belongs to [co-writing-flavour]'s design turn** rather than being decided here: the flavour design should include where planned writing lives, so the rule and the flavour ship as one thing rather than two rules on one subject. Filed by /rescan; raise it when [co-writing-flavour] is processed.
Blocked by: [co-writing-flavour]

#### Sidebar cannot edit `.claude/settings.local.json` — a TOOLS.md fact [sidebar-cannot-edit-settings-json]
Filed by /rescan, 2026-08-29. Learned live while walking [discord-script-permission-rule]: the user could not edit the settings file in the desktop side panel and had to open it through File Explorer in Notepad. Any future walkthrough handing over a settings edit should name the Notepad route from the start rather than assuming the sidebar can do it.

Folds into [tools-md-owes-three-facts] at processing — that capture already collects environment facts owed to `TOOLS.md`, and this is one more of the same shape.

#### First port-facing changelog now has a real consumer waiting — verify the next release publishes it [first-port-changelog-has-a-consumer]
Filed 2026-08-29 by the goal session that assessed the Egnatia-OC OpenCode port and sent its assessment pack (register line in `INBOX/sent.md`). The generator and its release-ritual step shipped in 819f7f1, but no release has run since, so no changelog has ever been published — and the pack's CYCLES.md tells his port's weekly [upstream-catch-up] cycle to look for one on each release, described as coming soon. Two things to check at the next weekly release turn: that the publish step actually attaches the changelog, and that its output over the range his pin trails (743aa63..release) reads usefully for the one tracking port known to exist — he is its first real reader, and the fallback his cycle runs until then is a raw diff. Worth telling him when the first one is up.

#### Ports-forum posts can now cite a live tracking port, and two of its findings are upstream material [ports-forum-gains-a-live-example]
Filed 2026-08-29 by the goal session that assessed the Egnatia-OC OpenCode port (throughliner-opencode on GitHub — a pristine-vendor tracking port, 34/34 files byte-identical to 743aa63). Bears on [ports-forum]: posts 3 and 4 (pulling changes in; declaring your flavour) can now point at a real port doing both, subject to his say-so on being named. Two of the assessment's findings are also candidates for upstream's own docs rather than only his queue: the zip-separator defect already filed as [zip-entries-use-backslash-separators] matters more now a Linux-side porter demonstrably consumes our artifacts, and his ANALYSIS.md's mapping table (Claude Code hook protocol → another harness's events) is exactly the worked example `docs/ports.md` says the mapping judgment needs — worth weighing whether ports.md should link out to ports' own analyses or stay mapping-agnostic. The full assessment survives in this session's LOG record; the pack itself was extracted and not kept.

#### Scope-lock refuses the harness's plan-mode plan file [scope-lock-blocks-harness-plan-file]
Found live 2026-08-29 in the OpenCode-port goal session. Plan mode is a harness feature: it designates one file under `~/.claude/plans/` as the only file the session may edit, and ExitPlanMode reads the plan from it. `pre_tool_use.py`'s planning branch refused the Write — the path is outside the standing list and the scratchpad test — so the session had to write the plan to the scratchpad and copy it across with a shell `cp`, which is a workaround the hook cannot see. The hook predates plan-mode plan files. Candidate: permit the harness's plans directory the way the scratchpad is permitted — it sits outside the repo, so nothing the scope-lock protects lives there. Filed under the rule that any observation of the plugin's behaviour is a testing outcome.

#### Queue lint narrates after every Bash command, not only after queue edits [queue-lint-narrates-on-every-bash]
Found live 2026-08-29 in the OpenCode-port goal session: the advisory line "5 flag(s), all of them already present in the last commit and none introduced by this change" arrived after every Bash command in the session — `git show`, `ls`, hash computations — none of which touched QUEUE.md. The lint's job is flagging format drift after a QUEUE.md edit; a line repeated after unrelated commands is noise that trains the reader to skim, which is the cry-wolf shape this project has repealed measures for. Check `post_tool_use.py`'s trigger: it appears to run its narration on Bash regardless of whether the command could have changed the queue. Candidate: emit only when the flagged set changed, or only on tools and commands that touched QUEUE.md. Filed under the rule that any observation of the plugin's behaviour is a testing outcome.

#### First announced-claims sweep turn is due — the cycle has never run [announced-claims-sweep]
Filed 2026-08-29 at a close's cycles check: the cycle's observable is the date of the most recent `LOG/` entry under its slug, and none exists. The definition was declared earlier the same day, so the honest reading is "first turn owed" rather than "a week behind"; /plan may reasonably decide the first turn rides the next weekly release, which is the rhythm the cadence was matched to. The turn itself: re-read every retained claim in `INBOX/sent.md` for retiring channels and both forums against the installed plugin, file one capture per falsified claim, check forum topic ordering, and record the turn under this slug.

#### Ongoing research: how to support someone into self-hosting Throughliner, whatever their capacity [self-hosting-onboarding-research]
**Raised by you, 2026-08-30**, at the close of the OpenCode-port goal session, when you asked that its artifacts be preserved "for reference and deriving findings for new ports" and framed the outcome sought: we know better how to support someone to become self-hosting on Throughliner, in whatever capacity that is. The standing subject: what a person needs — a porter on another harness, a consumer adopting the method, anyone in between — to reach the point where their project develops itself with the method. The first data point is on file: the OpenCode assessment pack (`resources/research/opencode-port-assessment-pack-2026-08-29.md`), whose reusable parts are the assessment lenses, findings-delivered-as-a-queue, the bootstrap gate before self-hosting, a per-port catch-up cycle, and the hand-delivered seed. What accrues here: how the Egnatia-OC injection actually goes (his bootstrap results and first /plan are the live experiment), the next port's pack, and what [setup-self-hosting-seed] and the ports-forum posts teach about the non-port capacities. For processing: decide whether this stays a standing research line the record accretes under, or spawns specific work items as findings arrive — it is deliberately not a build.

