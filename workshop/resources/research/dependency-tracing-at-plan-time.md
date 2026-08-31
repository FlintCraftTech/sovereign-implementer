# Dependency tracing at plan time — prior art

Filed 2026-06-29 during the [plan-dependency-tracing-gap] design session. Question: how do real build systems and AI planning/SDD tools work out what depends on what *before* building, so /plan's tracing fix borrows from approaches that already work rather than being designed from scratch.

## Headline

The prior art strongly supports the **middle (bounded) option** and sharpens its mechanics. Two findings reframe the design:

1. **"Surface dependency problems at planning time, not during execution" is the established, validated principle** — exactly the [plan-dependency-tracing-gap] reframe (fix /plan, not the execution guards).
2. **No static dependency check can ever be complete** (stated outright by Bazel). This is the honest limit: the fix *reduces* the failure modes, it does not eliminate them — so /next's scope-lock + abort stays the backstop, and modes 4 (ripple) and 5 (on-device reversals) are correctly named as accepted residual, not /plan's to solve.

## Findings

### 1. Build systems: declared deps must be a *superset* of actual deps (the anchor for "traced-ness")

Bazel's core rule: *"the graph of actual dependencies A must be a subgraph of the graph of declared dependencies D"* — i.e. declare every actual direct dependency, **and no more**. Under-declaring is the error: the build may pass by luck (transitive closure happens to cover it) and break later when an intermediate dependency is refactored away.

This is *exactly* failure mode 1 (a real dependency that was assumed/omitted and only surfaced when /next read the code). The transferable rule for SI: a batch's `Depends on:` must cover every *actual* dependency — over-declaring is safe, under-declaring is the bug. So the trace's job is to close the gap between declared and actual.

Crucial caveat, stated by Bazel itself: *"Bazel checks for missing dependencies and reports errors, but it's not possible for this checking to be complete in all cases."* Even a mature build system can't statically catch every missing dependency. → Don't design /plan's trace as exhaustive; design it to catch the common cases and lean on /next as the net.

Bazel/Buck do **not** auto-derive deps from imports by default — authors *declare* them explicitly. For import-driven languages they add *dynamic dependency detection* that reads file contents to derive deps (Buck2), or a pre-build tool (Reindeer) that discovers deps and generates targets *before* the build. Lesson: deriving deps from real source is a known, separate, deliberate pass — not something assumed inline.

### 2. AI task planning: a "missing-dependency detector" is a validated mechanism

Agent-oriented planning research runs a *detector* that "determine[s] whether there are any missing dependencies before a sub-task is assigned to an agent for execution." Handling missing dependencies gave a measured **+2.5% accuracy** (43.7% → 46.2%). Direct support for SI's **completeness check** (every named dependency must have a producer) as a real, worthwhile, pre-execution step.

### 3. Production AI coding: validate + topologically sort *before* scheduling

A "Task IR" (task intermediate representation) represents work as structured tasks with explicit dependencies, then "validates dependencies and performs topological sorting using Kahn's algorithm before scheduling, ensuring that execution deadlocks are surfaced at planning time rather than during execution." This is the SI reframe in someone else's system.

Kahn's algorithm is also the mechanical detector: process nodes with no unmet dependencies first; if the queue empties before all nodes are processed, the remainder have unresolved dependencies (a missing producer or a cycle). That is precisely how a **producer-existence / completeness check** is implemented — a `Depends on:` edge pointing at a node that no batch produces and no code/SPEC satisfies is an unresolvable edge.

### 4. SDD insight on why this matters

"When an LLM tries to plan and execute simultaneously, it makes execution decisions before planning is complete and edits files in ways that are incompatible with other changes because it had not thought through the full dependency graph before starting." This is the argument for SI's plan/execute split *and* for tracing the graph at plan time rather than discovering it mid-build.

### 5. spec-kit: derive dependencies from the design artifacts, and the trend is toward *explicit* declarations

GitHub spec-kit derives task dependencies from the design docs (spec.md, plan.md, data-model.md, contracts/), mapping endpoints→user stories and ordering models→services→endpoints. Two lessons:
- **Trace against the spec/design layer, not only raw code** — cheaper than whole-codebase reading and often sufficient. For SI this means SPEC + the specific files a batch names, not a full repo sweep.
- spec-kit has an **open feature request to add explicit `(depends on T001)` declarations** because implicit/derived ordering wasn't enough for agents. SI already *has* explicit declared edges (`Depends on:` slugs); the gap isn't declarations, it's that they're **asserted, not verified**. So the fix is verification + completeness, not adding a declaration mechanism.

## What this means for the SI design

- **Middle option confirmed; heavy mildly counter-indicated.** A full whole-codebase graph trace every /plan is both expensive on every consumer and falsely implies completeness Bazel says is unattainable.
- **Completeness check = producer-existence (Kahn-style).** Every `Depends on:` slug resolves to a producer: a queued batch that builds it, already-built code, or SPEC. No producer → flag. Cheap, mechanical, validated (+2.5% in the planning research). Extends today's ordering-only check.
- **Bounded trace = enforce the superset principle.** A build batch's declared deps must cover its *actual* deps, traced against SPEC + the files the batch names (not the whole repo). Source citations on the `Depends on:` line are the evidence of tracing.
- **Honest limit, named not hidden.** Static checking can't be complete → /next's scope-lock + abort remains the backstop; modes 4 and 5 stay accepted residual.

## Sources

- [Bazel — Dependencies](https://bazel.build/concepts/dependencies) (declared-superset-of-actual rule; "checking can't be complete")
- [Bazel — External dependencies overview](https://bazel.build/external/overview)
- [Buck2 — Why Buck2](https://buck2.build/docs/about/why/) (dynamic dependency detection reading file contents)
- [Agent-Oriented Planning in Multi-Agent Systems (arXiv 2410.02189)](https://arxiv.org/pdf/2410.02189) (missing-dependency detector, +2.5% accuracy)
- [Production-Grade AI Coding System for Client-Side Development (arXiv 2603.01460)](https://arxiv.org/pdf/2603.01460) (Task IR, validate + Kahn's topological sort before scheduling)
- [Separation of Planning and Execution (DEV)](https://dev.to/varun_pratapbhardwaj_b13/separation-of-planning-and-execution-the-key-pattern-for-reliable-ai-coding-agents-5b53)
- [Topological Sort / Kahn's algorithm — dependency resolution](https://read.thecoder.cafe/p/topological-sort)
- [GitHub spec-kit](https://github.com/github/spec-kit) and [tasks.md template](https://github.com/github/spec-kit/blob/main/templates/commands/tasks.md); [Issue #1934 — explicit task dependency declarations](https://github.com/github/spec-kit/issues/1934)
