# What a spec is expected to contain, and whether this project's SPEC is the document the tools expect

Researched 2026-09-06 at a planning session, on the user's request as the first step of the spec-free question raised there: before deciding whether builds stop reading SPEC, find out what a spec is supposed to contain and whether we are doing it the way Claude would expect. Read alongside `spec-document-standards.md` (2026-08-12), which settled that there is no length standard and that this SPEC carries implementation description; this finding asks the narrower question of shape and consumption. Findings are Claude's.

## 1. What Anthropic's own documentation means by SPEC.md

Claude Code's best-practices page uses the exact filename this method uses, and means something different by it. The recipe: for a larger feature, have Claude interview you, "then write a complete spec to SPEC.md", and "once the spec is complete, start a fresh session to execute it. The new session has clean context focused entirely on implementation, and you have a written spec to reference." On what it should carry: "The most useful specs are self-contained: they name the files and interfaces involved, state what is out of scope, and end with an end-to-end verification step that proves the feature works."

So Anthropic's SPEC.md is a per-feature implementation brief: files, interfaces, scope boundary, verification step, consumed by one fresh session. That is this method's kept work item — the Files line, the observation, the refused options — not this method's SPEC.md.

The same page's governing constraint bears on a whole-document read at run start: "Most best practices are based on one constraint: Claude's context window fills up fast, and performance degrades as it fills." And on always-loaded text: "Bloated CLAUDE.md files cause Claude to ignore your actual instructions!" with the test "for each line, ask: would removing this cause Claude to make mistakes? If not, cut it."

Source: [Claude Code best practices](https://code.claude.com/docs/en/best-practices), read 2026-09-06.

## 2. What the spec-driven tools put in a spec

GitHub Spec Kit's spec template, the most-copied shape, has five sections: user scenarios and testing (user stories "PRIORITIZED as user journeys ordered by importance", each "INDEPENDENTLY TESTABLE" with Given/When/Then acceptance scenarios), requirements ("System MUST [specific capability]", numbered, with `[NEEDS CLARIFICATION: …]` markers for gaps), success criteria ("technology-agnostic and measurable"), key entities where data is involved, and assumptions. The guidance: focus on what users need and why, avoid how, written for stakeholders rather than developers. Durable project rules go in a separate constitution, and every plan runs a constitution check against it.

Two structural facts matter more than the section list. A Spec Kit spec is **per feature**, living at `specs/###-feature-name/spec.md`, not one document for the product. And it is written to be **tested against**: each story has acceptance scenarios, and the success criteria are measurable.

Sources: [spec-template.md](https://github.com/github/spec-kit/blob/main/templates/spec-template.md), [spec-driven.md](https://github.com/github/spec-kit/blob/main/spec-driven.md), read 2026-09-06.

## 3. What the field says about agents not following a spec

Nobody claims a spec is followed because it exists. Thoughtworks is quoted rejecting the view that "specs alone suffice"; the recurring statement is that a spec read by humans and a spec that "executes as validation gates" are different things, and adherence comes from the second.

The June 2026 paper "The Spec Growth Engine" (arXiv 2606.27045) names the two failure modes directly: **context explosion**, where agent quality degrades as it reasons over a whole repository, and **silent spec-code drift**, where code evolves and the spec does not. Its answer to both is the same shape: a machine-readable spec graph with a "Spine context assembler" that "limits agent reasoning to specific ownership paths rather than the full codebase", so the implementing agent reads only the slice of spec its task touches, plus a "drift gate" that makes spec-code divergence "a blocking merge condition".

Sources: [arXiv 2606.27045](https://arxiv.org/abs/2606.27045), [DEV: SDD in 2026](https://dev.to/krlz/spec-driven-development-in-2026-what-it-is-the-tooling-and-how-teams-actually-use-it-2fk2), [Augment Code guide](https://www.augmentcode.com/guides/what-is-spec-driven-development), read 2026-09-06.

## 4. This project's SPEC against that

- **Shape.** One product-wide document of about 98KB, mostly prose paragraphs describing how mechanisms behave, with no per-feature units, no acceptance scenarios, no measurable success criteria and no scope boundaries per feature. Nothing in the field expects an implementer to read a document of this shape.
- **Consumption.** /next reads it whole at run start. Every source read here treats that as the failure to avoid: Anthropic on context filling, the paper on context explosion, Spec Kit by making the spec per feature so a task reads only its own.
- **Where the expected spec actually lives here.** The kept work item already carries what Anthropic's SPEC.md and Spec Kit's spec carry: files, what changes inside them, an observation that shows it landed, refused options, rests-on facts. The usage audit's zero-scoring builds (`spec-usage-versus-maintenance.md`) are consistent with this: a build whose item already carries its brief has nothing to take from a product document.
- **What SPEC does that nothing else here does.** It carries the long-term direction and product truth no item holds yet, and planning decides against it in every sampled session. That is the constitution-plus-product-truth role, which every tool keeps separate from the implementing brief and consults at planning, not at implementation.
- **Drift.** The method's drift control is the planning close's spec-sync gate and the build's file-a-contradiction rule, both judgment. The field's answer is mechanical: a gate that blocks a merge. The one mechanical piece here is the lift-time SPEC grep shipped 2026-09-06.

## 5. What this settles and what it does not

It settles that a build reading a 98KB product document whole is not the pattern any of the tools or Anthropic's own guidance prescribe, and that the document those sources call a spec is this method's work item. It does not settle whether removing the run-start read costs anything: three of eight sampled builds did decide on a SPEC sentence, and the spec-driven-development finding of 2026-06-25 rests on the spec being read at implementation time. What would settle that is the experiment the user proposed, or a per-item slice of SPEC handed to the build in place of the whole.

## Frame assessment

- **TIME RANGE** — not applicable; the product has no period.
- **PEOPLE** — the sources describe engineers using agentic tools; the method's users are no-code developers, whose spec is more likely to be the only written statement of intent, which weighs toward keeping the product document even if builds stop reading it.
- **FRESHNESS** — Anthropic's page and Spec Kit's template both change on no schedule; read 2026-09-06 and worth re-reading before a shipped rule cites either.
- **RISK IF WRONG** — wrong about the field: builds lose a read that three of eight used, recoverable by restoring one line in next.md. No red flag.
- **ALTERNATIVES** — reading more tools (Kiro, OpenSpec, BMAD) was not done; Spec Kit was taken as representative because the earlier finding named it as the shape the others share. Not ruled out, merely unread.
