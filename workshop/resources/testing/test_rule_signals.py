#!/usr/bin/env python3
"""Regression tests for rule_signals.py's backfill skip.

Host-only dev artifact — not shipped in the plugin package.

Run:  py resources/testing/test_rule_signals.py
(Plain script, never pytest — see CLAUDE.md's scripting constraints.)

A real git repository is built per case, because the thing under test reads
`git log` and the defect is specifically about which commit is newest.
"""

import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile

for _stream in (sys.stderr, sys.stdout):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError, OSError):
        pass

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SCRIPT = os.path.join(ROOT, "workshop", "resources", "rule_signals.py")

_spec = importlib.util.spec_from_file_location("rule_signals", SCRIPT)
signals = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(signals)

failures = []


def check(label, ok, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + label + ("" if ok else f" — {detail}"))
    if not ok:
        failures.append(label)


def git(root, *args):
    subprocess.run(["git"] + list(args), cwd=root, check=True,
                   capture_output=True, text=True, errors="replace")


def repo(heading):
    """A repo with a baseline commit, then one commit touching a rule file.

    `heading` is the LOG entry's first line — a real hash or the `[HASH]`
    placeholder — written before the rule-bearing commit is made, exactly as a
    close writes it.
    """
    root = tempfile.mkdtemp(prefix="rule-signals-test-")
    git(root, "init", "-q")
    git(root, "config", "user.email", "t@example.com")
    git(root, "config", "user.name", "T")

    os.makedirs(os.path.join(root, "LOG"))
    with open(os.path.join(root, "README.md"), "w", encoding="utf-8") as f:
        f.write("baseline\n")
    git(root, "add", "README.md")
    git(root, "commit", "-q", "-m", "baseline")
    baseline = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=root,
                              capture_output=True, text=True).stdout.strip()

    docs = os.path.join(root, "plugin", "throughliner", "docs")
    os.makedirs(docs)
    with open(os.path.join(docs, "plan.md"), "w", encoding="utf-8") as f:
        f.write("A rule-bearing file.\n")
    with open(os.path.join(root, "LOG", "2026-08-21-thing.md"), "w",
              encoding="utf-8") as f:
        f.write(f"# {heading} — a session\n\nRule gate: run — admitted.\n")
    git(root, "add", "-A")
    git(root, "commit", "-q", "-m", "a rule-bearing commit")
    return root, baseline


def rule_commits(root, baseline):
    signals.DISPOSITION_BASELINE = baseline
    return signals._rule_bearing_commits(root)


def test_placeholder_entry_suppresses_the_freshest_commit():
    """Run immediately after a close, the check must find nothing.

    The disposition is written and correct; its heading just cannot be matched
    to a hash that did not exist when the entry was written.
    """
    root, baseline = repo("[HASH]")
    commits, err = rule_commits(root, baseline)
    check("a pending backfill hides the newest commit",
          err is None and commits == [], f"{err!r} {commits!r}")
    shutil.rmtree(root, ignore_errors=True)


def test_backfilled_entry_restores_normal_behaviour():
    """With every heading backfilled, nothing is skipped."""
    root, baseline = repo("PLACEHOLDER")
    real = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=root,
                          capture_output=True, text=True).stdout.strip()
    entry = os.path.join(root, "LOG", "2026-08-21-thing.md")
    with open(entry, "w", encoding="utf-8") as f:
        f.write(f"# {real} — a session\n\nRule gate: run — admitted.\n")
    commits, err = rule_commits(root, baseline)
    check("a backfilled repository checks the newest commit as before",
          err is None and len(commits) == 1, f"{err!r} {commits!r}")
    shutil.rmtree(root, ignore_errors=True)


def test_placeholder_only_counts_in_a_heading():
    """A prose mention of the placeholder is not a pending backfill."""
    root = tempfile.mkdtemp(prefix="rule-signals-test-")
    os.makedirs(os.path.join(root, "LOG"))
    with open(os.path.join(root, "LOG", "e.md"), "w", encoding="utf-8") as f:
        f.write("# abc1234 — a session\n\nThe close writes [HASH] first.\n")
    check("a placeholder in prose does not read as pending",
          not signals._backfill_pending(root))
    shutil.rmtree(root, ignore_errors=True)


def test_no_log_directory_is_not_pending():
    root = tempfile.mkdtemp(prefix="rule-signals-test-")
    check("a project with no LOG/ is never pending",
          not signals._backfill_pending(root))
    shutil.rmtree(root, ignore_errors=True)


def test_nested_project_reads_both_histories():
    """A nested project's rule corpus straddles two repositories.

    The outer holds CLAUDE.md and LOG/; the inner holds the shipped docs. Both
    histories carry rule-bearing commits, and the dispositions for both sit in
    the outer's LOG. Run from the outer, the check must find both commits and
    match each to its disposition — before this, run from either repository it
    saw half the corpus.
    """
    outer = tempfile.mkdtemp(prefix="rule-signals-nested-")
    git(outer, "init", "-q")
    git(outer, "config", "user.email", "t@example.com")
    git(outer, "config", "user.name", "T")
    os.makedirs(os.path.join(outer, "LOG"))
    inner = os.path.join(outer, "product")
    os.makedirs(inner)
    git(inner, "init", "-q")
    git(inner, "config", "user.email", "t@example.com")
    git(inner, "config", "user.name", "T")

    # The inner: a baseline commit, then a commit touching a shipped doc.
    with open(os.path.join(inner, "README.md"), "w", encoding="utf-8") as f:
        f.write("product\n")
    git(inner, "add", "README.md")
    git(inner, "commit", "-q", "-m", "baseline")
    baseline = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=inner,
                              capture_output=True, text=True).stdout.strip()
    docs = os.path.join(inner, "plugin", "throughliner", "docs")
    os.makedirs(docs)
    with open(os.path.join(docs, "plan.md"), "w", encoding="utf-8") as f:
        f.write("A rule-bearing file.\n")
    git(inner, "add", "-A")
    git(inner, "commit", "-q", "-m", "inner rule commit")
    inner_sha = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=inner,
                               capture_output=True, text=True).stdout.strip()

    # The outer: CLAUDE.md with the Visibility line naming the inner, then a
    # second commit touching it (rule-bearing in the outer).
    claude = os.path.join(outer, "CLAUDE.md")
    with open(claude, "w", encoding="utf-8") as f:
        f.write("# Project\n\nVisibility: nested — the outer repository holds "
                "the documents; the inner repository (`product/`) holds only "
                "the product.\n")
    with open(os.path.join(outer, ".gitignore"), "w", encoding="utf-8") as f:
        f.write("product/\n")
    git(outer, "add", "CLAUDE.md", ".gitignore")
    git(outer, "commit", "-q", "-m", "outer first commit")
    with open(claude, "a", encoding="utf-8") as f:
        f.write("\n- **A rule.**\n")
    git(outer, "add", "CLAUDE.md")
    git(outer, "commit", "-q", "-m", "outer rule commit")
    outer_sha = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=outer,
                               capture_output=True, text=True).stdout.strip()

    # Dispositions for both, in the outer's LOG.
    with open(os.path.join(outer, "LOG", "2026-09-05-inner.md"), "w",
              encoding="utf-8") as f:
        f.write(f"# {inner_sha} — inner session\n\nRule gate: run — admitted.\n")
    with open(os.path.join(outer, "LOG", "2026-09-05-outer.md"), "w",
              encoding="utf-8") as f:
        f.write(f"# {outer_sha} — outer session\n\nRule gate: run — admitted.\n")

    check("the inner is found from the Visibility line",
          signals.inner_root(outer) == inner, repr(signals.inner_root(outer)))
    commits, err = rule_commits(outer, baseline)
    shas = {c["sha"] for c in commits}
    check("both repositories' rule-bearing commits are read",
          err is None and shas == {inner_sha, outer_sha}, f"{err!r} {shas!r}")
    check("the outer's root commit, which imported CLAUDE.md, owes no "
          "disposition", len(commits) == 2, repr([c["subject"] for c in commits]))
    born = signals.signal_born(outer)
    check("each commit matches its disposition in the outer's LOG",
          not born["firing"], born["message"])
    total, per_file = signals.count_statements(
        outer, ["CLAUDE.md", "plugin/throughliner/docs/plan.md"])
    check("corpus files are read from whichever repository holds them",
          set(per_file) == {"CLAUDE.md", "plugin/throughliner/docs/plan.md"},
          repr(per_file))
    shutil.rmtree(outer, ignore_errors=True)


def test_flat_project_has_no_inner():
    root = tempfile.mkdtemp(prefix="rule-signals-flat-")
    os.makedirs(os.path.join(root, "LOG"))
    check("a flat project reports no inner repository",
          signals.inner_root(root) is None)
    check("a flat project reads one repository",
          [l for l, _ in signals.repos(root)] == ["outer"])
    shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    print("test_rule_signals")
    test_nested_project_reads_both_histories()
    test_flat_project_has_no_inner()
    test_placeholder_entry_suppresses_the_freshest_commit()
    test_backfilled_entry_restores_normal_behaviour()
    test_placeholder_only_counts_in_a_heading()
    test_no_log_directory_is_not_pending()
    print(f"\n{len(failures)} failure(s)" if failures else "\nall passed")
    sys.exit(1 if failures else 0)
