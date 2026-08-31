# Pronoun use, working memory, and how much to name things explicitly

Run 2026-08-09, in a /plan session, after a live failure: Claude switched what
"it" pointed at mid-paragraph, the user could not follow the argument, and
Claude's repair was to strip pronouns out of the passage almost entirely. The
user reported the repair as **condescending**. The question for research: how do
you write for limited working memory by using pronouns *less*, without switching
them off?

The headline finding reverses the intuition behind the repair, so it is stated
first.

## 1. Removing pronouns makes comprehension WORSE, not better — this is measured

The **repeated-name penalty** is a robust, decades-old psycholinguistic result.
Sentences that repeat a name are read **more slowly** than the same sentences
using a pronoun, when the referent is the current topic (the subject of the
preceding sentence). The effect appears in reading times and in ERP measures
(an N400 response to the repeated name).

**Almor's Informational Load Hypothesis** (1999) explains why. Anaphors — the
words that point back at something already mentioned — sit on a continuum from
least to most informationally loaded: a pronoun at one end, a full repeated name
at the other. The cost of an anaphor has to be *functionally justified*. When the
referent is already the focus of attention, a full name supplies information the
reader did not need, and the reader pays for it. Across five self-paced reading
experiments, anaphors were read faster when their cost was better justified.

The corollary matters as much as the finding: the penalty **disappears** when the
referent was *not* the previous sentence's subject. So a full name is the right
choice exactly when the referent is no longer the thing in focus — and the wrong
choice when it still is.

**What this establishes for the method.** "Use fewer pronouns" is not a safe
general instruction, and a pronoun-free rewrite is not a neutral clarification.
It imposes a measurable cost on the reader at every point where the pronoun was
doing its job, which is most of them. It also reads as talking down, which is the
user's own report and is consistent with the mechanism: being told information
you already hold is the felt experience of an unjustified informational load.

## 2. The real defect is referent-switching, not pronoun density

Style and technical-writing guidance converges on one rule: **a pronoun should
have exactly one possible antecedent** in its context. Ambiguity arises in two
ways — two candidate nouns competing for one pronoun, or the same pronoun
pointing at different things in consecutive sentences.

The second is what happened live. In one passage, three uses of "it" referred to
the bullet, the bullet, and then the bullet's *content*, with nothing marking the
change. Guidance for this case is specific and modest: **replace the pronoun with
the specific noun at the point where the referent changes** — not everywhere.

This is the reconciliation of the two findings. Finding 1 says pronouns are
cheaper when the referent is stable. Finding 2 says naming is required when the
referent moves. They do not conflict; they partition. The expensive thing is
*silently* moving the referent, which forces re-reading — the one operation
limited working memory cannot absorb.

## 3. Working-memory guidance: one to three items, held at once

W3C's **COGA** guidance (*Making Content Usable for People with Cognitive and
Learning Disabilities*) records that people with impaired working memory may hold
only **one to three items** in memory simultaneously. Its plain-language
recommendations are short sentences, active voice, no unexplained jargon, no
implied or ambiguous information, and literal rather than metaphorical phrasing.
Plain-language standards are being folded into WCAG 3.

**Read against finding 1, the number is the useful part.** The constraint is not
"how many pronouns" but **how many live referents a passage asks the reader to
hold at once**. A paragraph tracking one thing can use pronouns freely. A
paragraph tracking three needs each of them named, because the reader has no
spare slot to resolve an ambiguity with.

That reframing also explains why the pronoun-free rewrite failed on its own
terms: it did not reduce the number of things being tracked. It only made each
mention longer.

## 4. The limits of this research, stated plainly

- The repeated-name-penalty literature measures **reading times and ERP responses
  on constructed sentences**, mostly in a laboratory. It does not measure whether
  a reader can follow a multi-paragraph technical argument, which is the case the
  method actually cares about.
- COGA's working-memory figure covers **cognitive and learning disabilities** as a
  category. It is not a measurement of any particular individual, and it is not
  about symbol search specifically.
- Nothing found measures **AI-generated chat prose** for any of this. Every
  finding here is transferred from adjacent literature, which is the same
  evidential gap that thinned the pseudocode-vs-prose case.
- Two searches for the exact intersection (pronoun policy *for* limited working
  memory in technical instructions) returned nothing directly on point. The
  synthesis in section 2 is the researcher's, drawn from two separate literatures.

## 5. What this supports writing as a rule

Stated here as the research's recommendation, not as a decision:

- Keep pronouns where the referent is the thing under discussion and has not
  moved. Removing them costs the reader and reads as condescension.
- **Name the thing again at the moment the referent changes** — that is the
  whole intervention, and it is one word or two, not a rewrite.
- Count live referents rather than pronouns. Where a passage tracks more than
  about three things at once, name them; where it tracks one, do not.
- Never repair an ambiguity by stripping pronouns from the whole passage. Repair
  the point where the reference actually moved.

## Sources

- [Almor, *Noun-phrase anaphora and focus: the informational load hypothesis* (1999)](https://www.semanticscholar.org/paper/Noun-phrase-anaphors-and-focus:-the-informational-Almor/ed66cc7fe687fd3ce3fdc01cf870de03e0abdabd)
- [*The N400 in processing repeated name and pronoun anaphors in sentences and discourse*](https://pmc.ncbi.nlm.nih.gov/articles/PMC5582981/)
- [*A review of the repeated name penalty: implications for null subject languages*](https://www.researchgate.net/publication/301204226_A_review_of_the_repeated_name_penalty_implications_for_null_subject_languages)
- [*Exploring the Repeated Name Penalty and the Overt Pronoun Penalty in Spanish*](https://pubmed.ncbi.nlm.nih.gov/29086144/)
- [W3C, *Making Content Usable for People with Cognitive and Learning Disabilities* (COGA)](https://www.w3.org/TR/coga-usable/)
- [W3C COGA Task Force techniques](https://w3c.github.io/coga/techniques/index.html)
- [*Adding Plain-Language Standards to the WCAG 3*](https://publications.ici.umn.edu/impact/38-3/adding-plain-language-standards-to-the-wcag-with-julie-rawe-and-lisa-seeman-horwitz-)
- [MLA Style Center, *On Pronouns and Their Referents*](https://style.mla.org/pronouns-and-referents/)
- [UCLA Writing Center, *Pronoun-Antecedent Agreement & Ambiguous Reference*](https://wp.ucla.edu/wp-content/uploads/2016/01/UWC_handouts_pronounantecedent.pdf)
- [*Using Pronouns Clearly & Effectively in Academic & Scientific Writing*](https://www.proof-reading-service.com/blogs/academic-publishing/using-pronouns-clearly-effectively-in-academic-scientific-writing)
