# How law puts legislation on a review cycle — and where those cycles fail

Researched 2026-08-10 at the user's request, for [rule-lifecycle-system]. The
project already borrows its drafting rules from legislation
(`legal-drafting-for-tight-rules.md`, `legislative-prose-syntax.md`); this asks
the next question — what law does about *keeping* a corpus reviewed, which is
the "maintained / audited / repealed" half the design has no answer for.

## The three mechanisms law actually uses

**1. Sunset clause.** A provision expires on a fixed date unless the legislature
re-enacts it. Typical terms are five or ten years. Some variants expire on a
condition rather than a date.

**2. Post-legislative scrutiny (PLS).** In the UK, the government produces a
memorandum on an Act **three to five years after Royal Assent**, submitted to
the relevant select committee, which then decides whether to hold a fuller
inquiry. The Law Commission defines PLS as review addressing whether the
intended policy objectives were met and how effectively. Memoranda are
deliberately **not** produced for Acts that are routine, already repealed, of
very limited policy significance, or already subject to regular review by
another route.

**3. Statute law revision and consolidation.** A standing body — the Law
Commission — runs continuing programmes that identify spent and obsolete
provisions for repeal, and consolidate scattered enactments into single Acts.
This is periodic maintenance owned by a *standing body*, not by whoever authored
the original law.

## The failure evidence, which is the more useful half

PLS is the mechanism closest to what this project has been trying to build, and
it fails at scale:

- **Only 7.6% of 344 eligible Acts** passed between 2005 and 2017 received any
  post-legislative scrutiny at all. Of the 61 instances that did, only 20 were
  formal PLS inquiries.
- Where reports were produced, **61% of recommendations across 17 PLS reports
  (2005–2016) were rejected, ignored, or given indeterminate responses.**
  Acceptance fell with the size of the ask — around 52% for minor actions, and
  **zero** for substantial ones.
- The Commons committees that own PLS as a "core task" **rarely find time**,
  because the same committees carry all policy scrutiny.
- Worked example: the Criminal Justice and Courts Act 2015's judicial review
  provisions were never scrutinised despite being due. Asked in 2020, the
  government said only that it would "continue to keep the provisions under
  review".

## What transfers

**Finding A — the decisive difference is what happens when nobody acts.** A
sunset clause works because inaction *repeals*: the default state does the work
and the busy party must act to keep the rule. PLS fails because inaction leaves
everything exactly as it was, and a memorandum that is due but unwritten
produces no signal. Every cycle this project has tried — the merge cycle, the
audit, FAQ sync — has been PLS-shaped: a duty to review, with inaction as a
silent no-op. That is the same finding the queue already records three times
from its own history, now corroborated from outside.

**Finding B — reviewing everything is the failure; scoping the obligation is
the fix.** The UK system explicitly exempts routine Acts, spent Acts, and
anything already reviewed by another route. A cycle that claims the whole corpus
gets 7.6% coverage. One that claims a narrow slice can be honoured.

**Finding C — maintenance belongs to a standing owner, not to the author or to
the body already doing the primary work.** Repeals and consolidation sit with
the Law Commission precisely because the legislature has no capacity for them.
The project's analogue is that a review cannot be a duty of whichever /plan or
/next session happens to be running, since those sessions are already fully
occupied with the primary work — which is exactly why the audit reached ~218
instructions before anyone counted.

**Finding D — recommendation strength predicts rejection.** Substantial
recommendations had a zero acceptance rate. An audit that produces large
restructuring proposals will not be acted on; one producing small, specific,
cheap changes will. Bears directly on how audit findings should be sized.

## What this does not settle

Whether a time-based expiry has any meaning here — the project has no calendar
pressure and no legislature, and a doc that silently expires is not obviously
safe. The transferable part is the *default-state* principle (Finding A), not
the calendar.

## Sources

- [Sunset Clauses and Post-Legislative Scrutiny: Bridging the Gap between Potential and Reality — Westminster Foundation for Democracy](https://www.wfd.org/what-we-do/resources/sunset-clauses-and-post-legislative-scrutiny-bridging-gap-between-potential)
- [Did you get the memo? Post-legislative scrutiny and the case of judicial review — Hansard Society](https://www.hansardsociety.org.uk/blog/did-you-get-the-memo-post-legislative-scrutiny-and-the-case-of-judicial) (the 7.6% and 61% figures, from Dr Thomas Caygill's research)
- [Post-legislative scrutiny of Acts — Erskine May, UK Parliament](https://erskinemay.parliament.uk/section/4989/postlegislative-scrutiny-of-acts/)
- [Post-legislative Scrutiny – The Government's Approach (Cm 7320)](https://assets.publishing.service.gov.uk/media/5a7c82caed915d48c24103d5/7320.pdf)
- [Post-legislative scrutiny in the UK Parliament — Dr Thomas Caygill, WFD](https://www.wfd.org/sites/default/files/2021-12/2021-10-18-PLS-in-the-UK-Parliament-Dr-Thomas-Caygill-FINAL.pdf)
