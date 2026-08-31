# CLAUDE.md — Throughliner

Claude Code auto-loads this file on session start.

## The two-section model is what main runs

Main carries the two-section work-line model — Processed / Unprocessed, build and `[audit]` flavors with `[user]` walk-through and `[freeform]` for work /next must not run, red flags as tagged state-carrying lines. It arrived by merging the `queue-redesign` fork (LOG `execute-merge-to-main.md`), keeping main's plugin identity (then `sovereign-implementer` / `flintcraft`, now `throughliner` / `flintcraft`); the founding decision is in QUEUE.md's history under `[adopt-queue-redesign]` and LOG `fable-goal-queue-drain-adopt.md`. The rollout that section used to describe as pending is done: the merged plugin has shipped, been released, and is what the other projects run.

## What this is

Throughliner — a Claude Code plugin that gives non-coders a structured workflow for building apps with Claude Code. Renamed from "Sovereign Implementer" on 2026-08-13; the plugin slug, the package folder, both project marker files and the positioning all moved together in one build.

**Who it's for.** Non-coders who know what their app should do but need a framework to keep Claude aligned.
**Core tension it solves.** Non-coders need heavy docs to keep Claude on track, but heavy docs burn context window. The plugin balances this: hooks enforce mechanically (cheap), skills load procedures on demand (only when needed).

## Audience

The plugin's users are external non-coders building their own apps with Claude Code — not the person developing the plugin. This project is the unusual case: the developer (Alex) is also a non-coder using the plugin to build the plugin. Skill docs must be written for the external user, not for Alex.

Concretely: anything a skill causes Claude to *say to the user* — chat narration, drafts, prompts, headings, status lines, error messages — must read cleanly for an external non-coder. No internal procedure terms (e.g. "skill-nonspecific-rules.md," "the [SILENT] tag," "Step 2.4," "Pass B," "trickle-up"). Internal terms belong inside procedure docs where Claude reads them; they must not leak into output the user sees.

When editing any skill doc, check the output-facing strings against this audience before saving.

**A request describing a behaviour is complete with no filename** — locate the part it lives in and name it in the answer; when the user asks about the method's parts or where something is decided, read [`workshop/resources/method-map.md`](workshop/resources/method-map.md) and answer from it.

**This project's narration is not evidence the method's communication rules work.** Two layers assert them here — Alex's global `~/.claude/CLAUDE.md` and the method's own always-loaded rules (a shipped output style was a third until it was deleted on 2026-08-14) — so correct behaviour in this project may be coming from a layer consumers do not have. Which rules are doubled, and by which layers, is enumerated in [`workshop/resources/method-compliance-audit-checklist.md`](workshop/resources/method-compliance-audit-checklist.md).

## Model target

**The method runs on one docset, and no model detection.** `plugin/throughliner/docs/` is it. There is nothing to pick between, so nothing picks: session_start carries no docset logic and no model logic, and the skills point straight at `docs/`.

The docset serves the **5-series — Fable 5 and Opus 5** — which converge on wanting less prescription rather than more. It was authored by *subtraction* from the older, heavier docset A — now retired, see below — and it is lighter for that reason: A over-explained because Opus 4.8 needed a rule's why to travel with it to follow the rule reliably, and the 5-series does not.

**Docset A is retired (2026-08-09), and 4.8 is no longer a supported target.** The two-docset design existed for one reason — a no-strand guarantee, so a bad migration to the new docset could never leave the project with no working plugin. That reason expired when both 5-series models proved out on B. A was retired once already on 2026-08-08; the emergency revert of 2026-08-09 brought it back, and this build re-applies the decision rather than making a new one. Its 4.8 steering research stays on file as history, not as a live target: `workshop/resources/research/opus-4-8-verbosity-steering.md`, `workshop/resources/research/model-instruction-compliance.md`.

**Why one docset and not N — the fork this closes for good.** The intuitive worry was one docset per model, which drifts under dual maintenance. It never got that far, because Opus 5 is not "as fussy as 4.8" — it is fussy the *opposite* way: it over-does (self-verifies, expands scope, runs verbose), so Anthropic's guidance for it is *subtraction*, and Fable 5 wants the same. Both 5-series models therefore converge on one lighter docset. With A gone the sync burden is not merely dodged but absent. Research: `workshop/resources/research/opus-5-instruction-compliance.md`, `fable-5-instruction-compatibility.md`.

**Authoring register.** Author by subtraction, in the docset's lighter register. A future model is adopted when it arrives; the retired docset is history, not somewhere to regress to — we do not reach for an older model or an older register to dodge a newer model's behaviour.

**The frontmatter stamp on each `docs/` file reads `docset: current`, renamed from `docset: B` on 2026-08-16.** The stamp itself stays and must: session_start's behaviour-rules redirect self-checks against it, so it is the one guard proving the always-loaded rules reached the session at all. What changed is only the value, which used to name a sibling that no longer exists — a self-check asserts a new value exactly as well as an old one.

**The folder was renamed from `docs-b/` to `docs/` on 2026-08-21.** Session records, archived INBOX messages and `workshop/resources/plugin-behaviour-retired.md` still name the old path, and correctly so: an entry written before that date records what the folder was called at the time. Dated findings under `workshop/resources/research/` keep it too, because they quote file-and-line as evidence.

## Host and target

**Host** = the plugin as installed in the desktop app. Its hooks fire, its skills are available, its procedures govern sessions. Nothing in this repo changes host behaviour — only a `claude` CLI install/update against the committed marketplace plus a full app restart does (the desktop app's in-app plugin upload is gone; the exact commands are in the Push section below and in `workshop/resources/release-ritual.md`). A bare working-tree or zip edit changes nothing the host sees, because the host runs a frozen snapshot the CLI copied into `~/.claude/plugins/cache/...` at install time, not the live files. **The rezip builds every zip and the release only copies one.** The install itself uses no zip — the local marketplace sources the folder and the CLI snapshots it directly — but immediately after the install, once the stamps are proved equal, the **rezip** zips `plugin/throughliner/` into `plugin/rezip-archive/` with a readme carrying that build's label, `Commit:` line and version. A **release** then copies the picked build's archived zip to `plugin/throughliner.zip` and attaches it to the GitHub Release; it runs no `Compress-Archive` of its own.

**That ordering is the point rather than a detail.** A zip built at release time is a zip of whatever the working tree has become since the build was tested, so the release could ship bytes nobody had run. Building it at the one moment the folder is provably the installed build closes that, and it makes the label-to-commit lookup a local file read instead of a person reading Discord.

**So the word "rezip" is literally true, and this is the full truth so it stops misleading:** the archive is a 15-entry local mirror of the test-rezips-for-nerds channel — one zip and one readme per build, the readme being the channel post's own text — pruned to 15 as the channel is. The folder is gitignored: every archived build is rebuildable byte-for-byte from its `Commit:` line, so committing the zips would store what git already holds. `plugin/release-zip-archive/` is retired and deleted, GitHub Releases keeping every release's zip. **Renaming the word was refused:** the channel name keeps it public, and docs saying "refresh" against a channel saying "rezips" would mislead more, not less.
**Target** = the editable source at `plugin/throughliner/`. This is what sessions build and edit. Target changes have no effect until packaged and installed as the new host.

Host and target are the same plugin at different stages. Ambiguous references to "the plugin," "the hooks," "the procedures," etc. must specify host or target. **Default assumption: discussion is about the target unless the user says otherwise.** Most target changes become host changes automatically on reinstall. Changes that live outside the plugin package (e.g. project doc structure, this CLAUDE.md) won't propagate through reinstall and need manual updates.

## Architecture

**3 project docs** (created by `/setup` in consumer projects):
- `SPEC.md` — product truth. What the app is, who it's for, how it works.
- `QUEUE.md` — two sections (Processed / Unprocessed), each holding work lines as `#### ` headings with rationale beneath. A work line that carries a security or privacy risk gets a red-flag marker (a `Red flag · State:` tag) — the flag rides the work, not the other way around.
- `LOG/` — per-session records. `LOG/index.md` for summaries (newest first), one file per session entry. Legacy entries from before the per-entry split remain in `LOG/log.md` and `LOG/log-v*.md`.

**5 skills:**
- `/setup` — scaffold docs + ask 5 questions to populate SPEC.md.
- `/plan` — all thinking work: queue management, read-back, ideas, questions, drift detection.
- `/next` — pick the top ready work, execute it (build or audit), walk the user through `[user]` items. Works the cleared region top-down, so one invocation can build several cleared items back-to-back — the unattended-in-practice runner, closed by /done.
- `/rescan` — look back over the conversation for anything decided, noticed or asked for that was never written into a file, and file it. Routed by the standard triage: work still to do goes to the queue, work that already happened is appended to this session's record as a marked tail. Commits nothing, and can be run repeatedly — it scans back only as far as the last /rescan.
- `/done` — record what happened, clean up, commit.

**4 hooks** — three enforcing, one advisory:
- `session_start` (enforcing) — detect project state (unadopted / adopted / active build), load behaviour rules, check plugin version against .throughliner-version.
- `pre_tool_use` (enforcing) — scope-lock to the active run's file list (which governs SPEC.md like any other file — SPEC is editable only by a run whose work items list it), git safety.
- `stop` (enforcing) — check Claude's finished response for a report naming a capture as filed, and confirm that entry is actually in the queue, or already on record as built work. Where it isn't, the turn is fed back so the write can be made before the user acts on a report of work that doesn't exist. Blocks once per claim, then stops blocking.
- `post_tool_use` (advisory) — QUEUE.md structure lint; flags format drift after a QUEUE.md edit, never blocks.

## Where things live

```
No code method/
  CLAUDE.md              — this file
  .gitignore
  plugin/                — plugin packaging
    throughliner.zip     — the zip a RELEASE builds and attaches (not the rezip)
    rezip-archive/       — each rezip's zip + readme, newest 15, gitignored
    throughliner/        — target source
      .claude-plugin/    — plugin manifest
      hooks/             — session_start, pre_tool_use, stop, post_tool_use
      skills/            — setup, plan, next, rescan, done
      templates/         — CLAUDE-TEMPLATE.md
      docs/            — procedure docs loaded by skills (the one docset)
  SPEC.md                — this project's spec (once /setup has run)
  QUEUE.md               — this project's work queue
  LOG/                   — this project's session logs (index.md + per-entry files)
```

## Working conventions

- **Use absolute paths** for sub-folder lookups. `<PROJECT_ROOT>\plugin\throughliner\...` — substitute `<PROJECT_ROOT>` with the absolute path to this project's folder on your machine.
- **Cross-doc references go by name.** When editing the docs under `plugin/throughliner/`, a reference to a step in another doc names its target ("the blocker gate in next.md's pre-flight"), never a step number. Step numbers silently retarget when a build adds, deletes, or reorders steps — the reference still resolves, but to the wrong content; names survive renumbering. Within-doc references are exempt: renumbering is visible in the file being edited.
- **Judge a design by whether it makes the intended outcome more likely, not by whether it guarantees it.** A missing guarantee is an objection only where the design depends on that guarantee to work at all. It fires at /plan's decision step, when weighing whether work is worth doing.

  **The carve-out, which ships with the rule because without it the rule strips the honest limits.** Statements like "this scan matches credential shapes only" or "this flag reaches only items that name the file" describe what a mechanism covers once built, and exist so the tool never over-claims. **The test: is the caveat arguing against doing something, or describing what the thing does?** The first is the failure; the second is required.

  **The failure evidence is one instance, and no more is claimed.** A planning turn offered "shortening the artifacts may not by itself restore the reading" as a reason to hold work apart, when the work made reading affordable and never depended on the reading happening. The user's words settling it: *"any caveats like that can't 100% control how it works or else what would we be left with?"* A corpus-wide audit for the same pattern was searched for and withdrawn — the other instances checked turned out to be refusals on cry-wolf or unapproved-send grounds, which are different arguments and still valid.
- **The rule gate — run this before adding any rule to the method's own text.** Four parts in use order: admission, eviction, distribution, wording. Every rule admitted degrades the rules already there — irrelevant and near-identical rules are optimal distractors for one another — so the cost is relevance, not a count. **No ceiling is stated and none may be invented.** Host-only: consumers never author method rules.

**1. Admission — does this rule get to exist?**

**First, name the parent: which existing rule does this amend?** An amendment competes with nothing; a freestanding rule competes with everything. A change that cannot name a parent is either new territory or, far more often, a refinement whose parent was never looked for.

**Then write it as a subordinate unit of that parent, and ship it in that form if it holds.** Freestanding is the fallback, not the default. Genuinely subordinate when all hold: at least two parallel units exist; each reads as a continuation of the parent's opening words; all share one grammatical function; every modifier points only at the opening words or at its own unit; none is a complete sentence. A complete sentence formatted as a nested bullet is a freestanding rule wearing a bullet, and spends a slot accordingly.

Then four questions:

1. Has this actually failed, in a way you can point to? A speculative rule stops here.
2. Does Claude already do it unprompted?
3. Does it apply to every session, or only some?
4. Could a hook do it instead, at no attention cost? Escalate to a hook when the failure's cost justifies its standing friction — a cheap, self-correcting slip earns sharper wording instead.

**A limit the method's text declares states what it was derived from.** A proportion of the thing it governs, a figure from research, or an externally imposed constraint each qualify; a bare number does not. A stated derivation makes a limit traceable and revisable — it does not make it correct.

**An exception must survive the restatement test.** Before writing one, restate the rule so that it does not need one; an exception is admissible only where restatement was attempted and lost content. Where restatement genuinely fails, the exception requires a recorded instance of the bare rule producing a wrong outcome — not the author's belief that an edge case exists — and the LOG entry admitting it cites that instance.

**2. Eviction — name what comes out.** Adding a rule names which rule it replaces or supersedes, and repeals it in the same move. A clearer restatement that leaves the old statement standing has doubled the text, not merged it. **Adding a scan to a skill's opening states what it displaces** — each scan is small and individually tagged, so nothing anywhere counts them. **Retiring a step retires the artifacts that step produced — name them and delete them in the same build**, and where a live doc describes the retired step's output, reword that too. This fires only when someone is knowingly retiring a step; it does nothing about junk that accumulates from nobody's decision in particular. The techniques for taking a rule out live in [`workshop/resources/rule-maintenance.md`](workshop/resources/rule-maintenance.md), opened during a subtraction pass rather than while authoring.

**3. Distribution — always-loaded, or fetched?** A session cannot fetch a rule it has never read, so a rule that must shape behaviour unprompted is always-loaded and pays the full admission cost. Reference material a session knows to go looking for can be fetched. The always-loaded shipped file is `docs/skill-nonspecific-rules.md`, and its name is its admission test: a rule belongs there only if it fires in all four skills, or in conversation with no skill running. That last limb is a fifth condition rather than a loosening — it admits a rule that is *wider* than any skill, which the bare four-skills test rejected for the same answer it gives a rule that is too narrow.

**4. Wording — state the action the rule requires.** An always-loaded rule statement is written in one of three shapes: a bullet, a paragraph whose bold leads the line, or a line inside a typed block. A rule written in any other shape — plain prose, or bold placed anywhere but the start of the line — is a defect at authoring time, corrected where it is written. The three shapes are the ones `workshop/resources/rule_signals.py` can see, so a rule outside them is invisible to the growth report and to the contradiction check alike; widening the pattern is not an available fix, because a rule stated as an ordinary sentence mid-paragraph is indistinguishable from explanation by any mechanical test. Anything described in terms of what *not* to do means the rule of what TO do was never adequately described; a prohibition is a signal to go back and specify the action. Express a qualification as structure, not explanation: state the rule bare with the qualification in structure; main clause first, conditions after; `subject to <X>` as a cross-reference rather than a restatement; multiple exceptions in their own subsection; short connectives (but, except that, unless, so long as) rather than explanations; one idea per provision; every exception at the same level as the rule it qualifies.

**Rationale lives outside the operative rule.** The operative statement stays bare. **Why a rule is worded as it is** — which alternative lost, what the trade-off was — goes to the LOG entry that decided it. **Decision history is rationale under this rule** — a date, a "was tried and retired", an alternative's defeat narrated in rule syntax — detected by the existing delete-and-read test, with no "because" required, and belonging to the record like any other why. An evicted why does not have to land anywhere: git history keeps it, and anything still needing a decision becomes a capture. **The FAQ is never an eviction destination** — an FAQ entry is written because a user would ask that question, never because a rule shed some prose.

**Where a reason is needed to apply the rule, reclassify it — don't exempt it.** If a rule cannot be applied correctly without a sentence, that sentence is part of the rule and is written as operative text. Three parts, in this order: it earns its place only where there is a recorded instance of the rule being misapplied without it; once admitted, write it into the operative sentence so it cannot be removed without leaving the rule incomplete; and the LOG entry admitting it cites the instance. The auditor's test is the same one in reverse — **delete the sentence and read what remains: a complete instruction means what you deleted was rationale, an unfinished one means it was operative.** Syntax protects a clause; it never admits one.

**The record behind these rules** — the repeal histories, the defeated proposals, and why each test is shaped as it is — is [`workshop/resources/self-authoring-rules.md`](workshop/resources/self-authoring-rules.md). Open it when something settled is about to be re-proposed, not while authoring.
- **The gate's site is /plan's decision step, and the disposition is written into the queue item there. /next TRANSCRIBES what the item already carries; the close transcribes it again into the LOG entry. Neither composes one.**

  **The disposition is /plan's and the rule TEXT is the build's, which is why the scope-lock's refusal to let a planning session edit this file is correct rather than a fourth oversight.** A planning session admits a rule and writes the disposition onto the queue item; the build that item schedules types the rule out. What the gate refuses is a build deciding whether a rule may exist — never a build writing one /plan already admitted. The question has been raised three times from three readings of the same standing list, so the answer is recorded here and in a comment beside the list itself.

  **A build that finds itself authoring a rule halts only where the item carries no disposition; where it carries one, the build transcribes it** — that is the one thing /next does with the gate beyond copying. The run reads the item whole, so a `Rule gate:` line written at the decision step is in front of it, and the halt is for a disposition that genuinely was never written.

  **When the gate fires at the decision step, say so in that item's message: what rule is proposed, which parent it amends, and what the gate decided.** One or two sentences folded into a message the user is already reading — never a turn of its own, which is the over-asking this method has spent months removing.

  **This introduces a party, not a field, which is the only thing that could answer the objection it comes from.** The user's words, 2026-08-13: *of what relevance is approval when you have literally never been asked.* Claude proposes the rule, runs the gate and writes the disposition; the one person with an independent view had never seen a gate decision at the moment it was made. A second required line written by the same author would not have changed that. Narration puts the decision in front of her while it can still be objected to.

  **State the limit wherever this is described: a narrated gate is Claude's decision announced, not the user's decision made.** It gives her a chance to object where she got none. It gives her no veto, and it does not make a dishonest disposition detectable — the same limit stated below about the two board checks. Do not describe it as giving the gate an independent approver.

  **Nothing is evicted for it.** The `--dispositions` listing at the /plan opening stays: narration reaches the sessions the user is in, and the listing still covers the ones she was not.

  **Why /plan and not the build, recorded because two earlier placements looked fine and were not.** A run once built thirteen items, several authoring or amending method rules, and wrote every disposition at the close in one sweep — after all the LOG entries existed, minutes before the commit. Each said `run — admitted` and each read plausibly. Not one was written before the rule it describes. That cannot perform admission; it can only describe. The give-away was in the artifacts: every disposition was favourable, nothing was rejected, nothing was evicted to make room, and one admitted a rule while recording that it passed the four-skills test "only weakly". **A gate that runs after the build has no power to refuse, because refusing would mean undoing finished work.**

  Moving it into the build working file fixed less than it appeared to. A disposition written as an item is built is still written after that item's rules were designed, so it improves attribution and restores no power to refuse. **Only /plan can refuse, because at /plan nothing has been built and refusing costs a conversation.** The planning session that settled this ran the gate about a dozen times and refused repeatedly and substantively — turning a proposed freestanding rule into an amendment costing no slot, refusing an exception outright on the restatement test against the source audit's explicit recommendation, and refusing three proposed evictions on recorded grounds.

  **The disposition therefore lives on the queue item, not in the build working file.** A planning session has no build working file, and the item is what /next reads, so a disposition on the item travels to the build automatically.

  The alternative — accept close-time dispositions as honest record-keeping and stop calling it a gate — was weighed and refused. It is the more honest of the two only if admission control is worth surrendering, and admission control is the thing this corpus most needs.

  **The honest limit, which none of this changes:** nothing can tell an honest disposition from a dishonest one. A /plan-sited gate can refuse, which a build-sited or close-sited one cannot. That is a real gain and it is the whole gain. Do not describe it as making the gate trustworthy.

- **A session that authored or amended a rule in the method's own text cannot close until its LOG entry carries a `Rule gate:` line.** The gate was run and what it decided, or it was not needed and why:

  ```
  Rule gate: run — <what it decided>
  Rule gate: not needed — <why>
  Retired: `<term>` — <what it was>        # only when this session retired something
  Retired artifacts: `<path>` — <what produced it>   # only when this session
                                           # retired a step that produced files
  ```

  **Write the label plain, not bolded.** `**Rule gate:**` is the ordinary Markdown instinct and it has twice hidden a whole session's dispositions from the board that reads them. The patterns in `workshop/resources/rule_signals.py` now tolerate the emphasis, but the plain form is what the specimen shows, so the instinct is corrected at the authoring end rather than only forgiven at the reading end.

  **This is the required-artifact shape (SPEC-sync's, and formerly FAQ-sync's) extended to a second subject, not a new obligation** — which is why it is authored as an amendment and consumes no slot. The shape is deliberate: a required artifact turns a silent omission into a visible one. "Not needed because X" is a claim a later reader can disagree with, and a missing line is a gap anyone can see. A pointer makes the gate visible; only this makes it produce evidence either way.

  **The trigger is mechanical** — a commit touching `plugin/throughliner/docs/`, `workshop/resources/self-authoring-rules.md`, `workshop/resources/rule-maintenance.md`, `workshop/resources/method-compliance-audit-checklist.md` or this file. It reaches files in this repository only, so a rule living outside it — a folder-level CLAUDE.md above the project — gets no gate, said plainly rather than implied covered. A judgment trigger ("is this change user-facing?") cannot be detected at all and has to ride a close-time read; this one is visible from git with no judgment involved.

  **It over-fires, and that is the design rather than a defect.** Touching `docs/` for a typo is not authoring a rule, but a false fire costs one line — "not needed, typo fix".

  **Nothing in the hooks or the shipped docs changes for this, and that is a finding rather than an omission.** The obligation lives in this always-loaded file, so both the build and the close read it without any change to `docs/`. Consumers never author method rules, so shipping it would put a rule in front of people it can never fire for. The disposition rides the queue item, which every session may already write. `workshop/resources/rule_signals.py` is untouched too: BORN and CONTRADICTED read the LOG entry, and the LOG entry still carries the line. **Neither gains any ability to tell an honest disposition from a dishonest one, and this change must not be described as fixing that.**

  **What checks the disposition, and what nothing checks.** Two board signals read it, and only together. BORN checks the line *exists*. CONTRADICTED checks it isn't contradicted by its own commit: where a commit's always-loaded rule-statement count **rose** and its LOG entry says `not needed`, that is a contradiction between two artifacts that are supposed to agree, detectable with no judgment. A fall or no change is never a finding — an eviction pass owes no defence. **Neither can tell whether a gate recorded as `run` ran honestly**; a dishonest "run — considered and kept" defeats both completely. **The third reader is the user, and only where the gate was narrated at the decision step** — see the narration obligation above; that reaches her in the sessions she is in, and it is a chance to object rather than a check. Say so rather than letting the three read as full coverage: a check that over-claims makes the corpus look guarded when it is only partly guarded. Both mechanical checks are bounded by a baseline commit (`DISPOSITION_BASELINE` in `workshop/resources/rule_signals.py`), so neither reports work done before the obligation existed.

  **A `Retired artifacts:` line also appends its entry to `plugin/throughliner/retired-artifacts.md`, in the same move.** That shipped list is what carries the fact out of this repository: a retirement removes the code that writes an artifact, never the artifact from the consumer projects that already ran it, and every one of those keeps an orphan nothing produces and nothing reads. `session_start` reads the list and names any listed path still present — report only, never delete, consistent with the top-up being add-only. One clause on the existing close line rather than a second obligation, the way README-sync rides the SPEC-sync trigger. The authoring half stays host-only; the reading half ships, because the orphan sits in their projects.

  **The `Retired:` line rides the same disposition rather than being a second close obligation** — one line, one place, carrying both what the gate decided and what this session retired. It appends to `workshop/resources/retired-terms.md`, which is what lets the board report every rule still naming a retired mechanism.

  **Host-only by residence**, like the rules above it: consumers never author method rules and would be baffled by the obligation.
- **`workshop/resources/rule_signals.py` runs five firing checks and one measurement over the rule corpus, and a check that finds something files a capture rather than standing as a notice.** Run `py workshop/resources/rule_signals.py .`. It is for Claude, not for Alex: nothing here asks her to do anything, and its findings reach her as ordinary queue items like any other work.

  **Five can find something:** whether every rule-bearing commit carries a gate line; whether any commit says the gate was not needed while the always-loaded rule text grew; whether two rules say nearly the same thing; whether a live rule still names a retired mechanism; and whether rule-bearing commits since the most recent compliance-audit record remain unaudited — which files one `[audit]` capture scoped to the changed files.

  **One only measures and can never fire:** how much rule text there is. It lost its trigger when the rule-corpus ceiling was removed, and no replacement threshold is defensible — inventing one is the bare-number failure this project bans. The sweep-due measurement is deleted, superseded by the audit-lag check above.

  **What a clean result means, and this is the part that was wrong until 2026-08-14.** It means those four things were checked and nothing was found. It is **not** evidence that the rules are correct, that they fire, or that they made anything better — no check here asks any of those questions. The proof is on the record: on 2026-08-13 the checks ran clean while five real rule defects were found by conversation in the same session. Reporting that as health is the over-claiming this project's own standard forbids, so the output no longer does, and neither does this description.

  **The header counts only the five that can fire.** A denominator including the measurement invites the reading that six things are being watched when five are. Keep the classes separate as entries are added, so the count stays meaningful.

  **A third class sits behind a flag and is counted by neither: the dispositions listing.** `py workshop/resources/rule_signals.py . --dispositions` prints every `Rule gate:` line on record with its commit, its LOG entry and its outcome, bounded to entries since the most recent planning LOG entry; `--dispositions-all` prints the full history. Nothing is wrong when it prints, so it is neither a check nor a measurement, and it must stay out of the denominator.

  **Run it at a /plan opening, and surface one short line only where the window holds a refused proposal — silence otherwise.** The listing prints a refusal count for exactly this check. A planning close's LOG entry carries one required line either way — refusals surfaced, or none since last session — the required-artifact shape: a required artifact turns a silent omission into a visible one. The reason it is not on demand: a refusal leaves no scannable artifact at all — a kept item sits in the queue, a built item leaves a vanished item and a LOG entry named after its slug, and a refused proposal leaves one sentence inside one entry. Asked how she would know to ask for it, the user's answer settled it: **"how would I even know to demand it?"** — which is the siteless-check failure recorded five times here, walked into by the recommendation itself. The window is *since the last planning session* — a planning entry is found by its body fields, not its filename, since the per-entry split names planning records by slug — because it tracks the moment she actually looks, and it goes quiet by itself when nothing has been refused.

  **It reports what a disposition claims, and the guard is printed wherever it prints.** It cannot say whether a refusal was correct, and it cannot see a proposal dropped in conversation before any disposition was written. **It must NOT go in `plan.md`:** that ships, this script does not, and consumers never author method rules — a step there would be a check that can never fire for them.

  Nothing is stored; everything is recomputed from the artifacts every time, because a state file must be maintained and the first session that forgets makes the output lie.

  **A check that finds something files one capture in Unprocessed under the slug it prints, and then gets out of the way.** It does not escalate over time — that would need a bare number, which the gate now bans — and it does not go quiet on a standing finding, which would recreate the silent inaction the whole design exists to prevent. The work goes where all work goes, ordered by the ladder and counting toward the throughput floor, where ignoring it is visible in the queue. **A check counts as satisfied while an open capture with its slug already exists**, which is the guard against filing the same capture every session.

  **Independent checks rather than a positional cycle**, because a cycle put compression permanently downstream of machinery that never ran. Independent triggers can each fire whether or not any other ran, and can be built one at a time. **That argument is weaker than it looked, and the instruction never to re-propose the cycle is repealed** — these checks then had no trigger either, for their entire life, so nothing ran them and the reasoning that defeated the alternative applies to the winner with equal force. A later session may re-propose a cycle on its merits.
- **FAQ entries are authored at the announcement, not with the work item.** When a posted announcement's line is written into `INBOX/sent.md`, the FAQ entry answering what that announcement teaches is authored in the same turn — into `plugin/throughliner/templates/faq-template.md` with its `faq-index-template.md` index line, then both files re-copied into `FAQ/` (`FAQ/faq.md` and `FAQ/index.md` are a straight copy of the shipped template, and the template is canonical; `FAQ/` is kept because `session_start` points every session at `FAQ/index.md` exactly as it does for consumers). This supersedes and repeals the FAQ-sync close gate and the FAQ-entries-ride-work-items decision step rule, replacing their judgment trigger ("does this alter what a user does?") with an unmissable one — the sent-register line is already required to be written in the approval turn, so the entry rides a write that cannot be skipped silently. Post source material lives in `ANNOUNCEMENT-IDEAS.md` at the project root, a static seed archive holding the retired FAQ's entries — read for material, not written to. **Fetch rule:** open the FAQ when working out how the plugin behaves on the user's side — neither always nor never; it is the record of what has been announced. Host-project rule — consumers never author FAQ entries.
- **README feature-list sync rides the SPEC-sync trigger.** A change that adds or removes a user-facing feature — a skill, a mode, a command, or user-visible hook behaviour — already must update SPEC.md. That same moment also syncs README.md's "What it does" feature list, which is the plain-English mirror of SPEC's feature list. One more clause on the existing trigger, not a new detection point. Host-only concern: consumers don't maintain the method's README.
- **A close whose staged paths include `plugin/throughliner/hooks/` runs the suites under `workshop/resources/testing/` before committing, and halts on any failure.** Read the trigger from `git status`, so it needs no judgment and fires only on the sessions that could have broken a hook. Where a suite fails, say in plain words which assertion failed and what it expected, and do not commit until it passes or the user decides otherwise.

  **Run them as plain scripts, never through `pytest`** — see the scripting constraints below for why that matters on this machine.

  **Verify a hook change by driving the new code directly — the suites, or `py` against the target file.** Never by performing the guarded action in the live project. The unsafe form is stated as its consequence rather than as a prohibition: performing it here exercises the **installed host**, which is the old code, so the guard never fires and the action completes for real. Every other statement of host-versus-target asks whether a change is *live*; this is a session choosing to **exercise** the change to confirm it, which turns passive staleness into an active write against the old, unguarded behaviour. The instance: a run had just built the guard refusing a Write onto an existing `LOG/` entry, performed that write to watch the guard refuse it, and overwrote a committed session record — recovered whole with `git checkout HEAD --`, and the destroyed entry's own text had predicted exactly this, was read during that run, and the mistake followed anyway. **A hook was considered and refused:** a write made to watch a guard refuse it is byte-for-byte a write meant to succeed, so nothing mechanical can separate them — which is also why the safe test and the destructive one look identical from the inside.

  **The gap this closes is the trigger, not the tests.** The suites exist, run in seconds, and the rezip ritual already stops on a failure — but a rezip happens when Alex asks for one and a commit is routine, so the check sat behind the rarer event. A `session_start.py` regression was committed clean and caught only because she happened to ask for a rezip minutes later; earlier, for a whole period when nothing ran them at all, a hook emitting a rejected payload shape stayed dead and invisible while sessions compensated by reading CLAUDE.md and the queue directly.

  **A non-blocking report was weighed and lost.** It ships sooner and depends on nothing, but a report listing known failures at every hook-touching close is exactly the output people learn to skim past — which is why the rezip ritual stops rather than warns.
- **A close whose staged paths include `plugin/throughliner/docs/`, `workshop/resources/self-authoring-rules.md`, `workshop/resources/rule-maintenance.md`, `workshop/resources/method-compliance-audit-checklist.md` or this file runs `py workshop/resources/rule_signals.py .` before committing, and reports one line either way.** Same shape as the hook-suite step above and read the same way, from `git status` — the same staged-path set the rule gate itself fires on. The close is the one moment these checks have anything new to say, because two of them read commits.

  **The one line is the point, not a nicety.** A clean run and a run that never happened are indistinguishable from outside, which is the exact condition these checks exist to remove for rules — and it is why nobody could tell, for the whole life of this mechanism, that nothing was running it. **Word the line as what was checked and found, never as a verdict on the rules' health**: "Rule checks: four run, nothing found" rather than anything implying the corpus is in good shape. Where something is found, the existing behaviour stands unchanged — file one capture under the slug printed, satisfied while an open item already carries it.

  **Running it at every close was rejected:** the checks are meaningless on a commit touching no rules, and this project has repealed measures for crying wolf.

  Host-only, like the suites above: consumers never author method rules and have no such checks.

  **Host-only by residence.** `workshop/resources/testing/` is not in the plugin package, so a consumer has no suites to run and the step could never fire for them.
- **A build that changes the document format bumps the format epoch.** `FORMAT_EPOCH` near the top of `plugin/throughliner/hooks/session_start.py` declares the shape the method expects a project's own documents to be in. Bump it whenever a build makes an *existing* project's files structurally wrong — a new section, a renamed heading the hooks parse, a field that becomes required, a work-item shape change. Do **not** bump it for anything an old project's files survive unchanged; the epoch's whole value is that it doesn't cry wolf the way the version number would. Sibling to the README-sync and SPEC-sync triggers, and load-bearing in the same way: without the bump, session_start's migration halt never fires and every consumer project silently keeps running on the old shape. Also add a line to the epoch history comment saying what the new number means — a bare number nobody can date is a number nobody dares change. **A build that bumps the epoch also refreshes `plugin/throughliner/docs/migrate-checklist.md` in the same session, and says in its LOG entry what it refreshed or why nothing needed refreshing** — the builds that make an existing project's files structurally wrong are the same builds that stale the recipe for converting them, so the trigger already exists and needs no new detection. A pass on every rezip was weighed and refused: most rezips touch no format at all, and a maintenance pass firing on unrelated work is the cry-wolf shape this project has repealed measures for twice. Host-only: consumers never author formats.
- **A new work-item flavor must be wired everywhere it is read, or it ships half-working.** Flavors today are build (no tag), `[audit]`, `[user]` and `[freeform]`. Adding one means: `plugin/throughliner/docs/plan.md` (how it is marked and placed at the decision step), `next.md` (execution routing — build it, walk it, or halt on it), and `done.md` (close routing, and whether the close must announce it). The queue lint in `post_tool_use.py` is **not** a fourth site: it validates slug, red-flag state and `Blocked by:`, and holds no list of valid flavors, so a new tag needs nothing from it — verified when `[freeform]` was added. Check that rather than assuming it either way. The rule exists because the retired spec-edit type was caught half-wired once, omitting next.md's router, and a later session had to finish it. Host-only concern: consumers never author flavors, so this stays in this CLAUDE.md, not in shipped plan.md.
- **A hook-enforced-format change traces its ripple by grep — a specialisation of the shipped repeal-trace limb, not a peer of it.** `plan.md`'s decision step already requires that an item repealing or rewording a specific sentence or value greps its distinctive words across the project before writing the Files line. That is the general rule and it ships, because a consumer repealing a sentence in their own SPEC has the identical problem. What follows is the narrower host-only case, which adds one requirement of its own: the grep must also name the enforcing hook. Stated as a specialisation deliberately — two rules on one subject, at the same level, with no declared relationship is exactly the defect the law-prose pass exists to find, and leaving these as peers would author it. When a work item changes a format or enum the hooks enforce — a marker format, a state value, a section heading the lint parses, a work-item shape — its scope is traced by **grepping the format's literal values across the repo**, not written from the design discussion. The grep must name the enforcing hook AND every doc, template, and FAQ entry that names the values, so the file list is complete before the build starts. The why, from a real miss: the red-flag-states change (`State: cleared`/`uncleared`) was scoped from discussion and missed `post_tool_use.py`'s valid-state set — which would have rejected every new marker — plus done-family docs, setup.md, CLAUDE-TEMPLATE.md, and two FAQ entries; /next's self-scoping caught it only by halting mid-run, the interruption an unattended run shouldn't need. Same family as "A new work-item flavor must be wired everywhere it is read": plan-time tracing shrinks the ripples /next must catch, and when it still catches one it captures rather than blocks (see the discovery-vs-underspecification rule in next.md Step 2.2). Host-only: consumers don't author hook-enforced formats, so this stays in this CLAUDE.md, not shipped plan.md.
- **Scripting constraints for this repository's own code** — `plugin/throughliner/scripts/` and `workshop/resources/`. Five rules, each from a failure that has already happened here.

  - **Standard library only.** Already how these scripts are written; recording it stops a dependency being added casually, and it is right anyway for code shipping to machines whose interpreters nobody controls.
  - **Invoke the test suites as plain scripts, never through `pytest`.** On this machine `python` resolves to `C:\Program Files\Inkscape\bin\python.exe` — an application's bundled interpreter, first on PATH, shadowing the user's own Python. It has no pytest, so `python -m pytest` fails with a message naming Inkscape, which reads as nonsense and sends a session chasing the wrong cause. `py` reaches the user's own interpreter.
  - **A new script reconfigures stdout and stderr to UTF-8**, copying the block from `reorder_queue.py`, which is the canonical copy. The duplication is deliberate: the hooks run standalone from a copied plugin cache and cannot import a shared module, which is also why one was rejected.
  - **Any subprocess read, and any PowerShell read of a text file, names UTF-8 explicitly** — `encoding="utf-8"` on the subprocess call, `-Encoding utf8` on the PowerShell read. Same defect one layer up, and the one a shared module would have missed — `session_start.py` mangled every em-dash until this was added, and a PowerShell read that never named the encoding split queue text into mojibake on the way to an append.
  - **Before diagnosing an encoding fault seen through a console, check `ascii()` or the raw bytes.** Twice in one session a correct string was read as corrupt data, once with a full wrong diagnosis built on it.

  Host-only: consumers have their own PATH and their own interpreters.
- **A tersify pass over the queue exists and runs when Alex asks for it — never at a close, and never on a schedule.** The procedure and both measured passes are written up at [`workshop/resources/research/tersifying-the-queue.md`](workshop/resources/research/tersifying-the-queue.md); read it when she asks, not before.

  **The pass-2 method is mandatory whenever it runs:** item-level splice keyed by slug, unchanged blocks carried byte-identical, a slug-uniqueness assertion, and per-block deltas so nothing grows silently. **Pass 1's rewrite-from-memory is the method not to repeat.** **Fenced blocks are untouchable** — see the write-up's §8d and [two-column-fences-wrap-unreadably].

  **Not at the close, on measured grounds rather than taste.** Its yield was 8% then 3%, and its own conclusion is that this queue is not verbose — the length is accumulated decision history. Against that, a close already carrying the session's heaviest work would take on a whole-file read and rewrite. **And its two failure modes are the kind that must not run unattended:** a silent duplication of fifteen items that reading could not see, and a probable upgrade of a paraphrase into a quotation claim, one instance of which was found live in this queue and repaired the same day.

  **The close reports nothing about length.** With the ceilings retired there is no breach to report, and a distribution printed at every close would be a measurement nobody asked for at the moment they are least able to act on it. The on-request pass is the whole of what this is.

  Host-only — the write-up is a dev artifact and consumers have no such pass.
- **Old plugin history.** The plugin was rebuilt from scratch on 2026-06-01, and both this folder and the GitHub repo (`FlintcraftTech/throughliner`) start there — the remote is not a pre-rebuild archive. Some pre-rebuild history does survive locally, as the `v17`–`v157` orphan tags, which are not ancestors of HEAD. Anything earlier than that, if it exists at all, would be on Alex's old machine. Don't send a session chasing pre-rebuild commits on GitHub; there are none.

  Before this repository existed, the method was developed inside Cowork for roughly a month. Alex moved to Claude Code with support from people on Discord, having found starting alone intimidating. Two traces of that period survive here: the `v17`–`v157` orphan tags, and a single back-reference in `LOG/log-v1.5.2.md` to a decision dated 2026-05-22, ten days before the first commit. No pre-rebuild log entry itself survives, and the legacy logs never name the venue — so this paragraph is the only place it is recorded.

### Self-hosting dependency ordering

Work ordering in QUEUE.md implicitly assumes the next item sees the previous item's effects. That's true for **target-side** changes — edits to files under `plugin/throughliner/` that Claude can read at author time. It's false for **host-side** changes — the installed plugin's hooks, the loaded skill procedure docs (`docs/setup.md`, `plan.md`, `skill-nonspecific-rules.md`, and the `next*.md` / `done*.md` families) — which only refresh after a rezip or release plus a full app restart.

When an item depends on a previous item's host-side effects, that dependency does not resolve in-session. /plan holds it below the cleared-to-run line with `Blocked by:` naming the item it waits on — or several items, comma-separated, where it waits on a group and must lift only when all of them resolve — and says in its prose that the dependency is host-side.

**The old `--- Push required before continuing ---` and `--- Plan session here: … ---` markers are gone.** `docs/next.md`'s pre-flight states it plainly: there is no blocker gate, no push marker and no unpark scan — those belonged to the earlier model. Don't write either marker into QUEUE.md, and don't expect /next to halt on one. What replaced them: readiness is settled at /plan before work reaches the cleared region, host-side liveness is read from the installed build's content stamp rather than asserted by a marker, and a genuine dependency is carried by the `Blocked by:` field, which survives a reorder where a positional marker does not.

One thing the old marker's note said is worth keeping, because it was misread repeatedly: a decided-but-unshipped rule is **in force from the moment it is decided**. In-repo sessions read the queue and the discussion, not just the installed plugin. "Not shipped yet" is never a reason to suspend decided reasoning.

## Rezip (local testing), Push (routine), and Release (on request)

**Three separate actions, and the words mean what they say.** "Push" once meant the full release ritual, so a push and a release were one event; they were decoupled on 2026-08-04 and stay decoupled.

- **Rezip** refreshes the installed host from the local `plugin/throughliner` folder so Alex can dogfood the plugin privately. Never publishes, never releases, touches no remote. The install uses no zip — the local marketplace sources the folder and the CLI snapshots it directly — but the rezip does archive one afterwards, into the gitignored `plugin/rezip-archive/`, which is where a release later gets its bytes. **A rezip runs before the push, not after it.**

  **Never run `claude plugin marketplace add` against the GitHub repository on a machine using the local `flintcraft` directory marketplace.** The CLI silently overwrites a same-name registration — no warning, no error — so the local `flintcraft` would be repointed at the remote, and every later rezip would install the published plugin while reporting success. The derivation is a verified external bug, anthropics/claude-code#44042, open and tracked; the evidence is in `workshop/resources/research/marketplace-name-collision.md`. Only this project's own machines are exposed, because testers have no local directory marketplace to collide with.
- **Push** is `git push`, and nothing else. Routine and cheap — it runs after every /next and at any /done, with no consistency sweep, no zip and no GitHub Release. `plugin.json` is committed carrying whatever `-testN` suffix the rezip left; the release bump strips it. It needs no confirmation, so don't ask for one.
- **Release** publishes a version: the release bump, the consistency sweep, the repackage, the GitHub pre-release and the host reinstall. **It runs when Alex asks for it, or when the weekly release cycle falls due — and at no other time.**

**Releases are on request, or on the weekly cycle.** The at-no-other-time clause of Alex's 2026-08-09 decision is superseded to this extent and no further: there is still no trigger that fires on a session's commits touching `plugin/throughliner/`, still no release-due file check, and asking to rezip or to push is still not asking for a release. Wait to be asked, or read the cycle.

**The cycle is `[weekly-release]` in `CYCLES.md`** — Wednesdays, its observable the published date of the latest GitHub release, its pick the most recent rezip labelled stable on the nerds list. **The reason the 2026-08-09 failure does not recur is that the cycle asks no readiness question:** the calendar and a label applied when the rezip was posted settle which build goes, retrospectively. The rejected middle option asked "is this good enough?" prospectively, and it stays rejected — see the paragraph below, which is not weakened by this.

**What this supersedes, recorded so it isn't re-derived.** From 2026-08-04 to 2026-08-09 the release fired automatically at any /done whose commits touched the plugin, and this document explicitly barred asking whether a release was warranted. The reasoning behind that was sound and is not being called wrong: welding release to push had made every routine save ask "is this good enough to publish?" — a question with no honest answer on a project that will never feel finished — so releases stopped happening and the work stayed invisible. It is outweighed rather than refuted. An automatic publish that Alex has to interrupt is a worse failure than a release that waits to be asked for, and she has now stopped one twice.

**The intuitive middle option is already rejected — don't propose it.** Keeping the trigger automatic but pausing once before publishing ("about to publish v1.21.0, go ahead?") looks like a compromise and is not one: that pause *is* the readiness question, and it is the exact moment Alex stopped. If a later session feels the pull toward it, this paragraph is the answer.

**Every release is marked pre-release, and that is the honest label.** The plugin is in active testing and is not ready for the Claude marketplace. GitHub's pre-release flag states that structurally, so it never has to be re-decided or re-worded release by release, and a release is never a claim that the plugin is finished.

**A release only ever runs on `main`.** Check the branch first — `git rev-parse --abbrev-ref HEAD`. Releasing from a branch would publish unmerged work and fork the version line, so if Alex asks for a release from somewhere else, say so and stop.

Do whichever Alex actually asked for.

### Rezip and Release live in a fetched doc

Their full step-by-step is [`workshop/resources/release-ritual.md`](workshop/resources/release-ritual.md) — open it when Alex says "rezip" or "release", and not before. It also carries the project-folder-move recovery. Both rituals fire only on an explicit word from Alex, which is exactly the shape that can be fetched; keeping their ~25 steps always-loaded spent about a third of this file's instruction budget on text that never fires unprompted.

**Push stays here, deliberately**, because it runs after every /next and at any /done — a standing condition Claude has to notice, not a word Alex says. A rule that must fire unprompted cannot be fetched.

### Push (routine)

One step: `git push`. It runs when Alex says "push", after every /next, and at any /done — no sweep, no zip, no GitHub Release, and **no confirmation needed**. Never `--force`. Stage explicitly, as the file-safety rules require; never `git add -A`.

**`plugin.json` is committed as it stands, `-testN` suffix and all. The release bump strips it** — see `workshop/resources/release-ritual.md`.

**The version-clean step that used to sit here is repealed (2026-08-19), and this is a reversal of a same-day refusal made on legitimate grounds.** That refusal — against stripping at the release — rested on the suffix being harmful, because a `-testN` would then sit on the public remote between releases, as `1.16.0-test4` once did. **The owner of the repository says it is not harmful: just untidy.** The premise is removed rather than the reasoning overruled. What changed alongside it is frequency: the earlier reasoning assumed occasional rezips, and Alex now rezips at every run, so a clean step ran constantly to prevent something nobody minds.

**One interaction, already favourable.** The content stamp drops the version key, so committing a suffixed version cannot report the host stale.

**So a close meeting a `plugin.json` diff whose only change is the `-testN` suffix commits it like any other change** — no investigation, no note, no question. It is no longer a dirty-then-cleaned file; it is simply the version the plugin is on. Host-only, and it stays here rather than in the shipped `done.md`: consumers never rezip.

Pushing often is the point: it decouples "the work is safely on the remote" from "I am publishing a version," so the routine action never carries a publishing decision. **No release-due check runs here.** A release happens when Alex asks for one.

## Discord posts

**There are two kinds of post, each with its own test, and nothing that fails both.** Not tips on using Claude Code, not general development lessons, not interesting findings the project happened to make along the way. When a session turns up something genuinely useful that is neither kind, its home is the LOG or `workshop/resources/research/`, not the channel.

```
NEWS  ->  #announcements   a release, or a big happening.
          The test: did Throughliner CHANGE?
TIP   ->  #tips            one Throughliner feature explained. Maybe newish,
          with no release or big event behind it.
          The test: does this EXPLAIN ONE FEATURE the plugin has?
```

**For news, the test is not "did we learn it" but "did Throughliner change".** A session that has just learned something useful feels like it has something to announce, and that feeling is not the criterion. The exclusion of general Claude Code tips stands for both kinds: a tip is about *this* plugin's features.

**Where a post passes both tests — it reports a change AND explains how to do something — the tip test wins and it goes to #tips.** News is reserved for the change itself: a release, or a big happening. Without the tie-break both tests pass and the post lands wherever it was drafted, which is how a how-to went to #announcements on 2026-08-27 and had to be deleted and reposted the same hour.

**And a tip walks the reader through the how-to rather than reporting that a capability exists.** A post saying the plugin can now do X is a change report wearing a tip's clothes; a tip says what to type, where to look, and what tells you it worked.

**Old posts may be recycled into future ones**, so a subject already covered is not spent.

**The tip pipeline.**

```
1. REZIP      tip candidates are noticed as features land in the installed
              build, and filed as ordinary captures in Unprocessed — the one
              file every session may write, whatever it is doing.
2. RELEASE    the release is what makes a candidate postable. The ritual marks
              which open candidates its shipped features clear, by appending a
              line to each of those captures naming the version.
3. /PLAN      reads those lines and processes the cleared candidates into dated
              post items — new or updated features first, historical tips on
              slow news days.
```

Tip staleness is covered by the existing repeal-grep over `INBOX/sent.md`, which is why the register records the channel per post.

**Every outbound post checks the how-to topics before it goes.** The forum's how-to topics exist for welcoming and onboarding; **their number stays small enough to serve that purpose, and a new one is Alex's call rather than something accumulated by drift.** Each tip, rezip entry or announcement may bear on one, so the posting step reads the how-to topics' lines in `INBOX/sent.md` for claims the new post touches. A needed tweak is the bot editing its own how-to post, under the approval rule like any send — which is why bot authorship of those posts is being migrated ([howto-posts-bot-authorship]): bot maintainability requires bot authorship.

**Announce only what has shipped: every claim in a post is true of the installed plugin at the moment it is posted.** Where a post describes work that is designed but not built, the post waits for the build — file it as a queue item naming what it waits on. **A planning session therefore has nothing to announce at the time it plans**, however much it decided — but drafting is its part, because the reasoning is richest there; say that plainly rather than reaching for a substitute subject.

**The planning close sweeps for post candidates.** Present them as one numbered set for approval, and on the yes write each approved draft as a dated capture — the post itself still waits for the work to ship, which the capture names.

**The posting brief.** A draft is written for a reader who does not know this project's internals: lead with what changes for them, in plain words, and leave decision history out entirely. The exemplar — benefit first, no commentary on what was weighed:

> Throughliner now checks your GitHub issues when you plan. If you filed a problem report and someone answered it, that answer shows up as work in your queue instead of sitting on a page you'd have to remember to open.

**A post describes something the user can see in a session they are sitting in, or answers a question they actually ask.** Internal arrangement is not postable however well it is worded — where the method's own text moved, what was merged, which rule now lives where. The recorded failure: a draft about splitting rationale out of operative rules passed both existing tests and was rejected on five separate visibility grounds (`LOG/2026-08-27-announcement-rationale-split-correction.md`).

**Verify against the shipped plugin at post time, not at draft time.** Before the draft goes out, re-read what it claims against the installed build; where the claim has drifted, rewrite it or hold the post.

The limit is **2,000 characters**, which is Discord's.

**Claude has a route to Discord: the bot, driven by `workshop/resources/discord_post.py`.** It reads the channels it has been granted, and it sends, edits and deletes its own messages. Reading and posting are separate: reading needs nothing beyond the grant, while **every send is gated by the approval rule — the exact text is shown and needs an explicit yes before anything leaves the machine, and an automated edit is still a send.** That is the existing rule on anything leaving the machine, restated here because the sentence it replaces was carrying it: the old text said Claude had no route, which was a fact doing double duty as a safeguard. Only the fact changed.

**The planning opening's correspondence check also runs the replies read** — `py workshop/resources/discord_post.py replies --since <date>`, anchored to the most recent planning session's record, the same anchor the issues check uses and with no state file. One capture per reply carrying something new, satisfied while an open capture with its slug exists; an owed reply is drafted and sent only on an explicit yes to the exact text, under the send gate above. Replies arriving mid-session wait for the next opening, as INBOX mail does. Recomputing the anchor from the record rather than storing it means a forgotten check costs nothing and no file can go stale.

**The draft-edit flow** is the general co-authoring mechanism in `docs/skill-nonspecific-rules.md`'s walkthrough requirements, applied to a post. A draft is written to a `.txt` file and edited in the desktop side panel, which opens `.txt` for editing with a save button — so Alex decides when her edits land. She edits, saves and says done; the script then posts that file's exact bytes on her explicit yes. Editing the file directly beats negotiating wording change-by-change in chat. A post-post correction is the bot editing its own message, since nobody can edit anyone else's Discord message.

Per-post manual copying stays available whenever Alex prefers it. The bot's environment facts — where the token lives, which channels are reachable, why channel ids are not kept on file — are in `TOOLS.md`.

**A posted draft gets its line in `INBOX/sent.md` like any other outbound artifact** — date, destination **including which channel it went to**, whether it was handed over for completion or continuation, what it claimed in one clause, and a pointer to the text. The channel is what lets the repeal-grep tell a tip from an announcement from a rezip entry, and what lets the how-to check find the how-to posts' own lines. Written in the same turn as the approval, because the wording exists then and nothing later reconstructs it. **Read the claim off the approved text as it stands on screen, never from what the session settled** — what was decided and what the post says come apart, and a claim composed from the decision describes a post that was never made. The reason this matters here specifically: a post makes a claim about how Throughliner behaves, and a later change can falsify it with nobody noticing. The record is what a repeal can be checked against. Full mechanics in `docs/feedback-and-inbox.md`.

### The test-rezips entry — posted at the close, not at the rezip

**Host-only by construction: this check lives here and never in the shipped close docs** — consumers have neither the bot nor the channel.

**At a close, check whether at least one full /plan session AND one full /next session have run on the installed build since its rezip.** Read that from the `LOG/` records dated after the install date the session opening reports. Both run → the new entry is ready to draft. **An entry describes a build that has been exercised, not a fresh one, which is why the readiness test is sessions rather than time — there is no timing to this.**

**The close's session record carries one of these lines, whichever the check found:**

```
Rezip entry: ready — <version>, one /plan and one /next since <date>
Rezip entry: not yet — <version>, <which half is missing>
Rezip entry: none — no rezip since the last entry was posted
```

Without it a clean run and a run that never happened look identical afterwards, which is how a 23-item close skipped this entirely and nobody would have known had the user not asked why the previous rezip was unposted. The check had no site — it lives here, outside the sequence `done.md` and its flavor sub-doc work through — and no artifact, and the line is the missing artifact. Same required-artifact shape as the rule-gate, forward-advisory and FAQ dispositions beside it, carrying the same honest limit: a line can be written dishonestly and nothing checks that. What it buys is that a **missing** line is visible.

**The entry's lifecycle is two steps.**

```
NEW entry      one of the three labels, a `Commit: <hash>` line, the version,
               and the zip of that exact build attached. NO rating — too new
               to rate is what "under testing" says.
PREVIOUS entry posting the new one unlocks the edit of the one before it: a
               short testing-outcomes summary read from the LOG, plus a
               usability rating out of 5, given by Alex at that moment.
```

The posting step attaches the build's zip from `plugin/rezip-archive/` — `--attach-archived-zip` on the posting script — so every entry carries the bytes that were actually installed and tested rather than a zip built at posting time from a tree that has moved on. Drafting, approval and posting run the ordinary way — a `.txt` draft file edited in the side panel, explicit yes to the exact text, the bot posts, a register line with a pointer confirmed to resolve. The prune runs in the same pass, keeping the channel and the archive at the same 15.

**An edit to an entry updates that build's readme in the same turn, under the same approval as the edit.** The archive readme and the channel post are the same text by design — that equality is what lets a release read a label from a local file — so changing a label or backfilling outcomes in one and not the other silently breaks the lookup the whole model rests on.

**First iteration, stated because it differs:** the entry currently in the channel is Alex's own post, so its backfill — outcomes plus her rating of 3/5, given 2026-08-27 — is hers to paste once. Every entry after that is bot-authored and bot-editable.

**Where a repeal falsifies something already announced, file a correction post as its own `[user]` item.** The check runs at /plan's decision step, on the repeal limb's existing grep, extended to `INBOX/sent.md` — so the trigger is the grep already being run and needs no separate detection. The item names what was announced and what is no longer true; the user posts it, as they post everything here. **This is the whole reason `INBOX/sent.md` records what a post claimed** rather than merely that one happened: a claim nobody wrote down cannot be checked against a repeal, so earlier cases are unfindable and this reaches only posts made from now on. Say that rather than describing the record as covering the channel's history.


## Handoff-claim provenance

When a session opens from a Claude-authored handoff or context prompt — a resume note, a "here's where we left off" summary — treat its claims as unverified until the user confirms them. Claude-written content is not read in the user's voice. The why: a handoff Claude authored is not a user-vouched fact, and a fresh or weaker session can't tell which claims the user stood behind versus which Claude wrote — so a Claude-authored line ("the lint keeps flagging X") must not be used as evidence that the user reported X. Confirm before relying on it. (Resolved 2026-06-26: no claim-marking format is added — this standing rule suffices. Multi-line /next takes its instructions from the queue, user-vouched by construction, so it never reads a mixed Claude-authored directive whose claims would need marking; the one Claude-authored thing a run reads is its own working-state file on resume, read as mechanical state, exactly what this rule already covers.) Where the user reports file state seen through a file browser — changed, updated, looks new — check `git log` and the filesystem before reasoning from it, and name what was checked rather than contradicting the report: a date shown in Google Drive means "last synced", not "last edited".

## Cross-platform ports

This project is the **canonical** Throughliner, for Claude Code. **Other people are porting it to other harnesses, and ports are a supported thing this project actively helps** — two flavours are recognised, one tracking this project closely and one diverging under its own name, and both are welcome. Where the mechanics live: [port-flavours-named] defines the two flavours in the shipped docs, and [port-facing-changelog] produces the per-release changelog a tracking port surveys, marking the host-only changes that must not be ported.

**Alex's own Codex port is shelved indefinitely** (dormant since 2026-07-28), and the reason is hers rather than a judgment about porting: she found running a port herself mentally destabilising while developing in isolation. That says nothing about what anyone else may want.

**The port's working folder and its `codex/si-port` branch were deleted on 2026-08-14, and there is nothing left to read.** The folder was a git worktree of this repository, so `git worktree list` reported it as live work every session. Removing the worktree and dropping the branch ref was chosen over rewriting history: a rewrite changes every commit hash, and this project's LOG entries are full of hashes that are the record the whole method rests on. The port's commits are therefore unreachable rather than erased, recoverable from the reflog until git garbage-collects them; the branch tip was `59da478`. Uncommitted edits sitting in that folder were discarded on Alex's explicit decision after being told they could not be recovered.

**So an old Codex-side slug can no longer be looked up.** This section used to point at the folder for exactly that; it points nowhere now. If the port is ever revived it starts from the reflog or from scratch, and this section gets rewritten to describe a live relationship again.

## E2E testing

**Taskflowapp** at `<TASKFLOWAPP_ROOT>` (its folder on your machine; on this machine it sits under `Taskflow Planning\Planning in here\Taskflowapp`) is the test consumer project. Alex runs E2E in a separate desktop-app session; observations come back here as queue items.

### Reading session transcripts

Self-hosting and E2E testing increasingly evaluate Claude's behaviour from the raw session transcript. How to get and read one:

1. **Source the raw transcript** from `.claude/projects/<project-slug>/*.jsonl` — the authoritative, unedited record of the session. Read that file rather than asking Claude to regenerate or recall the conversation: a regenerated transcript is a lossy reconstruction, and it hits the handoff-provenance problem (Claude-authored content read as fact rather than as the user's own words).
2. **When the .jsonl is large enough to swamp context, preprocess it.** Run a short Python pass that strips the file to just the conversation text — drop the tool_use / tool_result blocks, the thinking, and metadata — write a slim file, then read that.

The why, weighed against the alternatives: reading the raw file in chunks does NOT save context (the same bytes accumulate across turns); a subagent keeps Claude's context clean but adds a reconstruction layer one step from the evidence; preprocess-then-read keeps Claude on the primary evidence at moderate cost; a targeted grep is lighter still but risks missing findings phrased without the search term. Applies both to the consumer E2E project (Taskflowapp) and to goal/dev sessions here.

## User context

Alex is a non-coder using the Claude Code desktop app. Explain things in plain English. The desktop app doesn't support `--plugin-dir` or `/plugin` CLI commands.

No Editor or Working mode field. Both were retired on 2026-08-09 — the desktop app opens `.md` in its own viewer whatever editor is named, and the location field turned out to record how much text Alex wanted pasted rather than where she was sitting. Doc-resident text renders as a pointer + link unconditionally, with a plain-English summary inline where a discussion needs one — the inline-paste offer is retired (skill-nonspecific-rules.md, view-in-doc rendering).

## Current state

**Status:** Target v1.20.0. Repo on GitHub, method docs set up (/setup complete).

**Priority, the user's word 2026-08-29: ports are the current number-one priority.** Dated so its age is visible when the focus moves on — one sentence to update on her word. It was previously carried only by where the port items sat in the queue, and a single planning session buried them under a dozen newer cleared entries the day after she said it, so placement is not the carrier. SPEC was refused as a home (ports being supported is product truth; a current focus is not), and so was the memory project (it ranks projects against each other, while this must reach a fresh session opening this one).

## Method docs

- **SPEC.md** — what this product is, who it's for, how it works. Source of truth for design decisions.
- **QUEUE.md** — two sections. **Processed** holds work discussed and agreed, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** holds captures — ideas, discoveries, and tasks not yet weighed — that the next /plan processes. A work item is a `#### ` heading (its one-line description) with a `[slug]` at the end of that heading line and its rationale as prose beneath; the block also carries a provenance label ("captured by you" / "by Claude"). A leading `[audit]`, `[user]` or `[freeform]` tag names how the item is executed; no tag means a build. A work item carrying a security or privacy risk gets a `Red flag · State: <cleared | uncleared>` marker on its own line in that block — the flag rides the work, not a separate section. Deferred verification for shipped work is not a separate section either: it lives as a `[user]` work line (below the cleared-to-run marker while it waits on something), revisited each session by plan.md Step 1's below-line revisit, which reads each item's prose lift-condition and proposes lifting when it clears. Host-side liveness is resolved by content stamp, not version: the session-start hook surfaces the installed host's build stamp (a content hash of the installed plugin's files), and /plan compares it against the target's current stamp (the same `content_stamp()` run over `plugin/throughliner/`) — a match means host-side changes are live, with no asking the user. **The stamp hashes `plugin.json` with its `version` key dropped**, because the rezip sets a `-testN` suffix and the push resets it while neither changes what the plugin does — left in, the stamp reported the host stale immediately after every rezip, which is the check's most common moment. One consequence: a pure release bump, where only the version changes, no longer moves the stamp, and that is correct, since the installed host does still match the source.- **LOG/** — per-session records of what was built, tested, and decided. `LOG/index.md` for summaries (newest first), each full entry as its own file named on its index line. Legacy entries from before the per-entry split remain in `LOG/log.md` and `LOG/log-v*.md`, findable by hash.
- **workshop/resources/self-authoring-rules.md** — the admission-and-eviction gate every new method rule passes through, and the home of the rationale-lives-outside-the-operative-rule split. Run at authoring time, per rule.
- **workshop/resources/method-compliance-audit-checklist.md** — the standing criteria for a routine, corpus-wide compliance audit of the method's procedure docs: four lenses — self-authoring compliance (by reference to `workshop/resources/self-authoring-rules.md`), response-shape tag placement, narration drift, and decision history in operative text (the delete-and-read test). Distinct from the gate's per-rule-at-authoring use: this is the periodic sweep of already-shipped docs. Host-only dev artifact (not shipped in the plugin package). A future /plan scoping a compliance audit reuses this rather than re-deriving the criteria.

## Workflow

- `/setup` — initial project scaffolding (already done).
- `/plan` — manage the queue, add ideas, resolve questions, check for drift.
- `/next` — execute the top queue entry (build, test, or audit).
- `/done` — close the session, record what happened, commit.

## Rules for Claude

- SPEC.md is a normal doc any work item can edit — the spec-edit batch type is retired. A SPEC change decided in /plan is edited in that same /plan session; a large SPEC rework is a normal build item that lists SPEC.md. **A build never writes product truth**: the decision step asks of every item whether it changes what SPEC says and writes the sentence there, ahead of the build, and a build that discovers a missing sentence files it as a capture rather than writing it — so SPEC lags at most one sentence, visibly, until the next planning session. The reason is a session boundary rather than scope: the session that made a choice is not the session that certifies it in product truth. Deferring the write to the build's own close was proposed and refused on that ground, since the close is the same session. The scope-lock still denies SPEC unless the active run lists it in Files, so a build can't touch SPEC silently. Drift is prevented by two close-out spec-sync gates (done-plan.md at the /plan close, done-build.md at the /done-build close): a session can't close with SPEC behind the decision that changed it — the SDD same-commit atomicity the gates protect is why they replace the old batch.
- Design for fresh, short sessions. The system must work for a fresh, short session that carries none of a prior session's memory: the files (SPEC, QUEUE, LOG, the session's build working file) must suffice on their own, and conversation memory is a convenience, never a dependency. Short sessions on the weaker post-Fable development model (from ~2026-06-20) are the design target — and every consumer is already in this case. A long session that remembers everything is the exception, never the case to design for. (This is about robustness to session-memory loss; it does not change the Model target above.)

  **Which model runs which session here: planning sessions run on Fable, build sessions run on Opus 5.** What follows from that — writing an item's instructions for a reader with less of the project in view and possibly less capability — is the shipped rule at plan.md's decision step, and is not restated here. One host-only consequence remains: weigh a capture filed from a build session, at the decision step, as coming from a session with less of the project in view than the planning session reading it — check its premise against the queue and the record before moving it into Processed on the strength of how it is stated.
- All use of the plugin to develop the plugin is testing the plugin. Any observation of Claude's behaviour — wrong, unexpected, or improvable — is a testing outcome and must be routed to Captures, not discussed and dropped. In particular: any moment you notice session memory covering for something the docs or files should carry — a step that worked only because you remembered the conversation — is itself a mandatory capture. That gap stops hurting under a model with strong session memory, so it stops being found, while fresh short sessions and consumers still hit it.
