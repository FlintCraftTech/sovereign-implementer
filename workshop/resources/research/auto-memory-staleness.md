# Auto-memory staleness — is Claude Code's memory system harming us?

**Date:** 2026-06-09
**Question:** Are the entries in `~/.claude/projects/.../memory/` injecting stale or wrong context into sessions in a way that's degrading planning quality?

## Re-verified 2026-08-15 — one paragraph below has fallen

Re-checked before drafting [competition-comparison-article], because the finding is two months old and the article makes claims about third parties. **The staleness finding itself stands unchanged.** Two things below are now wrong:

**AutoDream is live, and the "we don't have it running" sentence is false.** It consolidates between sessions — merging new facts, deleting contradicted notes, converting relative dates to absolute ones, trimming the index — and it triggers automatically after roughly 24 hours plus at least five sessions of new activity. It was introduced in March 2026 and is on a gradual rollout, but **a manual `/dream` command is available to everyone**, so the consolidation is reachable regardless of rollout state. A cycle runs about 8–10 minutes. That means the manual-cleanup conclusion at the bottom of this file is no longer forced, and any comparison claiming automatic consolidation is something only competitors have is wrong.

**"Obsidian memory systems" is a category, not a project, and must not be described as one thing.** There are many independent implementations — vault-as-memory guides, several separate open-source projects offering things like hybrid semantic search, self-rewriting notes and scheduled maintenance agents, and a Claude Code skill distributed through a marketplace. Obsidian's own official Agent Skills, released January 2026, teach Claude Code to handle wikilinks, frontmatter, Bases and JSON Canvas correctly. So a comparison must either name the specific project it is comparing against or describe the general vault-as-memory pattern and say that is what it is doing.

## Re-verified 2026-08-23 — one claim above is now too strong

Re-checked before drafting [competition-comparison-article], eight days after the
block above, because the article rests on both of its claims.

**The Obsidian finding stands, and is reinforced.** "Obsidian memory systems" is
still a category rather than a project, and the search turned up further
independent implementations (`obsidian-second-brain`, now at 45 commands and
citing 408 forks; `claude-obsidian-memory`; `claude-code-memory-setup`) alongside
the ones already listed. The article must still name a specific project or say
plainly it is describing the general vault-as-memory pattern.

**"A manual `/dream` command is available to everyone" has fallen.** Two sources
now say the command itself is still behind the gradual rollout — "the `/dream`
command exists but hasn't rolled out to everyone yet", and a second describing it
as shown in the `/memory` UI but absent from the base release. Third parties are
shipping plugins and skills that replicate it, which is itself evidence it is not
universally reachable.

**What survives, and it is the part the article needs.** Consolidation is still
reachable by every user — by asking Claude for it in plain words ("dream",
"consolidate my memory files") rather than by a command — and AutoDream is
Anthropic's own feature, introduced March 2026. So the article's concession holds:
automatic curation ships in the base tool and is not something only competitors
have. What the article must **not** say is that everyone has a `/dream` command.

**Sources are conflicting rather than settled**, and this section says so instead
of picking a winner: the rollout is gradual, so availability legitimately differs
between accounts and any single report is true of whoever wrote it.

## Finding

Yes, this is a recognised failure mode of Claude Code auto-memory as of 2026 — not a one-off. Auto-memory accumulates well but doesn't curate itself: snapshots of project state ("V47 promoted X," "ideas scoped to V51/V52") rot fast because the underlying state moves while the memory doesn't. Behavioural/preference memories don't have this problem and stay durable.

Anthropic's own remedy is **AutoDream**, a background sub-agent that consolidates memory between sessions — replacing vague time refs with exact dates and resolving contradictions. ~~We don't have it running, so cleanup is manual.~~ **Corrected 2026-08-15 — see the re-verification above: it is live and `/dream` is available manually to everyone.**

## Pattern (what goes stale vs. what doesn't)

| Memory shape | Goes stale? | Why |
|---|---|---|
| Project-state snapshot (queue contents at a moment, version-specific scope claims) | Yes, fast | Queue and version state move; the memory is frozen |
| Time-relative references ("yesterday," "last week," "now scoped V51/V52") | Yes | Lose meaning past their window |
| Behavioural feedback ("don't fire a modal over prose," "use tags not prose") | No | Preferences don't decay with project state |
| Reference pointers (where bugs live, what dashboard to check) | Slow | Decay only if the external system moves |

## Implication for this project

Of the eight memory files indexed in `MEMORY.md` at the time of this research:
- Six behavioural feedback files — durable, keep.
- `project_v47-oq-promotion.md` and `ideation-research-and-build-log.md` — both are version/queue snapshots from V47 and V51/V52. Target is at v1.9.0 with no current OPEN-QUESTIONS structure. These are the textbook failure mode and should be deleted, not relied on.

Going forward: avoid writing project-state snapshots into memory at all. The queue itself is the source of truth for "what's planned." Memory is for behaviour, preferences, and external pointers — not for caching queue contents.

## Sources

- [Claude Code Memory Guide (2026): CLAUDE.md vs Auto Memory vs Plugins](https://blog.laozhang.ai/en/posts/claude-code-memory)
- [Automatic Memory Is Not Learning — Brent W. Peterson](https://medium.com/@brentwpeterson/automatic-memory-is-not-learning-4191f548df4c)
- [Claude Code Memory System Explained — Milvus Blog](https://milvus.io/blog/claude-code-memory-memsearch.md)
- [Persistent Memory Across Context Compactions — anthropics/claude-code#34556](https://github.com/anthropics/claude-code/issues/34556)
- [Claude Code AutoDream: Memory Consolidation for AI Agents](https://zenvanriel.com/ai-engineer-blog/claude-code-autodream-memory-consolidation-guide/)

### Added at the 2026-08-15 re-verification

- [Claude Code Auto Dream Explained: Memory Like REM Sleep](https://decodethefuture.org/en/claude-code-auto-dream-explained/)
- [Auto Memory and Auto Dream: how Claude Code learns and consolidates its memory](https://antoniocortes.com/en/2026/03/30/auto-memory-and-auto-dream-how-claude-code-learns-and-consolidates-its-memory/)
- [Claude Code Auto-Dream Explained: How AI Organizes Its Memory While You're Away](https://claudelab.net/en/articles/claude-code/claude-code-auto-dream-memory-consolidation-guide)
- [Anthropic introduces dreaming for Claude agent memory consolidation](https://letsdatascience.com/news/anthropic-introduces-dreaming-for-claude-agent-memory-consol-32a279c9)
- [obsidian-memory-for-ai](https://github.com/jrcruciani/obsidian-memory-for-ai)
- [ai-memory-vault](https://github.com/jaredrhod/ai-memory-vault)
- [obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)
- [obsidian-mind](https://github.com/breferrari/obsidian-mind)
- [Obsidian Memory System — Claude Code skill listing](https://mcpmarket.com/tools/skills/obsidian-memory-system)
- [Stop Calling It Memory: The Problem with Every "AI + Obsidian" Tutorial](https://limitededitionjonathan.substack.com/p/stop-calling-it-memory-the-problem)
