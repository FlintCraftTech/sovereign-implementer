# Getting Claude to notice an unverified premise and offer the search unprompted

Compiled 2026-08-30, on the spot in the planning session that asked. The
question: the user still has to ask for research most of the time, most users
will not know when to ask — so how do you make the offering fire without them?
The companion file `risk-classes-beyond-security.md` establishes what the
costliest un-noticed class is; this one is about the noticing itself.

## What the outside literature says

- Instructing models to admit uncertainty works measurably — explicit
  admit-when-unsure prompts reduce hallucination substantially in many
  contexts ([Lakhera, prompt-engineering and hallucinations](https://devopslearning.medium.com/can-we-reduce-hallucinations-in-llms-through-prompt-engineering-df7d275d9cfa);
  [tonybaloney, can you prompt LLMs to tell the truth](https://tonybaloney.github.io/posts/the-big-fib-can-you-prompt-llms-to-tell-the-truth.html)).
  **But the mechanism depends on the model feeling unsure**, and models
  seldom acknowledge inability — they answer instead
  ([uncertainty expression outside parametric knowledge](https://arxiv.org/pdf/2311.09731);
  [confidence elicitation survey](https://arxiv.org/abs/2306.13063)).
- **Premise-driven errors bypass uncertainty entirely**: a model can hold the
  correct fact and still trust a false premise embedded in the task, feeling
  no doubt at any point
  ([premise verification via retrieval-augmented reasoning](https://arxiv.org/html/2504.06438)).
  This is the shape of the user's costly instance: no question was ever asked
  that felt uncertain — the unverified thing was load-bearing, not queried.
- Self-monitoring under-performs external structure: agents' own verification
  is superficial, confident language is mistaken for completion, and
  **deterministic gates recover failures that self-auditing misses**
  ([false success in LLM agents](https://arxiv.org/pdf/2606.09863);
  [verify before you commit](https://arxiv.org/html/2604.08401);
  [deterministic gates vs silent policy violations](https://arxiv.org/pdf/2607.07405)).

## What this project's own record says — and it agrees

- **Every noticing rule that works here is site-bound**: the capability check
  fires at the moment of tagging `[user]`; the re-verify fired because it was
  written into the item as a step; the claims sweep fires on a cadence at a
  named observable. **Every free-floating duty has failed at least once**: the
  method records the siteless-check failure five times, and the always-loaded
  offer-a-search rule was loaded and silent through the costly instance.
- The freshest specimen is first-hand (2026-08-30, this session): research was
  misrouted into the queue against a shipped rule that was read at session
  start — rule presence did not produce rule firing; an outside reader's
  challenge did ([research-misrouted-to-queue-live-instance]).

## A further instance, from the session that commissioned this file (appended 2026-08-31)

In the 2026-08-30 planning session researching exactly this failure shape, two research efforts were processed into Processed as cleared build items — against two shipped rules both loaded in that session (plan.md's resolve-now list names research first among what planning does on the spot, and its decision step says a research item wearing a build's shape must not pass the check). The same session had followed the pattern correctly hours earlier (the determinism example bank, researched and filed within the hour of being asked). The user caught it from outside ("research is not queued work — it's always done on the spot"); both items were pulled and the research run on the spot the same day. First-hand confirmation of this file's core claim: rule presence does not produce rule firing, and the miss was invisible from inside until an outside reader challenged it. (Relocated from the deleted queue capture [research-misrouted-to-queue-live-instance], 2026-08-31.)

## The finding

Exhortation is the weak lever and site-binding is the strong one, on both
evidence bases independently. The productive question is not "how do we tell
Claude to notice better" but "at which committed moments should a mechanical
step ask the premise question". Candidate sites, ranked by how much recorded
loss each would have reached:

1. **The decision step, per kept item**: name the external facts the item's
   design rests on, and for each, when it was last verified — a "rests on"
   line beside Files. Would have reached the stale-research and
   environment-generalisation instances; the strongest candidate.
2. **The below-line revisit and every re-offer of a dated capture**: re-ask
   what the item's premise rests on and whether anything has verified it since
   it was written. Reaches slow-cooking work — the shape of the months-long
   instance.
3. **Sustained-effort checkpoints outside this method's reach** (the costly
   instance happened in ordinary conversation, not under any skill): only an
   always-loaded rule reaches there, which is exactly the kind shown weakest.
   Named honestly as the residual rather than papered over.

**No wording is adopted here.** Each candidate files as its own capture for
the rule gate at a planning turn, citing this file — and the gate's evidence
question is answered by the instances above, per candidate, not in bulk.

**The honest limit:** site-bound checks reach the sites they are bound to.
The residual — a premise going unverified in a moment no mechanism watches —
remains, and any rule this produces must say it improves odds only.
