# QUEUE

## Red flags

Security, privacy, and data-exposure risks the agent has surfaced — kept at the top so they're the first thing seen each session. Each carries a state: open, resolved, or accepted. Empty until a risk comes up.

## Batches

Worked top to bottom. Each batch is one /next session. Subheadings name the kind of work (Build, Test, Audit).

### Parked

## Deferred tests

Verification waiting on an event — not a parallel to-do list. A planned test lands here when it can't run in the session that planned it: the behaviour only goes live after a reinstall, a person has to do something first, or an outside event hasn't happened yet. Each line records what to verify, what will confirm it, and two things about the wait — the deferral reason (why it waits: host-side / needs-user / external) and the runnability (who runs it: agent-runnable / user-run). Agent writes lines here and clears them; each /plan asks which waits have cleared and rolls the now-runnable ones into a test batch. You don't maintain this section.

## Captures

Captured outside /plan. Picked up and routed during the next /plan session.

### Parked
