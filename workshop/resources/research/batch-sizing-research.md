# Batch sizing research

Research into better sizing gates for work batches, given the constraint that each batch must complete within one context window lifecycle (compact after /next or /plan, clear after push).

## Key finding: attention budget, not token count

Model performance drops as simultaneous requirements increase. Even large-context models struggle when asked to satisfy many instructions at once. The constraint isn't raw token count — it's attention budget. Studies show that as you pile on more instructions or data into the prompt, the model's performance in adhering to each one drops significantly.

## Context utilization targets

- Aim for 60-80% context utilization rather than maxing out capacity.
- Progressive compaction at ~40% usage is recommended over waiting until context is full.
- In multi-step agent loops, tokens accumulate across turns — budgeting must treat the full run as the cost unit.

## Task decomposition principles

- Small, focused context beats one giant prompt.
- "One task focus" and "relevant info only" improve quality.
- Each TODO/unit should act as a mini-spec for a small task, keeping the AI focused.

## Possible better sizing gate

The current verification-burden gate (>5 testable things = too big) measures the wrong dimension. What matters is how many distinct concerns Claude needs to hold in mind at once during the build. Three related changes serving one goal is lighter than three unrelated changes.

A coherence test: "Can Claude explain the batch's purpose in one sentence? If describing it requires 'and' more than once, it's likely two batches." This naturally handles the context constraint because coherent work shares context (one set of files, one design goal) while incoherent work fragments it.

## Status

Parked. Current gates aren't causing failures yet, and a replacement needs more real usage data to validate.

## Sources

- [Context Engineering for AI Agents](https://machinelearningmastery.com/effective-context-engineering-for-ai-agents-a-developers-guide/)
- [How to Write a Good Spec for AI Agents](https://addyosmani.com/blog/good-spec/)
- [Claude Code Context Window Optimization](https://claudefa.st/blog/guide/mechanics/context-management)
- [Five Levels of AI Agent Autonomy](https://www.swarmia.com/blog/five-levels-ai-agent-autonomy/)
- [LLM Context Windows Explained](https://devtk.ai/en/blog/llm-context-window-explained/)
- [Context Length Optimization Guide](https://local-ai-zone.github.io/guides/context-length-optimization-ultimate-guide-2025.html)
