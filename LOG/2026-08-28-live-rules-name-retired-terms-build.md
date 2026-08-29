# 4efdcff — The two retired-term references reworded out of hook comments, and the checks run clean

Both sites were comments, as processing settled: `pre_tool_use.py`'s docstring "keep-step" (three occurrences, not the one the check named — the check reports one line per term) became "the decision step", and `session_start.py`'s epoch entry 4 kept its dated record while gaining the 2026-08-27 retirement and the deliberate no-bump reasoning, phrased so the literal marker string no longer appears. Comment-only, no behaviour change. While here, the checks' one finding — rule-bearing commits uncovered by a compliance audit — was filed as `[compliance-audit-lag]`, the slug open in neither section.

Tick: done, confirmed — `py resources/rule_signals.py .` reports no live references to retired terms; all 27 suites passed.
Files touched: plugin/throughliner/hooks/pre_tool_use.py, plugin/throughliner/hooks/session_start.py.
Rule gate: not needed — comment-only edits to hook code, no method rule authored.
