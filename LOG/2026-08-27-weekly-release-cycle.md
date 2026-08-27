# beac9d2 — This project gets a cycles doc and a weekly Wednesday release, and the release model is amended to run on it

Releases had been on request and at no other time — the user's decision of 2026-08-09, made after she stopped an automatic release twice. This narrows that clause rather than overturning it: a release runs when she asks, **or** when the weekly release cycle falls due.

**Why the 2026-08-09 failure does not recur, which is the only thing that made this admissible.** The old automatic trigger made every routine save ask "is this good enough to publish?" — a prospective readiness question with no honest answer on a project that will never feel finished. The cycle asks no such question. The calendar and a label applied when the rezip was posted settle which build goes, **retrospectively**: the label describes a build that already exists. The pre-rejected middle option — keep the trigger automatic but pause once before publishing — stays rejected, and the paragraph saying so is untouched, because that pause *is* the readiness question.

**The selector is the superseded one, and the supersession is the user's.** The definition's pick is the most recent rezip labelled stable on the nerds list, not the original "newest rezip at least a week old". The week-old property now lives in the promotion step of the three-channel model rather than in the pick. The recorded refusal survives intact: no choosing among candidates on the day, the selector stays mechanical.

**The definition is written to be buildable on the release half alone.** The three-channel model — a Wednesday turn producing two events, this week's pick becoming the new beta and last week's beta promoting to stable — is not yet built, so the steps cover the release and the promotion step joins when [beta-tester-pathway] ships. The superseded selector is kept in the file rather than deleted, because its reasoning is cited elsewhere.

**Verified by running the shipped parser rather than by reading the file.** `cycles_facts()` from the installed `session_start.py` was run against the new `CYCLES.md` and returned the slug, cadence and observable — which is what caught the one real defect: **the parser reads only the first line of `Cadence:` and `Observable:`**, so both fields had wrapped and were being truncated mid-sentence, comma and all. A read of the doc would not have shown it, and a truncated cadence still reads like a cadence. Both fields were rewritten single-line and the reasoning moved below them. Filed as [cycles-fields-are-single-line], since nothing a future cycle author reads mentions the constraint.

**Files:** `CYCLES.md` (created), `CLAUDE.md`. `resources/release-ritual.md` needed no change from this item — the ritual itself is untouched.

Rule gate: run — amendment to the Release section of CLAUDE.md, naming and superseding its at-no-other-time clause; the 2026-08-09 reasoning is outweighed on the stated ground rather than called wrong.

Routed to Captures: [cycles-fields-are-single-line]
