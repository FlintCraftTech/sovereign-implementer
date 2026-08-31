# Borrowing from legal drafting: packing rules tightly, and amending instead of adding

Researched 2026-08-09, alongside `instruction-file-bloat-and-subtraction.md`. The user's
framing: the method has a habit of writing a rule, then writing its exceptions as massive
explanations, when they should be subclauses. And the structural half — a change should
land as an augmentation of an existing related rule, not as yet another rule. That second
point is the one that matters most, because the binding limit is a count of instructions.

## 1. The structural principle: amendment versus freestanding

Legislative drafting has an exact name for the distinction this project needs. When a bill
becomes law it either **amends or repeals** earlier statutes, or it creates a new
**"freestanding"** law — defined as "a provision of an act that is not an amendment to or
repeal of existing law."

That is the choice the method makes every time it adds a rule, and it has been silently
choosing freestanding every time. Mapped onto the instruction-count ceiling: a freestanding
rule consumes a slot out of the ~150–200 a model follows reliably. An amendment to an
existing rule consumes none — it changes a rule already occupying its slot.

So the drafting question at every addition is: **which existing rule is this a modification
of?** A change that cannot name one is either genuinely new territory, or — far more often —
a refinement whose parent has not been looked for.

## 2. Three named consolidation techniques, in increasing strength

- **Codification** — a statute that "states exhaustively the whole of the law upon a
  particular subject," gathering the scattered provisions on that subject into one place.
  Applied here: one subject, one rule, stated once. It forbids the same concern appearing in
  five documents, which is the shape the method's rules currently take.
- **Consolidation** — combining all existing statutes on a topic into one and **repealing the
  priors**, explicitly *without* changing the law. The repeal is the essential half: a
  consolidation that doesn't repeal what it absorbs has doubled the text rather than merged
  it. This is precisely the failure mode when a method rule is "restated more clearly" in a
  new place and the old statement is left standing.
- **Recasting (EU law)** — the strongest, and the closest match to what this project needs.
  Defined as "a process used to update legislation whereby previous legislation on a topic is
  repealed and replaced by a single new act incorporating both the original legislation and
  any previous amendments to it," while also "making substantive changes to the text." It
  differs from codification, which reorganises without substantive change, and from ordinary
  amendment, which "patches the old" act rather than replacing it.

**Recasting is the eviction mechanism the project has no version of.** When a rule has
accumulated enough amendments that the accretion is the problem, the move is not another
clause: it is to re-enact the whole rule as one clean text and repeal every predecessor. The
research on instruction bloat found nothing about removing existing instructions — this is
the borrowed answer.

## 3. The rationale question — where legal drafting most sharply contradicts current practice

This is the finding with the largest consequence, and it was not what was being looked for.

**Legislation does not put its reasoning in the operative text.** The binding rule is stated
bare. The *why* lives in a separate, non-operative place — recitals, preambles, explanatory
memoranda — which aid interpretation but are not the law. The operative provision carries
the obligation; the explanatory document carries the reasoning.

The method does the opposite, deliberately. The why-pipeline requires rationale to travel
inline with each rule, on the grounds (from the 4.8 research) that a rule is followed more
reliably when its reason travels with it. That belief is load-bearing and it is why almost
every rule in plugin-behaviour.md carries a paragraph of justification.

**Both cannot be fully true, and the tension should be resolved deliberately rather than
drifted through.** Points worth weighing:
- The 4.8 finding was measured on a model now frozen as the fallback. The active docset
  serves the 5-series, whose published guidance asks for *less* prescription and warns
  against over-explaining to more capable models.
- The project already owns the exact vehicle legal drafting uses: the LOG is a non-operative
  record of reasoning, retrievable on demand. A rule's why does not have to be deleted to be
  moved out of the always-loaded text.
- The counter-case is real and must not be waved away: a rule whose reason is absent can be
  misapplied at its edges, and the method has repeatedly observed rules slipping when their
  why was stripped — the docset-B subtraction audit found exactly that (rules that had been
  *stated inside* their why-clauses were lost with them).

A middle position exists and is probably where this lands: the *operative* statement stays
bare and precise; the reasoning moves to the LOG entry that decided it; and the rare rule
whose reason is genuinely necessary to apply it correctly keeps one short clause, by
exception rather than by default. That inverts the current default without denying the
finding behind it.

## 4. Style: how legal drafting packs conditions and exceptions

The techniques, all of which replace a paragraph of explanation with a structural device:

- **Avoid provisos.** Manuals widely instruct drafters to avoid subclauses beginning
  "provided that" — split the sentence instead. The proviso is the exact shape the user
  described: a rule, then a swelling qualification appended to it.
- **Signal the exception before the general rule.** Limitations, exceptions, and conditions
  on a provision's application are described *first*, so the reader never applies the rule
  and then discovers it didn't apply. One state manual puts conditions "in the first part of
  the legislative measure."
- **"Subject to \<X\>"** is the tight-packing device: it signals that an exception exists and
  points to where it lives, without restating it. A cross-reference costs a few words; a
  restatement costs a paragraph and creates a second copy that can drift.
- **Multiple exceptions go in their own subsection**, referred to from the general rule
  rather than crammed into it.
- **Simple exceptions use short connectives** — "but", "except that", "if", "unless", "so
  long as". A connective, not an explanation.
- **One idea per sentence or provision.**
- **Don't mix conditions and exceptions in one sentence** — don't put "if" and "unless"
  clauses together.
- **Main clause first when the conditions are long**, so the reader knows what is being
  qualified before working through the qualifications.
- **Don't hide exceptions.** Multiple and complex exceptions make a rule easy to misread, so
  clarity of the exception is not in tension with brevity — both are served by structure over
  prose.

## 5. What this implies for `self-authoring-rules.md`

Recorded as analysis, not decision.

The admission gate already agreed gains a question that precedes all the others: **which
existing rule does this amend?** Freestanding status becomes something a rule has to earn,
not the default it currently is.

The eviction half gains two named mechanisms rather than a general exhortation:
*consolidation* (merge and repeal the priors) and *recasting* (re-enact one clean text when
amendments have accreted past legibility).

The wording check — "action, not prohibition", the sole survivor of the old seven — gains the
drafting devices above, which are all forms of one instruction: **express a qualification as
structure, not as explanation.**

And the rationale question in §3 is a genuine fork that the design pass has to decide
explicitly, because it determines whether rules stay at their current per-rule weight or drop
substantially.

## Sources

- [Understanding Federal Legislation: A Section-by-Section Guide — Congressional Research Service](https://www.congress.gov/crs-product/R46484)
- [Recasting (EU law)](https://en.wikipedia.org/wiki/Recasting_(EU_law))
- [Amending, Consolidating and Codifying Statutes](https://lawnotes.wordpress.com/2015/05/15/amending-consolidationg-and-codifying-statute/)
- [State Legislative Drafting Manuals and Statutory Interpretation — Yale Law Journal](https://yalelawjournal.org/note/state-legislative-drafting-manuals-and-statutory-interpretation)
- [The SARAL Manual: a plain language drafting manual for better laws — Vidhi Centre for Legal Policy](https://vidhilegalpolicy.in/wp-content/uploads/2023/03/230301_The-SARAL-Manual_v3.pdf) (not machine-readable in this session; cited from search summaries, not read directly)
- [Federal Plain Language Guidelines](https://wid.org/wp-content/uploads/2022/03/FederalPLGuidelines.pdf)
- [Legislative Drafting Guide — Tennessee Office of Legal Services](https://www.capitol.tn.gov/Archives/joint/staff/legal/Drafting%20Guide%202025.pdf)
