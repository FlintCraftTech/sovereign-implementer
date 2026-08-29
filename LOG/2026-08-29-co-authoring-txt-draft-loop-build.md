# 819f7f1 — A draft the user edits is handed over as a file, not as chat text

Co-authoring kept being shaped as Claude work the user writes into, and the painstaking part is explaining a change to Claude when it is much easier to go in and edit the text yourself. That is the user's framing and it is the whole reason for the rule.

Her observation the same week overturned a tested record. `CLAUDE.md` stated, as tested, that the desktop side panel opens `.md` read-only and `.txt` "not at all", which is why the posting flow detoured through Notepad. She checked live: `.txt` is editable in the side panel and carries a save button, so she controls when her edits land. The finding was stale and the detour unnecessary — both Notepad references are evicted in the same move that adds the rule, including a second one in the rezip-entry paragraph that the item did not name.

The general form ships as a fourth subordinate requirement on the walkthrough block: the draft goes to a `.txt` whose location the step names, and Claude reads it back only when the user says to, asks whether there is more, and loops until they say they are finished.

An external dependency was recorded and deliberately not waited on. An open Claude Code request would make `.md` editable in the viewer, which would remove the reason for the format choice — but it has no ship date and the `.txt` route works now.

Tick: done, confirmed — the block carries the fourth requirement, and a grep of `CLAUDE.md` for "Notepad" and "not at all" returns nothing.

Depth: short.

Rule gate: run — admitted as an amendment. Parent named: the `[user]` walkthrough requirements block in the always-loaded rules, which already carries subordinate limbs. Evicted in the same move: `CLAUDE.md`'s Notepad sentence, both stale and superseded.

**Files touched:** `plugin/throughliner/docs/skill-nonspecific-rules.md`, `CLAUDE.md`, `README.md`.

**Routed to Captures:** none.
