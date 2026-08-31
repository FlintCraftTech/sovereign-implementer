# Prior art: the always-loaded universal behaviour doc

Researched 2026-08-10, during the /plan session processing [retire-plugin-behaviour-doc].
Question asked: has anyone else built an always-loaded universal behaviour document, does it
require the constant audit-and-eviction maintenance this project has ended up doing, and is
the pattern sound?

## Finding 1 — the pattern is not novel; it is the ecosystem default

`CLAUDE.md` and `AGENTS.md` are exactly this artifact: one always-loaded file of
cross-cutting behavioural instruction. Every Claude Code and Codex user has one. The method's
`plugin-behaviour.md` is a second, larger instance of the same shape layered on top.

## Finding 2 — it fails the same way for everyone, and the failure is documented

The reported failure mode matches this project's history closely enough to be quotable:
a rule is disobeyed, so a clearer version is added; a different rule is disobeyed, so that
one is added too; weeks later the file is hundreds of lines and the model follows fewer
rules than before. Multiple independent write-ups describe accretion with no removal, and
state the mechanism plainly: past a certain size, more instructions produce *less*
compliance, because the model underweights rather than filters.

This corroborates `resources/research/instruction-file-bloat-and-subtraction.md` from an
independent direction — the ~150–200 instruction ceiling is the same phenomenon measured.

## Finding 3 — the consensus remedy is size, not retirement

Nobody recommends deleting the universal file. The published advice is consistently:

- keep the always-loaded file small (commonly cited targets: under 200 lines, ideally
  under 100; one team cited at 60)
- treat pruning as the file's primary ongoing maintenance, not an occasional tidy
- move everything else into either per-concern rules files or on-demand skills

So the direction of travel is: a *small* universal file plus distribution — which is the
narrow re-scope option, not full retirement, and not the status quo either.

## Finding 4 — the split alone does not save context, and this is the trap

One practitioner report: an 80-line CLAUDE.md plus twenty auto-loaded rules files averaging
60 lines each = ~1,200 lines of behavioural instruction active every session. Splitting one
big always-loaded file into many small always-loaded files buys organisation and nothing
else.

What buys context back is **on-demand loading** — the progressive-disclosure model, where
only a name and one-line description sit in context at startup and the body loads when the
work actually calls for it. That is precisely the method's own fetched-doc mechanism, and
it is the half that matters. Distribution into skill docs is only a saving because skill
docs are fetched.

## Finding 5 — the audit machinery IS this project's invention, and that is the tell

No prior art was found for what has grown up around this doc: admission gates, eviction
policy, instruction counting against a ceiling, trickle-down/trickle-up compliance audits,
periodic three-lens sweeps. The ecosystem's answer to the same problem is "keep it small
enough that none of that is needed."

The honest reading is that the maintenance regime is a symptom rather than a discipline.
It exists because the file was allowed to reach the size where a rule can hide in it, and
every mechanism added since is an attempt to make an oversized artifact governable rather
than to stop it being oversized. That does not make the individual mechanisms wrong — the
self-authoring gate has caught real defects — but it does mean their cost should be counted
against the file that necessitates them, not treated as fixed overhead.

## What this does and does not settle

Settles: the user's instinct that the doc as it stands is unsound is corroborated by
independent practice, and the accretion was not a local failure of discipline.

Does not settle: whether the answer is full retirement or a small always-loaded core plus
fetched skill docs. The published consensus points at the second, but no source addresses
the specific case that motivated this doc — rules that must fire in ordinary conversation
when no skill is running at all.

## Sources

- https://tianpan.co/blog/2026-02-14-writing-effective-agent-instruction-files
- https://www.aicodex.to/articles/claude-md-maintenance
- https://rahuulmiishra.medium.com/your-claude-md-is-doing-too-much-heres-how-to-fix-it-2cc495ed3599
- https://medium.com/@richardhightower/claude-code-rules-stop-stuffing-everything-into-one-claude-md-0b3732bca433
- https://claudelog.com/faqs/what-are-claude-rules/
- https://claudefa.st/blog/guide/mechanics/rules-directory
- https://marcelcastrobr.github.io/posts/2026-01-29-Skills-Context-Engineering.html
- https://developers.redhat.com/articles/2026/07/27/standardize-project-context-agentsmd-and-agent-skills
