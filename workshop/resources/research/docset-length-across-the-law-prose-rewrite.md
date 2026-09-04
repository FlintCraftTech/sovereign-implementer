# Docset length across the law-prose rewrite — what the numbers say

Measured 2026-09-04 during the law-prose article walk-through, from git, with
`wc -w` over `plugin/throughliner/docs*/` at each commit. The rules file is
`skill-nonspecific-rules.md`, the one every session reads; the docset is every
`.md` in the shipped procedure-docs folder at that commit (named `docs-b/`
until 2026-08-21, `docs/` after).

| Commit | Date | Rules file (words) | Whole docset (words) | What the commit was |
|---|---|---|---|---|
| de2f5fc | 2026-08-16 | 9,485 | 49,305 | before the law-prose restyle |
| 7e3c1c8 | 2026-08-17 | 9,918 | 51,115 | the always-loaded rules restyled |
| b485ee3 | 2026-08-20 | 10,132 | 56,341 | |
| a2e9f2b | 2026-08-21 | 10,132 | 56,697 | `docs-b/` becomes `docs/` |
| cc33c1e | 2026-08-21 | 10,402 | 55,281 | the corpus restyled and its rationale split |
| 9c98504 | 2026-08-21 | 10,185 | 50,626 | the freeform decision-history cut: 528 lines out of thirteen docs, every rule kept |
| 576506c | 2026-08-22 | 10,247 | 50,662 | |
| beac9d2 | 2026-08-27 | 11,916 | 58,201 | |
| HEAD (a33f6a4) | 2026-09-04 | 13,859 | 67,009 | before this run's edits |

**Findings.**
- The law-prose restyle of the rules file (2026-08-17) made it about 430 words
  longer, not shorter. Its own acceptance test was a flat rule-statement count:
  299 before and after (`LOG/2026-08-17-law-prose-restyle.md`).
- The one real reduction was the 2026-08-21 decision-history cut: 56,697 →
  50,626 words, −6,071, about 11% of the docset, with no rule removed
  (`LOG/2026-08-21-cut-length-remaining-docs-2.md`).
- Since that cut the docset has grown by a third (50,626 → 67,009) and the
  rules file by 36% (10,185 → 13,859), through rules being admitted, not
  through the writing sliding back.
- The earlier figure the article opens on — plugin-behaviour.md growing from
  6,162 to 21,445 words in a week before the 2026-08-09 revert — is a different
  document and a different period (`LOG/2026-08-09-plan.md`).

**Why it is filed:** the article's section 4 was redrafted around these numbers
on 2026-09-04, and the article will be edited further; the numbers exist nowhere
else in one place.

**Frame assessment.**
- TIME RANGE: 2026-08-16 to 2026-09-04, the whole life of the law-prose
  standard so far; the product addresses no range, so none was stated.
- PEOPLE: not applicable — a measurement of this repository's own files.
- FRESHNESS: HEAD moves every session; the row is dated and the command is
  reproducible at any later commit.
- RISK IF WRONG: an article claim about doc length would be false; the counts
  are `wc -w` over named commits and can be re-run.
- ALTERNATIVES: counting rule statements (`rule_signals.py`) was the earlier
  measure and is reported alongside; counting characters or lines was not
  done, and would move together with words.
