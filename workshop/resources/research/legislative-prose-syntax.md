# How legislative prose is actually shaped: sentence syntax and the test for subordination

Researched 2026-08-09, at the user's direction. The companion to
[`legal-drafting-for-tight-rules.md`](legal-drafting-for-tight-rules.md), which took the
*structural* lessons (amendment vs freestanding, consolidation, recasting) and the *style*
devices, but left the prose itself unexamined. The user's framing: we threw the baby out —
there need to be specific rules about what makes one rule a subset of another.

This file answers that question, and one other it turned up on the way.

## 1. The legislative sentence has named parts

The convention originates with George Coode, mid-19th century, and is still the spine of
drafting manuals. A legislative sentence carries three elements:

- **Legal subject** — the person or class whose position the rule changes.
- **Legal action** — the right, power, privilege or duty the rule confers or imposes.
- **Case and condition** — the facts that must have occurred and the circumstances that must
  be present for the rule to operate.

Most law works by changing a person's position, so a sentence missing one of these is
usually incomplete rather than merely terse. Applied to the method: a rule that names no
actor and no action is not a tightly-written rule, it is an observation.

## 2. Where the condition goes is genuinely contested — and our current rule takes the losing side

Coode put the case and condition **first**, so the reader knows whether the provision
applies before reading what it does. That convention is what
`legal-drafting-for-tight-rules.md` §4 absorbed, and it is what
`self-authoring-rules.md` now instructs: *signal an exception before the general rule.*

The Canadian Department of Justice's *Legistics* takes the opposite position, and does so on
evidence rather than tradition: modern linguistic research finds that adverbial clauses at
the start of a sentence **increase** comprehension difficulty, because readers need the
principal parts of a sentence before they can place the rest of the information. Their
worked contrast:

> "An inspector may take measures if [conditions]" reads better than
> "If [conditions], an inspector may take measures."

Their rule is therefore **main clause first**, especially when the conditions are long.

**This is a live contradiction inside the method's own gate, not a curiosity.** The gate's
wording section currently carries the 19th-century convention as an instruction. Both
positions are defensible — Coode's serves a reader scanning for applicability, Legistics
serves a reader trying to understand a provision — but the method has taken one side by
inheritance rather than by decision. Worth noting which reader the method actually has:
Claude reads every rule in the corpus every session, so scanning-for-applicability is not
the dominant mode; understanding is. That argues for main-clause-first.

## 3. The subordination test — what makes one rule a subset of another

This is the answer to the question that prompted the research, and it is more precise than
expected. Legislative drafting does not decide subordination by topic or by feeling. It
applies **syntactic** tests to the relationship between a parent provision's opening words
(the *chapeau*) and the units beneath it.

A unit is a genuine paragraph of its parent when all of these hold:

1. **There are at least two parallel units.** A single subordinate unit is not a
   subdivision; it is the parent, written badly.
2. **Grammatical compatibility.** Each unit must read grammatically as a continuation of the
   opening words. Chapeau + unit must form a well-formed sentence.
3. **Grammatical equivalence.** All units must have the same grammatical function and modify
   the same part of speech. Mixing a condition and an obligation in one list breaks this.
4. **Consistent modification.** Every modifier inside a unit must modify either the same
   thing in the opening words, or something inside that unit — never something in a sibling.
5. **No complete sentences.** A unit that stands as a complete sentence is not subordinate to
   anything; it is a separate provision wearing a bullet.

Test 5 is the sharpest for the method, and the one it fails most often. Most nested bullets
in `plugin-behaviour.md` are complete sentences — frequently complete *paragraphs* — which
means they are freestanding rules formatted as subordinate ones. Under the instruction-count
ceiling that distinction is not cosmetic: a genuine subordinate unit shares its parent's
slot, and a complete sentence consumes its own.

**So the test for "is this rule a subset of that one" is: can it be written as a fragment
that completes the parent's opening words?** If it can, it is subordinate and costs nothing.
If it cannot, it is a freestanding rule and must earn admission on its own.

## 4. The nesting hierarchy, and what it is for

Section → subsection `(1)` → paragraph `(a)` → subparagraph `(i)` → clause `(A)` →
subclause `(I)`. The labels matter less than the discipline they enforce: each level is a
grammatical subdivision of the level above, not a topical grouping. A section holds one
idea; when a sentence expressing it grows past comprehension, it is divided into units that
still read as one idea when read together.

Two placement conventions worth carrying:

- A statement applying to a whole section is the **first** subsection of it, not a trailing
  note.
- Provisions are ordered principal operative → special and subordinate → enforcement →
  definitions.

## 5. On sentence length, against the instinct

*Legistics* explicitly rejects an absolute brevity rule: "it is a mistake to assume that
legislation can or should always be drafted in short sentences." A long sentence can show a
logical link that two short ones lose. Splitting is right when a sentence holds
undistinguished groups of ideas that strain short-term memory, when paragraphing is not
available, or when the original obscures an ambiguity — and splitting still has to preserve
the relationships the single sentence carried.

This is a useful corrective to a subtraction pass: the goal is fewer *instructions*, not
shorter *sentences*, and chopping a well-formed conditional into three staccato rules makes
the count worse while reading cleaner.

## 6. What this implies for the method

Recorded as analysis, not decision.

- The subordination test in §3 is directly usable as an admission sub-test: before a rule is
  admitted as freestanding, try to write it as a fragment completing an existing rule's
  opening words. Success means it was an amendment all along.
- The condition-placement rule in `self-authoring-rules.md` §4 should be re-decided rather
  than left as inherited convention (§2).
- Most nested bullets in the corpus are complete sentences, so the file's apparent hierarchy
  overstates how much of it is genuinely subordinate. A count that treats nesting as
  subordination will under-report.
- §5 warns against a plausible failure of the eviction work: measuring success by sentence
  length rather than instruction count.

## Sources

- [Legistics — Paragraphing (Department of Justice Canada)](https://www.justice.gc.ca/eng/rp-pr/csj-sjc/legis-redact/legistics/p3p1.html)
- [Legistics — Sentence Structure: Complexity and Organization (Department of Justice Canada)](https://www.justice.gc.ca/eng/rp-pr/csj-sjc/legis-redact/legistics/p2p4.html)
- [How to Draft the Legislative Sentence — Mary Osmond](https://maryosmond.com/2007/09/22/how-to-draft-the-legislative-sentence/)
- [The Basic Elements of a Legislative Sentence — Commonwealth iLibrary](https://www.thecommonwealth-ilibrary.org/index.php/comsec/catalog/download/873/873/7312?inline=1)
- [Statutory Structure and Legislative Drafting Conventions: A Primer for Judges — Federal Judicial Center](https://www.fjc.gov/sites/default/files/2012/DraftCon.pdf) (fetched but not machine-readable this session; listed as an unread lead)
- [Legislative Drafting Manual — Senate Office of the Legislative Counsel](https://law.yale.edu/sites/default/files/documents/pdf/Faculty/SenateOfficeoftheLegislativeCounsel_LegislativeDraftingManual(1997).pdf)
