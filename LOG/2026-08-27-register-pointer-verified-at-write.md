# beac9d2 — A register line claiming text is on file verbatim is written only after the target is confirmed to hold it

Two lines in `INBOX/sent.md` claimed post text sat "verbatim" in a record that held no quoted text. One repair had even pointed back at the register in a circle. The fault was findable only because a session happened to need the text — nothing would have surfaced it otherwise, and a pointer that resolves to nothing reads exactly like one that resolves.

Both instances were repaired in the session that found them, through the bot. This build fixes the rule so the fault cannot be written silently again.

**The design is one more site for a rule that already exists**, which is why it consumes no slot: the always-loaded write-verify-point rule — write, re-read to confirm the content is there, then point. Applied to the sent-register line, it means a verbatim pointer is written only after the place it names is confirmed by re-read to hold the quoted text, **in the same turn**, because that is the only moment the wording is guaranteed on hand.

**The second arm matters as much as the first.** Where the text is not stored anywhere, the line says so plainly instead of pointing. Without that, a rule requiring a resolving pointer would quietly pressure a session into inventing one.

**The rule was exercised twice in the same session that shipped it, and both times it changed what got written.** The register line for the how-to install post edit was written only after the edited post was read back live through the bot. The line for the plain-English consent tip points at that item's LOG entry rather than at the draft file, because the draft lived in a session scratchpad that clears itself — a pointer to it would have resolved that day and rotted by the next.

**Files:** `plugin/throughliner/docs/feedback-and-inbox.md`.

Rule gate: run — amendment to the register-line specification in feedback-and-inbox.md (the "written in the same turn" paragraph gains the resolve check); parent named, the write-verify-point rule cited rather than restated, nothing evicted.
