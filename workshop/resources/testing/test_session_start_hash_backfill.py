#!/usr/bin/env python3
"""Regression tests for session_start.py's hash backfill and its alarm.

Host-only dev artifact — not shipped in the plugin package.

Run:  py workshop/resources/testing/test_session_start_hash_backfill.py

No test framework, matching the suites alongside it.

Why this exists ([near-miss-hash-token-defeats-both-checks]): both the backfill
and its alarm matched the literal word `[HASH]`, so a near-miss token —
`[COMMIT_HASH]`, `PENDING` — in hash position was neither filled nor reported.
Eight of them sat in a consumer's LOG for twelve days. Both now key on the
SLOT: any non-hash token before the first " — " on a record heading or an
index line is a placeholder. Body prose mentioning a token is untouched.

Each case builds a small git repository, because the backfill reads commits.
"""

import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
HOOK = os.path.join(ROOT, "plugin", "throughliner", "hooks", "session_start.py")

_spec = importlib.util.spec_from_file_location("session_start", HOOK)
hook = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(hook)

failures = []


def check(name, condition, detail=""):
    if condition:
        print("  ok   " + name)
    else:
        print("  FAIL " + name + ("\n       " + detail if detail else ""))
        failures.append(name)


def git(cwd, *args):
    return subprocess.run(["git"] + list(args), cwd=cwd, capture_output=True,
                          text=True, encoding="utf-8")


def repo():
    d = tempfile.mkdtemp(prefix="hash-backfill-")
    git(d, "init", "-q")
    git(d, "config", "user.email", "suite@example.invalid")
    git(d, "config", "user.name", "suite")
    os.mkdir(os.path.join(d, "LOG"))
    return d


def write(d, rel, text):
    with open(os.path.join(d, rel), "w", encoding="utf-8", newline="") as f:
        f.write(text)


def read(d, rel):
    with open(os.path.join(d, rel), "r", encoding="utf-8") as f:
        return f.read()


# --- 1. a [COMMIT_HASH] heading is filled from the fixture commit -------------
d = repo()
write(d, "LOG/2026-01-01-thing.md",
      "# [COMMIT_HASH] — Fixture entry about the thing\n\nBody.\n")
git(d, "add", "LOG")
git(d, "commit", "-q", "-m", "fixture")
expected = git(d, "log", "-1", "--pretty=%h").stdout.strip()
report = hook.backfill_log_hashes(d)
after = read(d, "LOG/2026-01-01-thing.md")
check("a [COMMIT_HASH] heading is filled with the commit's hash",
      after.startswith("# %s — Fixture entry" % expected), repr(after))
check("the report says one placeholder was filled",
      "filled 1 commit-hash placeholder" in report, repr(report))
shutil.rmtree(d, ignore_errors=True)

# --- 2. a PENDING index line no commit matches is reported --------------------
d = repo()
write(d, "LOG/index.md", "# LOG index\n\n- PENDING — original wording → a.md\n")
git(d, "add", "LOG")
git(d, "commit", "-q", "-m", "fixture")
# Reword after the commit, so git log -S finds no commit for the new text.
write(d, "LOG/index.md", "# LOG index\n\n- PENDING — reworded since → a.md\n")
report = hook.backfill_log_hashes(d)
after = read(d, "LOG/index.md")
check("the PENDING token is left in place", "- PENDING — reworded" in after,
      repr(after))
check("the report names the file and the token it found",
      "index.md (PENDING)" in report and "should have resolved" in report,
      repr(report))
shutil.rmtree(d, ignore_errors=True)

# --- 3. a body line mentioning [HASH] is untouched, and a real hash is not a
#        placeholder; a record's own "- x — y" bullet is not an index line ------
d = repo()
body = ("# abc1234 — A real record\n\nThe [HASH] token is what the close "
        "writes; this line discusses it.\n- `file.md` — a bullet in the "
        "record's own shape\n")
write(d, "LOG/2026-01-02-real.md", body)
git(d, "add", "LOG")
git(d, "commit", "-q", "-m", "fixture")
report = hook.backfill_log_hashes(d)
after = read(d, "LOG/2026-01-02-real.md")
check("the record is byte-for-byte unchanged", after == body, repr(after))
check("nothing is reported for it", report == "", repr(report))
shutil.rmtree(d, ignore_errors=True)

# --- 4. the misplaced-placeholder alarm reads the shape, not the word ---------
check("a **Commit:** field holding [COMMIT_HASH] is misplaced",
      hook._hash_is_misplaced("**Commit:** [COMMIT_HASH]"))
check("PENDING alone on a line is misplaced",
      hook._hash_is_misplaced("PENDING"))
check("a **Commit:** field holding a real hash is not",
      not hook._hash_is_misplaced("**Commit:** abc1234"))
check("prose discussing the token is not",
      not hook._hash_is_misplaced("The [HASH] token goes in the heading."))
check("a backticked token is prose",
      not hook._hash_is_misplaced("**Commit:** `[HASH]`"))

print()
if failures:
    print("%d failure(s):" % len(failures))
    for name in failures:
        print("  " + name)
    sys.exit(1)
print("all cases passed")
