# Codex port post-mortem, with Rygel's OpenCode port as a comparison

Audited 2026-08-05 at Alex's request, against the current method on main (v1.17.0, post-merge two-section model). Sources: the Codex port folder's LOG and QUEUE (read-only archive at `..\Sovereign Implementer - Codex port\`), Rygel's [PR #1](https://github.com/FlintCraftTech/sovereign-implementer/pull/1) (branch `rygel:port/opencode-v2`, head `71eac4c`), and this repo's LOG entries from the shelving period (2026-07-28 to 2026-07-31).

## The Codex port's timeline, from its own LOG

- **2026-07-15** — bootstrap and founding contract (`codex-port-bootstrap.md`, `plan-2026-07-15-3.md`). The founding session defined "one method with separate Claude Code and Codex **products**": equivalence measured by platform-neutral *outcomes*, not copied files; every queue item classified shared-method / Codex-only / Claude-only; a `PLATFORM-CONTRACT.md` peer agreement between the two sides; release gated behind a supervised desktop E2E walkthrough.
- **2026-07-15 to 07-16** — platform fights: the marketplace-recognition failure (`plan-2026-07-16-3.md`), a disposable four-variant ingestion matrix to isolate the cause (`codex-bootstrap-installable-skill.md`), then the hook launcher and payload adapter failing live and being replaced with PowerShell enforcement (`codex-hook-launcher-live-failure.md`). These were eventually *won* — 19 checks passed.
- **2026-07-17 to 07-20** — the workflow family was built (next/done/setup/plan entries) and **the live behavior audit passed with zero findings** (`codex-behavior-audit.md`): a fresh installed Codex task ran two cleared build items in order, stopped at the readiness line, filed a discovery correctly. This is the port's high-water mark — the thing worked.
- **2026-07-21 to 07-26** — a stale-cache update defect consumed a session and produced a four-state SHA-256 "update-reinstall proof protocol" (`codex-update-reinstall-proof-protocol.md`). More lifecycle guidance, capture-routing, close-behavior work.
- **2026-07-27** — the burst: ~15 LOG entries in one day, nearly all meta-work — root-SPEC "purity" audits (`audit-spec-product-truth-purity.md` plus four root-SPEC remediation entries), vocabulary hardening (`codex-work-item-vocabulary.md`), single-shelf enforcement, capture-narration discipline, a full rebuild of Codex /plan (`codex-plan-processing-flow-redesign.md`). Zero product-facing movement.
- **2026-07-28** — the end: three consecutive reinstall loops failed to stop the Codex host narrating internals before reading the procedure docs (`[codex-plan-pretool-announcement-host-compliance]` in QUEUE.md — versions `…223932`, `…232018`, `…234104` all failed; two test tasks even opened the wrong folder). The response was to queue a "foundational Codex-only workflow redesign" (`[codex-user-stateless-workflow-realignment]`). Two final planning sessions reordered blockers ahead of the still-held E2E (`plan-2026-07-28.md`, `plan-2026-07-28-2.md`). Then nothing. Dormant since.

The single release gate, `[codex-desktop-e2e]`, was never reached. Every planning session that approached it filed new blockers ahead of it faster than old ones cleared.

## What went wrong — four findings

### 1. The promise inverted on day one

The pitch was "a method-only space, mirrored into Claude Code practically automatically." The founding contract (`plan-2026-07-15-3.md`) built the opposite: **two separate products** whose equivalence was *outcomes*, not files — meaning nothing could ever be mirrored automatically, because there was no shared artifact to mirror. Sync became a manual reconciliation IOU: the queue item `[audit-codex-session-findings-for-claude]` grew to ~500 words of accumulated debt, and its own text records that "the SI planning state has not remained frozen" — the Claude side kept evolving (the two-section redesign, the merge, /cruise's rise and retirement all happened *during* the port), so the port chased a moving target by hand. Main's closing verdict (`LOG/2026-07-28-plan-3.md` in this repo) names it exactly: two independently hand-maintained plugins forced Alex to keep them in sync **from memory — the exact memory-dependence SI exists to prevent.**

### 2. The method's overhead, doubled, ate the project

Every Codex queue item had to state its scope class, its adaptation, its proof obligation, and its contract references. The result is visible in the archived QUEUE.md: items of 300–500 words, walls of re-stated ceremony. That is the "slowly forgetting what it was making" Alex observed — the *product* (a working workflow for non-coders on Codex) is barely findable inside items that are mostly about the process of porting. The 07-27 burst is the same failure at session scale: a day of purity audits and vocabulary enforcement on a product no user had ever run.

### 3. Perfection-gated release with a blocker-generating loop

One supervised E2E gated everything — release, the shared-core audit, the reconciliation. Each /plan re-inspected the path to that gate and found new blockers (narration compliance, path-containment hardening, conversational-spine correctness), which were themselves processed with full ceremony. A gate that must be *perfect* before anyone uses the product, fed by a process that generates blockers on inspection, converges on never. Contrast main's own release rule, adopted a week later (2026-08-04): release fires *mechanically* on file changes, precisely because "is it good enough to publish?" has no answer on a never-finished project. The Codex port is the case study that motivated that rule.

### 4. The final blocker was genuinely platform-shaped — and was met with more prompt engineering

The 07-28 narration failure was not a docs problem: the Codex host composed its pre-tool progress messages *before* reading any doc the port could edit. Three reinstall loops varied the wording location and changed nothing. The port's own capture eventually says the right thing ("do not request another reinstall until a causal experiment materially differs") — but by then the pattern had burned the last of the momentum. The general lesson is the one already in plugin-behaviour.md: when the host seems to ignore you, check what the host actually *promises* before iterating on your side. The port's control surface for narration simply didn't exist on Codex the way hooks exist on Claude Code.

**What was NOT the failure:** the engineering. The hooks were made to work, 37+ fixture tests passed, and the live behavior audit passed clean on 2026-07-20. The port died with a working core, buried under process.

## Rygel's OpenCode port — what he did differently

PR #1 (opened 2026-07-02, still open, no description beyond one sentence, no review comments) is a **complete snapshot port in one artifact**: 2,815 added lines under `open-si/` — all four commands, all 14 procedure docs (at full docset-A fidelity: `plan.md` 51KB, `plugin-behaviour.md` 47KB), all three hooks rewritten as a JavaScript plugin, templates, README, INSTALL, LICENSE.

- **Snapshot, not sync.** He ported the ~late-June SI (old queue model: red-flags section with open/resolved/accepted states, Build/Test/Audit batch subheadings, freeform and test flavors, `.si-version`, LOG hash backfill) and never chased upstream. Consequently it is now stale against main on essentially every axis the redesign touched — which is the honest cost of the approach, paid visibly instead of continuously.
- **Real engineering, faithfully translated.** `pre-tool-use.js` reimplements scope-lock, git safety, and the subagent cost gate — including per-command-segment splitting of git-safety checks, a correctness detail main itself only fixed on 2026-07-01. This is not a skeleton.
- **Platform adaptation by subtraction.** He dropped the 4.8 model-target machinery entirely ("model-agnostic — steer with the general authoring heuristic"), mapped skills → OpenCode commands, hooks → `session.created` / `tool.before.*` / `tool.after.write`, and adapted the session loop to OpenCode's `/done` then `/undo` habit. He adapted where the platform differed and copied where it didn't — no outcome-equivalence contract, no scope-classification ceremony.
- **Zero process overhead.** No PLATFORM-CONTRACT, no reconciliation items, no E2E gate, no port queue. Whether it deeply *works* on OpenCode is unproven (no test evidence in the PR) — but it exists, is installable, and took its author from zero to complete inside the method's own July feature set.

Caveat: an external contributor's PR is unreviewed third-party content; nothing above vouches for its behavior, only for what the files contain.

## Lessons

1. **A port is a snapshot-and-re-derive operation, not a sibling product.** Rygel's model and main's own post-shelving conclusion (`2026-07-28-plan-3.md`: one canonical source, Codex downstream, a change-time port-ledger — decided but never executed before shelving) agree: the method evolves in one place; a port is periodically *re-derived* from it, whole. The Codex port's peer-product contract guaranteed hand-sync from memory.
2. **Port when the upstream is still, not while it churns.** The Codex port ran concurrently with the largest redesign in the method's history. Any future port should start from a released, stable main — staleness then becomes a versioned fact ("ported from v1.17.0") instead of a live debt.
3. **Ship a walking skeleton to a user before hardening anything.** The Codex port passed its live audit on 07-20 and then spent eight days polishing narration and SPEC purity without a single external user. Release-on-file-change (main's 2026-08-04 rule) is the antidote; it should govern a revived port from day one.
4. **Budget platform fights, and check the platform's contract before iterating.** Three of the port's defining sinks (marketplace recognition, stale caches, uncontrollable pre-tool narration) were host behaviors. The third was unwinnable by prompt iteration, and three reinstall loops were spent learning that. "What does the host actually promise?" is the first question, not the last.
5. **Port ceremony is drag, not safety.** Scope-classification labels, outcome-equivalence proofs, and per-item contract recitals made every item slower to write, read, and process — and the bloat itself became the drift Alex noticed. Rygel's ceremony-free port produced more usable artifact in less elapsed effort.

## Loose ends surfaced by this audit (filed as captures, 2026-08-05)

- **PR #1 has had no response since 2026-07-02.** It can't merge as-is (it snapshots a superseded model into this repo's tree), but an open PR from the project's tiny community deserves an explicit answer.
- **The Codex port's Claude-handoff items may hold undelivered findings.** At least one looks live: `[claude-retire-forward-recommendation-advisory]` argued the forward-recommendation advisory duplicates queue order and goes stale — main's docset B still ships that mechanism. The port's `[audit-codex-session-findings-for-claude]` names several more shared findings (empty-cleared-region resolution path, whole-queue reading contract) whose arrival on main was never verified.
