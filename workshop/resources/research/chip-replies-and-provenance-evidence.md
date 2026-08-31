# Suggestion-chip replies and what can evidence a user's authorship

Filed 2026-08-17 from a finding made 2026-08-13. **The objection is the user's, in her own words: "those are ALL chip answers, i don't write like that."** The metadata check and the containment test are Claude's.

Kept as a durable file because it must be re-read word-for-word: it is the evidence behind a shipped always-loaded rule, and the metadata claims below cannot be reconstructed without re-reading raw transcripts.

## What was being checked

The user asked where the `Runs alone` marker came from, saying she did not remember approving it. The item that introduced it recorded two user-credits: that she directed settling it before the next run, and that the marker was "the route, chosen by the user". Claude read the raw transcript, judged the first accurate and the second wrong, and said so confidently. She then said all of those replies were suggestion chips.

## The metadata finding — the primary evidence cannot answer the question

Every user message in `.claude/projects/<slug>/*.jsonl` carries:

```
origin:       {kind: "human"}
promptSource: "sdk"
```

Messages the user plainly typed — including ones carrying her own typos — are **byte-for-byte indistinguishable** from one-line affirmatives produced by clicking a suggestion chip. The transcript records who **sent** a message and never who **composed** it.

So the evidence this method relies on for provenance cannot settle provenance. No harness field distinguishes the two, and Claude cannot detect a chip reply at all.

## The laundering loop

Claude proposes a design → the harness renders Claude's proposal as a suggestion chip → the user clicks it to move on → Claude records "chosen by the user, in their own words". Claude's own recommendation is laundered into the user's authorship, and the resulting artifact is indistinguishable from a real user decision — to a later session, to an audit, and to the session that wrote it. It was believed and asserted twice in the exchange that discovered it.

## The one signal that still works: containment

A real user message contains something Claude's preceding message did not — a disagreement, a new fact, a redirect, a question, a correction. **A reply wholly contained in what Claude just proposed cannot evidence authorship**, because the chip could have supplied every word of it.

Checkable with no harness support and no new field: compare the reply against the message before it.

## What this does NOT establish

That the decisions were bad. `Runs alone` may be correct on its merits; the objection is to a record claiming an authorship it cannot support. Whether a wrongly-credited decision needs re-deciding is a separate question from re-labelling it.

## The user-side half, which no mechanism can supply

Her realisation, rendered in Claude's words: answering in the affirmative with a chip reads as understanding and agreement, so it should never be used to defer. When deferring to Claude's judgement, say **"as you recommend"** instead — which makes the deferral explicit at the one point where the ambiguity is otherwise unresolvable.

**First evidence that this works: 2026-08-17.** She used the phrase twice in one planning session and both were recorded as deferrals rather than as her decisions.

**A once-per-session notice was designed and refused.** It would fire on a detection that does not exist, so it would have to fire at every user every session, including those who never use the chips. **Her words on it: "seems a bit much."**
