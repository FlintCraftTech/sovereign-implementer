---
name: setup
docset: current
note: >
  /setup procedure. It runs on two kinds of session: a fresh adoption, where the
  always-loaded behaviour rules are absent, and a migration or top-up inside an
  already-adopted project, where they are present. It states its own
  plain-language guard, so that it holds on the run where nothing else governs
  it, and each step's prose carries its behaviour in full so a tag never has to
  be read to follow the step.
---

# /setup procedure

/setup is where the project gains the documents that will carry the user's
intent across every session to come. You are setting up a project folder with
the Throughliner method.

**Each step's prose carries its behaviour in full, and the response-shape tags
are a summary of it.** /setup runs on two kinds of session: a fresh adoption,
where the rules defining those tags are not loaded, and a migration or top-up
inside an already-adopted project, where they are. So a step is followed from
its prose on either run, and a tag never carries anything the prose does not
already say.

**Plain-language guard.** Everything you say during /setup is read by a non-coder
who may be brand new to all of this. Keep internal terms out of what they see — no
hook filenames, no working-file names, no "scope-lock," "method docs," or "Case B"
labels. Say "your project's files," not "method docs"; say "I'll set this up as a
migration," not "this is Case B."

## Step 0: Is a build running right now?  [SILENT] when no build and no planning session; [BRIEF] when refusing a build; [BRIEF, PROMPT] when describing a planning session

Look for a file named `_build-<session-id>.md` in the project folder. That file
means a build is in progress — either in this chat or another one — and /setup
must not run alongside it.

**Say so plainly and stop.** /setup creates and rewrites a lot of the project's
files, and while a build is running the safety check refuses every write outside
that build's own list. Starting anyway would not be blocked cleanly at the door;
it would fail partway, file by file, leaving the setup half-finished. So:

> There's a build running in this project at the moment, and setting up while it
> runs would leave things half-changed. Finish it, or run /done to close it, and
> then start me again — I'll pick up from there.

Then stop there — no scaffolding, no continue-anyway question, no workaround.

**A planning session is different — it is not refused.** There is no build file
there, and /setup's own marker (Step 0.5 below) is what lets its writes through:
without it, a session with no build file is read as planning, and every write
outside that session's usual few files is refused outright — no prompt, no
override. What /setup owes that situation is a description rather than a
refusal, because the failure to avoid is silence, not permission. Say what is
about to happen and let the user choose:

> You've got a planning session going here. I can set up now — setting up
> changes a few files outside the usual ones, which is fine and expected. Worth
> knowing that the planning work in this chat isn't saved yet; /done is what
> records it. Set up now, or close first?

Then wait for their answer, and do what they say.

## Step 0.5: Declare the run  [SILENT]

Before writing anything, create an empty file named
`.throughliner-setup-active` in this session's scratchpad directory. Delete it
when the run ends — including on every path that ends early: the user declining
above, a stop partway through, an error.

It is what tells the safety check that this session is a setup run rather than a
planning one. Without it, every write /setup makes outside QUEUE.md, SPEC.md,
LOG/ and FAQ/ is refused: the version marker, the format-epoch marker, the
`.gitignore` lines, the managed block in CLAUDE.md, and any scaffold file the
run finds missing.

The scratchpad is used because it is writable in every session type — so the
marker can always be created — and because it clears itself, so a run that dies
partway leaves nothing to tidy up by hand.

## Step 1: Detect folder state  [SILENT] while detecting; [BRIEF, PROMPT] when the project is already up to date

```
Case A  no content            the folder is empty or nearly so. Fresh start.
Case B  content, no SPEC.md   the user's own files exist but no method docs.
                              Either a true fresh start OR a MIGRATION.
Case C  already set up        SPEC.md exists.
Case D  inside another        no SPEC.md here, but walking up the folders
        project               finds one. A POP-OUT — see below.
```

**Case D takes precedence over B for a folder inside an adopted project**: walk
up from this folder looking for a project marker before treating its contents as
a migration.

**On Case B, treat existing planning or spec documents as a possible migration**
and follow the migration framing below. Recognise a migration **by what the docs
do, not by a fixed list of old names** — the source could be anything.

For Case C, check `.throughliner-version`:

```
version matches current plugin   ->  fully up to date. Say so in a sentence,
                                     offer /plan instead, then STOP and wait.
version missing or outdated      ->  Step 2C (migration scaffolding)
```

## Case D: popping a subpart out into its own project

This folder sits inside a project that is already set up, and the user is
adopting it separately. That is a **pop-out**: a subpart that has outgrown the
parent — one unmanageable piece of a large differentiated project — becoming a
project of its own.

**Read the parent's SPEC, infer which subpart this folder covers, and put it to
the user in clarifier form**  [PROMPT] — inviting their answer rather than
proposing one, exactly as Case B's peek does.

**State the irreversibility in that same confirmation, plainly: there is no
scripted way back in.** Popping out is a one-way move; folding the work back
into the parent later is hand work nobody has written a path for.

Then run the ordinary interview with that context, and write the ordinary docs.
**The new project is an ordinary project in every respect and never reads
outward** — it does not consult the parent's queue, spec or records while it
runs.

**Dependencies run upward only, one level deep.** Subproject work may hold
parent work; parent work may never hold subproject work — that is what makes a
cross-project loop structurally impossible. A child genuinely waiting on its
parent uses the ordinary outside-the-project pattern instead: name what would
show it done, or wait for the user to mention it.

**No session ever writes another project's queue.** A dependency crossing the
boundary travels as approval-gated mail, and the receiving project files it with
its own hands.

**At the close, draft the pop-out message to the parent's INBOX**  [PROMPT] —
shown to the user in full, sent only on an explicit yes, like any other outbound
mail.

## Case B: pre-existing content rules

**1. Peek before Q1.** Read the pre-existing content before the first interview
question, and use what you learn to *frame* that question rather than to
*pre-answer* it.

```
a clarifier INVITES the user's own answer:
    "I can see a tax brief in this folder — is that what this project is about,
     or something separate?"
pre-answering PROPOSES the answer for confirmation:
    "From the brief, this is a tax-prep project for your 2025 return — right?"
```

Ask cold and you miss context the folder already gave you; pre-answer and the spec
fills with your words instead of the user's.

**1b. Where the folder already holds more than one git repository — a clone, a
fork, or a `git init` in a subfolder — say so and ask which root this project
adopts** [PROMPT]. Name which repository would hold the method's documents under
each answer, and record the choice as the standing visibility line described at
the keep-private step. Without it, a fork splits the code from the documents and
nothing later says which repository the project is actually in.

**2. Leave it untouched; name it at close.** Pre-existing content is not edited,
moved, or reorganized during scaffolding — scaffolding only adds the method docs.
In the closing message, name that content explicitly as source material the user
can refer back to.

## Case B: migration framing

When the content is a migration, /setup maps it into SI's docs. The mapping is
your judgment, not a fixed table; these guardrails keep it from importing the
source's shape wholesale.

- **State SPEC's purpose first.** Before mapping anything, say plainly what SPEC.md
  is for: product truth — what the app is, who it's for, how it works, why it
  exists. **It is not a UX spec or an implementation manual.** Map the source
  into that frame, with SPEC's purpose deciding the shape rather than the source.
- **Check role-fit before renaming.** A source doc and the SI
  doc it seems to map to may not cover the same ground: the old one might be
  broader (a UX doc walking every screen) or narrower. If the roles don't match,
  say so plainly and let the user decide how to split or combine rather than
  silently renaming one into the other.
- **Scrub the source's self-description from the content.** Renaming the file isn't
  enough — the old framing hides inside the text. A line like "this describes every
  functionality and UI element as the user experiences it" silently re-mandates the
  exhaustive detail SPEC is meant to leave out. Rewrite or drop any purpose, intro,
  or self-description sentence that re-asserts the source's role, so SPEC describes
  **the product**, not the old doc.
- **SI docs live at the project root.** No path setting, no doc-location config. If
  the source used a path block or pointed its docs elsewhere, that doesn't carry
  over.

## Step 2C: Migration scaffolding  [SILENT] for the checks and file creation; [BRIEF] at the close

The plugin version changed since this project was last set up. Re-scaffold without
overwriting user content. Run the checks and file creation **silently**; keep the
close to a sentence or two.

**1. Check each doc/folder** from the Step 2 scaffold list. Exists → skip. Missing
→ create from the standard scaffold (empty structure, not interview-filled).

**1a. Run every document-format conversion the project is behind on**  [SILENT]
when the project is on the current epoch; [PROMPT] for each conversion shown
before writing. Read the
project's recorded epoch from `.throughliner-format-epoch` and compare it against
`FORMAT_EPOCH` near the top of `${CLAUDE_PLUGIN_ROOT}/hooks/session_start.py`:

```
recorded epoch < FORMAT_EPOCH
        ->  load ${CLAUDE_PLUGIN_ROOT}/docs/migrate-checklist.md and follow
            EVERY epoch section from the recorded number up to the current
            one, in order, drafting each conversion and getting approval
            before writing
recorded epoch == FORMAT_EPOCH
        ->  skip; open the checklist at all
no marker file
        ->  the project predates the marker: treat it as epoch 1 and run the
            whole checklist from the beginning
```

**Read the epoch from the marker rather than inferring it from the documents** —
inferring guesses about files users legitimately hand-edit.

Showing each conversion before writing it is the general write-first test
applied, not an exception to it: a project being adopted or migrated may not be
a committed git repo, so its old documents may not be recoverable once
overwritten.

**1b. Reconcile the settings attached to the scaffold list**  [SILENT] for the
settings added without an answer; [BRIEF, PROMPT] for the brevity-style offer
and for INBOX files already in git history. Step 1 restores
missing *files*. It does not re-run the *decisions* attached to them, so a
migrated project can end up with a file and none of the setup that goes with it.
Check each, and make it so if it isn't:

```
INBOX/ present          ->  `.gitignore` carries an `INBOX/` line
.gitignore present      ->  it carries a `.throughliner/` line
no outputStyle set in the project's .claude/settings.local.json
                        ->  make the brevity-style offer from Step 2, exactly
                            as a fresh setup would — this project was set up
                            before the style shipped
```

**Where the project has INBOX files already in git history, say so plainly.**
Adding an ignore line stops future commits; it does not untrack what is already
committed, and it cannot remove anything from history. Tell the user what is
there and that the line does not undo it — the line goes in only alongside that
plain statement, so nobody is left thinking the mail is now private.

**2. Retire REGISTRY.md if present**  [SILENT] when it holds only what the old
setup put there; [BRIEF, PROMPT] when the user has written into it. No longer
one of the method's docs, but
**read it before deleting** — the user may have written real notes there.

```
holds ONLY what the old setup put there
    (a # REGISTRY heading, the "Components that exist…" line, and either the
     empty placeholder or an auto-generated file list)
        ->  remove it quietly as part of the migration
holds anything the user clearly added
        ->  LEAVE it. Tell them plainly what's in it and ask where that content
            should live now (usually SPEC.md) before removing the file.
```

Where their own content goes is the user's call, not yours.

**2a. Rewrite a plain-prose section preamble as a blockquote**  [SILENT]. Where the
paragraph directly under `## Processed` or `## Unprocessed` in the project's
QUEUE.md is ordinary prose, prefix each of its lines with `> ` so it becomes a
blockquote. Leave the wording alone — this changes the shape, not the text.

The queue lint reads any un-quoted, un-headed prose inside a section as an
orphaned rationale and warns that an item's heading may have been overwritten —
and a preamble legitimately has no heading.

```
preamble is already a blockquote  ->  nothing to do
preamble is plain prose           ->  quote it, wording untouched
no preamble under the heading     ->  nothing to do; the scaffold's own
                                      wording is not backfilled here
```

**Widening the lint's exemption to any first paragraph was refused, and stays
refused (2026-08-15):** it would exempt genuinely orphaned prose, which is the
thing the check exists to catch.

**3. Update `.throughliner-version`**  [SILENT] to the current plugin version.

If the project instead carries the pre-rename marker `.si-version`, write the
new file and delete the old one — the method was called Sovereign Implementer
until epoch 3 and both marker files were named for it. Do the same for
`.si-format-epoch` in step 3a. Leaving the old file behind means every later
session reads a marker the plugin no longer writes to, so the two names drift
apart silently.

**3a. Write `.throughliner-format-epoch`**  [SILENT] when the conversion ran to
completion; [BRIEF] when the user skipped it — the document-format number this migration
brings the project up to. Read it from `FORMAT_EPOCH` near the top of
`${CLAUDE_PLUGIN_ROOT}/hooks/session_start.py` and write that number, on its own,
into `.throughliner-format-epoch` at the project root.

Do this **last among the migration edits**, and **only when the conversions for
that epoch ran to completion**. It is what clears the session-start halt that
sent the user here, so writing it early would silence the warning while the
project was still on the old shape — and nothing else would ever raise it again.

```
conversion ran to completion   ->  write the new epoch number
user skipped the conversion    ->  leave the marker at its old value, and say
                                   plainly that the halt will fire again next
                                   session because the conversion is still owed
```

**3b. Read the project's own CLAUDE.md for retired terms, and report what you
find**  [SILENT] when clean; [BRIEF] when reporting.

A project's CLAUDE.md was written when it was set up and is read at the start of
every session since; where it describes a piece of the method that has since
been retired, every session reads that description as current.

Search the file for each retired term the method carries, and for each hit say
plainly what the term was and what replaced it.

```
retired terms to search for, with their replacements:
    "batch", "Build/Test/Audit"  ->  a work item is a single `#### ` heading
                                     with a flavor tag; there are no batches
                                     and no sub-headings inside one
    "Deferred tests"             ->  deferred verification is a `[user]` work
                                     line, revisited each planning run
    "Parked:"                    ->  work is held below the cleared-to-run line
                                     by `Blocked by:` or `Not before:`
```

**Also read the project's SPEC.md for a "Project docs" section** — the old
scaffold wrote one describing the method's own machinery into the user's
product truth, and it goes stale in a way no refresh repairs, because SPEC is
the user's document and is never rewritten by a migration. Report it the same
way: say the section describes the method rather than their product, that the
same description now lives in the managed block of their CLAUDE.md, and edit
nothing — removing it is their call.

**Report only — edit nothing.** The file is the user's, and reconciling its
wording against the current template would clobber whatever they wrote into it.
Tell them what is stale, what it means now, and leave the change to them.

```
no hits    ->  say nothing; carry on
one hit    ->  name the term, what it was, what replaced it
several    ->  one message listing all of them, then carry on
```

**3c. Refresh the plugin-managed block in the project's CLAUDE.md**  [SILENT]
when the regions match; [BRIEF] when replacing the region or reporting a missing
one.

Compare the region between the PLUGIN-MANAGED markers in the project's CLAUDE.md
against the same region in the installed `templates/CLAUDE-TEMPLATE.md`.

```
regions match          ->  nothing to do; say nothing
regions differ         ->  say what will be replaced, then:
                           1. any text inside the block that is not the
                              template's — user-authored lines — moves below
                              the end marker, and the narration says so
                           2. the region is replaced with the template's
                              current text
no markers found       ->  report it like a retired term (3b): say the managed
                           block is missing and what it is, edit nothing
```

This is the one deliberate exception to the add-only rule below: the
block's own marker promises it is updated on /setup, and the method-owned text
between the markers is exactly what goes stale as the method evolves — a stale
queue model there is read as current at the start of every session. The move-
then-replace order is what keeps the exception safe: nothing the user wrote is
deleted, only relocated below the marker, and the narration names it.

**4. Skip the interview**  [SILENT] — the project is already described in SPEC.md.

**5. Close state-aware**  [BRIEF].

```
a leftover build working file    ->  an earlier build was interrupted: name it
    is present
                                     and recommend resuming with /next. The
                                     migration's new files get recorded when
                                     that build closes.
otherwise                        ->  tell the user what was created or updated
                                     and recommend /done
```

**Add only — existing files stay as they are.** The goal is to add what a newer
plugin version introduced, not to refresh content. The one carve-out is the
plugin-managed block in CLAUDE.md (3c), which is method-owned text the marker
promises is kept current — and even there, user-authored lines are moved rather
than deleted.

## Step 2: Scaffold the docs  [SILENT] for the file creation; the tagged offers inside it govern their own turns

Create these files (empty structure; content comes from the interview),
**silently** — the Step 4 close-out reports the full list.

**SPEC.md:**

````markdown
# SPEC — [Project Name]

## What this is
[filled by Q1]

## Who it's for
[filled by Q1]

## How it works
[filled by Q2]

## Principles
[filled by Q3]
````

**QUEUE.md:**

````markdown
# QUEUE

## Processed

> Vetted work, ready to build — worked top to bottom. Each piece of work is one
> item: a `#### ` heading naming it, a short name in square brackets at the end of
> that heading line, and a short rationale beneath. **That bracketed name is a
> handle, so you and Claude can refer to a piece of work without retyping its whole
> description — "let's do the login one" works too, and Claude never asks you to
> write one.** A leading flavor tag names how it runs — none for a
> build (Claude edits files), `[audit]` for a review pass, `[user]` for a step only
> you can do. A security or privacy risk Claude surfaces lives here too, as a work
> item carrying a `Red flag · State: cleared/uncleared` marker. The line below marks
> how far down is cleared to build; anything below it is decided but not ready yet.

--- Cleared to run above this line ---

## Unprocessed

> Captured ideas and tasks not yet fully processed. The next /plan run goes
> through these with you and decides each one's fate — keep it (move it up to
> Processed) or drop it. Each is filed as its own `#### ` heading, so the list shows
> up in an editor's outline.

[filled by Q4]
````

**LOG/ folder** — create the directory with one file in it, `LOG/index.md`:

````markdown
# LOG Index

One-line summaries of each session. Newest first. Each line names the session's
full entry file in this folder.
````

Session entries are written by /done, each as its own file in LOG/ — nothing else
to scaffold.

**FAQ/ folder** — create the directory **first**, then copy the templates in (the
folder must exist before the copies, or they fail):

```
FAQ/faq.md    <-  ${CLAUDE_PLUGIN_ROOT}/templates/faq-template.md
FAQ/index.md  <-  ${CLAUDE_PLUGIN_ROOT}/templates/faq-index-template.md
```

**resources/research/ folder** — create it empty. It's the home for research notes
(`resources/research/<topic>.md`). Creating it at setup means research notes have a
place from day one rather than the folder being conjured on first use.

**INBOX/ folder** — create it empty, with an `INBOX/archive/` inside it. It's this
project's mailbox: another project you run can drop a message file in here, and
session_start surfaces anything waiting in one line. A project only ever reads its
own INBOX — it never goes looking through other projects for mail.

Add `INBOX/` to `.gitignore`, and say so in one line  [BRIEF] — that mail from other
projects stays out of the repository, and they can remove the line if they want it
committed. No question is asked.

Why it isn't asked: anything committed is published, an un-ignored mailbox
accumulates another project's raw text in the repository forever, and the safe
outcome must not depend on a question being asked, because a question is
skippable.

**CLAUDE.md:**

```
no CLAUDE.md exists  ->  scaffold from
                         ${CLAUDE_PLUGIN_ROOT}/templates/CLAUDE-TEMPLATE.md
one already exists   ->  APPEND the method block; never overwrite
```

The template carries no rendering settings — how doc-bound text is surfaced is a
default plus a session-opening offer, not a stored field (skill-nonspecific-rules.md,
view-in-doc rendering).

**.throughliner-version** — write the current plugin version (from
`${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`). session_start reads it to
detect when the plugin has been updated.

**.throughliner-format-epoch** — write the document-format number, read from `FORMAT_EPOCH`
near the top of `${CLAUDE_PLUGIN_ROOT}/hooks/session_start.py`. Separate from the
version on purpose: the version changes at every release, the format number only
when a change makes older projects' documents structurally wrong. session_start
compares the two and halts the session when the project is behind, so a project
on an old shape finds out instead of quietly running on stale scaffolding.

**.gitignore** — create it if absent, and make sure it carries an entry for
`.throughliner/`, added only where it is missing.

That folder holds the editing-state signal: while Claude is writing a file, the
hooks drop a small file in there saying so, so a Markdown reader or editor open
on the same document can hold off rather than the two of you typing over each
other. It is transient state about the session running right now, so it stays
out of the repository.

**Git repository** — if the folder isn't already one, run `git init`, silently and
mechanically like the rest of the scaffold. Without a repository there is nothing
for the close-out to commit to.

**Keep-private option**  [BRIEF, PROMPT]. Offer once, as part of scaffolding, to
add the project's Throughliner documents to `.gitignore` so they stay out of the
repository entirely — **and offer the three separately, so any combination of them
is reachable:**

```
SPEC.md    what the project is
QUEUE.md   what to work on next, and the reasoning behind each piece
LOG/       what happened, session by session
```

**Ask it as ONE question with three answers, not as three questions.** "All of
them, none, or just some — and if some, which?" A private queue with a public
history is the combination someone most plausibly wants, and a bundled choice
makes it unreachable rather than merely un-defaulted.

Say what it costs and what it buys, in one short exchange, and **state the trade
once rather than once per document**: these documents hold the project's plans,
its reasoning and its session history, which is the most personal material the
method produces; keeping them out of the repository is the only complete
protection if it is ever published.

**State the cost as the three things that change, not as "you lose undo".** It is
larger than that, and the moment of choosing is the one moment it can be said.
Each applies to whichever documents the user keeps out:

```
1. Claude normally writes to these first and reports what landed, because a
   revert costs nothing. Untracked, it cannot — so text going into them is
   SHOWN before it is written instead.
2. A deleted queue item is genuinely gone. Git is not keeping a copy.
3. The close cannot read its own work back from the file's history, so it
   records the session from what it remembers.
```

They also do not travel with a clone.

**Nothing here is asserted again later as a fault.** Every session opening
reports which of the three are untracked and what follows, because this state
can also arrive from an ignore file the user wrote themselves, or from a choice
made weeks ago in a project nobody has looked at since.

```
user names some or all  ->  add exactly those paths to `.gitignore`, say in one
                            line which went in and which stayed tracked
user says none          ->  state plainly what results: these documents are
                            tracked in this folder's history and readable
                            nowhere else until the project has an online home,
                            which is set up whenever they ask. Not asked again
                            at any later setup run.
```

**Write the visibility answer as a standing line in the project's own
CLAUDE.md**, in the slot the template carries for it, so every later session
reads it — not only the setup session's record.

**A public repository is set up only when the user asks**, never volunteered,
and the licence question travels with that offer rather than sitting in the
interview. **The offer may set up the repository and may never represent the
contents as screened** — not publishing these documents is the only complete
protection.

**Change no default.** Nothing is ignored unless the user asks for it, whichever
documents they name.

**This adds no sixth interview question.** It is part of scaffolding, where the
files are being created, and it is answerable without knowing anything about the
project.

**The brevity-style offer**  [BRIEF, PROMPT]. The plugin ships an output style
called Throughliner Brevity — a setting that keeps Claude's replies short and
decision-led in this project. Offer it once, as part of scaffolding, opt-out
with acceptance as the default:

1. Check whether the project (or the user's own settings) already sets an
   output style. Where one is set, name it and say plainly where it and the
   brevity style would pull in different directions.
2. Give the reason acceptance is strongly preferable: on projects with this
   much documentation, models that run verbose bury the one thing the user
   must see under narrative, and a style is the strongest lever there is
   against that.
3. State the scope: this applies to this project only — nothing outside it
   changes, and the user's own style file is never edited.
4. Invite discussion, then act on the answer:

```
user accepts (the default)  ->  write "outputStyle": "Throughliner Brevity"
                                into the project's .claude/settings.local.json
                                (creating the file if absent, merging if not)
user declines               ->  say nothing further; every session opening
                                will carry one short line noting the style is
                                not enabled
```

Say once that the style takes effect at the next session or /clear — styles
never apply mid-conversation.

**The public-repository offer — one subject, four provisions** [DISCUSS,
PROMPT]. Make it only where the user asks for a public repository, and then:

- ask what licence the project should carry, and why it is being asked now:

```
a licence is what says who may use the code and on what terms, and it only
becomes a real question once the code is going somewhere public
```

- set up the repository;
- describe the contents as unscreened, and say what the only complete protection
  is — not publishing these documents, which is what the keep-everything-private
  option above does;
- treat "not now" as a plain answer that ends it, with the offer not repeated
  and nothing set aside for later.

The method scans for things shaped like credentials and reads its own writing
against a checklist, and neither can tell whether a sentence quietly identifies
a real person — so this offer may set up the repository and may say nothing
about the documents being checked, clean, or safe to publish. Any wording
implying they have been checked contradicts a shipped rule, and it is the
sentence most likely to slip in here.

**Two things are deliberately NOT asked, recorded so they are not re-proposed.**
A standalone licence question in the interview — moved onto this offer, because
most non-coders cannot answer it while still describing what their app is, which
turns a question into a small failure with "I don't know" as the honest reply. And
the idea that open source implies open logging — dropped entirely, because raising
it at all nudges a user toward publishing their planning documents, which is the
exact direction the scrub gate's stated limit exists to avoid nudging. Both costs
were named and accepted: a user who never asks for a public repository never
considers licensing, and a user who publishes may never think about whether their
logs belong in it.

## Step 3: Interview (adaptive discovery)  [SEQUENCE, PROMPT]

The interview is an **adaptive discovery, not a fixed script.** Its job is to reach
a shared, buildable understanding — enough to fill SPEC's What / Who / How /
Principles and capture a first piece of work — by reading each answer and asking
the next question that actually matters.

**Write the project's files once discovery has covered** what the project is, who
it's for, its core, and a first thing to build. Principles and the free-form
"anything else" are optional and don't hold the writing up.

**Where a scaffolding choice is the user's — which folder to adopt, whether
existing content is a doc to leave alone, how to read an ambiguous answer — ask
before acting.** The question costs one turn; a wrong guess makes the user undo a
scaffold.

**The framing throughout is "adopt the folder":** the method is being applied to
their project, not their project reorganised to suit the method.

**Ask one question per message and stop after each, however short the questions
are** — two in one message is bundling.

- **Use the user's own language.** Ask in their words and record their answers in
  their words, rather than rephrasing into the method's vocabulary.
- **Where an answer is vague, ask a follow-up** — subject to the stopping rule
  below, which bounds how far probing goes.
- **Read each answer, then reason about what's still unclear** before choosing the
  next question. Walk the design one branch at a time. The next question is
  generated from what's missing, not from a fixed position in a script.
- **Recommend an answer to each question** rather than asking cold — offer a
  plausible answer the user can accept, correct, or replace ("My guess is this is for
  personal use rather than a team — is that right?"). A non-coder finds it far
  easier to react to a proposal than to fill a blank.
- **Cover these topics** — a bank to draw on, not a checklist to recite:

```
what the project is, and who it's for   ->  What this is / Who it's for
the core — the main thing it produces,  ->  How it works
    organises, or does
principles or constraints               ->  Principles
    ("must work offline", "no accounts", "everything in plain text")
the first thing to build today          ->  becomes the first capture
anything else worth knowing
```

  Skip what an earlier answer or the existing content already settled; probe deeper
  wherever the picture is thin.
- **Explore whatever already exists first.** There may be an old doc, a sketch, a
  notes file, or a running app. Use it to inform your questions rather than asking
  things the existing content already answers. Where there's genuinely nothing,
  interview from a blank slate.

**The stopping rule (the anti-overwhelm guard).** Keep probing only until the
answers bottom out into something concrete enough to build from — you're done when
the Whys are answered, not when every branch is exhausted.
Tell the user plainly, early on, that they can end it any
time by saying **"build from what we have"**, at which point you stop asking and
write the docs from whatever's been gathered.

**The first capture** — whichever answer names the first thing to build — creates
**one rough capture** in Unprocessed: a `#### ` heading **in the user's words**,
with a kebab-case `[slug]` at the end and a "captured by you" note beneath.

**Write the heading in the user's own words, and stop there.** Their words are
the whole content of the item — anything added is Claude's scope decision wearing
the user's voice, and the tempting case is a parenthetical example drawn from
what they said, which reads as a commitment they agreed to.

Scope decisions belong in /plan, which is where this item gets processed. If
examples would clarify scope, ask a follow-up rather than smuggling them in.

**There is no settings question at all, here or anywhere.** The last one —
whether INBOX messages were committed — was dropped in favour of ignoring
`INBOX/` on both paths, because the safe outcome must not depend on a question
being asked. Discovery ends where it ends; there is no settings round after it.

The editor and working-mode questions that used to sit here are **gone**,
replaced by one default: point at the doc, with a plain-English summary inline
where a discussion needs one.

## Step 4: Write the docs  [BRIEF, PROMPT]

Once discovery reaches a buildable understanding (or the user says "build from what
we have"), write the docs, then close in a sentence or two and **stop and wait**.

```
1.  fill SPEC.md from the interview answers
2.  write ONE capture in Unprocessed from the first-thing-to-build answer
    # the user's words, a [slug] at its end, a "captured by you" note.
    # Not multiple scoped entries.
3.  show the user what was created (file list + one line each)
4.  delete `.throughliner-setup-active` from the session scratchpad — the run
    is over, so the declaration from Step 0.5 comes down with it
5.  recommend /done to record this setup and commit the new files
6.  teach the working rhythm (below)
```

The file list shows what appeared in the folder; the session's single summary is
the LOG entry /done writes at close.

**Teach the working rhythm in plain words** — a few short sentences:

- **/setup** you've now run once; you won't run it again for this project.
- From here, two commands carry the work: **/plan** to think and organise, and
  **/next** to build the next thing on the list. Run /plan whenever planning is
  needed, and /next once per item as you work down the queue.
- However a session goes, end it the same way: **/done** to record what happened,
  then **/clear** to start fresh. The habit that matters: **always /done before
  /clear**, so each session is saved before the context resets.

