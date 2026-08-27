# d31b553 — Register audit: two false pointers found and repaired, verify-at-write rule queued

The capture [sent-register-pointer-resolves-to-nothing] was processed by doing the checkable half in-session. Every "verbatim in X" pointer in `INBOX/sent.md` was tested against its record: eight of ten resolved to real quoted text; two pointed at `LOG/2026-08-26-beta-day-one-posts-2.md`, which holds none. Worse, the one prior repair was circular — the pin-edited record said the full text was "reproduced in the register line's pointer", which points back at the record.

Both repaired through the bot: the pin fetched live and written verbatim into the pin-edited record (old pin reconstructible from its two quoted deltas); the "living dangerously" post found in **announcements** — not "main", which the user corrected to be a Chagora testing channel, fixed in the register, the record and TOOLS.md — and written verbatim into the beta-day-one record. Register lines updated to say what happened.

The rule half became the build [register-pointer-verified-at-write]: the always-loaded write-verify-point rule applied to the register-line site — a verbatim pointer is confirmed to resolve by re-read in the same turn, and where no text is stored the line says so instead of pointing. Rule gate: run — amendment to feedback-and-inbox.md's register spec, parent cited, nothing evicted.

**Queue changes:** [sent-register-pointer-resolves-to-nothing] deleted into the repairs (done) and [register-pointer-verified-at-write] (cleared).
**Work processed:** kept — [register-pointer-verified-at-write]; deleted — the source capture.
