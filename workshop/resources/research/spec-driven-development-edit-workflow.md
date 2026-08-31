# Spec-driven development: does inline spec editing (no spec-edit batch) comply?

Filed 2026-06-25, during the /plan design session on retiring the spec-edit batch type.

## The question

SI's design (decided f4fba84, [spec-edit-batch-type]) made every SPEC change its own "spec-edit batch" — a separate queued, /next-executed batch that lists SPEC.md. In practice these became one-line batches and a time sink across projects. The proposed change: allow SPEC edits during /plan in-session and during /next via the scope-lock ask, retire the batch type, and prevent drift with spec-sync checks at the /plan and /done close-outs. Does this still comply with spec-driven development (SDD)?

## Finding: it complies — and aligns better with mainstream SDD than the batch type did.

### What SDD actually requires

- The spec is the source of truth; code is the derived artifact. When the AI drifts, you point it back to the spec. (Microsoft, IBM, OpenSpec.)
- The load-bearing contract: every change that alters system behaviour must either CITE the spec or UPDATE it — in the same pull request. This is the atomicity rule that prevents spec/code drift. (martinfowler.com SDD-3-tools; arXiv 2602.00180.)
- Agreement before dependent code: the spec is "authored and agreed upon before development begins."

### What SDD does NOT require

- It does NOT mandate that a spec change be its own separate, gated step. Flexible SDD workflows explicitly allow editing the spec during implementation: "you can edit design.md whenever needed... there are no phase gates forcing you to finish one stage before moving to another." (liatrio-labs, intent-driven.dev, OpenSpec.)
- The stricter phase-gated reading (Kiro-style spec → design → tasks → implement) still doesn't require a separate queued batch — only that the spec be updated and approved before dependent code depends on it.

### How our design maps to SDD

- Source of truth preserved: SPEC stays authoritative; nothing here changes that.
- Atomic cite-or-update satisfied: the two close-out spec-sync checks sit at commit boundaries — the /plan commit and the /done commit. A behaviour change can't CLOSE a session (commit) with SPEC behind. That is exactly SDD's "update the spec in the same PR." Our spec-drift trigger ("does any SPEC sentence go wrong or incomplete given this change?") is the cite-vs-update fork: already covered by SPEC -> cite, made wrong -> update.
- Agreement preserved: SPEC changes stay user-approved — in /plan the user is present; at /next the scope-lock forces the ask before the build proceeds on the change.
- Large changes: our "a big spec rework is a normal build batch that lists SPEC.md" mirrors Spec-Kit's branch-isolation for big features.

### The friction we are fixing is a recognised SDD-tooling weakness

- Spec-Kit issue #1191: current SDD tooling is bad at updating/refining EXISTING specs — optimised for net-new feature creation, hard to iterate without redundant specification artifacts. Our one-line-batch pain is the same weakness. Retiring the batch type fixes a friction SDD tools also struggle with, rather than deviating from SDD.

### The one principle we must keep enforcing

- The atomic contract only holds if the spec-sync checks are ENFORCED at close, not advisory or skippable. If a behaviour-changing build could commit with SPEC behind, that breaks SDD's core atomicity rule. So both close-out checks must be hard enough to stop the close, not merely flag — this is the design constraint the compliance verdict rests on.

## Relation to existing items

- [spec-sot-rethink] — the parked design item on making SPEC genuinely useful and right-sized. Same root (thin SPEC, disproportionate ceremony). This workflow change and that structure question shape each other.
- resources/research/spec-structure-multi-product.md — the earlier research on SPEC structure (single vs multiple specs). This file is the edit-workflow companion to it.

## Sources

- https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- https://developer.microsoft.com/blog/spec-driven-development-ai-native-engineering
- https://www.ibm.com/think/topics/spec-driven-development
- https://github.com/Fission-AI/OpenSpec
- https://github.com/github/spec-kit/issues/1191
- https://arxiv.org/html/2602.00180v1
- https://github.com/liatrio-labs/spec-driven-workflow
- https://intent-driven.dev/knowledge/workflows/
