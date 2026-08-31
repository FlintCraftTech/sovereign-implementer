# Does instruction *format* affect rule adherence? — fresh literature check

Researched 2026-08-03 (web), to re-ground the open question in
[docset-b-register-decision-weaker-than-recorded]: our docset-B register decision
rejected typed pseudocode on the strength of one section read once, and the prior
research note (`pseudocode-format-for-skill-docs.md`) had already flagged that the
evidence base measured something other than what we care about. This check asks
whether anyone has since measured the thing we actually care about.

## The headline: nobody has tested our question directly

No study found tests **prose vs. pseudocode for standing behavioural rules** — the
governance case, where a document constrains how an agent behaves across all tasks
rather than telling it how to accomplish one. Every pseudocode result available is
measured on task accuracy or task completion. That is not a gap in our reading; it
is a gap in the field.

## What the pseudocode evidence actually measures

**Prompting with Pseudo-Code Instructions** (Mishra et al., EMNLP 2023) — the source
of the "+7–16 F1 / +12–38%" figures the earlier note quoted second-hand. Scope, now
confirmed: 132 tasks drawn from Super-NaturalInstructions (classification, QA,
generative), comparing pseudo-code instructions against natural-language ones.
Models: **BLOOM and CodeGen**. Two caveats that matter for us and were not visible
in the second-hand citation — these are 2023-era models, and CodeGen is a *code*
model, so a code-shaped prompt suits it in a way that says little about a frontier
instruction-tuned model. The measure is NLP task accuracy throughout.

**Skill-as-Pseudocode** (arXiv 2605.27955) — agent task completion on ALFWorld,
gpt-4o-mini. Already recorded in the prior note; the scope caveat stands.

So both pillars of the pseudocode case measure task outcomes, on models that are not
ours, and neither observes behavioural constraint adherence at all.

## What the field does say about format and adherence

- **Prompt formatting has a real, model-dependent effect** — *Does Prompt Formatting
  Have Any Impact on LLM Performance?* (arXiv 2411.10541). Format is not neutral, but
  the effect varies by model, so results do not transfer between models for free.
- **Structural delimiting is the better-evidenced lever for long, multi-section
  prompts.** Provider guidance (Anthropic, OpenAI, Google) converges on XML-style
  tags for complex prompts, on the reasoning that explicit section boundaries stop an
  instruction in one section being read as applying to another. Practitioner testing
  is consistent about *when*: no measurable difference on short, single-purpose
  prompts; the gains appear on long, multi-section prompts and untrusted input.
- **Agentic instruction-following fails hardest on format and style constraints** —
  AGENTIF (arXiv 2505.16944), which benchmarks constraint adherence in agentic
  scenarios across content, format, style and task-specific constraints. It does
  **not** test instruction format, but its failure profile matters: the constraint
  types models hold worst are precisely the kind SI's response-shape rules are.
- **IFEval and its successors supply the missing method.** IFEval formalised
  instruction-following as *verifiable* multi-constraint compliance — constraints
  objectively checkable by script ("at most N words", "include X exactly three
  times") rather than by judgement. Later work (M-IFEval, MCJudgeBench, AGENTIF)
  extends it to multi-constraint, multi-turn and agentic settings.

## What this changes for us

**1. The register decision now rests on less than we thought, in a new way.** The
prior note's caveat was that the evidence was measured on the wrong axis. This check
adds that it was also measured on the wrong models — BLOOM and CodeGen, one of them a
code model. So the case *for* pseudocode was weaker than assumed at the same time as
our case *against* it was weaker than logged. Both sides thinned; the question is
more open than either the LOG or the capture states.

**2. A re-test should measure, not read.** Our decision came from reading one section
and judging how it felt. IFEval's design is the correction: express SI's most-slipped
rules as script-verifiable constraints ("exactly one item per message", "the ask is
bolded", "no output at a [SILENT] step"), then run the same scenarios against a
prose docset and a pseudocode docset and count violations. That measures adherence
directly instead of inferring it from a read. It is also cheap — the constraints we
care most about are mechanically checkable, which is why the response-shape tags were
written the way they were.

**3. The real third option is structural delimiting, not pseudocode.** The framing has
been prose vs. pseudocode throughout. The better-evidenced intervention for a document
of SI's exact shape — long, multi-section, always loaded, mixing many independent
rules — is explicit section boundaries, and the evidence says the benefit appears
specifically in long multi-section prompts rather than short ones. `plugin-behaviour.md`
is markdown-sectioned today, not tag-delimited. This is a distinct, cheaper experiment
than a register change, and it does not require re-authoring the docset's voice.

**4. AGENTIF's failure profile predicts our own.** Independently of format, the
constraint types that models hold worst in agentic settings are format and style —
which is what SI's response-shape rules are. That is corroboration that the rules that
keep slipping here are hard for structural reasons, not because our wording is poor.
It also implies a format change alone is unlikely to fix them.

## Bearing on the safe-window argument

Unchanged and reinforced. A re-test is worth running while docset A still stands as
the known-good fallback. What changes is what a re-test should look like: a measured
constraint-violation count, not a second read, and with structural delimiting as a
third arm alongside prose and pseudocode.

Sources: [Prompting with Pseudo-Code Instructions (EMNLP 2023)](https://aclanthology.org/2023.emnlp-main.939/);
[Skill-as-Pseudocode (arXiv 2605.27955)](https://arxiv.org/abs/2605.27955);
[Does Prompt Formatting Have Any Impact on LLM Performance? (arXiv 2411.10541)](https://arxiv.org/html/2411.10541v1);
[AGENTIF (arXiv 2505.16944)](https://arxiv.org/pdf/2505.16944);
[M-IFEval (NAACL Findings 2025)](https://aclanthology.org/2025.findings-naacl.344/);
[MCJudgeBench (arXiv 2605.03858)](https://arxiv.org/pdf/2605.03858);
[XML tags and prompt length](https://dev.to/manishramavat/xml-tags-dont-help-short-prompts-heres-when-they-actually-matter-2026-25gf).
