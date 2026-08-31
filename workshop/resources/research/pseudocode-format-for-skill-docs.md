# Pseudocode / structured formats for skill docs — pinning down the candidate style for docset B

Researched 2026-08-01 (web) to answer, before committing docset B to a style: can we combine pseudocode types, should we invent our own for skill docs, has anyone done this already, and which one or two formats are best-supported? Feeds the candidate-style note on [fable-docset-model-detection].

## Has someone done this for skills? Yes — and it's measured.

**Skill-as-Pseudocode (SaP)** — arXiv 2605.27955 — automatically refactors markdown skill libraries into **typed pseudocode**. The problem it names is exactly ours: free-form prose forces the agent to re-derive structure on every read ("issue a partially-correct action, receive uninformative feedback, re-retrieve the same prose"). Its fix gives two signals per skill: a **typed signature** (what the skill does) plus a **concrete template** (how to invoke it).

Measured (ALFWorld, gpt-4o-mini): 82/402 games won vs 47/402 baseline (p=8.2e-5), **22.8% fewer input tokens**, **14.5% fewer LLM calls**. So the structure pays off in both success and token cost.

Supporting evidence that structure helps generally:
- **Pseudo-code prompting** improves task accuracy — up to **+31 points** on complex reasoning vs ambiguous natural language (emergentmind survey).
- **PromptMN** (arXiv 2606.17164) — a lighter approach: annotate natural-language with compact `%`-prefixed typed directives (roles, goals, constraints, inputs, outputs). "Annotated prose" rather than full pseudocode.

## Should we invent our own pseudocode for skill docs? No — the research says don't.

This is the important caution against the "make our own" idea. **Grammar Prompting** (NeurIPS 2023) finds DSLs the model hasn't seen enough in pretraining are hard: a custom syntax is "unlikely to have been encountered often enough during pretraining for the LLM to acquire its full syntax," so the model needs the grammar spelled out and can still produce invalid output. And SaP deliberately uses **familiar typed pseudocode, not a novel DSL**, precisely to keep it accessible.

Takeaway: a bespoke SI notation risks the model not knowing the syntax — the opposite of the goal. Stay in **widely-pretrained conventions**: typed function signatures, IF/THEN blocks, arrays, standard markdown.

## Can we combine types? Yes — a hybrid is what the evidence actually supports.

The best-supported shape is not "pure pseudocode" but a **layered hybrid**:
1. **Typed signature** — what the rule/step is (SaP's "what").
2. **Concrete template/example** — the shape to follow (SaP's "how"; positive examples beat prohibitions, per Anthropic's own 5-series guidance).
3. **Thin natural-language** — only the genuine nuance/why that doesn't reduce to structure.

That layering maps directly onto SI: pseudocode carries the mechanics; a *thin* prose layer carries the lighter rationale the 5-series still benefits from (far less than 4.8, but not zero).

## Anthropic's own baseline conventions (don't fight these)

Skill best-practices (platform docs): SKILL.md = YAML frontmatter (name + description, used to decide loading) + markdown body; progressive disclosure; keep SKILL.md **under ~500 lines**; file references one level deep. Docset B should sit inside these conventions, not replace them.

## Pinned recommendation — one primary, one lighter alternative

- **Primary candidate: SaP-style familiar typed pseudocode** — typed signature + concrete template, in standard markdown, thin prose for nuance. Strongest evidence, and it's a skills-specific result.
- **Lighter alternative: PromptMN-style annotated prose** — keep natural-language sentences but tag them with compact typed directives. Less of a rewrite; a fallback if full pseudocode reads badly for SI's rule style.
- **Rejected: a bespoke SI DSL** — grammar-prompting caveat; the model may not know the syntax.

## Caveat that keeps this a "validate," not "decided"

The SaP/pseudo-code gains are measured on **agent task-completion benchmarks** (ALFWorld, tool-invocation), not on **procedural-rule adherence** for a governance doc like SI's plugin-behaviour.md, and not on Fable 5 / Opus 5 specifically. So the format is now *pinned to two familiar candidates*, but which one (and how much thin-prose nuance to keep) still needs testing against real Fable 5 / Opus 5 output when docset B is authored — exactly the validation the item already calls for. Research narrows the design space; it doesn't remove the test.

Sources: [Skill-as-Pseudocode (arXiv 2605.27955)](https://arxiv.org/abs/2605.27955); [Pseudo-code prompting survey (emergentmind)](https://www.emergentmind.com/topics/pseudo-instructions); [PromptMN (arXiv 2606.17164)](https://arxiv.org/pdf/2606.17164); [Grammar Prompting (NeurIPS 2023)](https://arxiv.org/pdf/2305.19234); [Anthropic Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).
