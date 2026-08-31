# Index + detail document architecture for AI agents

Filed 2026-06-17 while web-searching to inform the QUEUE.md restructuring design thread (the "make QUEUE.md easier to handle" capture / viable direction 3: keep the execution graph consolidated, move per-batch rationale to `plans/<slug>.md`). Search prompted by the capture's own "a web search on current index+detail doc-architecture patterns could inform it."

## Headline

The "consolidated index + on-demand detail" shape the user independently arrived at (from the LOG/FAQ track record) is an established, named pattern: **progressive disclosure**. The external critique's direction 3 is not novel or risky-by-itself — it's the mainstream agent-context pattern. The risk in SI's case is specific (the cross-referenced graph), not the pattern itself.

## What the pattern says (progressive disclosure)

Reveal information in layers, pulling deeper layers into context only when needed:
- **Layer 1 — Index:** titles / lightweight metadata, always available.
- **Layer 2 — Summaries:** 2–3 sentences.
- **Layer 3 — Full detail:** the complete entry, loaded only when relevant.
- **Layer 4 — Source:** the referenced code/files, loaded only if required.

This maps directly onto how Claude Code Skills already work (SKILL.md frontmatter always read at startup; body loaded when the skill is relevant; reference files loaded only when deeper detail is needed) — i.e. SI already lives inside this pattern at the skill layer. Applying it to QUEUE.md (index consolidated, per-batch rationale on demand) is the same move one layer down.

## The load-bearing caveat from the memory literature

Hierarchical/consolidated memory systems (MemGPT's OS-inspired layered memory; A-MEM; H-MEM) repeatedly stress: **keep the raw/detail linked to the consolidated index so compression doesn't lose detail.** This corroborates the why-pipeline worry in the capture — if per-batch rationale moves to `plans/<slug>.md`, the link from the consolidated graph to the detail must be reliable, and the approval flow (user co-reads/approves rationale) must be reconciled, not broken. The pattern works *because* the detail stays retrievable, not discarded.

These memory systems (vector stores, FAISS/SQLite, semantic retrieval) are runtime retrieval machinery, not human-readable doc files — so they don't transfer wholesale to SI's plain-markdown, human-co-read design. The transferable idea is architectural (index + linked detail + load-on-demand), not the storage tech.

## Bearing on the SI decision

- Direction 3 (consolidated graph in QUEUE.md, rationale to `plans/<slug>.md`) is the pattern-aligned choice. The literature supports it.
- The hard constraint stands and is unaddressed by the generic pattern: captures and deferred tests can block batches, so they're part of the cross-item graph and must NOT be split out — progressive disclosure splits *detail read alone*, never the *cross-referenced graph*. The user's own rule ("only per-entry detail that's read alone can safely move") is exactly the correct reading of the pattern.
- Suggested next step from the capture still holds: a small reversible experiment (convert 2–3 batches to index+detail, see if /next and /plan hold the thread) before any wholesale migration.

## Sources

- [Progressive Disclosure in AI Agents — MindStudio](https://www.mindstudio.ai/blog/progressive-disclosure-ai-agents-context-management)
- [Progressive disclosure — Claude-Mem docs](https://docs.claude-mem.ai/progressive-disclosure)
- [Progressive Disclosure Pattern — microsoft/agent-skills (DeepWiki)](https://deepwiki.com/microsoft/agent-skills/5.3-progressive-disclosure-pattern)
- [Agent Skills: Progressive Disclosure as a System Design Pattern — SwirlAI](https://www.newsletter.swirlai.com/p/agent-skills-progressive-disclosure)
- [A Practical Guide to Memory for Autonomous LLM Agents — Towards Data Science](https://towardsdatascience.com/a-practical-guide-to-memory-for-autonomous-llm-agents/)
- [MemGPT / hierarchical memory — A-MEM paper](https://arxiv.org/pdf/2502.12110)
