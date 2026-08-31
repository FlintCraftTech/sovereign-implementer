# Steering response length and one-at-a-time delivery — what actually works

Researched 2026-08-13, at Alex's request: she is fatigued by long Claude responses and
wanted to know what the most effective rules are for (a) stopping bundling and,
separately, (b) delivering detail less painfully. Sources are Anthropic's current
official guides plus the two earlier files in this folder.

Supersedes nothing. It **narrows** [opus-4-8-verbosity-steering.md](opus-4-8-verbosity-steering.md),
which was researched against Opus 4.8 and whose "quantified targets beat adjectives"
advice is 4.8-era; the Opus 5 guidance below is what governs the model this project
now runs on. It extends [opus-5-instruction-compliance.md](opus-5-instruction-compliance.md),
which established the subtraction principle but did not carry the specific levers.

## The single most important correction: length and narration are two different problems

Anthropic's Opus 5 guide treats them as separate sections with separate fixes, and the
project's output style only addresses one of them.

- **Response length** — how long a given message is.
- **Progress narration** — how often the model speaks at all during agentic work, and
  what it says before, during and after tool calls.

Long Claude Code sessions feel long mostly because of the *second*, and the current
output style has no instruction about it at all. This is the largest identified gap.

## Confirmed dead ends — do not spend work here

- **The effort parameter does not shorten visible output.** Official, explicit, and
  Opus 5 is named as the exception to the general rule: *"raising or lowering effort
  does not reliably change visible response length. Prompt explicitly for conciseness
  instead."* Lowering effort reduces thinking, not talking.
- **Restating the rule more times, or louder.** The one-at-a-time rule is currently
  stated in three separate layers — global CLAUDE.md, project CLAUDE.md, and the
  shipped output style — and it still slips. That is direct local evidence for the
  official line that volume is not the missing ingredient. It is also why
  [communication-rules-untestable-here] cannot be dismissed: the layers mask each
  other.
- **Negative instructions.** *"Tell Claude what to do instead of what not to do"* is
  stated as one of the few particularly effective formatting levers, in the positive
  direction. The current output style is roughly half negatives ("don't preview the
  later items", "never cram", a "Bad:" exemplar).

## The levers that are documented to work, in the order they are worth trying

### 1. A narration-cadence instruction (missing entirely today)

The official guide gives a ready-made one, quoted verbatim:

> Before your first tool call, say in one sentence what you're about to do. While
> working, give a brief update only when you find something important or change
> direction. When you finish, lead with the outcome: your first sentence should answer
> "what happened" or "what did you find," with supporting detail after it for readers
> who want it.

This describes *cadence and shape*, which is what the guide says the model responds to,
rather than an adjective. Nothing in the plugin currently says how often to speak.

### 2. A short conciseness instruction, plus a reminder near the END of the prompt

Also verbatim from the guide:

> Keep responses focused, brief, and concise. Keep disclaimers and caveats short, and
> spend most of the response on the main answer. When asked to explain something, give
> a high-level summary unless an in-depth explanation is specifically requested.

And the part that is easy to miss: *"In a long system prompt, pair the instruction with
a short reminder near the end of the prompt"* — a bare `<tone_preference>Keep outputs
reasonably concise.</tone_preference>`.

That applies here more than the wording suggests. The output style is appended to the
end of Claude Code's system prompt, but three further layers land after it — the
CLAUDE.md files, the session_start hook injection, and the skill procedure doc. By the
time the model acts, the concision instruction is a long way back. A tail reminder is
the documented answer and costs one line.

### 3. Written-deliverable length is a separate control, and nothing here targets it

*"Separate from conversational verbosity, files that Claude Opus 5 writes to disk
(reports, Markdown documents, summaries) are often longer than on prior models."* The
official fix:

> Match the length of written documents to what the task needs: cover the substance,
> but do not pad with filler sections, redundant summaries, or boilerplate.

This is worth flagging beyond Alex's original question. **Nearly everything this
project produces is a written deliverable** — LOG entries, queue rationale, the
procedure docs themselves. The corpus-growth problem the rule-lifecycle board's
MEASURED report exists to watch, and the bloat described in
[instruction-file-bloat-and-subtraction.md](instruction-file-bloat-and-subtraction.md),
may be partly a model default with a documented one-line countermeasure that has never
been tried. That is a hypothesis this file raises, not a finding it proves.

### 4. Positive exemplars beat descriptions — and this project already has the proof

*"Positive examples of the communication style you want tend to be more effective than
instructions about what not to do."* Examples are called *"one of the most reliable ways
to steer Claude's output format, tone, and structure."*

The local evidence is stronger than the citation. `plan.md`'s checkpoint is the one
place in this method where bundling was actually fixed, and it was fixed by showing a
specimen message — *"this is the shape of the message"* — followed by a flat statement
of what does not appear beneath it. Every other site states the rule in prose and the
rule keeps slipping.

**So the answer to Alex's bundling question is: there is no documented "stop bundling"
lever, and the working substitute is a shown specimen of a single message.** Say that
plainly rather than implying an official fix exists.

### 5. Markdown and bullet restraint — ASKED AND ANSWERED: do not apply this one

The guide carries a ready-made block for suppressing excessive markdown, on the
reasoning that bullets fragment information and that flowing prose reads better. That
was raised with Alex on 2026-08-13 rather than assumed, because fatigue at long
responses and fatigue at dense formatting feel identical from inside and have opposite
fixes.

**Her answer, in her own words: "the formatting helps".** The queue item was deleted
rather than built.

**This is a constraint on the other four builds, not a footnote.** The bold lead-ins,
short paragraphs and fenced blocks are load-bearing for a reader with a low
symbol-search score — they are how the point gets found without scanning prose. So a
concision pass must cut *length and narration frequency* and must leave *formatting
density alone*. Anthropic's markdown-suppression block is the one documented lever in
this file that is wrong for this user, and it should not be reached for later by a
session that reads the guide and not this paragraph.

## What does NOT transfer from the general LLM literature

Searches on "one step at a time" prompting return prompt-chaining research —
decomposing a *user's* request across turns to improve model accuracy. That is a
different problem in the opposite direction: it is about how the human should prompt,
not about getting the assistant to release its output in pieces. It should not be cited
as support for the one-at-a-time rule.

## Sources

- [Prompting Claude Opus 5 — Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
- [Prompting best practices — Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Prompting Claude Fable 5 — Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)
- [Output styles — Claude Code Docs](https://code.claude.com/docs/en/output-styles)
