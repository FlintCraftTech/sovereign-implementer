# What a FAQ is for, and the technical-writing case against having one

Researched 2026-08-14 during the /plan that filed [faq-entry-criteria] and
[faq-cost-versus-value]. Commissioned by the user, who asked for the criteria for
an FAQ entry to be defined rather than left as a judgment, and who had separately
questioned whether the FAQ still earns its maintenance cost. Findings are
Claude's; the sources are named below.

Searched inline, no subagent. Two searches: one on FAQ-versus-reference criteria,
which returned only generic match-the-format-to-the-audience advice and settled
nothing; one on FAQs as a documentation anti-pattern, which returned the
substantive material below. Recording both is deliberate — the first framing is
the one that fails, and a later session asking the same question should not
repeat it.

## 1. The first search failed, and why

Asking "what belongs in an FAQ versus a reference guide" returns the same answer
from every technical-documentation source: choose the format that matches the
audience's goals and technical level. True, and useless as a trigger — it cannot
discriminate, which is exactly the defect [faq-entry-criteria] was filed about.
No source publishes criteria for what makes a question an FAQ question.

That absence turns out to be the finding rather than a gap in the searching.

## 2. The mainstream technical-writing position is against having a FAQ at all

Three sources, independently and over more than a decade:

- [FAQs: why we don't have them](https://gds.blog.gov.uk/2013/07/25/faqs-why-we-dont-have-them/) — UK Government Digital Service
- [No More FAQs: Create Purposeful Information for a More Effective User Experience](https://alistapart.com/article/no-more-faqs-create-purposeful-information-for-a-more-effective-user-experi/) — A List Apart
- [FAQs are not the answer](https://passo.uno/what-the-faq/) — Fabrizio Ferri Benedetti

The position is not "write better FAQs". It is that the format itself produces
the failure.

## 3. The four recurring findings

**FAQs come from needing somewhere visible to put pressing questions**, rather
than from a deliberate choice about information architecture. They are attractive
because they are easy to produce without doing the structural work.

**They don't live in context.** A separate page answers questions spanning
unrelated areas, held away from the material each one belongs to. The user has to
find the FAQ, then find their question in it, instead of meeting the answer where
the subject is explained.

**Duplicated content falls out of sync.** Where the answer exists both in the FAQ
and in the material proper, the two drift.

**The page becomes a dumping ground** for anything that needs publishing
somewhere and has no other home.

One source declines to call it an anti-pattern on the grounds that an
anti-pattern implies a conscious choice, and documentation-by-FAQ is usually not
chosen at all. That distinction is worth keeping: it means the fix is a decision,
not a correction.

## 4. How this bears on this project, stated as evidence rather than as a decision

The third finding is already an open queue item —
[own-faq-diverged-from-shipped-template] records that this project's own FAQ and
the shipped template have drifted, with the authoring rule pointing at only one
of them. That is the sync failure above, observed here before this research was
done.

The first finding describes how the FAQ-sync gate is written: the trigger asks
whether a non-coder meeting a change would have a question the FAQ does not
answer, which is the "somewhere visible to put it" impulse expressed as a rule.

**What this does not settle.** Whether to retire the FAQ, which is
[faq-cost-versus-value]'s question and the user's decision. The literature argues
the content should live where the subject is explained; it does not say what a
project should do when that material is a procedure doc the consumer never opens.
That is the specific question this project has to answer for itself, and no
source found addresses it.

**A position Claude argued and the evidence went against.** During the same
session Claude argued that the FAQ has a distinct reader — the consumer opening a
document of their own, as against the work-cycle orientation which only Claude
reads — and that retiring it would leave that reader unserved. The literature's
answer is that the reader is better served by the answer living in context, so
the distinct-reader argument supports *relocating* the content rather than
*keeping the format*. Recorded because it is the intuitive position and will be
re-proposed otherwise.
