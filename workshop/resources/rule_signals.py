#!/usr/bin/env python3
"""The rule-lifecycle status board — five independent signals, computed.

Host-only. This lives in resources/ rather than the plugin's scripts/ folder
because consumers never author method rules, so the whole lifecycle would
misfire for them. The session-start surface that carries the output DOES ship;
it stays silent when this file is absent, which is the two-doors pattern.

## What this is, and what it is not

It is NOT a cycle. That was the design's first decision: a positional cycle —
one stage following another — is what failed before, because compression ended
up permanently downstream of machinery that never ran. These are independent
mechanisms, each firing on its own trigger whether or not any other ran, and
what a session reads at start is which of them are currently signalling. A
board, not a position.

Nothing here is stored. The board is recomputed from the artifacts every time,
because a state file must be maintained and the first session that forgets to
update it makes the board lie. The one exception is the retired-terms list,
which is source data — a recorded event, authored once — not derived state.

## Six entries, in two classes

One REPORT (MEASURED) measures and can never fire. Five SIGNALS (BORN,
CONTRADICTED, MAINTAINED, REPEALED, AUDIT-LAG) have a trigger and do fire. Only
signals are counted in the header: a denominator including the report invites
the reading that six things are watched when five are, and a check that
over-claims makes the corpus look guarded when it is only partly guarded.

The AUDITED entry — "whether a corpus sweep is due" — is deleted, not renamed.
Its trigger was the ceiling, the ceiling was repealed, and a measurement that
can never fire is a measurement nobody reads. AUDIT-LAG supersedes it with a
trigger that needs no threshold: rule-bearing commits since the most recent
compliance-audit LOG entry.

MEASURED   a structural rule-statement count across the always-loaded files,
           reported per audience as a growth report. No threshold, no verdict:
           it never fires. See GROWTH_NOTE for why the ceiling was removed.
AUDIT-LAG  rule-bearing commits made since the most recent compliance-audit
           LOG entry. Fires while any exist; the capture it files is one
           [audit] scoped to the changed files (delta scope, never the corpus).
BORN       commits that should carry a gate-disposition line and do not,
           matched against commits touching the rule-bearing file set.
CONTRADICTED
           commits whose LOG entry says the gate was not needed while the
           always-loaded count ROSE. BORN checks a disposition EXISTS; this
           checks it isn't contradicted by the commit it describes. It cannot
           tell whether a gate recorded as *run* ran honestly, and does not
           claim to.
MAINTAINED near-duplicate rule statements across the corpus. This is
           codification — one subject, one rule, stated once.
REPEALED   live rules naming a term on the retired list.

BORN and CONTRADICTED are both bounded by DISPOSITION_BASELINE, so neither
reports commits made before the obligation existed.

## What a signal does

It files a capture, once, and gets out of the way. It does not escalate (that
would need a bare number) and it does not go quiet on a standing signal (that
recreates the silent inaction the whole design exists to prevent). The work
goes where all work goes — the queue — where ignoring it is visible.

A signal counts as satisfied while ANY OPEN WORK ITEM CARRIES ITS SLUG, IN
EITHER SECTION — Unprocessed or Processed, captured or designed and cleared.
Only deleting that item re-arms the signal. This is the guard against filing
the same capture every session.

Saying "in either section" is not pedantry. The wording used to name
Unprocessed as the filing destination and then leave the satisfied-test
unqualified, so a session could read it as "an open capture *in Unprocessed*".
On 2026-08-12 a single /plan processed all four board-filed captures into
Processed at once; under that reading the very next session would have filed
four duplicates on top of four items that were not merely open but designed,
kept and cleared — the signal firing loudest exactly when the work was
furthest along.

The check is NOT mechanical, which is the easiest thing here to miss. This
script computes and prints; it never parses QUEUE.md and never files anything.
The satisfied-test is performed by whoever reads the output, so this wording
IS the mechanism — there is no code to fall back on.

Having the script scan QUEUE.md itself was weighed and rejected:
post_tool_use.py already parses QUEUE.md for the lint, and a second parser in
a second script is two things that must agree about the file's shape and will
drift.

Usage:
    py throughliner/workshop/resources/rule_signals.py [project root]

Run it from the OUTER repository — the folder the app opens, where LOG/ and
CLAUDE.md live. In a nested project the checks read two histories: the outer's
for CLAUDE.md and the self-authoring files, the inner's (the product subfolder)
for the shipped docs. Each commit's touched paths are matched against the
trigger set relative to its own repository; LOG entries are read from the outer
alone. A flat project has one repository and reads exactly as before.
"""

import os
import re
import subprocess
import sys

for _stream in (sys.stderr, sys.stdout):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError, OSError):
        pass


# --- Configuration ------------------------------------------------------

# The always-loaded corpus, split by AUDIENCE, because there are two and
# collapsing them hides which one is carrying the weight.
#
# A consumer project loads only the shipped file. THIS project loads that file
# AND its own CLAUDE.md in every session, so its real always-loaded burden is
# the sum. Reporting one number understated this project's position by the
# whole of CLAUDE.md, and the eviction work scoped off that number was scoped
# against the smaller figure.
#
# resources/method-compliance-audit-checklist.md has always required the count
# be reported split by audience. This is the tool finally doing it.
# The shipped output style used to sit here too — applied automatically at
# system-prompt priority, so always-loaded in the only sense this count cares
# about. It was deleted on 2026-08-14 as triplication of rules the file above
# already carries; its three unique rules migrated into that file, so the
# corpus this list measures is unchanged in substance and smaller in text.
SHIPPED_ALWAYS_LOADED = [
    "plugin/throughliner/docs/skill-nonspecific-rules.md",
]

HOST_ALWAYS_LOADED = [
    "CLAUDE.md",
]

# Every file loaded in every session of THIS project. CONTRADICTED measures
# growth against this combined set rather than the shipped file alone: a
# commit that adds rules to CLAUDE.md grows the corpus a session actually
# carries, and CLAUDE.md is already in RULE_BEARING, so measuring only the
# shipped half left that growth invisible to the one check aimed at it.
ALWAYS_LOADED = SHIPPED_ALWAYS_LOADED + HOST_ALWAYS_LOADED

# Fetched procedure docs. Not always-loaded — each is paid only by the sessions
# that run its skill — so they are reported as their own group and never summed
# with the always-loaded counts. Redistribution to a fetched doc is how bloat
# gets hidden rather than cut; two groups is what makes a relocation read as a
# relocation instead of as a reduction.
FETCHED_DOCS = [
    "plugin/throughliner/docs/plan.md",
    "plugin/throughliner/docs/next.md",
    "plugin/throughliner/docs/next-build.md",
    "plugin/throughliner/docs/next-audit.md",
    "plugin/throughliner/docs/done.md",
    "plugin/throughliner/docs/done-build.md",
    "plugin/throughliner/docs/done-plan.md",
    "plugin/throughliner/docs/setup.md",
]

# How far back the growth report looks for its direction of travel. This is a
# reporting WINDOW, not a threshold — nothing passes or fails against it, and
# no work is triggered by it. It matches the window _rule_bearing_commits
# already uses, so the board reads one span of history rather than two.
GROWTH_WINDOW = 30

# Files where a method rule can be born. A commit touching one of these is
# BORN's trigger — mechanical, with no judgment involved, which is what makes
# this stage buildable at all.
RULE_BEARING = [
    "plugin/throughliner/docs/",
    "workshop/resources/self-authoring-rules.md",
    "workshop/resources/rule-maintenance.md",
    "workshop/resources/method-compliance-audit-checklist.md",
    "CLAUDE.md",
]

# Matched by startswith against commit file lists, so these carry the full
# post-move path. The pre-move `resources/` forms were dead here for the same
# reason the retired-terms constant below was — e04b514 moved the folder and a
# string constant is read by nobody until it is needed.
RETIRED_TERMS_FILE = "workshop/resources/retired-terms.md"

# The commit in which the rule-gate disposition obligation shipped. BORN and
# CONTRADICTED examine only commits AFTER this one; everything at or before it
# predates the obligation and owes nothing.
#
# 7c9922a (2026-08-11) is the build that added the `Rule gate:` block to
# CLAUDE.md, alongside the rule-lifecycle board itself. Found by
# `git log -S'Rule gate: run —' -- CLAUDE.md`, not from memory.
#
# Named rather than left bare, deliberately: a hash nobody can date is a
# constant nobody dares change. If the obligation is ever re-founded, move this
# and say in this comment which commit it now names and why.
DISPOSITION_BASELINE = "7c9922a"

# Backfilling dispositions for pre-baseline commits was considered and REJECTED.
# A backfilled disposition is written by someone reconstructing what a past
# session decided — it would look like evidence and not be, which is exactly the
# handoff-provenance problem the method already names.

# THERE IS NO CEILING, AND ONE MUST NOT BE RE-DERIVED TO FILL THE GAP.
#
# There used to be: CEILING = 200, in the proxy's own units, derived from the
# 150-200 instruction figure in
# resources/research/instruction-file-bloat-and-subtraction.md. That figure was
# re-validated against the 5-series on 2026-08-12 and found roughly an order of
# magnitude too tight — the benchmark was re-run a year on, frontier models had
# improved about tenfold, and the nearest tested Claude model only begins
# failing between 2,000 and 5,000 constraints. Full finding, with both caveats
# (neither Opus 5 nor Fable 5 was tested, and the benchmark measures keyword
# constraints rather than behavioural rules):
# resources/research/instruction-ceiling-revalidated-for-5-series.md
#
# So the ceiling lost its derivation, and a threshold with no derivation is
# what the method bans. Being conservative is not a defence — an invented
# number fires against correct work.
#
# What this deliberately gives up: nothing here will ever say the corpus is too
# big. That is the honest position rather than a regression. The case for
# eviction now rests on RELEVANCE — irrelevant content degrading the model's
# treatment of all instructions, near-identical rules acting as optimal
# distractors for each other, and Anthropic's own 5-series guidance to remove
# prior-model scaffolding. A count measures none of those.
GROWTH_NOTE = (
    "These are growth reports, not verdicts. There is no ceiling: the 150-200 "
    "instruction figure the old one derived from was re-validated against the "
    "5-series and found roughly an order of magnitude too tight "
    "(resources/research/instruction-ceiling-revalidated-for-5-series.md), and "
    "a threshold with no derivation is what the method bans. Read the numbers "
    "as direction of travel. The case for eviction is relevance — irrelevant "
    "and near-duplicate rules degrade every instruction around them — and no "
    "count measures that."
)

# --- Two repositories ----------------------------------------------------
#
# A nested project (setup's split or wrap) keeps the method's documents in the
# outer repository and the product in an inner one. The rule corpus straddles
# them: CLAUDE.md and LOG/ in the outer, plugin/throughliner/docs/ in the
# inner, workshop/ wherever it currently sits. Every read below that used to
# assume one root now resolves each file to the repository that holds it, and
# every git read runs in the repository the commit belongs to.

VISIBILITY_INNER_RE = re.compile(r"inner repository \(`([^`]+?)/?`\)")


def inner_root(root):
    """The product subfolder in a nested project, or None for a flat one.

    Read from the project CLAUDE.md's Visibility line, which names the inner
    in backticks; failing that, the one immediate subfolder holding a `.git`.
    Two candidates and no Visibility line is ambiguous, and None is returned
    rather than a guess.
    """
    claude = os.path.join(root, "CLAUDE.md")
    try:
        with open(claude, "r", encoding="utf-8") as f:
            for line in f:
                if not line.startswith("Visibility:"):
                    continue
                m = VISIBILITY_INNER_RE.search(line)
                if m:
                    cand = os.path.join(root, m.group(1))
                    if os.path.isdir(os.path.join(cand, ".git")):
                        return cand
    except OSError:
        pass
    found = []
    try:
        for name in os.listdir(root):
            p = os.path.join(root, name)
            if (not name.startswith(".") and os.path.isdir(p)
                    and os.path.isdir(os.path.join(p, ".git"))):
                found.append(p)
    except OSError:
        return None
    return found[0] if len(found) == 1 else None


def repos(root):
    """(label, path) for every repository whose history the checks read."""
    out = [("outer", root)]
    inner = inner_root(root)
    if inner:
        out.append(("inner", inner))
    return out


def locate(root, rel):
    """(repository path, rel) for a corpus file — the outer where it holds
    the file, else the inner; the outer by default where neither does, so a
    missing file reads as missing in one place rather than two."""
    if os.path.exists(os.path.join(root, rel)):
        return root, rel
    inner = inner_root(root)
    if inner and os.path.exists(os.path.join(inner, rel)):
        return inner, rel
    return root, rel


def _has_commit(repo, sha):
    try:
        out = subprocess.run(["git", "cat-file", "-e", sha + "^{commit}"],
                             cwd=repo, capture_output=True, text=True,
                             timeout=20)
    except (OSError, subprocess.SubprocessError):
        return False
    return out.returncode == 0


# A structural rule-statement: a bullet, a bolded lead-in, or a line inside a
# typed block. Counted by structure, never by judgment.
BULLET_RE = re.compile(r"^\s*[-*]\s+\S")
BOLD_LEAD_RE = re.compile(r"^\*\*[^*]+\*\*")
FENCE_RE = re.compile(r"^\s*```")


# --- MEASURED -----------------------------------------------------------

def count_text_statements(text):
    """Structural rule-statements in one document's text.

    Split out from count_statements so the same counter can run over a blob
    read from git history (CONTRADICTED's delta) as over a file on disk. One
    counter, two callers — a second implementation is what would drift.
    """
    count = 0
    in_fence = False
    for raw in text.splitlines():
        if FENCE_RE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            # A line inside a typed block carries a rule as surely as a
            # bullet does — the blocks are where this docset puts
            # structure. Blank and comment-only lines do not.
            stripped = raw.strip()
            if stripped and not stripped.startswith("#"):
                count += 1
            continue
        if BULLET_RE.match(raw) or BOLD_LEAD_RE.match(raw.strip()):
            count += 1
    return count


def count_statements(root, files=None):
    """Structural rule-statements across a named set of documents.

    Defaults to the whole always-loaded corpus. Callers pass one audience's
    list to get that audience's number.
    """
    total = 0
    per_file = {}
    for rel in (ALWAYS_LOADED if files is None else files):
        path = os.path.join(*locate(root, rel))
        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
        except OSError:
            continue
        count = count_text_statements(text)
        per_file[rel] = count
        total += count
    return total, per_file


def _count_at_rev(root, ref, files, strict=False):
    """Statement count for `files` as they stood at revision `ref`.

    Returns None if git is unusable, or — under `strict` — if any file in the
    set did not exist at that revision.

    The two modes exist because two callers want opposite things from a
    missing file. CONTRADICTED compares one commit to its parent and wants a
    missing file to count zero, so that adding a corpus file doesn't make
    every earlier commit uncountable. The growth report wants the opposite: a
    file that did not exist yet makes the comparison FALSE, not zero, because
    the difference then reads as growth when it is really the file's creation.
    That exact misreading appeared on the first run of this report.
    """
    total = 0
    for rel in files:
        repo, rel = locate(root, rel)
        try:
            out = subprocess.run(
                ["git", "show", "%s:%s" % (ref, rel)],
                cwd=repo, capture_output=True, text=True, timeout=20,
            )
        except (OSError, subprocess.SubprocessError):
            return None
        if out.returncode != 0:
            if strict:
                return None
            continue
        total += count_text_statements(out.stdout)
    return total


def _growth(root, files, now):
    """Direction of travel: this count against the same count GROWTH_WINDOW
    commits back. Returns a short phrase, never a verdict.
    """
    then = _count_at_rev(root, "HEAD~%d" % GROWTH_WINDOW, files, strict=True)
    if then is None:
        return "not comparable over %d commits (a file here is newer than that)" % (
            GROWTH_WINDOW,)
    delta = now - then
    direction = "up" if delta > 0 else ("down" if delta < 0 else "flat")
    return "%s %+d over the last %d commits (was %d)" % (
        direction, delta, GROWTH_WINDOW, then)


def _group_report(root, label, files):
    total, per_file = count_statements(root, files)
    detail = ", ".join(f"{k.split('/')[-1]}: {v}" for k, v in per_file.items())
    return "%s %d (%s) — %s" % (
        label, total, detail, _growth(root, files, total))


def signal_measured(root):
    """A growth report per audience, and per group. It never fires.

    Two audiences, because there are two: a consumer loads the shipped rules
    file only, while this project also loads its own CLAUDE.md in every
    session. And a third group for the fetched procedure docs, kept separate
    because their cost profile genuinely differs — a fetched doc is paid only
    by the sessions that run its skill — and because keeping them separate is
    what makes text MOVED out of the always-loaded file read as a relocation
    rather than as a reduction.

    skill-nonspecific-rules.md is deliberately NOT in the fetched group even
    though a skill fetches it: it is always-loaded, already counted above, and
    listing it twice would double-count the one file the report is most about.
    """
    shipped, _ = count_statements(root, SHIPPED_ALWAYS_LOADED)
    host, _ = count_statements(root, HOST_ALWAYS_LOADED)
    lines = [
        "always-loaded, consumer: " + _group_report(
            root, "", SHIPPED_ALWAYS_LOADED).strip(),
        "always-loaded, this project: %d (consumer's %d plus %d host-only) — %s" % (
            shipped + host, shipped, host,
            _growth(root, ALWAYS_LOADED, shipped + host)),
        "fetched procedure docs: " + _group_report(
            root, "", FETCHED_DOCS).strip(),
    ]
    return {
        "stage": "MEASURED",
        # A REPORT, not a signal: it has no threshold, so it cannot fire. The
        # `firing: False` key it used to carry read as meaningful and was not.
        "kind": "report",
        "value": shipped + host,
        "slug": "rule-corpus-over-ceiling",
        "message": (
            "Growth report (no ceiling, no verdict). " + " | ".join(lines)
            + " | Counts three shapes only: a bullet, a paragraph whose bold "
            "leads the line, and a line inside a typed block. A rule stated in "
            "plain prose, or with its bold anywhere but the start of the line, "
            "is invisible here — which is why those three are the authoring "
            "constraint rather than something to widen the pattern for."
        ),
    }


# --- AUDIT-LAG ----------------------------------------------------------

COMPLIANCE_AUDIT_ENTRY_RE = re.compile(r"compliance-audit", re.IGNORECASE)

# A filename naming a compliance audit is not enough: a planning session that
# PROCESSES an audit item writes a record named for that item's slug, so the
# filename match alone took a processing record as the boundary and silenced
# the check. The body decides: an audit record routes findings ("Routed to
# Captures:") or states what it touched ("Files touched:"), while a processing
# record carries "Work processed:" and neither of those necessarily. An entry
# carrying "Work processed:" is a planning record whatever else it carries.
AUDIT_RECORD_MARKERS = ("Routed to Captures:", "Files touched:")
PROCESSING_RECORD_MARKER = "Work processed:"


def _is_audit_record(path):
    """True where the entry's body reads as an audit's own record."""
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            body = f.read()
    except OSError:
        return False
    if PROCESSING_RECORD_MARKER in body:
        return False
    return any(m in body for m in AUDIT_RECORD_MARKERS)


def signal_audit_lag(root):
    """Rule-bearing commits made since the most recent compliance-audit entry.

    Supersedes the AUDITED measurement, which lost its trigger when the
    ceiling was repealed and could never fire. This needs no threshold: the
    boundary is an artifact — the newest LOG entry whose filename names a
    compliance audit — and the trigger is any rule-bearing commit after it.

    The capture it files is one [audit] scoped to the files those commits
    changed — delta scope, never the corpus; the one full pass is its own
    item, filed separately. Satisfied while an open item carries the slug,
    like every other check here. Over-fires by design, exactly as BORN does: a
    typo commit to docs/ summons an audit whose finding is "nothing to audit",
    which costs one line.
    """
    log_dir = os.path.join(root, "LOG")
    boundary = None
    if os.path.isdir(log_dir):
        # Newest first, and the filename match is only the candidate set: each
        # candidate's body must read as a genuine audit record, or the search
        # continues older. A planning record named for the audit item it merely
        # processed silenced this check once.
        for name in sorted(os.listdir(log_dir), reverse=True):
            if name.endswith(".md") and COMPLIANCE_AUDIT_ENTRY_RE.search(name):
                if _is_audit_record(os.path.join(log_dir, name)):
                    boundary = name
                    break
    # The date prefix on the entry's filename is the boundary. Same-day
    # commits before the audit re-report — the over-fire direction, accepted.
    since = None
    if boundary:
        m = re.match(r"^(\d{4}-\d{2}-\d{2})", boundary)
        since = m.group(1) if m else None

    commits, files = [], set()
    for _label, repo in repos(root):
        cmd = ["git", "log", "--format=%H%x00%s", "--name-only"]
        if since:
            cmd += ["--since", since]
        elif _has_commit(repo, DISPOSITION_BASELINE):
            cmd += [DISPOSITION_BASELINE + "..HEAD"]
        # A repository without the baseline and without a boundary date is
        # read whole: in a nested project that is the outer, whose history
        # postdates the obligation entirely.
        try:
            out = subprocess.run(cmd, cwd=repo, capture_output=True,
                                 text=True, timeout=20)
        except (OSError, subprocess.SubprocessError):
            out = None
        if out is None or out.returncode != 0:
            return {"stage": "AUDIT_LAG", "firing": False, "value": 0,
                    "slug": "compliance-audit-lag",
                    "message": "git unavailable; AUDIT-LAG not computed."}

        current_sha = None
        for line in out.stdout.splitlines():
            if "\x00" in line:
                sha, _subject = line.split("\x00", 1)
                current_sha = sha[:7]
            elif line.strip() and current_sha is not None:
                if any(line.startswith(p) for p in RULE_BEARING):
                    if current_sha not in commits:
                        commits.append(current_sha)
                    files.add(line.strip())

    return {
        "stage": "AUDIT_LAG",
        "firing": bool(commits),
        "value": len(commits),
        "slug": "compliance-audit-lag",
        "message": (
            "%d rule-bearing commit(s) since %s have not been covered by a "
            "compliance audit. The capture is one [audit] scoped to the "
            "changed files (delta scope): %s" % (
                len(commits),
                boundary if boundary else
                ("the disposition baseline — no compliance-audit entry exists "
                 "at all"),
                ", ".join(sorted(files)[:8]),
            )
            if commits else
            "No rule-bearing commits since the last compliance-audit entry"
            + (" (%s)." % boundary if boundary else ".")
        ),
    }


# --- BORN ---------------------------------------------------------------

# Both patterns tolerate an emphasised label (`**Rule gate:**`). Bolding a
# label is the ordinary Markdown instinct everywhere else in a LOG entry, and it
# has now defeated this check twice — the second time in a session that had just
# read the sentence describing the brittleness and then bolded every disposition
# it wrote. A rule depending on authors resisting an instinct they demonstrably
# cannot resist is not a rule.
#
# CHANGE THESE TWO TOGETHER, ALWAYS. Make only the first tolerant and a bolded
# `**Rule gate:** not needed` matches the disposition check while still failing
# the not-needed check — so it is counted as "run". That is a silent inversion
# of what the entry says, which is worse than the failure being fixed, where a
# bolded disposition is merely invisible.
DISPOSITION_RE = re.compile(r"^\*{0,2}Rule gate:", re.IGNORECASE | re.MULTILINE)
NOT_NEEDED_RE = re.compile(r"^\*{0,2}Rule gate:\*{0,2}\s*not needed",
                           re.IGNORECASE | re.MULTILINE)


PLACEHOLDER_HASH = "[HASH]"


def _backfill_pending(root):
    """True where any LOG entry still carries an unfilled `[HASH]` heading.

    An entry is written before its commit exists, so its heading carries a
    placeholder until the backfill replaces it with the real hash. Between the
    commit and the backfill the freshest commit has no entry matchable by
    heading — which is not a missing disposition, it is a disposition that
    cannot be matched yet.
    """
    log_dir = os.path.join(root, "LOG")
    if not os.path.isdir(log_dir):
        return False
    for name in os.listdir(log_dir):
        if not name.endswith(".md"):
            continue
        try:
            with open(os.path.join(log_dir, name), "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("#") and PLACEHOLDER_HASH in line:
                        return True
        except (OSError, UnicodeDecodeError):
            continue
    return False


def _rule_bearing_commits(root):
    """Commits after the baseline that touch a rule-bearing file.

    Returns (commits, error_message). Each commit is a dict with sha/subject.
    The baseline is what stops the signal reporting history that predates the
    obligation — every commit at or before it owes no disposition.

    **The newest commit is skipped while a backfill is outstanding.** Run
    immediately after a close, the check otherwise reports the commit just made
    as carrying no disposition, every single time — the dispositions are there,
    in entries whose headings still read `[HASH]`, and nothing can match them by
    heading until the backfill lands. A finding that fires on correct work at a
    predictable moment is the cry-wolf shape this project has repealed measures
    for twice.

    Two alternatives were refused. Filename-fallback matching reintroduces the
    misattribution the heading-only rule was written to fix. Running the check
    before the commit changes what the close's step means, for the same result
    this skip gets more cheaply.
    """
    all_repos = repos(root)
    with_baseline = [r for _l, r in all_repos if _has_commit(r, DISPOSITION_BASELINE)]
    if not with_baseline:
        # An unknown baseline is the likely cause — a shallow clone, or the
        # constant edited to a hash this repository doesn't carry. Say so
        # rather than silently falling back to the whole history, which would
        # re-report everything the baseline exists to exclude.
        return None, "git log failed (is %s in this repository?)" % DISPOSITION_BASELINE

    pending = _backfill_pending(root)
    commits = []
    for _label, repo in all_repos:
        # The repository carrying the baseline is read from it; a repository
        # without it — the outer of a nested project, created after the
        # obligation — is read whole, since every commit in it postdates it.
        rng = [DISPOSITION_BASELINE + "..HEAD"] if repo in with_baseline else []
        try:
            out = subprocess.run(
                ["git", "log", "-30", "--format=%H%x00%P%x00%s", "--name-only"] + rng,
                cwd=repo, capture_output=True, text=True, timeout=20,
            )
        except (OSError, subprocess.SubprocessError):
            return None, "git unavailable"
        if out.returncode != 0:
            return None, "git log failed in %s" % repo

        found, current = [], None
        for line in out.stdout.splitlines():
            if "\x00" in line:
                sha, parents, subject = line.split("\x00", 2)
                # A root commit creates the repository and imports files that
                # already existed — the outer of a wrap — so it authors no
                # rule and owes no disposition. Its file list is skipped too.
                if not parents.strip():
                    current = None
                    continue
                current = {"sha": sha[:7], "full": sha, "subject": subject,
                           "hits": False, "repo": repo}
                found.append(current)
            elif line.strip() and current is not None:
                if any(line.startswith(p) for p in RULE_BEARING):
                    current["hits"] = True

        # `git log` returns newest first, so found[0] is that repository's
        # HEAD. Skipped only while a placeholder is outstanding, so a project
        # with every heading backfilled is checked exactly as before. Per
        # repository, because a nested close makes one commit in each.
        if found and pending:
            found = found[1:]
        commits.extend(found)

    return [c for c in commits if c["hits"]], None


def _log_dispositions(root):
    """Map of short sha -> set of disposition kinds found in LOG entries.

    Kinds are "run" and "not needed". A commit's entry is matched by the hash
    in the entry's HEADING — the position the backfill writes and the one the
    entry's own identity rests on.

    Prose mentions of a hash do NOT count, and that restriction is the fix for
    a real misattribution. This used to match a hash anywhere in the entry, so
    an entry citing a prior commit — which entries in this project do
    constantly — silently donated its own disposition to that commit. It
    flagged `b51d205`, a two-file commit whose own entry records `run`, purely
    because an unrelated entry described reproducing a test "against a detached
    checkout of b51d205".
    """
    log_dir = os.path.join(root, "LOG")
    found = {}
    if not os.path.isdir(log_dir):
        return found
    for name in os.listdir(log_dir):
        if not name.endswith(".md"):
            continue
        try:
            with open(os.path.join(log_dir, name), "r", encoding="utf-8") as f:
                text = f.read()
        except OSError:
            continue
        if not DISPOSITION_RE.search(text):
            continue
        kind = "not needed" if NOT_NEEDED_RE.search(text) else "run"
        # The heading is the entry's first non-empty line, written as
        # "# <sha> — <title>". Only hashes there attribute the disposition.
        heading = next((ln for ln in text.splitlines() if ln.strip()), "")
        for sha in re.findall(r"\b([0-9a-f]{7,40})\b", heading):
            found.setdefault(sha[:7], set()).add(kind)
    return found


def signal_born(root):
    """Commits that should carry a gate-disposition line and do not.

    Over-fires by design: touching docs/ for a typo is not authoring a rule.
    A false fire costs one line — "not needed, typo fix". FAQ-sync makes
    exactly this trade and it is why it works.

    Bounded by DISPOSITION_BASELINE, so it reports only commits that were
    subject to the obligation when they were made.
    """
    rule_commits, err = _rule_bearing_commits(root)
    if err:
        return {"stage": "BORN", "firing": False, "value": 0,
                "slug": "rule-gate-dispositions-missing",
                "message": err + "; BORN not computed."}

    dispositions = _log_dispositions(root)
    missing = [c for c in rule_commits if c["sha"] not in dispositions]
    return {
        "stage": "BORN",
        "firing": bool(missing),
        "value": len(missing),
        "slug": "rule-gate-dispositions-missing",
        "message": (
            f"{len(missing)} of the {len(rule_commits)} commits since "
            f"{DISPOSITION_BASELINE} touching rule-bearing files have no "
            "'Rule gate:' disposition line in any LOG entry: "
            + ", ".join(f"{c['sha']}" for c in missing[:8])
            if missing else
            f"All {len(rule_commits)} rule-bearing commits since "
            f"{DISPOSITION_BASELINE} carry a gate disposition."
        ),
    }


# --- CONTRADICTED -------------------------------------------------------


def signal_contradicted(root):
    """Commits whose always-loaded rule count ROSE while their LOG entry says
    the gate was not needed.

    BORN is a PRESENCE check: a session that added four rules and wrote
    "Rule gate: not needed — typo fix" satisfies it completely. That reasoning
    holds against omission and does nothing against a FALSE artifact, and the
    two had never been separated.

    This compares two artifacts that are supposed to agree — the corpus size at
    a commit, and what that commit's LOG entry claims about the gate — so it
    needs no judgment. It runs at the NEXT session's start, over a commit
    already written and no longer editable to suit the check; a check at the
    close would be the session judging its own disposition in the same breath
    as writing it, which is the self-report problem this exists to close.

    One-directional by design, and unanimous:

        count ROSE  + EVERY disposition "not needed"   ->  FLAG
        count ROSE  + any disposition "run — ..."      ->  fine
        count FELL or unchanged                        ->  fine, ALWAYS

    An eviction pass lowers the count and owes no disposition defence, so a fall
    is never a finding.

    The unanimity requirement is what makes the check usable on a large run. A
    commit is the wrong unit once one run ships sixteen items under one hash:
    a single item legitimately recording "not needed" put that kind into the
    commit's set while a sibling item authored a rule and correctly recorded
    "run", and the signal reported a contradiction between two artifacts that
    agreed. The COST is stated rather than left to be found: a mixed run in
    which one item genuinely authored a rule and wrongly recorded "not needed"
    now passes silently, because a sibling entry recorded "run". That is a real
    loss of coverage, accepted against a check that would otherwise fire
    falsely at every large run — and a check that cries wolf gets skimmed past.

    WHAT IT CANNOT DO, and must not claim: it cannot tell whether a gate that
    *ran* ran honestly. A dishonest "run — considered and kept" defeats it
    completely. It catches omission-dressed-as-disposition, not bad judgment. A
    check that over-claims is worse than none — it makes the corpus look guarded
    when it is only partly guarded.

    The count is the same proxy MEASURED uses, so this reports a contradiction
    between two artifacts rather than a measured fact about rules.
    """
    rule_commits, err = _rule_bearing_commits(root)
    if err:
        return {"stage": "CONTRADICTED", "firing": False, "value": 0,
                "slug": "rule-gate-disposition-is-unverified",
                "message": err + "; CONTRADICTED not computed."}

    dispositions = _log_dispositions(root)
    flagged = []
    for commit in rule_commits:
        kinds = dispositions.get(commit["sha"], set())
        # EVERY disposition naming this commit must say "not needed". A commit
        # is the wrong unit once a run ships sixteen items under one hash: one
        # item legitimately recording "not needed" — a script fix, a test
        # repair — sat alongside a sibling that authored a rule and correctly
        # recorded "run", and the pair was read as a contradiction between two
        # artifacts that do not in fact disagree.
        if not kinds or kinds != {"not needed"}:
            continue
        delta = _count_delta_at(root, commit["full"], commit.get("repo", root))
        if delta is not None and delta > 0:
            flagged.append((commit["sha"], delta))

    return {
        "stage": "CONTRADICTED",
        "firing": bool(flagged),
        "value": len(flagged),
        "slug": "rule-gate-disposition-is-unverified",
        "message": (
            "%d commit(s) where EVERY gate disposition says 'not needed' while "
            "the always-loaded rule-statement count ROSE: %s. This is a "
            "contradiction between two artifacts, not proof of a bad rule. Two "
            "things it does NOT cover: a commit whose gate is recorded as run "
            "(it cannot tell an honest 'run' from a dishonest one), and a mixed "
            "run where one item wrongly recorded 'not needed' alongside a "
            "sibling that recorded 'run'." % (
                len(flagged),
                ", ".join("%s (+%d)" % (sha, d) for sha, d in flagged[:8]),
            )
            if flagged else
            "No commit since %s claims the gate was not needed while the "
            "corpus grew." % DISPOSITION_BASELINE
        ),
    }


def _count_delta_at(root, rev, repo=None):
    """Always-loaded statement count at `rev` minus the count at its parent.

    Returns None where either side can't be read — a first commit, a file that
    didn't exist yet, an unreadable blob. Reuses the same counter MEASURED
    uses via `git show <rev>:<path>`, so there is no second counting logic to
    drift. `repo` is the repository the commit belongs to; only the corpus
    files that repository holds are counted, since a commit in one repository
    cannot have changed a file in the other.
    """
    repo = repo or root
    files = [rel for rel in ALWAYS_LOADED
             if os.path.normcase(locate(root, rel)[0]) == os.path.normcase(repo)]
    if not files:
        return None
    before = _count_at_rev(root, rev + "^", files)
    after = _count_at_rev(root, rev, files)
    if before is None or after is None:
        return None
    return after - before


# --- MAINTAINED ---------------------------------------------------------

def _normalise_statement(line):
    text = re.sub(r"[*`_\[\]]", "", line).strip().lower()
    text = re.sub(r"[^a-z0-9 ]+", " ", text)
    return " ".join(text.split())


def signal_maintained(root, threshold=0.82):
    """Near-duplicate rule statements across the always-loaded corpus.

    This IS codification — one subject, one rule, stated once — which is the
    eviction technique the authoring gate never absorbed. It catches drift
    that is not growth, which is precisely the hole AUDITED's ceiling trigger
    leaves open.

    Flags for a human to judge, never a gate: two rules may legitimately say
    similar things in different contexts.
    """
    statements = []
    for rel in ALWAYS_LOADED:
        path = os.path.join(*locate(root, rel))
        try:
            with open(path, "r", encoding="utf-8") as f:
                lines = f.read().splitlines()
        except OSError:
            continue
        for n, raw in enumerate(lines, 1):
            if BULLET_RE.match(raw) or BOLD_LEAD_RE.match(raw.strip()):
                norm = _normalise_statement(raw)
                if len(norm.split()) >= 6:
                    statements.append((rel, n, norm))

    pairs = []
    for i in range(len(statements)):
        _, ln_i, a = statements[i]
        words_a = set(a.split())
        for j in range(i + 1, len(statements)):
            _, ln_j, b = statements[j]
            words_b = set(b.split())
            union = words_a | words_b
            if not union:
                continue
            score = len(words_a & words_b) / len(union)
            if score >= threshold:
                pairs.append((ln_i, ln_j, round(score, 2)))

    return {
        "stage": "MAINTAINED",
        "firing": bool(pairs),
        "value": len(pairs),
        "slug": "near-duplicate-rule-statements",
        "message": (
            f"{len(pairs)} near-duplicate rule statement pair(s): "
            + "; ".join(f"lines {a}~{b} ({s})" for a, b, s in pairs[:8])
            if pairs else "No near-duplicate rule statements found."
        ),
    }


# --- REPEALED -----------------------------------------------------------

def load_retired_terms(root):
    """Terms recorded as retired. Source data, not derived state."""
    path = os.path.join(*locate(root, RETIRED_TERMS_FILE))
    terms = []
    # Only read under the "## The list" heading. The file explains its own
    # format above that point, and the format example is a line of exactly the
    # shape the parser matches — which on the first run loaded the literal word
    # "term" as a retired term and flagged half the corpus.
    in_list = False
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if re.match(r"^##\s+The list\s*$", line.strip(), re.IGNORECASE):
                    in_list = True
                    continue
                if not in_list:
                    continue
                match = re.match(r"^-\s+`([^`]+)`\s*—\s*(.*)$", line.strip())
                if match:
                    terms.append((match.group(1), match.group(2)))
    except OSError:
        return []
    return terms


# A line that says a term IS retired is correct text, not a stale reference.
# Without this the signal fires on every doc doing the right thing — including
# the rules that record the retirement — which is how a lint becomes noise.
#
# Widened 2026-08-12 from the phrasings that actually appeared in the corpus:
# a doc says a mechanism is gone in more ways than the first list imagined.
RETIREMENT_CONTEXT = (
    "retired", "retire", "no longer", "is gone", "are gone", "it's gone",
    "was removed", "were removed", "repealed", "superseded", "deprecated",
    "stays retired", "never write", "don't write", "do not write", "not a",
    "vestigial", "reintroduce", "used to", "formerly", "replaced by",
    "there used to be", "has been removed", "does not exist",
)

# Files that RECORD what was true when they were written. Editing a retired
# term out of one falsifies the record, so a hit inside one is never a finding
# and reporting it is pure noise. Same exclusion list the identity rename
# carries, and for the same reason.
ARCHIVAL_PATHS = (
    # This file itself. Its comments name retired terms as worked examples of
    # what the detector must and must not match — the same reason the
    # retired-terms list is already excluded. A file whose subject is retired
    # terms will always name them.
    "workshop/resources/rule_signals.py",
    "workshop/resources/research/",
    "workshop/resources/testing/",
    "workshop/resources/plugin-behaviour-retired.md",
    "INBOX/archive/",
    "LOG/",
)

# A dated file at the top of resources/ is a record of an event, not a live
# rule — e.g. resources/2026-08-09-emergency-revert-plan.md.
DATED_FILE_RE = re.compile(r"(^|/)\d{4}-\d{2}-\d{2}-")


def _is_archival(rel_path):
    return (
        any(rel_path.startswith(p) for p in ARCHIVAL_PATHS)
        or DATED_FILE_RE.search(rel_path) is not None
    )


def _term_appears_as_a_name(term, raw):
    """True where `term` is used as the NAME of the mechanism, not incidentally.

    The terms include field names ending in a colon — `Blocks:`, `Depends on:`,
    `Editor:`. A bare case-insensitive substring test matches the Python line
    `for b in blocks:` and the prose "not only when it blocks:", neither of
    which mentions the retired field at all. Both were in the corpus, and
    between them they are most of what the signal was reporting.

    So a colon-terminated term counts only where it is quoted in backticks,
    bolded, or begins a line — the three ways a document actually names a
    field. Terms that are not field names (a filename, a docset) keep the
    plain substring test, which is right for them.
    """
    low = raw.lower()
    t = term.lower()
    if not term.rstrip().endswith(":"):
        # Whole-word at each end, or `docset A` matches the words "docset and"
        # — which is what it was doing, in this project's own CLAUDE.md.
        # Anchored only where the edge character is one \b understands, so a
        # term like `plugin-behaviour.md` still matches.
        pattern = re.escape(t)
        if t[:1].isalnum():
            pattern = r"\b" + pattern
        if t[-1:].isalnum():
            pattern = pattern + r"\b"
        return re.search(pattern, low) is not None
    if ("`" + t) in low or ("**" + t) in low:
        return True
    return low.lstrip().lstrip("-*# ").startswith(t)


def _paragraph_says_retired(lines, index):
    """True where the hit's own paragraph says the mechanism is retired.

    The context test used to read one line. Prose splits a sentence across
    lines constantly — "still carry an `Editor:` … line — all three settings
    are retired" puts the term and the word `retired` on different lines — so a
    per-line test flagged correct writing. The paragraph is the contiguous run
    of non-blank lines around the hit: structural, with no window size to pick.
    """
    start = index
    while start > 0 and lines[start - 1].strip():
        start -= 1
    end = index
    while end + 1 < len(lines) and lines[end + 1].strip():
        end += 1
    block = " ".join(lines[start:end + 1]).lower()
    return any(c in block for c in RETIREMENT_CONTEXT)


def signal_repealed(root):
    """Live rules naming a term on the retired list.

    This is where the sunset research finally transfers. A sunset clause works
    because inaction repeals; a duty to review fails because inaction is
    silent. Time-based expiry does not transfer here — no calendar pressure,
    and a doc that silently expires is not safe. What transfers is the
    default-state principle: retiring a mechanism automatically puts every
    rule that mentions it into question, and leaving the references standing
    produces a visible signal. No number, no calendar.
    """
    terms = load_retired_terms(root)
    retired_path = os.path.join(*locate(root, RETIRED_TERMS_FILE))
    if not terms and not os.path.isfile(retired_path):
        # A missing list is a footing failure, not a clean result. The old
        # behaviour returned a no-list line grouped with the passes, which
        # read as clean while one of the five checks had not run at all —
        # worse than a failure, which would at least be visible.
        raise SystemExit(
            "rule_signals: FOOTING FAILURE — no retired-terms list at %s. "
            "The retired-terms check cannot run, so no report is produced at "
            "all: a clean-looking result with a dead check inside it is the "
            "failure this refusal exists to prevent. Fix the path or restore "
            "the file." % RETIRED_TERMS_FILE)
    if not terms:
        return {"stage": "REPEALED", "firing": False, "value": 0,
                "slug": "live-rules-name-retired-terms",
                "message": "Retired-terms list present and empty — nothing "
                           "is retired, so nothing can be named."}

    scan_roots = ["plugin/throughliner", "workshop/resources", "FAQ",
                  "CLAUDE.md", "SPEC.md"]
    hits = []
    for rel in scan_roots:
        base_repo, rel = locate(root, rel)
        base = os.path.join(base_repo, rel)
        files = []
        if os.path.isfile(base):
            files = [base]
        else:
            for dirpath, dirnames, filenames in os.walk(base):
                dirnames[:] = [d for d in dirnames if d != "__pycache__"]
                files.extend(
                    os.path.join(dirpath, n) for n in filenames
                    if n.endswith((".md", ".py"))
                )
        for path in files:
            if os.path.abspath(path) == os.path.abspath(retired_path):
                continue
            try:
                with open(path, "r", encoding="utf-8") as f:
                    lines = f.read().splitlines()
            except OSError:
                continue
            # Relative to the repository that holds the file, so the archival
            # paths match in a nested project exactly as in a flat one.
            rel_path = os.path.relpath(path, base_repo).replace("\\", "/")
            if _is_archival(rel_path):
                continue
            seen = set()
            for n, raw in enumerate(lines, 1):
                if _paragraph_says_retired(lines, n - 1):
                    continue
                for term, _why in terms:
                    key = (rel_path, term)
                    if key in seen:
                        continue
                    if _term_appears_as_a_name(term, raw):
                        seen.add(key)
                        hits.append((f"{rel_path}:{n}", term))

    return {
        "stage": "REPEALED",
        "firing": bool(hits),
        "value": len(hits),
        "slug": "live-rules-name-retired-terms",
        "message": (
            f"{len(hits)} live reference(s) to retired terms: "
            + "; ".join(f"{p} names '{t}'" for p, t in hits[:8])
            if hits else "No live references to retired terms."
        ),
    }


# --- Board --------------------------------------------------------------

def board(root):
    measured = signal_measured(root)
    return [
        measured,
        signal_audit_lag(root),
        signal_born(root),
        signal_contradicted(root),
        signal_maintained(root),
        signal_repealed(root),
    ]


# What each entry actually reads, in plain words. The internal stage names
# (BORN, CONTRADICTED, MAINTAINED, REPEALED, MEASURED, AUDITED) stay as the
# dict keys and inside the capture slugs, where they are stable identifiers —
# but they never reach the output any more. They were invented here, they
# reached the user's always-loaded CLAUDE.md without ever being explained, and
# the user was never the intended audience of this output.
CHECK_LABELS = {
    "MEASURED": "How much rule text there is",
    "AUDIT_LAG": "Rule changes are covered by a compliance audit",
    "BORN": "Rule-bearing commits carry a gate line",
    "CONTRADICTED": "No commit says 'gate not needed' while rules grew",
    "MAINTAINED": "No two rules say nearly the same thing",
    "REPEALED": "No live rule names a retired mechanism",
}

# The framing this whole script had wrong until 2026-08-14. On 2026-08-13 it
# ran clean while five real rule defects were found by conversation in the same
# session — a bare number shipped into the output style, the turn-by-turn asks
# removed from every session, the rule gate having no site in the build, this
# board having no trigger, and a shipped component missing from the project
# map. Not one of the five checks asks whether a rule is CORRECT, whether it
# FIRES, or whether it improved anything: they ask whether a required line
# exists, whether two artifacts contradict, whether two rules read alike,
# whether a rule names a retired word, and whether rule changes have been
# audited. So a clean run is evidence the paperwork was completed, and
# reporting that as health is the over-claiming this project's own standard
# forbids.
CLEAN_RUN_NOTE = (
    "What a clean result means: these five things were checked and nothing was "
    "found.\nIt is not evidence the rules are correct, that they fire, or that "
    "they made anything better —\nno check here asks any of those questions."
)


PLANNING_ENTRY_RE = re.compile(r"-plan(-\d+)?\.md$", re.IGNORECASE)

# A planning entry's body fields, per done.md's plan/setup template. Since the
# per-entry split a planning close writes one entry PER ITEM PROCESSED, named
# by the item's slug — so the filename pattern above matches nothing and the
# window silently became full history (176 entries at two real openings). The
# body fields are what a planning entry carries whatever it is named.
PLANNING_BODY_RE = re.compile(
    r"^\*{0,2}(Queue changes|Work processed):", re.IGNORECASE | re.MULTILINE)

# A disposition recording a refusal — the outcome the /plan-opening surface
# exists for. Matched on the line's own text.
REFUSAL_RE = re.compile(r"refus|reject", re.IGNORECASE)


def _latest_planning_entry(log_dir, names):
    """Newest LOG entry written by a planning close.

    Filename match first (pre-split entries), then body-field match — reading
    newest-first so the scan usually stops after a few files.
    """
    boundary = None
    for name in names:
        if PLANNING_ENTRY_RE.search(name):
            boundary = name
    for name in reversed(names):
        if boundary is not None and name <= boundary:
            break
        try:
            with open(os.path.join(log_dir, name), "r", encoding="utf-8") as f:
                text = f.read()
        except OSError:
            continue
        if PLANNING_BODY_RE.search(text):
            return name
    return boundary


def dispositions(root, window=True):
    """Every `Rule gate:` line on record, newest LOG entry first.

    **A mode behind a flag, not a fifth check.** Nothing is wrong when this
    prints, so it joins neither class the board counts — it reuses the same
    `Rule gate:` parsing the checks already do, and stays out of the
    denominator.

    **It reads every disposition, not only refusals.** The question it answers
    is "what did I ask for that did not get built", and refusals are half of
    that; the same parse yields the rest for one more column.

    Windowed to entries since the most recent planning LOG entry, because that
    is the moment someone actually looks. `window=False` prints the whole
    history. Where no planning entry exists, the window cannot be established —
    the caller says so and names the flag, rather than silently printing
    nothing, which would read as "no refusals".

    **The guard, stated wherever this prints.** It reports what a disposition
    *claims*. It cannot say whether a refusal was correct, and it cannot see a
    proposal dropped in conversation before any disposition was written.
    """
    log_dir = os.path.join(root, "LOG")
    if not os.path.isdir(log_dir):
        return [], "no LOG/ directory"

    names = sorted(n for n in os.listdir(log_dir) if n.endswith(".md")
                   and n != "index.md")
    boundary = _latest_planning_entry(log_dir, names)
    scope = names
    note = None
    if window:
        if boundary is None:
            note = ("no planning entry found, so the since-last-plan window "
                    "could not be established — showing full history "
                    "(--dispositions-all prints this deliberately)")
        else:
            scope = [n for n in names if n >= boundary]

    found = []
    for name in scope:
        try:
            with open(os.path.join(log_dir, name), "r", encoding="utf-8") as f:
                text = f.read()
        except OSError:
            continue
        heading = next((ln for ln in text.splitlines() if ln.strip()), "")
        shas = re.findall(r"\b([0-9a-f]{7,40})\b", heading)
        sha = shas[0][:7] if shas else "unrecorded"
        for line in text.splitlines():
            if DISPOSITION_RE.match(line):
                outcome = ("not needed" if NOT_NEEDED_RE.match(line) else "run")
                found.append({
                    "entry": name, "sha": sha, "outcome": outcome,
                    "text": line.strip(),
                    "refusal": bool(REFUSAL_RE.search(line)),
                })
    found.reverse()
    return found, note


DISPOSITION_GUARD = (
    "This reports what each disposition SAYS. It cannot tell whether a refusal "
    "was correct,\nand it cannot see a proposal dropped in conversation before "
    "any disposition was written."
)


def print_dispositions(root, window=True):
    found, note = dispositions(root, window)
    scope = "since the last planning session" if window else "full history"
    print(f"## Rule-gate dispositions — {len(found)} on record ({scope})")
    if note:
        print(f"\nNote: {note}")
    print()
    if not found:
        print("- none recorded in this window.")
    for d in found:
        mark = " — REFUSAL" if d.get("refusal") else ""
        print(f"- {d['entry']} [{d['sha']}] — {d['outcome']}{mark}")
        print(f"    {d['text']}")
    refusals = sum(1 for d in found if d.get("refusal"))
    print()
    # The /plan opening surfaces this listing only where the window holds a
    # refusal; this line is what that check reads.
    print(f"Refusal-bearing dispositions in window: {refusals}")
    print()
    print(DISPOSITION_GUARD)
    return 0


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("-")]
    flags = {a for a in argv[1:] if a.startswith("-")}
    root = args[0] if args else "."
    if "--dispositions" in flags or "--dispositions-all" in flags:
        return print_dispositions(root, window="--dispositions-all" not in flags)
    entries = board(root)
    # Reports are instruments; signals are alarms. Only signals can fire, so
    # only signals are counted — a denominator that included the reports
    # invited the reading that six things are being watched when four are, and
    # this project's own standard is that a check which over-claims makes the
    # corpus look guarded when it is only partly guarded.
    reports = [s for s in entries if s.get("kind") == "report"]
    signals = [s for s in entries if s.get("kind") != "report"]
    firing = [s for s in signals if s["firing"]]

    print(
        f"## Rule-corpus checks — {len(firing)} of {len(signals)} found something"
    )
    if reports:
        print()
        print("### Measurements — no threshold, so nothing here can be failed.")
        for s in reports:
            print(f"- {CHECK_LABELS.get(s['stage'], s['stage'])}: {s['message']}")
    print()
    print("### Checks — each can find something, and what it finds becomes work.")
    for s in signals:
        mark = "FOUND SOMETHING" if s["firing"] else "nothing found"
        label = CHECK_LABELS.get(s["stage"], s["stage"])
        print(f"- {label} [{mark}] {s['message']}")
    if firing:
        print()
        print("Each check that found something files one capture in Unprocessed, "
              "under the slug shown below.")
        print("A check is already satisfied — file nothing — while ANY open work "
              "item carries its slug,")
        print("in EITHER section: Unprocessed or Processed, captured or designed "
              "and cleared to run.")
        print("Only deleting that item re-arms the check. Nothing here scans the "
              "queue; you perform this check.")
        for s in firing:
            print(f"  [{s['slug']}]")
    print()
    print(CLEAN_RUN_NOTE)
    print()
    print(GROWTH_NOTE)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
