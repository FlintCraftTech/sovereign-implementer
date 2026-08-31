# Model instruction compliance across Opus 4.6 / 4.7 / 4.8

Researched 2026-06-10. Triggered by user observation that 4.7 and 4.8 don't follow the plugin's structured procedures reliably — verbose, skip silent/brief tags, bundle items that should be sequential.

## Opus 4.6 degradation (confirmed)

Anthropic published an engineering postmortem (April 23, 2026) confirming three overlapping harness-level changes caused the quality drop — not model nerfing:

1. **Reasoning effort downgrade** (March 4 – April 7): default effort changed from `high` to `medium` to reduce latency.
2. **Thinking cache bug** (March 26 – April 10): optimization bug cleared thinking on every turn instead of only after idle.
3. **Verbosity system prompt** (April 16 – April 20): 25-word cap between tool calls caused 3% intelligence drop on evals.

All fixed by April 20 (Claude Code v2.1.116). Separately, an RLHF safety update caused agentic performance spillover. Same degradation pattern repeated with 4.7 after launch. No evidence of further 4.6 degradation after 4.8 shipped (May 28).

External validation: AMD senior director filed GitHub #24991 with telemetry from 6,852 sessions showing measurable drop (92/100 to 38/100). BridgeMind, Artificial Analysis, VentureBeat, Fortune, Axios all covered it.

## The priority architecture finding

Skill docs and CLAUDE.md are delivered at **user-message priority**, not system-prompt priority. The built-in system prompt wins when they conflict. This is why [SILENT] and [BRIEF] tags don't hold on newer models — the system prompt's helpfulness/thoroughness directives outrank a skill doc saying "say nothing here."

Source: Support Tools analysis of Claude Code's prompt architecture.

**Correction (2026-06-15):** the premise that the system prompt mandates thoroughness over brevity is partly wrong — Anthropic's consumer system prompt actually instructs conciseness, and Opus 4.8's length is task-complexity calibration, not a thoroughness mandate. Verbosity is steerable with positive, quantified, exemplified instructions and an output style at system-prompt priority. See [opus-4-8-verbosity-steering.md](opus-4-8-verbosity-steering.md).

## Techniques for 4.7/4.8 compliance (ranked by likely impact)

1. **Move mechanical enforcement to hooks.** Hooks are deterministic — Claude can't skip them. Anything that must happen (scan before recommend, read before edit) should be a hook gate.

2. **Add "why" to behavioral tags.** `[SILENT] — this step produces intermediate data the user should never see` gives the model a reason to comply that aligns with helpfulness training instead of fighting it.

3. **Positive quantified constraints.** "Output zero text at this step" beats "be silent." "Deliver exactly one item, then stop and wait for user input" beats "one at a time."

4. **Explicit scope statements.** "This rule applies to every output in this skill execution, with no exceptions" — 4.7/4.8 are more literal and don't carry implied scope.

5. **Keep skill docs under 500 lines** with progressive disclosure. Anthropic's skill authoring guide says this.

6. **Effort level is critical.** Anthropic says effort matters more for 4.8 than any prior Opus. `xhigh` recommended for agentic work.

## 4.7/4.8 behavioral shift

4.6 inferred intent and filled gaps. 4.7/4.8 follow instructions literally. "Clean up this email" means grammar/formatting only unless you explicitly say to reorganize. This literalism cuts both ways — precise instructions land better, but implied scope and abstract behavioral tags land worse.

## Known unresolved issue

GitHub #65951 confirms Opus 4.8 still skips user-defined multi-step workflows. Community notes: "task completion takes priority over process compliance." This is a known, unresolved behavioral pattern.

## Sources

- Anthropic April 23 postmortem: anthropic.com/engineering/april-23-postmortem
- Anthropic prompting best practices: platform.claude.com/docs/en/build-with-claude/prompt-engineering
- Anthropic skill authoring best practices: platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Anthropic Opus 4.8 what's new: platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8
- Support Tools prompt architecture analysis: support.tools/claude-code-system-prompt-behavior-claude-md-optimization-guide
- MindStudio 4.7 prompting guide: mindstudio.ai/blog/how-to-prompt-claude-opus-4-7
- MindStudio 4.8 prompting guide: mindstudio.ai/blog/how-to-prompt-claude-opus-4-8
- GitHub issues: #24991, #53459, #65951, #32295
