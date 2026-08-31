# AI memory/context trajectory — what the ground under "heavy docs in context" is doing

Filed 2026-06-23. Deep-research pass (fan-out web search → adversarial verification → synthesis) run because the Sovereign Implementer deliberately loads heavy documentation into context, and programmers critique it as "heavy on memory." Question: is that design bet getting safer or riskier over time? Covered three distinct axes because they have different answers.

## Headline verdict

**The bet is getting safer on cost and memory; the standing risks are quality-at-scale and tier-gating.** The user's instinct that "constraints go up because AI profitability is tough" is half right: raw per-token cost is falling fast, but capability is increasingly fenced behind subscription tiers. Those two pull in opposite directions.

## Axis 1 — Context window size: a quality ceiling, not a size ceiling

- Windows kept growing (200K → 1M+), but **bigger nominal windows don't mean bigger usable ones.** Multiple independent sources (Chroma "context rot," Databricks long-context RAG, an EMNLP 2025 paper) found every model degrades well before its advertised limit — and degrades *even when it retrieves the right text perfectly.* Confidence: high.
- Implication for SI: the "heavy on memory" critique is partly fair, but not for the cost reason assumed — it's that **curation beats volume.** A leaner, well-ordered doc load is both cheaper and more *reliable* than a big one.

## Axis 2 — Cost / affordability: the safest axis

- Inference prices falling ~50×/year (steeper since 2024); Anthropic removed the old long-context price premium; prompt caching cuts the cost of re-sending the same docs ~90%. Confidence: high.
- Caching catch: the discount only holds inside an active session — the ~5-min cache TTL **resets each time the cache is used**, so a session with steady back-and-forth stays warm start to finish; it goes cold only on a >5-min idle gap or on `/clear` + return. So caching helps *within* a session (turns 2..N are cheap), never *across* the `/done`→`/clear`→return gap. The reason cost stays the smallest worry is the raw per-token price drop, which applies cached or not.

## Axis 3 — Persistent cross-session memory: coming, not consumer-ready

- The capability that would let a tool NOT reload heavy docs each session exists (Claude memory tool; Claude Managed Agents memory, beta April 2026) but cross-session memory is **enterprise beta, not the consumer desktop app** SI's users run. Confidence: high.
- Implication: a real future off-ramp from in-context document loading, but not one to build on today.

## The 1M-context thread (user reported the 1M option vanishing from her desktop UI)

- Documented: **1M context is gated to Claude Code specifically; chat caps at 500K; Pro-tier needs paid usage credits to reach the big window**, and one source flags a 1M-beta retirement dated April 30 2026. So a 1M option disappearing fits documented gating/retirement, not a glitch. Confidence: high.
- Caveat: her account wasn't inspected, so a bug isn't fully ruled out — but the weight is on "real." This is the one place the "profitability fences access" thesis is clearly correct: the capability didn't vanish, it got fenced behind a tier.

## Caveats

Fast-moving June-2026 snapshot; prices and beta status can shift. The verification pass hit rate-limiting partway, so a few votes abstained rather than fully confirming — the four headline findings held at high confidence.

## Key sources

- Chroma "context rot" — https://research.trychroma.com/context-rot
- Databricks long-context RAG — https://www.databricks.com/blog/long-context-rag-performance-llms
- Epoch AI inference price trends — https://epoch.ai/data-insights/llm-inference-price-trends
- Anthropic prompt caching docs — https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- Anthropic context-window plan limits — https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans
- Claude Managed Agents / memory — https://claude.com/blog/claude-managed-agents-memory
