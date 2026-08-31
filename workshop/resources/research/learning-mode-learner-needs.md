# Learning mode — what the evidence says about learners in AI-assisted coding

Researched 2026-08-08 during the /plan session that processed
[learning-mode-fork-at-setup]. Web findings; links at the bottom.

## 1. The audience is real and large

- A 2025/2026 survey (HostingAdvice) found **76% believe learning to code is
  still worth it in the age of AI**, and 48% name career advancement as a
  motivator; 45% were considering learning to code. The attachment the user
  described — people not ready to relinquish "one day I'll learn" — is the
  majority position, not a niche.
- The surrounding content economy splits exactly as the user described: a
  "you must understand your code or it explodes" camp (code-academy content)
  and a vibe-coding camp that treats reading code as optional. Beginners meet
  both messages at once.

## 2. The load-bearing finding: HOW you use AI decides whether you learn

Anthropic's own 2026 study (52 developers learning an unfamiliar Python
library, randomized AI vs docs-only):

- AI cohort scored **17 points lower** on a comprehension quiz (50% vs 67%)
  and saved no significant time.
- BUT the split inside the AI cohort is the design input: **those using AI
  for conceptual inquiry scored 65%+; those delegating code generation
  scored below 40%.**

Corroborated by CHI 2026 / arXiv work on novices with LLM assistants:

- Six distinct interaction patterns observed, comprehension ranging
  **24%–86%**. Delegation is the weakest pattern; **generate-then-actively-
  question is the strongest — and can beat coding without AI at all.**
- "Epistemic debt": accepting AI output without understanding accumulates
  like technical debt. Mitigations that test well are **metacognitive
  prompts** — being asked to justify/predict/explain — not longer
  explanations.
- Cognitive-load research: **verbal explanation alone does not reduce
  load**; explanation works when paired with structure (visual scaffolds,
  templates, directed attention). Implication: learning mode must not just
  mean "Claude explains more" — unprompted wall-of-text insights are the
  overwhelm failure, and passive explanation is the non-learning failure.

**Design consequence for the fork:** jargon-flow (the item's current seam) is
the *smallest* part of what makes a learning mode teach. The evidenced levers
are (a) conceptual Q&A — the user asking why, the mode inviting it; (b) small
active contributions by the learner; (c) prediction/justification prompts at
natural moments. Terminology exposure supports (a) but does not substitute.

## 3. Competitive landscape — nobody forks at onboarding; the harness already half-does

- **No mainstream vibe-coding tool asks "do you want to learn?" at setup.**
  Replit and Cursor have explain-this-code affordances and education
  positioning, but no learn-vs-build mode a beginner chooses once.
- **Claude Code itself ships the closest thing**: built-in output styles
  **Explanatory** (educational "insights" alongside work) and **Learning**
  (collaborative learn-by-doing — Claude leaves small `TODO(Human)` pieces
  for the user to write themselves). Saved per-project in settings.
- That is both a lever and a conflict for SI: **SI ships its own concise
  output style, applied automatically** — one style is active at a time, so
  a learning mode has to decide its relationship to the harness's Learning /
  Explanatory styles (adopt, wrap, or replace). This is a real mechanism
  question the design must settle, not positioning.

## 4. What "not overwhelming them" concretely means, from the evidence

- Insights short and attached to the work just done, not lectures.
- Active beats passive: one small question or contribution beats three
  paragraphs of explanation.
- The learner controls depth (ask-to-go-deeper), mirroring the method's
  existing gate-the-detail principle — which SI already does well and should
  not abandon in learning mode.
- Glossary fits as the memory layer: terms defined once at point of use,
  recorded, then usable — the same define-and-record mechanic, with learning
  mode introducing terms more freely.

## Sources

- [HostingAdvice: 3 in 4 say learning to code still important](https://www.hostingadvice.com/studies/coding-in-todays-world-report/)
- [the-decoder: AI coding tools hurt learning unless you ask why (Anthropic study)](https://the-decoder.com/ai-coding-tools-hurt-learning-unless-you-ask-why-anthropic-study-finds/)
- [InfoQ: AI coding assistance reduces skill mastery by 17%](https://www.infoq.com/news/2026/02/ai-coding-skill-formation/)
- [Stephen Turner: How AI assistance impacts the formation of coding skills](https://blog.stephenturner.us/p/ai-assistance-coding-skills-anthropic)
- [CHI 2026: From Black Box to Learning Artifact (novice patterns, 24–86%)](https://dl.acm.org/doi/full/10.1145/3772363.3798522)
- [arXiv: Mitigating "Epistemic Debt" in GenAI-scaffolded novice programming](https://arxiv.org/html/2602.20206v2)
- [BJET: GenAI coding hints, performance and cognitive load](https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13589)
- [Claude Code docs: Output styles (Explanatory, Learning, TODO(Human))](https://code.claude.com/docs/en/output-styles)
- [Walturn: Comparing Replit and Cursor](https://www.walturn.com/insights/comparing-replit-and-cursor-for-ai-powered-coding)
