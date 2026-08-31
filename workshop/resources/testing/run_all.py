#!/usr/bin/env python3
"""Run every test suite in resources/testing/.

Host-only dev artifact — not shipped in the plugin package.

Run:  py resources/testing/run_all.py

Why this exists ([testing-suite-runner-discovers-all]): the release ritual named
three suites by hand. That list went stale the moment a fourth was written, and
nothing anywhere reported the omission — a suite left out of the list is
indistinguishable from a suite that passed. Discovery removes the list.

**What counts as a suite is a naming convention, not a list**: a `.py` file in
this folder named `test_*.py` or `*_check.py`. A new suite named that way is
picked up with no edit here, which is the whole point. Anything else in the
folder is a fixture, a transcript, or a probe — `statusline_probe.py` reads a
status line off stdin and would hang a runner that tried to execute it.

**Any `.py` file that matches neither is REPORTED as skipped rather than passed
over in silence.** A suite misnamed at birth would otherwise be invisible in
exactly the way the hand-written list was.

Suites are invoked as plain scripts through `py`, never through pytest — see
CLAUDE.md's scripting constraints: `python` on this machine resolves to an
application's bundled interpreter that has no pytest, and its error names that
application, which sends a session chasing the wrong cause.

Exits non-zero on the first failing suite, so the rituals that call it stop
rather than warn.
"""

import os
import subprocess
import sys

for _stream in (sys.stderr, sys.stdout):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError, OSError):
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
SELF = os.path.basename(os.path.abspath(__file__))


def is_suite(name):
    if not name.endswith(".py") or name == SELF:
        return False
    return name.startswith("test_") or name.endswith("_check.py")


def main():
    entries = sorted(
        n for n in os.listdir(HERE) if os.path.isfile(os.path.join(HERE, n))
    )
    suites = [n for n in entries if is_suite(n)]
    skipped = [
        n for n in entries
        if n.endswith(".py") and n != SELF and not is_suite(n)
    ]

    if not suites:
        print("run_all: no suites found in resources/testing/ — that is itself "
              "a finding, not a pass.")
        return 1

    print(f"run_all: {len(suites)} suite(s) discovered in resources/testing/")
    if skipped:
        print("run_all: not run (name matches neither test_*.py nor "
              "*_check.py): " + ", ".join(skipped))
    print()

    failed = []
    for name in suites:
        path = os.path.join(HERE, name)
        print(f"=== {name} ===")
        proc = subprocess.run(
            ["py", path],
            cwd=HERE,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        sys.stdout.write(proc.stdout)
        if proc.stderr.strip():
            sys.stdout.write(proc.stderr)
        if proc.returncode == 0:
            print(f"--- {name}: PASSED\n")
        else:
            print(f"--- {name}: FAILED (exit {proc.returncode})\n")
            failed.append(name)
            break

    print("=" * 60)
    if failed:
        print(f"run_all: STOPPED at {failed[0]} — it failed. "
              "Nothing after it was run.")
        return 1
    print(f"run_all: all {len(suites)} suite(s) passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
