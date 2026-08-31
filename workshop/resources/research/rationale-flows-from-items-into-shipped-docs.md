# Rationale flows from work items into the shipped docs

Filed 2026-08-19. Tests the hypothesis in [rationale-in-items-flows-into-shipped-docs]:
that /next transcribes a work item's decision history into the doc it is editing,
because the item carries no marker separating *what to build* from *what was
preserved for the record*.

**Result: confirmed.** Reasoning written into a work item reaches the shipped
procedure docs in recognisable, often near-verbatim form.

## Method

Commit `de2f5fc` (2026-08-16, ten items) was read from both ends: the item text
removed from `QUEUE.md` as each item was consumed, against the text added to
`plugin/throughliner/docs-b/plan.md` in the same commit. Both artifacts are in
git, so nothing was reconstructed from memory.

## Case 1 — [research-cited-not-restated]

Item prose (removed from QUEUE.md):

> restating research inside an item is what produces the uncited dependency, and
> a restatement reads as complete, so nobody goes upstream.

> **The limit, and it goes in the shipped text rather than only here:** nothing
> detects an uncited dependency. This makes a citation visible and a restatement
> a named fault. Do not describe it as closing the hole.

What `plan.md` gained:

> A restatement reads as complete, so a later session takes the item's account
> for the finding and can propose exactly what the research already refused.

> **Nothing detects an uncited dependency, and this must not be described as
> closing that.** … What this makes possible is a visible citation and a named
> fault for restating one.

**This case is weak evidence on its own and is recorded as such.** The item
explicitly instructed that the limit be written into the shipped text. So the
transcription was directed, not leaked.

## Case 2 — [tool-build-implies-an-audit] — the case that settles it

The item directed nothing about what should ship.

Item prose:

> so a measuring build completes, the queue shows nothing outstanding, the log
> records a shipped item, and the step that reads the output was never written
> down. Nothing detects the absence of a step that never existed.

What `plan.md` gained:

> A measuring build that ships alone completes, leaves nothing outstanding in the
> queue and gets a session record, while the step that reads its output was never
> written down. Nothing detects the absence of a step that never existed, so the
> filing is what has to be required.

Clause order preserved; the final sentence is identical. Nothing in the item asked
for it.

## Proportion

In the `plan.md` hunk carrying the research-and-level clause, the build added
roughly eight lines of operative rule and seventeen lines of explanation — about
two thirds of what entered the always-loaded corpus that day was the item's own
decision history, transcribed.

## What this does not establish

Two items were examined, both of which flowed. No search was made for items whose
reasoning stayed in the queue and never reached a doc, so this establishes **that
the mechanism operates**, not that it operates every time, and no rate is claimed.
A counterfactual sample would strengthen it and was not run.

## What it changes

Two live efforts treat this accumulation as an authoring-discipline problem and
remove rationale after the fact: the rationale audit, and the per-paragraph
delete-and-reread lens folded into [law-prose-restyle-heavy-docs]. If the cause is
upstream, both remove text the items keep putting back and will have to run again.

The remedy adopted is structural rather than disciplinary, on the ground that this
corpus records four instances of a correctly-worded always-loaded rule failing to
fire: the build reads a derived view of the cleared region carrying instructions
and no history, so it cannot transcribe what it was never given. See
[split-the-cleared-region-for-concurrent-sessions].

**The throughline rule is untouched by that remedy**, and this is the distinction
the design turns on. The full queue still carries rationale inline and whole, as
the always-loaded rule requires — keep the whole chain, keep it inline, keep the
nuance. What the build reads is a projection, not a deletion.
