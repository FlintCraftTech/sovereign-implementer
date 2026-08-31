# skill-nonspecific-rules.md — contradictions and duplicates

Audit of `skill-nonspecific-rules.md` (1,037 lines), 2026-08-13. Line numbers refer to the file as supplied.

Findings are split into three groups: **contradictions** (two rules give opposing instructions for the same situation), **duplicates** (the same rule stated more than once, so it can drift), and **admission-test failures** (rules in this file that do not fire in all four skills, which the file's own opening test forbids).

---

## A. Contradictions

### A1. The retrieve source contradicts itself inside one section — *Prior decisions*, lines 1010–1036

Lines 1022–1029 state plainly: **"The source is the record, not LOG alone. Most decisions sit in QUEUE prose until a close, so a rule naming only LOG points at the wrong place for the common case."**

Seven lines later, line 1032 instructs: **"run the retrieve *before agreeing*: read LOG/index.md, open at most the one matched entry."** That is a rule naming only LOG — exactly the error the paragraph above it diagnoses. The cheapest-first ladder at 1014–1020 puts LOG *last*; this bullet makes it the only step.

This is the most consequential finding in the file, because the second bullet is the one that fires on the higher-stakes case (a user reversing a prior decision).

### A2. Retrieve order is stated three different ways

| Location | Instruction |
|---|---|
| 740–745 (*Throughline → Retrieve*) | Search `LOG/index.md` **first**, then the matched entry, then infer from code |
| 1014–1020 (*Prior decisions*) | This session → QUEUE rationale → SPEC → LOG index, "cheapest-first" |
| 1030–1036 | LOG index only |

A session following 740 and a session following 1014 open different files first.

### A3. The one-line post-write report may not re-paste text — except the inline offer says it may

- Line 133–135: **"The report after the write is one line** naming what landed and where — **never a re-paste of the text just written.**"
- Lines 194–196: the inline-text offer's effect is "paste doc-bound text inline for this session, **including the one-line report after a write**".

One forbids the re-paste; the other names the post-write report as the thing to paste. Neither cites the other.

### A4. "Pointing is the unconditional default" — with a stated override

Line 176–178: "Pointing is the unconditional default; **the one thing that overrides it is the user saying so**." A default with a named override is conditional. Wording only, but this sentence is load-bearing for the render rule and reads as absolute on a fast scan.

### A5. `[freeform]` sits above the line, but /next takes its work from above the line

- Line 573: "Processed, above the line — kept and ready. **/next picks work from here.**"
- Lines 499–503: `[freeform]` is work that must **not** be built by /next, and "sits **above** the cleared-to-run line."

The file acknowledges this ("the tag carries the exception"), but line 573 is written as an unqualified rule and the states table carries no pointer to the exception.

### A6. `[freeform]` uses the exact phrase another rule bans

- Line 434: `[freeform]` = "work done by hand **in a session of its own**".
- Lines 591–594: "Resolve any pull toward a new state, tag, shelving category, or **a 'focused session of its own'** by recommending skip-to-defer… This is a recurring failure."

`[freeform]` is a tag whose definition is the invented-category shape the later rule exists to suppress. Either the ban needs to carve `[freeform]` out by name, or the tag needs different wording.

### A7. Append-always vs. Claude-owns-sequencing

- Lines 537–539: "Placement: append to the bottom of Unprocessed, **always**. **No judgment call**, no narration line."
- Lines 935–937: "**Claude owns sequencing** — the order work sits in… Ordering is a judgment call you make and narrate, not a question you ask."
- Lines 950–953: "**Narrate the ordering work.** Any time you exercise ordering judgment… say why."

Lines 939–945 partially reconcile these ("most of the queue's order carries no weight"), but 537 says *no judgment* and 935/950 say *judgment, narrated*. A session reading only the Captures section and a session reading only Dependency ownership behave differently on the same file write.

### A8. "Run commands yourself" vs. the terminal-surfacing rule

- Line 26: "**Run commands yourself.** Don't ask the user to run things you can run."
- Lines 27–30 and 89–93: surface the terminal requirement; fence "commands the user runs in a separate terminal."

Reconcilable in principle (26 is scoped to what Claude *can* run), but 26 is stated bare, immediately before a rule that presumes user-run commands are routine. Worth an explicit scope clause on 26.

### A9. Red flags: "screen every session" vs. "the risks Claude happened to spot"

- Line 620: "**Screen every session** for anything that could expose the user's data."
- Lines 630–632: a standing section would claim the tool tracks every risk, "when all it holds is **the risks Claude happened to spot**."

One frames screening as a systematic duty performed every session; the other frames detection as incidental. The honesty argument in 630–632 is right, but it undercuts the obligation stated at 620.

### A10. The consolidated opening narration is a bundle not listed as an inversion

- Lines 43–48 and 261–263: one item per message, no previews, whenever the next action depends on the prior.
- Lines 49–53: consolidate several opening scans into **one** narration.
- Lines 74–81: the inversions block lists exactly two exceptions — alternatives, and a deterministic result set. The consolidated opening is not one of them.

If any consolidated scan produces something the user must act on, the two rules collide with no stated precedence.

### A11. Header scope vs. /setup

- Lines 13–17: a rule belongs here only if it fires in **all four** skills, including `/setup`.
- Line 19: "Active in every session where the plugin is installed **and the project is set up**."

`/setup` is the skill that performs setup, so by line 19 nothing in this file is active during it — which contradicts the admission test that includes it. Line 239 ("no SPEC.md → unadopted; offer /setup") confirms /setup runs pre-setup.

---

## B. Duplicates

### B1. "What would answer this?" — stated three times, twice near-verbatim

| Lines | Form |
|---|---|
| 31–36 | Communication bullet, with the wrongly-confident-session rationale |
| 307–313 | *Research and evidence filing*, same trigger, same rationale, reworded |
| 452–455 | `[user]` over-tag check — a distinct firing site, correctly cross-referenced at 329–330 |

31–36 and 307–313 are the same rule with the same justification written twice. One should be the canonical statement and the other a pointer.

### B2. One-item-per-message — stated twice in full

Lines 43–48 (Communication) and 261–263 (`[SEQUENCE]` tag) both carry: one item, no previews, write the full set to the working file first. The tag definition should be the canonical text.

### B3. The whole-file-read digest carve-out, twice, back to back

Lines 966–968 ("A digest generated from the whole file by code satisfies this more strongly than paging does…") and lines 970–975 ("**A mechanically generated digest covering the whole file satisfies this rule.**"). Same rule, consecutive paragraphs, second adds only the "not assembled by whoever is reading" guard. Merge into one.

### B4. Below-the-line meaning — three statements

- 573–582 (states table): "Processed, below the line — blocked by a named queue item, and by nothing else."
- 584–588: "Below-the-line is **not** a second shelf."
- 668–684 (its own H2 section): restates both, plus the world-waits routing already given at 486–491.

The dedicated section at 668–684 adds only "/plan's revisit is one question per item" (which is /plan-specific — see C).

### B5. Position never encodes a relationship — twice

Lines 612–616 ("a *blocking* relationship is carried by the `Blocked by:` field, not by position") and lines 946–949 ("**queue position never encodes a relationship**"). Same rule, two sections.

### B6. Slug placement — three times

Line 398 (line-format block), lines 406–407 ("the `[slug]` sits at the **end** of that same line"), line 437 ("the slug stays at its **end**"). Plus 946–949 for immutability.

### B7. Reference-by-slug-not-status vs. cross-references-only-as-slugs

Lines 562–564 and 948–949 overlap substantially; the first adds the status-staleness reason, the second adds grep-ability.

### B8. Provenance is asymmetric and default-AI — twice in full

Lines 408–423 (Captures) and lines 709–715 (Throughline). The second says it "applies here in full" and then restates it anyway, including "Never add an AI-authorship marker" against line 409's "never write an AI-authorship label."

### B9. "Risk-addressing, never risk management" — same coinage, two sections

Line 528 (scrub) and line 632 (red flags). Not wrong, but the phrase is doing definitional work in two places with no single home.

### B10. Filing vs. processing boundary — twice

Lines 554–556 ("Don't process work outside /plan") and lines 834–839 ("No planning work in any execution skill. The boundary is **filing vs processing**"). The second is the fuller statement.

### B11. Capture close-out by who raised it — twice

Lines 83–88 (Communication, the general rule) and lines 850–853 (mid-session discovery, restating "a discovery is Claude-raised, so don't close with 'anything else?'"). The second is an application, but it re-derives the rule rather than citing it.

### B12. "Don't presume the user has a terminal" — twice

Lines 27–30 and line 327 (Guards).

### B13. Fenced-block rendering for code/commands — twice

Lines 89–93 (verbatim-copy strings, paste targets only) and lines 138–139 (exception: "content whose exact characters are the substance (code, shell commands) keeps a fence").

### B14. Red-flag marker line format — twice

Line 400 (inside the capture line-format block) and line 625 ("one line under the item's description").

### B15. Not-ready work goes to the bottom of Unprocessed — three times

Lines 537–539, lines 584–588, lines 590–591.

---

## C. Rules in this file that fail its own admission test

The file's opening (13–17) states the admission control: **a rule belongs here only if it fires in all four of /setup, /plan, /next, /done.** These do not:

| Lines | Rule | Fires in |
|---|---|---|
| 510–511 | Scrub at "the three authoring moments — filing a capture, **keeping a work item**, **writing a LOG entry**" | keeping is /plan; LOG writing is /done |
| 459–465 | Two-weight `[user]` check: "/plan keep-step → thorough; /next pre-hand-off → light" | /plan and /next only |
| 657–659 | "Processing (**plan.md's keep-step**) is the moment a flag is cleared" | /plan |
| 683–684 | "**/plan's revisit** is one question per item" | /plan |
| 785–787 | Index entry doubles as "a **readiness check at /plan**" | /plan |
| 834–839 | "**/done's wind-down re-scan** is filing, so it's allowed" | /done |
| 859–864 | "A new build or design directive arising during **a close** routes out" | /done |
| 49–53 | Consolidated opening naming "/plan's read-state, /next's pre-flight, /done's close-out" | not /setup |
| 265–268 | `[SEQUENCE]` carve-out scoped to "the **/plan captures loop**" | /plan |
| 106–111 | Worked case scoped to "converting a project's whole QUEUE.md **at setup or migration**" | /setup |

Each may still be correct; the point is that the file's stated filter would have excluded them, so either the filter is aspirational or these belong in the per-skill docs.

---

## D. Structural, not strictly contradictions

- **Line 903, "An empty Processed section is normal"** sits at the tail of the parallel-sessions/worktree discussion, which has nothing to do with it. It looks like it belongs with the work-item states block (566–616).
- **Lines 173–178, "Ignore stale fields from older setups silently"** sits inside *View-in-doc rendering* but governs CLAUDE.md setting fields generally (`Editor:`, `Working mode:`, `Completion mode:`), only one of which is a rendering concern.
- **The capture line-format block (397–401) is described as "this exact shape is what the hooks parse"** but omits `Blocked by: [slug]`, which line 674 says is "one line in the item's block, **lint-checked**." If the lint checks it, the canonical format block should show it.
- **Two competing claims of canonical authority on rendering.** Line 151 declares *View-in-doc rendering* "the canonical rule for how doc-bound text is rendered. Other docs point here." But lines 136–140 (blockquote-with-bold-lead-in) and 89–93 (fenced paste targets) also specify rendering, in a different section, without pointing there.

---

## Notes on method

Some items in section B are deliberate cross-references rather than accidents — B8 and B11 both flag their own restatement. They are listed anyway because a restatement drifts as readily as a duplicate: when the canonical text changes, nothing forces the restatement to follow. The distinction worth acting on is whether each is a *pointer* or a *copy*. Every one listed here is currently a copy.

Nothing in section A is a formatting quibble. A1, A3, A5 and A6 each admit a session behaving one way or the opposite depending on which section it read.
