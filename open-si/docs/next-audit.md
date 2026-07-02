# Audit procedure

Execution procedure for audit batches. Reached from next.md after pre-flight checks and scope lock are complete. The output contract defines an audit: findings route through Captures so /plan can convert them into normal batches — no direct edits to the artifacts the audit reads. What gets read varies — procedure docs, the user's spec, code, UI flows, workflow output, any other artifact; the procedure shape is the same regardless: read many, propose many. The audit _build.md carries a `Files:` section with no entries, so the scope-lock holds the session to the method docs (QUEUE.md, LOG/, _build.md) — the strictest setting, matching a session that edits no source files.

## If the batch's Output names a write-target, stop and ask [PROMPT]

Before reading, check the batch's own entries against the contract. An audit's contract is findings-to-Captures with no direct edits to what it reads. So if this batch's Output directs a write into a named document (for example "append findings to MAP.md," or a Files list naming a findings doc to fill), that Output contradicts the contract — don't silently follow it. Surface the conflict in plain language and ask which the user wants: file the findings as captures the normal way, and let a later build write the document from the vetted findings; or treat this session as a build that writes the document now. Wait for the answer before reading. The why: a batch authored as an Audit but pointed at a doc-write is a planning slip, and following it silently writes unvetted findings straight into a durable doc — the exact thing the route-to-Captures contract prevents. Exemplar: "This batch is an audit, but its Output says to write findings into review-notes.md. An audit files findings to Captures for vetting first — it doesn't write them into a doc. Want me to file them as captures, or run this as a build that writes review-notes.md directly?"

## Read the target systematically against the criteria [SILENT]

Read every artifact named by the target. Apply the criteria pass by pass — one criterion across the whole target, then the next, not mixing criteria per artifact. Don't skim; an audit's value is reading what's there. Accumulate observations in _build.md Changes with precise references (file:line for files) so the user can verify each.

## Compile findings [SILENT]

Once the read is complete, group observations into discrete findings. One finding per actionable change. Phrase each as observed + why it matters — the shape a capture takes, since that's where they'll land.

## Present findings as one numbered set [BRIEF, PROMPT]

Compile every finding into one numbered set and present it in a single message. State the count upfront, then list all findings — for each: the number, the observation, the file:line reference, why it matters. Ask the user to approve the whole set, or to list the numbers they don't accept as-is. Then wait.

This is the one inversion of one-at-a-time (see plugin-behaviour.md Communication, sequencing rule): the findings are a deterministic result set produced by criteria the user already approved when they queued the audit, so approving each separately costs round-trips without adding judgment the bulk view doesn't already give. Bulk approval keeps the Captures always-show rule fully intact — the user reads every finding's exact wording before any of it is filed.

## Handle contested findings one at a time [SEQUENCE, PROMPT]

If the user lists numbers they don't accept as-is, take those one at a time — state how many, then the first. For each, the choice is reword or drop: reword means redraft and show the new wording for approval; drop means remove it. Wait for the user's call on each before presenting the next. Every finding the user didn't contest is approved as-is.

## Route the approved set to Captures

Append the approved findings to Captures in QUEUE.md, each placed per plugin-behaviour.md Captures placement, each written to the capture-authoring standard (plugin-behaviour.md Captures). Tick each finding in _build.md Progress as `captured` or `dropped`.

## Close [BRIEF, PROMPT]

Tell the user the audit is complete with the captured/dropped counts. Say: "Run /done to record this and commit, or keep reviewing." Reviewing means re-examining what was already found — not raising new work. Anything new routes through the existing paths: a discovery outside the audit's target follows the discovery rule (plugin-behaviour.md Routing and discipline), and thinking work goes to Captures. No chat summary of the routed findings — the LOG entry /done writes is the single session summary.
