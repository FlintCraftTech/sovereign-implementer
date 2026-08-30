# [HASH] — Audit findings always route to the queue, and the actionable filter comes out

Two rewordings from one ruling the user gave on 2026-08-29, after a live instance the same day: Claude read the always-loaded triage's middle arm ("a finding → the observing chat's LOG entry") over the audit procedure's "findings route to Unprocessed", and recommended routing a repository inventory out of the queue. Her words: findings of audits always belong in the queue — it's work (planned writing) that doesn't.

The triage's middle arm now carries the exclusion explicitly, and carries its reason as operative text rather than as an attached why: findings are filed for the user to weigh, and nobody processes a session record, so a finding parked there is one the user never meets. Delete that clause and the rule stops being applicable, which is the test for keeping it in the operative sentence.

The second half is a distinct ruling of hers rather than a consequence of the first. `next-audit.md`'s "one finding per actionable change" becomes one finding per discrete observation, because Claude does not decide whether a finding is actionable — it already exercises enough discretion deciding what counts as a finding within the audit's parameters. Worth-doing is settled at /plan, with the user present. A filter running in a silent step before the work reaches her can only drop things, never surface them.

Kept on Claude's recommendation and her non-objection: `next-audit.md`'s `dropped` route for a finding Claude re-reads and finds factually wrong before filing. That doc's own text already fences it from being a worth-it judgment or a user-rejection route.

The change was exercised the same session: this run's own audit filed five findings and dropped none, and its close records that as a routing count rather than as an approval outcome.

**Observable met:** a grep for "actionable" in `next-audit.md` returns nothing, and the triage's middle arm names the audit exclusion.

**Depth:** full — reasoning contested.
**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md`, `plugin/throughliner/docs/next-audit.md`.
**Routed to Captures:** none from this item.
