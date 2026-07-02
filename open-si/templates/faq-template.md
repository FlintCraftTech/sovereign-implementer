# FAQ

Answers to common questions about how this project's workflow operates.

## What do /plan, /next, and /done each do?

They split work into three modes. **/plan** is for thinking — queue management, captures, design questions. **/next** is for doing — picks the top batch and builds it. **/done** is for closing — records, updates docs, commits. Always in order: plan, do, close.

## How do the four commands fit together day-to-day?

You run **/setup** once, right at the start of a project. After that, every working session is either **/plan** (thinking and organising — managing the queue, adding ideas, resolving questions) or **/next** (building — it picks the top item and does it). You'll run /plan as often as planning needs, and /next once per item as you work down the queue: planning repeats for long stretches, building repeats across many items. However a session goes, it ends the same way — **/done** to record what happened, then **/clear** to start fresh. The one habit that matters: always /done before /clear, so each session is saved before the context resets.

## What does /setup do, and do I run it more than once?

/setup adopts your project folder into the method: it scaffolds the working docs (SPEC.md, QUEUE.md, the LOG folder, and this FAQ) and interviews you with five short questions to fill in SPEC.md — what the project is, who it's for, how it works. You run it once per project. If you run it again later — for instance after a plugin update — it only backfills scaffolding that's missing; it does not overwrite or reconcile content you've already written. So re-running it is safe, but it won't refresh or rewrite your existing docs.

## Why does setup ask which editor I use?

So Claude can point you to your open docs instead of re-pasting their text into the chat. When Claude needs to show you a captured idea or the next batch of work, that text already lives in one of your project files (usually QUEUE.md). If Claude knows the editor you keep those files open in, it can just link you to the file — "it's in QUEUE.md" — and you glance at it there, rather than Claude copying the whole block into chat every time. Over a project's life that saves a real amount of tokens. The question is optional: skip it and nothing breaks — Claude simply quotes the text inline the way it always has. It's asked once, during /setup, and never again.

## What's the difference between Batches and Captures in QUEUE.md?

**Batches** are ready-to-build work — entries under Build/Test subheadings, worked top to bottom. One batch per /next session. **Captures** is an inbox — ideas, questions, and observations from builds or between sessions. Not actionable yet — during /plan, each gets discussed and either promoted, parked, or dropped.

## How are entries organized in the queue?

Batches group entries under **Build**, **Test**, and **Audit** subheadings. Build entries create or change things. Test entries verify things work. Audit entries review what exists and route findings back into the queue. Not every batch needs a Test section — only when verification isn't self-evident. Captures are plain bullets — each carries its own reasoning inline.

## Why did my audit file its findings as captures instead of writing them into a doc?

Because an audit's job is to find things and route them for review — not to write them anywhere durable yet. Everything an audit turns up goes into Captures, where the next /plan session and you look it over before any of it lands in a real document. That review step is the whole point: it keeps an unchecked finding from going straight into a doc you'll rely on. So if you want a lasting findings document — a report, or a summary for someone outside the project — that document is its own piece of work, built *after* the findings are vetted. The order is: the audit files findings as captures → /plan reviews them with you → a build session writes the document from the ones you kept. And if you happen to set up an audit batch that points at a document to write into, Claude won't silently follow it — it'll notice the mismatch and ask which you meant: file the findings for review first, or run it as a build that writes the doc now.

## What is `/next freeform`?

A fourth kind of /next session, for work that isn't a build, a test, or an audit — an ad-hoc change, talking through edits you've already made, or surfacing something without the pressure of sorting it out right away. Reach for it when none of the other three fit. It keeps the safety rails — Claude still asks before touching a file, and still flags risks — but drops the fixed step list, so it suits work that doesn't know its shape up front. One thing it won't do: process your captures. A freeform session can jot ideas into Captures, but promoting, parking, or dropping them is /plan's job — Claude will say so and offer to move to /plan when captures pile up.

## What is the Red flags section at the top of QUEUE.md?

It's where Claude lists security and privacy risks it has spotted — anything that could expose your data or your users' data, or amount to a breach. It sits at the very top of the queue so it's the first thing you see each session; a risk you should know about shouldn't be buried. The section stays empty until something comes up.

Each red flag carries one of three states:

- **Open** — the risk has been raised but not yet dealt with.
- **Resolved** — the risk has been fixed or designed out; the work no longer carries it. This includes a risk Claude designs out during planning, before any code is written — it's still recorded here as resolved, with a note on how.
- **Accepted** — you were told the risk plainly and chose to go ahead anyway. That choice is written into the session log: what you were warned about, and that you agreed to proceed. It's a clear record if the risk ever matters later.

Claude raises and updates these — you don't maintain the section. Accepting a risk is a decision only you can make.

## What is the "Deferred tests" section in QUEUE.md?

A waiting list for tests that couldn't run in the session that planned them — some only become checkable later, some need you to try something, some wait on an outside event. When /done closes a session and a planned test couldn't run, it adds a one-line entry here: which batch the test came from, what to verify, and what confirms it. /plan reads this list each session and folds the ones that can now run into a test batch; and when a later session happens to confirm one along the way, /done removes its line and records the result in the session log. Claude writes and clears this section — you don't maintain it.

## Why do some tests run straight away and others wait?

Claude runs every test it can in the same session it builds in — that's the default. A test only waits for one of two reasons: a person has to run it (a visual check, or tapping through a screen — something Claude can't see or do), or it needs a device or setup that isn't connected yet. Tests that wait go on the "Deferred tests" list and get picked up once they can run. Waiting is the exception, not the norm — if a test can run now, it runs now.

## Why does Claude sometimes ask me to run a test instead of running it itself?

Because some tests need something only you can provide — and when that's the case, Claude tells you plainly what the test checks, what it needs, and why it can't run it. A test might need you to look at a screen and judge how something appears, tap through your app on a phone, or run a command in a terminal Claude can't reach. Claude usually can't see your setup, so it doesn't guess what you can or can't do — instead it names exactly what the test requires ("needs the terminal," "needs a phone connected," "needs you to look at the screen") and leaves it to you to judge whether that's yours to do. If a test needs nothing of yours, Claude just runs it — handing one to you is only ever for the checks that genuinely need you.

## Do I need to use the terminal to install or update SI?

No. The plugin installs and updates through Claude Code's own plugin system, and **Claude runs those commands for you** — you just ask it in plain English inside a Claude Code chat. You never open or type into a terminal. "Marketplace" and "CLI install" sound technical, but in practice they mean: Claude Code knows where to find this plugin (a marketplace is just the published location on GitHub), and it fetches and installs it with a couple of commands it runs itself. To install, you ask Claude Code to add the `FlintCraftTech/sovereign-implementer` marketplace and install `sovereign-implementer@flintcraft`; to update later, you ask it to run the update. Either way it's Claude doing the typing, then you fully restart the app so the new version loads.

## How do I find out when there's a new version of the plugin?

GitHub can email you whenever a new version of Sovereign Implementer is published. Go to the plugin's page at `https://github.com/FlintCraftTech/sovereign-implementer`, click **Watch** near the top right, choose **Custom**, tick **Releases**, and click **Apply**. After that you get an email each time a new release goes out. It needs a free GitHub account, which costs nothing to set up.

## I just updated the plugin — how do I check it still works?

Run a quick session and confirm the new behaviour works the way you expect — that check is itself a testing session. The method saves up exactly these checks for after an update: when something could only be confirmed once the update was installed, it's set aside, and the first session after you reinstall is when it becomes checkable. So when you open a session right after updating, Claude may point out that now's a good moment to confirm the update — run /plan and it'll line up what's worth checking into a quick test session.

## What is the "build stamp" the plugin records at the start of a session?

A short fingerprint of the installed plugin's own files — a content check that reflects exactly what's installed right now, not just a version number. Its job is to tell whether a plugin update is genuinely in place after you reinstall. Some checks the method sets aside (on the "Deferred tests" list) can only be confirmed once an update is actually live, and a version number alone can miss a change that didn't bump the version — so the stamp gives Claude a reliable yes/no on whether the installed files are current. It runs behind the scenes: you don't see it or manage it, and nothing about your own project goes into it — it only fingerprints the plugin's files.

## I closed the app in the middle of a build. What happens when I reopen it?

Nothing is lost. `_build.md` tracks progress. When you reopen, session start detects the unfinished build. Run /next to resume.

## Is it safe to clear the conversation or start a new session between steps?

After /done, yes — everything is recorded in the session log and committed, so a fresh conversation loses nothing. Before /done, the plugin can still recover: it reads its working file (`_build.md` or `_plan.md`) rather than relying on the conversation, so an interrupted build or planning session picks up from the file. But closing with /done first is the clean habit — it's the moment the work becomes a permanent record instead of something the plugin has to reconstruct.

## What's the difference between committing and pushing, and why does Claude only ask about pushing?

Two different saves. **Committing** saves a snapshot of your work to your project's history on your own computer. It always happens when you close a build session, and you don't have to approve it — the snapshot's description is the session summary you already approved. **Pushing** additionally sends that snapshot to a remote backup, like GitHub, if your project has one set up. So at the end of a build, Claude commits first (the safe, local save), then asks whether to also push (the part that sends your work somewhere external). If your project has no remote set up, there's nothing to push to, so Claude just commits and doesn't ask. Planning and test sessions commit too, but never offer a push — they record bookkeeping, not a change to release.

## Why did Claude say my new change has to wait for a fresh session?

Because the close (/done) is for recording and saving the work that was just finished — not for starting new work. If you ask for something brand-new while Claude is closing a session — a redesign, a new feature, a change to something that already worked — Claude finishes the close first, then that new change becomes its own build session (or gets noted for later if it isn't urgent). The one thing Claude will fix on the spot is a genuine bug in what was just built — that's finishing the job, not starting a new one. Keeping new work to its own session means it gets planned and built properly instead of squeezed into the close.

## Can I change SPEC.md, and how?

Yes. SPEC.md is your project's source of truth, and the method keeps it changing only in deliberate, approved ways — but it's a normal document now, not something locked behind a special batch. A SPEC change happens one of two ways. If a planning session decides something that changes what SPEC says — a new capability, a different rule, who it's for — Claude updates SPEC right there in that /plan session, with your approval. If a build turns out to need a SPEC change, Claude asks you, adds SPEC.md to that build's file list, and edits it as part of the build. Either way you approve the change before it lands, and the safety check still blocks a build from touching SPEC unless its batch lists it — so a spec change never slips in quietly as a side effect of something else. (There used to be a separate "spec-edit batch" for this; it's gone — it added a whole extra step to change one line and protected nothing that the approval and the safety check don't already.)

## What's the difference between SPEC.md, CLAUDE.md, and Claude's memory?

Three different homes for three different kinds of thing, and they're easy to mix up:

- **SPEC.md** is *what your project is* — what it does, who it's for, how it works. Product truth. A feature, a rule your app enforces, who the users are: all SPEC.
- **CLAUDE.md** is *how Claude should work on this project* — your conventions, workflow rules, house style. Instructions for Claude, specific to this one project.
- **Claude's memory** is for things that apply *across all your projects* — how you like Claude to communicate, your general preferences — not tied to any single project.

Two quick tests sort almost everything. "What it is" vs "how to work on it" splits SPEC from CLAUDE.md: if it describes the product, it's SPEC; if it's an instruction for working on the product, it's CLAUDE.md. "This project" vs "every project" splits CLAUDE.md from memory: only-here goes in CLAUDE.md, everywhere goes in memory. One thing Claude watches for on your behalf: if you say "make Claude always do X" but it's really describing what the app should *do*, that's product truth — Claude will point out it belongs in SPEC, rather than filing it as a working instruction.

## When Claude edits a doc or other writing during a build, do I see the new wording?

Yes. For readable changes — a doc, a piece of copy, a section of your spec, anything you read rather than run — Claude shows you the actual new wording in chat right after making the edit, so you don't have to open the file to see what changed. (Code changes aren't shown this way; reading raw code back wouldn't tell a non-coder much.) The exact wording is written while building, so this is your first look at the real words, not just the plan for them. If something's slightly off, you can ask for a small tweak on the spot — "change this one bit" — and Claude adjusts it there and then, as part of the same build, no separate step. Only a genuinely new or bigger change — a different feature, or reworking something that already worked — waits for its own session.

## I just had an idea for a feature. How do I record it without losing my train of thought?

Tell Claude. It gets added to Captures without derailing current work. Next /plan session picks it up for discussion and routing.

## Why does Claude sometimes re-read our conversation at the end of a planning session?

Before wrapping up a planning session, Claude takes a pass back over the conversation and points out things you mentioned in passing but never asked to save. It's a safety net: when you think out loud, good ideas and concerns slip by without being formally captured, and this catches them before the session closes. It's best-effort — Claude can only re-read what's still in view, so in a long session some earlier discussion may already be out of reach. That means "I didn't find anything" means nothing jumped out in what Claude could still see, not a guarantee nothing was missed. Whatever it surfaces, you approve (or wave off), and approved items get sorted into the queue like any other captured idea.

## Does Claude do that end-of-conversation pass when I close with /done too?

Yes — a lighter version. When you close any session with /done, Claude takes the same quick pass back over the conversation and points out things you mentioned but never asked to save. The difference from a planning session is what happens next: at /done it only *files* what it finds into your captures list, so nothing is lost, and leaves the sorting — whether each one becomes real work, gets parked, or gets dropped — for your next /plan. You still approve what gets filed; Claude shows you the wording first. Two limits worth knowing: if you opened a brand-new conversation just to run /done, there's no earlier discussion to re-read, so it won't find anything; and if you already did a planning session in the same conversation, it may turn up the same things you already captured, which is harmless.

## The queue is empty. Does that mean the project is done?

No — an empty queue is a normal resting state. Run /plan when you have ideas or want to review. The project is done when you say it is.

## What is _build.md? Should I edit it?

The active build's working file. It does four jobs: carries the batch being built (so QUEUE.md stays free while the build runs), lists which files the build may change (the plugin's safety check blocks edits to anything else), ticks off finished steps (so an interrupted session can resume without redoing work), and keeps the batch's reasoning (so /done can write the session record). Claude manages it — don't edit it. Deleted when /done closes the session; if it exists at session start, a previous build was interrupted and /next will offer to resume.

## What is _plan.md? Should I edit it?

A planning session's working file — the planning counterpart to _build.md. When /plan starts working through your captures, it creates `_plan.md` to track where it is: which items it's processing, the current one, and what it has routed so far (promoted, parked, or dropped). It does three jobs: it survives a cleared or compacted conversation, it lets an interrupted /plan pick up where it stopped, and it gives /done a record of what was decided. Claude manages it — don't edit it. /done deletes it when the planning session closes; if it exists at session start, a previous /plan was interrupted and you can resume with /plan.

## What if my project already has planning docs from another tool or an older version?

/setup handles it as a migration. When it sees your folder has content but none of the method's own docs yet, it treats your existing planning or spec documents as a starting point rather than assuming a blank slate. With your help, it maps that content into the method's docs (SPEC.md, QUEUE.md, and the LOG folder), keeping them at the top level of your project. Before renaming anything, it checks that each old doc actually fits the method doc it's mapped to — and if something doesn't fit, it asks you rather than guessing. It won't blindly rename or overwrite your existing files.

## Claude says my project is "out of date" and offers to run /setup. What does that do?

It means the plugin has been updated and now creates a file or folder your project doesn't have yet. Running /setup catches the project up: it adds what's missing without touching your existing work — it backfills the missing scaffolding and does not overwrite or reconcile content you've already written. So it's safe to run, but it isn't a cure-all: it won't refresh or rewrite your existing docs, only add what's absent. If something already in your docs is out of step with the new version, that's a separate change you'd make deliberately, not something /setup does for you.

## A session opened by asking which editor I use, or saying my project was missing something — what happened?

The plugin keeps improving after your project is set up, so a project can end up missing a setting the method has since added. At the start of a session, before /plan or /next, Claude checks for this and catches the project up — adding only what's missing, and never rewriting or clobbering anything you've written. Some settings need an answer from you: the first one is which .md editor you work in (it lets Claude point you to a doc instead of re-pasting its text, saving tokens), so Claude opens by asking that in one line — and you can say to skip it. Settings that need no answer are just added, with a note telling you what changed. This only ever adds; if something already in your docs is out of step with a new version, that's a separate change you'd make deliberately.

## What happens if Claude needs to touch something outside the current batch?

Claude stops and asks. It stays within batch scope. If something else needs changing: "I need to edit [file] because [reason]. Add to scope?"

## Will Claude use my phone or another device to test my app?

Only if you say yes. Some checks need a real device or emulator — installing the app on a phone, tapping through a screen. Before Claude connects to or tests on any device attached to your computer, it asks your permission first and waits for your answer. It won't reach into your hardware silently. And if no device is connected, Claude asks whether one is available rather than guessing — so a check that needs a device doesn't quietly get skipped or run behind your back.

## Why did Claude ask before starting a "subagent"?

A subagent is a separate helper Claude can spin up to go off and work on something on its own — handy for wide, open-ended research. The catch is cost: a subagent burns through usage fast, and a single run that fans several out at once can use up your session's usage in one go. So before Claude starts one, the method stops and asks you first — a prompt saying Claude wants to start a subagent, which you approve or decline. Declining is completely fine: Claude just does the work directly instead, which is usually all that's needed. The prompt exists so a subagent can never quietly run up a big cost without you knowing — you always get the choice.

## What does "Parked" mean in the queue?

Items you've decided not to work on now but don't want to lose. During /plan, parking moves an item to the Parked subsection until revisited. Dropping removes it entirely.

Parked items carry one of two reason lines that signal whether they come back automatically:

- `Blocked by: [slug] + condition` — a trigger exists. When the named item ships or the condition fires, Claude offers to unpark it during the next /plan or /next.
- `Parked: short reason` — no trigger. The item stays parked until you bring it up; Claude won't auto-surface it.

Nothing leaves active flow without one of these — prose alone isn't enough for Claude to track it mechanically.

## What does a "Plan session here" line in the queue mean?

It's a planning checkpoint Claude placed between batches. When /next reaches it, /next stops and tells you a planning session is needed first, naming the reason — usually because the next work depends on a decision, or on findings that only get sorted out in /plan. Run /plan: it handles the named reason and removes the line, and then /next can carry on. You don't add these yourself — Claude places them when it sees a planning moment coming.

## When I add new work to the queue, why does Claude read through my files first?

Before a piece of work goes in the queue as ready to build, Claude traces what it depends on rather than guessing. It reads the files that work would touch — and the relevant part of your SPEC — to work out what has to exist first, then checks that each of those things has something that actually builds it: another queued item, work already finished, or code that's already there. If it finds a dependency with nothing to build it — a "missing-producer" gap — it tells you, so the gap gets filled before the work is lined up. The point is to catch ordering problems while planning, where they're a quick fix, instead of hitting them mid-build where they stall the work. Claude does this for build work only — checking and reviewing work don't carry build dependencies.

## What does the "Cleared to run above this line" marker in the queue mean?

It's a line Claude keeps in your queue showing which work is ready to build. Everything above it has been checked over in planning — its order is right and everything it depends on is accounted for — so it's safe to build next. Everything below it still needs a planning pass before it's ready. Claude positions the line at the end of every planning session and tells you where it sits, so you never have to work out for yourself how much of the queue is safe to run. When the unattended build mode arrives, it stops at this line — a clean finish, rather than running on into work that hasn't been vetted. You don't manage the line; Claude does.

## What does it mean when Claude says a dependency is "out of order" or "dangling"?

Some pieces of work depend on others — one batch needs another finished first. Claude tracks those links in the queue. Now and then a link breaks: a batch is lined up *before* the thing it depends on (out of order), or it points to a piece of work that's no longer in the queue (dangling). Either way, building in that order would trip up.

Claude checks the links when a planning session wraps up, and checks them again at /done. If it finds a break, it won't quietly carry on:

- For a simple ordering mix-up, it offers to reorder the queue right then, with your okay.
- For anything needing more thought, it sends you back to /plan to sort out before any building starts.

You don't track these links yourself — Claude does, and it fixes or flags them before they reach a build.

## What does Claude mean by a "circular dependency"?

Sometimes a piece of work would be better if you added something first — but that something can't be finished until the very work you're about to do is done. That's a circular dependency: each side waits on the other, so "do the other thing first" never actually finishes. When Claude spots this, it won't send you round in a loop. It builds a first version of the work now to break the circle, and keeps the missing piece on the queue (parked, or marked as blocked) to add once this work exists. Nothing is lost — the gap is tracked, just filled later instead of first.

## Claude tidied up the queue while committing, without asking me. Is that normal?

Yes. Some queue housekeeping is Claude's to handle on its own — clearing a "waiting on" note once the thing it was waiting for is done, or fixing a pointer to a section that has moved. These change nothing you decide: they drop no work, reorder nothing, and don't alter any choice you've made — they're bookkeeping on entries that are otherwise fine. So Claude makes the fix and tells you it did, as part of the commit, rather than stopping to ask. Anything that's a real judgment call — dropping an item, rewriting it, or deciding whether to keep it — still waits for a planning session and your say. You always see what was tidied; you just aren't asked to approve the routine kind.

## How do I know what was done in a previous session?

Check LOG/. `index.md` has one-line summaries with commit hashes (newest first), and each line ends with the name of that session's full entry file. The entry file holds the detail — files touched, reasoning, captures routed. For design rationale, search the index, then open the named file.
