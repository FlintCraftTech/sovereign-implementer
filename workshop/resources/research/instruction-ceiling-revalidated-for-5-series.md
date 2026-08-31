# The 150–200 instruction ceiling, re-validated against the 5-series

Researched 2026-08-12 at the user's instruction, during the /plan that was about to
process [board-reports-one-audience-not-two]. The question they asked: is the existing
ceiling research relevant to Opus 5 and Fable 5, and if not, re-run it.

Supersedes §1 of [`instruction-file-bloat-and-subtraction.md`](instruction-file-bloat-and-subtraction.md)
on the **number**. It does not supersede that file's other sections, and §2 and §3 in
particular survive intact — see "What did not change" below.

## 1. The finding, stated first

**The 150–200 figure is roughly an order of magnitude too tight for the models this
method targets.** The benchmark it came from was re-run a year later and frontier
models had improved about tenfold. The 2026 figures put meaningful degradation at
around 2,000 constraints, with the closest-tested Claude model beginning to fail
between 2,000 and 5,000.

Reported per model in the 2026 run:

```
DeepSeek V4 Pro    starts dropping instructions around N=750
Claude Opus 4.7    begins failing around N=2,000–5,000 (refusal errors)
Gemini 3.1 Pro     strong through N=5,000
GPT 5.5            99% accuracy through N=5,000
```

The benchmark's own vocabulary had to be expanded from 500 words to 10,000 because
frontier models exceeded the previous ceiling entirely.

## 2. Why the old number was not wrong when it was written

The 150–200 figure traces to the IFScale benchmark (Jaroslawicz et al., 2025), which
found nearly all models peaking around 150–200 instructions before selective attention
began favouring earlier ones. That was an accurate reading of the 2025 evidence. The
2026 authors state the change plainly: a year ago models lost track somewhere around
200–300 simultaneous constraints, and depending on the model that boundary is now
closer to 2,000.

So this is a superseded measurement rather than a mistaken one, which matters for how
the project treats it: the number was measured honestly and then the ground moved.

## 3. The caveat that stops this being a licence to grow

**Neither Opus 5 nor Fable 5 was tested.** The 2026 run covers DeepSeek V4 Pro,
Claude Opus 4.7, Gemini 3.1 Pro and GPT 5.5. Opus 4.7 is the nearest Claude data point
and it sits in the 2,000–5,000 band, but it is not our model and this file must not be
cited as if it were.

**And IFScale measures a different thing from what this method does.** Its task is
incorporating required keywords into a business report — many simultaneous, mutually
compatible, mechanically checkable constraints in a single generation. A method rules
corpus is behavioural instructions, competing for attention across a long agentic
session, many of which do not apply to the task at hand. A model that can hold 2,000
keywords is not thereby shown to follow 2,000 behavioural rules.

## 4. What did NOT change, and is now the load-bearing argument

The case for subtraction does not rest on the ceiling, and removing the ceiling leaves
it standing:

- **Irrelevant content causes wholesale dismissal, not selective filtering** (§2 of the
  prior file). A rule inapplicable to the current session taxes the rules that do apply.
  Nothing in the 2026 result addresses this.
- **Distractor interference** (§3) — semantically similar but irrelevant content is the
  worst case for attention, and a rules corpus is made of near-identical material. Also
  untouched.
- **Anthropic's own 5-series guidance is subtraction**, and is the most directly
  relevant evidence we have because it is about our actual models. The Opus 5 guide
  tells authors to *remove* verification instructions, self-correction prompting and
  legacy harness scaffolding, because they compound with built-in behaviour and cost
  tokens with no quality gain. The Fable 5 guide says skills built for prior models are
  often too prescriptive and can degrade output. See
  [`opus-5-instruction-compliance.md`](opus-5-instruction-compliance.md) and
  [`fable-5-instruction-compatibility.md`](fable-5-instruction-compatibility.md).
- One thing the Opus 5 guide adds that bears directly on a long rules file: its
  instruction following "stays consistent throughout" a 1M-token context window. That
  weakens a position-based worry, not a relevance-based one.

## 4a. A field observation from the user, and the qualification it needs

The user's own experience, given in their words when this research was reported
(2026-08-12): even when the docs were at their most bloated, Claude was doing an amazing
job of soldiering on. That is consistent with the finding above and is recorded as
corroboration.

**The qualification is Claude's, and it is why this is not filed as confirmation.**
Soldiering on is what a session looks like under either hypothesis. The failure the
research describes is not stopping or erroring — it is individual rules quietly not
firing while the session otherwise goes well. So a session that felt good is weak
evidence in the one direction that matters.

And this project holds direct counter-evidence from the same week: three correctly
worded, always-loaded rules that were read at session start and did not fire —
[subagent-ask-rule-slipped], [invented-rationale-compounds-past-the-shipped-rule] and
[write-first-report-without-write]. Each occurred in a session that was going fine. That
is what silent non-compliance looks like from the inside.

**The two claims to keep apart:** the corpus is not near a cliff (supported by both the
benchmark and the user's experience), and every rule is landing (contradicted by those
three). The case for eviction should be made on relevance, not on either count.

## 5. What this means for the project, as analysis rather than decision

Recorded for the /plan that will process it; the fate calls are not made here.

- The **200 ceiling in `resources/rule_signals.py` has lost its derivation.** It was
  built on the 150–200 figure, and that figure no longer describes our models. Under the
  project's own [derivation-required-for-limits] rule, a threshold with no live
  derivation is exactly what is banned — so the number cannot simply be left standing
  because it is conservative.
- **The MEASURED signal's readings should be re-read.** A consumer at 234 and this
  project at 330 were being reported as 17% and 65% over. Against the nearest current
  evidence, both are an order of magnitude *inside* the tested degradation band.
- **This does not make the eviction work pointless, and should not be used to cancel
  it.** The reasons to cut are now §2, §3 and Anthropic's 5-series guidance rather than a
  count — and those argue for removing *irrelevant and over-prescriptive* text, which is
  a different and better-targeted job than getting a number under 200.
- **The honest replacement may be no number at all.** A growth report with no threshold
  was already proposed for SPEC in [shipped-spec-maintenance-rules] and for the fetched
  docs in [fetched-docs-have-no-measure]; the same shape now has a stronger claim here,
  because no defensible threshold exists for our models and inventing one would be the
  bare-number failure the method bans.

## Sources

- [Models got an order of magnitude better at following instructions in one year — Arize AI](https://arize.com/blog/llm-instruction-following-benchmark-2026/)
- [How Many Instructions Can LLMs Follow At Once? (IFScale, Jaroslawicz et al. 2025)](https://arxiv.org/pdf/2507.11538)
- [Prompting Claude Opus 5 — Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
