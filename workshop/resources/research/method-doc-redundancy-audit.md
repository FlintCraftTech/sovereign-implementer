# Redundancy audit — skill docs vs. skill-nonspecific-rules.md

Audit date: 2026-08-14
Files: `skill-nonspecific-rules.md` (always loaded, "B"), `setup.md`, `plan.md`,
`next.md`, `done.md`.

## What counts as a finding

A finding is a passage in a skill doc that **restates the substance** of a rule
already in the always-loaded doc, such that a reader who had loaded both would
get the rule twice.

Not findings:
- A bare pointer ("the full rule is in skill-nonspecific-rules.md, §X") — that is
  the intended pattern and it appears correctly in several places.
- A **site-specific application** of a general rule (e.g. /next's light capability
  check vs. /plan's thorough one) — these narrow the rule rather than repeat it.

Marked **[cite+restate]** where the doc both points at the canonical rule *and*
reproduces it. These are the cheapest fixes: the pointer already works, so the
restated body can be deleted with no loss.

---

## Summary table

| # | Skill doc | Lines | Duplicates | Severity |
|---|---|---|---|---|
| 1 | plan.md | 112–118 | Provenance / user-credit, all four clauses | High |
| 2 | plan.md | 119–133 | Flavor marker table + over-tag guard | High |
| 3 | plan.md | 135–145 | `[freeform]` definition | Medium |
| 4 | plan.md | 165–166 | Filing vs. processing boundary | Low |
| 5 | plan.md | 167–170, 942–948 | Red-flag clearing states — twice in one doc | High |
| 6 | plan.md | 25–29 | Write-first rule [cite+restate] | Medium |
| 7 | plan.md | 808–814, 816–827, 917–929 | Capability check / matched pair — three times | High |
| 8 | plan.md | 20 | "never build" / plan-next boundary | Low |
| 9 | next.md | 22–29 | Flavor marker table | High |
| 10 | next.md | 265–267 | Definition of build scope | Medium |
| 11 | next.md | 300–306 | Two-limb buildability test (owned by plan.md) | Medium |
| 12 | done.md | 170–175 | Rationale provenance [cite+restate] | Medium |
| 13 | done.md | 233–238 | Index-line length cap [cite+restate] | Low |
| 14 | done.md | 303–317, 319–332 | Red-flag clearing states | High |
| 15 | done.md | 288–295 | `[user]` item vs. Claude-runnable check | Low |
| 16 | setup.md | 20–26 | Plain-language rule — conditional, see §S | — |
| 17 | setup.md | 384–385 | `[SEQUENCE]` one-per-message — conditional | — |

Plus three **inverse findings** (§I): rules duplicated across skill docs that are
*absent* from the always-loaded doc, and one that is present but under-scoped.

---

## plan.md

### 1. Provenance and user-credit — lines 112–118 · High

```
- **A work item carries a user-credit only when the user raised it.** Provenance is
  asymmetric and default-AI; the credit stays on the item after processing...
```

Reproduces all four clauses of skill-nonspecific-rules.md **Captures ->
Provenance is asymmetric and default-AI** (lines 443–458): default-AI, the
own-words bar, mixed authorship written as mixed, and the same bar binding
reason-shaped sentences. The only non-duplicated content is the half-clause
"the credit stays on the item after processing," which is a genuine /plan
addition.

**Fix:** reduce to that one clause plus a pointer.

### 2. "Who does the work, and how" — lines 119–133 · High

The fenced block reproduces two separate always-loaded blocks:
- the **Flavor marker** table (nonspecific 463–470) — `(no tag)` / `[audit]` /
  `[user]` / `[freeform]`;
- the **over-tag guard** (nonspecific 479–485), including the blocked-on-a-push
  carve-out and the below-the-line placement, near-verbatim.

New content: only "must carry a DESCRIBED walkthrough, settled at the keep-step."

**Fix:** keep the walkthrough line; delete the rest of the block.

### 3. `[freeform]` definition — lines 135–145 · Medium

The first two sentences reproduce nonspecific 505–509, including the identical
example list ("the queue mover, the scope-lock, the lint") and the identical
reasoning ("running the broken mechanism to build past it is the failure").

Genuinely /plan-specific and worth keeping: the placement rule (one end of the
cleared region, which end and why) and the `Blocked by:` fallback.

### 4. Filing vs. processing — lines 165–166 · Low

"Filing is any session; processing is /plan's" duplicates nonspecific 795–799,
which states the same boundary with more detail (including the test-judging
consequence).

### 5. Red-flag clearing — lines 167–170 **and** 942–948 · High

Both passages restate the nonspecific **States and lifecycle** block (641–655):
cleared by designing out or by informed consent, LOG records which, an
unclearable flag returns to the bottom of Unprocessed.

This is stated **three times in the corpus** — once canonically, twice in
plan.md — and a fourth and fifth time in done.md (§14). The two plan.md copies
also duplicate *each other*, roughly 400 lines apart.

**Fix:** keep at most one, at the keep-step (942–948), reduced to a pointer plus
the marker's literal syntax.

### 6. Write-first — lines 25–29 · Medium · [cite+restate]

Four lines restating write-then-report, followed by a correct pointer to the
canonical rule. The pointer alone would do; the restatement adds a risk of drift
because the canonical version carries the recoverability test and this one
doesn't.

### 7. Capability check — lines 808–814, 816–827, 917–929 · High

Three passages in the same sub-step, all restating the same material:

- **808–814** restates the matched pair (over-tag + don't-under-file) from
  nonspecific 479–503.
- **816–827** states the thorough check and its "what would answer this?" reframe.
- **917–929** states the thorough check and its reframe *again*, with a second
  anecdote, and cites nonspecific.

/plan being the thorough site is correct and belongs here — but it is currently
established three times within about a hundred lines. This is the densest
redundancy in the corpus.

**Fix:** merge into one passage. Recommend keeping 816–827 (it carries the
sharpest anecdote and the "don't enumerate everything" bound) and folding the
best sentence of 917–929 into it.

### 8. "never build" — line 20 · Low

Duplicates nonspecific 783, "/plan is for planning, /next is for building. Don't
cross them." Low severity — an opening ground rule restating the boundary is
arguably load-bearing framing rather than redundancy.

---

## next.md

### 9. Flavor table — lines 22–29 · High

`flavor(item):` reproduces the nonspecific Flavor marker table (463–470) with the
routing targets substituted in. The routing targets (`next-build.md`,
`next-audit.md`) are the only new information.

Note this table now exists in **three** places: nonspecific 463–470, plan.md
121–133, next.md 22–29 — plus a prose paraphrase in setup.md's QUEUE.md scaffold
(270–273), which is user-facing template text and defensible.

**Fix:** reduce to the routing map alone.

### 10. Build scope definition — lines 265–267 · Medium

"Build scope is the active work's described work — the changes the work items
call for, and nothing past them, enforced by judgment" reproduces nonspecific
752–754 word-for-word in substance.

This one is odd, because nonspecific's Scope section explicitly delegates the
mechanical half to next.md ("Its mechanical approximation, and how /next derives
it, is in next.md"). The delegation is correct; next.md just restates the half it
was *not* delegated first.

**Fix:** open at "The `Files:` list below is its mechanical approximation."

### 11. Two-limb buildability test — lines 300–306 · Medium

Duplicates plan.md 708–719 — including the identical illustrative string
`"Files (rough): skill-nonspecific-rules.md, plan.md"` and the identical
conclusion that a files-only test passes undesigned work.

Not a duplicate of the always-loaded doc (the test isn't there), so this is a
**skill-to-skill** duplication. next.md already names /plan's keep-step as the
owning site, so the pointer exists — the restatement doesn't need to.

---

## done.md

### 12. Rationale provenance — lines 170–175 · Medium · [cite+restate]

Inside the entry template, the bracketed note restates the credit-requires-their-
words bar and mixed-authorship rule, then cites nonspecific. Same shape as
finding 6: the pointer is doing the work; the restated body is the redundancy.

Note this makes provenance the corpus's **second most-repeated rule**: nonspecific
443–458, plan.md 112–118, done.md 170–175.

### 13. Index-line length — lines 233–238 · Low · [cite+restate]

"There is no length cap on the line — the bound is what it must carry" restates
nonspecific 737–748, then correctly points there. The 20%-cap repeal history and
the "do not restore it" instruction are done-specific and worth keeping.

### 14. Red-flag clearing — lines 303–317 and 319–332 · High

**303–317** restates the two clearing paths and the informed-consent trail from
nonspecific 641–651. **319–332** then restates the backstop from nonspecific
659–661.

Combined with §5, the red-flag clearing model is written out **five times** across
the corpus. The genuinely done-specific content is small: that the how-it-cleared
record goes in the LOG entry, that recording is unconditional, and that the close
does not re-decide.

**Fix:** collapse 303–332 into one short section carrying only those three facts.

### 15. User-runnable checks — lines 288–295 · Low

```
a verification only the user can run  ->  a [user] work item
a check Claude can run                ->  just part of building
```

This is the over-tag guard's test ("can Claude do this at all?") restated as a
two-row table. Low severity — it reads as the answer to a specific question
(what happened to the deferred-tests section) rather than as a rule statement.

---

## §S — setup.md: conditional findings

setup.md's front matter and Step-0 guard both assert that the always-loaded rules
are not available, and on that basis restate two of them in prose:

- **20–26**, the plain-language guard — duplicating nonspecific 55 and the
  Vocabulary section (229–255);
- **384–385**, "Ask one question per message and stop after each" — duplicating
  `[SEQUENCE]` (nonspecific 289–292) and the message-shape rule (64–71).

**These are correct for Case A and Case B and redundant for Case C.** The
always-loaded doc says at lines 19–22 that its rules *are* active for /setup's
migration and top-up runs, which are exactly Case C / Step 2C. So a Step 2C run
loads both copies.

This is a **specification conflict, not just redundancy** — the two docs disagree
about when setup.md's rules are loaded. Worth resolving before deciding whether
these two passages are duplicates at all.

Also conditional: **425–431** (first work item, "captured by you" credit) touches
the provenance rule, same caveat.

---

## §I — Inverse findings

Rules repeated across skill docs that are **not** in the always-loaded doc. These
are the mirror image of the audit's question, and each is a candidate for
promotion under the all-four-skills admission test.

### I1. The one-narration bundling rule — fires in 3 skills, promoted in 0

Near-verbatim in three places:

| Doc | Lines |
|---|---|
| plan.md | 280–291 |
| next.md | 59–66 |
| done.md | 103–114 |

All three carry the same two sentences: *"Each check being individually bounded
does not bound the sum"* and *"Anything the user must act on leaves the bundle...
The consolidation is for what the [session/run/close] is telling them, never for
what it is asking them."*

Fails the strict all-four test (setup.md has no equivalent multi-check moment),
which is presumably why it wasn't promoted. But three near-identical copies is a
worse outcome than one slightly over-scoped rule. **Recommend promoting it** and
noting the /setup exception inline.

### I2. "Never ask whether a `[user]` item is done" — 5 statements, 0 canonical

plan.md 328–332; next.md 147–151, 456–460, 469, 525–529; done.md 56–60.

next.md alone states it four times. The rule is absolute ("not at /next, not at
/plan, not at /done") — which is precisely the shape that belongs in the
always-loaded doc, since it fires in three skills and its whole content is that
it has no exceptions.

### I3. `Runs alone` — defined twice, canonical nowhere

plan.md 147–163 (authoring site) and next.md 34–51 (consumption site). Both
carry the full "binds /next and nothing else" caveat and the not-`[freeform]`
distinction. The always-loaded Captures section documents every other marker
(`Blocked by:`, `Red flag · State:`, the flavor tags) but not this one, so the
line format block at nonspecific 428–434 is incomplete.

---

## Recommended order of work

1. **Red flags** (§5, §14) — five copies, one canonical. Highest ratio.
2. **Capability check in plan.md** (§7) — three copies within one sub-step.
3. **Provenance** (§1, §12) — three copies, two of them [cite+restate] and so
   trivially deletable.
4. **Flavor table** (§2, §9) — three copies.
5. **Resolve the setup.md loading conflict** (§S) before touching setup.md.
6. **Promote I1 and I2**; add `Runs alone` to the nonspecific line-format block
   (I3).

## Honest limits of this audit

- Substance-level judgment, not string matching. A restatement that reworded
  everything and shares no vocabulary with its source could have been missed.
- The four sub-docs the corpus references — `next-build.md`, `next-audit.md`,
  `done-build.md`, `done-audit.md`, `done-plan.md` — were not supplied. done.md
  and next.md delegate substantial material to them, so there is likely more
  duplication at those boundaries than this report can see. `done-plan.md`'s
  hold-back-unverified-work rule in particular is referenced from three places.
- Findings marked Low are judgment calls; a reasonable reading treats several of
  them as useful framing rather than redundancy.
