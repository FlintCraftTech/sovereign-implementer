# Autonomous build-loop design — prior art for cruise control

Filed 2026-06-25, opening the [cruise-control] design session. Direct web searches (not the deep-research subagent fan-out — the cost guard [subagent-ask-gate] exists because that fan-out blew Max usage). Question: how do existing autonomous coding agents handle stopping conditions, not-pushing-through-uncertainty, and human-in-the-loop gates?

## Headline

Cruise control is a well-trodden pattern, not novel. The field has settled answers for most of our design concerns. The one thing our concerns list is **missing** is the field's most universal safeguard: explicit hard stops (iteration ceiling, no-progress detection, budget ceiling). Every source treats these as mandatory for an unattended loop. We have "stops when it needs the user" but no ceiling on a loop that never asks — which is exactly the runaway-cost failure the subagent incident already showed once.

## The autonomy-levels frame (Swarmia)

Five levels: (1) assistive autocomplete, (2) conversational multi-file, (3) task agent — hand off a scoped task, get a PR back, review without real-time supervision, (4) autonomous teammate — picks work from a backlog unprompted, human reviews outcomes not steps, (5) multi-agent orchestration.

Cruise control sits at **Level 3 → 4**: it picks the top queue batch unprompted (4) and runs it to a committed result (3). The load-bearing claim: **higher isn't better, and each level has prerequisites.** Level 3 "requires well-scoped tasks and solid CI; operating at higher levels without the prerequisites creates more work than it eliminates." This reframes [plan-dependency-tracing-gap]: it isn't an arbitrary blocker on deployment — a traced dependency graph and well-scoped batches *are* the prerequisite that earns the autonomy level. The method's existing gates (scoped batches, verification, the why-pipeline) are what make Level 3-4 safe.

## Stopping conditions (loop-engineering sources)

Three hard stops, treated as universal:
1. **Iteration ceiling** — cap total loop cycles (e.g. MAX_ITER=20).
2. **No-progress detection** — stop when the same error, an empty diff, or a failing test repeats N times in a row.
3. **Budget ceiling** — a per-run token/cost budget set before you walk away.

"Done" is defined as an explicit contract up front: *all checks green, OR N iterations, OR $X spent.* Anchor files (their VISION.md; our SPEC.md + QUEUE.md + _build.md) hold the intent so each loop tick doesn't re-derive it from scratch — a pattern the method already uses.

## Not pushing through uncertainty

Concrete mechanism worth stealing: when blocked twice on the same error, the agent **writes BLOCKED to a file and exits**, rather than retrying indefinitely. This is a mechanical version of concern (1) — a stuck-detector that halts-and-records instead of thrashing or rationalising past the problem. "A loop with nothing to push back on is the agent agreeing with itself" — verification gates (tests, review, the red-flag screen) are what keep the loop honest, which is concern (3).

## Human-in-the-loop gates

Standard pattern is **risk-tiered**: low-risk changes auto-proceed (a utility function, a typo); high-risk changes halt for a human (schema migration, security-critical, infra). Our gates fit this exactly — red flags (4) and SPEC/product-truth changes (6) are the "high-risk → halt" set; ordinary in-scope builds are "low-risk → proceed." Research note (OpenHands): treating the agent as a pair rather than a vending machine — stopping it when it heads down a wrong path — "roughly doubled completion rate on non-trivial tasks." So the gates that pull the human back aren't only safety; intervention improves results. Full autonomy is earned through trust-building, not assumed.

## What this changes for the design

- **Add hard stops as a first-class concern (new).** Iteration ceiling + no-progress detector + budget ceiling. Not on our list; the field treats them as mandatory; directly addresses the Max-usage fear.
- **Steal "write BLOCKED and exit"** as the mechanism for concern (1) — halt-and-record on a repeated stuck state.
- **Reframe [plan-dependency-tracing-gap]** as the prerequisite that earns Level 3-4, not an arbitrary gate.
- **Validates** concerns (3) verification-can't-be-skipped and (4)/(6) risk-tiered halts against standard practice — we're not inventing these, which is reassuring.

## Sources

- [Five levels of AI coding agent autonomy — Swarmia](https://www.swarmia.com/blog/five-levels-ai-agent-autonomy/)
- [Loop Engineering: coding agent loops that run while you sleep — explainx.ai](https://explainx.ai/blog/loop-engineering-coding-agents-claude-code-guide-2026)
- [OpenHands review 2026 — Pickuma](https://pickuma.com/for-dev/openhands-review-open-source-autonomous-coding-agent-2026/)
- [Human-in-the-loop agentic systems — Medium](https://medium.com/@tahirbalarabe2/human-in-the-loop-agentic-systems-explained-db9805dbaa86)
- [Measuring AI agent autonomy — Anthropic](https://www.anthropic.com/research/measuring-agent-autonomy)
