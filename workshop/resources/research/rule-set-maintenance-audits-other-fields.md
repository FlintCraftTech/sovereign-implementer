# How other fields audit a layered rule set for restatement — legislative drafting, policy manuals, technical documentation

Read 2026-09-05 at a planning session, for the maintenance sweep's redesign toward restatement removal (the user's scope: no rule evicted, unnecessary restatement across documents found and reduced). One bounded web search, three queries; summaries below are this project's words.

## What the three fields do

**Legislative drafting (US federal and state drafting manuals).** Three practices transfer. First, the drafting offices discourage a *purpose statement* where the operative text already states what is required — a restatement of the rule in different words is the named defect, which is this project's Lens 4 said from the other side. Second, every cross-reference is verified to resolve: a reference to a section is checked to see that the section actually provides what the reference claims — a pointer that has drifted from its target is treated as an error class of its own. Third, *statute law revision* is a distinct activity from amendment: a periodic pass that repeals obsolete enactments and consolidates, done as its own project rather than riding each bill.

**Policy management (healthcare and compliance manuals).** A fixed hierarchy — policy, standard, procedure, work instruction — with each level supporting the one above and *not* restating it; a document that blends levels is the named failure, because it cannot be maintained and is expensive to audit. Governance assigns one accountable owner per document and a retirement step in the lifecycle. Consolidation of overlapping documents and retirement of obsolete ones is a standing maintenance task, and the recommended depth is two levels, three at most.

**Technical documentation (single source of truth, content reuse).** One authoritative location per piece of information, from which every other mention derives; the audit is an information-architecture exercise that *maps* what exists and what overlaps before anything is consolidated. Duplication is removed by making the other sites references (or transclusions) rather than copies, and review cycles with quality checklists keep it that way.

## What bears on the sweep

- All three fields separate *ownership* from *mention*: one site owns a rule, and every other site is a pointer. The audit's first product is the owner map, and a restatement is any non-owner site carrying the rule's content. This project's checklist has the principle inside Lens 8 but no owner map — `method-map.md` maps documents, not mechanisms.
- Legislative drafting adds a lens this checklist lacks: the *drifted cross-reference* — a pointer naming a section that no longer says what the pointer claims. Related to the retired-terms check (which reaches mechanisms, not section names) and to Lens 7.
- Legislative drafting's "no purpose statement beside operative text" is a restatement class: prose beside a typed block or specimen saying what the block already shows.
- Policy management's "a document that blends levels" names the host-versus-shipped and SPEC-versus-procedure overlaps: a document carrying a level that is not its own.
- Revision as its own periodic pass, not riding each change, is the shape the sweep already has; none of the fields runs it at a weekly cadence — statute revision is years, policy review is annual or on a trigger.

## Frame assessment

- **TIME RANGE** — not applicable: the practices are stable across decades; none is tied to a period.
- **PEOPLE** — applies partly: these fields audit documents read by people, and this corpus is read by a model; the ownership-and-pointer principle transfers because a model, like a reader, is degraded by near-identical passages (the project's own admission-cost finding), but the depth limits (two or three levels) come from human navigation and are not evidence about a model.
- **FRESHNESS** — the manuals are revised on cycles (one dated June 2026); the principles cited are unchanged across editions.
- **RISK IF WRONG** — low: a lens admitted on this basis is judged at planning through the rule gate and finds restatements that are then decided one by one; a wrong frame costs audit effort, not a shipped defect.
- **ALTERNATIVES** — software engineering's DRY and API-documentation practices were not searched; they say the same thing as the SSOT material and were left out rather than ruled out.

Sources: [HOLC Guide to Legislative Drafting](https://legcounsel.house.gov/holc-guide-legislative-drafting), [Quick Guide to Legislative Drafting (rev. 2026)](https://legcounsel.house.gov/sites/evo-subsites/legcounsel.house.gov/files/documents/quick_guide.pdf), [Statute law revision](https://en.wikipedia.org/wiki/Statute_law_revision), [Legislative drafting error](https://en.wikipedia.org/wiki/Legislative_drafting_error), [Maryland Legislative Drafting Manual](https://dls.maryland.gov/pubs/prod/LegisBillDrafting/LegislativeDraftingManual2025.pdf), [Healthcare policy and procedure management](https://www.accountablehq.com/post/healthcare-policy-and-procedure-management-a-practical-guide-to-workflows-templates-and-compliance), [Policies vs standards vs controls vs procedures](https://www.complianceforge.com/grc/policy-vs-standard-vs-control-vs-procedure), [Building a single source of truth (Atlassian)](https://www.atlassian.com/work-management/knowledge-sharing/documentation/building-a-single-source-of-truth-ssot-for-your-team), [What is SSOT (Paligo)](https://paligo.net/blog/content-reuse/what-is-single-source-of-truth-ssot/), [Content reuse in technical documentation (Paligo)](https://paligo.net/blog/content-reuse/quick-guide-to-mastering-content-reuse-in-technical-documentation/).
