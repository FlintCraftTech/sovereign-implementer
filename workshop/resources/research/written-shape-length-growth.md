# Written-shape length growth

**Measured**, by `plugin/throughliner/scripts/measure_written_shape_length.py` (moved there 2026-08-20 when the script began shipping; it was `resources/measure_written_shape_length.py` when this was written). Every figure is a word count against a date. No threshold is stated here and none may be read off the middle of these distributions — this is the corpus the measurement exists to question, so its typical length is not a target.

## Captures — length when first filed

852 items, first appearance in QUEUE.md.

**Coverage limit.** QUEUE.md's history starts 2026-06-01, but the earliest item this reads is 2026-07-02. The queue used a different section structure before the two-section model, so snapshots older than that parse to no items and contribute nothing. Read the earliest month as the start of the measurable record, not the start of the project.

| month | n | min | median | mean | max |
|---|---|---|---|---|---|
| 2026-07 | 187 | 0 | 176 | 265 | 7912 |
| 2026-08 | 665 | 0 | 336 | 389 | 1901 |

## Work items — growth from first filing to Processed

511 items currently in Processed, each compared against its own first-filed length. Grouped by the month it was FIRST filed.

| month | n | min | median | mean | max |
|---|---|---|---|---|---|
| 2026-07 | 91 | -2929 | 0 | 45 | 1701 |
| 2026-08 | 420 | -412 | 141 | 219 | 4425 |

Per item, largest growth first:

- [rule-lifecycle-system] filed 2026-08-10: 1528 -> 5953 words
- [rename-to-throughliner] filed 2026-07-31: 494 -> 2195 words
- [rule-corpus-over-ceiling] filed 2026-08-11: 165 -> 1597 words
- [approval-flow-token-doubling-simplification] filed 2026-08-01: 294 -> 1460 words
- [queue-pointer-hard-to-follow-and-possibly-stale] filed 2026-08-05: 856 -> 2013 words
- [close-sweeps-unattributed-hand-edit] filed 2026-08-10: 357 -> 1483 words
- [nothing-blocks-it-read-as-a-dead-end] filed 2026-08-13: 520 -> 1601 words
- [fences-wrap-so-prose-rule-reason-is-false] filed 2026-08-07: 435 -> 1499 words
- [self-hosting-auto-detection] filed 2026-07-29: 127 -> 1149 words
- [concurrent-session-support] filed 2026-07-12: 122 -> 1071 words
- [plan-close-priorities-over-reorder] filed 2026-08-05: 460 -> 1367 words
- [method-advice-invents-capabilities-on-domain-mapping] filed 2026-08-04: 643 -> 1532 words
- [message-ending-drives-the-suggestion-chip] filed 2026-08-13: 504 -> 1367 words
- [dispatch-return-check-blind-across-projects] filed 2026-08-07: 498 -> 1360 words
- [isolation-model-is-not-ours-to-choose] filed 2026-08-11: 374 -> 1214 words

## LOG entries — by flavor

550 entries. Earliest per-entry file: 2026-06-12 — everything before that date lives in the legacy combined log and is not measured here.

### plan entries — 126

| month | n | min | median | mean | max |
|---|---|---|---|---|---|
| 2026-06 | 36 | 106 | 464 | 452 | 787 |
| 2026-07 | 51 | 151 | 323 | 340 | 837 |
| 2026-08 | 39 | 279 | 895 | 1010 | 3658 |

### build entries — 424

| month | n | min | median | mean | max |
|---|---|---|---|---|---|
| 2026-06 | 85 | 83 | 300 | 335 | 1226 |
| 2026-07 | 91 | 87 | 229 | 245 | 740 |
| 2026-08 | 248 | 95 | 478 | 498 | 1766 |

## LOG index lines — line length, and the entry it points at

545 index lines resolved to an entry file.

| month | n | min | median | mean | max |
|---|---|---|---|---|---|
| 2026-06 | 117 | 15 | 39 | 47 | 241 |
| 2026-07 | 142 | 12 | 40 | 44 | 103 |
| 2026-08 | 286 | 17 | 76 | 85 | 337 |

Longest index lines, with the entry each points at:

- 2026-08-09: index line 337 words -> entry 1710 words (2026-08-09-plan-3.md)
- 2026-08-13: index line 248 words -> entry 2511 words (2026-08-13-plan-2.md)
- 2026-08-14: index line 247 words -> entry 1265 words (2026-08-14-plan.md)
- 2026-08-13: index line 241 words -> entry 1248 words (2026-08-13-plan.md)
- 2026-06-15: index line 241 words -> entry 657 words (2026-06-15-goal-2026-06-14.md)
- 2026-08-10: index line 228 words -> entry 1766 words (2026-08-10-queue-machinery-repair-freeform.md)
- 2026-08-14: index line 225 words -> entry 1378 words (2026-08-14-snr-ad-contradictions-and-misplacements.md)
- 2026-08-11: index line 221 words -> entry 1355 words (2026-08-11-plan.md)
- 2026-08-09: index line 219 words -> entry 1839 words (2026-08-09-plan-2.md)
- 2026-08-14: index line 218 words -> entry 1434 words (2026-08-14-retiring-a-step-leaves-its-artifacts.md)
- 2026-08-14: index line 216 words -> entry 3658 words (2026-08-14-plan-4.md)
- 2026-08-11: index line 213 words -> entry 1419 words (2026-08-11-plan-2.md)
- 2026-08-13: index line 209 words -> entry 1133 words (2026-08-13-plan-3.md)
- 2026-08-13: index line 194 words -> entry 1224 words (2026-08-13-rename-to-throughliner.md)
- 2026-08-10: index line 190 words -> entry 1433 words (2026-08-10-plan-2.md)

## Added 2026-08-15 — did the length rule change anything?

**The question.** A rule telling Claude to match a written file's length to what the task needs, naming queue rationale and LOG entries explicitly, shipped on 2026-08-13. [invented-rationale-compounds-past-the-shipped-rule] had been skipped three times waiting for exactly this observation: whether volume falls now the rule exists, before any fourth mechanism is designed. The monthly buckets above cannot answer it, because the rule landed mid-month. August was therefore split at the ship date, using the same script's own `queue_lengths()`.

**Capture length at first filing, split at the rule's ship date:**

| window | n | median | mean | max |
|---|---|---|---|---|
| 2026-07 (pre-rule) | 187 | 176 | 265 | 7912 |
| 2026-08-01 to 08-12 (pre-rule) | 515 | 321 | 368 | 1707 |
| 2026-08-13 to 08-15 (post-rule) | 152 | 396 | 461 | 1901 |

**The finding: volume did not fall. It rose — about 23% on the median and 25% on the mean.** On the available evidence the third remedy has not worked, and the direction is the opposite of the one it aimed at.

**Three caveats, none of which rescues the rule.** The window is three days, though n=152 is not a small sample. The rule's home moved during that window — it shipped inside an output style that was deleted on 2026-08-14 and re-homed into the always-loaded rules — so part of the period ran it from a file that no longer exists; that is a reason the rule may have been weakly present, not a reason to read the numbers as a fall. And word count cannot distinguish invented rationale from reasoning genuinely reached, which is the caveat this file already carries and which still applies: these numbers answer the *volume* half of that item and say nothing about the *provenance* half.

**What it licenses.** The item's own condition was that a fourth mechanism should not be designed on an untested third. The third is now tested. All three remedies to date have been prose — state the rule, sharpen the rule, add a length rule — and the corpus now has a measured non-result for the last of them alongside its earlier finding that attribution held while volume grew regardless. A fourth prose remedy is the one shape the evidence rules out.

