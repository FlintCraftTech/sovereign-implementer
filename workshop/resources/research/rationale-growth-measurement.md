# Rationale growth, measured

Measured 2026-08-10 by the `[rationale-growth-audit]` item; approved as-is by the user. Source LOG entry: `LOG/2026-08-10-rationale-growth-audit.md`, commit `94bba66`. Consolidated into this file on 2026-08-11 from five separate queue items, which were deleted once their content landed here.

**Why this is a file rather than five queue items.** None of them was work: ask what changes inside which files and the answer is nothing, so each would fail the keep-check's second limb and halt a build run that reached it. They are findings, and the method routes a durable finding to `resources/research/` when a future session needs to re-read it word for word — which these meet, for the reason in §5.

**Method.** A script walked every commit touching `QUEUE.md` since 2026-07-20 — 113 commits — and for each slug compared its first Unprocessed form against its first Processed form, and separately its first Processed form against its latest. 186 items had both a capture form and a processed form. The method is reproducible, so the figures can be re-taken later to see whether any fix moved them.

## 1. Processing roughly doubles a work item

59,216 capture words became 107,795 processed words across 186 items. Median growth factor **1.77** — a median 290-word capture becomes 536 words.

This is the number the argument in `[invented-rationale-compounds-past-the-shipped-rule]` had been conducted without; every previous proposal there was reasoned from single instances.

What it does and does not license: it establishes the scale of the effect and gives any future rule something to be derived from, which `[derivation-required-for-limits]` requires. It does **not** by itself say the growth is wrong. Processing is supposed to add the decisions reached in the interview.

## 2. The growth is concentrated, not uniform

The distribution is long-tailed. The worst item grew **17×**, the top ten account for a disproportionate share of all added words, and roughly **thirty items shrank** during processing.

So "processing adds reasoning" is not a general property of processing — a small minority of items does nearly all of it.

**Consequence for any fix.** A rule applied at every keep-step would tax the majority that is already fine in order to reach the few that are not — the shape `[rule-lifecycle-system]`'s Constraint D warns about, where a broadly-scoped obligation is the one that goes unperformed. Whatever is done should be narrow enough to fire on the outliers. What identifies an outlier *in advance* is unanswered by this measurement.

## 3. The worst-growing item compressed by 56% when reworked

`[concurrent-session-support]` went from 130 words as a capture to 2,267 at processing — the largest growth in the measured set — and then to 994 when a later session reworked it. A human-driven pass removed 56% of it without the design being lost; the item remained buildable and kept its rejected alternatives.

**This is the only finding that speaks to whether the added words were worth their cost, and for at least one item it says no.** It also suggests a lever nobody had proposed: a rework pass over an already-processed item is demonstrably productive, where every previous proposal tried to prevent the growth at the moment of writing.

**The honest bound: n=1.** One item, read by hand. It shows the growth *can* be compressible; it does not show it usually is.

## 4. Growth happens at processing and barely afterwards

Comparing each item's first Processed form against its latest: only **27 of 186** items grew at all after processing, adding **1,815 words** between them — against roughly 48,000 words added at the capture→processed step itself.

**This contradicts a premise the queue had been reasoning from.** `[invented-rationale-compounds-past-the-shipped-rule]` describes rationale as compounding, re-authored and added to at every stage. Measured, it does not: there is one step where growth happens and the rest of the chain is nearly flat.

That is good news for any fix — one moment has to be addressed rather than a pipeline — and it means the re-author-forward design is not the leak it was suspected of being.

## 5. What these numbers cannot show — carry this with any citation

Word counts measure volume and nothing else. **They cannot distinguish reasoning Claude produced unprompted from decisions the interview genuinely reached**, which is the actual question `[invented-rationale-compounds-past-the-shipped-rule]` asks. Nor can a count tell a rule holding from a session that happened to write less.

**This section is why the five findings are one file.** These figures are unusually quotable, and a number in the record gets cited later without its limit. The risk is a future session reading 1.77 as a measure of invention and designing against it. Split across five separate items, four are quotable alone and this one is the one nobody opens; bound into the same document, the caveat cannot be dropped by accident.

§3 is the closest anything here comes to evidence on the real question, and it is one item read by hand, not a measurement.

## Live consumers

- **`[rule-lifecycle-system]`'s Maintained stage**, designed 2026-08-11, whose subject is whether accumulated text is compressible. §3 is the finding that bears on it directly.
- **`[invented-rationale-compounds-past-the-shipped-rule]`**, whose compounding premise §4 contradicts.
- Any future limit on rationale length, which under `[derivation-required-for-limits]` must state what it was derived from. §1 and §2 are the available derivations — and §2 says a uniform limit would be aimed at the wrong target.
