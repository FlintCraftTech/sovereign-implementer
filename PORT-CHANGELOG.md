# Port-facing changelog: v1.21.0..v1.21.1

For anyone running Throughliner on a tool other than Claude Code. Every entry
below is a change inside the shipped plugin package; the development project's
own work is not listed.

Three limits this states about itself:

- it says WHAT changed, never how to map it — the translating stays yours;
- a change to a Python hook may have no equivalent on your side at all;
- a format-epoch bump means your own users' documents need migrating, which is
  yours to handle. It is flagged here and nothing more.

### 2c76e53 — Mid-build scope asks now lead with a recommendation instead of offering a flat menu

Shipped files: plugin/throughliner/docs/next-build.md, plugin/throughliner/docs/skill-nonspecific-rules.md

A build in the AFK-cats project found a real daylight-saving bug in a file already in scope, stopped, and asked whether to add the fix or file it as its own item — two outcomes, no recommendation, in a message that had already established the fix was small, in one file, and in scope. The user answered "as you recommend", which is a turn spent asking for the recommendation the question owed them.

**Why it was made** (from the record of the session that decided it, `LOG/2026-08-26-build-scope-ask-lands-as-a-menu-plan.md`): Kept on Claude's recommendation and your agreement. The AFK-cats finding: a mid-build scope ask landed as a flat two-option menu though the run had already established the fix was minor, and you spent a turn asking for the recommendation. The fix: the run decides which arm applies and asks one recommended question, the other route named only as the escape. The keep's grep corrected the discussion's one-file scope to two: the scope-growth ask lives in next-build.md, and the discovery table's needed-and-minor arm lives in the always-loaded skill-nonspecific-rules.md. ANNOUNCEMENT-IDEAS.md's description stays true and is untouched.

Record: `LOG/2026-08-26-build-scope-ask-lands-as-a-menu-build.md`

### 2c76e53 — Build blocks gain an optional Inputs: line, and a rule that anything the work needs to start travels in the block

Shipped files: plugin/throughliner/docs/plan.md

Noticed while running this session's own transcript audit. The audit item named the exact `.jsonl` paths to read, but those paths sat in its rationale prose rather than its `Changes:` line — so the generated view, which carries the block and no decision history, showed "preprocess both transcripts" with nothing saying which two. The run had to open QUEUE.md to find them, against the standing rule that a build leaves the queue closed.

**Why it was made** (from the record of the session that decided it, `LOG/2026-08-26-build-view-drops-paths-in-rationale-plan.md`): Kept on Claude's recommendation and your agreement. The view dropped transcript paths that sat in rationale prose, forcing a run to open the queue. The cheaper of the item's two directions won: the block template in plan.md gains `Inputs:` (files the work reads but does not change) plus one authoring sentence — anything the work needs to start goes in the block, never only in rationale. The extra buildability-test limb refused as duplicating that sentence at a per-keep cost. Checked at the keep: today's audit item already complies and the held build items name their files in their blocks, so nothing existing fails. The view copies blocks byte-for-byte, so no script change is expected — the build confirms rather than assumes.

Record: `LOG/2026-08-26-build-view-drops-paths-in-rationale-build.md`

### 2c76e53 — Self-invocation of the method's own skills now refused by the hook, with the early-typing trigger named

Shipped files: plugin/throughliner/hooks/pre_tool_use.py, plugin/throughliner/docs/skill-nonspecific-rules.md

A planning session in the AFK-cats project opened by saying "Rules loaded. Starting the planning run", tried to run the skill itself, and failed. Its next message told the user the skill couldn't be started from Claude's side and asked them to type it again. The user's first experience of that session was a red error followed by being asked to repeat what they had just done.

**Why it was made** (from the record of the session that decided it, `LOG/2026-08-26-claude-invoked-plan-against-the-rule-plan.md`): Kept on Claude's recommendation and your agreement, reframed by your account at processing. The transcript was re-read and confirms the incident (typed /plan, Claude tried to start it, red error, retype). Your account changed the diagnosis: the desktop app takes ~15 seconds before /plan is runnable at session start — typed early it lands as plain chat text, possibly colliding with Claude Code's native plan mode; the other four skills are unaffected, only /plan. And you usually can't resist typing it early, so it recurs. Two halves: the method's — a pre_tool_use guard refusing a Skill invocation of the method's own skills with calm guidance, plus the hand-over prohibition hoisted into its own rule; and Claude Code's — a GitHub issue drafted, approved, and posted under your account (anthropics/claude-code#89739, register line written from the approved text). Two search passes found no adjacent issue.

Record: `LOG/2026-08-26-claude-invoked-plan-against-the-rule-build.md`

### 2c76e53 — Coverage caveat: full sentence once per session, a one-clause back-reference after

Shipped files: plugin/throughliner/docs/done.md, plugin/throughliner/docs/rescan.md

The line about not being able to tell whether earlier conversation has dropped out of view appeared three times across one pair of sessions — twice inside a single session, minutes apart. Every instance was honest and the rule requiring it was doing its job, which is why the fix is not to say it less truthfully.

**Why it was made** (from the record of the session that decided it, `LOG/2026-08-26-coverage-caveat-repeats-within-a-session-plan.md`): Kept on Claude's recommendation and your agreement. The caveat was stated in full three times across one session pair, twice minutes apart; every instance honest, the third reading as boilerplate — which is how an important caveat stops being read. Settled: the teaching moment is the first statement per session; later statements in the same session may be the one-clause form restating the operative fact ("same limit as before: this reaches only what I could still see"). Held in conversation, no stored state, the once-per-rest pattern. Grep found the specimen at done.md ~420 and rescan.md ~120; done-build.md's no-gauge sentence and the fresh-chat-offer rule are different rules, untouched.

Record: `LOG/2026-08-26-coverage-caveat-repeats-within-a-session-build.md`

### 2c76e53 — Environment check reworded so a tool failing from Claude's shell triggers the ask instead of answering it

Shipped files: plugin/throughliner/docs/next-build.md

A run in Taskflowapp watched Gradle fail from its own shell, concluded it could not compile, recorded an outstanding check and asked whether to carry on uncompiled. It never asked whether you could build. You quoted the method back at it, and you were right: `next-build.md` already said to check before assuming an environment is absent.

Record: `LOG/2026-08-26-environment-check-skipped-user-had-to-cite-it-build.md`

### 2c76e53 — The processing pass now opens checkpoint-shaped, so the first item gets its own take-this-one ask

Shipped files: plugin/throughliner/docs/plan.md

You stopped a planning session mid-flow when the first capture arrived with summary, analysis and recommendation in one message: "you're supposed to ask if I want to process it, then I say yes or no, then you make a recommendation."

**Why it was made** (from the record of the session that decided it, `LOG/2026-08-26-first-item-presentation-reads-as-bundling-plan.md`): Raised by you in this session ("you're supposed to ask if I want to process it, then I say yes or no, then you make a recommendation"), filed at /rescan and processed on your direction. The behaviour followed the shipped rules — the first item deliberately had no checkpoint ask — and still read as bundling to the person it serves, in the session whose subject was rigidity. Consistency won: the order-narration message ends with the first item's pointer and "start with this one?", summary and analysis on the yes. One extra turn per session, once; the old over-asking reasoning outweighed rather than called wrong, since the turn now carries the order narration and the pointer.

Record: `LOG/2026-08-26-first-item-presentation-reads-as-bundling-build.md`

### 2c76e53 — Working-file rule-gate lines now carry their slug, so a later tick can't steal them

Shipped files: plugin/throughliner/docs/next.md, plugin/throughliner/docs/done-build.md

Each ticked item writes up to three lines into a build working file: the tick, a slug-bound `Depth:` line, and where the item carries one, a transcribed `Rule gate:` line. The depth line is slug-bound and next.md says plainly why — a bare positional line attaches to whichever tick it happens to sit under. The gate line carried no slug and had exactly that problem, three times in the run that filed this.

**Why it was made** (from the record of the session that decided it, `LOG/2026-08-26-gate-line-in-working-file-is-positional-plan.md`): Kept on Claude's recommendation and your agreement. Three times in one run a tick landed between an item's depth line and its gate line, leaving a gate disposition under the wrong item — caught only because that run was watching. The slug-bound fix won as it did for the depth line: the write-order alternative depends on care rather than removing the need for it. Format becomes `Rule gate: <slug> — …` at next.md's Progress-block spec; done-build.md's transcription reads it by slug; CLAUDE.md's description updated only if it states the slugless form. The LOG-entry `Rule gate:` format is untouched — rule_signals.py parses that, not the working file.

Record: `LOG/2026-08-26-gate-line-in-working-file-is-positional-build.md`

### 2c76e53 — Issue-channel check now speaks one line either way wherever the channel exists

Shipped files: plugin/throughliner/docs/plan.md

From the compliance audit's consistency lens. Two sibling checks sit in `plan.md`'s opening and fire at the same moment. The cycles check had just been rewritten to speak whenever a project has a cycles doc, on the ground that a check speaking only when it files cannot be told from a check that never ran — which is what the cycles check had turned out to be for its entire life. The issue-channel check was still tagged silent unless it filed something.

**Why it was made** (from the record of the session that decided it, `LOG/2026-08-26-issue-check-silent-while-cycles-check-speaks-plan.md`): Kept on Claude's recommendation and your agreement. The cycles check's reasoning applies unchanged — a scan that found nothing is indistinguishable from one that never ran — with its cost bound carried over: the check speaks only where the channel exists at all (`gh` present, and open outbound issues or a repository), and there one line either way. A project without the channel stays silent and pays nothing. SPEC's correspondence sentence checked at the keep and survives.

Record: `LOG/2026-08-26-issue-check-silent-while-cycles-check-speaks-build.md`

### 2c76e53 — Word-growth counter excludes the readiness marker, so moving the line stops inventing deltas

Shipped files: plugin/throughliner/hooks/post_tool_use.py

After a below-line lift — a mover call plus one edit to that item's own block — the advisory word-growth report claimed a different item had lost 8 words, an item no edit in that session had touched.

**Why it was made** (from the record of the session that decided it, `LOG/2026-08-26-lint-word-growth-misattribution-plan.md`): Noticed by Claude, filed at /rescan, kept on Claude's recommendation and your agreement — the cause checked, not assumed. The flagged item's text between HEAD and the working tree is byte-identical; the lint's per-item counter runs each span to the next heading, so the readiness marker's 8 words counted as the adjacent item's and moving the marker at the lift made the item appear to shrink. Fix: post_tool_use.py's word-growth counter excludes the marker line from item spans, with a suite case (item beside the marker, marker moved, delta zero).

Record: `LOG/2026-08-26-lint-word-growth-misattribution-build.md`

### 2c76e53 — TOOLS.md: a home for what a project has on hand, writable under the scope-lock in every session type

Shipped files: plugin/throughliner/hooks/pre_tool_use.py, plugin/throughliner/docs/next-build.md

A build session in Taskflowapp established four facts worth keeping — Android Studio installed, its bundled JDK at a known path, the SDK at another, and Gradle's daemon connection failing from Claude's shell specifically while a plain loopback test succeeded — and had nowhere durable to put any of them. The last one especially: rediscovering it costs a run its first act, which is exactly what had just happened. You expected a list, and the method had none.

Record: `LOG/2026-08-26-no-home-for-a-projects-tool-facts-build.md`

### 2c76e53 — Verification guidance now says to read a check's exit status from the tool, not from a pipeline around it

Shipped files: plugin/throughliner/docs/next-build.md

**The record for this change discusses host-only reasoning.** Read it before porting: part of what it describes may belong to the development project rather than to the plugin.

A run put a Gradle build through a pipe ending in `tail`, read the exit status, and reported the compile as succeeding. Gradle had already failed; the status belonged to `tail`. Claude caught it later and said so plainly.

**Why it was made** (from the record of the session that decided it, `LOG/2026-08-26-piped-check-reports-the-wrong-exit-code-plan.md`): Kept on Claude's recommendation and your agreement. A Gradle failure piped through `tail` reported as a pass — the status belonged to the pipe's last stage — and the tick that followed asserted "done, confirmed", the one false-pass shape worse than no check. The fix, stated as the action in next-build.md's verification guidance: read a check's exit status from the tool itself — bare invocation, or its own status captured explicitly — and trim output separately. The hook suites are invoked as plain `py` scripts by standing rule, so the direct route is safe; the build checks the release ritual's and close step's suite invocations and adds the line only where one could grow a pipe.

Record: `LOG/2026-08-26-piped-check-reports-the-wrong-exit-code-build.md`

### 2c76e53 — Three rationale evictions from plan.md: the orientation read, the cycles step, and the delete branch

Shipped files: plugin/throughliner/docs/plan.md

From the compliance audit's fourth lens, the delete-and-read test. This item hosted all three of that lens's evictions in `plan.md`; the sibling captures [plan-cycles-step-carries-dated-history] and [plan-delete-branch-commentary] were folded into it at planning and deleted.

**Why it was made** (from the record of the session that decided it, `LOG/2026-08-26-plan-log-index-read-carries-rationale-plan.md`): Kept on Claude's recommendation and your agreement as the host of all three rationale-in-operative-text findings; [plan-cycles-step-carries-dated-history] and [plan-delete-branch-commentary] folded in and deleted, their facts carried whole into the host's prose. One build deletes the two why-sentences at plan.md's orientation read, the cycles step's dated-history clause with its shorter copies in next.md and done.md (moved together so the copies agree), and the delete-branch commentary line. Every evicted why already has a named home — the LOG entries for [plan-log-index-read-underdesigned] and [cycles-check-fires-nowhere] — so nothing is relocated anywhere new.

Record: `LOG/2026-08-26-plan-log-index-read-carries-rationale-build.md`

### 2c76e53 — A specimen at the process-now offer, showing the timing answer and the disposition as two separate asks

Shipped files: plugin/throughliner/docs/plan.md

You raised this live: after the process-now offer for the beta install pin, your "yes, process it now" — an answer to *when* — was treated as approval of a design first shown in that same offer message, and two items were written and cleared with no recommendation turn. Your words: "you skipped processing and landed stuff straight to queue like was always happening with 'keep' in the last version."

**Why it was made** (from the record of the session that decided it, `LOG/2026-08-26-process-now-yes-spent-as-disposition-plan.md`): Kept on Claude's recommendation and your agreement. Your correction from this morning's /plan: "yes, process it now" was spent as approval of a design first shown in the same message. The rule already forbids it, so the fix is the mechanism that has actually worked — a specimen, as at the checkpoint. This session is the control case: the same flow ran correctly here (timing yes, interview, separate recommend turn), so the specimen records the working shape. Accept-as-a-slip refused on the capture's cited evidence.

Record: `LOG/2026-08-26-process-now-yes-spent-as-disposition-build.md`

### 2c76e53 — "The ready list" moved into the always-loaded rules, where its three sites can actually read it

Shipped files: plugin/throughliner/docs/skill-nonspecific-rules.md, plugin/throughliner/docs/plan.md

From the compliance audit's distribution lens. `plan.md` declared "the ready list" the standing plain-English name for the cleared region and said it is "used identically in every session's asks" — a claim the rule could not deliver on. It fires at /plan's recommend step, at /next's off-ramp when the run is presented, and at /done when the close reports what is ready. Only the first of those reads `plan.md`; the other two load their own docs and the always-loaded rules, neither of which carried the name.

**Why it was made** (from the record of the session that decided it, `LOG/2026-08-26-ready-list-name-defined-where-only-plan-reads-it-plan.md`): Kept on Claude's recommendation and your agreement. The name is declared in plan.md yet binds every skill's asks — two of its three sites could never read it. The move passes the always-loaded file's admission test (fires at /plan's recommend, /next's presentation, /done's report, and in conversation). Declaration up, usage stays, plan.md's declaring sentence evicted in the same edit.

Record: `LOG/2026-08-26-ready-list-name-defined-where-only-plan-reads-it-build.md`

### 2c76e53 — Register lines must be read off the approved text; the back-check found one line claiming what its post never said

Shipped files: plugin/throughliner/docs/feedback-and-inbox.md

A planning session recorded three settled answers as having been sent to another project, then caught itself: the reply it actually sent didn't contain them. The record ended correct only because the same session noticed within the hour.

**Why it was made** (from the record of the session that decided it, `LOG/2026-08-26-sent-line-written-from-decisions-not-from-the-message-plan.md`): Kept on Claude's recommendation and your agreement. A Taskflowapp session wrote a register line from what it had settled rather than from the message it sent — caught within the hour by luck, which is the wrong mechanism. The clause: the line's claim is read off the approved text on screen at that moment, never composed from decisions. Grep at the keep found the rule stated in feedback-and-inbox.md and this project's CLAUDE.md (Discord section); SPEC's "the exact wording exists at that moment" sentence survives unchanged. The build also runs the one-pass back-check over this project's own `INBOX/sent.md` — nothing has ever checked it — correcting any line claiming what its pointed text does not contain, and naming off-machine texts as unchecked.

Record: `LOG/2026-08-26-sent-line-written-from-decisions-not-from-the-message-build.md`

### 2c76e53 — Session openings now report when the installed build arrived, and refuse to guess when they can't tell

Shipped files: plugin/throughliner/hooks/session_start.py

You raised this from a live instance: an announcement draft claimed you had been running a build "all week" when you had been running it since late the night before. Claude had no way to know how long an installed build had been in place, and the misjudgment recurs.

**Why it was made** (from the record of the session that decided it, `LOG/2026-08-26-session-start-reports-install-age-plan.md`): Kept on Claude's recommendation and your agreement, from your post-close-tail capture. Install age won: the plugin cache directory's timestamp is a readable fact needing no maintenance, and it covers the failure that raised this ("installed 11 hours ago" kills an "all week" claim on sight). Time-under-use refused — it needs a state file, refused here on the standing ground that the first session that forgets to update one makes it lie. The line reports the fact bare, never a verdict on how tested the build is; a missing timestamp degrades to no claim. SPEC's session_start clause written at the keep.

Record: `LOG/2026-08-26-session-start-reports-install-age-build.md`

### 2c76e53 — Queue digest now flags a cleared item carrying no build block, where planning actually looks

Shipped files: plugin/throughliner/scripts/queue_digest.py

Six items sat cleared to run in Taskflowapp and a build run was the first thing to catch them — it stopped before locking scope and named all six as unscopeable. The planning run hours earlier had worked fourteen captures and reported "24 items cleared to build" with nothing flagged.

**Why it was made** (from the record of the session that decided it, `LOG/2026-08-26-unbuildable-items-persist-in-the-ready-region-plan.md`): Kept on Claude's recommendation and your agreement, with the cause established at processing rather than assumed — the item explicitly required it. The digest was run read-only against Taskflowapp's queue: zero placement contradictions with 26 items cleared, and the file counts 40 items to 24 build blocks. So the rot was cleared items with no build block, and the only detections of that state — the advisory lint (fires on queue edits) and the view generator's halt (fires when a run starts) — never fire at a planning opening. The fix: queue_digest.py's placement contradictions gain the class "a cleared build or [audit] item with no build block", one printed line per item; `[user]` items are exempt by design. SPEC's contradiction-class sentence written at the keep.

Record: `LOG/2026-08-26-unbuildable-items-persist-in-the-ready-region-build.md`

### 2c76e53 — Write-first rule: two rationale clauses evicted, the consent clause reclassified as operative

Shipped files: plugin/throughliner/docs/skill-nonspecific-rules.md

Found by the compliance audit's fourth lens, the delete-and-read test. The always-loaded write-first rule had grown two clauses that read as explanation rather than instruction, and because this is the file loaded at every session start, their weight is paid by every session in every project.

**Why it was made** (from the record of the session that decided it, `LOG/2026-08-26-write-first-rule-carries-its-why-inline-plan.md`): Kept on Claude's recommendation and your agreement, from the compliance audit's lens-4 finding. The split settled at processing: "Consent happens in conversation, in plain words, before the write" states an action and stays; "the file is the record of what was agreed" and "costs a wait that buys nothing" are rationale and go. The evicted why already lives in `2026-08-26-audit-write-first-contradiction.md`, which the build cites — the wording was authored deliberately there yesterday, so this is that decision's rationale returning to its record, not new history.

Record: `LOG/2026-08-26-write-first-rule-carries-its-why-inline-build.md`

### 32675a3 — A release compares stamps before packaging, and "as planned" means read the record

Shipped files: plugin/throughliner/docs/skill-nonspecific-rules.md

**The record for this change discusses host-only reasoning.** Read it before porting: part of what it describes may belong to the development project rather than to the plugin.

Two halves of one failure: an instruction pointing at something written down was resolved from memory instead of from the writing.

**Why it was made** (from the record of the session that decided it, `LOG/2026-08-27-as-planned-reads-the-record-and-stamps.md`): From the release trace's other two failures: "as planned" accepted without the plan being opened, and v1.21.0 cut from the working tree rather than the installed test20. Two fixes: a Prior-decisions clause (a phrase pointing at a recorded plan is resolved by reading the record), and the ritual's pre-package stamp comparison with a standalone warning turn — the warn-don't-enforce shape at the exact point it was missed. The user's corrections during processing were folded in as content after she pressed that they must land somewhere: her invariant — a release releases a tested rezip, rezips never imply releases — is stated on the item, with the ritual to say plainly that packaging reads the working tree and the stamp step guards the invariant. The dissolved-soak capture ([pre-release-rezip-dissolved-into-the-ritual]) was deleted as relocated here, its finding preserved in the audit record.

Record: `LOG/2026-08-27-as-planned-reads-the-record-and-stamps-build.md`

### 32675a3 — Audit findings file straight to the queue; the write-time approval is repealed

Shipped files: plugin/throughliner/docs/next-audit.md, plugin/throughliner/docs/skill-nonspecific-rules.md, plugin/throughliner/docs/plan.md

An audit presented its findings as a numbered set and waited, then handled contested ones one at a time, then filed the survivors. The user pointed at the double assessment: they judged the same material twice — once as a list with no context, and again at planning when it was actually being decided.

Record: `LOG/2026-08-27-audit-findings-file-unapproved-build.md`

### 32675a3 — Builds read the queue whole again; the generated view and build blocks are retired

Shipped files: next.md, next-build.md, plan.md, done.md, done-build.md, skill-nonspecific-rules.md, setup.md, migrate-checklist.md, pre_tool_use.py, post_tool_use.py, queue_digest.py

A run used to read a generated file assembled from delimited `--- Build block ---` regions, with the queue itself refused by the scope-lock. The reasoning was structural rather than economical: a build transcribes what it reads, and rationale written into work items had been measured reaching this method's own shipped documents in near-verbatim form. Withholding the prose made that impossible.

Record: `LOG/2026-08-27-builds-read-the-queue-again-build.md`

### 32675a3 — Captures gain a bow-out: `Blocked by:` now works in both sections

Shipped files: plugin/throughliner/docs/skill-nonspecific-rules.md, plugin/throughliner/docs/plan.md, plugin/throughliner/hooks/post_tool_use.py

`Blocked by:` belonged to the held region alone. That left an unprocessed capture with no way to wait on something already in the queue: it returned to the top every planning session and was set aside again, and the only alternative — a `Not before:` date — guesses at a wait the queue could simply check.

Record: `LOG/2026-08-27-capture-blocked-by-build.md`

### 32675a3 — The planning checkpoint says how many entries are left

Shipped files: plugin/throughliner/docs/plan.md

The checkpoint banned every count and tally, which took the useful number out with the clutter. A user deciding whether to carry on through another item has one question the queue can answer — how much is left — and the checkpoint was silent on it.

Record: `LOG/2026-08-27-checkpoint-carries-remaining-count-build.md`

### 32675a3 — One exception to the no-completion-asks bar, keyed on two recorded facts

Shipped files: plugin/throughliner/docs/skill-nonspecific-rules.md, plugin/throughliner/docs/next.md

The bar on asking whether `[user]` work is done is strong and stays strong. It leaves three routes to knowing: the item was walked to its end this session, the user volunteered it, or its walkthrough named an observable check that passed.

Record: `LOG/2026-08-27-completion-ask-carveout-post-close-handover-build.md`

### 32675a3 — The droppable-set ask states its recommendation at any batch size

Shipped files: plugin/throughliner/docs/plan.md

The plural specimen carried its recommendation implicitly — "Drop both, or name any to keep?" reads as a recommendation because of the shape of the question. At a batch of one that shape collapses, and the natural phrasing becomes "drop this, or keep it?", which hands the user a balanced choice where the pass has in fact reached a view.

Record: `LOG/2026-08-27-droppable-set-ask-lacks-recommendation-singular-build.md`

### 32675a3 — Developer and testing words join the translate-away list

Shipped files: plugin/throughliner/docs/skill-nonspecific-rules.md, plugin/throughliner/docs/next.md

The vocabulary rule's translate-in-passing list named method-internal terms — step numbers, procedure filenames, tag names. It said nothing about ordinary developer and testing vocabulary, which is just as opaque to the audience and far more likely to slip out, because it does not feel like jargon to the person using it.

Record: `LOG/2026-08-27-general-jargon-translate-and-walkthrough-readback-build.md`

### 32675a3 — "Keep" retires as the disposition term; an entry is processed, with its outcome named

Shipped files: plugin/throughliner/docs/plan.md, next.md, next-build.md, done.md, feedback-and-inbox.md, migrate-checklist.md, skill-nonspecific-rules.md

"Keep" said nothing about where a piece of work went. It named the operation by its opposite — not-delete — and the queue has two destinations behind it: cleared to run, or held below the line. So the word made the user ask a follow-up question every time, and "keep-step" named the step after the vaguer of the two answers it produces.

Record: `LOG/2026-08-27-keep-term-retired-for-processed-build.md`

### 32675a3 — The queue mover's report is read before continuing, and no retry is blind

Shipped files: plugin/throughliner/docs/plan.md

The mover prints what it moved and where the readiness marker ended up. That report was going unread, and a second run fired on a guess can compound the first rather than correct it — which matters here because the marker's position decides what a whole run builds.

Record: `LOG/2026-08-27-mover-report-confirmed-before-continuing-build.md`

### 32675a3 — Sessions read the date from a fact line instead of assuming it

Shipped files: plugin/throughliner/hooks/session_start.py, plugin/throughliner/docs/skill-nonspecific-rules.md

Sessions were deriving today's date by assumption and writing wrong ones into records, captures and holds. The user reported it recurring across sessions rather than as a one-off, which is what decided the shape of the fix: correcting the two wrong dates would have left the next session deriving the next wrong one.

Record: `LOG/2026-08-27-session-date-anchor-build.md`

### 32675a3 — setup.md's tag-free declaration repealed and every step tagged

Shipped files: plugin/throughliner/docs/setup.md

/setup used to declare itself free of response-shape tags, on the reasoning that it runs on two kinds of session — a fresh adoption where the rules defining those tags are not loaded, and a migration inside an adopted project where they are — and that one text cannot carry markers meaning something on one run and nothing on the other.

**Why it was made** (from the record of the session that decided it, `LOG/2026-08-26-setup-case-d-untagged-plan.md`): Kept on Claude's recommendation and your agreement. A compliance correction, nothing designed: setup.md's pop-out section carries no response-shape tags while two of its steps must wait for the user (the subpart clarifier; the pop-out INBOX message, which keeps its show-first shape). Conditions written outside the brackets per the tag-authoring rule.

Record: `LOG/2026-08-27-setup-case-d-untagged-build.md`

### 32675a3 — The method's own words are the shared vocabulary; standing aliases are retired

Shipped files: plugin/throughliner/docs/skill-nonspecific-rules.md, plugin/throughliner/docs/plan.md

"The ready list" was a standing plain-English name for the queue's cleared region — a second name for something the method already names in the artifact the user is looking at. The corpus was growing such names faster than any session could translate them, and each one costs the user twice: they learn the alias, and they learn the real thing anyway the moment they open the file.

Record: `LOG/2026-08-27-shared-vocabulary-not-standing-names-build.md`

### 32675a3 — The spec-sync gate stops describing a SPEC-trails-behaviour model

Shipped files: plugin/throughliner/docs/done-plan.md

The /plan close's spec-sync gate carried a paragraph from the model that preceded SPEC-leads. It said editing SPEC when a change was merely *decided* would make it describe a product that does not exist yet — "a false SPEC, not a synced one" — and that SPEC moves when the behaviour does.

Record: `LOG/2026-08-27-spec-sync-gate-aligned-to-spec-leads-build.md`

### 32675a3 — `[freeform]` and `Runs alone` are assigned only against a re-read definition

Shipped files: plugin/throughliner/docs/plan.md

The two uncommon execution markers were being reached for interchangeably. They are rare enough that nothing keeps their difference fresh, similar enough in shape to be confused, and each carries a consequence the other does not — so the recorded failure cost the user two corrections at the moment ordering was being settled.

Record: `LOG/2026-08-27-uncommon-flavor-definition-check-build.md`

### 32675a3 — Walkthroughs end at the observable, and another project's steps are filed rather than driven

Shipped files: plugin/throughliner/docs/skill-nonspecific-rules.md, plugin/throughliner/docs/next.md

Two clauses from one recorded stall. A `[user]` item had proved what it existed to prove and then kept going: its remaining steps were cleanup, in a different project, and a run waited on them. The user's own words at the time were that the hand-over was the mistake — the verification had already passed.

Record: `LOG/2026-08-27-user-item-ends-at-observable-cleanup-separate-build.md`

### 32675a3 — "`[user]` line" becomes "`[user]` item" across the shipped docs

Shipped files: plugin/throughliner/docs/skill-nonspecific-rules.md, plan.md, next-build.md, done.md

The method called the same thing an item everywhere except when it carried the `[user]` tag, where it became a "line". Nothing turned on the difference — it was residue from a queue format where a piece of user work genuinely was one line — and it made the docs teach two words for one concept, which is precisely what the shared-vocabulary rule built alongside it forbids.

Record: `LOG/2026-08-27-user-line-terminology-retired-build.md`

### 32675a3 — Walkthroughs name where each stored text lives, and verification steps list their claims

Shipped files: plugin/throughliner/docs/skill-nonspecific-rules.md

Two clauses on the existing walkthrough requirement, both from the same root: a step that reads clearly to its author can be unfollowable to the person driving it.

Record: `LOG/2026-08-27-walkthrough-artifacts-named-and-verify-enumerated-build.md`

### 32675a3 — Every `[user]` item the pass reaches gets its own turn

Shipped files: plugin/throughliner/docs/next.md

A walk-through pass was filtering items away before presenting them, on a judgment about whether each one's moment had come. That decides something the user owns, and decides it out of their sight — the item never appears, so there is nothing to disagree with.

Record: `LOG/2026-08-27-walkthrough-no-batch-precondition-skip-build.md`

### 32675a3 — Walk-through outcomes get a third value, and "deferred" needs the user's word

Shipped files: plugin/throughliner/docs/next.md, plugin/throughliner/docs/done.md, plugin/throughliner/docs/done-build.md

Two outcomes could not describe what actually happens to `[user]` work. An item the run never presented was being recorded as deferred, which tells the next session a decision was made when none was — and the item then sits unpresented with a record explaining why nobody need present it.

Record: `LOG/2026-08-27-walkthrough-outcome-not-reached-build.md`

### 32675a3 — Warn once, then do it: a direct request stops being refused by a rule

Shipped files: plugin/throughliner/docs/skill-nonspecific-rules.md

A direct do-it-now request was being refused on a rule the user had already heard. The instance earning this rule's slot is in the 2026-08-26 build transcript: four asks for one thing, refused each time.

Record: `LOG/2026-08-27-warn-dont-enforce-immediate-requests-build.md`
