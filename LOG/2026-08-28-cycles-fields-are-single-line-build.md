# 4efdcff — Cycles parser reads wrapped Cadence and Observable fields whole, removing the constraint instead of documenting it

`cycles_facts()` matched both fields with single-line regexes, so a naturally wrapped field was silently cut at the line break — and a truncated cadence still reads like a cadence, so nothing downstream could tell. The parser gained a continuation state ending a field at a blank line or the next field line (`CYCLE_FIELD_START_RE`). The kept disposition's reasoning held: a format note in every cycles doc would guard a limitation that can simply be deleted. The suite gained the live instance that found this — the first draft's wrapped definition now parses whole — plus a case proving prose after a blank line stays out of the field.

Tick: done, confirmed — the new cases pass; all 27 suites passed. `resources/testing/` was missing from the run's Files list at self-scoping and was added before editing; the item's own acceptance names the suite, so this completed the derivation rather than growing scope — one of the two instances behind [self-scoping-misses-observable-files].
Files touched: plugin/throughliner/hooks/session_start.py, resources/testing/test_session_start_cycles_facts.py.
Rule gate: not needed — hook code, no method rule authored.
