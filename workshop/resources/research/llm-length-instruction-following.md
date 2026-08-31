# Can a model write to a length target without measuring? — the external evidence

Researched 2026-08-15, at Alex's request, while processing
[log-entry-length-may-be-mirrored]. She and a friend had independently concluded
that "AI can't write to a word count — it guesses, writes, then measures", and
she did not want a method that makes Claude measure its own output constantly.
The question put to the search was whether that is right, and whether this
project is barking up the wrong tree by considering a length range at all.

Complements [response-length-and-bundling-steering.md](response-length-and-bundling-steering.md),
which carries Anthropic's *model-specific* guidance. This file carries the
*general* literature. They do not conflict — see "How the two fit together".

## The friend's claim is correct, and it is the field's named root cause

LIFEBench (arXiv 2505.16234; NeurIPS poster) evaluates length-instruction
following across 10,800 instances, 4 task categories, English and Chinese, at
targets from 16 to 8,192 words. Its stated core bottleneck:

> LLMs are unable to accurately recognize how many words they have generated.

That is the claim, confirmed as the mechanism rather than as a symptom. A model
estimates from the amount of text produced; it does not count. Secondary sources
add the qualifier that matters most here: **models measure short texts
accurately and lose that ability as length grows.**

## The failure direction is the OPPOSITE of what was feared

This is the finding that changes the design, and it was not what either of us
expected. Given an explicit length instruction, models

> often generate far too **short** outputs, terminate prematurely, or even
> refuse the request.

So the documented bias under a length instruction is **undershoot**, not
overshoot. Alex's own live observation matches it exactly and independently: the
Discord posts land at roughly 75% of the 2,000-character limit, "there or a
little above, every time." That is not luck and not a well-behaved edge case —
it is the benchmark's central result reproduced on this project's own output.

For a user whose stated problem is reading fatigue, a systematic undershoot is
the safe direction to fail in.

## Short targets work; the failures are at lengths this project never writes

> Most models reasonably follow short-length instructions but deteriorate
> sharply beyond a certain threshold.

Almost all models fail to reach vendor-claimed maximum output lengths, and this
holds even for long-context models, which counterintuitively do not improve.
Those failures live at thousands to tens of thousands of words.

**Every shape this project was considering governing is short** — a capture, a
work item's rationale, a LOG entry, an index line. All sit in the regime where
length instructions are reported to work reasonably, and where the model's own
length estimation is reported to be accurate. **The evidence against length
targets is evidence against them at 8K–32K words, and does not transfer to a
200-word artifact.** Do not cite the general "LLMs are bad at length control"
result as though it applied here; it is a claim about a different regime.

## Exact control is achievable and every method costs the thing Alex refused

Three families in the current literature reach *exact* length compliance, and
all three add machinery:

```
countdown markers /       explicit positional counting written into the prompt
  positional awareness    (arXiv 2410.07035, 2508.13805)
plan-and-write            structure-guided allocation before generating
                          (arXiv 2511.01807)
dynamic length feedback   generate, measure, regulate — training-free or
                          training-efficient variants (arXiv 2601.01768)
```

Each vastly outperforms naive prompting on exact-match length. Each is also, in
substance, "guess, write, then measure" — the loop Alex explicitly does not want
running on every write. **So exact compliance is available and is correctly
refused here; approximate compliance on short text is available for free.**

## How the two fit together, so a later session does not read them as opposed

> **This section's conclusion is CORRECTED further down — see "Where this leaves
> specimen-versus-number, corrected".** It reads "specimen first; a range is a
> backstop", and that was drawn too strongly. The corrected reading is that a
> two-tier word range is defensible as the primary lever for length. Marked here
> on 2026-08-16, after a planning session read this section, stopped, and
> proposed a design the correction below rules out.

Anthropic's Opus 5 guidance says a **positive exemplar** is one of the most
reliable ways to steer output shape, and that the 4.8-era "quantified targets
beat adjectives" advice no longer governs. The general literature says a
**length target on short text** is followed reasonably, with an undershoot bias.

These are not in tension. The exemplar is the stronger lever and the one with
local proof in this project (`plan.md`'s specimen is the only place bundling was
actually fixed). A range is the weaker lever that nevertheless works at these
sizes. The reading that follows: **specimen first; a range is admissible as a
backstop, not as the primary mechanism** — and if a range is ever declared, this
file is its derivation for the claim that it can be followed at all, while the
figure itself still needs a measurement of what a good specimen of that shape
actually needs.

## Which unit — words, not characters, and it is not close

Extended 2026-08-15 in the same session. Alex reasoned that since a model
estimates from the amount of text produced rather than counting, a **character**
range might be the more honest unit. The evidence says the opposite, and the
gap is large:

- **Character counting is near-chance.** Recent architectures fail character
  counting at close to a random baseline's 33% accuracy — this is a
  well-studied weakness with interpretability work behind it (arXiv 2604.00778).
- **Word counting is markedly better**, and models comply with word-length
  constraints more than with token-based ones, because word count sits closer to
  how the model processes text. Non-word-count numerical constraints —
  characters, sentences — are named as the unreliable class.

**So a declared range in this project is stated in WORDS.** Do not restate it in
characters on the intuition that characters are more primitive; that intuition is
backwards for a token-based model.

**Why the Discord case is not a counter-example.** Those posts run against a
2,000-**character** limit and land near 75% of it. That works because it is a
*ceiling to stay under*, not a target to hit, and because the undershoot bias
above keeps the model clear of it. A ceiling in the wrong unit is forgiving; a
target in the wrong unit is not.

## A two-tier range is a documented pattern, not an invention

Alex asked whether something more sophisticated than a two-number range exists —
her example: *"200–500 with an absolute upper limit of 700 before you consider
splitting into two separate work items."* It does, and that is close to its
canonical shape.

The literature distinguishes **hard** from **soft** constraints: a hard
constraint is explicitly verifiable with binary pass/fail validation, a soft
constraint is a gradient. Stating which is which is described as mimicking an
optimisation function — telling the model which rules are Pass/Fail and which are
Better/Worse. A soft target band plus a hard ceiling is exactly that pairing.

**The breach action is the part that answers this project's own repeal.** The
20% index-line cap was repealed because it fired on correct work. A hard tier
that names an *action* on breach — reconsider the shape, split the item — is
advisory rather than refusing, so firing on correct work costs a moment's thought
instead of blocking it. The action has to be authored per shape: "split into two
items" is meaningful for a work item and meaningless for a LOG entry.

**And the literature supplies a derivation method for the figure**, which is what
this project's bare-number ban actually requires. Researchers set target length
limits from the generation lengths of strong models — taking the minimum across
them — rather than choosing a number (arXiv 2406.17744). The local analogue is
exact: derive the band from measuring this project's own *good* specimens of each
shape, which is what [log-entry-length-may-be-mirrored] does.

## Where this leaves specimen-versus-number, corrected

The earlier reading in this file — specimen first, range as backstop — was drawn
too strongly, and the correction matters. **Anthropic's exemplar guidance, and
this project's local proof of it, are about SHAPE, not length.** `plan.md`'s
specimen fixed *bundling* — what appears in a message and in what order. Nothing
here shows an exemplar is the better lever for *length* specifically, and the
general literature shows a numeric target working on short text.

They govern different properties. A specimen also costs what a range does not:
it is doc text in an always-loaded corpus, and this project's own rule gate names
worked examples as the growth engine. It additionally dictates structure and
appearance, which is more than a length decision needs to settle.

**So: a two-tier word range is defensible as the primary lever for length, and
the exemplar argument does not defeat it.**

## What this does NOT establish

That a range would hold over time; that is drift, and nothing here measures it.
That the mirroring hypothesis is true — this file says nothing about whether
length is inherited from what is in view, which is what
[log-entry-length-may-be-mirrored] exists to measure. And no figure of any kind:
the literature establishes that short targets are followable, never what the
right target is for any of this project's shapes.

## Sources

- [LIFEBench: Evaluating Length Instruction Following in Large Language Models](https://arxiv.org/abs/2505.16234)
- [PositionID: LLMs can Control Lengths, Copy and Paste with Explicit Positional Awareness](https://arxiv.org/pdf/2410.07035)
- [Prompt-Based One-Shot Exact Length-Controlled Generation with LLMs](https://arxiv.org/html/2508.13805v1)
- [Plan-and-Write: Structure-Guided Length Control for LLMs without Model Retraining](https://arxiv.org/html/2511.01807)
- [Can LLMs Track Their Output Length? A Dynamic Feedback Mechanism for Precise Length Regulation](https://arxiv.org/html/2601.01768v1)
- [Length Controlled Generation for Black-box LLMs](https://arxiv.org/pdf/2412.14656)
