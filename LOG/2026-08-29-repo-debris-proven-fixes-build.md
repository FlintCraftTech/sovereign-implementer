# [HASH] — `resources/captures/` is gone, and the one file only it held is safe

The folder was created to hold a session transcript too large to embed in a queue entry, so it held *attachments to* captures rather than captures — which is what made the name misleading. Its contents moved into `resources/testing/` on 2026-08-02, where re-read-later evidence belongs under the rule that `resources/` holds two things only, and the 2026-08-09 emergency revert resurrected the whole folder as a duplicate.

Three of its four files were re-verified byte-identical to the copies already under `resources/testing/` by checksum before anything was deleted — the item's claim, checked rather than trusted. The fourth existed nowhere else in the repository and was moved with `git mv`, so its history follows it rather than being severed. `rule_signals.py`'s archival-path list drops the entry for the deleted folder, since its sibling entry already covers the surviving copies.

Tick: done, confirmed — the folder no longer exists, the moved file does, and the board runs with no reference to the deleted path.

Depth: short.

Rule gate: not needed — no method rule is authored. Deleting the folder makes the repository match the existing rule rather than changing it.

**Files touched:** `resources/captures/` (deleted), `resources/testing/532ea359-spec-write-slim.txt` (moved in), `resources/rule_signals.py`.

**Routed to Captures:** none. The 4.5MB icon at the root stays out of scope as the item recorded — deleting it reclaims nothing, since the blob stays in history and this project refuses history rewrites.
