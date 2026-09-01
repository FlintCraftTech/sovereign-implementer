# Scripted turns in the shipped procedure docs — where each is defined, what tag it carries, and whether any content rule governs it

**Compiled 2026-08-31 by an `[audit]` run under [scripted-turns-inventory].** A
*scripted turn* is any point where the method requires Claude to say something
with a particular shape — a report, an offer, an ask, a checkpoint, a close
message. The audit was raised because the per-turn content rules built
2026-08-31 reached planning-session turns only, and nobody had checked which
other turns exist.

## How this was compiled, and what it does not cover

**Tagged turns were extracted mechanically** — a grep for the five
response-shape tags across every shipped doc — so that half of the inventory is
exhaustive.

**Untagged turns were not, and cannot be.** A turn stated as ordinary prose
("say in one line what was filed") is indistinguishable by any mechanical test
from explanation about a turn. The untagged turns listed below were found by
reading, and reading covered `skill-nonspecific-rules.md`, `next.md`,
`next-build.md`, `next-audit.md` and `rescan.md` in full, plus the turn sites in
`plan.md`, `done.md`, `done-build.md`, `done-plan.md`, `done-audit.md` and
`setup.md`. Those last six were **not** read end to end.

**So: the tagged inventory is complete; the untagged one is a floor.** That
asymmetry is itself the first finding below.

**This is the same limit the corpus already accepted for rules, now stated for
turns** (relocated here 2026-09-01 from the capture
[untagged-turns-are-unsweepable]): `rule_signals.py` sees a rule only in its
three shapes, and widening the pattern was refused because a rule stated
mid-paragraph cannot be told from prose. Any future sweep over turns inherits
the same bound — read its coverage from this section rather than treating any
turns inventory as complete. An always-loaded statement of this limit was
weighed at processing and refused on the distribution test: a session sweeping
turns knows to fetch this file, and every other session would pay for a
sentence that can never fire for it.

## The tagged inventory

Counts are tag occurrences per doc, including the definitions themselves.

```
skill-nonspecific-rules.md    8   (5 are the tag DEFINITIONS; 1 the composite
                                   specimen; 2 are cross-references)
plan.md                      29
next.md                      16
next-build.md                 7
next-audit.md                 4
done.md                      12
done-build.md                18
done-plan.md                 10
done-audit.md                 7
rescan.md                     4
setup.md                     25
feedback-and-inbox.md         4
migrate-checklist.md          1
ports.md                      0
recovery.md                   0
```

### Turns that carry BOTH a tag and a content rule saying what they must contain

```
plan.md, present-and-interview          [DISCUSS, PROMPT]
   -> the strongest content rule in the corpus: opens with a plain-English
      summary before any analysis, NAMES ITS SUBJECTS OUTRIGHT (no referring
      expression only the scrollback resolves), NAMES WHO RAISED IT where the
      item came from anyone but the project's owner, and first-and-later items
      share one shape.
plan.md, the ordering ask               [PROMPT]
   -> the question is quoted verbatim, and the asymmetric red-flag variant is
      specified.
rescan.md, Step 2 file-what-you-find    [BRIEF] / [PROMPT]
   -> a verbatim limit sentence with a specified restatement-in-one-clause on
      repeat; a louder verbatim sentence for the failed cross-check; a named
      proxy ban (length, duration, message count); a one-line nothing-found
      result, quoted.
rescan.md, Step 3 hand back             [BRIEF]
   -> names what the captures wait for, says it once, recommends nothing else.
done.md, wind-down re-scan set          [PROMPT]
   -> ONE numbered message, and the closing sentence is specified verbatim:
      "Say go to file them all, or contest by number."
done.md, the closing message            (untagged)
   -> carries ONE line naming the advisory; the ladder below it says what the
      next-work line must distinguish.
next.md, present the run                [BRIEF, PROMPT]
   -> render as a one-line pointer; the off-ramp sentence is given as an
      exemplar; the affirmative first, the exception second.
next.md, narrate the lock               [BRIEF]
   -> one sentence, and the content is enumerated (what the working file
      carries, that the queue keeps its own copy).
next-audit.md, the contradiction stop   [PROMPT]
   -> the whole turn is quoted as an exemplar.
```

### Turns that carry a tag and NO content rule

These are the gaps the audit was raised to find. Each has a shape (how long, whether
to wait) and nothing saying what it must say.

```
plan.md, start-of-processing reorder    [BRIEF]     — "narrate the order used"
   and throughput floor                              and a floor number; nothing
                                                     on what either must contain
plan.md, seed the queue from SPEC       [SILENT/BRIEF]
plan.md, cycles due-ness check          [SILENT/BRIEF]
plan.md, correspondence scan            [SILENT/BRIEF]
plan.md, below-the-line revisit         [SILENT/BRIEF] — gained a premise clause
                                                     2026-08-31, still no shape
                                                     for the lift message itself
plan.md, the checkpoint                 [PROMPT]
plan.md, process-now offer              [PROMPT]
plan.md, the `Not before:` date ask     [PROMPT]
plan.md, neutral end-of-queue gate      [PROMPT]
next.md, pre-flight single narration    [BRIEF]     — says to FOLD several checks
                                                     into one, not what it says
next.md, NOTHING_CLEARED                [BRIEF]
next.md, UNCLEARED_FLAG                 [BRIEF, PROMPT]
next.md, FREEFORM_HALT                  [BRIEF, PROMPT]
next.md, drop-an-item recommendations   [BRIEF]
next.md, ending-before-scope-lock       [PROMPT] / [BRIEF]
next-build.md, scope-grows              [PROMPT]    — an exemplar sentence for
                                                     the minor arm only
next-build.md, going in circles         [PROMPT]
next-build.md, approach not working     [DISCUSS, PROMPT]
next-build.md, completion               [BRIEF, PROMPT] — three requirements, all
                                                     about what NOT to end on
done-build.md, 1.1 verify completion    [SILENT/PROMPT]
done-build.md, 1.2 route findings       [PROMPT]
done-build.md, 1.3 spec check-against   [SILENT/PROMPT]
done-build.md, 1.4 red-flag close       [SILENT/PROMPT]
done-build.md, 1.5 reply to mail        [SILENT/PROMPT]
done-build.md, unconfirmed-item report  [BRIEF]
done-audit.md, 1.1 and 1.2              [SILENT/PROMPT]
done-plan.md, spec-sync gate            [SILENT/PROMPT]
done-plan.md, batch the human stops     [SILENT/BRIEF]
done-plan.md, position the line         [SILENT/BRIEF]
done-plan.md, completed [user] items    [SILENT/BRIEF]
done-plan.md, isolated-branch warning   [BRIEF]
setup.md, ~14 migration sub-steps       [SILENT/BRIEF/PROMPT]
```

### The capture loop in `skill-nonspecific-rules.md`

Named in the raising item as ungoverned. It is **partly** governed, and the
distinction matters:

```
HAS a content rule   the report is one line, names what landed and where, points
                     at the artifact, says the user may reject it and have it
                     reverted, and is never a re-paste. A capture report also
                     carries a clause saying WHY it was captured rather than
                     done now (next-build.md).
HAS a shape rule     close by who raised it: user raised it -> ask "anything
                     else?"; Claude noticed it -> confirm and resume.
HAS NEITHER          what the one line must say about the thing itself. "State
                     what was filed in one line" does not say whether the line
                     names the subject, the reason, or only the slug — and the
                     naming-its-subjects requirement built into plan.md's
                     summary turn was never carried here.
```

## Findings, in the order they were reached

1. **The tagged/untagged asymmetry is structural, not incidental.** A turn
   without a tag is invisible to every mechanical sweep over this corpus,
   exactly as a rule stated as ordinary prose is invisible to
   `rule_signals.py`. The corpus already accepted that limit for rules; nothing
   states it for turns.

2. **The raising item's premise is partly wrong about /rescan, and this is
   worth recording rather than quietly correcting.** `/rescan`'s turns are among
   the *best* governed in the corpus — two verbatim sentences, a specified
   restatement, a named proxy ban and a quoted nothing-found line. What is
   ungoverned is `/done`'s turns and the bulk of `/plan`'s non-item turns.

3. **`done-build.md` and `done-audit.md` are the densest ungoverned region:**
   eighteen and seven tags respectively, and essentially no content rules — the
   close's checks all have shapes and none has a script.

4. **Several `[PROMPT]` turns state only what not to say.** `next-build.md`'s
   completion turn is the clearest: three requirements, all prohibitions. The
   corpus's own wording rule says a prohibition signals that the action was
   never specified.

5. **The one-line capture report has no subject-naming requirement**, while the
   planning summary turn does. The same reader problem applies to both.

## Frame assessment

- **TIME RANGE** — not applicable in the usual sense: this describes the corpus
  as it stands on 2026-08-31, and it goes stale with the next doc edit. It is a
  snapshot, and a later reader should re-run the tag extraction rather than
  trust these counts.
- **PEOPLE** — the turns govern what an external non-coder consumer reads. The
  inventory was compiled by reading the docs, not by watching a consumer
  session, so it says what is *specified* and nothing about what is *emitted*.
- **FRESHNESS** — amended constantly; every rule-bearing commit can change it.
- **RISK IF WRONG** — low and self-correcting: an entry that is wrong is wrong
  about a document anyone can open. The real risk is over-reading it as
  complete, which the coverage statement above is written to prevent.
- **ALTERNATIVES** — a per-doc read of all seven docs end to end was considered
  and partly done; the tag extraction was chosen for the exhaustive half
  because a mechanical sweep cannot be silently truncated, which reading can.
  Watching live sessions to see which turns actually misfire was not done and is
  different work.
