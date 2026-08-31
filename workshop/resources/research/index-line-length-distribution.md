# The index-line proportional cap, measured against the whole LOG corpus

Measured 2026-08-12, building [index-cap-sample-was-three-entries]. This is
evidence a later session must be able to re-read word-for-word before restoring
or re-deriving a figure, which is why it is a durable file rather than a LOG
paragraph.

## What was measured

Every line in `LOG/index.md` that names an entry file, against the word count of
the entry it points to. The measure is the index line's length as a **percentage
of its entry's length** — the quantity the retired 20% cap governed.

The script is reproducible and read-only: it pairs each index line with the last
`YYYY-MM-DD-*.md` filename on that line, counts words on both sides with
`str.split()`, and reports the distribution.

## The result

```
index lines measured: 416      (unmatched/skipped: 162)
min 4.5%   median 16.1%   mean 17.1%   max 47.9%
over the 20% cap: 117 of 416 (28%)
```

The 162 skipped lines are pre-split legacy entries that have no file of their
own — they live inside `LOG/log.md` and `log-v*.md` — so there is nothing to
measure them against. **This differs from the count of 87 recorded in the queue
item**, which was measured over a smaller set on 2026-08-11. Both are honest;
the denominators differ, and the corpus has grown since. Nothing here turns on
which figure is right, because the finding is the *shape* below, not the count.

## The shape, which is the finding

Split by the length of the entry — the variable the original three-entry sample
held constant without anyone noticing:

```
entry under 200 words    n=78    median 21.3%   max 47.9%   over 20%: 51 of 78
entry 200-499 words      n=227   median 15.8%   max 33.9%   over 20%: 61 of 227
entry 500-999 words      n=96    median 13.8%   max 37.1%   over 20%:  5 of 96
entry 1000+ words        n=15    median 12.4%   max 19.9%   over 20%:  0 of 15
```

**The cap is monotonic in entry length, and it never fires on a long entry.**
Not one of the fifteen entries over 1,000 words breaches it; the worst sits at
19.9%. Two thirds of the entries under 200 words breach it, and the worst
breaches are all short entries carrying ordinary-length lines:

```
 47.9%   line 46w / entry  96w   2026-07-02-proactive-queue-referenced-pushback.md
 44.0%   line 48w / entry 109w   2026-07-02-sequence-record-then-release.md
 41.1%   line 39w / entry  95w   2026-08-01-why-clause-audit-pass-by-pass-criteria.md
 39.2%   line 40w / entry 102w   2026-07-02-retire-spectrum-offers.md
 39.1%   line 34w / entry  87w   2026-07-30-delete-x-worktree-folder.md
```

A 34-word line is not a long index line by any reading. It breaches only because
the entry it points at is 87 words.

**So the cap does not measure what it was written to measure.** It was written
to stop an index line restating its entry. What it actually measures is how
short the entry is. On the corpus it governs, it fires 117 times and — on the
evidence of the worst cases above — essentially never on the thing it was aimed
at.

## Why the original derivation missed it

The three entries measured at processing were 968, 1,055 and 1,738 words. All
three fall in the two longest buckets, where the cap has a 0–5% breach rate. The
sample was unrepresentative of entry length specifically, and entry length is
the variable that drives the whole result.

This is not an argument that measuring was wrong. Measuring on three entries is
more than the 1,200-word ceiling ever had. It was measured on too little, and
on a slice that could not show the effect.

## What this supports, and what it does not

It supports **dropping the proportion** and keeping the readiness test the rule
already carries: an index line must support the open/skip decision without
restating the entry.

It does **not** support a second number. Scoping the cap to entries above some
length reintroduces a bare figure, which this project has now banned twice — in
`rule_signals.py` and in the self-authoring gate. The absolute-length column
gives no threshold either: the longest lines (340w, 231w, 224w) all point at
entries of 1,355–1,766 words and all pass comfortably, so length alone
discriminates nothing.

**The cost of dropping it, recorded rather than discovered.** The rule becomes
unenforceable by script, at a moment when this project has been deliberately
preferring mechanical checks to judgment. The counter is the number above: a
mechanical check that fires 117 times against work nobody thinks is wrong is
worse than no check, because it is learned past and then ignored everywhere —
which is the failure this project fights hardest.

## Reproducing it

The script lives in the session scratchpad and is not kept; it is fifteen lines
and is described completely in "What was measured" above. Re-deriving it costs
minutes, and a script kept in the repository would need maintaining against a
format that has already changed once.
