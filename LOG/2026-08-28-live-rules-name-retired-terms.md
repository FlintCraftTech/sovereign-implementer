# 2e9cb18 — Retired-term findings settled: both are comments, kept as a comment-reword build

Read in context at processing: `pre_tool_use.py:866` is a docstring saying an option was "refused at the keep-step"; `session_start.py:54` is the format-epoch history comment whose entry 4 describes the build-block mechanism retired 2026-08-27 without a bump. No behaviour keys on either term, so the fix is comment rewording — the docstring to "the decision step", the epoch entry keeping its dated record while noting the retirement and dropping the checker's literal. Hook files touched, so the building close runs the suites (comments only; the trigger is mechanical).

Rule gate: not needed — hook comments, no method rule authored.
**Queue changes:** [live-rules-name-retired-terms] into Processed, cleared to run.
**Work processed:** kept — [live-rules-name-retired-terms].
