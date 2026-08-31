# When a subagent is genuinely needed — context-overflow vs token-cost

Filed 2026-06-26, during the [cruise-control] design session, to ground the plan-time subagent rule in a concrete list instead of letting Claude guess (and over-ask). The design question: under cruise control there is no user to answer a subagent permission prompt, so we want builds authored with subagent needs pre-decided — but only for the rare cases that genuinely need one, not on speculation.

## The core distinction (this is the whole point)

A subagent's real benefit is a **separate context window**: the heavy raw material (source files, logs, documents) goes into the subagent, and only a short, dense summary comes back to the main run. So a subagent is the right tool only when a task would **overflow a single context window** — not merely when it **costs a lot of tokens**.

These are two different problems, and the user's own experience pins the difference exactly:
- **Token cost** — deep research burns a lot of tokens but does *not* fill the context bar. Multi-agent / subagent work runs ~15× the tokens of a single chat (Anthropic's own figure). This is a cost problem, not an overflow problem.
- **Context overflow** — a single body of material too large to hold in one window at once. This is the only thing a subagent uniquely solves.

The user reports never having needed a subagent, and rarely seeing the context bar pass halfway. That is consistent with the research: normal build work does not approach context overflow. So **default-against-subagents is correct**, and the genuine-need list below is short.

## Genuine context-overflow cases (a subagent earns its place)

1. **Large / multi-repo codebase analysis.** A thorough read of even a modest ~200-file project can burn 100K+ tokens before producing useful output; larger or multi-repo codebases overflow a single window. The subagent reads files and returns a dense structured summary, so the main run grows by summary size, not source size. This is the headline case.
2. **Large document-set or archive synthesis.** End-to-end analysis over a whole document archive, a year of support tickets, a set of legal/financial filings — a single corpus several times larger than one session can hold.
3. **Large log / large-file analysis.** Reading very large log files or doing flaky-test/anomaly analysis across many runs, where the raw content floods the window with material you won't reference again.

Common thread: each is **ingesting and reasoning over one large corpus** that doesn't fit. If a build isn't doing that, it isn't this.

## Token-cost-only cases (NOT a context-overflow reason)

- **Multi-source research synthesis** (the deep-research pattern) benefits from subagents for **parallel speed** and for keeping accumulated summaries (not raw sources) in the orchestrator — but in the user's usage it burns tokens without overflowing context. So under cruise control it stays **default-against**: it is a cost, and cost is exactly what an unattended run must not spend silently. Parallelism speed is not a reason to spend 15× tokens unattended.

## When a subagent is NOT warranted (the normal case)

- Short or simple tasks — a single lookup, one file read, a quick grep.
- Tasks whose steps depend on each other's intermediate results (sequential is simpler and just as good).
- Tasks needing shared context across the work (subagents don't share context).
- Anything that fits comfortably in one window — which is essentially all routine SI build work (editing a handful of procedure docs, building one app feature per batch).

## Implication for the cruise-control design

- **Default:** cruise control uses **no subagents at all**.
- **The only exception:** a build that plainly matches one of the three context-overflow cases above (large codebase sweep, large document/log/archive synthesis). Only then does the plan-time rule engage — surface it to the user when the build is authored, name the cost, and offer the alternative of **splitting the batch along context-bearing lines** (e.g. cover a subset of the codebase per batch instead of one big subagent sweep).
- **No match → no subagent, no question asked.** The trigger is a concrete match to this list, never Claude's anticipation — which is what stops the rule from pestering on builds that never needed one.
- **At run time:** an unforeseen subagent need that the plan didn't anticipate is a halt-for-the-user (the batch was bigger than scoped — surface it), not a silent inline workaround.

## Sources

- [Create custom subagents — Claude Code Docs](https://code.claude.com/docs/en/sub-agents)
- [How to Use Sub-Agents in Claude Code to Manage Context and Speed Up Research — MindStudio](https://www.mindstudio.ai/blog/sub-agents-claude-code-context-management)
- [How to Use Sub-Agents for Codebase Analysis Without Hitting Context Limits — MindStudio](https://www.mindstudio.ai/blog/sub-agents-codebase-analysis-context-limits)
- [Claude Code Subagents: A 2026 Practical Guide — Tembo.io](https://www.tembo.io/blog/claude-code-subagents)
- [How we built our multi-agent research system — Anthropic](https://www.anthropic.com/engineering/built-multi-agent-research-system)
- [Why Multi-Agent AI Beat a Single Agent by 90% at Anthropic — Virtasant](https://virtasant.com/ai-today/why-multi-agent-ai-beat-a-single-agent-by-90-at-anthropic)
- [Context Window Overflow in 2026 — Redis](https://redis.io/blog/context-window-overflow/)
