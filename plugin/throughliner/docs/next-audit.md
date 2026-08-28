---
name: next-audit
docset: current
note: Execution procedure for `[audit]`-flavor work items. Reached from next.md.
---

# Audit procedure

**The output contract defines an audit:** findings route to Unprocessed so /plan
can process them into normal work items — **no direct edits to the artifacts the
audit reads.**

What gets read varies — procedure docs, the user's spec, code, UI flows, workflow
output. The shape is the same regardless: **read many, propose many.**

Audit items contribute nothing to the run's `Files:` list — settled at next.md's
self-scoping step.

## If the audit item directs a write into a document, stop and ask  [PROMPT]

Before reading, check the item's wording against the contract.

```
item directs a write into a named document   ->  CONTRADICTS the contract
    ("append findings to MAP.md", or names        surface it; don't silently follow
     a findings doc to fill)
```

An item marked `[audit]` but pointed at a doc-write is a planning slip. Following
it silently writes unvetted findings straight into a durable doc — exactly what
the route-to-Unprocessed contract prevents.

Lead with the recommendation, then wait before reading:

> "This item is an audit, but it says to write findings into review-notes.md. An
> audit files findings to the queue so you can weigh them before anything lands
> in a document, so I'd file them as captures. If you'd rather have them written
> straight into review-notes.md, say so and I'll run it as a build instead."

## Read the target systematically against the criteria  [SILENT]

Read every artifact the item names. **Apply the criteria pass by pass — one
criterion across the whole target, then the next** — not all criteria per
artifact. A single criterion held across the whole target is applied more
consistently than re-deciding every criterion afresh for each artifact, and it
groups findings by criterion ready for the compile step. Reading each artifact
once against everything tends to collapse into a per-artifact skim.

Read each artifact through, since an audit's value is reading what is there.
Accumulate observations in the build working file Changes with precise references
(file:line) so the user can verify each.

## Compile findings  [SILENT]

Group observations into discrete findings — **one finding per actionable change.**
Phrase each as *observed + why it matters*, the shape a capture takes, since
that's where they'll land.

## File the findings to Unprocessed  [SILENT]

Append every finding to Unprocessed, each placed per the Captures placement rule
and written to the capture-authoring standard. Tick each in the build working
file Progress as `captured`. Then say in one line how many were filed and which
audit they came from.

**Each capture carries a prose line saying it is unreviewed audit output** —
"from the <name> audit, not yet reviewed" — written into the rationale like any
other provenance. Not a parsed field: /plan's decision step reads the line, and
nothing else needs to.

**Nothing waits for approval here.** A finding is a capture like any other, and a
capture is filed and then weighed at /plan — asking the user to accept a set of
findings before filing them makes them assess the same material twice, once with
no context and again when it is actually being decided.

The `dropped` tick form stays available for a finding that turns out to be
wrong on Claude's own re-reading before filing — it is not a route for the user
to reject one, which happens at /plan.

## Close  [BRIEF, PROMPT]

When the audit item is done, next.md moves to the run's next item. When the whole
run is done, tell the user how many findings were filed, and say: "We can run the
rescan first to catch anything decided but never written down, then /done to
record this and commit — or keep reviewing."

Reviewing means re-examining what was already found — not raising new work.
Anything new routes through the existing paths: a discovery outside the audit's
target follows the discovery rule; thinking work goes to Unprocessed. No chat
summary of the routed findings — the LOG entry /done writes is the single session
record.
