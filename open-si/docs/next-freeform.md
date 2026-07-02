# Freeform procedure

Execution procedure for freeform work. Reached from next.md when a Freeform batch sits at the top of the queue, or when the user runs `/next freeform` on-demand and the gate has confirmed the work fits none of build, test, or audit.

Freeform is the fourth /next type: a place for unqueued or loosely-scoped work — an ad-hoc change, a discussion of edits already made, surfacing something without the pressure of processing it. It's a refuge from ceremony, not from discipline. The scope lock still holds, problems are still stated plainly, and nothing unrouted survives the session. What's relaxed is structure: there's no fixed entry list to tick and no completion signal, because freeform work doesn't always know its own shape up front.

## Scope lock, ask-by-ask

A queued build batch names its files at planning time; freeform usually can't, because the work is discovered as it goes. So the scope lock grows by asking:

1. **Create _build.md** with an empty `Files:` section — the same structure next.md Step 2 uses, but with no files listed. An empty `Files:` locks the session to the method docs only (QUEUE.md, LOG/, _build.md), exactly as an audit's empty list does.
2. **Each file the work needs is requested and added before it's edited** [PROMPT]: name the file and why it's needed, and on the user's okay, append its bare path to _build.md's `Files:` section — then edit it. The scope lock denies any file not yet listed, so the ask comes before the edit, never after. This is the build's "scope grows" ask made the normal rhythm rather than the exception.

For a queued Freeform batch, copy its text into _build.md's Entry as next.md Step 2 does, but still start `Files:` empty unless the batch named specific files — freeform scope is granted ask-by-ask regardless.

## Do the work

Make the changes, have the discussion, surface what needs surfacing. Accumulate close notes in _build.md's Changes as you go — what changed and why — so /done needn't re-explore. There's no entry list to tick, so Changes is the record the session leaves behind.

State problems plainly as they come up. If something looks like a security, privacy, or breach risk, raise it as a red flag (plugin-behaviour.md Red flags) — freeform doesn't relax that.

## Captures can be made, never processed [PROMPT]

Freeform may surface ideas and observations. Making a capture — drafting its wording and writing it to Captures — is open here, same as any session. Processing a capture — promoting, parking, or dropping it — is /plan's alone, and freeform doesn't change that.

So when the session yields captures, warn the user plainly: /next can file these to Captures, but it can't process them — that waits for /plan. Then offer the choice: move this work to /plan now to process them, or continue here and let /plan pick them up later. Wait for the user's call.

## No completion signal

Freeform has nothing to tick, so there's no "all entries done" moment and no Completion section. The session closes when the user runs /done — that's the only close. The one close prompt Claude initiates is the standing context-running-long nudge: if context gets tight mid-session, suggest wrapping up the current thread and running /done, so the next session resumes cleanly from _build.md.

Do NOT delete _build.md yourself. That's /done's job.
