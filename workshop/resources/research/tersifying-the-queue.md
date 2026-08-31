# Tersifying QUEUE.md — what was actually done

**Provenance:** written by a Claude session in another chat that ran the two passes, at the user's request, and supplied here by her on 2026-08-18. Reproduced verbatim. It is a procedure to follow exactly, not a summary to paraphrase — §4's declines and §7's provenance failure are the parts that carry the most weight.

**Read this before running any tersify pass.** Its own conclusion (§8e) is that the queue is not verbose and a wording pass is not the lever for real reduction.

---

Two passes, 2026-08-18, on this project's own QUEUE.md. Pass 1: 28,603 → 26,228 words (8%), 67 items. Pass 2, on a later version of the file: 31,309 → 30,409 words (3%), 74 items, touching only material that had changed since pass 1.

Written from what happened, including one real error and one probable provenance failure that was not caught at the time.

## 1. The cut/keep rules applied

**Rule 1 — cut a sentence only if deleting it leaves the surrounding claim complete and correctly applicable.** This is the same delete-and-reread test the queue itself uses on rationale. Applied per sentence, not per paragraph.

**Rule 2 — a paragraph's bold lead-in is a signpost; the sentence after it is the content. Compress the sentence, keep the signpost.** Evidence: every `**What happened.**` / `**Why it matters.**` / `**To settle at processing.**` header survives both passes verbatim. These carry the item's structure for a reader who scans rather than reads.

**Rule 3 — cut hedges and softeners, keep qualifiers.** "which is worth noting" goes; "probably", "may", "unverified", "not decided" stay. A hedge is about the writer's confidence in saying it; a qualifier is about the claim's truth status, which a later session acts on.

**Rule 4 — cut a restatement, keep the first statement.** Where a point was made twice in one item with different wording — common in the long accumulated items — the later one usually restated the earlier. Cut the second occurrence, not the first, because the first sits where the argument needs it.

**Rule 5 — cut connective throat-clearing that reintroduces what the reader just read.** "As noted above", "so, to restate the position", "this brings us to".

**Rule 6 — keep every numeral, filename, slug, commit hash and date.** Never compressed, never rounded, never converted to "several".

**Rule 7 — where a sentence is doing two jobs, compress the framing and keep the operative half.** Example: "The likely fix, to settle at processing, and the obvious answer may be too broad." → kept; the "and the obvious answer may be too broad" clause is operative (it forecloses a route), the rest is framing.

**Rule 8 — if compressing would require deciding something, stop and keep the original.** Any sentence whose shortening depended on resolving an ambiguity got left alone. This is the rule that produced most of the declines in §4.

**Rule 9 — do not merge two items, do not reorder, do not delete an item, do not repair a stale cross-reference.** A tersify pass changes wording only. Several items cite retired paths (`plugin-behaviour.md`, `docs-b/`) or slugs that have shipped; all were left exactly as written, because fixing them is queue work with its own decisions.

## 2. Preserved unconditionally

- Every `#### ` heading, verbatim, including its `[slug]`, its `[user]` / `[audit]` / `[freeform]` tag, and its position in the file.
- Both section headers and the `--- Cleared to run above this line ---` marker.
- Every `Blocked by:` line.
- Every `Files:` / `Files (rough):` / `Files (to settle):` line.
- Every `Rule gate:` disposition line and every `Runs alone` line.
- Every fenced block's structure (contents lightly compressed once; see §8).
- Every direct quotation of the user, inside its quotation marks.
- Every attribution line — "Captured by you", "Filed by Claude", "mixed authorship: the observation is yours, the diagnosis is Claude's".
- Every date and every commit hash.
- The file header paragraph's definitions (what a work item is, what a slug is, what the marker means) — compressed in wording, but no definition dropped.

## 3. What was removed, by category

**a. Meta-commentary about the item's own filing.** Original: "Recorded rather than quietly amended, because a running counter is the intuitive fix and would otherwise be re-proposed by the next session to read this." — kept, because it instructs a future session. But its neighbours like "this is worth a queue line rather than a shrug, and the reason is as follows" were cut to "why it is worth a line".

**b. Doubled framing on a single point.** In `[processing-asserts-reversibility-without-checking]`, the original ran "Why the processing session could not have known, and why that is the point" then re-explained the same in the next sentence. One statement kept.

**c. Redundant restatement of a rule the item had already named.** In `[standing-audit-programme]`, the sequencing argument (dedupe before restyle) appeared in the strategy paragraph and again in the "what the strategy buys" paragraph. Second occurrence compressed to a clause.

**d. Softening phrases.** "which is arguably worth considering", "it may perhaps be the case that", "worth noting here that" — all removed wherever they prefixed a claim the item then made plainly anyway.

**e. Verbose connectives inside long dated amendments.** The `[law-prose-restyle]` chain of dated re-scopings carried a lot of "and the reason is / what that means is / so the position is now". Compressed to the positions themselves.

**f. In pass 2 only: one instance of near-verbatim repetition between two paragraphs of the same item.** `[law-prose-restyle]` stated the acceptance test's hole twice — once as "the caveat that closes the hole" and once as "the test has a hole this pass could walk through". Merged into one paragraph, keeping the stronger wording and both operative instructions (a rise is a fail; a fall is also a fail).

## 4. Declines — where cutting was refused, and why

These are the more important half of the record.

**Declined: shortening `[standing-audit-programme]` (1,222 → 1,207 words, effectively untouched).** It carries an argument with a load-bearing distinction — admission gates prevent bad rules, audits catch drift, and no gate can prevent drift because the cause arrives after admission. Every attempt to compress the middle collapsed that distinction. Kept nearly whole.

**Declined: cutting the "what this does NOT establish" paragraphs.** Several items end with an explicit negative — e.g. `[chip-replies-are-indistinguishable-from-user-authorship]`'s "What this does NOT establish. That the decisions were bad." These read as padding and are not: they stop a later session over-reading the finding. Kept in every case.

**Declined: cutting recorded refusals of alternatives.** `[invented-rationale-compounds-past-the-shipped-rule]` records a cap that "was refused" and why. Deleting it invites the next session to re-propose it. Kept in every item that had one.

**Declined: compressing measurement caveats.** `[ideation-loop-holds-the-write]`'s "Read that as direction, not proof" paragraph, and `[session-survey-coverage-gap]`'s "a floor, never a ceiling". These qualify figures that would otherwise be quoted forward as settled.

**Declined: acting on `[files-line-names-excluded-files]`.** That item prescribes moving `[law-prose-restyle]`'s exclusion sentence out of its Files line. In pass 2 the exclusion sentence was briefly split out and then put back on the same line, because making that change is the *build's* job, not a compression pass's. Recorded because the pull to "improve while you're in there" was real.

**Declined: fixing stale references.** `[post-close-tail-state]` names `plugin-behaviour.md`, which no longer exists — and says so itself. Left alone under rule 9.

**Declined: compressing anything inside a `Rule gate:` disposition.** Those lines are read by two corpus checks. Untouched.

## 5. How the work was done

**Pass 1 — whole file, rewritten in four sequential chunks, in file order.** Each item was read once (the whole file was read before any writing) and rewritten from that reading. **This is the weaker method and I would not repeat it**, for two reasons: the rewrite is from memory of the source rather than from the source in front of you, which is exactly the condition under which a paraphrase drifts; and it makes verification hard, because every item's text differs from the original whether or not it needed to.

**Pass 2 — item-level splice, and this is the method to follow.** Concretely:

1. Split both files on `^#### ` into blocks keyed by slug.
2. Diff by slug to get three sets: unchanged, changed, new.
3. Touch only changed and new. Unchanged blocks are carried through byte-identical — not re-read, not re-compressed.
4. Write each compressed replacement into its own file, one per slug.
5. Reassemble programmatically, preserving original order and trailing whitespace.
6. Assert order and slug list are identical to the source.

Reading order within a block: read the whole block, compress, then re-read the compressed version against the original before moving on. In pass 2 that comparison was done by eye, block by block. In pass 1 it was done only in aggregate at the end, which is how the duplication in §8 survived as long as it did.

## 6. Verification actually run

Both passes:
- `grep -c '^#### '` on both files — item count.
- Ordered list of slugs extracted from headings, diffed. Pass 2 asserted `order identical: True`.
- `sort | uniq -d` on the slug list to catch duplicated items.
- Counts of `^Blocked by:`, `Files`, and the cleared-to-run marker, compared before and after.
- `wc -w` before and after, reported to the user as the actual reduction.

Pass 2 additionally:
- Per-block word counts before/after, sorted by delta, so any block that *grew* would surface. None did.
- An assertion that every prepared replacement was consumed (`unused reps: set()`), catching a replacement written for a slug that no longer existed.

**What none of this checks: whether meaning survived.** Every mechanical check here is structural. The only test of meaning was reading. That is the honest limit of both passes.

## 7. The user's own words — and a probable failure

**The intent was: direct quotations never reworded, credits never reworded, recorded reasons never reworded.** Quotations inside quote marks were carried across character-for-character, including the user's own capitalisation ("has NEVER successfully happened").

**But I am not confident the framing around quotes survived pass 1, and there is evidence it did not.** The version of the file you uploaded for pass 2 carries phrases like *"Her reason, rendered in Claude's words rather than quoted"* and *"Your objection the second time, rendered in Claude's words rather than quoted"* — in `[discord-post-cycle-awareness]`, `[discord-post-session-start-strength]` and `[announcement-rationale-split-correction]`. My pass-1 output for those same items reads *"Her words:"* and *"Your words the second time:"*.

I cannot prove the direction of travel from what I have, but the likeliest reading is that pass 1 compressed an explicit not-a-quotation disclaimer into a bare "her words", **upgrading a paraphrase into a quotation claim** — which is precisely the provenance defect `[chip-replies-are-indistinguishable-from-user-authorship]` and `[invented-rationale-compounds-past-the-shipped-rule]` exist to catch. It was not caught by me; it appears to have been corrected by hand between passes.

**So the rule, stated properly and not as I actually followed it:** an attribution's *hedging* is part of the attribution. "Rendered in Claude's words rather than quoted", "in substance", "as reported", "paraphrased" are as untouchable as the quotation marks themselves. Compressing them is a meaning change of the worst available kind, because the result reads more authoritative than the original.

## 8. What went wrong

**a. Silent duplication — the real failure.** In pass 1 an append operation ran twice, duplicating 15 items at the end of the file. The output looked fine and read fine; every duplicated item was correct text. It was caught by `sort | uniq -d` on the heading slug list, not by reading. Without that check it would have shipped.

Lesson: **a duplicated block is invisible to reading and trivially visible to a slug-uniqueness check.** Run it every time.

**b. Miscounting the source, briefly.** A first attempt to compare heading counts read 67 for the source and 82 for the output and I initially suspected I had invented items. Resolved by recounting properly. Worth noting because the panic reaction — "did I fabricate content?" — is the right instinct and the wrong first hypothesis; check the count method before checking the content.

**c. The improve-while-you're-in-there pull.** Twice in pass 2 a compression edit began turning into a content fix (the Files-line exclusion; a stale path). Both were reverted. Nothing caught these except noticing; there is no mechanical guard, which is a real weakness in this procedure.

**d. Fenced blocks.** In pass 1 two two-column fenced blocks were kept structurally but their right-hand text was compressed. This was not flagged to the user at the time. Given `[two-column-fences-wrap-unreadably]` — filed after those passes — a fenced block's column widths affect whether it renders readably, so compressing inside one is not purely a wording change. **Treat fenced blocks as untouchable in future passes** unless the user says otherwise.

**e. Yield was low and was reported as low.** 8% then 3%. Both times the honest finding was that the file is not verbose — its length is accumulated decision history, and the lever for real reduction is a planning decision about what belongs in LOG rather than a wording pass. A tersify pass that reports a large cut on this corpus should be treated with suspicion.

---

## Verified against this project's live queue, 2026-08-18

§7's predicted failure was **found live**. `[discord-post-context-adjacency]` still carried *"Her words: one a day, don't drown out the server"* — no quotation marks, over a paraphrase, while its three sibling post items carried the hedged form. Repaired the same day. **So §7 is not a hypothetical: one instance survived both passes and the hand correction, and this document is what found it.**
