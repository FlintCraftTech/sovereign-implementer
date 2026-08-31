# Routine method-compliance audit checklist

The standing criteria for a periodic compliance audit of the method's own procedure docs — `skill-nonspecific-rules.md`, `setup.md`, `plan.md`, the `next*` family, the `done*` family, and any procedure doc added later.

**What this is for, and how it differs from the authoring gate.** The rule gate — in this project's `CLAUDE.md` — is a per-rule check run *once, at authoring time* — you run it over a rule before that rule ships. This checklist is the *corpus-wide periodic sweep*: you run it over docs that already shipped, to catch what drifted or was never checked. The un-hardened tool-use rule that slipped past for so long (the subagent-cost incident, 2026-06-24) is exactly the gap this exists to close — an authoring-time check never re-examines old rules, so without a periodic sweep, a rule authored before a standard existed never gets held to it.

It is a dev artifact. It audits the method's own docs, so it is host-only — not shipped in the plugin package, no FAQ, no SPEC entry — the same status as the gate it builds on.

**What triggers an audit — the board's AUDIT-LAG check, since 2026-08-22.** `resources/rule_signals.py` fires when rule-bearing commits exist that no compliance audit has covered — the boundary is the most recent compliance-audit LOG entry, an artifact rather than a threshold. The check files one `[audit]` capture scoped to the changed files and stays quiet while it is open. (The earlier arrangement — a person deciding by judgment after the AUDITED ceiling was repealed — meant nothing ran the sweep, for the same reason the checks themselves once had no trigger. The count-based ceiling stays repealed: the 150–200 instruction figure it derived from was re-validated against the 5-series and found roughly an order of magnitude too tight, `research/instruction-ceiling-revalidated-for-5-series.md`, and a sweep every N sessions stays rejected as a bare number with no derivation.)

**The routine form is DELTA SCOPE: audit the rule files changed since the last audit, against every lens, at parent axis.** The corpus-wide sweep is not the standing shape — one full pass exists as its own separately filed item, and after it the delta is the unit. Delta scope is what keeps each audit small enough to actually run, which the full-sweep duty never was.

Run all four lenses over each doc in scope. One read of the doc serves all four. Findings route to Captures for a later /plan to scope — an audit produces findings, not edits to the docs it reads.

## State the axis before you start, and it is the parent axis

**An audit compares a doc against its parent, never against its sibling.** Say which axis you are running on before the first read, and if it is not the parent axis, argue for the one you have chosen.

```
parent axis     done-build.md vs done.md; next-audit.md vs next.md; any
   (right)      sub-doc vs skill-nonspecific-rules.md. Finds a child restating
                what its parent already carries — genuine duplication, because
                the child is loaded WITH the parent and the reader has both.

sibling axis    done-build.md vs done-audit.md, next-build.md vs next-audit.md.
   (wrong)      Finds WORDING similarity between docs that are parallel by
                design, so near-identical phrasing is the expected state rather
                than the defect.
```

**The worked instance, which is why this is not a stylistic preference.** An audit once reported `done-build.md` and `next.md` carrying the same rule in near-identical words. True as text, wrong as a finding: `next.md` guards *presenting* a run, `done-build.md` guards *writing a size cap into the note for the next session*, and no session reads both. Two holes, two plugs, one wording. The finding was refused at processing weeks later, with both docs untouched. On the parent axis it would never have been produced, since neither doc is the other's parent.

## Every finding names where each site fires

A finding gives the moment each site is read, not only the line it sits on. One sentence per site, and it is what catches a false duplication at the audit rather than weeks later at processing — two rules that read alike but fire at moments no single session reaches are not duplicates at all.

## The instruction count — run this first

The gate's binding limit is a **count of instructions**, not a word count, so a sweep that doesn't produce a number can only produce opinions: "evict what fails admission" has no target and no stopping rule without one. Count before disposing of anything.

**Scope the count to the always-loaded corpus.** That is `skill-nonspecific-rules.md` plus, in the dev project, `CLAUDE.md`. The skill docs (`plan.md`, `next.md`, `done.md`, `setup.md` and the flavor families) are excluded: they load only when their skill runs, and the ceiling is about what competes for attention in every session. Audit them under the three lenses below; don't count them against the ceiling.

**Counting rule.** One instruction per discrete directive Claude must follow — a bolded rule statement, a bullet, or a decision block. Descriptive prose, rationale and worked examples score zero. Count per section and record the section totals, not just the sum: the sum tells you whether there is a problem, and the section totals tell you where it is.

**Report the split by audience, not just the total.** A consumer loads only `skill-nonspecific-rules.md`; the dev project loads both. Those are two different numbers against the same ceiling, and collapsing them hides which one is actually over.

### Dispositions

Every rule the inventory touches gets one:

```
keep                    admissible today, correctly placed, correctly worded
recast                  amendments have accreted past legibility; repeal the
                        whole thing and replace with one new text
consolidate-and-repeal  merge the rules on a topic into one AND delete the
                        priors — the repeal is the essential half
evict                   delete outright: fails admission, or is stale
relocate-rationale      the rule stays; its why moves out (consumer-facing why
                        to the shipped FAQ, authoring decision to its LOG entry)
```

`relocate-rationale` saves no slot and is still worth doing: the ceiling counts instructions, but per-rule weight is the other half of what makes a corpus hard to follow.

**Redistribution is a disposition the gate deliberately does not list, and it needs its own justification each time.** Moving a rule to a fetched doc removes it from the count without removing it from the method, which is how bloat gets hidden rather than cut. It is legitimate only where the rule has a trigger a session cannot miss — a word the user says, a hook that surfaces something. Record that reasoning per rule, never once for a batch.

### Two things learned running this (2026-08-09, the first inventory)

- **The eviction list is the audit's output, and it goes to Captures like every other finding.** This document used to say the list went in as build work cleared to run, and separately that eviction had to happen inside the run — both were repealed on 2026-08-12 by the user's ruling that audits always file to Captures, made when the contradiction was surfaced at /plan. The ruling also restores agreement with the shipped contract, which says an `[audit]` reports findings instead of editing files; the checklist had been contradicting the plugin.
- **The concern those clauses carried is real and is rehomed rather than dropped.** An audit whose findings are never acted on reproduces the failure it exists to fix. What answers that is the queue, not the audit: findings are ordinary work, ordered by the ladder and counted toward the throughput floor, where ignoring them is visible. Filing an eviction list and never building it is a queue problem with a queue remedy — it is not a reason to let a review pass rewrite the corpus it is reading.
- **An `[audit]` item that names a document to write into contradicts the audit contract and must be surfaced, not followed.** This checklist is named as the criteria home, which reads as a doc-write. The resolution that worked: the *findings* went to the queue, and only the *method* — this section — was written here.

## Lens 1 — self-authoring compliance

Apply the four parts of the rule gate — admission, eviction, distribution, wording — to each doc. The gate in this project's `CLAUDE.md` is the single source of truth for the tests; read them there rather than re-listing them here, so the two never drift. [`self-authoring-rules.md`](self-authoring-rules.md) carries the record behind them — the repeals, the defeated proposals, the measurements — and is worth opening when a finding turns on why a test is shaped as it is.

Read corpus-wide, the gate asks things it can't ask one rule at a time:

- **Admission, retroactively.** Which rules here would not be admitted today? A rule with no pointed-to failure, one Claude follows unprompted, one that applies to only some sessions but is always loaded.
- **Eviction debt.** Where does a rule sit alongside the earlier version it was meant to supersede? Consolidation that never repealed its priors is the signature.
- **Distribution.** Which always-loaded rules are reference material that could be fetched on demand — and, the reverse error, which fetched material is a standing behavioural rule a session would never know to look for?
- **Rationale placement.** Which operative statements still carry their why inline, and where should it go — the shipped FAQ if a consumer would want it, the deciding LOG entry if it's an authoring decision? When moving one, check the clause isn't *stating* a rule while arguing for it.
- **Consistency.** Is a rule held to its own standard across docs? Hardened in one doc but cited loosely in another is a finding even when each instance reads fine alone.

**Eviction does not happen in this run.** The sweep names what should go and why; the removal is separate work, filed to Captures like every other finding — see the dispositions note above for why the concern behind the older, opposite instruction is answered by the queue rather than by letting an audit edit.

## Lens 2 — tag placement

Each procedure step carries the response-shape tag that fits what it does (`[SILENT]` / `[BRIEF]` / `[DISCUSS]` / `[PROMPT]` / `[SEQUENCE]`, defined in skill-nonspecific-rules.md). Check each step for three failure modes:

- **Missing** — a step that produces output (or withholds it, or waits, or sequences) but carries no tag, so its output behaviour is left to chance.
- **Wrong** — a tag that fights what the step does: `[SILENT]` on a step that must ask the user, `[DISCUSS]` on pure internal bookkeeping, `[BRIEF]` on a genuine decision point that needs room.
- **Prose where a tag belongs** — a step that describes its output behaviour in a sentence ("keep this short," "don't say much here," "stop and wait") instead of carrying the tag that encodes it. The tag is the mechanism; prose substitutes are what the tags exist to replace.

## Lens 3 — narration drift

Check what the doc causes Claude to *say to the user* against the communication rules in skill-nonspecific-rules.md. Three drift patterns:

- **Background vocabulary in user-facing narration** — a structural or bookkeeping term from skill-nonspecific-rules.md's Vocabulary list (loop, Step N, gate, pre-flight, slug, "processed/unprocessed captures," "staleness sweep," "hash backfill," and the rest) leaking into text the user reads. Background terms belong in the procedure prose Claude reads, never in narration to the user.
- **Menu where a recommendation was due** — the doc steering Claude to lay out flat options ("file it, drop it, or commit now?") at a moment it actually has a preference, instead of leading with the recommendation and offering the alternatives as fallback (skill-nonspecific-rules.md Dependency ownership narration; the spectrum-not-flat-list rule).
- **Multi-finding openings that should consolidate** — a doc that fires several scans, watches, or narrations at one skill opening without consolidating them into one narration. The rule is stated per skill, in that skill's own opening step: plan.md's read-state, next.md's pre-flight, done.md's close.

**Not a target: a purpose clause.** Where a sentence is welded into a rule's operative text because the rule cannot be applied correctly without it, that sentence *is* the rule, not rationale riding it. An eviction sweep must leave it alone. The test in reverse: delete it and read what remains — a complete instruction means it was rationale, an unfinished one means it was operative.

## Lens 4 — decision history in operative text

**The detector is the delete-and-read test, run sentence by sentence over operative text.** Delete the sentence and read what remains: a complete instruction means what was deleted was rationale or history, and it belongs in the record — the deciding LOG entry, or git history — not in the rule. An unfinished instruction means the sentence was operative and stays.

This lens catches **disguised rationale**: decision history written in the syntax of a rule — a dated "reinstated by the user's decision of…", a "was tried and retired on measured grounds", an alternative's defeat narrated inside the operative statement. The SPEC output-style paragraph found and rewritten on 2026-08-22 is the founding instance: it survived every earlier audit because the earlier lenses looked for rationale *clauses* riding rules, and this was history wearing a whole paragraph's worth of rule syntax. No "because" is required for a sentence to fail this lens — history is rationale whatever conjunction it travels under.

## The doubled communication rules — what this project's own narration cannot test

**Read this before treating anything about this project's narration as evidence the method works.** Three layers assert the method's communication rules in every session here, and only one of them is the method. Where a rule is doubled, no session can tell which layer it followed — so a rule that is weak, badly worded, or missing from `skill-nonspecific-rules.md` still produces correct behaviour in this project, supplied by a layer consumers do not have. The defect then ships and this project never sees it.

**Two layers now, not three, and the change is recent.** A shipped output style — `plugin/throughliner/output-styles/concise-throughliner.md`, applied automatically at system-prompt priority — was the third until it was deleted on 2026-08-14 for asserting rules the other two already carried. Its three unique rules migrated into the method's own file. What remains: **(G)** the user's global `~/.claude/CLAUDE.md`, loaded in every session on this machine and in every project; **(M)** the method's own `plugin/throughliner/docs/skill-nonspecific-rules.md`. Only M ships as the method's steering; G is personal and reaches every project.

| Rule | G | M |
|---|---|---|
| One item per message when the next action depends on the last | yes | yes |
| State the count upfront before a multi-part exchange | yes | yes |
| Never preview later items | yes | yes |
| Alternatives the user is choosing between are shown together | yes | yes |
| Lead with the decision; don't front-load reasoning | yes | yes |
| Skip recaps of what the user can already see | yes | — |
| The single user-facing ask goes in bold, as a question, at the end | yes | yes |
| Offer a web search rather than guessing at an external fact | yes | yes |
| Plain English for a non-coder; no unexplained jargon | yes | yes |
| Gate detail behind an explicit request | — | yes |
| How often to speak while working (narration cadence) | — | yes |
| A written file's length matches what the task needs | — | yes |

**How to read it.** Eight of the twelve are asserted by both layers, so this project's behaviour on those eight is unattributable and its good behaviour on them is not evidence about M. The four single-layer rows are where this project's narration *does* test something: the three M-only rows are M working alone, and the one G-only row is carried by nothing the method ships. **The deletion of the style improved this table's diagnostic value** — three rules that were previously S-only and untested here are now M's, so they are exercised by the layer that actually ships.

**What was rejected, and why it is not reopened.** Stripping the duplicated rules out of G was refused: those instructions serve the user across every other project, and removing them to improve one project's test fidelity trades real everyday benefit for a diagnostic. Testing the communication rules in a consumer project without the global overrides is the real answer and is separate work. Making the overlap visible — this table — costs nothing and loses nothing, which is why it is what was built.

## Output

Findings to Captures, one per drifted spot — name the doc, the step or rule, the lens, **the moment each site fires**, and what drifted. No edits to the audited docs; the fixes get scoped in a later /plan that processes the findings.
