# Rule maintenance — evicting and repairing rules that already exist

Host-only. Consumers never author or maintain method rules.

**When to open this.** When the rule-lifecycle board's **MAINTAINED** signal
fires — near-duplicate rule statements detected across the always-loaded corpus
— and whenever a subtraction pass is being run for any other reason. Its sibling
is the rule gate in this project's `CLAUDE.md`, which governs a rule being
*written* — always-loaded, because that moment has no trigger to fetch on. The
record behind the gate's tests is
[`self-authoring-rules.md`](self-authoring-rules.md).

**Why the split.** The authoring gate mixed rules about *writing* a rule with
rules about *maintaining* the ones that exist, so a session opening it to author
something read maintenance procedure it had no use for, and a session running a
subtraction pass had no document of its own to open at all. Splitting by topic
would produce documents nobody knows when to open; splitting by the moment they
are used does not.

**The research is not partitioned along this split.** Both
[`legal-drafting-for-tight-rules.md`](research/legal-drafting-for-tight-rules.md)
and [`legislative-prose-syntax.md`](research/legislative-prose-syntax.md) bear on
authoring *and* on maintenance, and each procedure is designed against both. The
subordination test tells an author to write a rule as a subordinate unit where it
can be, and tells a maintenance pass which standing rules should have been
subordinate and are not — and consolidation cannot decide what may merge without
it.

## Eviction — what comes out

Adding a rule names what it replaces or supersedes. Rules mostly arrive as
refinements of existing ones, and the superseded version is what never gets
removed. Three named mechanisms:

- **Codification** — one subject, one rule, stated once. This is what the
  MAINTAINED signal detects: where the same rule is stated in two places, the
  two can be edited apart and nothing mechanical notices when they disagree.
  A cross-doc duplicate is the worse case, because a duplicate inside one file
  is at least visible to whoever edits it.
- **Consolidation** — combine the rules on a topic into one and **repeal the
  priors**. The repeal is the essential half: a clearer restatement that leaves
  the old statement standing has doubled the text, not merged it.
- **Recasting** — where amendments have accreted past legibility, repeal the
  whole thing and replace it with a single new text incorporating the original
  and all its amendments. Substantive changes are allowed in the same move.

Also apply a **staleness test**: is this still true? A confidently wrong rule is
worse than a missing one.

## Resolving a near-duplicate flag

The signal raises flags; it never decides. Two rules may legitimately say
similar things in different contexts, so a flag is read, not obeyed.

```
the same rule, stated twice        ->  codify: keep one, repeal the other,
                                       and cross-reference by name
one rule and a narrower case       ->  make the second a subordinate unit of
    of it                              the first, per the gate's §1 test
genuinely different rules that     ->  leave both; note it so the same pair is
    read alike                         not re-litigated next time
```

## When moving a why, don't take an operative statement with it

Docset B's fidelity audit found rules that had been *stated inside* their
why-clauses — an exception at the end of a sentence, a definition in a
parenthetical, a mechanism named in a subordinate clause — and lost when those
clauses went. The risk in a subtraction pass is not what a paragraph argues; it
is what a paragraph quietly defines while arguing.

The auditor's test, which is the purpose-clause protection read in reverse:
delete the sentence and read what remains. A complete instruction means what you
deleted was rationale. An unfinished one means it was operative, and it stays.

## Repeal — a rule's exit

A rule is repealed when the mechanism it governs is retired. That retirement is
recorded in [`retired-terms.md`](retired-terms.md) at the close that performs it,
which is what lets the board's **REPEALED** signal report every rule still naming
it. Leaving the references standing produces a visible signal rather than
silence — the default state does the work.

**Removing a term from the retired list is itself a decision**, not tidying: it
turns the signal off. Do it only when no live reference remains.
