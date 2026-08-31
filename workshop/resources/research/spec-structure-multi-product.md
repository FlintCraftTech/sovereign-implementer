# Spec structure for multi-product / multi-area projects

Research filed 2026-06-22 to tee up the [spec-sot-rethink] design session — the question of whether SI keeps one `SPEC.md` (restructured project-shaped), invents per-product specs, or takes a middle path, and how SPEC stays useful rather than drifting into boilerplate.

## The decision this informs

[spec-sot-rethink] fork:
- (a) keep one `SPEC.md`, restructured to be project-shaped with top-level sections per product/area
- (b) multiple specs, one per product/area
- (c) a middle path

Plus the sub-questions: can /setup seed SPEC less sparsely, and how does SPEC stay useful rather than drifting into boilerplate.

## What the research found

### 1. The established pattern is a TWO-LAYER structure, not single-vs-multiple

The most on-point sources are the spec-driven-development (SDD) tools — Kiro, spec-kit, Tessl — because SI *is* an agent-driving spec method. The pattern they converge on:

- A **shared top-level context layer** that applies across everything — Kiro calls it "steering," spec-kit/others call it a "memory bank": files like `constitution.md`, `product.md`, `architecture.md`. This is the whole-project truth.
- **Per-feature (or per-file) specs** underneath it. Kiro: three docs per feature (requirements / design / tasks). spec-kit: a folder of ~8 files per spec. Tessl: one spec per code file.

So the real-world answer to "single vs multiple" is **both, layered**: one project-level spec (the steering/product layer) PLUS narrower specs beneath it. That maps directly to SI's option (c) middle path, and is the strongest-supported option.

### 2. Multi-product docs: centralized vs distributed is a known trade-off

- **Centralized** (one place): consistency, single point of access, but can overwhelm without careful organization.
- **Distributed** (per-product spaces): flexibility and product-specific tailoring, but management complexity and inconsistency risk.
- Repeated advice: keep structure/navigation **as simple as possible** — complex navigation confuses users juggling multiple products. The goal stated everywhere is "centralization without sacrificing per-product flexibility" — i.e. the layered middle path again.

### 3. Monorepo single-source-of-truth: centralized standards + local specifics

- Org-wide rules live in one place and apply everywhere (the SOT benefit).
- BUT each package keeps its own package-specific config/docs when needed.
- Same shape: shared standards centralized, per-unit detail local.

### 4. PRD practice for portfolios: hierarchy

- Theme (multi-year strategic goal) → Initiative/Epic → Feature/User Story.
- "Living documentation" — requirements attached to the feature they serve, each carrying the goal/insight/context behind it — is favoured over text "locked inside a static file."

### 5. Boilerplate drift is a RECOGNISED, UNSOLVED problem — directly relevant

The SDD article's sharpest warning: spec-kit "created a LOT of markdown files... repetitive, both with each other, and with the code that already existed," and questions whether reviewing verbose markdown actually improves control over AI output. **Lesson for SI:** a fuller SPEC is not automatically a better one. The failure mode is verbose spec that restates the code/other specs and adds no control. SPEC should stay lean and decision-bearing, not exhaustive — which fits SI's existing "readable output is a control requirement" principle.

## How this bears on the SI decision (for the design session to weigh)

- **Option (c) / middle path is the best-supported by prior art** — a single project-level SPEC (the "steering/product" layer: what the whole project/business is) with per-product/area sections or sub-specs beneath. Pure (b) per-product specs is the "distributed" pattern: more flexibility, but it multiplies the scope-lock / spec-edit-batch machinery (which all assume one `SPEC.md` by name) and risks inconsistency. Pure (a) one flat spec is the "centralized" pattern: simplest for the machinery, but the Simply Sew failure (SPEC took app-shape and squeezed out the wider business) shows a flat single section won't hold a multi-product project without an explicit per-area structure.
- **On "seed SPEC less sparsely at /setup":** prior art doesn't say seed *more* — it says seed the *right two layers*. The /setup interview could establish the project-level layer (what the whole thing is, how many products/areas) first, then a thin per-area stub each — rather than one flat app-shaped spec.
- **On "stays useful not boilerplate":** keep it lean and decision-bearing; the drift risk is verbose restatement, not under-specification.

## Sources

- [Exploring Spec-Driven Development: Kiro, spec-kit, Tessl (Martin Fowler)](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) — most relevant; the two-layer steering + per-feature pattern and the boilerplate-drift warning
- [Multi-Product Documentation Strategy (Document360)](https://document360.com/blog/multi-product-documentation-strategy/) — centralized vs distributed trade-off
- [How to Structure Documentation for Multi-Product Companies (Archbee)](https://www.archbee.com/blog/multi-product-documentation-strategy)
- [How to Write a PRD (Perforce)](https://www.perforce.com/blog/alm/how-write-product-requirements-document-prd) — portfolio hierarchy, living documentation
- [Monorepo.tools](https://monorepo.tools/) — single source of truth + per-package specifics
