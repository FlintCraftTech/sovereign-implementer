#!/usr/bin/env python3
"""Status-line probe: does the desktop app run a status-line command at all?

Claude Code feeds the live context percentage to exactly one surface — the
status-line command's stdin. Hooks receive no context data whatsoever
(resources/research/context-window-hook-access.md), so if a session is ever to
know how full its context is, this is the only door.

What is being tested is NOT whether the field exists — that is confirmed at the
Claude Code level. It is whether the *desktop app* runs a status-line command
at all. An earlier in-session attempt produced an empty marker file, which is
consistent with the app reading settings only at launch. That is why the test
needs a full application restart, and why the marker file lives in the repo
rather than in the session scratchpad: the scratchpad does not survive the
restart the test is about.

Reads the status-line JSON from stdin, appends a timestamped line to the marker
file, and prints a visible string so the status bar itself shows whether the
probe ran. Never raises: a status-line command that crashes would take the
status bar with it, and this is a probe, not something worth breaking the app
over.

Delete this script, its marker file, and the settings entry once
[statusline-restart-test] has reported — it is scaffolding for one observation.

Outcomes it distinguishes:
    real percentages   -> the mechanism works; a context reader is buildable,
                          with an offset for the known undercount
    null values        -> a payload-timing problem, not a dead mechanism
    file never written -> the desktop app does not run status-line commands;
                          the mechanism is dead in this environment
"""

import datetime
import json
import os
import sys

MARKER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "statusline-marker.log")


def main() -> int:
    used = "NO-PAYLOAD"
    raw_keys = ""
    try:
        payload = json.load(sys.stdin)
        if isinstance(payload, dict):
            raw_keys = ",".join(sorted(payload.keys()))
            window = payload.get("context_window")
            if isinstance(window, dict):
                # Recorded exactly as received, `null` included: a null is a
                # different finding from a missing key, and flattening the two
                # would lose the one distinction the test is for.
                used = repr(window.get("used_percentage"))
            else:
                used = "NO-CONTEXT-WINDOW-KEY"
    except Exception as exc:  # noqa: BLE001 - a probe must never break the bar
        used = f"ERROR:{type(exc).__name__}"

    try:
        stamp = datetime.datetime.now().isoformat(timespec="seconds")
        with open(MARKER, "a", encoding="utf-8") as f:
            f.write(f"{stamp}\tused_percentage={used}\ttop_level_keys={raw_keys}\n")
    except OSError:
        pass

    print(f"SL-TEST ctx={used}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
