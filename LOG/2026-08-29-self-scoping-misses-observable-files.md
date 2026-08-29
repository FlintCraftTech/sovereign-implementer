# 7b751b6 — plan — the observable's files join the decision step's list, and the matching /next clause is refused

`/next` derives a run's scope from an item's **Changes** line, but the **Observable** line routinely names other files — the suite that must pass, the sibling doc an acceptance check greps. Twice in one run those were missing, the scope-lock refused them mid-build, and the run stopped to ask. Nothing was built out of scope; the cost was two interruptions in a run designed not to need any.

**The fix goes at the decision step, with evidence from the session that settled it.** Every item cleared on 2026-08-29 already names its observable's files among its changed files — the register guard names its suite, [digest-answers-whats-next] names `test_queue_digest.py`, [ritual-declares-writable-paths] names `test_plan_quiet_list.py`. That happened by habit rather than by rule, which is the argument: the requirement is followable at no cost with the user in the room, and free to state.

**Rule gate: run — an amendment.** A fifth item in the decision step's existing four-item enumeration of what a kept item carries, sharing its shape, so no freestanding rule.

**Refused: a matching clause at `/next`'s scoping step.** It would duplicate — fixing the input removes the failure rather than catching it downstream, and `/next` already handles a genuine ripple correctly, having noticed both instances, added the file on approval and recorded it at the tick.

**The cost of that refusal is stated rather than discovered:** every item already in the queue was written under the four-item form, so `/next` will keep meeting this on legacy items until they are built out. It decays rather than persisting.

**Queue changes:** [self-scoping-misses-observable-files] kept and cleared; SPEC's matching list updated.
**Work processed:** kept — [self-scoping-misses-observable-files].
