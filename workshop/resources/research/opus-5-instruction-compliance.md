# Opus 5 instruction-following — and what it means for the multi-model fork

Researched 2026-07-31 (web) to settle the [fable-docset-model-detection] strategic fork: now that Opus 5 has shipped (launched 2026-07-24), is it "as fussy as 4.8" (→ build an Opus-5-specific docset) or close enough to Fable that one target serves both?

Sources: Anthropic's official [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5) and [Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) guides, plus secondary coverage (apidog, metacircuits, note.com "removing is more effective than adding").

## The headline finding: Opus 5 is fussy in the OPPOSITE direction to 4.8

4.8's failure mode was *under*-steering: it's literal, needs explicit scope, and needs a why-clause travelling with each rule or the rule slips. The whole SI docset is hardened around that — heavy why-clauses, explicit scope-locks, verbosity steering, redundant guards.

Opus 5's failure mode is *over*-doing: left alone it self-verifies, expands scope, narrates readily, and is verbose by default. Anthropic's guidance is **subtraction, not addition** — "the focus of Opus 5 prompt design has shifted from adding to make it smarter to subtracting to stop it from overdoing things."

Concretely, from the official Opus 5 guide:
- **Self-verification is built in** — remove "double-check," "include a verification step," "use a subagent to verify"; leaving them in causes over-verification that burns tokens for no quality gain.
- **Verbose by default** — user-facing responses and written deliverables (reports, READMEs) run longer than 4.8. Length is a *prompt-side* control; the effort parameter controls thinking, not output length. Fix with an explicit brief-conciseness instruction.
- **Expands scope** — adds steps not asked for. Fix with an explicit "deliver what was asked, at the scope intended" constraint.
- **Narrates readily** — announces what it's about to do; per-message agentic output longer than prior models.
- **Literal on conservative instructions** — "only report high-severity issues" makes it report less; ask for everything and filter in a separate pass.
- Runs well out of the box on existing 4.8 prompts — but the *optimisation* is removing 4.8-era scaffolding, not adding.

## Fable 5 and Opus 5 converge

Fable 5's guide says the same things in the same direction: strong instruction following (steer most behaviours with a *brief* instruction rather than enumerating each), elaborates beyond need at high effort, and critically — **"Skills developed for prior models are often too prescriptive for [Fable 5] and can degrade output quality. Review and consider removing older instructions if default performance is better."**

So both 5-series models want **less prescription than 4.8**, brief steering, and both self-verify / run long / can over-reach on scope. They do not behave like 4.8's "spell everything out or it slips."

## What this means for the fork

1. **Opus 5 is not "as fussy as 4.8" in the additive sense.** It doesn't need the heavy why-clause hardening. So an Opus-5-specific docset built *like* the 4.8 one would be wrong — it would over-prescribe and degrade Opus 5.
2. **Fable 5 and Opus 5 are close enough that a single "5-series" target is viable** — Alex's preferred branch. Both want a lighter, subtraction-tuned docset.
3. **But that unified target is a NEW, lighter docset, not the current 4.8 docset re-aimed.** The current docset's defining feature (why-clauses travelling with every rule, explicit scope guards) is exactly the over-prescription the 5-series guidance says degrades output. Re-aiming the heavy docset at the 5-series would carry the 4.8 medicine into models that don't need it.
4. **Preserve the 4.8 docset as-is (the working fallback).** This is what the project already runs on and depends on — Alex's non-negotiable. It stays the frozen, known-good target.

### The architecture that falls out — roughly 2 docsets, not N

- **Docset A (heavy):** the current 4.8-hardened docset. Frozen, the working fallback.
- **Docset B (light):** a new subtraction-tuned "5-series" docset serving both Fable 5 and Opus 5.
- Session-start model detection (feasibility already confirmed: SessionStart can receive a `model` field, with a fallback needed when absent — see resources/research/sessionstart-hook-model-detection.md) picks A for 4.8, B for the 5-series, defaulting to A (the safe fallback) when `model` is absent.

This collapses the earlier "N per-model docsets" worry into two, which is far more maintainable.

### The hard design risk to carry forward

The difference between docset A and docset B is **prescription density** — a cross-cutting quality of the whole doc, not a localised delta. The method's shared-core + per-model-overlay plan (from the prior research) assumes deltas factor cleanly into small local overlays. Prescription density may NOT factor that way: "lighter everywhere" is not "change these three sections." So the two docsets could diverge in every paragraph, reintroducing exactly the cross-doc drift the method fights. Whether a shared-core+overlay can express "same procedure, less prescription" is the core unsolved design question — and it may push toward keeping A frozen and hand-authoring B once, rather than a live overlay.

### A live "defer the split" option

Because Opus 5 runs acceptably on 4.8 prompts out of the box (just over-verified / occasionally over-scoped), SI could keep running the 4.8 docset on Opus 5 for now and only build docset B when that over-prescription cost becomes painful in practice. This trades some Opus-5 output quality for zero new maintenance surface until the need is proven — consistent with the method's "broken behaviour re-captures itself in use" stance.

## Bottom line for the fork

Alex's "one target serves both Fable and Opus 5" branch is the correct read of the evidence — with the correction that it's a *new light docset*, not the current one re-aimed, and the 4.8 docset stays frozen as the fallback. The remaining open design work is (a) whether to build docset B now or defer until the cost bites, and (b) whether prescription-density can live as an overlay on a shared core or forces a separate hand-authored doc.
