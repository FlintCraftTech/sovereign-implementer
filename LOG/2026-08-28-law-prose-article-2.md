# [user] Write the law-prose article for the site [law-prose-article]

Walk-through started 2026-08-28 in a /next run, appended as it goes. The planning record for this item is `2026-08-28-law-prose-article.md`; this is the drive.

## Step 1 — the article's claims, read out of the record

Source records read: `2026-08-17-law-prose-restyle.md`, `2026-08-18-restyle-continues-and-the-audit-is-re-held.md`, the four 2026-08-21 restyle and re-count entries, `2026-08-10-prohibition-and-subordination-audit.md`, `2026-08-11-prohibitions-rewritten-as-actions.md`, `2026-08-22-post-restyle-compliance-audit-2.md`, and `2026-08-27-announcement-rationale-split-correction.md` for the guardrail.

### The narrative claims

1. **The arc, which is the user's and opens the piece.** Massive prose rule sets written with no system; then pseudocode; then law prose.
2. **The rulebook grew from 6,162 words to 21,445 in a week, and every single addition passed the gate honestly.** There was no eviction policy, so each rule looked free. The file got worse the whole time.
3. **A week of work was rolled back — 65 commits — to the day that file was born.**
4. **Pseudocode died on three findings, and the worst is the one worth the space: the format made a rule wrong.** A standing instruction applying everywhere became a comment inside one branch, so a rule governing everything now looked like it governed one case. A pure reformatting pass silently shrank a rule's reach.
5. **Law has spent centuries on the same problem.** Four borrowings carry the piece: recasting (repeal and re-enact rather than layer clarifications), amendment-versus-freestanding (a new rule names the rule it amends, and an amendment costs no slot), subordination (a complete sentence in a nested bullet is a freestanding rule wearing a bullet), and bare rules with the reasoning published separately.
6. **The why-clause result, which is the measured one.** The older model genuinely needed a reason attached to each rule; the 5-series does not. The light docset was authored purely by deleting them: 255,885 → 156,964 bytes, a 39% cut. The per-document breakdown is close to a controlled result — the reduction tracks how much rationale a document carried, not how long it was. Two rule-dense docs fell 56% and 41%; two near-pure routing docs fell 4% and 11%.
7. **The reclassification move**, which is the subtlest thing here and the part a reader building their own rules can use: the exception permitting "a short why clause where the reason helps" was repealed outright, because an exception phrased as a judgment is decided by whoever is authoring, every one of whom believes their own rule is the edge case. What replaced it is a purpose clause welded into the operative sentence — so the reason cannot be stripped without leaving the rule visibly unfinished.

### The honest limits, and they travel with the claims rather than in a footnote

8. **"The 5-series doesn't need the why-clauses" is not measured.** The 39% is. The claim about why it worked is the vendor's guidance plus a reading of the result — the same weakness the piece criticises in the pseudocode evidence, so it gets the same treatment.
9. **The pseudocode evidence is thinner than it looks, and the gap is in the field rather than in the reading.** The impressive numbers come from a 2023 study measuring task accuracy, on models including a code-specialised one. Standing behavioural rules are a different question, and nobody appears to have tested it.
10. **The restyle found its targets by grep, and that is its coverage limit.** It searched for sentence-leading prohibitions, so mid-sentence ones went unread until a later pass went looking.
11. **Every estimate of how many prohibitions remained was wrong, and each was corrected by re-counting rather than trusted.** The queue item's own "~151" was re-taken at **310** occurrences across all fourteen docs. A separate claim of "~150" in one file was re-counted at **68**, of which 45 were restyled and 23 left standing as protected kinds. **The article must not repeat the ~151 figure — it is superseded, and it currently sits in this item's own text.**
12. **The acceptance test's arithmetic ran backwards.** Rule counts *rose* in three files after a pass that removed prohibitions, because bulleting prose makes text the counter could not previously see countable. The measure was measuring the wrong thing.
13. **A file read and correctly left alone is byte-for-byte identical to one never opened.** That is why the pass had to emit a per-occurrence coverage list as its evidence — one line per occurrence, with file, line and a one-word verdict.

### The guardrail, from the recorded failure

### Step 1 shown as a card, and the walk-through paused there

The claims list was published as an artifact on the user's request — she was on remote control and wanted it readable on the device. Laid out as a statute, claims numbered so they can be answered by number, with two marginal flags: claim 11 marked keep-out (the superseded ~151 figure), claim 12 marked for the centre (the backwards arithmetic).

**Paused at step 1 on the user's own direction.** She proposed processing each claim the way /plan processes a capture, rather than approving the set by number, and raised that this may point at a co-writing work flavour. Filed as [co-writing-flavour] rather than acted on — a flavour needs the rule gate and three docs wired, which is planning work, not a mid-walk-through change.

**Drafting has NOT started.** Step 1's verdict is outstanding: no claim has been cut, added or reweighted, and the article's shape is unsettled while the processing question is open.

**An outbound message about the co-writing idea is held on her instruction** so it does not muddy a test running in a parallel session. Nothing drafted, nothing sent. She will say when the test is done.

## Dispositions — the claims processed one at a time, on the user's direction

**Claim 1 — the three-attempts arc. IN, opens the piece, kept short.**

Two corrections from the user during this turn, both changing what the claim contains:

- **The fifteen-year interest is not Throughliner's and does not belong in this article.** It is Simply Sew, and it is the ADHD article's material. Claude had folded it into this claim's framing; the user corrected it.
- **Throughliner is about four months old, and the repository's first commit (2026-06-01) is not the start.** The user's account, given here and not previously on record anywhere: the method was originally developed **inside Cowork, because she was too scared to use Claude Code**, for roughly a month before the Claude Code repository begins. That reconciles her four months with the repo's just-under-three.

**The corrected arc is the stronger one, and it is the recommendation the user agreed:** three rule-writing approaches tried and two abandoned — prose with no system, pseudocode, law prose — with the rulebook trebling to 21,445 words and a 65-commit rollback, all inside the project's first four months. The timespan is the hook rather than an aside.

**Corrected by the user in the following turn — she REVIEWS rather than authors.** Claude had recorded claim 1 as a passage she would write herself. Her correction: she is happy to review it, but the draft has to reach her **as a `.txt` file, linked, so she can edit it in a Claude Code sidebar**. So the co-writing mechanism here is not two authors taking turns at the keyboard — it is Claude drafting and the user editing the file directly, which is a different shape and a cheaper one. Recorded because [co-writing-flavour] turns on exactly this distinction, and the first version of this paragraph got it wrong.

**One conflict to resolve before a draft is handed over this way.** `CLAUDE.md`'s Discord draft-edit flow records the opposite finding, tested: the side panel opens `.md` read-only and `.txt` not at all, which is why that flow opens drafts in Notepad instead. Either the app's behaviour has changed, or "sidebar" here means the Notepad route. Not resolved in this session; whoever hands over the first draft checks it rather than assuming, per the capability-claim rule.

**Where the origin fact lives.** The Cowork month exists nowhere else in this project's records. It is written here, as part of this claim, and a session wanting it later will find it under this item.

**Claim 2 — the growth. IN as the SYMPTOM only, and SPLIT on the user's caveat.**

She rejected the single-cause framing: *"the law prose is not the one saving Grace."* Agreed and recorded as two claims.

**2 keeps the symptom** — 6,162 to 21,445 words in a week, and every addition individually justified. The "nobody was careless" line is load-bearing rather than a concession: a gate working as designed still produced a file three times too long, because nothing was ever removed.

**2b is new and carries the causes, of which there are at least four:**

1. no eviction policy, so nothing ever came out;
2. a forgotten always-loaded layer silently pushing why-clauses and oversized specimens — and possibly worked examples of laws going wrong — all of it styled for Opus 4.8 and unnecessary for the 5-series;
3. **the arrival of the 5-series itself, which the user named as a saving grace in its own right** — it is what made radical simplification possible at all;
4. law prose, which is the article's subject but is one of four rather than the cause.

**A precision point that must be settled before publishing, and it is the article's own standard applied to itself.** The user recalled cause 2 as stale *self-authoring rules* loaded at session start. The record points at something adjacent but distinct: the self-authoring gate was loaded by **nothing at all**, which was its own defect (`LOG/2026-08-10-plan.md`). The layer that genuinely was always-loaded, that she had never heard of, that sat outside both the admission gate and the growth report, and that was written for 4.8, was the **shipped output style** — found 2026-08-13 (`LOG/2026-08-13-plan-brevity-and-the-checks-that-did-not-fire.md`) and deleted 2026-08-14. Her description matches it in every respect except the name.

**So the claim is written around the mechanism — a forgotten always-loaded layer, invisible to the very checks meant to catch growth — and the artifact is named only once confirmed.** A wrong claim about the project's own history is the same failure the item already guards against for third parties.

**Claim 3 — the rollback. IN, folded into claim 2 as its closing beat rather than standing alone.**

65 commits reverted to the day the rulebook was born. Standing alone it reads as drama; at the end of the symptom claim it is what makes the numbers land — not merely a long file, but a week of real work thrown away to escape it.

**One addition from the record the claim did not carry: the rollback was recoverable, and the good parts were deliberately pulled back out afterwards.** Without that the reader concludes a week vanished. With it the point sharpens: the work was not lost, the *file* was unsalvageable — which is a harder indictment of letting a rule corpus grow unchecked than the loss would have been.

**Claim 4 — the format made a rule wrong. IN, and given the most space of any claim.**

The reason it earns that space: it is the only claim in the article where the failure is **demonstrable rather than argued**. Show the rule before, show it after, and the reader watches its reach shrink without a word of it changing. Everything else here is measurement or reasoning; this is evidence a sceptic can check.

It also does work claim 9 cannot. Claim 9 reports an absence — nobody has tested this — and an absence persuades nobody who already believes. Claim 4 is a present, positive harm from the same format. The two together are the case; claim 4 alone is what lands.

**The drafting risk, named so the draft avoids it: inventing an illustrative example because the real one needs setup.** The real rule — *never pick up work from below the ready line* — takes two sentences of context before the failure is visible. Spend them; do not substitute a cleaner fiction.

**Claim 5 — the legal borrowings. IN, restructured from four peers into two load-bearing techniques and two consequences.**

Four techniques given equal weight reads as a listicle, and the list was the most generic-looking part of the piece. Ranked by what each actually did here:

- **Amendment over freestanding** is the one that changed the most, and it is the direct answer to claim 2's "every addition was individually justified" — it is what makes a further addition cost nothing.
- **Recasting** is the answer to the file already standing at 21,445 words.
- **Subordination** and **bare rules** are refinements of those two, and read better as what followed than as peers.

That structure gives the section a spine matching the article's own argument: two techniques answering the two failures already described, then their consequences.

**The caveat travels with the claim, and the record already states it:** these are borrowings from a discipline that solved a *related* problem, not a proven transfer. If the legal borrowings turn out to be wrong too, the article says so.

**Claim 6 — the why-clause cut. IN, as the article's evidentiary centre.**

255,885 → 156,964 bytes, a 39% cut, authored purely by deletion. The per-document breakdown is what makes it more than a before-and-after: the reduction tracks how much *rationale* a document carried rather than how long it was, so where there was nothing to subtract, nothing came out. That is close to a controlled result, and it is the one place the piece can point at a number and show the mechanism in the shape of it.

Two changes from how the claim was first written:

- **It links back to 2b.** The forgotten always-loaded layer was pushing why-clauses *in* while this pass was cutting them *out* — the same substance moving in opposite directions through two mechanisms. A reader who has just met 2b expects that connection, and without it the 39% reads as a tidy-up rather than the cleanup of a named inflation.
- **The four percentages are paired as claim and control, not listed.** The two rule-dense figures (56% and 41%) go in the sentence; the two routing figures (4% and 11%) follow immediately as the control. Four numbers in a row get skimmed.

**Claim 7 — the repealed exception. PRESENTED, not settled. Deferred with the rest.**

The recommendation on the table when the session stopped, recorded so the next one does not re-derive it: **in, promoted out of last place** to sit beside claim 5's amendment-over-freestanding — it is the same move applied to the gate itself, since the gate had an exception and the exception was the leak. And **made the spine of the giveaway**: a platform-agnostic prompt is precisely a set of rules someone else's model applies with nobody there to interpret them, so "can this rule be applied correctly without this sentence?" is the part that travels furthest.

The argument for promoting it: every other claim describes something that went wrong and was fixed. This one describes a *class* of failure — a rule whose enforcement depends on the judgment of the person it constrains. It is the only claim that survives being lifted out of the article entirely, which is a fair test of where the value sits.

## Outcome — DEFERRED, on the user's own word

The user asked to defer and finish the session: *"cen we please defer this and finish the session? I can't concentrate"*. Recorded as **deferred** rather than not-reached, because she said so.

**Where the processing stopped, for the session that picks it up:**

```
claims 1, 2, 2b, 3, 4, 5, 6   settled — dispositions above
claim 7                        presented, recommendation recorded, not answered
claims 8 – 14                  not reached, present them fresh
```

**Nothing was drafted.** Step 1 of the walkthrough is six-sevenths done; steps 2 onward have not started. The item stays in the queue.

**Two things the next session must carry forward**, both settled here and easy to lose: the article now has **fifteen** claims rather than fourteen, since claim 2 split; and the claims card at
https://claude.ai/code/artifact/204181de-8ab8-4bdf-beaf-549bdb6af055
still shows the original fourteen, so it is behind this record and should be republished before it is used again.

## The claims (continued)

14. **The story is how models follow rules — never internal reorganisation dressed as user benefit.** The one attempt to announce this subject to users was rejected on five separate visibility grounds and dropped entirely on the user's direction ("I say drop it"). An article is the right home precisely because it is not asking a user to care about where a rule now lives.
