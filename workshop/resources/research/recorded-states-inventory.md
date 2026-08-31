# Recorded states in the method — computable or decision

Filed 2026-08-31 by the `[recorded-states-inventory]` audit. It exists to ground the purpose hypothesis recorded on `[mcp-server-standing-intent]`: that an MCP server retires the recorded copies of *computable* states and must not touch the *decision* trail. An MCP design cannot be scoped until someone knows which recorded states exist and which side of the split each falls on.

**What was read:** the shipped docs under `plugin/throughliner/docs/`, the templates, the hooks, `SPEC.md`, `CLAUDE.md`, and the queue's own field set.

**COMPUTABLE** means derivable from an observable a tool could read live, and the observable is named. **DECISION** means a record of a person deciding, which no tool can compute. **MIXED** means the state has both halves and they are separable — which turns out to be the most useful category, because the two states already built that way are the model the rest should copy.

## Already computed live, stored nowhere — the model cases

| State | Observable |
|---|---|
| Installed host build stamp | a content hash of the installed plugin's files, recomputed at every session start |
| Cycle due-ness | each definition's own observable — a release date, a register line, a record's opening sentence. SPEC states the design intent: *position is never stored* |
| Retired-artifact orphans | the listed path is present in the project, or is not |
| Held-item resolution | `locate()` on the named slug, plus the kind of record it left behind |
| Date holds passing | `Not before:` compared against the clock |

These need no MCP work. They are here because they are the shape everything below is measured against: nothing is stored, so nothing can go stale, and a session that forgets to update something cannot make the output lie.

## COMPUTABLE, but currently stored

| State | Where | Observable that would replace it |
|---|---|---|
| `.throughliner-version` | project root | the installed plugin's own `plugin.json`, already read live at session start — the file is a copy of a fact the hook independently computes |
| `.throughliner-setup-active`, `.throughliner-close-active` | session scratchpad | which skill is running, which the harness knows |
| `.in_use`, `.orphaned_at` | plugin cache | the cache's own occupancy |
| `stop-claim-<session>-<slug>.marker` | `.throughliner/` | whether this session already blocked this claim — session-scoped history the harness holds |
| `editing-<session>.json` `active` | `.throughliner/` | genuinely live already: the heartbeat's staleness rule means a reader computes "not editing" from the timestamp whatever the flag says |

## DECISION — no tool can compute these

| State | Where | Why not computable |
|---|---|---|
| Section membership (Processed / Unprocessed) | QUEUE.md | the trust boundary itself: moving an entry into Processed authorizes an unattended build |
| Position relative to `--- Cleared to run above this line ---` | QUEUE.md | the user set it; it is the run's bound |
| `Red flag · State: cleared` | a queue entry | clearing is a design-out or the user's informed consent, and the LOG carries which |
| `Runs alone` | a queue entry | a planning judgment that the work moves paths under a run |
| `Cycle: [slug]` | a capture | which cycle owns this material |
| `Rule gate: … — run \| not needed` | a LOG entry, a queue item | **explicitly uncomputable.** CLAUDE.md states that nothing can tell an honest disposition from a dishonest one, and that this must not be described as fixed |
| `Depth: <slug> — short \| full` | the build working file | a judgment about whether reasoning was contested |
| `Files:` list | the build working file | agreed scope |
| `deferred` as a walk-through outcome | a LOG entry | the user's own word, never inferred — stated as a rule |
| `for completion` / `for continuation` | `INBOX/sent.md` | the sender's intent, which is what lets a send close work |
| `Superseded by:` / `Copied from:` | a research file | a judgment that one finding overtakes another |
| `.throughliner-format-epoch` | project root | see below — the one entry whose classification is a finding in itself |

## MIXED — the decision is stored, the resolution is computed

Two states are already built this way, and they are the pattern:

- **`Blocked by: [slug]`** — that the item is held is a decision; whether the blocker has resolved is computed live by the digest, every time, from the queue and the record.
- **`Not before: YYYY-MM-DD`** — the date is a decision; whether it has passed is read off the clock.

Two more have the split available and do not yet use it:

- **The build tick's confirmed field** (`done, confirmed` / `done, UNCONFIRMED: <what still needs running>`). Whether a named check ran is observable; what still needs running is a judgment. `done-plan.md`'s hold-back rule reads this field to decide whether dependent work may clear, so the computed half is doing safety work while stored as prose.
- **The walk-through outcome `done`**, where the walkthrough names an observable check. `deferred` stays a decision; `done` via a named check is already computed at the point of use, but recorded as a flat value afterwards.

## The two findings this sweep produced

**The format epoch cannot be made computable, and the refusal is on record.** Every other stored-but-computable state above has a live observable. This one does not: the alternative — inspecting the documents' structure to detect their format — was considered and rejected, because it guesses about files users legitimately hand-edit. So `.throughliner-format-epoch` is a record that a migration was performed, which is a decision, and it is load-bearing: without it `session_start`'s migration halt never fires. Any MCP design keeps it.

**`INBOX/sent.md`'s "approved, not yet posted" is a stored state that went stale silently and caused a public falsehood.** A post recorded under that status was in fact posted, so no repeal-grep ever fired on it, and two claims in it stayed public after both were superseded. It is the clearest case in this inventory of a stored boolean the world could answer: the bot can now read the channel, so whether a message exists is observable. Recorded on `[announcement-back-catalogue-rehomed]`.

## Frame assessment

**TIME RANGE** — a snapshot of the corpus as it stands at plugin version 1.21.1-test3, 2026-08-31. It has no time range beyond that and does not need one; it is an inventory, not a trend.
**PEOPLE** — for whoever scopes the MCP work. Not user-facing, and nothing here is a claim about consumers.
**FRESHNESS** — amended on the same cycle as the corpus itself, which changes at nearly every build. Expect it to be stale within a few sessions; re-run the sweep rather than trusting the table.
**RISK IF WRONG** — a state classified computable that is really a decision would have an MCP design silently discard part of the decision trail, which is the one thing the umbrella item says must not happen. That is why every DECISION row states *why* it is not computable rather than merely asserting it, and why the two explicitly-uncomputable entries (the rule gate, the format epoch) carry their recorded refusals.
**ALTERNATIVES** — the classification frame is the two-kinds split recorded on `[mcp-server-standing-intent]`, adopted rather than derived here. MIXED was added by this sweep because the two-way split could not place `Blocked by:`, and the addition is the sweep's own contribution rather than a finding about the world. No other frame was considered.
