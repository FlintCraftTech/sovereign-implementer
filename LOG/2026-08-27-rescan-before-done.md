# beac9d2 — The rescan is recommended wherever the close is named, and the close's own scan stands down when one just ran

Two halves of one idea, captured by the user at the session's rest and processed in the same exchange.

**One: the recommendation goes where closing comes up, and nowhere else.** The end-of-queue gate in `plan.md` and the close hand-off in `next.md` each gain a clause naming the rescan first — so the suggestion arrives exactly when the user is deciding whether to stop, never mid-work. That siting is the whole design: a rescan recommended during a build would be an interruption, and one recommended after the close would be too late.

**Two: the close's wind-down scan does not re-run when a rescan literally just ran.** The window rule already limited the close's scan to what the last rescan did not reach; this adds the final step. Where nothing has happened since — no work, no decisions, only the close being invoked — the close performs no second pass and its record carries one line, "covered by the rescan just run". Conversation between the rescan and the close is still scanned under the existing window rule, so the stood-down arm reaches only a genuinely empty window.

**The required line is not decoration.** A stood-down scan and a scan that never happened are indistinguishable from outside, which is the exact condition this method keeps building required artifacts to remove. Without the line, "the close skipped its scan" would be unfalsifiable.

**A fourth site exists and was deliberately not touched.** `next-audit.md`'s close names /done without the clause, so a run of only audit items reaches its end and never hears the suggestion while a run with a build item does. The item scoped itself to two named sites, and extending to a third would have been scope the user never agreed. Filed as [audit-close-missing-rescan-clause]. `next-build.md`'s abort path is genuinely different — it names /done after a failed item, not at a session's rest — and is not part of that finding.

**A wording trap worth recording:** the two `plan.md` gate sentences are identical in content and wrap differently, so a replace-all matched only one. Both were checked by grep afterwards rather than assumed.

**Files:** `plugin/throughliner/docs/plan.md`, `done.md`, `next.md`.

**SPEC lags one sentence**, filed rather than written: this changed what the method says to the user, and SPEC's `/rescan` paragraph does not yet say the method offers the rescan at the points where closing comes up. Filed as [spec-owes-rescan-recommendation].

Rule gate: run — both halves are amendments to existing steps (the gate's wording; the wind-down's window rule), parents named, nothing evicted.

Routed to Captures: [audit-close-missing-rescan-clause], [spec-owes-rescan-recommendation]
