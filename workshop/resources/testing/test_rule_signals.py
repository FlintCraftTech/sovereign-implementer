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

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT = os.path.join(ROOT, "resources", "rule_signals.py")

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


if __name__ == "__main__":
    print("test_rule_signals")
    test_placeholder_entry_suppresses_the_freshest_commit()
    test_backfilled_entry_restores_normal_behaviour()
    test_placeholder_only_counts_in_a_heading()
    test_no_log_directory_is_not_pending()
    print(f"\n{len(failures)} failure(s)" if failures else "\nall passed")
    sys.exit(1 if failures else 0)
