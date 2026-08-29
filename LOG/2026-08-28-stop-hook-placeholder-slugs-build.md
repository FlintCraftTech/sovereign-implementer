# 4efdcff — Stop hook ignores placeholder slugs, with the boundary derived from the specimen vocabulary

A `PLACEHOLDER_SLUG` pattern drops a claimed slug containing "slug" as a word before the check runs. The derivation is in the comment: it is the shipped docs' own specimen vocabulary — [slug-a], [some-slug], [work-slug], [old-slug] — while no real slug in this queue's history contains the word, because a real slug names its work. The residual stays stated: an item deliberately named `something-slug` slips the check, which is now also a reason never to name one that way. The suite gained both directions — a specimen does not block, a genuinely absent real slug still does.

Tick: done, confirmed — driven directly against the new code rather than by provoking the hook live; all 27 suites passed.
Files touched: plugin/throughliner/hooks/stop.py, resources/testing/test_stop_hook.py.
Rule gate: not needed — hook code, no method rule authored.
