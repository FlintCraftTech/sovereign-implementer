# d31b553 — Prune red flag cleared: author-scoped deletion, keep 15, halt on error

Processed into Processed, cleared to run, placed after the bot script build it extends. The uncleared red flag — unattended deletion in a public channel with `Manage Messages` — cleared as designed out: the prune deletes only bot-authored messages (author checked per message), excludes pinned messages as a second independent guard, keeps the newest 15 (the user's figure, given at processing), and stops with a report on any partial failure. Residue stated: `Manage Messages` stays granted, consented on the bot-setup item 2026-08-26.

The user's edit-the-posts-first concern was resolved by fact rather than design: nobody can edit anyone else's Discord message, so pre-post editing happens in the draft file — the Notepad flow, tested live this session (side panel opens `.md` read-only and `.txt` not at all; Notepad round-trip verified on a burner file). Refused: pruning by position or count without the author check.

**Queue changes:** [bot-prunes-test-rezips] rewritten whole and moved Unprocessed → Processed, cleared.
**Work processed:** kept — [bot-prunes-test-rezips].
