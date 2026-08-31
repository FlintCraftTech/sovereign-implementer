# 778d6a3 — The test-rezips readiness check gains a required line in the close's record

Found live on 2026-08-29: the close of a 23-item run did not run the check, and nobody would have known if the user had not asked why the previous rezip was unposted.

**Why it was missed rather than refused.** The close works through `done.md` and its flavor sub-doc, and this check lives in `CLAUDE.md` outside that sequence. A close can complete every step its own procedure names and never touch it. That is a step with no site rather than a discipline failure.

**And it left no trace either way**, which is what made it recur: a clean run and a run that never happened look identical afterwards. This project has solved that shape three times already — the rule-gate disposition, the forward-advisory disposition, the FAQ disposition — each by requiring a recorded line in the session record rather than by hoping.

So `CLAUDE.md`'s test-rezips section now carries the line in three forms: ready, not yet, or none.

**Settled at processing, with a counter-argument that dissolved on inspection.** The shipped close doc cannot hold it — consumers have neither the bot nor the channel, so the obligation could never fire for them. And residence was not what failed: `CLAUDE.md`'s other close obligations fire because each has a required artifact or a mechanical trigger, and this check had neither. The line is the missing artifact.

**The honest limit is carried in the text, as the shape always carries it:** a line can be written dishonestly and nothing checks that. What it buys is that a *missing* line is visible.

This close is the first to owe one, and the answer is `none` — no rezip has happened since the 1.21.1-test1 entry was posted in this same session.

**Observable met:** the section carries the three-form block.

**Depth:** full — alternative seriously weighed.
**Files touched:** `CLAUDE.md`.
**Routed to Captures:** none from this item.
