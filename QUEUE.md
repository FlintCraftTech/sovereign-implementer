# QUEUE

Two sections. **Processed** — agreed work, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** — captured, not yet processed; the next /plan weighs each item. Every entry in either section is a `#### ` heading (its description) with a `[slug]` at the end of that line and its rationale beneath; an entry in Unprocessed is a **capture**, and it becomes a **work item** when /plan keeps it into Processed. A leading `[audit]` / `[user]` tag names how it's executed; no tag means a build. An item carrying a security or privacy risk gets a `Red flag · State: …` marker — the flag rides the work.

**Authoring a rule for the method's own text? The rule gate is in `CLAUDE.md`, always loaded — run it before you write.**

## Processed

#### Bot cannot create a forum topic, so no forum post can be bot-authored [bot-cannot-create-forum-topics]
Found live 2026-08-29, attempting to post the showcase guidelines through the bot on your go. The exact failure, recorded so nobody re-derives it:

```
POST /channels/<forum id>/messages -> HTTP 400
{"message": "Cannot send messages in a non-text channel", "code": 50008}
```

A forum channel holds threads, not messages. Creating one is a different call that carries a title, and `resources/discord_post.py`'s `send` has no title parameter — which is why the attempt was made rather than assumed either way.

**What it blocks, and one of these is already cleared to run.** [ports-forum] cannot post its four how-ports-work topics. The showcase guidelines cannot be bot-authored, so they stay either invisible or owned by the user — the exact unmaintainable shape [howto-posts-bot-authorship] exists to undo. **[howto-posts-bot-authorship] itself is probably unaffected**: re-homing posts into *existing* topics is posting into a thread, a different call again, and likely works — untested, and deliberately not tested against the live onboarding forum.

**Changes.** `resources/discord_post.py` gains a forum mode: create a topic in a forum channel by posting to `/channels/{id}/threads` with a name and the message body, taking the title as an argument alongside the existing `--channel` and `--body`. The same pass confirms whether posting into an existing thread works through the current `send`, since two of this project's queued items depend on it.
Observable: a forum topic created through the script appears in the forum under the bot's name with the given title; posting into an existing thread either works through `send` unchanged or is reported as a second gap.

**Filed rather than built because a planning session may not write `resources/`** — the scope-lock refuses it, correctly. This is what the lock is for: the change becomes a queued item instead of an edit nobody agreed to.

**Related, and now filed as [bot-cannot-read-permissions]:** the bot also cannot read roles or channel permissions, which came up the same day when you asked for a permissions review and nothing could answer it. It edits this same file, so whichever builds second reads the other's change rather than assuming the file's shape.

**The showcase guidelines are approved and waiting on this build — your decision 2026-08-29 to wait rather than post them yourself**, on the ground that a self-posted copy is another stored text the bot cannot maintain, against a few hours of a quiet forum. The text is carried here because it exists nowhere else durable; it leaves with the other post drafts when [post-drafts-leave-the-queue] settles a destination. Post it as a forum topic titled **📌 Read first — showcase guidelines**, body verbatim:

> This forum is for ports of Throughliner to other tools, and for projects built with it. The point is that someone can browse it and pick something to try, so keep it current rather than complete.
>
> **Posting here needs the Throughliner expert role.** DM me and I'll add you. The name isn't a bar to entry: it's just that anyone working on a port, or building seriously with the method, ends up knowing things about it that nobody else does.
>
> **One post per port or project.**
>
> **When yours changes, delete your old post and put up a fresh one.** Don't edit in place, and don't add "update:" replies underneath. A new post puts the current state at the top where people are looking, and stops the forum filling with a history nobody is shopping for. You do lose the replies on the old post — that's the trade, and for a showcase it's the right one.
>
> **In your post, say:**
> • what it is, and what tool it runs on
> • what works, and what doesn't yet
> • whether it tracks this project closely or has gone its own way
> • how someone tries it

Once it is up, cut the forum's settings-field guidelines to one line pointing at the pinned post, so there is one canonical text rather than two — and pinning is the user's, since the bot has no pin command either.

#### Cross-platform section states a personal decision as a project fact [cross-platform-section-speaks-for-others]
**Raised by you, 2026-08-29**, on being told the section reads as false now that two people are porting. Your correction, and it is the better diagnosis: *"that's from when I was developing in isolation. I found running a port very mentally destabilising. Says nothing of what others may want, though."*

`CLAUDE.md`'s "Cross-platform ports" section says the Codex port is shelved, that the method now evolves solely on the Claude side, and that there is "no live two-way relationship to maintain, and no port-side work to weigh against". The first is a fact about your own decision. The rest speaks for everyone, and a fresh session reads that paragraph to decide whether ports matter at all.

**Changes.** `CLAUDE.md`'s "Cross-platform ports" section is rewritten: your reason recorded as yours (running a port yourself was destabilising, so the Codex port stays shelved), and the standing claim that no port relationship exists removed. In its place, what is true now — other people are porting, ports are a supported thing this project actively helps, and the section names [port-flavours-named] and [port-facing-changelog] as where the mechanics live. The Codex history and the deleted-worktree record stay; they are still the answer to "can an old Codex slug be looked up".
Observable: the section records the shelving as the user's own decision and makes no claim about ports in general; a grep for "solely on the Claude side" returns nothing.
Rule gate: not needed — a correction of fact and scope in an orientation section, authoring no rule. The trigger fires because the commit touches `CLAUDE.md`, which is the case the "not needed" line exists to make visible.

**Ordering:** first of the four port items because it is what a session reads to learn ports matter, and the other three are meaningless to a session that has just been told they don't.

#### Name the two port flavours, so a port can say what it is [port-flavours-named]
**Your observation, 2026-08-29**, from two people porting Throughliner to other harnesses: two flavours are emerging, and nothing lets a porter say which they are.

**Your definitions, recorded as yours.** A port that *accepts changes at face value and adds no new ones of its own beyond what its system required to fit*. And a port that is *unique and special, which may or may not accept changes derived from the changelogs*. Your stated goal: people should have the **opportunity** to run a Throughliner led by the original project and carrying all its features so far as their setup allows — and diverging, renaming, developing it themselves is equally fine.

**Why naming them is the work rather than a nicety.** Today nobody can tell what a given port promises, including you. A user choosing between ports cannot tell whether the one they install will follow the method or has quietly gone its own way; a porter cannot signal it; and you cannot tell which ports your changelog is even for. The names make the promise legible in both directions.

**Changes.** `plugin/throughliner/docs/` — the two flavours defined where a porter reading the shipped docs will meet them, with the definitions above and the explicit statement that both are welcome. `README.md` — one clause naming them, since a porter arriving at the repository reads that first. The exact shipped file is chosen at build time from where a porter actually lands; if that turns out to be a new doc, it ships in the package like the rest.
Observable: both flavours are defined in a shipped file, and the README names them.

**Rule gate: run — admitted as a definition rather than a rule.** It constrains no session's behaviour and adds nothing to the always-loaded set; it gives two things names. Parent is therefore not applicable, and that is stated rather than a parent invented for form's sake.

**Refused: a registry of who runs which flavour.** Maintaining a list of other people's projects is a standing obligation this project cannot keep accurate, and being absent from it would read as disapproval. The flavour is something a port declares about itself.

**Ordering:** before [ports-forum], whose "declaring your flavour" post has nothing to describe until these exist.

#### Port-facing changelog per release, so a port can survey and apply what changed [port-facing-changelog]
**Your question, 2026-08-29**, and it is the one that decides whether ports can track this project at all: *can their AI systems simply survey the changelogs on my repo since the version they last ported from, then apply the changes from there?*

**The answer is yes, conditional on what the changelog carries.** A human release note ("beta channel wired") is unusable — it names no file, no rule and no wording. What a port's session needs per change is: which shipped file changed, what changed inside it in behavioural terms, and why. This project's LOG entries already carry exactly that shape, so the raw material exists and only a port-facing view of it per release is missing.

**The ship boundary is a folder, which makes it derivable rather than hand-written.** Everything under `plugin/throughliner/` ships; everything else is host-only. That distinction is load-bearing here rather than incidental: a large share of this project's work is explicitly host-only — the release rituals, the rule gate, the compliance checklist — and **a porter following the LOG blind would try to port things that were never meant to ship.**

**Three limits the changelog states about itself, so it cannot be over-read.** It says what changed and never how to map it onto another harness — the translating stays the port's. A change to a Python hook may have no equivalent on their side at all. And a format-epoch bump means their own users' documents need migrating, which is theirs to handle; the changelog flags it and stops there.

**Changes.** A generator under `plugin/throughliner/scripts/` producing the changelog for a release: commits touching `plugin/throughliner/` since the previous release, each with its LOG entry's behavioural summary, marked where the entry records host-only reasoning and where `FORMAT_EPOCH` moved. `resources/release-ritual.md` — the release generates and attaches it. `resources/testing/` — a case over a fixture range of commits.
Observable: running the generator over the range between two releases prints one entry per shipped change, with epoch bumps flagged, and prints nothing for a range whose commits touch only host-only paths.

**Rule gate: run — admitted as an amendment.** Parent named: the release ritual's step list, which gains one step. The generator is a script rather than a rule and adds nothing to the always-loaded set.

**It closes a second gap already on record:** [marketplace-submission] states that a changelog does not exist and that version-consistency discipline is the commonest submission rejection cause. One artifact answers both, and neither needs to wait for the other.

**Ordering:** before [ports-forum], whose "pulling changes to your own port" post describes this artifact and where to find it.

#### Rezip's archive step writes to a folder the scope-lock refuses at rezip time [rezip-archive-blocked-by-scope-lock]
Found live 2026-08-28, on the archive step's first ever run — in the same session that built it, and in the exact shape that session had just fixed for tip pooling. Filed by Claude.

[rezip-archive-mirrors-nerds-channel] sited the archive step inside the rezip ritual, immediately after the stamp comparison — correctly, since that is the one moment the folder is provably the installed build. But a rezip runs after a close, when no build working file exists, so the scope-lock classifies the session as planning — and `plugin/rezip-archive/` is not on the planning session's standing writable list. The readme write was refused outright, correctly by the rule as it stands. The zip write would fail the same way.

**The irony is the evidence:** the same run processed [tip-pooling-step-blocked-by-scope-lock], whose lesson was that a ritual step must check what the session running it may write. The archive step was designed in the same session and nobody ran that lesson against it.

**Settled 2026-08-29 on Claude's recommendation and your agreement, as a sequence rather than a choice between the two routes.** This item takes the narrow carve-out now; the general fix — a ritual declaring the paths its own steps write — is filed separately as [ritual-declares-writable-paths] and designed without a deadline on it. When that lands, this carve-out is what it evicts.

**Why the narrow one first: the release cycle is due Wednesday 2026-09-02 and the archive is empty.** Checked at processing — `plugin/rezip-archive/` does not exist at all, so the step has never once succeeded. The release ritual reads the build's commit from its archive readme and copies the archived zip instead of building one, so those steps currently point at nothing. The general fix cannot be designed, built, rezipped and restarted safely in four days; the carve-out can.

**Fallback if it does not ship in time, so Wednesday is not blocked either way:** the archive readme is the channel post's own text, so the commit is readable from the test-rezips channel, and the zip rebuilds byte-for-byte from that commit with `git archive`. Slower and by hand, and it works.

**One honesty note about the precedent.** The `plugin.json` carve-out this copies is deliberately ONE PATH, and its comment records that a self-declared marker was refused as a full bypass. This permits a folder, which is a step beyond that precedent — defensible because `plugin/rezip-archive/` is gitignored build output rather than part of the plugin package, so permitting it opens nothing under `plugin/throughliner/`. Stated rather than passed off as the same move.

**Changes.** `plugin/throughliner/hooks/pre_tool_use.py` — the planning branch permits paths under `plugin/rezip-archive/`, with a comment recording that it is host-only by residence and why it is a folder where its sibling is one path. `resources/testing/test_plan_quiet_list.py` — cases in both directions.
Observable: the suites under `resources/testing/` pass, with a case proving a write under `plugin/rezip-archive/` is permitted in a planning session and a write to a sibling path under `plugin/throughliner/` is still denied.
Rule gate: not needed — no method rule is authored. The shipped planning list in `plan.md` is untouched, exactly as the `plugin.json` carve-out left it, because a host-only path stated in shipped text would put a folder in front of consumers who do not have one. Nothing in SPEC changes for the same reason.

Refused: rerouting the write the way tip pooling was rerouted — there is no queue-shaped substitute for a zip, so the substitution does not transfer.

**What the interrupted first run leaves:** the 1.21.1-test1 rezip completed in every other respect (bump, suites, prune, install, stamps proved equal 8c874952044d), and its archive entry does not exist. The build is rebuildable byte-for-byte from commit `4efdcff`, so nothing is lost — but a release picking from the archive will not find this build until the step can run. The readme text drafted for it is in the session record.

#### Rituals declare the paths their steps may write, instead of accumulating carve-outs [ritual-declares-writable-paths]
Filed 2026-08-29 at the settlement of [rezip-archive-blocked-by-scope-lock], which takes the narrow carve-out because the release cycle is four days away. This is the general fix, designed without that deadline; when it lands it evicts that carve-out.

**The failure has now happened twice, so it is a class rather than a case.** [tip-pooling-step-blocked-by-scope-lock] and [rezip-archive-blocked-by-scope-lock] are the same shape: a ritual step needs to write somewhere the session running the ritual may not. A rezip runs after a close, so no build working file exists and the scope-lock classifies the session as planning — which is right for a planning session and wrong for a ritual that happens to be fired from one.

**The candidate design.** Rituals became real on 2026-08-28: named step lists in `CYCLES.md`, run when the user says the word. A ritual definition could name the paths its steps write, and the scope-lock could permit exactly those while that ritual is running — mirroring the `[freeform]` scope file, which already lets a session run against a declared list rather than the standing one.

**Why this is not the bypass the record already refused.** `pre_tool_use.py`'s comment beside the `plugin.json` carve-out refuses "a self-declared marker like /setup's", on the ground that a session granting itself permission is a full bypass. A ritual's declaration is not that: it lives in `CYCLES.md`, written at a planning session with the user present and committed, exactly as a `[freeform]` session's list comes from a queued item's Files line. The distinction is who wrote the permission and when — not whether a file is read at run time. Design it so that distinction stays true, or it becomes the refused thing.

**The load-bearing unknown dissolved at processing, 2026-08-29, and the existing carve-out is what dissolved it.** `plugin.json` is permitted **unconditionally** — not only while a rezip runs. Nobody gated it on a live ritual and nothing has gone wrong. So the hook never needs to detect which ritual is running: it reads the project's `CYCLES.md`, takes the union of the paths its ritual definitions declare, and permits those. No marker file, and the self-granted-bypass objection never arises, because the declaration lives in a committed file written at planning with the user present.

**Your decision, 2026-08-29: allow them all the time**, rather than only while the ritual runs. The cost was put to you and is recorded rather than buried — a declared path is writable in any session, not just during its ritual. Here that is one gitignored folder of build output; for a consumer it is whatever their own definition names, which is their decision in their own file.

**It ships rather than being host-only** — consumers define rituals too, so a consumer ritual writing outside the standing list has the identical problem.

**Changes.** `plugin/throughliner/hooks/pre_tool_use.py` — the planning branch also permits paths declared by ritual definitions in the project's `CYCLES.md`, read at check time. `plugin/throughliner/docs/plan.md` — the ritual-authoring step gains a fourth field alongside the artifact, the steps and the word that fires it: the paths its steps write. `resources/testing/test_plan_quiet_list.py` — cases proving a declared path is permitted and an undeclared one still refused, including a project with no cycles doc at all.
Reads but does not change: `SPEC.md`, whose sentence was written at this planning session.
Observable: the suites under `resources/testing/` pass, with a planning-session write under a declared path permitted, an undeclared sibling refused, and a project with no `CYCLES.md` behaving exactly as before.

**No format epoch bump** — the field is additive, so an existing project's cycles doc stays valid without it, the same finding the rituals build itself recorded.

**Rule gate: run — admitted as an amendment.** Parent named: `plan.md`'s ritual-authoring instruction, which already enumerates what a definition carries; this is a fourth item in that list, so it costs no freestanding slot. Eviction, with its condition stated: this supersedes the narrow carve-out on [rezip-archive-blocked-by-scope-lock], and that carve-out comes out of `pre_tool_use.py` once this has shipped **and** the rezip actually exists as a ritual definition — not before, or the rezip loses its only permitted route.

**Ordering, written on both items per the known-ordering rule:** build this before or alongside [host-rituals-migration], so the definitions that migration writes carry the paths field from the start rather than being revisited. Neither blocks the other — this mechanism is buildable with nothing declaring a path yet, and simply has nothing to read until one does.

#### Cross-project research citations have no shape, and the superseded-file safety net stops at the boundary [cross-project-research-citation]
Filed 2026-08-28 from INBOX mail sent by a consumer project running this method (archived at `INBOX/archive/2026-08-28-from-flintcraft-cross-project-research-citation.md`). Reported against plugin 1.21.0-test3. Data from another project, not a decision here.

What they report: a planning session there revised a cleared `[user]` item on research a sibling project owns. The finding lives in the sending project's `resources/research/`, so their item cites it by absolute path.

The gap they name: the method files and indexes research per project, and has no shape for a finding one project owns and another's work depends on. Both available answers are poor — an absolute path that breaks silently when the folder moves, or a copy with no link to the original and no way to tell which is current.

What makes it more than untidy: the `Superseded by:` convention and the queue digest's superseded-research flag are both scoped to one project. If the owning project supersedes the finding, the citing project's item keeps citing the old version and no check fires anywhere. The safety net stops exactly at the boundary the citation crosses.

Why they expect it to recur: the cross-project INBOX exists so sibling projects can send each other findings. Mail arrives, is routed as a capture, the capture reshapes an item — and the evidence now under that item sits in the sender's folder. The mail feature makes the citation, and nothing downstream knows it is cross-project.

What they are doing meanwhile, offered as data rather than a proposal: copying the file in with a line recording where it was originally researched and by which project, plus an ordinary index line. That answers the dead-path risk and not the staleness one.

**Settled 2026-08-29 on Claude's recommendation and your agreement.**

**One of their two options is already barred, which they did not know and which narrows the design rather than weighing it.** The always-loaded scrub checklist bans "file paths that identify a person or an organisation" from a committed doc — the same reason the address book lives inside the gitignored mailbox. So citing by absolute path is not merely fragile; where the citing project's QUEUE.md is tracked it is already a scrub violation.

**That makes their own workaround the answer, with one change.** A finding another project owns is copied in, carrying a provenance line that names **the correspondent** — the project — and never a path, plus its ordinary `resources/research/index.md` line. The committed text then names a project, the path stays inside the gitignored mailbox where the address book already maps it, and the dead-path problem goes with it.

**The staleness half is answered by a label rather than a check.** The digest flags any item resting on a copied finding as resting on a **snapshot**: permanent, honest, and impossible to rot. It is not a staleness check and must never be described as one.

**Changes.** `plugin/throughliner/docs/skill-nonspecific-rules.md` — the research-filing block gains the cross-project case beside its `Superseded by:` sibling: copy the finding in, name the owning project in a provenance line, write the index line in the same move. `plugin/throughliner/scripts/queue_digest.py` — read that provenance line the way it already reads `Superseded by:`, and flag every item naming such a file as resting on a snapshot. `resources/testing/test_queue_digest.py` — cases both directions.
Reads but does not change: `SPEC.md`, whose sentence was written at this planning session.
Observable: a research file carrying the copied-from line makes every item naming it print a snapshot flag; a file without the line prints nothing; the suite covers both.

**Rule gate: run — admitted as an amendment, and it authors no prohibition.** Parent named: the research-and-evidence-filing block's `Superseded by:` convention, which this sits beside as the cross-project case. The ban on absolute paths is not written here because it already exists in the scrub checklist; what is added is the positive action, which is the shape the wording rule requires.

Refused: citing by absolute path — already barred by the scrub list, so this is a statement of existing law rather than a new decision. Refused: a pull-check reading the owning project's research index at the citing project's planning opening. It was weighed seriously and the precedent exists — the subprojects rule already permits one circumscribed cross-project read of a child's log index — but it costs a standing check, works only where both projects sit on one machine, and rests on a gitignored address book that can be lost. One reported instance does not carry it.

**A reply is owed to the sending project**, whose mail asked whether this shape was worth designing at all. It now has an answer. Nothing has been drafted or sent; the send needs the user's explicit yes to the exact text.

#### Retiring the generated build view left BUILD-VIEW.md orphaned in migrated projects [retired-feature-leaves-orphan]
Filed 2026-08-28 from INBOX mail sent by a consumer project running this method (archived at `INBOX/archive/2026-08-28-from-flintcraft-retired-feature-leaves-orphan.md`). Reported against plugin 1.21.0-test3, topped up from 1.20.0-test17 the same day. Data from another project, not a decision here.

What they report: they ran the format 3 to 4 migration on 2026-08-23, which wrote build blocks into every cleared item and generated `BUILD-VIEW.md` at their project root — 15KB, committed. The generated view was retired 2026-08-27. On 2026-08-28 their version top-up refreshed the managed CLAUDE.md block, ran every scaffold and settings check, and reported nothing to do. The orphaned file was still at the root. A planning session found it only because a queue item happened to ask whether it should be committed or gitignored — a question whose premise had quietly become false.

The gap they name: a retirement removes the code that writes an artifact, not the artifact from projects that already have one, and the top-up has no notion of what a previous epoch generated. So a file sits at the root that nothing produces and nothing reads, in every project that ran the earlier migration and then took this version.

The part that shows it was nearly caught: `post_tool_use.py` records that the `--- Build block ---` delimiters were deliberately left alone, because they read as ordinary text now and rewriting them would edit records to match a vocabulary they predate. That reasoning covers the text inside the queue; the retirement also had a file outside it, which no note mentions.

Why they call it worth more than one deletion: the orphan explains itself to nobody — a user opening the folder finds a large unowned file at the root, and the honest answer takes reading the plugin source. Theirs is deleted; every other migrated project still has one.

**Settled 2026-08-29 on Claude's recommendation and your agreement — and the sender's diagnosis is corrected here so it is not inherited.**

**The eviction rule did not fail. It fired for both halves.** The report says it caught the in-queue text and missed the generated file; the retiring build's own record names the file explicitly — `Retired artifacts: plugin/throughliner/scripts/generate_build_view.py, BUILD-VIEW.md, resources/testing/test_build_view.py, resources/testing/test_build_view_gate_disposition.py` (`LOG/2026-08-27-builds-read-the-queue-again-build.md`). Nothing failed at the recording end.

**What is missing is delivery.** That line lands in a session record in this project, and nothing carries it to the projects holding the orphan. So the sender's second route — a new limb on the eviction rule — is the wrong fix: the rule already records precisely what is needed, and a second obligation would duplicate it.

**Changes.** A new shipped list under `plugin/throughliner/` naming each retired artifact and what produced it. `plugin/throughliner/hooks/session_start.py` — read that list and, where one of its paths is still present in the project, say so in one line naming what produced it; **report only, never delete**, consistent with the top-up being add-only and never clobbering anything the user wrote. `CLAUDE.md` — the existing `Retired artifacts:` close line gains one clause: append the same entry to the shipped list. `resources/testing/` — a session-start case, both directions.
Reads but does not change: `SPEC.md`, whose sentence was written at this planning session.
Observable: a fixture project containing a listed path gets one session-start line naming the path and what produced it; a fixture without it gets nothing.

**Rule gate: run — admitted as an amendment, and it adds no detection point.** Parent named: the `Retired artifacts:` close obligation in `CLAUDE.md`, which already fires at exactly the right moment; the manifest append rides that same trigger, the way README-sync rides the SPEC-sync trigger. The authoring half stays host-only — consumers never retire method artifacts — while the reading half ships, because the orphan sits in their projects.

**No format epoch bump:** nothing about an existing project's own documents becomes structurally wrong, which is the only thing the epoch is for.

**Honest limit on verification, stated because it is unusual here:** this project has no `BUILD-VIEW.md` — its own was never generated — so the check cannot be dogfooded against ourselves and is provable only against a fixture.

**It answers the sender's real complaint rather than only the file.** Their point was that the orphan explains itself to nobody and the honest answer takes reading the plugin source; the reported line names what produced it.

#### Self-scoping derives Files from Changes and misses what the observable needs [self-scoping-misses-observable-files]
Found live 2026-08-28, twice in one /next run, and filed by /rescan at that run's end.

/next's self-scoping step reads each item whole and lists the files its instructions name. In practice it reads the **Changes** line, because that is where files are named. An item's **Observable** line routinely names others — the suite that must pass, the sibling doc the acceptance test greps — and those went missing from the Files list both times.

- [cycles-fields-are-single-line] named `session_start.py` in Changes and required "the suites under `resources/testing/` pass, with a case covering a wrapped field" in its observable. Writing that case needed a file the lock denied.
- [ca-commit-steps-untagged] named two close docs in Changes and set its observable as "no untagged commit step remains in the done family" — which `done-audit.md` violated, a third file the finding never noticed.

Both were added to the run's Files list before editing and recorded at the tick, so nothing was built outside an agreed scope. The cost was two interruptions in a run that is meant not to need them.

**Worth weighing at processing: the fix may belong at /plan rather than /next.** The decision step already requires an item to state what changes inside the files it names; it does not require the Files line to cover the files the observable reaches. A scoping step that read both lines would catch it, and so would a decision-step limb requiring the observable's files to appear in Files. The second is cheaper and fires with the user present.

Related: the repeal-grep limb already makes the decision step trace a change's ripple by grep. This is the same shape one field over.

**Settled 2026-08-29 on Claude's recommendation and your agreement: the fix goes at the decision step, and nowhere else.**

**Changes.** `plugin/throughliner/docs/plan.md` — the decision step's enumeration of what a kept item carries in its own prose gains a fifth item: the files the observation reaches are named among the files that change.
Reads but does not change: `SPEC.md`, whose sentence was written at this planning session.
Observable: that enumeration lists five things rather than four, the fifth naming the observable's files.

**Rule gate: run — admitted as an amendment.** Parent named: the four-item enumeration already at the decision step. A fifth unit in an existing list, sharing its grammatical shape, so it costs no freestanding slot.

**Evidence it is followable at no cost, from the session that settled it.** Every item cleared on 2026-08-29 already names its observable's files among its changed files — the register guard names the overwrite-guard suite, [digest-answers-whats-next] names `test_queue_digest.py`, [ritual-declares-writable-paths] names `test_plan_quiet_list.py`. That was habit rather than rule, which is the argument: writing it down costs a clause and the user is in the room when it fires.

**Refused: a matching clause at /next's self-scoping step.** It would duplicate. Fixing the input removes the failure rather than catching it downstream, and /next already handles a genuine ripple correctly — both recorded instances were noticed, added to the run's Files list on approval, and recorded at the tick, so nothing was built outside an agreed scope.

**The cost of that refusal, stated rather than discovered:** every item already in the queue was written under the four-item form, so /next will keep meeting this on legacy items until they are built out. It decays rather than persisting, and an interruption is recoverable, which is why it was taken over a second rule.

#### Delete `resources/captures/`, the folder the emergency revert brought back [repo-debris-proven-fixes]
Filed 2026-08-29 when you asked what that folder was. The answer is that it is not captures at all, and it should not exist.

**What it was.** Created 2026-06-14 to hold a session transcript too large to embed in a queue entry — the capture stayed in QUEUE.md and linked out to the file. So it held *attachments to* captures, which is what makes the name misleading; your own reading of it ("captures go in the queue") is correct and is the confusion the name causes.

**Why it is debris rather than a live folder.** On 2026-08-02 its contents were moved into `resources/testing/`, where re-read-later evidence belongs under the always-loaded rule that `resources/` holds two things only. The 2026-08-09 emergency revert restored the whole working tree to its 2026-08-02 state and resurrected the folder; all four files carry that revert's timestamp. It has been a duplicate ever since.

**Verified at processing, not assumed.** Three of its four files are byte-identical to copies already in `resources/testing/` — checksums compared. The fourth, `532ea359-spec-write-slim.txt` (16KB), exists nowhere else in the repository, so a blind folder delete would lose it. Its only live reference anywhere is one line in `resources/rule_signals.py`'s `ARCHIVAL_PATHS`, sitting directly beside `resources/testing/`, which already covers the surviving copies.

**Changes.** Move `resources/captures/532ea359-spec-write-slim.txt` to `resources/testing/`, then delete `resources/captures/` and its remaining three files. `resources/rule_signals.py` — remove the `"resources/captures/"` entry from `ARCHIVAL_PATHS`.
Observable: `resources/captures/` no longer exists; `resources/testing/532ea359-spec-write-slim.txt` does; `py resources/rule_signals.py .` runs and reports no reference to the deleted path.
Rule gate: not needed — no method rule is authored. Deleting the folder makes the repository match the existing rule rather than changing it.

**Deliberately not in scope: the 4.7MB `Throughliner-icon.png`.** Deleting it would reclaim nothing that matters — the blob stays in git history, and this project refuses history rewrites because its records are full of commit hashes. Whether it belongs at the root is a presentation question, and it rides [repo-cleanup-product-forward].

#### A [user] walkthrough can assert unchecked facts about an outside surface [walkthrough-asserts-unchecked-surface]
Found live 2026-08-28, when [howto-posts-bot-authorship] was driven and halted at its own step 3.

Its walkthrough assumed two things about Discord that nobody had checked, and both are load-bearing: that each how-to topic is a single post, and that the user can delete her opening post so the bot's replacement stands in its place.

Reading the live forum found six topics each holding between two and five further messages of hers plus an attachment — so re-homing "the post" leaves those under her name in a topic the bot would present as its own. And a forum topic's opening message shares its id with the topic, which raises the question of whether deleting it destroys the topic and the bot's replacement with it. A search was run on the user's go and did not settle it: one Discord support thread implies the topic survives with its subtitle reading "Original message was deleted", another was summarised as the opposite, and the developer documentation is clear only about the different case of a thread started from an existing message in a text channel.

**The general shape, which is what makes this worth processing rather than only fixing the one walkthrough.** The rule built earlier the same day covers a doc sentence asserting what a *tool* can do: run the read that would verify it, or write it as intended rather than as fact. A walkthrough step asserting what an outside *surface* permits is the identical failure at a site that rule does not reach — and it is worse there, because a walkthrough is handed to a non-coder to perform with nobody to ask.

Weigh against the project's ban on speculative rules: this is one recorded instance, which the gate accepts as a pointable failure. The candidate fix is an amendment to the same what-would-answer-this rule rather than anything freestanding.

**A safe test exists for the specific question and was not run:** the bot can create its own throwaway topic in the forum and delete its own opening message, which settles it with nothing of the user's at risk. Not run because it posts to a public onboarding forum and needs her say-so.

**Settled 2026-08-29 on Claude's recommendation and your agreement: this item is the rule amendment alone.** The specific Discord question — whether deleting a topic's opening message destroys the topic — was moved onto [howto-posts-bot-authorship]'s own walkthrough in the same turn, along with the finding that six topics each hold further messages of yours. That item is cleared to run, so leaving its blocker filed beside it rather than on it would let a run halt at the same step twice.

**Changes.** `plugin/throughliner/docs/skill-nonspecific-rules.md` — the capability-claim rule under Research and evidence filing widens by one clause: a sentence asserting what a tool can do **or what an outside surface permits** is a claim about the world, so run the read that would verify it, and where no such read exists write it as intended rather than as fact. Name the walkthrough as where it bites hardest, since a walkthrough is performed by someone with nobody to ask.
Observable: that rule's statement names outside surfaces as well as tools, and a grep for its distinctive words returns one statement rather than two.

**Rule gate: run — admitted as an amendment that widens one existing sentence.** Parent named: the capability-claim rule itself, which this item's own filing already identified as the right parent. **The alternative placement was rejected rather than overlooked:** putting it in the `[user]` walkthrough requirements list would have stated one rule in two places, and it would have collided with [co-authoring-txt-draft-loop], which is already adding a bullet to that same list.

**No ordering against the other items naming this file.** [co-authoring-txt-draft-loop] and [cross-project-research-citation] also edit `skill-nonspecific-rules.md`, in different sections; the digest will flag the shared filename, and there is nothing to sequence.

#### View-in-doc pointing fails a reader who cannot open the file [rendering-for-a-reader-away-from-the-files]
**Raised by you, 2026-08-28**, in the middle of a `[user]` walk-through: *"sorry can you please give it to me as a card? I'm on remote control"*. Filed by /rescan at the run's end.

The always-loaded render rule is unconditional and deliberately so: text already living in a project doc is surfaced as a one-line pointer plus a link, never re-pasted, with no user override and no stored setting. The reasoning behind removing the override still stands — the reader away from the file is served by the plain-English summary that opens each item's discussion.

That reasoning assumes the reader *could* open the file if they wanted to. On remote control there is no filesystem to open, so the pointer resolves to nothing and the summary is all there is — which is fine for one queue item and not fine for a fourteen-part deliverable the user is being asked to approve item by item.

What this session did instead, offered as data rather than as the proposal: published the list as an artifact and gave her the link. That worked, and it is not in any rule.

**Settled 2026-08-29 on your agreement.** It is a **class**, not one instance — the same gap appears for any long approval set put to a reader who is not at the machine, whatever put them there.

**Changes.** `plugin/throughliner/docs/skill-nonspecific-rules.md`, the View-in-doc rendering section: pointing stays the unprompted default, and the absolute "Pointing is unconditional — there is no user override" sentence is **reworded out in the same move** rather than having a limb bolted beside it, since a new exception would contradict it rather than extend it. In its place, one user-spoken trigger with the shape the show-first block already uses — the user says they cannot open the file, and doc-resident text comes into the message for the rest of that chat; nothing is stored, and the switch moves one way, toward more showing.
Reads but does not change: `SPEC.md`, whose matching sentence was corrected at this planning session.
Observable: the section states pointing as the default with the away-from-the-file trigger named, and a grep for "no user override" finds nothing.

**Two things this must NOT say, both caught during processing.**

**No detection and no asking.** An earlier draft of the rule read "render it where the reader is, by whatever route the session has" — **your correction, and it was right**: that forces Claude to infer or ask where you are, which defeats the purpose and re-creates the over-asking this method has spent months removing. The trigger is you saying so, and nothing else fires. It inherits the show-first precedent, which considered remote control explicitly and refused to make it a detection trigger, on the ground that nothing should be built to reach an outcome that asking reaches.

**No named mechanism.** What the 2026-08-28 session actually did was publish the list as a page and hand over the link. That worked, and it stays out of the rule: naming it would be a capability claim about every consumer's setup, which nothing here can verify — the reverse-direction check admitted the day before. The rule says the text comes into the message; how a session does that is its own affair.

**Rule gate: run — admitted as an amendment with an eviction.** Parent named: the View-in-doc rendering rule. The absolute sentence comes out as the same edit adds the trigger, so the section carries one statement rather than a rule and its contradiction.

**No ordering against the other items naming this file** — [co-authoring-txt-draft-loop], [cross-project-research-citation] and [walkthrough-asserts-unchecked-surface] each edit a different section of it.

#### The Cowork origin month lives in one article's walk-through record and nowhere else [cowork-origin-month-unrecorded]
**Your account, 2026-08-28**, given while settling the law-prose article's opening claim: the method was originally developed inside Cowork for roughly a month, which is what reconciles your "about four months old" with this repository's first commit of 2026-06-01.

**Corrected 2026-08-29, on your challenge to the paraphrase.** The 2026-08-28 record has "too scared to use Claude Code", which is Claude's wording and not yours. Your account: you found it **intimidating** and **needed support**, and you got that support from nice people on Discord. The correction is being written into `LOG/2026-08-28-law-prose-article-2.md` too, dated, rather than silently replacing what that record says.

It was written into that record as part of claim 1's disposition, because that is where it was said. That is a poor home: a session wanting the project's origin story looks at `CLAUDE.md`'s plugin-history section, which begins at the 2026-06-01 rebuild and says nothing about what came before.

**Checked at processing, on your point that the record reaches back further — it does, and the refinement matters.** No pre-rebuild log entry survives. What survives is a back-reference: `LOG/log-v1.5.2.md` cites "a decision from 2026-05-22 never implemented", ten days before the first commit, and that is the earliest date anywhere in the legacy logs. The word "Cowork" appears in none of them. So the record proves the work predates the repository; it does not say where it happened.

**Changes.** `CLAUDE.md`'s "Old plugin history" section gains a short paragraph. It earns its place operationally rather than as biography: that section exists to stop a session chasing pre-rebuild commits, and this tells it where the earlier work went and what can still be checked. Proposed text, to be written as it stands unless you say otherwise:

> Before this repository existed, the method was developed inside Cowork for roughly a month. Alex moved to Claude Code with support from people on Discord, having found starting alone intimidating. Two traces of that period survive here: the `v17`–`v157` orphan tags, and a single back-reference in `LOG/log-v1.5.2.md` to a decision dated 2026-05-22, ten days before the first commit. No pre-rebuild log entry itself survives, and the legacy logs never name the venue — so this paragraph is the only place it is recorded.

Observable: `CLAUDE.md`'s plugin-history section names the Cowork period and both surviving traces; a grep for "2026-05-22" in `CLAUDE.md` returns it.
Rule gate: not needed — a history fact, not a rule. The mechanical trigger fires because the commit touches `CLAUDE.md`, and this is the "not needed" answer it exists to make visible.

**The public-repository question was put and answered by you giving the accurate version rather than withdrawing it**: this file is published, so the sentence goes out under your name in the form above. Say the word and it comes out or changes.

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

**Settled 2026-08-29 on Claude's recommendation and your agreement. It reaches `done.md` too** — the wind-down re-scan looks back over the same conversation with the same blind spot, so the reworded statement belongs in both.

**The two durable sources are named here so the build does not invent them, one per chat type.** A build chat has its working file, which lists exactly which items were ticked: thirty listed against six visible in the conversation is two counts disagreeing, not a judgement about memory. A planning chat has `git diff HEAD -- QUEUE.md`, which is already how the close recovers what a planning session did. Different artifact, identical shape.

**Changes.** `plugin/throughliner/docs/rescan.md` — the sentence claiming compaction is undetectable from the inside is **reworded out in the same edit** that adds the failure-case statement, since it is the claim being falsified and leaving it standing would put a rule beside its own refutation. What replaces it: the limit sentence stays as the default, and where the cross-check *fails* — the conversation cannot account for work the files record — a second, louder statement fires. `plugin/throughliner/docs/done.md` — the same rewording at the wind-down re-scan.
Reads but does not change: `SPEC.md`, whose sentence was written at this planning session.
Observable: neither doc claims compaction is undetectable; both carry the failure-case statement; a grep for "undetectable" across `docs/` returns nothing.

**What the build must not soften, because it is the whole safety property.** The check admits a warning and never an all-clear. Absent artifacts are positive evidence something dropped out. **Present artifacts prove only that the recent window is intact and say nothing about the earliest stretch — which is exactly what /rescan reaches for**, since compaction takes the earliest material first. A check reporting "I can see the artifacts, so nothing was lost" would hand the user a false guarantee at the one moment they are relying on the scan to be complete. The current sentence over-claims ignorance; the naive fix over-claims knowledge.

**Rule gate: run — admitted as an amendment with an eviction.** Parent named: `rescan.md`'s existing limit statement, which this rewords rather than sits beside. It fires only when it has something to say, which is the shape this project's checks already take.

#### Checkpoint count dropped the ready number you asked for [checkpoint-count-dropped-ready-number]
**Raised by you, 2026-08-29**, on a checkpoint showing one number: *"when I asked for one to be displayed, the other disappeared. I meant we needed both."*

**The record proves it, which is why this is a defect rather than a preference.** `LOG/2026-08-27-checkpoint-carries-remaining-count.md` quotes the wording that produced the current rule: the line *"might more usefully have read '… — 20 ready. X yet to be processed.'"* That is two numbers. The rule that shipped kept one — `plan.md`'s checkpoint now specifies "the remaining-to-process count" and then "nothing else".

**Where the reasoning went wrong.** The justification given was that the other number is "a record of what has been done — so many kept, so many deleted, so many skipped", and that such a tally is clutter while the user is deciding about one item. The ready count is not that. It is the size of the cleared region: forward-looking, and the thing that tells you whether there is work to run. A ban aimed at a retrospective tally swept out a forward one that was never in its scope.

**Your decision, 2026-08-29: "ready", not a session tally.** Both readings were put to you — the size of the cleared region, or a count of what this session has got through — with the note that the second would mean reopening the ban rather than correcting how it was applied. You chose ready, which is also what your 2026-08-27 wording said.

**Changes.** `plugin/throughliner/docs/plan.md` — the checkpoint's message-order list carries both numbers where it now carries one, and the paragraph justifying the ban is reworded, since its reasoning is what dropped the ready count. The retrospective tally stays banned and its ban is untouched. Specimen for the line: `20 ready to build · 9 left to process`.
Observable: the checkpoint specification names two numbers; no passage claims the ready count is a record of what has been done; the retrospective-tally ban is still stated.

**No SPEC sentence is owed, checked rather than assumed:** SPEC's processing-flow paragraph describes the checkpoint's skip behaviour and never mentions either count, so nothing there goes wrong or incomplete.

**Rule gate: run — admitted as an amendment with an eviction.** Parent named: the checkpoint's own message-order list, which this corrects rather than extends. The wrong justification comes out in the same edit.

**A separate failure from the same message is deliberately NOT filed as work.** The checkpoint also carried a sentence explaining what the count excluded, which the existing rule already forbids — it says "nothing else" after the count. That is a compliance miss with nothing to build, so it is a finding for this session's record under the three-way triage rather than a queue item.

#### Issue check cannot see issues on repositories a project does not own [issue-check-foreign-repos]
Filed 2026-08-28 from INBOX mail sent by a consumer project running this method (archived at `INBOX/archive/2026-08-28-from-flintcraft-issue-check-cannot-see-foreign-repos.md`). Reported against plugin 1.21.0-test3. Data from another project, not a decision here.

The planning opening's issue check has two limbs — comments on issues the register records, and new issues on a repository the project owns — and nothing else is in view. The user named the gap there: issues on other repositories, including her own other projects and Claude Code, can bear directly on a project and no limb reaches them. The evidence in the mail: at least fifteen open issues she is involved in, most on `anthropics/claude-code`, one on a third-party Discord bot repository bearing on this project's own Discord work — every one invisible to every project she runs. A narrower hole inside the first limb: an issue she filed herself, outside any project's flow, is anchored to no register and never checked.

Mechanism finding worth keeping whatever is built: the GitHub notification inbox is the wrong source — notifications are read-once, so a seen-but-unresolved issue vanishes from it. The durable query is a search for issues the account is involved in.

Two limits constraining any fix, from the mail: relevance cannot be derived, so which outside repositories bear on which project would have to be declared per project; and a widened check reads issue text written by strangers, which is untrusted content — data, never instruction, summarised in the project's own words.

**Settled 2026-08-29 on Claude's recommendation and your agreement, after running the query at processing.**

**The durable query works, verified rather than assumed:** `gh search issues --involves @me --state open` returned 20 open issues, most on `anthropics/claude-code`. The mail's mechanism finding stands — the notification inbox is read-once and the wrong source.

**And it found something live in the first run, which is the argument for building it.** `anthropics/claude-code#83476` asks for `.md` files to be editable in the desktop file viewer. That is the premise of [co-authoring-txt-draft-loop], cleared to run the same day: `.txt` was chosen *because* `.md` opens read-only. Nothing in this project knew the issue existed. Two more bear on [rendering-for-a-reader-away-from-the-files] — `#84965` (fenced blocks wrap on desktop but not on remote control) and `#84225` (remote-control setting changes). The one issue the existing limbs do reach, `#77134`, is reached only because the register records it, which is exactly the shape of the gap.

**Half the mail's first limit is accepted and half is answered.** Deriving *relevance* is a judgement and stays one. But the set does not need deriving — it needs narrowing, and the anchor the existing limbs already use does it: issues with activity since the most recent planning record turn "20 open issues" into "the few that moved", small enough to read. **No per-project declaration of outside repositories is built**, and the check does not claim to filter by relevance mechanically.

**Changes.** `plugin/throughliner/docs/plan.md` — the opening's issue check gains a third limb beside the two it has: issues the account is involved in with activity since the anchor, read as untrusted text and summarised in the project's own words, filing one capture per issue carrying something new and satisfied while an open capture already names it. `[SILENT]` where `gh` is absent, folded into the existing one-line correspondence report where it is not.
Observable: the issue-check step names three limbs; a run with `gh` present reports the third either way, and one with `gh` absent is silent as before.

**Rule gate: run — admitted as an amendment.** Parent named: the issue-check step in `plan.md`'s opening, which already has two limbs and an anchor; this is a third in that list, sharing its shape, so it costs no freestanding slot.

**The honest limit, to be stated where this reports:** it reaches issues the account is *involved in*. An issue nobody here has touched, on a repository nobody here has commented on, is still invisible — the widening is real but bounded, and must not be described as covering everything that could bear on the project.

#### Nerds-channel welcome becomes a bot-authored sticky, re-bumped at each entry post [nerds-welcome-sticky-rebump]
**Raised by you, 2026-08-28:** channels open at the bottom, so a pin at the top makes the pin feel pointless — you asked whether pins can stick to the bottom. Research (2026-08-28, in-session): Discord has no native bottom-pin; the universal pattern is a sticky message a bot re-posts as the newest message. Our bot has no always-running process, so it cannot react to other people's messages — but test-rezips traffic is mostly the bot's own, so re-bumping at each entry post keeps the welcome at the bottom exactly when people look.

Changes: the welcome text moves to a source file in the repo (`resources/nerds-welcome.md`), bot-authored on its first sticky post — the same bot-maintainability reasoning as [howto-posts-bot-authorship]; `resources/discord_post.py`'s entry-posting step gains the re-bump: after posting an entry to test-rezips, delete the bot's previous welcome message and repost the source file's text as the newest message. The user's yes to posting the entry covers re-bumping the unchanged welcome bytes; any change to the welcome text needs its own explicit yes, under the standing send gate.
Observable: after an entry post, the channel's newest message is the bot-authored welcome, byte-identical to the source file.
Refused: a third-party sticky bot — nothing currently needs a bottom-sticky in a human-traffic channel, and adding an outside bot is a decision for when something does; a gateway/daemon listener for our own bot — the script-driven architecture stands.
**Lifted 2026-08-28.** The hold was ordering, not concept: [rezip-archive-mirrors-nerds-channel] was rewriting the same posting step this extends, and two builds editing it must not interleave. That build shipped and its tick is confirmed (`LOG/2026-08-28-rezip-archive-mirrors-nerds-channel-build.md`), so nothing is editing `resources/discord_post.py` any more and the interleave risk is gone. One thing for the build to read first: [rezip-archive-blocked-by-scope-lock] records that the archive step this sits beside was refused by the scope-lock on its first run, so the entry-posting path is live but the archive write is not yet.

#### Outbound register gains a deletion guard, since the mailbox is gitignored by design [sent-register-untracked]
Filed 2026-08-28 from INBOX mail sent by a consumer project running this method (archived at `INBOX/archive/2026-08-28-from-flintcraft-register-tracking-and-defect-watch.md`, report 1 of 2). Reported against plugin 1.21.0-test3. Processed 2026-08-28.

`INBOX/sent.md` is the permanent outbound register — what the repeal check greps for claims already announced — and `INBOX/` is gitignored on every path, so it has no history, no backup, and one accidental deletion ends it.

**The exposure is per-file, found by reading the folder at processing rather than taken from the report.** The register holds no absolute paths at all and names only projects that are already public. The address book beside it holds absolute paths identifying the user and their machine, and one entry naming a real person alongside a sensitive matter. So the blanket ignore is wrong for one file and load-bearing for the other, which is why the fix is not a folder-level change.

**Severity is lower than the report has it, and the item says so rather than inheriting the framing.** Most register lines point at LOG entries carrying the posted text verbatim, and `LOG/` is tracked — so what a post claimed survives in committed history. What would be lost is the index itself, which is what the repeal grep runs over.

**Changes.** `plugin/throughliner/hooks/pre_tool_use.py` gains a guard beside `_is_log_entry_overwrite`, refusing a Write whose target is `INBOX/sent.md` and a shell command that deletes or truncates it, wired into the same unconditional branch so it fires under every scope; Write-only like its sibling, so Edit and append are untouched. `resources/testing/test_pre_tool_use_overwrite_guard.py` gains cases in both directions. `README.md`'s "What it does" list gains one clause.
Reads but does not change: `SPEC.md`, whose sentence is written at this planning session.
Observable: the suites under `resources/testing/` pass, with a case proving a Write onto the register is refused and an Edit of it is not.

Refused: un-ignoring the register in `.gitignore` — this repository is public, and the user declined publishing it ("not really", 2026-08-28); the sender's own objection stands too, that `/setup` refreshes scaffolding so a hand-added exception could be silently overwritten while everyone believes the file is safe. Refused: moving the register out of the mailbox, the sender's suggestion — anywhere outside the ignored folder is tracked, so it fails on the same publication ground.

Red flag · State: cleared — designed out for the reported failure, a session or script destroying the file. Residual stated and accepted by the user at processing: a hook can only refuse what goes through Claude's tools, so deleting the folder by hand or losing the disk is untouched.

#### Co-authored drafts go to an editable `.txt` with a read-back loop [co-authoring-txt-draft-loop]
**Your proposal, 2026-08-28**, split out of [co-writing-flavour] at processing on your direction. **Your reason, in your framing:** co-authoring keeps getting shaped as Claude work, and the painstaking part is explaining a change to Claude when it is much easier to go in and edit the text yourself.

**Your observation the same day overturns a tested record.** `CLAUDE.md` states, as tested, that the desktop side panel opens `.md` read-only and `.txt` "not at all" — which is why the Discord posting flow detours through Notepad. You checked live: `.txt` **is** editable in the side panel and carries a save button, so you control when your edits land. The finding is stale and the detour is unnecessary.

**External dependency, found 2026-08-29 while processing [issue-check-foreign-repos] and written here because it bears directly on this item's premise:** `anthropics/claude-code#83476` asks for `.md` files to be editable in the desktop file viewer. `.txt` is chosen here *because* `.md` opens read-only; if that issue ships, the format choice is no longer forced and the rule should say `.md` rather than carry a workaround nobody needs. **Do not wait on it** — it is an open feature request with no ship date, and the `.txt` route works now. Re-read it if this item is still unbuilt when someone next opens it.

**Changes.** `plugin/throughliner/docs/skill-nonspecific-rules.md` — the `[user]` walkthrough block gains a fourth subordinate requirement alongside the stored-texts, verification-claims and ends-at-the-observable ones: where a step has the user edit text Claude drafted, the draft is written to a `.txt` file whose location the step names, and Claude reads it back only when the user says to, asks whether there is more, and loops until they say they are finished. `CLAUDE.md` — the draft-edit flow sentence corrected to the live behaviour and pointed at the general mechanism, with the Notepad route removed. `README.md` — the "What it does" list gains one clause, riding the SPEC-sync trigger.
Reads but does not change: `SPEC.md`, whose sentence was written at this planning session.
Observable: `skill-nonspecific-rules.md`'s walkthrough block carries the fourth requirement naming the `.txt` draft and the read-back loop, and a grep of `CLAUDE.md` for "not at all" and "Notepad" returns nothing.

**Rule gate: run — admitted as an amendment.** Parent named: the `[user]` walkthrough requirements block in the always-loaded rules, which already carries subordinate limbs, so this consumes no freestanding slot. Failure it answers is recorded rather than speculative — the law-prose claims session, plus your report that the shape has felt wrong throughout. Evicted in the same move: `CLAUDE.md`'s Notepad sentence, both stale and superseded.

Refused: pasting a draft into chat for the user to describe edits to — your recorded reason, that describing a change is painstaking where making it is not. Refused: Notepad as the route — superseded by the side panel editing `.txt` directly. Refused, from the parent item: processing each of a draft's claims one at a time, your verdict being that it was tedious and not time-saving.

The routing question this does not answer — planning work surfacing inside a walkthrough — stays on [co-writing-flavour] by your decision to split it off.

#### Queue digest gains a what's-next mode, so a pick costs one scoped call [digest-answers-whats-next]
**Raised by you, 2026-08-29**, from watching a single skip cost 350 tokens of tool work before a word of reply, and sharpened by your question about whether an MCP server would make it cheaper.

**Measured at processing, which is what settles the shape.** Re-deriving the ladder's rung and its top item by hand — the route taken twice this session — costs about 350 tokens, most of it Claude emitting the script rather than running it. Re-running the whole digest instead, which is what the procedure currently tells a session to do when the picture needs to be current, produces 14,311 characters, roughly 3,600 tokens. An answer scoped to the next pick alone is a few hundred. The sanctioned route is the expensive one.

**A correction recorded so it is not repeated.** Claude first argued the fix removes the operation entirely, since the opening digest would already carry the field. That is wrong: the rung is re-derived at every pick as the queue changes — items leave, are skipped, new captures land — which the procedure explicitly requires. It is a recurring cost, not a one-off.

**Changes.** `plugin/throughliner/scripts/queue_digest.py` gains a mode that answers only *what is next*: which rung the ladder fell to, that rung's top item, the item's starting line number, and its text — nothing else. This requires it to compute the incoming-citation count per entry, which is rung 2 and which nothing computes today. `resources/testing/test_queue_digest.py` gains cases, including a rung change between two calls. `plugin/throughliner/docs/plan.md` — the re-run-the-digest instruction and the per-pick checkpoint name the scoped mode instead of a full re-print.
Reads but does not change: `SPEC.md`, whose sentence was written at this planning session.
Observable: the scoped mode prints the rung, the top item's slug, its starting line number and its text; the suite passes with a case proving the rung reported changes when the queue changes beneath it.

**Rule gate: run — admitted as an amendment.** Parent named: `plan.md`'s existing instruction to re-run the digest whenever the picture needs to be current. The scoped mode replaces the full re-print at that site rather than sitting beside it, so the old sentence is evicted in the same edit and no freestanding rule is added.

Refused: building this as an MCP tool now — the measured saving comes from scoping the answer to one item, not from the transport, and a script flag reaches the same number; the transport comparison belongs to [run-token-cost-audit]. Refused: dropping rung 2 as too heavy for a default — it is heavy only because nothing computes it, and it carries the ladder's actual ordering principle.

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

#### [audit] Where a /next run's tokens actually go, measured against the MCP-server proposal [run-token-cost-audit]
**Raised by you, 2026-08-28**, from a build brief you brought in proposing a local MCP server shipped inside the plugin — purpose-built tools (`tl_log_append`, `tl_queue_next`, `tl_status`) replacing read-find-parse-write with one structured call. The brief is Claude-authored, so its claims are unverified; its own step 1 is to audit a real run first, and this item is that step.

**Measured at processing, and it is why this is an audit rather than a build.** A `/next` run loads before it edits anything: the always-loaded rules (76KB), `next.md` and `next-build.md` (55KB), the close docs (51KB), SPEC.md (83KB), and the cleared region of QUEUE.md (of 108KB) — roughly a quarter of a megabyte an MCP server does not touch. The one place structure could have replaced reading was deliberately refused on 2026-08-17: the digest carries computed facts and the file carries the reasoning a build needs, so a planning session pays both. What was NOT measured is the numerator — how many tool calls a real run spends on navigation — which is exactly what this audit counts.

**What it reads — two runs, not one, on your direction 2026-08-29.** A `/next` run and a `/plan` run are characteristically different and must be measured separately: a build run reads the cleared region and SPEC once and then edits files, while a planning run re-derives its ordering at every pick, re-reads the queue, and writes items back. A figure from one says nothing about the other. Sources: the 2026-08-28 30-item build run, and the 2026-08-28/29 planning run that raised this — both from `.claude/projects/<project-slug>/*.jsonl`, preprocessed per CLAUDE.md's transcript-reading procedure (strip tool_use/tool_result and thinking to a slim file, then read that). Reads only; findings go to Unprocessed as captures.

**Observable:** a count of pure-navigation tool calls in each of the two runs, stated separately and against the fixed read cost above, so the two can be compared rather than one asserted.

**Two data points already on the shelf, both from the planning side.** Re-deriving the ladder's rung and top item by hand cost about 350 tokens per pick, most of it Claude emitting the script rather than running it; re-running the whole digest instead — the route the procedure currently sanctions — produces 14,311 characters, roughly 3,600 tokens. [digest-answers-whats-next] takes the scoped-answer fix, which is transport-agnostic. What is left for this audit is whether MCP beats a script flag once the answer is already scoped, and the honest prior from these numbers is that the scoping is where the saving lives.

**Two findings already on the shelf for whoever picks this up.** Half the brief's table is already built as scripts rather than MCP tools — `queue_digest.py` returns the queue as structured facts in one call and `reorder_queue.py` does moves and marker placement byte-for-byte — so the real delta is script-versus-tool, not tool-versus-nothing. And the write-side tools (`tl_log_append`, `tl_queue_done`) are the exact shape `pre_tool_use` refuses: a project file written through a script rather than the editing tools, blocked because the shell's view can be stale, with the queue tool as the one carve-out. An MCP server could be carved out the same way, but that is a rule change rather than only a build.

**Unverified and to be checked before any build is scoped:** that a plugin may define an MCP server in `.mcp.json` at its root, that Claude Code starts it automatically when the plugin is enabled, the `mcp__plugin_throughliner_<server>__<tool>` naming, and whether the plugin-dev mcp-integration skill still sits at the path the brief names.

**Refused at processing: filing the MCP build now.** It cannot state which files change or what changes inside them until the audit says which operations dominate, and "research this, then build that" is the shape the decision step must not pass. The build item gets filed if and only if the audit finds navigation costs enough to matter.

#### [audit] Rule changes since the last compliance audit are uncovered [compliance-audit-lag]
Filed 2026-08-28 by `resources/rule_signals.py`'s audit-lag check, under the slug it prints. Nothing had filed it and the slug was open in neither section.

The check reports rule-bearing commits since `2026-08-27-compliance-audit-lag.md` that no compliance audit has covered. The count will have grown by the time this is processed: the run filing it is itself editing most of the files below.

**Delta scope, refreshed at processing 2026-08-29 by re-running the check as this item instructed:** three rule-bearing commits since the anchor record, covering `CLAUDE.md` and, under `plugin/throughliner/docs/`, `done.md`, `done-audit.md`, `done-build.md`, `done-plan.md`, `feedback-and-inbox.md`, `migrate-checklist.md` and `next-audit.md`. **The done family is what is uncovered, which the original snapshot did not show** — it named `next.md`, `plan.md`, `rescan.md`, `setup.md` and `skill-nonspecific-rules.md` instead, because it was computed mid-run against files that run was still editing. **Re-run the check on the day and take its list, not this one** — the same reason the snapshot was wrong is still live.

**Placement is load-bearing rather than incidental.** It sits at the end of the cleared region, where `[audit]` items go, and that ordering is what makes this pass worth running: [digest-answers-whats-next] and [ritual-declares-writable-paths] both edit `plugin/throughliner/docs/plan.md`, so an audit running after them covers those changes instead of leaving them to re-arm the check immediately.

**The other four checks were clean at processing**, and the growth report showed the always-loaded rules up 49 statements over thirty commits — a measurement with no threshold behind it, so nothing there is a finding.

The standing criteria are in `resources/method-compliance-audit-checklist.md`: four lenses — self-authoring compliance, response-shape tag placement, narration drift, and decision history in operative text. Reads only; findings go straight to Unprocessed as captures.

#### [audit] Inventory the root and `resources/`: what each file is, and what still reads it [repo-inventory-audit]
Filed 2026-08-29 from your framing that you have no idea what half the files in the repository are for. An inventory that explains each one is the answer to that; deciding their fates is separate work, and this reads and reports without deleting anything.

**Scope: the repository root and `resources/`.** For each entry, report three things — what it is, what still reads or references it, and when it was last touched by anything other than a bulk commit. `LOG/` entry files are excluded from the fate question: 1,375 session records are the archive working as designed, not clutter. `LOG/index.md`'s size is reported as a fact (316KB, larger than the archived June and July indexes together) without a verdict attached.

**One mechanical test to apply, derived at processing rather than invented.** The 2026-08-09 emergency revert restored the whole working tree to an earlier state, so anything retired in the week before it came back. 329 files still carry that revert's timestamp. **Restored is not the same as debris** — most of those are LOG entries and research findings that were deliberately restored, and correctly. What made [repo-debris-proven-fixes] debris is that its contents had been *relocated*, so the folder returned as a duplicate. So the test is: among files the revert restored, find those that duplicate something elsewhere in the tree, or that nothing anywhere references.

**Known starting points, so the pass does not begin cold:** `resources/` mixes live tooling with dead history at one level — `discord_post.py` and `rule_signals.py` sit beside `plugin-behaviour-retired.md`, `2026-08-09-emergency-revert-plan.md`, `queue-two-section-migration-recipe.md` and a stray `reader-test-workflow.js`. At the root, `FABLE-BRIEF.md` and `ANNOUNCEMENT-IDEAS.md` (153KB) are both worth a line saying whether anything still reads them.

Observable: one finding per root entry and per `resources/` entry, each naming what it is and what references it, filed to Unprocessed as captures.

**The honest limit, to be stated where this reports:** an inventory finds what it can trace. A file nothing references may still matter to a person, which is why the fates stay yours and this pass proposes none.

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

## Unprocessed

#### Last session advises building [bot-cannot-create-forum-topics] next [forward-advisory]
Filed at the 2026-08-29 planning close. The cleared region holds 28 items, rebuilt from two, and it is ordered deliberately rather than by accident — so a /next run starting at the top is the recommendation, not a planning run.

**Why that item is first.** It is small, it was found by trying rather than assumed, and it blocks two items the user made her top priority the same session: [ports-forum] cannot post its four topics without it, and the showcase guidelines she approved are sitting on it unposted. The four port items follow immediately behind, in build order.

**One deadline is live.** The weekly release falls due 2026-09-02, and [rezip-archive-blocked-by-scope-lock] — sixth in the region — is what lets the release read a build from the archive. It has a hand fallback written into it, so Wednesday is not blocked either way, but building it before then removes the need.

**Nothing unprocessed contradicts the top of the region.** [bot-cannot-read-permissions] edits the same file as the first item, which is ordering rather than a block, and it is written on both.

**One thing a planning run would do that a build cannot:** twelve captures are waiting, four of them filed by this session's own /rescan, and the tips cycle's material still ranks as ordinary captures until [cycle-material-captures-still-ranked] is settled — so the next planning session will meet seventeen tip items again.

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
**Ordering, written on both items per the known-ordering rule (2026-08-29):** [ritual-declares-writable-paths] builds before or alongside this, so the definitions this migration writes carry the writable-paths field from the start rather than being revisited. Not a blocker either way — the two are independently buildable.

#### Demo-session guide for the legal-case YouTube video [legal-demo-video-guide]
**Your idea, 2026-08-28, processed at raising.** One of the first YouTube videos: an essentially unscripted demo where you set up a fresh legal-case-shaped project with Throughliner on camera, phrasing your questions as though you don't know what Claude will suggest, and steering toward a structure similar to one you already proved — a family-law source-of-truth template and method in your legal project (located 2026-08-28; the path and matter names are deliberately not recorded here, per the scrub rule on identifying paths). You never show or use the template; the guide's job is knowing the destination so your naive-sounding questions reliably arrive there. Your virality read: a legal case is a very weird project type to run inside Claude Code, which is exactly why it travels.

How it gets made: hand-work with you in a dedicated session — the drafting reads the legal project's sensitive files, so it is done deliberately with you present, not inside a build run. Output lands in `YouTube/` (gitignored once [youtube-folder-gitignored] ships), which keeps the guide and any matter-adjacent notes out of this public repository. This capture holds the intent; the dedicated session does the work, and the close there records it.
Blocked by: [youtube-folder-gitignored]
The hold is real: the guide must not be written into a tracked folder, so the ignore line lands first.

#### Pop the YouTube folder out into its own project [youtube-subproject-popout]
Your direction, 2026-08-28: the `YouTube/` subfolder starts life inside this project and pops out as its own full Throughliner project later — your timeframe, "maybe in a month or something", written as the date below and adjustable on your word. The pop-out is the shipped subprojects flow: /setup run inside the subfolder reads this project's product truth, confirms which part it covers with you, and tells the parent it moved out. Until then the folder is gitignored working space ([youtube-folder-gitignored]).
Not before: 2026-09-28

#### Lesson video: deterministic versus probabilistic output, taught through Throughliner's tool-finding [determinism-lesson-video]
**Your idea, 2026-08-28, filed at your direction; the arc and the heuristic are yours.** A different video type from the legal-case demo — a lesson, not a case study, though it carries case-study elements rather than being example-free (your framing).

The arc: first show what Throughliner does when it finds tools for you — accomplishing things it is not necessary to use AI for. Then identify what is different about those tasks: beyond not needing the AI directly, their output is **deterministic**. The teachable heuristic, in your words: *a good way to recognise when an output is deterministic is when you can imagine a tool that might accomplish it.* The payoff is double — you stop spending valuable AI generating things a different way every time (probabilistically), and you start identifying and suggesting CLI tools yourself, even when Claude Code hasn't.

Grounding on the shelf: the method's own CLI-tool rule and capability check ("name the tool that would do the work") are the shipped behaviour the lesson demonstrates. Designs with the other video capture, [legal-demo-video-guide], in the YouTube folder's own sessions. (The intro-video capture that used to be named here was deleted 2026-08-29 — the user is exploring that concept outside the queue.)

#### Reusable priming prompt for demo recording sessions [recording-priming-prompt]
Filed 2026-08-28 from the site project's mail (archived same day), the idea Alex's — raised in that project's planning session and sent here as the side that owns it. A prompt given to Claude before any case-study recording session: this session is a demo, and it must not put revealing information on screen. Her reason, carried from the mail: demoing a real personal project exposes more than the method being shown — the structure of the work, what is being tracked — and preventing it at the source is far cheaper than blurring it in the edit afterwards. Reusable by construction, since every case-study recording wants it; the [legal-demo-video-guide] session is its first consumer, so the two design together in the YouTube folder's sessions.

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

#### Repo cleanup: foreground the product, and treat everything peripheral [repo-cleanup-product-forward]
**Raised by you, 2026-08-29.** Your framing: you have no idea what half the files littering the repository are for, many may have outstayed their welcome, others need better organising or gitignoring — and you want the repository more product-forward, foregrounding what Throughliner is, with anything peripheral to the product itself treated by delete, reorganise, or gitignore.

Filed at the moment you raised it so the reference from [post-drafts-leave-the-queue] resolves; processed in the same session, and split there into three pieces on your agreement. [repo-debris-proven-fixes] took what was already provable; [repo-inventory-audit] answers what each file is; this item keeps the presentation question, which is the one that needs your taste rather than a finding.

**The question this owns: what a visitor to the repository sees first.** The root currently holds seventeen tracked files with no separation between the product and the workshop — `README.md`, `INSTALL.md`, `LICENSE` and `SPEC.md` alongside `CLAUDE.md` (82KB), `QUEUE.md` (141KB), `ANNOUNCEMENT-IDEAS.md` (153KB), `FABLE-BRIEF.md`, three image files and the dot-files. Foregrounding the product means deciding which of those stay in view and which move into a folder.

**One fact that changes what is worth doing, found at processing.** `Throughliner-icon.png` is 4.7MB, roughly 40% of the working tree, and **deleting it reclaims nothing that matters**: the blob stays in git history, and this project refuses history rewrites because its records are full of commit hashes. So the icon is a presentation decision only — where it sits, not how big the repository is. There is already a 191KB badge version beside it.

**Held on the audit rather than designed now.** What to foreground cannot be settled before knowing what each file is, which is exactly what [repo-inventory-audit] produces. Deciding twice is the failure this avoids.

**Two items wait behind this**, so the chain is stated rather than discovered: [post-drafts-leave-the-queue] needs a destination that only this can give, and it is held on this item as this is held on the audit. A chain of three resolves; it is slow rather than stuck, and shortening it means settling the drafts destination independently, which is yours to call.
Blocked by: [repo-inventory-audit]

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

