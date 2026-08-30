# [HASH] — A defeated position written in rule syntax is deleted from the INBOX doc

From the compliance audit of 2026-08-29, lens 4. Common reasoning for this run's five compliance fixes is in `2026-08-30-done-audit-records-a-repealed-approval-step-build.md`.

The sentence sat inside `feedback-and-inbox.md`'s return-path rule and told the reader that the rule supersedes an earlier refusal in the same document, which had held that writing a path into another project's repository risked committing it.

The delete-and-read test settles it: delete the sentence and what remains is a complete instruction — the return path is safe to write because the recipient's `INBOX/` is gitignored, which the send already confirms. So what was deleted was history, and history belongs in the record rather than in the rule.

Where it fired makes it worse than a stray sentence. The doc is fetched on demand — when a user reports a method problem, or when mail is waiting — so it was read by a session mid-task on something else entirely, and it was telling that session about a decision made in this document's own past.

It is the founding shape lens 4 exists for: no "because" appears in the operative half, the sentence carries a whole defeated position in rule syntax, and it survived earlier passes precisely because it does not read as a why-clause riding a rule.

**Two nearby sentences were checked and are NOT findings, and the build left both standing** — verified by grep after the edit. `done.md`'s "Two limits, and neither may be softened" is an honest-limit statement the method requires. And this doc's rejection of an automatic read-receipt states a live prohibition: delete it and a future session builds the receipt.

The superseded reasoning survives twice over — in git history, and in this entry.

**Observable met:** a grep for "supersedes an earlier refusal" over the shipped docs returns nothing; both excluded sentences confirmed present.

**Depth:** short.
**Files touched:** `plugin/throughliner/docs/feedback-and-inbox.md`.
**Routed to Captures:** none from this item.
