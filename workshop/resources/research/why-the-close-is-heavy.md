# Why the close is heavy — measured, 2026-08-21

Alex asked why a planning close ran to roughly 6,000 tokens. Measured rather than
estimated, from the files this close actually read and wrote.

## The headline: the close spends most of its budget reading how to close

```
INSTRUCTIONS READ        done.md          7,443 words
                         done-plan.md     2,854 words
                                         ------------
                                         10,297 words

RECORD WRITTEN           six entries       3,603 words
```

**Roughly 2.9 words of procedure read for every 1 word of record produced.** The
output is not the expensive half. Cutting the record — fewer entries, shorter
entries — attacks the smaller number, and the method has already retired one
length lever for that reason.

## Where the reading goes

`done.md` is read by **every** close whatever its shape; the sub-doc adds a
flavour delta on top:

```
plan / setup / freeform close    done.md + done-plan.md    = 10,297 words
build close                      done.md + done-build.md   =  8,949 words
audit close                      done.md + done-audit.md   =  7,443 + n
```

So `done.md` is a fixed toll on every close in every project, and it is the
second-largest document in the method after `plan.md` (14,153 words).

**Two of its fourteen sections are 45% of it.** "LOG entry files" runs 217 lines
and "Commit core" 171, out of about 860. The first holds the entry template for
*every* flavour, the placement conventions for a chat-level entry, and the
history of two conventions weighed and rejected. The second holds the staging
rules, the dirty-path recognitions, the message derivation, and the account of a
partial-staging failure that cost nineteen entries.

**And a given close does not use most of what it reads.** A planning close reads
and discards: the completion-verification step, the record-a-routing-step-sweeps
section, the build and audit body fields of the entry template, the audit's
approval-outcomes line, the red-flag lifecycle where no flag cleared, and the
isolated-session branch. None of it can be skipped by the reader, because knowing
which parts apply requires having read them.

## The shape this repeats

This is the same finding the build view was built for, one layer out. A run used
to read the whole queue to build a handful of items; `generate_build_view.py`
now gives it only the instructions for the items it is building. **A close reads
the whole close manual to run one flavour of close.** The diagnosis transfers;
the remedy has not been applied here.

## What is already queued, and what is not

Two cleared items already target these files, and neither needs re-proposing:

- **[law-prose-restyle-heavy-docs]** — `done.md` and `plan.md` restyled to the
  wording standard, with a subordination lens for rules stated at the same level
  with no declared relationship.
- **[rationale-lens-after-the-build-view]** — the per-paragraph delete-and-reread
  test over the same two files, relocating history out of operative statements.

**Both are wording passes, and the largest single lever is not a wording
problem.** It is distribution: flavour-specific material sitting in the file every
flavour reads, while sub-docs exist precisely to carry flavour deltas. Moving the
entry template's per-flavour body fields, the audit approval line and the red-flag
lifecycle into the sub-docs that use them changes no rule and removes them from
every close that does not need them. Nothing in the queue currently proposes that.

## What this does not establish

**No figure here is a target.** The 2.9:1 ratio is a measurement of one close, and
a close that produced a single entry would read the same 10,297 words and look far
worse. That is the point rather than a flaw in the sample: the reading cost is
fixed and the writing cost scales with what the session did.

**It says nothing about whether the instructions are correct.** A shorter close
manual that drops a step is worse than a long one that works — `done.md`'s length
is largely accumulated repairs to real failures, several of which it names.

**And it does not measure this session's other costs.** The /plan opening read
the whole queue plus `plan.md`, roughly 39,000 words. Against that the close is
the second-largest single cost of the chat, not the first.
