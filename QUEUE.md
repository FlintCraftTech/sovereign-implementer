# QUEUE

Two sections. **Processed** — agreed work, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** — captured, not yet processed; the next /plan weighs each item. Every entry in either section is a `#### ` heading (its description) with a `[slug]` at the end of that line and its rationale beneath; an entry in Unprocessed is a **capture**, and it becomes a **work item** when /plan keeps it into Processed. A leading `[audit]` / `[user]` tag names how it's executed; no tag means a build. An item carrying a security or privacy risk gets a `Red flag · State: …` marker — the flag rides the work.

**Authoring a rule for the method's own text? The rule gate is in `CLAUDE.md`, always loaded — run it before you write.**

## Processed

#### Untrack this project's method files: gitignore lines plus git rm --cached [untrack-method-files-here]
**Your decision, 2026-08-30, with the warning given and your "proceed" on record.** Applies your gitignore-everything decision to this project immediately, rather than waiting for [gitignore-choice-with-snapshots] — your framing: enabling the gitignore is not build work in substance, and doing it now lets the very next build clear up the scrubbing rule. Attempted in the planning session; the scope-lock refused `.gitignore` (correctly), and you could not paste the lines yourself because you were on remote control — which is why this is an item.

**Changes.**
- `.gitignore` — append seven lines: `SPEC.md`, `QUEUE.md`, `LOG/`, `FAQ/`, `CYCLES.md`, `TOOLS.md`, `CLAUDE.md`. README, INSTALL, LICENSE and `plugin/` stay tracked — they are the product. Plus one line for the beta-tester material's destination, `workshop/resources/testing/beta-tester/` (and its `workshop/` successor path), folded in here on the user's agreement to [tester-data-carries-employer-material]'s design since both edits land in the same file.
- Run `git rm -r --cached SPEC.md QUEUE.md LOG FAQ CYCLES.md TOOLS.md CLAUDE.md` so git stops tracking them; the files stay on disk untouched. The close then commits the removal like any other change.

Observable: `git status` shows the seven paths as deleted-from-index and `git check-ignore SPEC.md` reports the ignore matching; the files themselves still present on disk with content unchanged.

**Warned and accepted, recorded from the warning turn:** the repo's existing history stays public forever (no rewrite — records anchor to hashes); until the snapshot build ships, these files have no undo and doc writes flip to show-first under the current rule; machinery reading their git history (item ages, held-since dates, ladder age rungs, spec-sync gates, board checks reading LOG per commit) degrades from the untrack onward.

**Ordering, in prose:** first of the cleared items, ahead of [gitignore-choice-with-snapshots], which builds the snapshot net and the scrub amendment that this untracking makes urgent.

#### Gitignore choice at setup made first-class, with local pre-change snapshots keeping write-first alive for untracked method docs [gitignore-choice-with-snapshots]
**Your decision, 2026-08-30**, from your position that the privacy headaches of public method files are not worth it — "enough is enough" — refined in discussion to a choice at setup rather than a mandatory flip: the user keeps the tracked setup as now, or has the method documents gitignored, and the plugin itself supplies the undo safety git no longer provides. SPEC's sentence was written this session, ahead of this build.

**What already exists, so the build extends rather than invents:** setup's privacy posture already offers per-document gitignore for SPEC.md, QUEUE.md and LOG/, session_start already detects and reports untracked docs, and the always-loaded rules already define the untracked consequence — writes flip to show-first, deletions are final. This build replaces that consequence with snapshots.

**Changes.**
- `plugin/throughliner/hooks/pre_tool_use.py` — before a Write/Edit (or a queue-tool run) touching an untracked method document, save a copy of the file as it stands into a local snapshot folder (gitignored, e.g. under `.throughliner/snapshots/`), pruned to a bounded depth stated as a proportion or derived figure, not a bare number.
- `plugin/throughliner/docs/skill-nonspecific-rules.md` — the untracked-doc arm of write-first ("An untracked doc answers the test with a no, so its writes are show-first") is superseded: with snapshots present the recoverability test passes, so write-first stays; the two stated consequences (deletion final, close records from memory) reduce to the close read-back one.
- `plugin/throughliner/docs/setup.md` — the privacy-posture offer presents the tracked-versus-gitignored choice as the two named configurations, **with gitignored as the default — the user's decision, 2026-08-31, superseding the no-default-changes posture**: setup proposes the private configuration in the acceptance-default shape the brevity offer already uses, and tracking is the alternative chosen by answer. The offer states the snapshot net in the gitignored default, and the trade text drops the you-lose-undo warning it can no longer honestly make. SPEC's sentence was rewritten to the new default this session, ahead of the build.
- `plugin/throughliner/hooks/session_start.py` — the untracked-docs report line updated to name snapshots as the recovery route.
- Suites the observation reaches: `workshop/resources/testing/test_session_start_untracked_docs.py` (updated), plus a new snapshot suite file under `workshop/resources/testing/` named by the build.
Reads but does not change: SPEC.md (sentence already written), CLAUDE.md.

Observable: the suites pass; in a fixture project with an untracked QUEUE.md, a guarded write leaves a snapshot copy of the prior version; a grep for "answers the test with a no" in `plugin/throughliner/docs/` returns nothing.

**Honest limit, carried so the build degrades it visibly:** machinery reading these files' git history — first-seen and held-since dates, the ladder's age rungs, commit-anchored records — works less well or not at all in a gitignored project; the build says so where those features report rather than failing silently. Snapshots are one machine, no history: a lost disk loses them, and this is stated at the setup offer.

**Refused options, each with why it lost:** mandatory gitignore for everyone — superseded by your choice-at-setup decision; private repos as the route — fails the product's core case, consumers building public-facing work; encrypted-in-repo (git-crypt/SOPS) — key management is unworkable for a non-coder audience, filenames and commit messages still leak, and history reads would likely return ciphertext (unverified, and not worth verifying while the simpler route stands).

**This project's own configuration is not changed by this build** — you choose gitignore here afterwards, through the same offer at a setup top-up, and that run is when this repo's method files come out of the public repo.
Rule gate: run — an amendment to the write-first rule's untracked-doc consequence, naming its parent; the setup change is procedure, not a rule; nothing freestanding admitted, no slot spent.

#### [user] Beta tester's transcripts land in gitignored storage, unscrubbed, and he is told his employer is identifiable [tester-data-carries-employer-material]
Found 2026-08-30 by /next, from screenshots the tester sent the user while locating his session files; **processed 2026-08-30, design agreed by the user.** His Throughliner project lives inside a work OneDrive folder whose path names his employer, his Windows login is a work account, and a memory filename carries his occupation — so paths alone identify a third party who consented to nothing, in a public repository. Nothing has been opened or downloaded.

Red flag · State: cleared

**Cleared by design, 2026-08-30:** the five raw `.jsonl` transcripts live only in `workshop/resources/testing/beta-tester/` (later `workshop/resources/testing/beta-tester/` once the folder move goes live), which is gitignored — the ignore line ships with [untrack-method-files-here], folded there because both edit `.gitignore`. Never published means no scrubbing of the stored material, per the scrub-moves-to-the-boundary amendment agreed this session (shipping with [gitignore-choice-with-snapshots]). The one residue, accepted knowingly: while any of this project's documents remain tracked, a finding written into them still rewrites his paths to placeholders and uses first name only — a residue that dies as the untracking lands.

**Walkthrough.** Runs after [untrack-method-files-here] builds the ignore line — carried by placement and this sentence.
1. You download the five `.jsonl` attachments from the tester's second email (subject thread "Throughliner beta test — session record, 30 Aug", sent 4:58 the same day) into `workshop/resources/testing/beta-tester/` in this project's folder. Yours because the Gmail connector cannot read attachment content — your own issue anthropics/claude-ai-mcp#943 records exactly that. Look for: five files in the folder, and `git status` NOT listing any of them.
2. Claude confirms the folder is ignored (`git check-ignore` on one file) and makes slim conversation-only copies beside the originals, per the transcript-preprocessing practice in CLAUDE.md. Look for: a one-line report naming the slim files.
3. Claude drafts the message telling him his employer, work login and role are identifiable in the folder paths and filenames of what he sent, that the material is being kept unpublished, and asking whether he minds and whether he wants to move the project out of the work folder for future sessions. The same message asks what his git `user.name` and folder path say (which settles where [setup-infers-a-name-into-spec]'s inferred string came from) and points out the name in his SPEC is his to correct. You see the exact text and it goes only on your explicit yes, by whatever channel you choose. Look for: the draft in chat, then your send.
4. His answer, when it comes, is filed as a capture; the content processing itself is [beta-test-session-records].

Observable: five `.jsonl` files plus slim copies sit in `workshop/resources/testing/beta-tester/`, `git check-ignore` matches them, and `INBOX/sent.md` carries the told-him message's line.

Related: [beta-test-session-records] processes the content; [tester-data-collection-instructions] should carry the store-location decision. ([beta-raw-transcripts-arrived] was folded into the records item and deleted, 2026-08-30.)

#### Setup never writes a name it was not given — inference designed out [setup-infers-a-name-into-spec]
**Reported by the first beginner beta tester, 2026-08-30**, by email to the user; **processed 2026-08-30, fix agreed by the user.** He was never asked his name. SPEC.md — the file every session reads first — had it recorded as a **shortened form he does not use**, which nobody had given it. His reading is that it came from the machine's git settings or the folder path during setup and was then written down as fact.

**The build, agreed without waiting on the source question:** `plugin/throughliner/docs/setup.md` gains the rule that no personal fact — a name above all — is written into SPEC or any scaffolded document unless the user supplied it in the interview's own answers; any wording inviting inference from git config, folder paths or account names is removed. Observable: a grep of `plugin/throughliner/docs/setup.md` finds the supplied-only rule and no instruction to derive user details from the machine.
Red flag · State: cleared
**Cleared by design, 2026-08-30:** the class is removed at the source for every future setup, and his instance is repaired by him — the message going to him under [tester-data-carries-employer-material] step 3 now also asks what his git `user.name` and folder path say (settling where the string came from) and points out the name in his SPEC is his to correct. The wider question — whether anything checks a SPEC fact nobody sourced — is filed as its own capture [spec-facts-unsourced].

**How it surfaced, which is the part that should not be relied on.** It only came out because Claude drafted his email to the user, signed it off with the name from SPEC, and he saw the wrong name on something about to go out under his own. Nothing checked it. He also notes his session's spec-sync check had run and passed clean, and reads that check as testing whether SPEC agrees with what was built rather than whether what is in it was ever true — which matches what the check does.

**The user's addition, 2026-08-30, and it is why this is filed with a flag rather than as a tidy-up:** the shortened form is plausibly **a colleague's name**. At his workplace two people are told apart by exactly that pair, the full form for one and the short form for the other. If that is the source, setup did not shorten his name — it took **a different person's** name from somewhere on that machine and wrote it into a document his project commits. That is the exact class the scrub checklist exists to keep out: a personal name belonging to someone not in the room.

**Names deliberately absent from this entry, on the user's instruction 2026-08-30**, along with any relationship between her and the tester: he is a beta tester and this repository is public. The finding survives intact without them — what matters is that a name was inferred rather than asked for, and that the inferred string may belong to someone else.

**Unverified, and it decides the fix.** Where the string actually came from is not known from here — git `user.name`, a folder path, an account name, or something else. Nobody here can read his machine, and the answer changes whether this is a setup step to remove, an inference to gate behind a question, or a prompt to fix. **Do not treat the git-config theory as established**; it is his reading and the user's, not a measurement. The cheapest route to certainty is asking him what his git `user.name` and folder path say.

**Two things worth separating at processing.** Whether setup should ever infer a name at all — the interview asks five questions and could ask a sixth — and whether anything *checks* a fact in SPEC that was never sourced from the user, which is the more general hole and the one his spec-check observation points at. Same shape as [setup-asks-if-first-time]: setup assuming something about the person rather than asking.

Test data from the first beginner tester; the full session record and its nine observations are processed with [beta-test-session-records].

#### Per-turn content lines at the named turns of /plan and /next — each decision turn says what it carries and nothing else [per-turn-content-rules]
**The naming-of-turns proposal is the user's own, raised 2026-08-30 in the Chagora session and restated independently by AFK-cats' session the same day** — the inbound reports carried it anonymised as "their user", and she confirmed authorship here 2026-08-31. Processed 2026-08-31, kept on her agreement. The evidence base is five captures filed within two days, each a distinct failure of "lead with the decision" as a bare principle: bundled analysis ahead of the ask ("the process is unbearable"), a summary made entirely of back-references, options offered that failed the user's already-stated situation, walkthrough steps restating reasoning agreed minutes earlier, and plain-language effort spread evenly instead of concentrated at decisions. The diagnosis shared by all five: `[BRIEF]`/`[DISCUSS]`/`[SEQUENCE]` govern how many messages and how long, but nothing governs what belongs in a specific turn — a content-selection failure, not a length one.

**The build.** Each named decision-moment turn in the shipped docs gains one operative line stating what the turn carries and nothing else:
- the item-opening **summary** (plan.md, present-and-interview) — **settled turn by turn with the user, 2026-08-31:** names its subjects outright — no referring expressions resolvable only from the conversation — and names who raised the item where that is anyone other than the project owner. **No length figure, on her ruling:** a sentence cap is a bare number however it is derived, and summaries are already the method's least-verbose artifact. **No nothing-else prohibition either, her ruling:** a ban on extra material is speculative until a summary actually fails that way, and would be a prohibition where the wording rule wants stated actions — added later, phrased positively, only on a recorded failure;
- the **recommendation** turn (plan.md, recommend) — **settled with the user, 2026-08-31, wherever it appears, own turn or merged:** carries what would change plus the ask; reasoning, findings and alternatives arrive on request; an option is offered where the question is genuinely open and accounts for what the user has already said this session. **Two findability additions, hers:** the recommendation's first sentence is bold, and the ask is one fixed formula every time — "Do [the recommendation]?" or as near as grammar allows — replacing the varied ask phrasings, so she is never hunting for where the recommendation is or deciphering what the ask means. **And the turn covers ONE decidable part, added 2026-08-31 on her instruction after a third same-day instance of bulk clearing:** the test is whether the user could plausibly agree to one part and reject another — if so, it is that many decisions, each getting its own recommend-and-wait turn; a composite may be summarised in one message for orientation, but the ask at its end covers exactly the first part, never the set. The three instances, all 2026-08-31: four turn designs put as one item and reopened on her correction; a cycle's criteria repointed "to the checklist" whole; a four-lens criteria design about to be walked the same way. This amends the recommendation turn's what-would-change line and is the operative statement of "what counts as one item" that `[SEQUENCE]` lacked. **And the ask's wording never assigns authorship — added 2026-08-31 on her catch of a live instance:** an ask framed "shall I write this in as your hypothesis?" forces the origin claim whatever the answer, since any yes — even "as you recommend" — records the user as author of reasoning that was Claude's. The ask names the act alone; who authored which part is settled by the provenance rules' containment test and written into the item as mixed where it is mixed, never by the ask's framing. The instance: the user's guess (recorded states become unnecessary under MCP) was Claude's to analyse into a two-kinds split, and the ask offered to file guess and split together as "your hypothesis";
- a **walkthrough step** (next.md, walk-through lifecycle) — **settled with the user, 2026-08-31:** where a step's reasoning is already agreed and on the record, the step is the ask alone — what to do and what to look for, in the standard ask shape; full reasoning appears only for something not yet agreed. **Her wording ruling, binding on the build: exactly that, with no session-qualifying clause** — "whichever session agreed it" was chat emphasis and must not land in the shipped text;
- the **checkpoint** (plan.md, checkpoint) — **settled with the user, 2026-08-31:** the existing four-part shape is untouched and no fifth part is invented; the one addition is that **the pointer states the item's filed date when the order in play ranks by age** — the long-and-old and alternating rungs — and says nothing about age otherwise. The date is read from the digest's First seen field, which satisfies the derived-time rule ([no-underived-time-statements]). Her ruling on placement: age belongs here, at the pointer, not in the summary where it was first proposed;
- `skill-nonspecific-rules.md`'s Communication message-shape bullet points at the per-turn lines as the governing specification at those sites.

**Files:** `plugin/throughliner/docs/plan.md`, `plugin/throughliner/docs/next.md`, `plugin/throughliner/docs/skill-nonspecific-rules.md`.
**Rests on:** the four turns named here existing in the shipped docs as described — verified against the installed 1.21.1-test3 docset, 2026-08-31; and the five reported instances, which are reports rather than measurements this project made, the two inbound ones dated 2026-08-30 and 2026-08-31.
Observable: each named turn's doc section carries its content line; a grep finds the lead-with-the-decision restatements at those sites replaced by pointers, not joined by them.
Rule gate: run at the decision step — each line is an amendment to the turn description it sits in (parents exist at every site); eviction is the replacement of the general principle's restatements at those sites; four-sentence bound derived from a recorded instance, not invented. The build transcribes this disposition.

Evidence merged from the sibling captures as they process: [summary-turn-resolvability-and-length], [verbosity-pointless-options], [walkthrough-step-restates-agreed-reasoning], [plain-language-concentrates-at-decisions] — each folds to one evidence line here at its turn and is deleted.

#### Time statements only where derived from fact — the date rule widened to every relative-time expression, chat included [no-underived-time-statements]
**Your rule, ordered 2026-08-31**, after catching a live instance in this session: "twenty minutes earlier" said of reasoning actually agreed in a different session. Your report: multiple times per session over the last week, on both Fable and Opus 5 — "this morning" for the start of a session, "tonight" for its end, thrown in for no reason. The worst offenders are the ones asserting what day it was — "yesterday", "tomorrow" — because those skew the log: an invented relative date written into a record reads exactly like a derived one, forever.

**The build transcribes this disposition:** `plugin/throughliner/docs/skill-nonspecific-rules.md`'s date paragraph (Research and evidence filing, "Where the answer is a date, read a computed field") is widened from date decisions to **every time expression, in chat and in anything written**: a statement of when something happened or will happen — a date, "yesterday", "this morning", "N minutes ago" — appears only where it is derived from a computed field, a timestamp, or the record, and otherwise the event is stated without a time ("agreed earlier", "in a previous session, per its record"). Same paragraph, widened scope; no second rule.

**Files:** `plugin/throughliner/docs/skill-nonspecific-rules.md`.
Observable: the date paragraph carries the widened scope; a grep finds one time-expression rule, not two.
Rule gate: run at the decision step — an amendment to the existing computed-date rule, its named parent; the widening replaces nothing else and admits no freestanding rule. Recorded instances: this session's live catch, and your report of repeated occurrences across the week on both models.

#### Walk-through outcomes restated — done, deferred, not reached, or what actually happened in one plain sentence [walkthrough-outcomes-miss-halted-and-partly-walked]
Found at the close of 2026-08-30's /next run, which met both gaps in one session. Filed by Claude. **Processed 2026-08-31, the restatement agreed on Claude's recommendation and the user's yes — no fourth or fifth value, per this item's own warning below.** The build: next.md's outcome-values provision (the definition's home, ~line 623) is restated to *done, deferred, not reached — or, where none fits, what actually happened in one plain sentence, with the item's own record carrying the detail*. That widens the rule instead of adding boxes, and legitimises what the 2026-08-30 close already did off-book, which both instances show was right. The grep-derived file list: `plugin/throughliner/docs/next.md` owns the definition; `plugin/throughliner/docs/done.md` and `plugin/throughliner/docs/skill-nonspecific-rules.md` also carry "not reached" and are repointed only where they duplicate the list rather than cite it. Observable: next.md's provision carries the fourth arm; a grep for "not reached" finds the value list stated once and cited elsewhere.
Rule gate: run — an amendment restating next.md's outcome-values provision, its named parent; the recorded instances are the halted re-homing and the partly-walked nerds entry, both 2026-08-30; the restatement was chosen over an exception per the restatement test, and no slot is spent.

**The three values are done, deferred and not reached**, each carefully defined: `deferred` only from the user's own word, `not reached` meaning never presented or presented with no answer. Two of this run's items fit none of them.

**Halted on a defect.** The how-to re-homing was presented and driven, step 2 was answered, six posts went out, and the user stopped the drive because the item's own walkthrough was wrong — it said to post into the existing topic when re-homing needs a new one. She answered throughout, so `not reached` is false. She never said to leave it, so `deferred` is false. It is plainly not `done`. What actually happened is that the item was found unbuildable as written and stops for redesign.

**Partly walked, with the remainder the user's.** The nerds-channel entry was driven to the end of Claude's part — drafted, posted with its zip, read back, registered — and its final step is hers alone. Not `done`; obviously reached; not deferred.

**Why this is not cosmetic.** The values exist to tell the next session what to do: `not reached` says present it fresh, `deferred` says honour a decision, `done` says close it. A halted item needs *neither* presenting fresh nor honouring — it needs re-planning, and recording it as `not reached` would send the next run to drive a walkthrough already known to be wrong. A partly-walked item needs resuming after its recorded steps, which the lifecycle already supports by reading the item's LOG record — but no outcome value says so.

**Weigh an amendment before a new value.** The lifecycle already has the machinery: a walk-through opens the item's LOG entry and appends as it goes, and resuming reads that record. So the gap may be that the three values describe *the run's* relationship to the item while the record describes the item's own state, and the fix could be to say so rather than to add values. **A fourth and fifth value is the obvious move and the one most likely to be wrong** — every value added is another thing a close has to choose between correctly.

Both instances are in `LOG/2026-08-30-next-run-chat.md`, recorded there as fitting no value rather than forced into one.

#### Build ticks were written in the wrong form for all 22 items of one run — next.md's specimen corrected [build-ticks-omit-the-confirmed-form]
Found at the close of 2026-08-30's /next run, reading the working file back. Filed by Claude, about Claude. **Processed 2026-08-31, the eviction's first form agreed on Claude's recommendation and the user's yes:** next.md's progress-format block's specimen is corrected to show `— done, confirmed`, with one clause naming next-build.md's per-item completion step as the wording's home — the two copies then agree and one is marked as the citation. Pointing instead of showing lost: a run reads the progress block at the moment it writes the file, and a correct specimen costs nothing where a mid-run fetch is friction. Files: `plugin/throughliner/docs/next.md`. Observable: a grep finds `done, confirmed` in next.md's progress-format block. The tool-shaped version — the tick as a validated MCP call whose required field makes the wrong form impossible — is recorded on [mcp-server-standing-intent] as its structured-writes purpose, and does not hold this fix back.
Rule gate: run — an amendment correcting a format specimen against its normative statement in next-build.md, the named parent; the recorded instance is the 22-tick run of 2026-08-30; nothing freestanding admitted.

**The required form.** `next-build.md` has each tick read `done, confirmed` or `done, UNCONFIRMED: <what still needs running>`, and the close transcribes whichever it says into the item's LOG entry verbatim. Every tick in this run's working file reads plainly `— done`.

**Nothing is unconfirmed in substance.** Each item's observable was run at its tick — greps for the strings that should and should not appear, the hook suites, the digest against the live queue, the zip entry listing, the two Discord subcommands against the live server. So the omission cost no verification here.

**It is still not cosmetic, and the reason is one document away.** `done-plan.md`'s hold-back rule reads the confirmed field to decide whether dependent work may clear. A run that never writes the field gives that rule nothing to read, and the failure is silent: the entry looks complete, and the safety rule downstream quietly has no input. The close doc calls the announcement of unconfirmed items required rather than left to judgment for exactly this reason.

**The likely cause is worth recording because it predicts recurrence.** The tick format appears in two places — `next.md`'s progress-format block shows `- [x] item description — done`, and `next-build.md`'s per-item completion step carries the confirmed/UNCONFIRMED wording. This run read the first and followed it. Two statements of one format, one of them incomplete, is the near-duplicate-rules problem the gate exists to prevent, arriving in a format rather than in a rule.

**So the candidate fix is an eviction rather than an addition**: make `next.md`'s progress-format block show the confirmed form, or point at `next-build.md` instead of showing a competing shape. That is the processing turn's call, and the alternative — treating this as a one-off discipline slip and writing nothing — is defensible if the format block is judged clear enough in context.

#### Hook-touching runs are permitted the testing suites — the class fix for observation files stopping the run [observation-files-named-by-folder-stop-the-run]
Found live 2026-08-30, twice in one run. Filed by Claude. **Processed 2026-08-31, the class fix agreed on Claude's recommendation and the user's deferral to it:** a run whose agreed file list includes `plugin/throughliner/hooks/` is automatically permitted `workshop/resources/testing/` (and its pre-move path `resources/testing/`) — bounded to exactly that pairing. The ground: the close cannot commit a hook change until the suites pass, so a hook-touching run always meets its suites, and the refusal was guarding files the rules already make part of every such change. Files: `plugin/throughliner/hooks/pre_tool_use.py`, plus the scope-lock's own suite files under `workshop/resources/testing/` (the build derives the exact paths from the suites that test the lock — which this run may touch by this very rule once it ships, and until then names them in its working file). Observable: the suites pass, including a new case where a fixture run listing a hook writes a suite file and is permitted, and a case where a run listing no hook is still refused.
**The decision step's paths-not-folders tightening is deliberately NOT part of this item** — one clause on a different doc, weighed separately at its own turn; the folder-expansion alternative stays rejected as recorded below.
Rule gate: run — an amendment to the scope-lock's permitted-paths behaviour, its named parent being the hook-suite close requirement whose logic it completes; recorded instances are the two refusals of 2026-08-30; nothing freestanding admitted.

**What the decision step already requires.** A kept item names the observation that shows the change landed **and the files that observation reaches**, among the files that change — precisely so a build derives a complete file list and does not meet the observation's files only when the safety check refuses them. The stated reason: stopping to ask is the one thing a run nobody is watching should not need to do.

**What two items actually said.** "the lint's suite under `workshop/resources/testing/`" and "the digest suite under `workshop/resources/testing/`". A folder, not a file. Self-scoping listed the three suite files that could be named from the items' own text, and the run then met two others — `hook_schema_check.py`, whose fixture asserted the old `workshop/resources/retired-terms.md`, and `test_plan_quiet_list.py`, whose fixture asserted the old research path. Both refusals were correct; both cost an interruption and a scope-widening ask.

**The requirement was met in letter and missed in effect**, which is the interesting part. The items did name where the observation reaches. A folder is not a path a `Files:` list can carry, so the build could not derive the entries, and the guard fired exactly as designed on files the user had already agreed in substance.

**Candidate fixes, none chosen.** State at the decision step that an observation's files are named as **paths**, not folders — a one-clause tightening of a rule that already exists. Or accept folder-level naming and have self-scoping expand a named folder into its files, which is more machinery and quietly widens what a run may write. The first looks right and the second is written down so it is not re-invented.

**A third framing worth weighing before either:** these were suite files, and a run that touches a hook is *always* going to touch its suites, because the close cannot commit until they pass. That may be an argument for the suites being permitted to a run that changes a hook, rather than for better item authoring — which would fix the class instead of one instance.

#### Unbracketed `Blocked by:` slug makes an item permanently unliftable — two guards on one defect [unbracketed-blocker-invisible]
Filed 2026-08-31 from INBOX mail sent by Chagora, running 1.21.1-test2 (archived at `INBOX/archive/2026-08-31-from-chagora-unbracketed-blocker-invisible.md`). A defect report; no reply owed. **Processed 2026-08-31, the two-guard fix agreed on Claude's recommendation and the user's deferral to it.**

**The build.** The digest treats any `Blocked by:` line whose named blocker resolves to nothing — unparsed brackets included — as a placement contradiction, printed in the existing contradictions block (the sender's own suggestion); and the lint's mid-line marker guard gains the unbracketed-slug flag, catching the form at write time. **Files:** `plugin/throughliner/scripts/queue_digest.py`, `plugin/throughliner/hooks/post_tool_use.py`, and their suites under `workshop/resources/testing/` — suite paths derived by the build, permitted to it by the hook-suites class rule ([observation-files-named-by-folder-stop-the-run]). Observable: the sender's four-item repro rebuilt as a fixture — the `Blocked by: bravo` item prints as a contradiction and the lint flags its line; the suites pass.

**The count-only narration finding is deliberately not in this item** — same subject as [queue-lint-narrates-on-every-bash], where it merges at that capture's turn.

Reproduced by the sender under control: a four-item scratch queue where one held item carried `Blocked by: bravo` and another `Blocked by: [bravo]`. The digest resolves the bracketed one and prints nothing at all for the unbracketed one, so it reads as unheld. The item stays below the readiness line, so it is never built — and the below-the-line revisit works by reading what each held item names, so an item naming nothing has no arm of the revisit table at all: not lifted, not surfaced, not flagged. Silent and permanent, and the longer it sits the more it looks like deliberate deferral rather than a typo. Caught by eye in their project, not by tooling.

Their suggested shape, offered rather than assumed correct: treat a `Blocked by:` line whose slug resolves to nothing — including because it was never parsed — as a placement contradiction the digest already prints, rather than as no blocker.

**A second finding underneath it, and it reaches this project too:** the lint's hook output reports a flag count and whether the flags were already present in the last commit, never which flags they are. Where every flag has been "already present" for several sessions, a session sees the same count at every tool call, can act on none of them, and cannot tell whether a new class of problem has joined them — a pre-existing flag is invisible in exactly the way an absent one is. This project currently reads "18 flag(s), all already present" at every call, so the condition is live here. Candidate: have the lint name its flags, or at least the distinct kinds.

#### Queue lint speaks only when the flag set changes, and names the change — count-only narration retired [queue-lint-narrates-on-every-bash]
Found live 2026-08-29 in the OpenCode-port goal session: the advisory line "5 flag(s), all of them already present in the last commit and none introduced by this change" arrived after every Bash command in the session — `git show`, `ls`, hash computations — none of which touched QUEUE.md. The lint's job is flagging format drift after a QUEUE.md edit; a line repeated after unrelated commands is noise that trains the reader to skim, which is the cry-wolf shape this project has repealed measures for. Filed under the rule that any observation of the plugin's behaviour is a testing outcome.

**Processed 2026-08-31, one emission rule agreed on Claude's recommendation and the user's deferral to it, merging Chagora's count-only finding (2026-08-31 mail, archived) as the second recorded instance:** the count is all the line ever says, so a standing set of old flags hides any new kind joining it — a pre-existing flag is invisible in exactly the way an absent one is, and this project's own session watched the count creep 20 → 27 with the wording never changing. **The build:** `plugin/throughliner/hooks/post_tool_use.py` emits only when the current flag set differs from the last commit's — a new flag appears, or one clears — and names the changed flags rather than counting; an unchanged set emits nothing, so silence carries the meaning the constant line pretended to. Statelessly computable against the committed file. The full listing stays available by running the lint script directly. **Files:** `plugin/throughliner/hooks/post_tool_use.py`, plus its suites under `workshop/resources/testing/` (permitted via [observation-files-named-by-folder-stop-the-run]'s class rule). Observable: a fixture where an unchanged set emits nothing and a new flag emits its name; the suites pass.

#### Scope-lock permits the harness's plan-mode plans directory, the way the scratchpad is permitted [scope-lock-blocks-harness-plan-file]
Found live 2026-08-29 in the OpenCode-port goal session. Plan mode is a harness feature: it designates one file under `~/.claude/plans/` as the only file the session may edit, and ExitPlanMode reads the plan from it. `pre_tool_use.py`'s planning branch refused the Write — the path is outside the standing list and the scratchpad test — so the session had to write the plan to the scratchpad and copy it across with a shell `cp`, which is a workaround the hook cannot see, worse than either rule alone. The hook predates plan-mode plan files. Filed under the rule that any observation of the plugin's behaviour is a testing outcome.

**Processed 2026-08-31, the capture's own candidate agreed on Claude's recommendation and the user's deferral to it:** permit the harness's plans directory the way the scratchpad is permitted, on the same ground — outside the repository, so nothing the scope-lock protects lives there. **Files:** `plugin/throughliner/hooks/pre_tool_use.py`, plus its suites under `workshop/resources/testing/` (permitted via [observation-files-named-by-folder-stop-the-run]'s class rule). Observable: a suite case where a write under the plans directory passes in a planning fixture while repository writes stay refused; the suites pass.
**Rests on:** the plans directory's location as observed live 2026-08-29 — a harness fact that can move with versions, so the build resolves the actual path where the harness exposes it rather than hard-coding the observed one.

#### `Cycle:` field ships without appearing in the capture line format [cycle-field-missing-from-line-format]
Noticed by /next on 2026-08-30 while building [cycle-material-captures-still-ranked], and captured rather than folded in: that item's file list names plan.md, the digest, the lint and CYCLES.md, and this is a fifth site it does not reach.

The field is now read in three places — plan.md's third pass-over arm, the queue digest's parse-and-print, and the lint's mid-line marker guard — and SPEC already describes it as product truth. What no shipped document does is show it. `docs/skill-nonspecific-rules.md`'s Captures section carries the fenced line-format block that enumerates every field an entry may take (`Red flag · State:`, `Runs alone`, `Blocked by:`, `Not before:`), and `Cycle:` is absent from it.

That block is where a session learns the shape it is meant to write, so a field readable by three tools and shown by none is one nothing will ever produce unprompted. It is the write-path-with-no-read-path failure the research-index rule names, running in the other direction.

The fix is small and is an amendment to that block rather than a new rule: one line in the fence with the same one-clause gloss its siblings carry, saying the entry is a named cycle's material and the planning ladder passes over it. Whether the two-meanings-per-section treatment the `Blocked by:` and `Not before:` prose gets is also owed is the processing turn's question — `Cycle:` currently has meaning on a capture only.

**Processed 2026-08-31, agreed on Claude's recommendation and the user's deferral to it:** the one-line amendment as described above, with the open question answered in the gloss itself — the field is capture-only, so the gloss says so and no dual-meaning prose is written. **Files:** `plugin/throughliner/docs/skill-nonspecific-rules.md`. Observable: the line-format fence shows `Cycle: [slug]` beside its siblings with the one-clause gloss; a grep finds it.
Rule gate: run — an amendment to the Captures line-format block, its named parent; the recorded instance is the field shipping readable by three tools and shown by none; nothing freestanding admitted.

#### Held item that is itself the only verification of what holds it — a deadlock the queue cannot see [held-item-is-its-own-verification]
Filed 2026-08-30 from INBOX mail sent by AFK-cats, running 1.21.1-test2 (archived at `INBOX/archive/2026-08-30-from-afk-cats-circular-hold-deadlock.md`). A defect report; no reply owed.

The shape: the hold-back-unverified-work rule held a `[user]` walkthrough below the line against a built-but-unconfirmed script — and the only thing in existence that can confirm that script is a step inside the held walkthrough itself. The blocker cannot resolve until the held item runs; the held item cannot run until the blocker resolves. The general form: a build produces a script, deploy or migration whose first real run happens inside a walkthrough that depends on it — not rare.

Two mechanisms both report it as fine, by construction: the digest shows the blocker as absent-and-built (reads as resolved), and the loop check covers only blockers that are queue items — this loop runs through a verification, which is not one. It surfaced only because someone read the record behind the slug by hand.

The sender's own resolution, worth weighing as the fix's shape: the hold was dropped knowingly, with the reasoning written into the item — the item IS the verification, and a walkthrough is driven live with the user present, so a failure is seen as it happens. Checked against 1.21.1-test2: the rule carries no exception for this case, so it is not already fixed. For processing: a candidate exception to the hold-back rule (done-plan.md) for a dependent that is itself the verification — the restatement test applies, and the sender's instance is the recorded evidence an exception requires.

**Processed 2026-08-31, the exception admitted on Claude's recommendation and the user's deferral to it — the restatement test was run and the restatement lost content:** rewording the rule to hold only unattended work would also clear attended walkthroughs that do not verify their foundation, a hold the rule genuinely wants, so the narrow exception is the honest form and the sender's deadlock is the recorded instance it requires. **The build:** the hold-back rule in `plugin/throughliner/docs/done-plan.md` gains the clause that where the held item is itself the only verification of its blocker, the hold is not written — the item clears, its walkthrough is the verification, and its prose says so. **Files:** `plugin/throughliner/docs/done-plan.md` alone; plan.md's referencing site cites rather than restates and is untouched. Observable: the rule carries the clause; a grep finds it stated once.
Rule gate: run — an exception to the hold-back-unverified-work rule, its named parent; restatement attempted and lost content; recorded instance the AFK-cats deadlock of 2026-08-31, cited in the close's record per the gate's exception provision.

#### Nothing bars relocating an unpresented item's content ahead of that item's turn [unpresented-item-content-relocated-early]
Reported by the Chagora project through this project's INBOX, 2026-08-30, from a live instance in its own planning session caught by its user rather than by any rule. Filed here by /next; not yet processed.

**What happened there.** While processing one item, Claude wrote the settled answer into the item it belonged to and, in the same edit, also wrote in the content of the *next* unprocessed item, which had not yet been presented. When that item came up at the checkpoint it was offered as "a one-line confirmation rather than a discussion", the user agreed, and Claude executed. Their correction: "you didn't make a recommendation."

**Two failures, kept apart in the report and worth keeping apart here.** The first is Claude's own and needs no rule: the shipped procedure already says a timing answer is not a disposition, and that a checkpoint's "continue" answers which item comes next rather than that item's fate. Following either would have caught it. The second is the gap the report is actually about — nothing in `plan.md` bars relocating a not-yet-presented item's content ahead of its turn, and once the content is already written somewhere else the only honest thing left to offer at its turn is a confirmation, so the recommend-and-wait turn has nowhere to stand. The two compound: the missing rule manufactures exactly the situation in which the existing rule is easiest to skip.

**The suggested fix, as sent, narrow:** content belonging to an unpresented item is not relocated ahead of that item's turn. Whether that earns a rule at all is this capture's own processing question — it would be an amendment to plan.md's one-at-a-time pass, and the rule gate runs on it there rather than here.

Sent as a defect report; no reply owed.

**Processed 2026-08-31, the amendment agreed on Claude's recommendation and the user's deferral to it, stated as the action rather than the bar:** content belonging to a not-yet-presented entry is carried to that entry's own turn and written then. The first half of the report earns nothing — the timing-answer and disposition-cannot-fold rules existed and were not followed, which no new rule fixes. **Files:** `plugin/throughliner/docs/plan.md` (the one-at-a-time processing pass). Observable: the pass carries the clause; a grep finds it stated once.
Rule gate: run — an amendment to plan.md's one-at-a-time pass, its named parent; the recorded instance is Chagora's 2026-08-30 session, caught by its user; the second reported failure deliberately earns no rule, existing rules covering it unfollowed.

#### Bare `/plan` fails before any rule is loaded, so the retype workaround can never fire [bare-command-name-fails-before-rules-load]
**Captured by you, 2026-08-30**, with a screenshot from a planning session in another of your projects. Second recorded instance — the workaround designed for the first one does not work, which is what this capture is for.

**What happened.** The user typed `/plan`. Claude Code answered `/plan isn't available in this environment.` They then typed `/throughliner:plan`, which ran. The plugin's skills are namespaced, so the bare name resolves to nothing.

**Why the existing workaround cannot reach it — your diagnosis, and it is the load-bearing part.** `docs/skill-nonspecific-rules.md` already carries the arm: where a command the user typed arrived as ordinary chat text, say it likely had not registered yet and ask them to type it again. That rule is in the always-loaded file, and the always-loaded file is read by the session — but this failure happens at the session's very first message, before anything has read it, and the refusal comes from Claude Code itself rather than from a turn Claude is composing. There is no turn in which the rule could fire. A behavioural rule is the wrong instrument for a failure that precedes behaviour.

**Second problem in the same place, worth processing together.** That same rules file instructs Claude to name the commands as `/setup`, `/plan`, `/next`, `/rescan`, `/done` — the bare forms, which are exactly the ones that fail on a namespaced install. So the method's own text teaches the user to type the string that does not work.

**The fix you name: the session_start hook.** It is the one thing that speaks before anything else in the session and is not a rule anyone has to have read. Open questions for the processing turn: whether it prints the qualified names unconditionally or only where it can tell the bare form will fail; whether it can tell that at all; and whether the always-loaded rule's command names should change with it, which is a shipped-wording change reaching every consumer.

**Not verified from here:** why the bare form resolves in this project and not in that one, or whether it is a Claude Code behaviour that differs by how the plugin was installed. That is a read someone has to do rather than a thing to reason out — worth settling before the fix is designed, since it decides whether the hook can detect the case or must always print the long form.

**Processed 2026-08-31, the unconditional design agreed on Claude's recommendation and the user's deferral to it — it sidesteps the unverified fact rather than waiting on it:** `session_start.py`'s ready line names the commands in their qualified form (`/throughliner:plan` and siblings), correct in every project including where bare forms work; and the always-loaded workaround arm gains the second suggestion, retyping an unrecognised command with the plugin's name in front. The why stays unverified and this fix does not depend on it; it matters again only if the qualified form ever fails too. **Files:** `plugin/throughliner/hooks/session_start.py`, `plugin/throughliner/docs/skill-nonspecific-rules.md`, plus the session-start suites under `workshop/resources/testing/` (the class rule permits them). Observable: the hook's ready output carries the qualified names, the rules' arm names the qualified retry, and the suites pass.
Rule gate: run — an amendment to the command-arrived-as-text workaround arm, its named parent; recorded instances are the two failures in the user's other project, the second with a screenshot; the hook change is behaviour, not a rule, and spends nothing.

#### Walkthrough steps carry at most three actions — the working-memory range's low end, your call [walkthrough-steps-two-actions-max]
**Your rule, asked for 2026-08-31** with the recorded instance attached: a walkthrough step from another session bundling six actions — open a new PowerShell window, run a quoted command, type the login command, drive a keyboard-only menu, authorise in a browser, close the window — before any look-for. Your words: "This is impossible to follow."

**The build transcribes this disposition:** the walkthrough-authoring requirements in `plugin/throughliner/docs/skill-nonspecific-rules.md` (the bullet list under the `[user]` item rules, whose parent line already says each step names the thing to click or type and the thing to look for) gain the provision that a step carries **at most three instructions — where a check or verification counts as an instruction exactly as an action does** (your refinement, 2026-08-31: confirming something happened in a smoke test counts, not just typing the command) — with anything more split into further steps each carrying its own look-for. **The figure's derivation, supplied by you 2026-08-31 in place of the earlier bare declaration:** working-memory research puts instruction-following at 3–5 steps before people forget details or make mistakes, and you chose the very low end of that range — a figure from research with the low-end choice yours, which is the derivation kind the method admits. The slug keeps its original wording per the stable-slug rule.

**Files:** `plugin/throughliner/docs/skill-nonspecific-rules.md`.
Observable: the walkthrough requirements carry the two-action provision with its stated derivation; a grep finds it stated once.
Existing queued walkthroughs are re-cut to the ceiling as they are driven or at the maintenance sweep, not in a bulk pass — refused as a sweep now because the rule governs authoring and a bulk rewrite of approved walkthroughs would churn items nobody is about to drive.
Rule gate: run — an amendment to the walkthrough-authoring requirements, their named parent; the recorded instance is the screenshotted six-action step of 2026-08-31; the limit states its derivation; nothing freestanding admitted.

#### Open questions file a capture: a want set aside, a rejection repealed, a door left open in prose routes to the queue [open-question-files-a-capture]
**Named by you, 2026-08-31**, from a live instance: your maintenance-cycle intention, raised across many sessions, lost a design round to independent checks; the rejection was later repealed with "a later session may re-propose a cycle on its merits" written into the project instructions — and no capture was ever filed, so the intention's only storage was your head and it resurfaced only because you asked. Your naming of the failure: Claude not recording a named intended thing on account of it being blocked, on the basis that it exists in the human's head and they can name it again.

**The build transcribes this disposition:** `plugin/throughliner/docs/skill-nonspecific-rules.md`'s routing rule ("Nothing unrouted survives a chat") gains one arm — a question deliberately left open is routed as a capture at the moment it is left open, credited to whoever wants it: a user-named want set aside for a winning alternative, a rejection repealed, a resolution ending in "may be re-proposed later". The capture may carry `Not before:` or `Blocked by:` under their existing provisions; what it may not do is exist only as prose in a record or a rules file, which is read on demand while the queue returns things by itself.

**Files:** `plugin/throughliner/docs/skill-nonspecific-rules.md`.
Observable: the routing rule carries the open-question arm; a grep finds it stated once.
**Rests on:** the routing rule existing as described — verified against the installed 1.21.1-test3 docset, 2026-08-31.
Rule gate: run at the decision step — an amendment to the nothing-unrouted routing rule, its named parent; recorded instances are the maintenance cycle (this entry) and the MCP umbrella ([mcp-server-standing-intent]); nothing freestanding admitted.

#### Compliance-audit checklist gains the maintenance sweep's lenses, designed one by one [checklist-gains-sweep-lenses]
Filed 2026-08-31 while designing the [maintenance-sweep] cycle, whose criteria this checklist supplies. Each lens below was agreed in its own turn, per the one-decidable-part rule; the build transcribes them into `workshop/resources/method-compliance-audit-checklist.md` beside the four existing lenses.

**Lens: underived numbers — agreed 2026-08-31.** Grep the corpus for digits; read each hit that functions as a limit or threshold — a cap, a count, a depth, a cadence — and pass it only where the derivation is stated in the same or an adjacent sentence: a proportion of the thing governed, a figure from named research, or an externally imposed constraint. Dates, version numbers, message ids and worked examples are out of scope — they state facts, not limits. Each failure files one capture quoting the sentence and naming the file. The limit-or-threshold call is the lens's one reading step, stated as such.

**Lens: negatives — agreed 2026-08-31.** Grep the corpus for sentence-leading prohibition forms — "Never", "Do not", "Don't", "No <x> may" — and read each hit for whether the action wanted is stated anywhere in the same provision. A prohibition whose positive action exists beside it passes; one standing alone files a capture quoting it. The lens states its coverage limit as the restyle passes recorded it: sentence-leading forms only, with mid-sentence prohibitions (~151 at the 2026-08-21 count, most legitimate) unread — so a turn says what it covered rather than implying the corpus is clean.

**Lens: contradictions — agreed 2026-08-31, one lens with two stated steps.** Parent–child: for every subordinated unit — a nested bullet, an amendment naming its parent — read it against the parent's opening words and file a capture where the child is quietly wider or narrower than the rule it amends, or reads as a complete freestanding sentence (the gate's subordination test applied after the fact). In-document: within each file, read provisions sharing a subject — found by grepping the file for repeated key nouns — and file a capture where two command different things for the same case. Stated limit: the second step reaches provisions sharing vocabulary; two contradicting rules phrased with no common noun stay unread, the same limit the retrieve ladder documents for searches.

**Lens: duplication — agreed 2026-08-31.** Covers what the mechanical near-duplicate matcher cannot see: two passages doing one job at the same level. For each rule in the always-loaded files, ask which lower-level doc owns the same ground (the parent-axis method the 2026-08-22 style-dedup audits used), and file a capture where both state the rule rather than one stating and the other pointing. Within a single file, the merge rule's own test applies: two accounts of the same thing under different headings file as a merge candidate. Stated limit: the lens compares rules naming the same mechanism; a duplication paraphrased past shared vocabulary stays unread — the same residual the contradictions lens states.

**Files:** `workshop/resources/method-compliance-audit-checklist.md`.
Observable: the checklist carries each agreed lens with its test as written here; a grep finds the lens headings.
Rule gate: to run at this item's clearing — each lens is an amendment to the checklist's lens set; the checklist is in the gate's trigger file set, so the build's commit carries the disposition.

All four lenses were designed in their own turns and the cycle definition's criteria paragraph was repointed at the checklist the same day — nothing remains before the build.

#### Cycle and ritual definitions pass the kept-item test: no open class, no design decision scheduled into the turn [definitions-pass-the-buildability-test]
**Asked for by you, 2026-08-31**, from a live instance you caught: the [maintenance-sweep] cycle's criteria paragraph was authored as "whatever would fail the discipline" — an open class delegating the criteria-selection decision to the audit's own turn — and passed unchecked, because plan.md's design-decision clause runs on queue items at the decision step while a definition is written straight into the cycles doc by the same pen. Your framing of the general failure: two sessions given the text would not produce the same work list.

**The build transcribes this disposition:** plan.md's cycle-authoring step (and its ritual sibling) gains the clause that a definition's steps, criteria and observable pass the same test a kept item's instructions do — the design-decision clause applied at authoring: no open class, no decision scheduled into the turn, stated concretely enough that two sessions produce the same turn. Parent: the buildability check's "prose that schedules a design decision into the build fails" clause, extended to the definitions the same step authors.

**Files:** `plugin/throughliner/docs/plan.md`.
Observable: the cycle-authoring step carries the clause; a grep finds it once, and it names the parent clause rather than restating its test.
**Rests on:** the cycle-authoring step and the design-decision clause both existing in the installed 1.21.1-test3 plan.md — verified 2026-08-31.
Rule gate: run at the decision step — an amendment to the cycle-authoring step naming its parent; the recorded instance is the [maintenance-sweep] criteria paragraph, caught and repaired 2026-08-31; nothing freestanding admitted.

#### [audit] Recorded-states inventory: every true/false-shaped fact the docs store, classified computable or decision [recorded-states-inventory]
Filed 2026-08-31 while processing [mcp-server-standing-intent], whose purpose hypothesis this grounds: MCP retires the recorded copies of computable states and must not touch the decision trail — mixed authorship recorded on that item. An MCP design cannot be scoped until someone knows which recorded states exist and which side of the split each falls on, and that is answerable by reading.

The turn: sweep the shipped docs (`plugin/throughliner/docs/`), the templates, SPEC.md, CLAUDE.md and the queue's own field set for every state recorded as a true/false-shaped fact — version and epoch markers, content stamps, build ticks and their confirmed field, red-flag states, walk-through outcomes, `Blocked by:`/`Not before:` holds, register statuses like approved-not-posted, editing-state markers. Classify each as COMPUTABLE (derivable from an observable a tool could read live — and name the observable) or DECISION (a record of the user deciding, which no tool can compute). One finding per state, filed as captures to Unprocessed per the audit rule; where the table is worth re-reading whole, the durable copy goes to `workshop/resources/research/` with its index line.

Reads: the files named above. Edits nothing — an audit files findings only.
Observable: captures filed under this slug's findings, and the umbrella [mcp-server-standing-intent] lifts once this records complete.
Rests on: the two-kinds split as recorded on [mcp-server-standing-intent], 2026-08-31 — a classification frame, not an external fact.

#### [audit] Stop hook did not catch a reply claiming a capture was filed when it was not — reproduce, name the mechanism [stop-hook-missed-an-unfiled-claim]
Found live 2026-08-30 in a /next run. Filed by Claude, about Claude. **Processed 2026-08-31, kept as an [audit] on Claude's recommendation and the user's deferral to it:** the fix depends on the diagnosis, so the turn is the diagnosis — feed the recorded reply shape (a filing claim naming `[walkthrough-step-manufactures-an-ask]` in brackets, from `LOG/2026-08-30-next-run-chat.md`) through the hook's detection, read its pattern and its block-once-per-claim mechanics in `plugin/throughliner/hooks/stop.py`, and re-read `resources/testing/test_stop_hook.py`'s passing case against the live shape until one of the three candidate stories below is confirmed or all three are excluded. Reads those files; edits nothing; one finding capture per mechanism established, the fix filed as its own capture naming it.

**What happened.** A reply ended with "Filed as `[walkthrough-step-manufactures-an-ask]`, with the specific instance…". No write had been made — the slug never reached QUEUE.md. It surfaced only when the next turn tried to delete that entry in order to replace it, and the queue tool refused because no such entry existed.

**Why this is the stop hook's exact job.** The hook reads the finished response for a report naming a capture as filed and confirms the entry is in the queue, feeding the turn back where it is not. Its own description names the reason: a reply could report filing something the write never made, and the user would have no way to tell. Here the claim named its slug in brackets, which is the form the hook is documented to catch, and the turn completed.

**What is not known, and it decides the fix.** Whether the hook ran and failed to match, ran and matched but did not block, or did not run at all. Nobody has looked. The candidate explanations worth testing:
- the block-once-per-claim carve-out had already been spent earlier in this long session, so a later genuine miss passes;
- the response's phrasing did not match whatever pattern the hook uses to detect a filing claim;
- the slug appeared in a context the hook reads as a citation of existing work rather than a claim of a new filing — the hook deliberately does not block a slug that has a `LOG/` record or a tick in the run's working file.

**The user's exposure, stated plainly.** She was told a finding about her own method had been recorded. Had the next turn not happened to touch that slug, it would have been lost silently, and she would have believed it was in the queue. That is the precise failure the hook exists to prevent, so a miss here is worth more than the one lost capture.

**Reproduce before designing anything.** `workshop/resources/testing/test_stop_hook.py` exists and passes, including a case for "a claim with no heading and no record still blocks" — so the suite's model of this and today's live behaviour disagree. Settling which is right is the first step, and it may show the fault is in the suite's fixture rather than in the hook.

#### [user] Re-home the how-to forum posts under the bot's authorship [howto-posts-bot-authorship]
Filed 2026-08-27 with [posting-rule-two-kinds-and-tip-pipeline], from your instruction that the how-to topics be editable and maintainable by the bot. The constraint that makes this an item at all (recorded in `TOOLS.md`): a bot can only edit messages it authored itself, and the existing how-to posts are yours — so bot maintainability requires each one re-posted by the bot once, after which every later tweak is a bot edit under the approval rule.

**Walkthrough. Rewritten 2026-08-31 to the new-topic design**, merging in the deleted [howto-rehoming-needs-new-topics] after the 2026-08-30 drive was stopped by you mid-run: the bot had posted its copies as replies inside your topics, and in a forum the opening message IS the post, so the reply route would have left six hollow topics with the text underneath as a comment. All six bot replies were deleted and verified gone; your originals untouched; the register line was corrected the same turn. Two steps of the old design die with this rewrite, and why is recorded so they stay dead: the throwaway survive-the-delete test is moot because old topics are now deleted whole rather than having a message removed from inside them, and the what-about-your-other-messages step is moot because the 2026-08-30 type-check settled that every follow-up is an automatic rename or pin notice, which dies with its topic.
1. Claude fetches each of the six topics' opening text through the bot and shows it to you unchanged. Look for: the text matching what the forum shows.
2. On your yes per post, the bot creates a **new topic** in the how-to forum carrying the original's title and text byte-identical ([bot-cannot-create-forum-topics] built that ability). Posted in reverse title order — 6 first, 1 last — so under activity-sorting ([forum-order-is-by-latest-activity]) the list first reads 1 at the top; the numbered titles carry the reading order regardless. Look for: the new topic under the bot's name.
3. You delete each **old topic whole**: right-click (or long-press) the topic in the forum list, choose **Delete Post**, confirm. Only you can — the bot cannot delete your topics. Look for: the old topic gone from the forum list, the bot's new one remaining.
4. If any old topic was pinned, you pin the bot's replacement the same way you pinned the original. Nobody has checked whether pins carry any other way. Look for: the pin marker on the new topic.
5. The register lines re-point: Claude greps `INBOX/sent.md` for each old topic id and rewrites those lines to the new topic ids, channel named. Look for: a one-line report per line changed. This item closes when all six live topics are bot-authored and the grep finds no old id.
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
**Lifted 2026-08-28.** [beta-tester-pathway] shipped in the 2026-08-28 run and its tick is confirmed (`LOG/2026-08-28-beta-tester-pathway.md`): the announcement now exists as `workshop/resources/beta-offer-announcement-template.md`, the `beta` branch exists, and the record notes the tester install smoke test ran 2026-08-27 — which is step 2's condition, so that step is a confirmation rather than a wait.
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

#### [user] Post the 1.21.1-test1 entry to the nerds channel, with its archived zip [test-rezip-entry-1-21-1-test1]
**Your direction, 2026-08-29**, when you asked why the previous rezip had not been posted — it should have been, and the close missed the check. Folded to the next session on your instruction, with the zip back-filled first, which is done.

**Ready now, and both halves of the readiness test are confirmed rather than assumed:** a full planning session ran on 1.21.1-test1 (2026-08-29, confirmed from that session's own start block) and a full build run ran on it (2026-08-29). The archive holds its zip and readme, rebuilt from commit `4efdcff` and verified by content stamp `8c874952044d` — identical to the stamp proved equal when the build was installed, so the attached bytes are the tested bytes.

**Walkthrough.**
1. Draft the entry from `plugin/rezip-archive/throughliner-v1.21.1-test1.md`, whose text the archive and the channel post are required to share. Look for: the label, the `Commit:` line and the version matching the readme exactly.
2. The bot posts it to 💡test-rezips-for-nerds with the archived zip attached, on your explicit yes to the exact text:
   `py workshop/resources/discord_post.py send --channel test-rezips-for-nerds --body <draft> --attach-archived-zip 1.21.1-test1 --prune-to 15 --rebump-welcome workshop/resources/nerds-welcome.md`
   Look for: `Posted to #test-rezips-for-nerds — message id`, then a line saying the welcome was re-bumped.
3. Write the register line in `INBOX/sent.md` in that same turn, naming the channel and reading the claim off the posted text.
4. **Posting this entry unlocks editing the one before it** — the v1.21.0 post — to add a testing-outcomes summary and your rating out of 5. That entry is your own post rather than the bot's, so under the first-iteration note the backfill is yours to paste once.

Observable: the entry appears in the channel under the bot's name with the zip attached, and `INBOX/sent.md` carries its line.

**The practical block is gone, 2026-08-31:** [discord-script-permission-rule] was completed by the user and proved live the same day — a tip posted through the bot with no classifier block and no terminal — so this item's sends run terminal-free now.

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

**The example bank exists** — `workshop/resources/research/determinism-lesson-examples.md`, compiled at processing on your direction, covering all four quadrants with the good/bad call proposed on each and two claims flagged for re-verify at drafting. The bridge example in it is the lesson's strongest good-practice move: AI builds the deterministic tool once, then the tool runs free forever.

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

#### [user] Strip the Expert role to a member role: Administrator and the five manage-permissions come off [expert-role-holds-administrator]
From the Discord permissions audit of 2026-08-30; **processed 2026-08-30, the strip agreed on Claude's recommendation and the user's deferral to it.** Experts need to talk, post and be recognised, not reconfigure the server; anything they genuinely need is better granted per channel, where the existing setup already works. If someone is meant to help run the server, that is a separate admin role created deliberately, not a side effect of Expert.

**Walkthrough.** Only you can change role permissions.
1. In Discord: Server Settings → Roles → **Throughliner Expert** → Permissions tab. Look for: the permission toggles list.
2. Switch OFF: Administrator, Manage Channels, Manage Server, Manage Roles, Manage Webhooks, Manage Messages. Save. Look for: the green save bar appearing and clearing.
3. Tell this project; Claude re-runs `py workshop/resources/discord_post.py permissions` and confirms the role's grant no longer names any of the six. That read is the observable, and it checks exactly those six bits — nothing else about the server.
Red flag · State: cleared
**Cleared by design, 2026-08-30:** the fix is agreed and queued as this walkthrough — the over-grant is removed rather than accepted, and until step 3's read confirms it the risk is open work sitting visibly here, not a closed question.

**Observed.** `py workshop/resources/discord_post.py permissions` reports the `Throughliner Expert` role with a guild-level permission bitfield of `8864258447638527`, whose first named bit is `ADMINISTRATOR`, alongside `MANAGE_CHANNELS`, `MANAGE_GUILD`, `MANAGE_ROLES`, `MANAGE_WEBHOOKS` and `MANAGE_MESSAGES`.

**Why it matters.** This is the direct answer to the question that started this review on 2026-08-29 — how a member came to edit a forum's guidelines. Editing a forum's guidelines is a channel-settings change, gated by `MANAGE_CHANNELS`, and this role has it; it also has everything else, including renaming and deleting channels and managing roles.

**And the per-channel restrictions do not restrain it.** Discord documents `ADMINISTRATOR` as bypassing every channel permission overwrite. So the how-to forum's careful `@everyone` denial of `SEND_MESSAGES`, and its explicit narrow `Throughliner Expert allow: SEND_MESSAGES`, are both moot for anyone holding this role — the narrow grant reads as a restriction and is not one. **That bypass is Discord's documented behaviour and was not tested against this server**, which is the one claim here that a reader should not take as measured.

**Not a recommendation about what the role should hold** — that was the capture's original posture, before the strip above was agreed. What this paragraph records is that the role's actual grant is far wider than the record of what was intended.

#### [user] Take Mention @everyone out of the server's baseline role — grants become per-channel and deliberate [everyone-holds-mention-everyone]
From the Discord permissions audit of 2026-08-30; **processed 2026-08-31, the posture flip agreed on Claude's recommendation and the user's deferral to it.** The baseline `@everyone` role granted `MENTION_EVERYONE` server-wide, so safety was a hand-extended list of per-channel denials, and a new channel started silently pingable by any member. The flip inverts which mistake is possible: a forgotten grant is a nuisance someone complains about, where a forgotten denial was a server-wide ping nothing reports.

**Walkthrough.** Only you can change role permissions.
1. In Discord: Server Settings → Roles → Default Permissions (the `@everyone` baseline). Look for: the permission toggles list.
2. Switch OFF "Mention @everyone, here, and all roles". Save. Look for: the green save bar appearing and clearing.
3. Still in Discord: open `#🧬port-showcase` → Edit Channel → Permissions → the `@everyone` row. Set "Mention @everyone, here, and all roles" from allow back to neutral (the slash, not the X — the baseline now denies it). Save. **Merged 2026-08-31 from the deleted sibling [port-showcase-allows-mention-everyone]:** that forum was the one channel explicitly allowing the ping — the newest channel, departing from the posture every other one takes, which reads as a settings slip — and a channel allow overrides the baseline, so without this step it would be the one place members could still ping the server after step 2.
4. Tell this project; Claude re-runs `py workshop/resources/discord_post.py permissions` (from `workshop/bot/` after the repo cleanup moves it) and confirms `MENTION_EVERYONE` is gone from both the baseline bitfield and the port-showcase `@everyone` overwrite. That read is the observable, and it checks exactly those two places.

The existing per-channel denials become harmless redundancy and stay.

#### [user] Strip MANAGE_CHANNELS from the other project's bot role, matching the narrow shape this project's bot uses [second-bot-role-holds-manage-channels]
From the Discord permissions audit of 2026-08-30; **processed 2026-08-31, the strip agreed on Claude's recommendation and the user's deferral to it.** A role carrying another of your projects' names held `MANAGE_CHANNELS` at the guild level — rename, reconfigure and delete any channel, the announcements channel and both forums included — while its per-channel setup granted it exactly one view permission, the shape of an account meant to watch one channel, not manage the server. The contrast in the same audit output: this project's own bot holds sending powers at the base and gets everything else per channel. Two limits carried from the finding: the read reports what is granted, not what was used, and a role is not a person — who holds it is not reported.

**Walkthrough.** Only you can change role permissions.
1. In Discord: Server Settings → Roles → the role named for the other project → Permissions tab. Look for: the permission toggles list.
2. Switch OFF "Manage Channels". Save. Look for: the green save bar appearing and clearing.
3. Tell this project; Claude re-runs `py workshop/resources/discord_post.py permissions` and confirms that role's bitfield no longer names `MANAGE_CHANNELS`. That read is the observable, and it checks that one bit on that one role.

If that project's bot turns out to need channel management for something this audit could not see, say so at step 2 instead of toggling — the item then records your informed choice to keep the grant, which closes it just as well.

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

**The verification step runs BEFORE drafting, and is not optional.** `workshop/resources/research/auto-memory-staleness.md` is dated 2026-06-09 and names AutoDream as Anthropic's own consolidation sub-agent — two months old, and what the Discord means by "Obsidian memory systems" may be a specific community project rather than the general vault-as-memory pattern. **Publishing a wrong description of someone else's system under your name is worse than publishing nothing**, and unlike everything else this project writes, it is a claim about a third party. Search first, update the research file, then draft.

**Two artifacts, not one text, settled at capture.** The article is the full piece and may be long, may discuss competitors, and may say where Throughliner is weaker. The Discord post is capped at 2,000 characters, takes the shipped fix as its subject with the comparison only as framing, and points at the article. One text serving both would either saddle the announcement with a comparison it doesn't need or truncate the article into a changelog.

**The Discord post is this item's final step rather than a separate item — the user's decision.** Order: verify, draft the article, ship the digest work, finish the article with what actually shipped, then write the post. **Nothing is published without the user seeing the exact text and giving an explicit yes.** The Discord post goes through the bot on that yes (route corrected 2026-08-28); Claude genuinely has no route to the flintcraft.tech site, so the user publishes the article.

**One thing to resolve at drafting.** The site is another project, so the article is drafted here and delivered rather than written into that repository. Whether that delivery is an INBOX message or the user carrying it across is a question for the moment it is ready.

**The blocker has shipped and the `Blocked by:` line is dropped, 2026-08-15.** [digest-reports-computed-fields-not-summaries] has a LOG entry, so the digest work the article was waiting to describe now exists.

**Verification done 2026-08-15, in the /plan session that processed this — and it changed the argument rather than confirming it.** `workshop/resources/research/auto-memory-staleness.md` was re-checked and partly corrected; its index line carries the correction too. Two material findings:

- **AutoDream is live.** It consolidates memory between sessions — merging facts, deleting contradicted notes, converting relative dates to absolute, trimming the index — triggering automatically after roughly 24 hours plus five sessions, and **a manual `/dream` command is available to everyone** regardless of rollout state. The research file's claim that it is not running was two months stale. **This sharpens the weakness the draft already admits:** automatic curation is no longer something only competitors have, it is in the base tool this plugin runs on. An article treating manual curation as a fair trade must say so, and the honest framing is why typed documents and user-approved deletion are worth the manual cost — not that the alternative is unavailable.
- **"Obsidian memory systems" is a category, not a project.** Several independent implementations exist, some with semantic search, self-rewriting notes and scheduled maintenance agents, plus Obsidian's own official Agent Skills for Claude Code from January 2026. So the article names the specific project it compares against, or says plainly it is describing the general vault-as-memory pattern. Describing "the Obsidian memory system" as one thing is the wrong-about-a-third-party failure this item was right to guard against.

**Tagged `[user]` at processing 2026-08-15**, matching the other post items rather than inventing a shape: Claude drafts the article and the post, the user publishes both.

**The one-a-day pacing this paragraph used to defer to was repealed 2026-08-28** ([one-post-a-day-is-per-channel]) — the post goes out when it is ready, on your yes to the exact text, and the article can be drafted whenever.

**Walkthrough.** Authored 2026-08-22 at processing, closing [article-walkthrough-missing].
1. Claude re-checks the two 2026-08-15 findings still hold before drafting — AutoDream's status, and whether "Obsidian memory systems" now names a specific project — offering a fresh web search; anything changed is corrected in `workshop/resources/research/auto-memory-staleness.md` first. You'll see what the check found before the draft starts.
2. Claude drafts the full article: names the specific system it compares against or says plainly it describes the general vault-as-memory pattern, and is honest that automatic curation now ships in the base tool — the case made is why typed documents and user-approved deletion are worth the manual cost.
3. You read it and say what to change; repeat until you're satisfied.
4. You decide delivery: an INBOX message to the site project (you see the exact text first) or you carry the file across yourself. Claude does whichever you pick that it can.
5. Claude drafts the Discord post — under 2,000 characters, the shipped fix as its subject, pointing at the article.
6. You publish the article — Claude has no route to the site. The Discord post goes through the bot on your explicit yes to the exact text (route corrected 2026-08-28; pacing repealed the same day).
7. You confirm both are up; the send is recorded in `INBOX/sent.md` and this line closes.

**Held 2026-08-24 on your decision, made during this item's walk-through.** Drafting stalled because Claude didn't have enough how-Throughliner-works material to draw on, and the thinking fell to you. The announcement-driven FAQ shipped 2026-08-24 and fills as announcements are posted, so the material accumulates over time; `ANNOUNCEMENT-IDEAS.md` also now carries the retired FAQ's entries — exactly the material the drafting lacked. The recovered draft did not satisfy you, so this is a redraft when it resumes, not a patch. No single queue item completes as the blocker, so the hold is a date: when it passes, the lift judgment is whether the FAQ actually has enough on the relevant features — not automatic.
Not before: 2026-09-21

**Files:** none in this project — the artifacts are an article for the Throughliner site and a Discord post. Relates to [digest-reports-computed-fields-not-summaries] (shipped) and `workshop/resources/research/auto-memory-staleness.md` (verified and corrected). [comparison-article-post-needs-rewrite] follows this item — the post's rewrite runs against the final article, so it is held on this slug.

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

**Changes.** `workshop/resources/discord_post.py` — the existing `prune` subcommand reads its depth and its return-or-retire flag per channel instead of taking a fixed count, and where a channel returns, each pruned post is written back into QUEUE.md's Unprocessed as a capture carrying its original text, its original date and its message id. `CYCLES.md` — the per-channel settings live with the [tips-posting] definition, since the depth is derived from that cadence and belongs beside it.
Observable: pruning a return-flagged channel leaves a capture per pruned post carrying its text and original date; pruning a retire-flagged channel leaves none; a channel with no settings is not pruned at all.

**Blocked, and the dependency is mechanical rather than conceptual:** the bot can only delete its own messages, so pruning does nothing at all until the channel is bot-authored.

**A returning post is material, not an instruction to repost.** It arrives as a capture and is weighed like any other work — its claims may have been overtaken entirely, in which case the right outcome is deletion rather than a corrected repost.
Blocked by: [announcement-back-catalogue-rehomed]

#### [user] Article: Throughliner as a memory prosthetic — built by someone with bad recall, for a brain that avoids looking back [adhd-memory-prosthetic-article]
**Your idea, 2026-08-22, seeded from a grab bag of paragraphs from a conversation you had with Gemini** — processed the same session. Your own caveats set the editing brief: the parallels it draws between AI and human memory, and between the method's docs and memory types, are not all trusted; the 15-year-project storytelling is under-developed; there is a lot of lecturing and probable doubling-up.

**The core story, which is the article's force.** Throughliner is your coping mechanism for ADHD — advertised as a memory system for Claude, built by a person with bad recall. Friends encouraged you back into a project based on an interest you feel you have failed to build anything from in 15 years; on opening it, Claude immediately picked up audits and research planned six weeks earlier that you had completely forgotten — "a pleasant slap in the face. My memory system has got my back." The difference is invisible in projects you are continuously in; the long gap is what made it visible.

**Venue chain, your decision:** flintcraft.tech first, then a YouTube version, then potentially LinkedIn. This item covers the site article; YouTube and LinkedIn adaptations are follow-on work to file once the article exists.

**Disclosure settled, 2026-08-22: you are comfortable with the personal content everywhere it goes.** The photos-and-childhood-trauma element is on the chopping block for FOCUS, not privacy — your reason: its only connection is that you couldn't look back at your project much as you reflexively avoid your photo roll, and the rest may detract from the Throughliner selling points. The aversion analogy can survive as a sentence; decide the final cut at drafting.

**Science route, your decision: verify, keep only what fits.** The seed asserts amygdala-heavy encoding, dopamine deficits, episodic/autobiographical memory impairment in ADHD, trauma generalising recall into a threat, and a docs-to-memory-types mapping (LOG as episodic, FAQ as semantic, QUEUE unmapped). Before drafting, web-search each claim; file what holds in `workshop/resources/research/` with its index line; anything unsupported is cut or reframed as your first-person experience. The docs mapping is an analogy at best and is presented as one if kept.

**Known defects in the seed, to fix at drafting:** it names doc files Throughliner doesn't have (BACKLOG.md, UX.md, claude.md as the method's docs) — use the real four; the lecturing register and the repetition go; "brilliant" self-praise inherited from Gemini's voice goes.

**Walkthrough.**
1. Claude interviews you for the story — the project and interest (as much as you want public), what your friends said, the /plan moment and what it surfaced — and folds your answers into the draft material. Your choice, made at processing: interview at drafting rather than telling it now.
2. Claude verifies the science claims by web search, files the findings under `workshop/resources/research/` (index line in the same move), and lists which claims survived and which are cut. You see the list before drafting starts.
3. Claude drafts the article for flintcraft.tech, first-person throughout, with the photos/trauma element trimmed or kept per your call on reading the draft.
4. You read it and say what to change; repeat until you're satisfied.
5. You decide delivery to the site project: an INBOX message (you see the exact text first) or you carry the file across yourself.
6. You publish — Claude has no route to the site.
7. You confirm it's live; the send is recorded in `INBOX/sent.md`, follow-on captures for the YouTube and LinkedIn versions are filed, and this line closes.

**Held 2026-08-24 with the comparison article, same reason recorded there:** articles wait until the announcement-driven FAQ has material for Claude to draw on. Re-offered when the date passes; the lift judgment is whether the material is there.
Not before: 2026-09-21

**Files:** none in this project except the research file step 2 creates under `workshop/resources/research/`. The artifact is an article for flintcraft.tech. Relates to [competition-comparison-article] — a separate piece, no dependency either way.

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

#### Migrate this project's rezip, push and release prose into ritual definitions [host-rituals-migration]
Filed 2026-08-28 with the keep of [ritual-definitions-and-offers], from your framing that the release and rezip rituals are subparts of cycles. Host-only. **Designed 2026-08-29 at processing; both original blockers had built and are dropped.**

**The move:** the rezip's numbered steps and the release's numbered steps leave `workshop/resources/release-ritual.md` and become two ritual definitions in `CYCLES.md` — firing words "rezip" and "release", each with its `Writes:` field (the rezip declares `plugin/rezip-archive/`). The weekly-release cycle's step 3 points at the release definition instead of at the old document, so the steps live once. Nothing about how the user fires either changes.

**What stays, each for a recorded reason.** `release-ritual.md` survives as the reference companion holding the recovery procedures and the marketplace-collision guard — what-if material, not steps of a turn; its step lists are replaced by pointers to the definitions. CLAUDE.md's push section is untouched: push fires on a standing condition Claude must notice unprompted, not on a word, so it does not fit the ritual shape — the record already settled that a rule that must fire unprompted cannot be fetched.

**Files:** `CYCLES.md` (two definitions with `Writes:` fields), `workshop/resources/release-ritual.md` (step lists out, pointers in, recovery and guard kept), `CLAUDE.md` (the fetched-doc section repointed at the definitions).
Observable: a grep finds the rezip and release step lists in `CYCLES.md` and not in `release-ritual.md`, and CLAUDE.md's pointer resolves to the definitions.
Rule gate: run — an amendment relocating existing rules; nothing new admitted, no slot spent.

**Held on the zip fix, and the blocker is real:** [zip-entries-use-backslash-separators] rewrites the zip step in the same document, two items editing one file must not interleave, and the migrated definition should carry the new Python zip step rather than the PowerShell one it replaces.
Blocked by: [zip-entries-use-backslash-separators]
**Ordering, written on both items per the known-ordering rule (2026-08-29):** [ritual-declares-writable-paths] shipped 2026-08-29, so the definitions this migration writes carry the writable-paths field from the start.

#### [user] Rezip, restart, then run /setup so this project gets the workshop folder [workshop-migration-setup-run]
**Your sequencing, 2026-08-29:** the migration does the move, rather than a bespoke build doing it and the migration recipe being written separately. This project's own folders get carried across by the shipped machinery, which is the strongest test that machinery can have.

**The dependency is host-side and does not resolve in the session that builds [workshop-becomes-a-method-folder].** /setup runs from the installed plugin, not from the source in this repository, so the build has to be rezipped and the app fully restarted first — otherwise /setup migrates to the old shape and reports success.

**Walkthrough.**
1. Ask for a rezip once [workshop-becomes-a-method-folder] has been built and committed. Look for: the rezip reporting the installed stamp equal to the target's.
2. Quit the desktop app completely and reopen it — plugins load at launch, so a reopened window is not enough. Look for: the session opening reporting the new version.
3. Type /setup in this project. Look for: it reporting that the project's documents are on an older format and offering to migrate, rather than saying everything is current.
4. Let the migration run. Look for: a `workshop/` folder at the project root with `workshop/resources/` inside it, and `research/` and `testing/` still sitting inside that.

Observable: `workshop/resources/research/` and `workshop/resources/testing/` exist, and no `workshop/resources/` folder remains at the project root.

**References break between this step and the cleanup, and the window is minutes rather than days.** Six root documents name `workshop/resources/` paths — `CLAUDE.md`, `SPEC.md`, `README.md`, `QUEUE.md`, `CYCLES.md`, `TOOLS.md` — and they are repaired by [repo-cleanup-product-forward], which runs in the same sitting once this finishes.
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
- `CLAUDE.md`, `SPEC.md`, `README.md`, `QUEUE.md`, `CYCLES.md`, `TOOLS.md` — every `workshop/resources/` path repaired to `workshop/resources/`, derived from a grep for the literal string rather than from the design discussion.
- the moves themselves, by `git mv` so history follows the file.

Observable: a grep for `workshop/resources/` in a tracked file outside `workshop/` returns nothing, and the root's tracked entries are the list above and no others.

**The bot gets its own folder inside the workshop — your direction, 2026-08-29, answering half of [unreferenced-brand-files-and-brief]:** `throughlinerprojectboticon.svg` is the bot's live Discord avatar, so `workshop/bot/` holds everything that is the bot — `discord_post.py`, `nerds-welcome.md` and the avatar — healthily separate from the project and the posts it handles. Your words on its status: it is a folder, and it is not being popped out. Moving the file changes nothing live; Discord holds its own copy of the avatar.

**One consequence the build must surface as a `[user]` step:** the permission rule added 2026-08-29 names the script's path literally — `Bash(py workshop/resources/discord_post.py *)` in `.claude/settings.local.json` — and CYCLES.md's step commands name it too. The CYCLES.md repairs are the build's; the settings line only the user can edit, so the build stops and hands that one over when the move lands.

**`FABLE-BRIEF.md` is deleted — your call, 2026-08-29: it has done its job.** The build removes it with `git rm`, so history keeps it and the delete is revertible. It comes off the moves list.

**`workshop/resources/reader-test-workflow.js` is deleted too — your call, 2026-08-30, closing [reader-test-workflow-unreferenced]:** old stuff, not needed — you no longer run reader tests with subagents, you test the plugin by hand and find it better. Removed with `git rm` like the brief; history keeps it.

**`.pytest_cache/` is removed as a fossil — settled 2026-08-30, closing [pytest-cache-at-the-root] whose both halves inspection disproved:** its files predate this repository's 1 June rebuild and name a pre-rebuild folder layout, so nothing here has ever run pytest and no habit exists to hunt; and pytest's own ignore file inside the folder means git already ignores it, so no `.gitignore` entry is added. Plain `rm -r` — it is untracked, and nothing regenerates it.

**The badge becomes the repo's face — settled 2026-08-29 with [unreferenced-brand-files-and-brief].** Your account of `throughliner-icon-badge.png`: used on Discord only so far, possibly created to meet its size limits. The build embeds it at the top of `README.md` as the project's logo — it stops being unreferenced by being used, it serves the product-forward goal directly, and at 188K it is embeddable where the 4.5MB original is not. The original still moves to `workshop/`; history keeps it either way.
Runs alone
Blocked by: [workshop-migration-setup-run]

#### [audit] First announced-claims sweep turn — run after Wednesday's release [announced-claims-sweep]
Filed 2026-08-29 at a close's cycles check; processed 2026-08-30. The cycle has never run a turn — what the observable currently reads is the cycle's own authoring record, a collision [cycle-observable-slug-collision] fixes at the method level.

The turn: re-read every retained claim in `INBOX/sent.md` for retiring channels and both forums against the **installed** plugin, file one capture per falsified claim (satisfied while an open capture carries that post's id), check the forums' topic ordering against the numbers in the titles and report where they differ, and record the turn under this slug — the record opening by saying it records a completed turn, per the corrected observable.

**Held until after the weekly release on Claude's recommendation and your agreement**, from the capture's own reasoning: a release is the thing most likely to falsify a claim, so a sweep just before one checks claims the release then re-breaks. Reads `INBOX/sent.md` and the live channels; edits nothing.
Not before: 2026-09-02

#### [audit] Beta-test session records from the first beginner tester, read as test data — one capture per observation worth acting on [beta-test-session-records]
**On the user's instruction, 2026-08-30; processed 2026-08-31, kept as an [audit] on Claude's recommendation and her agreement.** The turn: read the tester's session record with its nine end-of-record observations, and the slim conversation-only copies of whichever of his five sessions are actually Throughliner runs (identified first; the rest stay unread — his privacy and the reading cost point the same way). File one capture in Unprocessed per discrete observation worth acting on; the `/clear` instruction disaster is flagged in advance as the strongest candidate. Edits nothing else. Reads: `workshop/resources/testing/beta-tester/` (or its `workshop/` successor). The record is Claude-written reconstruction, so its claims stay unverified until he confirms them or the raw files corroborate — findings say which footing they rest on.
Blocked by: [tester-data-carries-employer-material]
**Held 2026-08-31 because the material is not on disk yet:** the download is that walkthrough's step 1 (the Gmail connector cannot read attachments — issue anthropics/claude-ai-mcp#943), so this lifts by itself once it runs.

**Where it is.** An email to the user, subject "Throughliner beta test — session record, 30 Aug", from the tester's own address, with `Beta-test-session-record-2026-08-30.md` attached. **More are still incoming**, so the processing turn should check for later mail rather than assuming this is the whole set.

**What it is, in his own framing, and the caveat is load-bearing.** A reconstruction rather than a transcript: no internal reasoning, and his replies paraphrased except one directly quoted line, written by Claude at the end of his session for a Claude at this end to read. So it is Claude-authored content about a user's session — the handoff-provenance case exactly. **Read its claims as unverified until he confirms them**, and prefer the raw `.jsonl` where a question turns on what was actually said; see [tester-prompt-asks-for-reasoning], which is about getting that file instead.

**The two findings he leads with, both already filed separately so they are not buried in an attachment:**
- the session opened on guidance that told him to type `/clear` and then do a second thing; `/clear` wiped the screen before he could read the second instruction, and nothing had told him what `/clear` does. Most of his session is the recovery from that. **Not yet filed on its own** — it needs the attachment read, and it is the strongest candidate in the set;
- SPEC.md carrying a name he was never asked for — [setup-infers-a-name-into-spec].

**What he reports working, and it is the one positive in the set:** the recovery from the `/clear` problem succeeded, and succeeded *because* the method writes things to files — the next step was still sitting in the queue where the previous session left it. Searching for the lost conversation itself turned up nothing. That is the throughline doing the job it exists for, observed by someone with no stake in the design.

**Nine observations sit at the end of the attachment, most critical and one positive.** Reading them is the processing turn's work; the attachment has not been opened here.

**This is the first beginner tester**, so the material is worth more than its length: every other session on record was run by the person who wrote the method.

**What the raw material is, merged 2026-08-30 from the deleted [beta-raw-transcripts-arrived]:** five `.jsonl` files (~2.8 MB) from his second email the same day — and they are **all** his chats in that folder, not one test session; one is explicitly him installing git. So the processing pass first identifies from the slim copies which sessions are actually Throughliner runs and reads only those, leaving the rest unread — his privacy and the reading cost point the same way. The storage and download are [tester-data-carries-employer-material]'s walkthrough; the strip-to-conversation-text preprocessing pass from CLAUDE.md applies, and applies harder with five files.

#### First port-facing changelog now has a real consumer waiting — verify the next release publishes it [first-port-changelog-has-a-consumer]
Filed 2026-08-29 by the goal session that assessed the Egnatia-OC OpenCode port and sent its assessment pack (register line in `INBOX/sent.md`). The generator and its release-ritual step shipped in 819f7f1, but no release has run since, so no changelog has ever been published — and the pack's CYCLES.md tells his port's weekly [upstream-catch-up] cycle to look for one on each release, described as coming soon. Two things to check at the next weekly release turn: that the publish step actually attaches the changelog, and that its output over the range his pin trails (743aa63..release) reads usefully for the one tracking port known to exist — he is its first real reader, and the fallback his cycle runs until then is a raw diff. Worth telling him when the first one is up.

**Processed 2026-08-31, held to the release cycle's own day on the user's agreement:** the work rides Wednesday's release turn — during it, confirm the changelog is attached, read its output over 743aa63..release for usability, then draft the note to the porter, sent only on the user's yes and registered like any send. His new Kilo Code port (port-showcase, 2026-08-31) doubles the audience for the same artifact.

**The note also mentions MCP, on your instruction 2026-08-31, worded to what is actually true:** an MCP server is being explored, not committed — the design is held behind its own inventory work ([mcp-server-standing-intent]) — and the compatibility claim is stated at its evidence level: both his harnesses run local MCP servers per their vendor docs (`workshop/resources/research/port-harness-mcp-support.md`), read rather than tested. The shipped-only rule is why the wording carries "exploring" and not "coming": a DM creating an expectation the queue may not honour is the same exposure as a post, softer only in audience.
Not before: 2026-09-02

## Unprocessed

#### Last session advises processing [untrack-method-files-here] next [forward-advisory]
The cleared region holds 33 items and its head is the gitignore chain: [untrack-method-files-here] takes this project's method files out of git (the user's decision, warning given and accepted), [gitignore-choice-with-snapshots] builds the setup choice, the snapshot net and the scrub-boundary amendment, and the tester-data walkthrough follows — a /next run works them in that order. Two things for whoever runs it: the tester-data and Discord-permission walkthroughs need the user present (downloads and role toggles are hers), and the run's builds transcribe dispositions already written on their items — a build finding itself designing a rule should re-read its item, because the disposition is there. The overlap scan found nothing in Unprocessed that blocks the head of the queue: what waits — the tester-instructions wording, the maintenance sweep's first turn, the compliance-audit-lag audit, the MCP inventory's dependents and a dozen smaller captures — bears on later work, not on the untracking. Advice, not a command; read and cleared at the next planning opening either way.

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
**Your goal, 2026-08-22: actual release to the Claude marketplace so people can browse for it inside the desktop app.** The research (`workshop/resources/research/claude-marketplace-listing-paths.md`) found two routes: the official marketplace is the only one browsable in-app by default, is curated at Anthropic's discretion, and has no self-serve path — the submission form feeds the community marketplace instead. So the realistic sequence is community first: submission via the clau.de/plugin-directory-submission form, automated security scanning plus human review, a public listing at claude.com/plugins pinned to a commit SHA; then official at Anthropic's discretion.
What a keep must settle: ending the pre-release posture CLAUDE.md declares ("in active testing, not ready for the Claude marketplace") — the user's decision; version-consistency discipline (plugin.json, changelog, git tags — the commonest reported rejection cause; the weekly release cycle [weekly-release-cycle] supplies the cadence for it, and a changelog does not yet exist); and confirming the name is final, since a marketplace slug is immutable once published and a rename breaks every install. The submission itself is a `[user]` step — a web form Claude cannot submit.
Runs behind [weekly-release-cycle] in spirit — a regular release rhythm is what makes the version discipline real — carried as this sentence rather than a blocker, since the submission decision is independently the user's.
**Reframed 2026-08-22, same session: the listing is the stable channel of the three-channel model settled on [beta-tester-pathway].** The research question this paragraph used to flag is answered — see below.
**Your sequencing, 2026-08-22, revised the same day: the listing launches alongside the beta channel rather than after it** — your first thought was beta testers before any listing, revised when it emerged the listing may be the only realistic way testers arrive; the listing is framed honestly as early instead. YouTube videos come after both, on your reasoning that videos without a listing would look bad to viewers while YouTube may bring the very first users. Written on both items per the known-ordering rule.
**Update-cadence research answered, 2026-08-22** (`workshop/resources/research/claude-marketplace-listing-paths.md`, listing-updates section): the listing's commit pin updates **only after re-review**, and no turnaround is documented anywhere — so the Wednesday stable promotion cannot push to the listing. The realistic shape: the weekly stable channel lives on this repo, and the listing is updated on a slower submit-and-wait rhythm — monthly, or when something worth announcing lands — worded as "submit the update".
**Your decision, 2026-08-22: the not-ready-for-the-marketplace posture ends.** You are ready to remove it; the one thing genuinely holding the submission is company registration, which is [abr-identity-and-address] on the flintcraft.tech project's queue — designed there with its research done. A dependency note was sent to that project's INBOX the same day (recorded in `INBOX/sent.md`); it asks no new work, only flags that a second project now waits. Whether the submission form itself actually requires registered-business details is unverified — check at keeping.
**Dated 2026-08-22 with your approval.** It waits on the ABR work in another project, which nothing in this queue can build; a month out is when there is plausibly news. Not offered again before then. Still to settle at the eventual keep: the changelog, and confirming the Throughliner name is final (the slug is immutable).
**Understudy ordering, your decision 2026-08-22: the launch does not wait for it.** Understudy debuts as the standard companion app with the YouTube videos (already last in the chain); the listing stays silent on it until it is real. Until a companion app honouring the editing-state contract is out, launch materials carry one honest line: don't edit the project docs while a run is writing them. A dependency note went to Understudy's own project INBOX the same day (recorded in `INBOX/sent.md`). Written on both this item and the beta-channel item per the known-ordering rule.
Not before: 2026-09-22

#### [user] Discord post draft: subprojects [discord-post-subprojects]
Drafted 2026-08-25 at the planning close under the close-sweep design; approved as a candidate by you, with your addition of the start-big benefit. Waits on [subprojects-pop-out] shipping; verify against the shipped build before posting (one-a-day pacing repealed 2026-08-28). FAQ potential noted for posting time, per the announcement-time FAQ rule.
**Verified 2026-08-29 against the installed build's setup procedure — all five claims hold**: the parent-spec read, the confirm-with-you step, the mail to the parent, upward-only dependencies, no scripted way back in. **Re-verified 2026-08-31 against the installed 1.21.1-test3 docset — all five still hold.** **Destination is #tips by the two-kinds tie-break** — it reports a change and walks through the how, and where both tests pass the tip test wins. **Dated to 2026-09-01 on the user's citing of the one-post-a-day-per-channel rule**: today's tips slot was taken by the readiness-line tip, so this posts tomorrow at the earliest, on her yes to the exact text.
Not before: 2026-09-01
**Draft (under 2,000 characters):**
> **Subprojects: start big, split later.** When one part of your project outgrows the rest — the software inside a business plan, the contracts inside a venture — you can now pop that subfolder out into its own full Throughliner project. Run setup inside the subfolder: it reads the parent project's spec, works out which part this is, checks with you, and tells the parent it's moved out. From then on it's an ordinary project with its own clear queue.
>
> The quiet benefit: you don't have to understand your project's final shape at the start. If the idea is nebulous and multi-parted, start it as one big project, rest assured that any part which grows a life of its own can be popped out later.
>
> The link back is deliberately simple: work in a subproject can hold up work in the parent — never the other way round — so the popped-out piece marches forward on its own terms, and anything crossing between them travels as mail you approve, never as one project silently editing another. One thing to know going in: there's no scripted way to pop a subproject back in, so it's for parts that have genuinely outgrown the nest.

#### [user] Discord post draft: multi-person sessions [discord-post-multi-person]
Drafted 2026-08-25 at the planning close under the close-sweep design; approved as a candidate by you, with your additions: name Chagora — your new app by its-coughfee, designed to work with Throughliner but not dependent on it — and credit zebbern. Both names are published GitHub identities, which is what the scrub rule permits. Explanatory register. Waits on [multi-user-identity-layer] shipping; verify against the shipped build before posting (one-a-day pacing repealed 2026-08-28).
**Date passed 2026-08-30; posting waits for the next session on your agreement, same ground as [discord-post-subprojects]:** the send-permission rule takes effect only in a fresh session, so it posts terminal-free there, after the subprojects post. Claims are verified against the installed build at posting — unlike its sibling, this one has not been verified yet. Pacing between the two is the posting session's call.
Not before: 2026-09-02
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

#### Tip candidate: how work gets held, and how it lets itself go again [tip-holding-work]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.
Cycle: [tips-posting]

Observed: SPEC describes work sitting below the readiness line for exactly two reasons written on the item itself — `Blocked by:` naming one or more queue items, or `Not before:` naming a date — with the queue lint checking both and every planning session asking, per held item, whether the blocker shipped or the date passed. None of this appears in any post, how-to or FAQ entry.

Why it matters: it answers a question every user of a growing queue eventually has, which is what to do with work that is real but cannot happen yet. The tip's point is that you do not have to remember any of it: a date is read off the calendar, and a blocker is a queue item like any other, so the thing being waited on gets planned and done rather than living as a sentence buried inside another item. That last part is the recorded failure the design came from — one item sat shelved for weeks on a step nobody could see was work.

#### Tip candidate: cycles, for work that comes round again [tip-cycles]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.
Cycle: [tips-posting]

Observed: SPEC describes putting an artifact on a cycle — a named piece of recurring work defined once, with its steps, its cadence and the observable that marks a completed turn — after which the openings and closes of /plan and /next compute due-ness and file the work into the queue. A project with no cycles has no doc and pays nothing. Nothing in `INBOX/sent.md`, the FAQ or `ANNOUNCEMENT-IDEAS.md` mentions it.

Why it matters: recurring maintenance is the work that quietly stops happening, and this is the method's answer to it. The tip's angle is the part that makes it different from a reminder: due work becomes an ordinary queue item weighed against everything else, rather than a notification on a board nobody is obliged to read. Worth noting too that position is never stored — each check recomputes from the observable — so nothing drifts out of step if you skip a week.

#### Tip candidate: projects that can send each other mail [tip-cross-project-inbox]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.
Cycle: [tips-posting]

Observed: SPEC describes an `INBOX/` folder in every project, scaffolded at /setup, through which one project writes a durable message into another's mailbox; the session opening names waiting messages and directs the session to read them, mail is routed at the openings of both /plan and /next, and an arriving message is triaged and archived. Nothing has been posted about it, and the FAQ has no entry.

Why it matters: users running more than one project on the method have this and do not know it. The tip's honest angle is the guarantee and its limit together — sending places a file in the recipient's mailbox and nothing confirms it was read, which is why the design has no automatic read-receipt (a receipt would be an automatic send, and nothing leaves the machine unapproved). Also worth saying: a message is another project's report, not an instruction, and only the user's own words direct the work.

#### Tip candidate: TOOLS.md, so a fact about your machine is learned once [tip-tools-md]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.
Cycle: [tips-posting]

Observed: SPEC describes a `TOOLS.md` at the project root holding facts about a project's environment that are expensive to re-derive — a tool installed at a known path, a build command that fails specifically from Claude's shell — created the first time a session has such a fact, with a build's environment check reading it before assuming anything is absent. A project with none has no file and pays nothing. No post, no FAQ entry, no line in the pool.

Why it matters: the failure it fixes is one users feel directly — a session assuming a tool is missing and handing them a manual workaround, when the same project had already proved the tool works. The recorded instance cost a run its first act. It is also the smallest possible feature to explain, which makes it a good slow-news-day tip. Borderline on the visibility screen: the mechanism is internal, kept because the file sits visibly in the project root and the failure it fixes is one the user feels directly.

#### Tip candidate: seeding the queue from your spec, so features don't die in SPEC [tip-seed-from-spec]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.
Cycle: [tips-posting]

Observed: SPEC describes /plan seeding the backlog from SPEC — offered automatically only in the narrow thin-queue/rich-SPEC state, invocable manually any time, with the user choosing the granularity between a few coarse milestones and granular per-feature items, and the derived items landing in Unprocessed as ordinary captures rather than straight into ready work. Nothing has been posted and the FAQ has no entry, though `ANNOUNCEMENT-IDEAS.md` carries a line on it.

Why it matters: it addresses a failure the user can recognise in their own project — a rich setup interview produces a SPEC full of buildable features with no path into the queue, so the whole feature set sits there with nothing to build it. The tip is short: your spec already lists the work; ask and it becomes queue items you can weigh.

#### Tip candidate: what happens when your project falls behind the plugin [tip-keeping-projects-current]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.
Cycle: [tips-posting]

Observed: SPEC describes three checks at every session start — flagging whole docs the project is missing, topping up a doc missing a newer setting, and halting the session outright when the project's documents are on an older format than the plugin expects — plus the deliberate design that a plugin version change on its own produces no notice at all. Nothing has been posted about any of it and the FAQ has no entry.

Why it matters: the halt is the strongest thing the method does to a session, and a user who meets it with no warning will read it as a fault. It also carries a reassurance worth stating: the migration edits documents rather than replacing them, the top-up never overwrites anything the user wrote, and the format number is deliberately not the version number so it cannot cry wolf at every release.

#### Tip candidate: why Claude writes first and reports, and how to ask for the opposite [tip-write-first-and-show-first]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.
Cycle: [tips-posting]

Observed: SPEC describes write-first approval settled by one test — is the previous version recoverable without the user's help? — with queue items, captures, LOG entries, SPEC edits and ordinary build edits written first and reported, while a commit message, anything leaving the machine, and a wholesale conversion of an untracked document are shown first. It also describes the user being able to ask for show-first at any time, for the rest of that session, with the switch moving only toward more showing. No post, no FAQ entry.

Why it matters: this is the single most visible behaviour difference a new user notices, and without the explanation it reads as Claude changing their files without asking. The tip's honest half is the trade the design accepts: a file briefly holds content the user has not agreed to, which is cheap in a git repository, and the real risk is not rejection but the user not noticing — which is why the report has to name its artifact precisely enough to open. Pairs naturally with the queued [discord-post-plain-english-consent] draft; whether they are one post or two is a decision for processing.

#### Tip candidate: the freeform tag, for work a build run must not touch [tip-freeform-flavor]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.
Cycle: [tips-posting]

Observed: the "Running /next" how-to post names `[audit]` and `[user]` and stops there. `[freeform]` — work done by hand rather than by /next, because it is large or because it characteristically cannot run inside a run — is never mentioned in any post or FAQ entry, though it is one of the four flavors and the one /next halts on outright rather than skipping.

Why it matters: a user meeting an unexplained halt has no way to tell a deliberate stop from a fault. The tip also carries the clearest example the method has of why the flavor exists: a repair to the machinery /next itself depends on cannot run inside a run, because running the broken mechanism to build past it is the failure. Worth stating that most freeform work never passes through the queue at all — it is just you and Claude working by hand, and the close reads the edits as expected work.

#### Tip candidate: what the scrub gate does, and what it will never promise [tip-scrub-gate-limit]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.
Cycle: [tips-posting]

Observed: SPEC describes a hook scanning QUEUE.md, SPEC.md and LOG entries for credential shapes, alongside Claude reading its own writing against a checklist — personal names, case details, third-party data, identifying paths — at the three moments text enters a committed doc. It also states the limit that must never be softened: no pattern can tell whether a sentence quietly identifies a real person, so the method never tells a user their artifacts are scrubbed or safe to publish. Nothing has been posted and the FAQ has no entry.

Why it matters: this is the one place the project deliberately under-claims, and saying so publicly is worth more than the feature. A user deciding whether to make a repository public needs the honest answer — that not publishing these artifacts is the only complete protection — and they will not get it from a tool that markets the gate. Post it as the limit first and the mechanism second. Borderline on the visibility screen: the gate itself is invisible, kept because the tip answers a question users actually ask — whether their repo is safe to publish.

Note for processing: this is a tip about a safeguard, not an announcement of a change, so it fits the tips test ("explains one Throughliner feature") rather than the news test.

#### Tip candidate: the advisory note a close leaves for the next planning session [tip-forward-advisory]
From the features-needing-tips audit. Screened for visibility 2026-08-28 — passed the is-this-visible-to-a-user test; not yet processed as a post.
Cycle: [tips-posting]

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
Cycle: [tips-posting]
**Recycle from the #announcements post of 2026-08-12, "Your projects can now talk to each other"** (message id 1537247086179786772). Found by the announcement-history sweep of 2026-08-28, which mined the channel's full history — the early posts predate the sent register, so nothing had looked at them for tip material.

Passes the tip test: it explains one feature. Passes visibility: a user running two projects sees the waiting-mail line at a session opening and the INBOX folder in their own project.

What a tip would walk through, rather than merely reporting the capability exists: where the folder is, what a session opening says when mail waits, that a planning session opens it and files what it contains, that nothing is sent without seeing the exact wording, and that the folder is gitignored.

**Drift check before drafting — the original is 16 days old and the feature has grown since.** Build runs now open mail too, not only planning sessions; an address book records a correspondent's path on first use; `INBOX/sent.md` records what went out. The original post lists the first two as "coming next". Re-verify every claim against the installed build at drafting.

#### [user] Tip: what /next does with your spec while it builds [tip-recycle-spec-read-at-build]
Cycle: [tips-posting]
**Recycle from the #announcements post of 2026-08-14, "Spec-driven development, finally the right way round"** (message id 1537631817849380925). Filed by the announcement-history sweep of 2026-08-28.

Passes the tip test: one feature — SPEC.md read at the start of a build run, each item checked against it, and a halt naming the sentence it contradicts. Passes visibility: the user sees the halt, in their own words, in a run they are sitting in.

**Drift is material here and the recycle must not reuse the wording.** The original's last bullet says a build establishing new product truth "asks first, adds SPEC.md to its own file list, and edits it in the same commit". That is repealed: a build now files the sentence it thinks SPEC owes as a capture and never writes SPEC, because the session that made a choice is not the session that certifies it. A recycle that reuses the old bullet would announce behaviour the plugin no longer has.

#### [user] Tip: the work cycle, and the two ways work comes back to the start [tip-recycle-work-cycle-loop]
Cycle: [tips-posting]
**Recycle from the #announcements post of 2026-08-21, "Claude can now tell you how its own work cycle fits together"** (message id 1540223708210270219). Filed by the announcement-history sweep of 2026-08-28.

Passes the tip test: it explains one thing the plugin has — the loop the four commands sit in. Passes visibility, though it is the weaker of the two limbs: the user does not see the rules file, but they do live the loop, and "which command do I run now?" is a question they actually ask.

A tip here is the walk-through the original was not: capture, plan, next, done, fresh session — plus the return edges, which are the part a flat list misses. An audit files findings back into the queue; a build that discovers something files it and carries on; a step that is yours leaves the loop only when you have done it.

Borderline on visibility, and recorded as such: the original's subject was partly the internal fix (a section added to the rules). The tip has to be about the loop the reader is in, never about the section that was added.

#### [user] Tip: why your old queue items stop getting skipped [tip-recycle-ordering-ladder]
Cycle: [tips-posting]
**Recycle from the #announcements post of 2026-08-23, "your old queue items stop getting skipped"** (message id 1540901808090783824). Filed by the announcement-history sweep of 2026-08-28.

Passes the tip test: one feature — the order a planning session works through unprocessed captures. Passes visibility strongly: the user watches items being presented in that order, and the complaint it answers ("why does the same item keep coming up?") is one they actually voice.

The original already reads close to a tip. What a recycle adds is the how-to half: what to look for in the one-line narration naming the order used, and that naming a few items to start with sets the order rather than the length of the run.

**Drift check:** the ladder's rungs are described in SPEC as they now stand — re-read that before drafting rather than trusting the post's four-line list, which was written to an earlier shape.

#### [user] Tip: what the planning close does to your queue, and what it deliberately leaves alone [tip-recycle-close-reorder-restraint]
Cycle: [tips-posting]
**Recycle from the #announcements post of 2026-08-10, "Token savings, and most of them are things we're going to stop doing"** (message id 1536412983499165746). Filed by the announcement-history sweep of 2026-08-28.

Passes the tip test: one feature — the single pass the planning close makes over Processed, batching the steps that need you to the end. Passes visibility: the user can open QUEUE.md and see that their items sit in the order things landed, with the human stops grouped at the bottom.

The angle that makes it a tip rather than a changelog: file order records *when things landed*, and that is more useful than a ranking that goes stale. Three other reorders were removed to keep it that way.

**Drift check:** the post's framing is a savings announcement, which is the internal-arrangement shape the visibility rule now excludes. The recycle keeps only the user-facing half — what your queue looks like and why — and drops the token-saving story entirely.

#### Augmentatism article: where Throughliner fits the philosophy and where it fails its central claim [augmentatism-article-material]
Filed 2026-08-28 from INBOX mail sent by the flintcraft.tech site project (archived at `INBOX/archive/2026-08-28-from-flintcraft-augmentatism-article-idea.md`).

**Provenance is unusual and binding: the analysis in the mail is Claude's reading, not the user's.** She raised the idea and named its centre — an article on all the ways Throughliner is so augmentatist, and so not, especially the Law of Creative Latency, which she calls Throughliner's strong suit — then deliberately stopped before reading the analysis, so as not to prime herself. She is writing her own commentary on the manifesto and intends to cross-pollinate the two. Nothing in the mail's reading may be presented back to her as her position.

The source is `https://augmentatism.com/`, a manifesto by Manolo Remiddi. The mail's summary of it is a fetch from 2026-08-28 and is to be re-verified before drafting. The mail's candidate shape: Throughliner satisfies the philosophy's principles almost point for point — Creative Latency most of all, since the method's whole shape is friction placed on purpose — while failing its central political claim, the Many versus the One, because it is built entirely inside one company's ecosystem.

Two constraints from the sender's own rules travel with it: a named person's published work gets third-party care (describe accurately, verify, never argue the author is wrong), and the site's SPEC bars claiming Throughliner is the only holder of any value.

**What lands here is the sending-back half:** the mail asks that this be processed here and sent back. Articles for the site are written there; this project's part is its reading of the method against the manifesto. The send needs the user's yes to the exact text like any outbound message.

**Skipped 2026-08-30 at the user's direction, with her priority on record: this must come soon.** The processing turn surfaced a tension the next session starts from: approving the send means reading the analysis, and the user is deliberately unprimed until her own commentary exists — so the send cannot precede her commentary, and only she can say when she is clear. She declined to open the archived mail this session for exactly that reason.

#### [user] Tip candidate: rituals — a step list you fire with a word [tip-candidate-rituals]
Cycle: [tips-posting]
Filed at the 1.21.1-test1 rezip, 2026-08-28, per the rezip's tip-candidate step: rituals landed in this build. Passes visibility — a user sees their rituals named at every session opening with the word that fires each, and /plan offers to write one down when it meets procedure-shaped work. A tip would walk through: asking to save a repeated procedure as a ritual, where it lives (the cycles doc), saying the word to run it, and what promotes one to a cycle. Not postable until a release clears it; the release marks this capture with the version when it does.

#### Post drafts leave the queue, keeping their reasoning behind [post-drafts-leave-the-queue]
**Raised by you, 2026-08-29.** Your position, and the narrowing is yours: the captures themselves are not in dispute — what does not belong in the queue is the full post text. A finished draft is a deliverable rather than work-reasoning, and the method's own view-in-doc rule already says doc-resident text is pointed at rather than pasted.

**You ruled out the LOG, and your own doc routing agrees with you.** `LOG/` records what happened; a draft that has not gone out has not happened, so storing it there turns the record into a filing cabinet. Your words: *"log is not a place for writing to live."* Current practice is the other way — the 2026-08-22 comparison-article draft's full text sits in `LOG/2026-08-22-competition-comparison-article.md` — and that is evidence of practice, not of correctness.

**Measured at processing, and it must not be described as shortening the queue.** QUEUE.md is 772 lines / 138KB. The verbatim draft text is **10 lines**, across three items — [discord-post-subprojects], [discord-post-multi-person] and [discord-post-session-smoothings]. This is a principle fix and will not be felt as a size one. For the record of where the length actually comes from: roughly 155 of those lines arrived during the 2026-08-29 planning session itself, as settlement prose on processed items.

**Claude's position, recorded because it is the one contested point: tracked, not gitignored.** An approved-but-unposted draft carries a public claim and cannot be reconstructed — which is the exposure cleared the same morning on [sent-register-untracked]. A gitignored drafts folder recreates it.

**The destination is deliberately not chosen here.** Where it lands is a question about the repository's shape, which [repo-cleanup-product-forward] answers; deciding it here and re-deciding it in the same session would be the wrong order. That is also why this cannot yet state what it changes: the file list is one path short.

**What it will change once the destination is known:** the three items' `**Draft (under 2,000 characters):**` blocks come out and are replaced by a one-line pointer; the draft text is carried across byte-for-byte rather than retyped.
Blocked by: [repo-cleanup-product-forward]

#### Inventory of the repository root and `workshop/resources/`: what each entry is and what reads it [repo-inventory-table]
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
workshop/resources/               below.
```

**`workshop/resources/`.**

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

#### Third steering layer is live in this project, and the compliance checklist says there are two [doubled-rules-table-misses-the-brevity-style]
Found live 2026-08-29 while rebuilding an old build from its commit — `plugin/throughliner/output-styles/` was in it, which a retirement was supposed to have emptied.

**The retirement is real and this is not it.** `concise-throughliner.md` — auto-applied at system-prompt priority — was deleted 2026-08-14. What ships today is a different file, `brevity.md`, named **Throughliner Brevity**, offered at /setup and enabled per project with the user's consent. SPEC describes it correctly.

**But the compliance checklist reasons as though nothing shipped.** Its doubled-rules section says "**Two layers now, not three, and the change is recent**", lists (G) the user's global CLAUDE.md and (M) the method's own always-loaded rules, and builds a twelve-row table on that pair — concluding that eight rows are unattributable and that three M-only rows are "M working alone".

**In this project the third layer is switched on.** `.claude/settings.local.json` carries `"outputStyle": "Throughliner Brevity"`, and that style asserts the method's communication shape at system-prompt level — leading with the decision, one item at a time, plain English for non-coders. So several of the table's M-only rows are not M working alone here, and the table currently overstates what this project's narration tests.

**Why it matters beyond tidiness.** That section exists precisely to stop this project's own good behaviour being read as evidence the shipped rules work. A table that undercounts the layers does the opposite of its job — it makes the evidence look cleaner than it is. The 2026-08-29 compliance audit used this section and inherited the error.

**Changes.** `workshop/resources/method-compliance-audit-checklist.md` — the doubled-rules section restated for three layers, with the brevity style's rows marked, and the deletion of `concise-throughliner.md` kept as the history it is rather than as the current state. Whether the style's rows are marked per-project (it is opt-in, so a consumer may not have it) is the judgement the rewrite has to make.
Observable: the section names three layers, the table has a column for the shipped style, and a grep for "Two layers now, not three" returns nothing.

#### Project types nobody expects to run in Throughliner — a listicle video [project-types-listicle-video]
**Raised by you, 2026-08-29**, while reshaping [legal-demo-video-guide], and kept as work of its own on your decision rather than as a variant of that item.

One video running through several unexpected project types, each getting the length of a bullet rather than a whole video. A legal matter is one of them. The reason it works is the same one that makes the legal case worth filming at all: these are not what anyone expects a coding tool to be pointed at.

Undesigned: which project types, how many, how long each gets, and whether the material comes from projects you have actually run or from invented examples. Designs alongside [legal-demo-video-guide] and [determinism-lesson-video], which share the same YouTube-folder sessions.

#### Ports-forum posts can now cite a live tracking port, and two of its findings are upstream material [ports-forum-gains-a-live-example]
Filed 2026-08-29 by the goal session that assessed the Egnatia-OC OpenCode port (throughliner-opencode on GitHub — a pristine-vendor tracking port, 34/34 files byte-identical to 743aa63). Bears on [ports-forum]: posts 3 and 4 (pulling changes in; declaring your flavour) can now point at a real port doing both, subject to his say-so on being named. Two of the assessment's findings are also candidates for upstream's own docs rather than only his queue: the zip-separator defect already filed as [zip-entries-use-backslash-separators] matters more now a Linux-side porter demonstrably consumes our artifacts, and his ANALYSIS.md's mapping table (Claude Code hook protocol → another harness's events) is exactly the worked example `docs/ports.md` says the mapping judgment needs — worth weighing whether ports.md should link out to ports' own analyses or stay mapping-agnostic. The full assessment survives in this session's LOG record; the pack itself was extracted and not kept.

#### Ongoing research: how to support someone into self-hosting Throughliner, whatever their capacity [self-hosting-onboarding-research]
**Raised by you, 2026-08-30**, at the close of the OpenCode-port goal session, when you asked that its artifacts be preserved "for reference and deriving findings for new ports" and framed the outcome sought: we know better how to support someone to become self-hosting on Throughliner, in whatever capacity that is. The standing subject: what a person needs — a porter on another harness, a consumer adopting the method, anyone in between — to reach the point where their project develops itself with the method. The first data point is on file: the OpenCode assessment pack (`workshop/resources/research/opencode-port-assessment-pack-2026-08-29.md`), whose reusable parts are the assessment lenses, findings-delivered-as-a-queue, the bootstrap gate before self-hosting, a per-port catch-up cycle, and the hand-delivered seed. What accrues here: how the Egnatia-OC injection actually goes (his bootstrap results and first /plan are the live experiment), the next port's pack, and what [setup-self-hosting-seed] and the ports-forum posts teach about the non-port capacities. For processing: decide whether this stays a standing research line the record accretes under, or spawns specific work items as findings arrive — it is deliberately not a build.

#### Checkpoint counts dropped mid-session and the user had to ask for them [checkpoint-counts-drop-mid-session]
Observed live 2026-08-30, caught by the user. The planning checkpoint's required shape ends on two counts — ready to build · left to process — and the session held the shape for its first five checkpoints, then dropped the counts after a mid-session /rescan and never resumed them until asked. The counts had shipped into the checkpoint shape only the day before ([checkpoint-count-dropped-ready-number]).

Worth more than the apology because the shape of the failure is informative: the drop coincided with checkpoints whose outcome half grew complicated (merges, mover notes, a rescan interleaved), which suggests the last fixed element of a message shape is what gets crowded out as the front grows. Whether that needs anything — sharper wording in plan.md's checkpoint block, or nothing beyond this record — is the processing question. The counts also cost a digest refresh to state accurately late in a session, which may be part of why they slip.

**A second instance the same day, caught by the user again ("why did you roll in two turns just now?"):** a checkpoint fused the next item's presentation with a family-wide skip recommendation covering eighteen tip candidates — two decisions in one message, with the closing question covering only one of them. Different symptom, same site: the checkpoint's fixed shape giving way when the session has something extra to say. Process the two together.

#### Research queued as build work despite the shipped rule against it, in the session researching noticing failures [research-misrouted-to-queue-live-instance]
Observed live 2026-08-30, caught by the user ("research is not queued work — it's always done on the spot"). Two research efforts were processed into Processed as cleared build items, against two shipped rules both loaded in the same session: plan.md's resolve-now list names research first among what planning does on the spot, and its decision step explicitly says a research item wearing a build's shape must not pass the check. The same session had earlier followed the pattern correctly (the determinism example bank, researched and filed within the hour of being asked).

Worth keeping as a specimen beyond the correction: the misroute happened while designing research into exactly this failure shape — a rule present, loaded, and not firing at its moment. It is first-hand data for the eliciting-proactive-research-offers finding (`workshop/resources/research/eliciting-proactive-research-offers.md` once it exists): rule presence does not produce rule firing, and the miss was invisible from inside until an outside reader challenged it. Both misrouted items were pulled and the research run on the spot in the same session.

#### Re-offers of held and dated work re-ask what the premise rests on [premise-recheck-at-re-offer]
Candidate rule from `workshop/resources/research/eliciting-proactive-research-offers.md` (2026-08-30), ranked second there: when the below-line revisit lifts an item, or a dated capture returns, the presenting turn asks what the item's premise rests on and whether anything has verified it since it was written. Reaches slow-cooking work — the shape of the months-long scrubbed instance in `workshop/resources/research/risk-classes-beyond-security.md`, where cost accrued silently while effort continued. For the rule gate at a planning turn: parent is the below-line revisit's per-item check in plan.md. Improves odds only; the residual is stated in the research file.
Blocked by: [rests-on-line-at-decision-step]
The hold is design coherence rather than mechanics: what a re-check re-reads is cleanest if it is the "rests on" line the first candidate writes, so the gate should weigh them in order.

#### Build working file records what each item touched, so later items read that instead of re-reading [build-working-file-records-touches]
Filed 2026-08-30 while relocating the run-cost audit's findings to `workshop/resources/research/run-cost-measurements-2026-08-28.md`. The measurement behind it: a build run re-read files it had already opened 20 times in 417 calls, where a planning run did it 4 in 254 — the one navigation class where the session already had the content, which no transport change touches. The candidate design, deliberately not settled at filing: the build working file records which files each item touched and what changed there, so a later item in the same run consults that record before re-opening the file. Design questions for the keep: what the record carries (paths only, or a line about what changed), whether reading it actually beats re-reading for correctness (a stale summary misleading a build is worse than a re-read), and whether the win justifies the working file growing.

**Held 2026-08-31 behind the MCP umbrella, on Claude's recommendation and the user's agreement.** A touches-record is a computable state — a run's touches are its uncommitted changes, readable live from git, never stale — so a stored copy in the working file is the recorded-copy pattern the umbrella's purpose hypothesis proposes retiring. Whether the answer here is a stored record, a live git read, or an MCP tool is decided by that design; building the stored form now pre-empts it. Returns when the umbrella resolves; the chain terminates ([recorded-states-inventory] → [mcp-server-standing-intent] → this).
Blocked by: [mcp-server-standing-intent]

#### Tester prompt asks Claude for its own thinking, which a safeguard blocks and this project already rules against [tester-prompt-asks-for-reasoning]
**Reported by the beta tester to the user, 2026-08-30**, with a screenshot. He ran the prompt she gave him in a second chat and it was refused outright:

```
Request was blocked — Opus 5's safeguards flagged this message.
Details: `[reasoning_extraction]`
```

The prompt asks for "full transcript of this chat including thinking processes and my replies as test data", then to check Outlook is connected, prepare them and attach them to a draft email. The same prompt had worked in his earlier chat, which is what makes this worth filing rather than shrugging at: **it is not reliably refused, so a tester meets it at random** and has no way to tell a safeguard from a broken instruction.

**Two independent reasons the thinking-processes half should come out, and the second is ours.** The safeguard is the visible one. The other is that this project's own CLAUDE.md already says how to read a session: source the raw `.jsonl` from `.claude/projects/<project-slug>/`, because a regenerated transcript is a lossy reconstruction and hits the handoff-provenance problem — Claude-authored content read as the user's own words. Asking Claude to write out the conversation is the route that section exists to rule out, and the tester's own covering email says as much unprompted: his record is a reconstruction, his replies paraphrased except one quoted line, with no internal reasoning in it because Claude cannot retrieve its own thinking as text.

**So the fix is to change what testers are asked to send, not to work around the block.** The raw `.jsonl` is a file he can attach directly, it is the primary evidence, and it needs no cooperation from the model at all. What the processing turn settles: the replacement wording, where it lives so it is handed out consistently rather than retyped each time, and whether it belongs with [recording-priming-prompt] as a second standing prompt or somewhere of its own.

**Not verified from here:** what exactly trips `[reasoning_extraction]`, or whether the Outlook-and-draft half of the prompt contributes. Two runs of one prompt, one blocked and one not, is not enough to say which clause did it — and the fix above does not depend on knowing.

Filed by Claude from the user's report. Test data from the first beginner tester; the session records themselves are [beta-test-session-records].

#### Standing instructions for a beta tester sending session data, replacing the blocked prompt [tester-data-collection-instructions]
**On the user's ask, 2026-08-30**, so the wording lives somewhere rather than only in a chat. It replaces the prompt that produced [tester-prompt-asks-for-reasoning]'s refusal, and both were revised again the same hour after the tester's screenshots showed the first version's file-finding step failing.

**Three changes from the original prompt, each from an observed failure.** The request for "thinking processes" comes out — it triggers a `[reasoning_extraction]` refusal and asks for content nothing can retrieve. The request for a "full transcript" comes out, replaced by attaching the `.jsonl` the app already saves — the original produced a rewrite of the session with the tester's replies paraphrased. And the email step splits into its own message, because the old prompt bundled the two and one refusal cost both.

**The end-of-session prompt:**

> I'm a beta tester for Throughliner and my session data is being collected as test data.
>
> Claude Code saves each session's conversation as a .jsonl file under %USERPROFILE%\.claude\projects, in a folder named after this project's path. Please find the file for THIS session — the most recently modified .jsonl in that folder — and tell me its full path.
>
> Then write a short plain-English record of this session: what I was trying to do, what happened, anything that went wrong or confused me, and anything that worked well. Base it only on our conversation. Don't try to include your own reasoning — that isn't retrievable, and asking for it gets the request blocked.

**The email prompt, sent separately once the first is done:**

> Please check my Outlook connection is working, then start a draft email to <address> with the session file attached and the session record in the body. Subject: Throughliner beta test — session record, <today's date>. Leave it as a draft; I'll read it and send it myself.

**The manual fallback, and the correction that matters.** Where the tester finds the file himself, the step must say: **that folder holds sub-folders as well as files, and only the files matter** — sort by Type, take everything whose type is JSONL, and ignore every folder. The first version said "inside are one or more .jsonl files", and the tester opened the sub-folders instead and reported dead ends, because the `.jsonl` names are session ids and read as unopenable to anyone who does not know that. **Simplest instruction of all, and the one to prefer: attach every `.jsonl` in the folder.** They run a few hundred KB each, and which session is which is answerable at this end by reading them.

**Filed rather than fixed here:** whether any of this should ship. Throughliner already has a report route for "I think this is broken", and this manual collection exists to get richer data than that route returns while the tester is new. The user's framing, sent to him the same day: the setup process was truly broken and there is a gold mine here, but reporting will not normally look like this.

#### Welcome re-bump cannot replace a welcome the user wrote, so the channel ends up with two [rebump-welcome-cannot-replace-a-user-post]
Found live 2026-08-30 by /next, posting the 1.21.1-test1 entry. Filed by Claude.

**What the flag does.** `--rebump-welcome` on the posting script deletes the bot's previous copy of the welcome and reposts it, so the welcome always sits newest in the channel — the thing a tester should read before installing anything.

**What happened.** It reported `no previous copy found` and posted a fresh welcome as `1543588493400350823`. The standing welcome in that channel is the **user's own post** from 2026-08-26, and a bot cannot delete a user's message. So the flag did half its job: the newest message is now a bot-authored welcome, and hers is still sitting above the entry. The channel shows the welcome twice.

**It is the [howto-posts-bot-authorship] constraint again, in a channel nobody had considered.** Every automated maintenance move this project builds runs into the same wall — a bot can only edit or delete what it wrote — and the wall is only visible once the move is run against something the user authored.

**Two things to settle, and they are separable.**
- The channel now: whether the user deletes her original, leaving the bot's copy standing and editable from here on (which is the re-homing outcome, arrived at by accident), or the bot's new copy is deleted and hers left as the only welcome, which returns the channel to its previous state and leaves the welcome un-bumpable.
- The flag itself: it currently reports `no previous copy found`, which is true and reads as "nothing to do". A run that has just created a duplicate should **say so** — the script can see that a non-bot message matches the welcome text, and reporting that costs one line and is the difference between a silent duplicate and a visible one.

**Not proposed here: having the flag refuse.** It did what it was asked and the post is genuinely bumped; a refusal would leave the channel with a stale welcome instead of a duplicated one, which is worse.

**Scope note.** This affects any channel whose standing pinned or welcome post the user wrote, so it is not confined to the nerds channel. Nothing has been surveyed to find the others.

#### SPEC facts nobody sourced go unchecked — the tester's spec-sync pass proved it [spec-facts-unsourced]
Split out 2026-08-30 while processing [setup-infers-a-name-into-spec], on the user's agreement, because it is a far bigger design than the never-infer fix that shipped there.

The tester's observation, and it matches what the check does: his session's spec-sync gate ran and passed clean over a SPEC carrying a name that was never true, because the gate tests whether SPEC agrees with what was built — not whether what SPEC says was ever sourced from the user. A fact written into SPEC by inference reads identically to one the user gave, forever.

For processing: whether any mechanism should distinguish user-sourced product truth from derived statements, and what it would cost — a provenance convention inside SPEC prose, a setup-time read-back of everything scaffolded, or nothing beyond the never-infer rule now that the known entry route is closed. The last is a live option: with inference removed at setup and builds barred from writing product truth, the remaining routes for an unsourced fact are few, and a checking mechanism may be machinery without a failure left to catch.

#### Setup could ask whether this is the user's first time, which the install routes were assumed to answer and do not [setup-asks-if-first-time]
**Raised by the beta tester, 2026-08-30**, and passed on by the user with her own diagnosis attached — the diagnosis is the part worth keeping.

**The suggestion.** During setup, ask the user whether this is their first time running Throughliner.

**Why it is not already covered, in the user's words:** *"I honestly imagined the two install routes covering that."* They do not, and the reason is that they sort by a different question. The two routes ask **whether you already have Claude Code**; the tester's question asks **whether you have used this method before**. Someone can have Claude Code installed for months and have never seen a queue, which is exactly the tester's case.

**The hole was exposed by how it was used rather than by reasoning about it.** She walked him down the already-have-Claude-Code route expecting her own guidance alongside it to make up the difference for a beginner, and it did not. That is worth recording precisely because the route choice looked like it carried experience level and does not — a signal read as something it never encoded.

**It has a second instance in the same session, which is the argument for doing something rather than noting it.** The session's worst moment was being told to type `/clear` and then do a second thing: `/clear` wiped the screen before the second instruction could be read, and nothing had said what `/clear` does. That is guidance written for someone who already knows the tool, handed to someone who did not. A first-time answer is exactly what would let that instruction be written differently.

**What the processing turn has to settle, and it is the hard half.** What actually changes on a yes. An answer that only softens tone buys nothing; an answer that gates real behaviour — explaining a destructive command before asking for it, not bundling two instructions where the first destroys the second, pacing the interview differently — is worth a question, and each of those is a candidate rule rather than a decided one. **A sixth interview question is not free**, and setup's question count has been kept deliberately low, so the case has to be made on what the answer changes.

**Related, and worth reading together:** [setup-infers-a-name-into-spec] is the other setup finding from the same session, and both share a shape — setup assuming something about the person rather than asking.

**Skipped 2026-08-31 on Claude's recommendation and the user's agreement, held behind the transcript audit.** The design progress worth keeping: the two concrete failures behind the suggestion look better fixed unconditionally — the `/clear` bundling is bad guidance for anyone, and the name inference is already being removed with no question asked — so if every fix turns out unconditional, the right answer is no new interview question at all. Whether anything genuinely should fork on experience level is what [beta-test-session-records]'s nine observations will show; this returns by itself once that audit's findings exist to design against.
Blocked by: [beta-test-session-records]

Test data from the first beginner tester; the session record, its nine observations and the raw transcripts are all [beta-test-session-records].

#### Provenance survives correspondence: sent reports carry whose idea each thing was, and received reports' origin claims are preserved [correspondence-preserves-provenance]
**Raised by you, 2026-08-31**, while correcting exactly this failure live: the per-turn content proposal now built into [per-turn-content-rules] is yours, but the two inbound INBOX reports carrying it had anonymised the proposer to "their user", so it arrived here creditless and was nearly recorded as another project's user's idea until you said so.

The two halves, yours with the received-side extension raised in the same breath: outbound mail and reports apply the provenance rules (origin claims, quote claims, the containment test) to their own text rather than flattening everyone into "the user"; and a receiving project's triage carries an inbound message's origin claims into the capture it files instead of paraphrasing them away. Tension to settle at processing: the scrub checklist pushes the other way — names come out of committed documents — so the design has to say how an origin claim travels without a name (e.g. "the project owner's own proposal" versus a bare "their user"), and what changes in `docs/feedback-and-inbox.md`'s report format and triage. Rule gate applies; this instance is the recorded failure.

#### [audit] Compliance audit of the rule-bearing commits since the last audit record [compliance-audit-lag]
Filed 2026-08-31 by the rule-corpus checks at a planning session, which found 2 rule-bearing commit(s) since `2026-08-29-compliance-audit-lag-build.md` uncovered. Delta scope, the changed files as the check printed them: `CLAUDE.md`, `plugin/throughliner/docs/done-audit.md`, `done-build.md`, `done.md`, `feedback-and-inbox.md`, `migrate-checklist.md`, `next-audit.md`, `next.md`. Criteria: `workshop/resources/method-compliance-audit-checklist.md`. Satisfied while this item stays open; the check re-arms when it is deleted.

#### MCP server for Throughliner: the standing intention, kept whole while its pieces are measured [mcp-server-standing-intent]
**Your standing want, 2026-08-31 — "the biggest thing on my mind" — filed so it stops depending on your memory.** The trail so far, kept so the whole is visible: your build brief for a local MCP server shipped inside the plugin (2026-08-29) could not pass buildability as a build and became [run-token-cost-audit]; that audit measured where a run's tokens go (`workshop/resources/research/run-cost-measurements-2026-08-28.md`) and found the fixed read cost dwarfs what MCP tools could save, with half the proposed tool table already existing as scripts; its findings became narrow captures ([build-working-file-records-touches] survives in Unprocessed). The research-validity entry of 2026-08-30 records your own instance that MCP was never ruled out — the measurements bound what it saves on file work, and say nothing about other grounds: tool-shaped access for consumers, ports, or capabilities scripts cannot offer. For processing: what MCP would be *for* now that the token argument is measured, and whether a design item can be scoped — this capture is the umbrella and stays open until the question is genuinely settled or you close it.

**Your portability concern, raised and part-answered 2026-08-31.** Your first and largest concern: an MCP server makes Throughliner less portable to the harnesses people are porting to now. Checked the same day against the two live ports in the showcase (`workshop/resources/research/port-harness-mcp-support.md`): OpenCode and Kilo Code both run local stdio MCP servers natively through their own config — unlike the hooks, which every port re-maps by hand — so for the ports that exist, MCP is more portable than the plugin's current enforcement layer, not less. What the check does not settle, kept live on this item: whether the port authors want the component, how each harness's tool permissions compare to the approval rules' assumptions, and the philosophy cost — a porter can currently read everything, and a running component raises that floor.

**A first concrete purpose, 2026-08-31, mixed authorship written as mixed.** Your guess, raised in discussion: the states recorded as true or false in the docs won't be necessary anymore. Claude's analysis of it, which you agreed to file: the states split two ways, and the split scopes what MCP may touch. Computable states — host currency, cycle due-ness, blocker shipped-ness, item age — are already recomputed from observables rather than stored, and MCP's offer is making them live answers so recorded copies that can rot never need to exist; those copies could go. Decision states — a flag's cleared/uncleared, kept-or-deleted, recorded consent — are not computable by any tool, because they record the user deciding, and that written trail is the product itself. So the candidate purpose: MCP retires the recorded copies of computable states and must not touch the decision trail.

**A second purpose, yours, 2026-08-31, and you scoped it to cycles in the same breath:** a cycle's material lined up as a succession — the tips pool being the live example — where each entry's posting day is computed from the cycle's cadence and its position in the line, recomputed whenever one is slotted in the middle or deleted, rather than a `Not before:` date hand-written on each and hand-shuffled when the line changes. The instance that prompted it: two post drafts each carrying a stored date, both edited by hand today to apply the one-post-a-day rule. Your scoping: such a run of things is governed by a cycle — this is cycle machinery, not a general queue feature. Fits the computable-states purpose above: a stored date on cycle material is a recorded copy of cadence-times-position.

**A third instance, raised by you 2026-08-31: the checkpoint counts.** You watched "ready to build" hover then dip across turns and asked whether MCP could make it more consistent. The dips were real changes, but the number reaches you by Claude deriving it from the digest and the mover's reports, which goes stale or gets dropped late in a session — [checkpoint-counts-drop-mid-session] records exactly that, and its own diagnosis names the derivation cost as why the counts slip. The count is a computable state: under MCP the checkpoint asks a tool and gets the live figure, rather than remembering.

**A fourth purpose, yours, 2026-08-31: the staged next turn.** The gap between a recommendation and its execution annoys you every time, but you can never bundle the two, because the user might run the close — or anything else — in that gap, and the gap is also what lets them. Your design sketch: with MCP, the next turn's write is prepared while the ask waits, and released practically instantly on the yes — the thirty-odd times a session that happens — while the gap stays open for whoever wants to do something else in it. Your own cost accounting, accepted at raising: one or two staged writes dropped per session when the answer is not yes — no big deal.

**A fifth purpose, 2026-08-31, from processing [build-ticks-omit-the-confirmed-form] — structured writes.** Today every format the hooks parse after the fact — tick forms, markers, state lines — is free text the model writes by copying a specimen, so a wrong form is possible and is caught downstream or not at all; the 22-tick run is the instance. As tool calls, each format's required fields are validated at the moment of writing, so the wrong form is refused rather than corrected. Distinct from the computable-states purpose: that one retires stored copies of facts, this one guards the writes that remain. **Second instance, same day, from Chagora's defect report:** an unbracketed `Blocked by:` slug made an item permanently unliftable with nothing reporting it ([unbracketed-blocker-invisible], whose two-guard file-era fix is cleared) — as a tool call, the hold would take the blocker as a parameter, verify it resolves to a real entry at write time, and emit the canonical form itself, so the malformed line and the dangling reference are both refused at the door.

**Held 2026-08-31 behind its ground truth:** [recorded-states-inventory] is the cleared audit that produces the inventory this design needs; this capture returns by itself when that records complete.
Blocked by: [recorded-states-inventory]

#### Project CLAUDE.md has no plugin-managed block — add it, or record staying hand-written [claude-md-missing-managed-block]
Found 2026-08-31 by the epoch-5 migration's managed-block refresh step, which compares the region between the PLUGIN-MANAGED markers against the shipped template and found no markers at all: this project's CLAUDE.md is entirely hand-written, so nothing in it is refreshed automatically as the method evolves. The migration reported and edited nothing, per its own rule — the file is the user's. Filed by /rescan after the finding lived only in chat.

The decision this reveals, the user's to make at a processing turn: append the template's managed block (gaining the self-updating description of the queue model and working rhythm, at the cost of duplicating ground the hand-written file already covers in its own words), or record deliberately staying hand-written — in which case the standing risk is the known one, that descriptions of the method in this file go stale with nobody's job to refresh them, and the retired-terms read at each migration is the only check that reaches it.

#### [audit] First maintenance-sweep turn — the corpus against the compliance checklist [maintenance-sweep]
Filed 2026-08-31 by /rescan: the [maintenance-sweep] cycle was authored today with no completed turn on record, so it is due from birth, and nothing had filed its first turn. The turn, per the definition in CYCLES.md: one audit pass over the rule corpus — the always-loaded files, the procedure docs under `plugin/throughliner/docs/`, and the shipped templates — against `workshop/resources/method-compliance-audit-checklist.md` as written on the day of the turn, proposing no lens of its own. Until [checklist-gains-sweep-lenses] ships, that is the checklist's existing four lenses, and the turn says so. Findings filed as captures, one per discrete observation; the turn recorded in `LOG/` under this slug, the record opening by saying it records a completed turn of this cycle. Satisfied while this capture is open. (No `Cycle:` field, deliberately — that field marks a cycle's standing material the ladder passes over; a due-turn capture ranks like any other work, as the tips turn did today.)

