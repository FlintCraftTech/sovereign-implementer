# Writing long agent documentation: avoiding additive noise, and how to subtract

**Superseded by: resources/research/instruction-ceiling-revalidated-for-5-series.md (2026-08-12)** — in part, not wholly. Section 1's figure of roughly 150–200 instructions was re-validated against the 5-series and found roughly an order of magnitude too tight. **Anything scoped against that number needs its premise re-read.** The rest of this file — the relevance argument, near-identical rules as optimal distractors, and the subtraction techniques — was not challenged and stands.

Researched 2026-08-09, after the emergency revert caused by plugin-behaviour.md growing
from 6,162 to 21,445 words. Question asked: what are the best guidelines for writing long
documentation for Claude, focused on avoiding additive noise and making correct
subtractions and distributions?

## 1. The ceiling is a count of instructions, not a token budget

Frontier models reliably follow **roughly 150–200 instructions** before compliance starts
degrading. Claude arrives with roughly 50 of its own, leaving on the order of 100–150
before performance declines.

The consequence is the one that matters here: **past a certain size, adding an instruction
causes the model to follow fewer of them.** Additions are not neutral — they are paid for
out of the compliance of every rule already present. A method with several hundred
behavioural rules is past the ceiling, and each well-argued addition is silently
subtracting reliability from the rest.

## 2. Irrelevant content causes wholesale dismissal, not selective filtering

The most consequential finding, and the least intuitive. Non-relevant content does not get
neatly skipped while the relevant rules still land. It degrades the model's treatment of
**all** instructions in the file. A rule that is merely inapplicable to the current session
is not free; it is actively taxing the rules that do apply.

This kills the standard defence of an added rule — "it costs a few tokens and might help
one day." It does not merely cost tokens. It costs the reliability of its neighbours.

## 3. Context rot: three mechanisms, and the one that fits a rules file

Model accuracy degrades **non-linearly** as input grows, and degrades well before the
window is full — measured drops of 30–50% across 18 frontier models (Chroma, July 2025),
including the Claude 4 family. Three compounding mechanisms are named:

- **Lost-in-the-middle attention gaps** — material in the middle of a long input is
  attended to least.
- **Attention dilution** — a fixed attention budget spread across more tokens, so any one
  sentence becomes statistically less significant.
- **Distractor interference** from *semantically similar but irrelevant* content.

The third is the one that fits a behavioural-rules document precisely. Two hundred rules
that all sound alike — all about narration, asking, scoping, capturing — are not merely
long. They are optimal distractors for one another. Similar-but-not-applicable is the worst
case, and it is exactly what a large rules file is made of.

## 4. Anthropic's own framing: minimality is the goal, not a constraint on it

Anthropic's context-engineering guidance sets the target as finding "the smallest possible
set of high-signal tokens that maximize the likelihood of some desired outcome," and
striving for "the minimal set of information that fully outlines your expected behavior."

On altitude, it names a Goldilocks zone: "specific enough to guide behavior effectively,
yet flexible enough to provide the model with strong heuristics." It warns explicitly
against "hardcoding complex, brittle logic in their prompts to elicit exact agentic
behavior. This approach creates fragility and increases maintenance complexity over time."

The recommended *direction of travel* is the opposite of this project's habit: "start by
testing a minimal prompt... then add clear instructions and examples to improve performance
based on failure modes." Minimal first, add only against an observed failure. Notably, the
guidance does not address curating or removing existing instructions at all — subtraction
is under-specified in the source material, which is why this project has to define it.

## 5. Anthropic's skill-authoring guidance: admission control, stated plainly

- "The context window is a public good. Your Skill shares the context window with everything
  else your agent needs to know."
- "Agents are already very smart. **Only add context agents don't already have.**"
- Challenge every piece with: "Does the agent really need this explanation?" and "Can I
  assume the agent knows this?"
- Avoid over-explaining, especially for more capable models: "what works perfectly for more
  powerful models might need more detail for less capable ones."
- "Assume competence: treat agents as intelligent; provide guidance, not tutorials."
- Eliminate time-sensitive content; keep deprecated material in an "old patterns" section
  rather than inline.
- Keep a SKILL.md body **under 500 lines**.

**Degrees of freedom — match specificity to fragility**, which is the principle for deciding
how prescriptive to be rather than defaulting to maximum prescription:
- *High freedom* (prose instruction) when multiple approaches are valid.
- *Medium freedom* (pseudocode with parameters) for a preferred pattern with acceptable
  variation.
- *Low freedom* (a specific script) when the operation is fragile and consistency is
  critical.

## 6. Sizes observed to work, from repository analysis

From analysis of 2,500+ repositories using AGENTS.md:
- Median well-performing file: **300–350 words**.
- Beyond **500 words**: diminishing returns.
- Beyond **1,000 words**: *negative* correlation with agent performance.

For CLAUDE.md specifically, recommended 40–80 lines, with under 100 a reasonable upper
bound; other sources say under 300 lines, ideally under 100, and one team keeps theirs
under 60.

Calibration for this project: plugin-behaviour.md at its birth (6,162 words) was already
six times the size at which the correlation turns negative. At 21,445 it was twenty-one
times. The revert restored it to the smaller number, which is still far past the
threshold — so the revert bought room, not health.

## 7. The structural fix repeatedly named: point, don't contain

The single structural change credited with the biggest improvement: "CLAUDE.md stopped
containing information and started pointing to it." The resulting file is a short statement
of what the project is, what the agent's scope is, and **a routing table saying where the
details live.**

This is a *distribution* answer rather than a subtraction one, and the distinction matters:
moving a rule out of an always-loaded file into an on-demand one removes its distractor
cost from every session that doesn't need it, without deleting the rule.

Caveat this project has already established, and which limits the move: progressive
disclosure works for material fetched on a trigger, and fails for standing behavioural
rules, because a session does not know to go and fetch a rule it has never read. So
routing is correct for reference material and wrong for the standing rules — which is most
of what plugin-behaviour.md holds. Distribution alone will not save it.

## 8. Pruning: the diagnostic questions

The recommended review is diagnostic rather than comprehensive — the four questions asked
of each existing rule:

1. **Does Claude follow this rule without being told?** (If yes, it is dead weight.)
2. **Does it apply to only some tasks?** (If so, it does not belong in an always-loaded file.)
3. **Could a tool enforce this instead?** (A hook costs no attention budget.)
4. **Has Claude actually violated this recently?** (If it has not been relevant in months,
   it is dead weight.)

Plus the staleness question: **is this still true?** — stale facts being worse than missing
ones, because they are confidently wrong.

Cadence suggested: a short monthly pass, a longer quarterly one.

## 9. What this implies for the project's own authoring document

Recorded as analysis, not as a decision — the design pass is the work item.

The existing `resources/authoring-heuristic.md` has seven checks. Six of them either add
text (quantify the target, show an exemplar, state the scope in words, name the pattern
with its replacement) or resist removal (guard against over-terseness). Every one is sound
advice for a single rule, and collectively they are a growth engine: each addition passes
its checks honestly, and the file grows anyway.

More decisively, **not one of the seven asks whether a rule should exist at all**, or what
comes out to make room for it. It is a quality filter with no admission control and no
eviction policy, applied to text someone has already decided to add. That is consistent
with it having been in force throughout the growth it failed to prevent.

The research supplies exactly what it lacks: an instruction *count* ceiling (§1), a reason
additions are not neutral (§2), admission tests (§5), eviction tests (§8), and a
distribution mechanism with a known limit (§7).

## Sources

- [Effective context engineering for AI agents — Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Anthropic skill-authoring best practices (mirrored)](https://github.com/obra/superpowers/blob/main/skills/writing-skills/anthropic-best-practices.md)
- [Your CLAUDE.md Is Probably Too Long — TianPan.co](https://tianpan.co/blog/2026-02-14-writing-effective-agent-instruction-files)
- [Context Rot: Why LLMs Degrade as Context Grows — Morph](https://www.morphllm.com/context-rot)
- [Context rot explained — Redis](https://redis.io/blog/context-rot/)
- [Your CLAUDE.md Is Too Long — Florian Bruniaux](https://www.florian.bruniaux.com/blog/articles/your-claudemd-is-too-long/)
- [Writing effective tools for AI agents — Anthropic](https://www.anthropic.com/engineering/writing-tools-for-agents)
