# d31b553 — Epoch-gap capture refused by the rule gate and deleted

Filed earlier the same session from a consumer-project transcript review (a session that started on 1.20.0-test18 and had 1.21.0-test2 installed underneath it): a mid-session plugin update escapes the format-epoch check, which lives in session start. Processed against the gate, it failed both admission questions. No recorded failure — the observed instance behaved well: the session noticed the version change, said so, re-read the new rules in full, and closed cleanly; the harmful case (an update crossing a format change mid-session) has never occurred and is speculative. And the desirable behaviour already happens unprompted — the noticing and re-reading was nobody's written rule. Deleted on the user's approval. The re-file condition is stated here deliberately: a real epoch-crossing instance is the recorded failure that would pass admission.

Rule gate: run — refused; no rule authored, the capture deleted.

**Queue changes:** [midsession-update-skips-epoch-check] deleted.
**Work processed:** deleted — [midsession-update-skips-epoch-check].
