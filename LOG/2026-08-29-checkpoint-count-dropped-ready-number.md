# 7b751b6 — plan — the checkpoint count dropped half of what the user asked for, and her own recorded wording proves it

The user noticed a checkpoint showing one number where she had asked for two: *"when I asked for one to be displayed, the other disappeared. I meant we needed both."* She asked whether a rule had produced it.

**One had, and the record settles it rather than leaving it to memory.** `LOG/2026-08-27-checkpoint-carries-remaining-count.md` quotes the wording that produced the current rule: the line *"might more usefully have read '… — 20 ready. X yet to be processed.'"* That is two numbers. The shipped rule kept one, and then says "nothing else".

**Where the reasoning went wrong is the useful part.** The justification given was that the other number is a record of what has been done — so many kept, so many deleted — and that such a tally is clutter mid-decision. The ready count is not that: it is the size of the cleared region, forward-looking, and the thing that says whether there is work to run. A ban aimed at a retrospective tally swept out a forward one that was never in its scope.

**Both readings were put to the user before anything was written**, since guessing at her wording is what caused this. She chose **ready** — which is also what her 2026-08-27 wording said, and which needs no ban reopened.

**Rule gate: run — an amendment with an eviction**; the wrong justification comes out in the same edit and the retrospective-tally ban stays untouched.

**No SPEC sentence owed, checked rather than assumed** — SPEC's processing-flow paragraph describes the checkpoint's skip behaviour and mentions neither count.

**A separate failure from the same message is recorded as a finding, not filed as work:** that checkpoint also carried a sentence explaining what the count excluded, which the rule already forbids. Nothing to build.

**Queue changes:** [checkpoint-count-dropped-ready-number] filed and cleared.
**Work processed:** kept — [checkpoint-count-dropped-ready-number].
