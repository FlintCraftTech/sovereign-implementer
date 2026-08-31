# Skill content lifecycle — a skill invocation never ends another skill

Researched 2026-08-21, from Claude Code's own documentation, prompted by a
report that running `/rescan` inside a `/plan` session appeared to end that
planning session and force `/plan` to be run again.

**Source:** `code.claude.com/docs/en/skills`, the "Skill content lifecycle"
section, plus "Custom commands have been merged into skills" in the same page.

## The finding

**There is no such thing as a running skill, so there is nothing that can be
ended, exited or returned to.** The documentation's words:

> When you or Claude invoke a skill, the rendered `SKILL.md` content enters the
> conversation as a single message and stays there for the rest of the session.

Four consequences follow, and each one bears directly on the method's design.

**1. Invoking a second skill does not remove the first.** Both sets of
instructions are ordinary messages in the same conversation, so after `/rescan`
runs inside a `/plan`, `plan.md`'s content is still present and still governing.
Nothing was ejected.

**2. The documentation names this exact symptom and gives its cause.**

> If a skill seems to stop influencing behavior after the first response, the
> content is usually still present and the model is choosing other tools or
> approaches.

So a skill appearing to have "ended" is Claude's attention moving, not the
harness closing anything.

**3. Instructions meant to persist have to be written as standing instructions.**

> Claude Code does not re-read the skill file on later turns, so write guidance
> that should apply throughout a task as standing instructions rather than
> one-time steps.

A procedure written as a numbered march from Step 1 to a final step reads as
finished once the final step is done. That is an authoring property, not a
platform constraint.

**4. Re-invoking a skill is nearly free when nothing changed.**

> When Claude re-invokes a skill whose rendered content is identical to the copy
> already in context, Claude Code adds a short note that the skill is already
> loaded rather than a second copy of the content.

So "run `/plan` again" costs almost no context — but it is also unnecessary,
because the content never left.

## The one genuine limit

**Auto-compaction can drop a skill's content.** When the conversation is
summarised, Claude Code re-attaches the most recent invocation of each skill
after the summary, keeping the first 5,000 tokens of each, with all re-attached
skills sharing a 25,000-token budget filled newest-first. So in a chat that has
invoked several skills and then compacted, an older skill's content can be gone
entirely, and re-invoking it is the documented remedy.

That is the only case where a skill genuinely stops being present — and it is
unrelated to whether another skill was invoked.

## What this rules out, and what it leaves open

**Ruled out:** any design resting on the belief that a skill invocation is a
mode with a beginning and an end, that one skill can interrupt or suspend
another, or that a "return to the previous skill" mechanism would have to be
built. There is no state to return to because none was left.

**Left open:** how a procedure doc should end so the conversation does not read
as finished. That is a wording decision inside this project's own docs, not a
platform question, and the research says nothing about which wording works.

## Caveat on scope

This describes the documented behaviour of skill *content* in context. It says
nothing about whether Claude will in practice resume the earlier procedure —
only that the instructions for doing so are still there to be followed. The
documentation is explicit that this is a matter of the model's attention, which
is exactly what cannot be guaranteed by a doc.
