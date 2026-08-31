# Scope-lock audit — Sovereign Implementer

**Date:** 2026-08-04
**Scope of the audit:** the shipped plugin package only — everything under
`plugin/si-plugin/` (hooks, manifest, both docsets, skills, templates). Root
`CLAUDE.md`, `SPEC.md` and `README.md` are host-project governance that never
ships; they are referenced only where they *contradict* the shipped package
(§7.6).

**What "scope lock" is taken to mean here:** the property that the agent works
only inside boundaries the human defined, and makes no decision the human didn't
authorize. It is not one feature. It is produced by four layers that compose:
hook code that denies, procedure clauses that instruct, skill frontmatter that
gates entry, and template text that seeds the same rules into the user's own
project.

---

## Function tags used throughout

| Tag | Meaning |
|---|---|
| **BOUNDARY** | States what the agent may or may not touch, or where a mode's authority ends |
| **CHECKPOINT** | The agent must stop and get human input before proceeding |
| **ANTI-DRIFT** | Prevents the agent expanding scope or re-deriving state on its own initiative |
| **CAPTURE** | Records a decision or discovery — recorded decisions become enforceable boundaries |
| **SEQUENCING** | Constrains order, which implicitly limits what the agent can do at any moment |
| **PROHIBITION** | Explicit "do NOT do X" |
| **OWNERSHIP** | *(new category)* Names which party owns a specific decision |
| **ANTI-INVENTION** | *(new category)* Forbids deriving new states, tags or containers the method never authorized |

**Why two new categories.** *Ownership* was forced by clauses like
`docs-b/done-plan.md:66` — "Claude reorders and narrates; it does not ask. The
user owns keep/delete and scope, not order." That is neither a boundary nor a
checkpoint; it is an explicit allocation of decision rights, and it *removes* a
checkpoint as often as it creates one. *Anti-invention* was forced by
`docs-b/plugin-behaviour.md:463` — it guards the shape of the rule system itself
rather than the shape of the work, and the plugin treats it as a distinct
failure mode with its own named anti-patterns.

**Canonical vs restated.** Several rules have one canonical home and multiple
restatements. Restatements are marked and are **not** counted as separate
mechanisms in §8.

---

# Layer 1 — Mechanical enforcement (hooks)

The only unskippable tier. Everything in Layers 2–4 is instruction the model can
in principle fail to follow; this layer is code that returns a denial.

## 1.1 Hook wiring — `plugin/si-plugin/hooks/hooks.json`

| Lines | Quote | Function |
|---|---|---|
| 2 | "PreToolUse enforces the batch file-list boundary (SPEC editable only when a batch lists it), git safety, and a subagent cost ask-gate (the Task tool prompts for approval before a subagent runs — ask, never block)." | BOUNDARY |
| 4–13 | `"SessionStart": [ ... session_start.py ]` | SEQUENCING — state detection runs before any work |
| 14–23 | `"matcher": "Edit\|Write\|MultiEdit"` | BOUNDARY — every file mutation routed through the scope-lock |
| 24–32 | `"matcher": "Bash\|PowerShell"` | BOUNDARY — shell routed through git safety only (see gap §7.1) |
| 33–41 | `"matcher": "Task"` | CHECKPOINT — subagent spawn intercepted |
| 43–53 | PostToolUse on `Edit\|Write\|MultiEdit` | CAPTURE — queue lint, advisory |

**Portability:** *adaptable.* The wiring pattern (intercept mutations, intercept
shell, intercept subagents) is generic; the specific matchers are not.

## 1.2 The tri-state file-list lock — `plugin/si-plugin/hooks/pre_tool_use.py`

This is the single most load-bearing mechanism in the package.

| Lines | Quote | Function |
|---|---|---|
| 8–15 | "no Files: section = no enforcement; section present but empty = method docs only; entries listed = only those files. SPEC.md is not a method doc..." | BOUNDARY (spec) |
| 398–400 | "# Rule 1: _build.md's Files: section governs editability. Tri-state: # no section = skip enforcement, present but empty = method docs only, # entries listed = enforce the list." | BOUNDARY |
| 119–194 | `_parse_build_files` — returns `None` when no `Files:` line, else a list | BOUNDARY |
| 161–176 | `if stripped.lower().startswith("files:")` … inline comma split | ANTI-DRIFT — a malformed inline `Files:` yields a non-empty list, so it can never *silently disable* the lock |
| 284–292 | `_is_build_file` — exact normalised path match | BOUNDARY |
| 419–428 | "BLOCKED: this session's _build.md lists no editable files, so only QUEUE.md, LOG/, and _build.md can be edited. Audit and test sessions don't edit source files — route findings to Captures in QUEUE.md instead. If a file genuinely needs editing, halt and add it to _build.md's Files: section with the user's approval." | PROHIBITION + CAPTURE + CHECKPOINT |
| 430–443 | "BLOCKED: this file is not in the current build's file list. … If this file genuinely needs editing, halt the build and, with the user's approval, add it to _build.md's Files: section." | BOUNDARY + CHECKPOINT |
| 331–334 | "# Only enforce in adopted projects (SPEC.md exists)" | BOUNDARY (scoping) |

Note the denial messages do double duty: they block, *and* they teach the
recovery move (halt → ask → add to `Files:`). That pairing is the plugin's
stated theory of prohibition (see §2.9).

**Portability:** *adaptable.* Needs some declared file manifest for the active
unit of work; the manifest need not be `_build.md`.

## 1.3 The four deliberate exemptions — `pre_tool_use.py:202–281`, applied at `:407–417`

| Lines | Quote / mechanism | Function |
|---|---|---|
| 202–214 | `for doc in ("QUEUE.md", "_build.md", "_plan.md")` + `LOG/` | BOUNDARY — method docs always editable so capture never blocks |
| 217–233 | `if ".claude" not in parts: return False` / `return "memory" in parts[claude_idx + 1:]` | BOUNDARY — memory dir matched by path *shape*, not machine path |
| 236–248 | `resources/research` always permitted | CAPTURE — filing research never blocked |
| 251–281 | scratchpad allowed only when `"scratchpad"` and `"claude"` both appear **and** the path is outside the repo — "so an in-repo `scratchpad/` folder stays under the normal scope-lock" | BOUNDARY |
| 407–417 | exemptions evaluated in order, before the deny paths | SEQUENCING |

These are holes by design: each one is a place the plugin decided capture and
scratch work must never be blocked, because blocking them would push the agent
toward acting instead of recording.

**Portability:** *adaptable.*

## 1.4 Git safety — `pre_tool_use.py:38–58, 348–386`

| Lines | Quote | Function |
|---|---|---|
| 38 | `RESET_HARD = re.compile(r"\bgit\b.*\breset\b.*--hard\b")` | PROHIBITION |
| 46 | `PUSH_FORCE = re.compile(r"\bgit\s+push\b.*(?:--force(?!-with-lease)\b\|-f\b)")` | PROHIBITION (with `--force-with-lease` exempted by lookahead) |
| 49 | `BLANKET_ADD` — `-A`, `--all`, bare `.` | PROHIBITION |
| 51 | `COMMIT_ALL` — `-a`, `-am`, `--all` | PROHIBITION |
| 58, 103–116 | `SEGMENT_SPLIT` on `&&`, `\|\|`, `;`, `\|`, newline | ANTI-DRIFT — per-segment matching so tokens can't accidentally combine across a chain |
| 63–68 | "this check matches the command's text, not its intent… Assemble such strings at runtime instead of writing the pattern out literally." | PROHIBITION (meta) |
| 349–386 | four `_deny` blocks, each naming a safer substitute (`git stash`, `--force-with-lease`, `git add <path>`, explicit stage-then-commit) | PROHIBITION + named alternative |

**Portability:** *fully portable.* These four rules are standalone and depend on
nothing else in SI.

## 1.5 Subagent cost ask-gate — `pre_tool_use.py:16–23, 85–100, 310–326`

| Lines | Quote | Function |
|---|---|---|
| 16–23 | "returns permissionDecision \"ask\" — never \"deny\" — so the user is always prompted before a subagent runs, but keeps full choice." | CHECKPOINT |
| 310–318 | "# Checked before the cwd / SPEC.md gates below, because the cost protection is universal" | SEQUENCING — fires even in unadopted folders |
| 319–326 | "Claude wants to start a subagent. Subagents burn tokens fast… Approve if this genuinely needs wide, open-ended exploration; decline to have Claude do the work directly instead. Declining is a normal, safe choice." | CHECKPOINT |

The final sentence is doing real work: it legitimises the refusal, which is what
stops a checkpoint decaying into a rubber stamp.

**Portability:** *fully portable.*

## 1.6 Advisory queue lint — `plugin/si-plugin/hooks/post_tool_use.py`

Enums (the enforceable vocabulary):

| Lines | Constant | Function |
|---|---|---|
| 55 | `WORKLINE_HEADING = re.compile(r"^####\s+\S")` | BOUNDARY |
| 59 | `SLUG_AT_END` | CAPTURE — traceability to LOG |
| 64 | `RED_FLAG_MARKER` | BOUNDARY |
| 67 | `WORK_SECTIONS = ("Processed", "Unprocessed")` | BOUNDARY — the only two states |
| 69 | `VALID_FLAG_STATES = {"cleared", "uncleared"}` | BOUNDARY |
| 75/79 | `BLOCKED_BY` / `SLUG_REF` | SEQUENCING |

Checks at `:136–230`, including the ordering check at `:180–230` — "points at an
item sitting BELOW this one — the work depended on should come first. Reorder,
or the dependency reads backwards." **SEQUENCING**

Posture, `:36–42`: "Deny-list by design: only known violations are flagged… All
findings are advisory — fed back to Claude as context next to the tool result,
never blocking". **ANTI-DRIFT** — the lint constrains format, never judgment.

Explicit non-enforcement, `:27–35`: "Provenance is NOT linted… an unmarked item
is assumed to come from the AI, and an explicit 'captured by you' credit is
written only when the user personally raised, pushed through, or wrote the item."
**CAPTURE** — attribution is a convention, deliberately left to judgment.

**Portability:** *adaptable.* The advisory-not-blocking posture is portable as a
principle; the enums are SI's.

## 1.7 Session orientation and risk surfacing — `plugin/si-plugin/hooks/session_start.py`

| Lines | Quote | Function |
|---|---|---|
| 346–375 | `_uncleared_red_flags` — matches `^Red flag\s*·?\s*State:\s*uncleared\b` | CHECKPOINT (detection) |
| 552–559 | "UNCLEARED RED FLAG(S) — unaddressed security, privacy, or data-exposure risk(s) recorded in this project's queue. Tell the user about these first, in plain language, before other work:" | CHECKPOINT + SEQUENCING |
| 537–551 | "The injected context can be truncated… everything SHORT and load-bearing goes first… it is the line that can least afford to be cut." | SEQUENCING — truncation-survival ordering |
| 149–190 | `content_stamp(root)` — hash of installed plugin files | ANTI-DRIFT |
| 590–601 | "Installed host build stamp… stamps differ means it hasn't been reinstalled since the most recent host-side change, so host-side tests aren't live yet. This catches edits that bump no version." | ANTI-DRIFT |
| 576–581 | "Use it to judge whether a host-side deferred test has gone live, instead of asking the user what's installed." | ANTI-DRIFT (removes an unreliable human question) |
| 470–518 | nested-SI detection → "running /setup here would adopt this parent folder, not them. Tell the user this plainly so they can course-correct before anything is adopted." | CHECKPOINT |
| 483–485 | "Detection only; the choice stays the user's." | OWNERSHIP |
| 619–630 | "you must open your first reply by telling the user plainly… offer to bring the project up to date… State this as your own first message before doing anything else" | CHECKPOINT + SEQUENCING |
| 632–642 | "Add-only by design: the injected instruction tells Claude to *add* the missing setting, never to rewrite or clobber what the user wrote." | PROHIBITION |
| 658–673 | "Add only that section — change nothing else the user has written." | PROHIBITION |
| 700–708 | "A planning session (/plan) may run in a separate chat alongside this build — … don't refuse it or insist on resuming or closing the build first." | ANTI-DRIFT (against over-refusal) |
| 279–299 | "A is the fallback in every uncertain case… a wrong guess toward B strands the session… while a wrong guess toward A only costs verbosity." | ANTI-DRIFT (fail-safe routing) |
| 302–323 | "Don't mix them: read one doc from each procedure family, from docs-b only. This is internal routing — never narrate it to the user." | BOUNDARY + PROHIBITION |
| 411–427 | docset existence checked before routing | ANTI-DRIFT (no-strand guarantee) |
| 23–46 | `_HASH_POSITION` positional-only match; `git log -S` → "Oldest, never newest" | CAPTURE (integrity) |
| 259–276 | payload recorded only `if not os.path.exists(target)` — "a recording step must never be able to break the hook it observes." | CAPTURE |

**Portability:** the red-flag-first ordering and the build-stamp liveness check
are *portable ideas*; the implementations are *coupled*.

---

# Layer 2 — Procedural constraint (the docsets)

Both docsets are cited. Where a rule appears in both, the delta is **hardening**
— docset A carries why-clauses, dated failure stamps and explicit `Scope:`
sentences; docset B states the same rule compactly. No constraint exists in one
docset and not the other, with the single exception noted at §2.10.

## 2.1 Run bounds — the cleared-to-run marker

| Location | Quote | Function |
|---|---|---|
| `docs-b/next.md:19–20` | "/next builds only from Processed, and only from above the cleared-to-run marker." | BOUNDARY |
| `docs-b/next.md:23` | `run = Processed[ top .. --- Cleared to run above this line --- )` | BOUNDARY |
| `docs-b/next.md:30–31` | "**Never pick an item from past the marker.** This is a standing rule, not a branch condition — it holds at every step, on every path through /next." | PROHIBITION |
| `docs-b/next.md:34–35` | "The marker is the only thing that bounds a run." | BOUNDARY |
| `docs/next.md:7` *(restatement, hardened)* | "the boundary /plan maintains between work greenlit to build (above) and work still being settled (below)" | BOUNDARY |
| `docs/next.md:24` | "Don't pick an item past the marker." | PROHIBITION |
| `docs-b/next.md:55–61` | early exit `NOTHING_CLEARED` → "tell the user the next work isn't cleared to run yet, recommend /plan to vet it, and stop." | SEQUENCING + CHECKPOINT |

Marker *placement* is governed separately, in the close:

| Location | Quote | Function |
|---|---|---|
| `docs-b/done-plan.md:101–111` | "put the `--- Cleared to run above this line ---` marker just below the last item the user has agreed is ready to build" / "none greenlit -> at the TOP" | BOUNDARY |
| `docs-b/done-plan.md:119–131` | "A processed item must not be cleared if it depends… on another item that has been **built but whose verification is still pending**… a cleared item can be built unattended with no user in the loop" | BOUNDARY |
| `docs-b/done-plan.md:154–170` | "The marker is the single gate for walk-throughs as well as builds" / "**Anti-pattern: don't hold a `[user]` item below the marker merely because it's the user's to run.**" | ANTI-INVENTION |

**This is the core of scope lock as a *quantity*.** The marker is the one thing
that says how much autonomous work is authorized, and the human sets it.

**Portability:** *coupled.* Meaningless without a two-section ordered queue.

## 2.2 The one human checkpoint before an unattended run

| Location | Quote | Function |
|---|---|---|
| `docs-b/next.md:78–84` | "Put the run in front of the user and invite a last-glance change **in the same message**… What the pause is *for* is the one deliberate human checkpoint before /next runs unattended-in-practice: a last chance to change scope or reorder." | CHECKPOINT |
| `docs-b/next.md:98–99` | "**\"Say the word to change scope or reorder — otherwise I'll start.\"**" | CHECKPOINT |
| `docs/next.md:29` *(canonical, hardened)* | same rule with the "unattended-in-practice" rationale spelled out | CHECKPOINT |
| `docs-b/next.md:221–223` | "Between build items, keep going autonomously — the user confirmed the whole run at the Step 1 off-ramp, so there's no per-item re-confirmation." | BOUNDARY (defines what the one approval covers) |

The pairing matters: the plugin buys autonomy *by* concentrating consent at one
legible moment, rather than diffusing it across many low-information prompts.

**Portability:** *portable* as a pattern — "one consent moment that names its own
scope, then run" — though the wording assumes a queue.

## 2.3 The halt rules — the only two clauses that stop a run outright

| Location | Quote | Function |
|---|---|---|
| `docs-b/next.md:130–134` | "you CAN'T tell which files THIS item's described work would change -> underspecification SURFACE IT. The only case that halts — building it means inventing scope the user never agreed to." | CHECKPOINT |
| `docs/next.md:41–43` *(hardened)* | "That's a real gap: surface it rather than guessing, because building it means inventing scope the user never agreed. This is the only case that halts." | CHECKPOINT |
| `docs-b/plugin-behaviour.md:573–575` | "**Backstop:** an uncleared flag in Processed should be impossible, so if /next meets one it stops and surfaces it rather than building." | CHECKPOINT |
| `docs-b/done.md:362–366` | "marker still reads State: uncleared? # should be impossible. STOP and surface it rather than committing — an uncleared flag at a ship close means the model was bypassed." | CHECKPOINT |

Everything else that "stops" is a checkpoint inside a step or a
capture-and-continue. Recognising that only two conditions halt a run is
important for anyone porting this: the design deliberately minimises hard halts
so the run stays unattended, and pushes everything else into capture.

**Portability:** *portable.* "Halt when acting would require inventing scope" is
a standalone rule.

## 2.4 Capture-instead-of-act — the pressure valve

This is the mechanism that makes the low halt-count safe. Every out-of-scope
impulse is converted into a queue line instead of an action or a blocking ask.

| Location | Quote | Function |
|---|---|---|
| `docs-b/next.md:135–144` | "you CAN scope it, but notice OTHER work worth doing beyond it -> adjacent-work discovery CAPTURE AND CONTINUE on the decided scope. Never a blocking scope-ask." / "A blocking ask on adjacent work both defeats the unattended run and reopens a scope decision reserved for /plan." | CAPTURE + ANTI-DRIFT |
| `docs-b/plugin-behaviour.md:830–838` | "**Mid-session discovery — decide by one rule: is it needed to complete the work being built?** … needed and minor -> ask to add it / needed and significant -> propose splitting / NOT needed -> capture and continue / premise is broken -> halt and course-correct" | CHECKPOINT + CAPTURE |
| `docs-b/plugin-behaviour.md:840–843` | "'Capture and continue' means: draft the wording, show it, file it to Unprocessed, then confirm-and-resume… Don't hold it in conversation to deal with later" | CAPTURE |
| `docs-b/next-build.md:113–126` | "**file it as a `[user]` line, never float it as a live question.** The failure to avoid is waving it off as 'separate work you'd handle yourself'" | CAPTURE + PROHIBITION |
| `docs-b/next-build.md:129–133` | "**Coherence exception** (narrow…). Evaluate against the coherence rules, not user convenience. **When uncertain, capture.**" | CAPTURE (bounded exception) |
| `docs-b/plugin-behaviour.md:779–781` | "/next **self-scopes**… Work outside the described work is appended to Unprocessed, not folded in." | CAPTURE |
| `docs-b/plugin-behaviour.md:857` | "**Nothing unrouted survives a session.** File or drop before close." | CAPTURE |
| `docs-b/plugin-behaviour.md:785–786` | "**Route to artifacts, not memory.**" | CAPTURE |

**Portability:** *adaptable.* Needs a backlog artifact, but the rule "convert the
impulse into a record rather than an action or an interruption" is the single
most transferable idea in the package.

## 2.5 Approval-before-write

| Location | Quote | Function |
|---|---|---|
| `docs-b/plan.md:21–26` | "**Never write to QUEUE.md without showing the exact text first.** … the message immediately before any QUEUE.md write must contain the text verbatim. Approval attaches to shown text, never to a described shape" | CHECKPOINT |
| `docs-b/plan.md:27–28` | "**A recommendation is not a decision. A draft is not a written line.** Both need the user's call." | CHECKPOINT |
| `docs-b/plugin-behaviour.md:80–85` | "**Approval-time outputs render as blockquotes with a bold lead-in**… End the message with an explicit ask naming the decision needed — a draft with no ask isn't actionable." | CHECKPOINT |
| `docs/plugin-behaviour.md:20` *(hardened)* | "silence after a draft fails this rule even when Claude has stopped and is waiting." | CHECKPOINT |
| `docs-b/plugin-behaviour.md:383–386` | "The human co-reads and approves this text: **unreadable is unapprovable.**" | CHECKPOINT |
| `docs-b/migrate-checklist.md:102` | "**Approval before write.** Draft, show, get the okay, then write." | CHECKPOINT |
| `docs-b/plan.md:309–314` | "keep -> CAN fold [approval into the action]… delete -> CANNOT fold. It's terminal, with no later approval step, so explicit approval is still required." | CHECKPOINT |
| `docs-b/next-audit.md:63–69` | "Ask the user to approve the whole set or list the numbers they don't accept as-is. Then wait." / "It keeps the always-show rule fully intact — the user reads every finding's exact wording before any of it is filed." | CHECKPOINT |
| `docs-b/done.md:418–424` | "one at a time, user approves each [PROMPT] -> never auto-delete" | CHECKPOINT + PROHIBITION |

The reversibility calculus at `plan.md:309–314` is worth noting: approval is
folded into the action where a later gate exists, and required explicitly where
the action is terminal. That is a principled rule for *when* a checkpoint earns
its cost.

**Portability:** *fully portable.* "Approval attaches to shown text, never to a
described shape" stands alone anywhere.

## 2.6 The filing/processing boundary

The plugin's load-bearing separation, and the reason `/plan` and `/next` exist as
different modes at all.

| Location | Quote | Function |
|---|---|---|
| `docs-b/plugin-behaviour.md:394–397` | "**Don't process work outside /plan.** Filing is open to every session; moving an item into Processed or deleting it is /plan's, because that decision is the user's." | BOUNDARY + OWNERSHIP |
| `docs-b/plugin-behaviour.md:824–829` | "**No planning work in any execution skill.** The boundary is **filing vs processing**… processing one — moving it into Processed, deciding its fate — is /plan's, because that's where decisions the user owns get made." | BOUNDARY |
| `docs/plugin-behaviour.md:314` *(hardened)* | "an execution skill that quietly processed one would settle an owner's decision off the user's radar — the exact thing unattended execution must never do." | BOUNDARY |
| `docs-b/plugin-behaviour.md:811` | "**/plan is for planning, /next is for building. Don't cross them.**" | BOUNDARY |
| `docs-b/plugin-behaviour.md:812–817` | "**Executable work lives in the queue as work items — never in a standalone plan doc.** /next runs the queue and only the queue; it never reads a side document to find steps." | BOUNDARY + PROHIBITION |
| `docs-b/plan.md:11–17` | "/plan is where unprocessed work becomes processed work through discussion. **No building happens here.**" / "**Never build during /plan.** Want to write code? Queue it." | BOUNDARY + PROHIBITION |
| `docs-b/done.md:376–381` | "/done -> may FILE the surfaced captures -> never ROUTES them (keep / delete) # filing is capture-making, allowed in any session; routing is planning, /plan's alone" | BOUNDARY |
| `docs-b/done-build.md:25–39` | "new scope… -> ROUTES OUT: a fresh /next, or a capture to Unprocessed if not urgent. Even if it looks small. Even if the user raises it here. /done records and commits; it doesn't take on new build scope." | BOUNDARY |
| `docs-b/next-audit.md:9–11` | "**The output contract defines an audit:** findings route to Unprocessed so /plan can process them into normal work items — **no direct edits to the artifacts the audit reads.**" | BOUNDARY |
| `docs-b/plan.md:538–542` | "/plan -> runs the FULL re-scan: files the captures AND can process them / /done -> runs a FILE-ONLY version" | BOUNDARY |

Note `done-build.md:25–39` overrides even a direct user request made at the wrong
moment — it routes the request out rather than acting on it. That is a rare and
deliberate case of the boundary outranking an in-the-moment instruction.

**Portability:** *coupled* as written, *portable* as a principle ("the mode that
executes may record but may not decide").

## 2.7 Ownership — who decides what

| Location | Quote | Function |
|---|---|---|
| `docs-b/plugin-behaviour.md:920–921` | "**The user owns whether an item is kept or deleted**, and whether a build expands its scope." | OWNERSHIP |
| `docs/plugin-behaviour.md:351` *(hardened)* | "Don't move an item into Processed, delete it, or grow a build past its scope without the user's say." | OWNERSHIP |
| `docs-b/plugin-behaviour.md:905–910` | "**Claude owns sequencing**… Ordering is a judgment call you make and narrate, not a question you ask." | OWNERSHIP |
| `docs-b/done-plan.md:66–68` | "**Claude reorders and narrates; it does not ask.** The user owns keep/delete and scope, not order." | OWNERSHIP |
| `docs/done-plan.md:24` *(hardened)* | "order is low-stakes and reversible, so the narration is the catch-point" | OWNERSHIP |
| `docs-b/plugin-behaviour.md:916–919` | "**Narrate the ordering work.**… Silent ownership reads as no ownership." | ANTI-DRIFT |
| `docs-b/plan.md:77–79` | "**Filing is any session; processing is /plan's.** Moving an item into Processed or deleting it is the user's decision to make." | OWNERSHIP |
| `docs-b/plan.md:163–165` | "ask whether to derive **coarse milestones** or **granular per-feature items** — the user's call" | OWNERSHIP |
| `docs-b/plugin-behaviour.md:552–553` | "**Flagging, not fixing.** Name and route the risk; don't quietly handle it or redesign around it, even when the fix seems obvious. The user decides." | OWNERSHIP + PROHIBITION |
| `docs-b/setup.md:132` | "Where their own content goes is the user's call, not yours." | OWNERSHIP |
| `docs-b/plan.md:303` | "Stop and wait. The user decides." | CHECKPOINT |

The ownership clauses cut both ways, and that is the point: by naming ordering as
Claude's, they *remove* asks that would otherwise dilute the asks that matter.

**Portability:** *fully portable.* An explicit decision-rights table is the most
directly liftable artifact here.

## 2.8 Sequencing and response shape

| Location | Quote | Function |
|---|---|---|
| `docs-b/plugin-behaviour.md:191–194` | "[PROMPT] stop and wait for the user's reply. Zero further actions — no tool calls, no starting the next step, nothing done 'while waiting'. Confidence about what they'll say is not a reason to skip the wait." | CHECKPOINT (canonical) |
| `docs-b/plugin-behaviour.md:195–196` | "[SEQUENCE] exactly one item per message, then wait. No previews. Write the full set to the working file before releasing the first item." | SEQUENCING |
| `docs-b/plugin-behaviour.md:199–201` | "`[SEQUENCE]` carve-out: showing the *one next item*… is presentation, not a preview. The forbidden case is teasing items they must hold in their head." | SEQUENCING |
| `docs-b/plugin-behaviour.md:186–188` | "[SILENT] zero text for this step — no narration, no progress note, no after-the-fact summary." | PROHIBITION |
| `docs-b/plugin-behaviour.md:38–43` | "**One item per message when the user's next action depends on the prior one.**… No previewing later items — a preview is a bundle… there's no exception for items that seem short." | SEQUENCING |
| `docs-b/plugin-behaviour.md:45–52` | "inversions — deliver together, not one at a time: … NOT an inversion: [user] walk-through items # driven live, always sequential" | SEQUENCING |
| `docs/plugin-behaviour.md:87–88` | "Step-level tags override phase-level tags. During skill execution, procedure tags govern." | BOUNDARY (precedence) |
| `docs-b/next.md:191–193` | "The ordering here is deliberately destination-first: items are written into _build.md *before* being removed, so the run survives an interruption between the two." | SEQUENCING |
| `docs-b/plugin-behaviour.md:130–136` | "**Write, then verify, then point — in that order.** … Never emit a pointer from the intent to write." | ANTI-DRIFT |
| `docs-b/next-build.md:264` | "**Do NOT delete _build.md yourself.** That's /done's job." | PROHIBITION + SEQUENCING |
| `docs-b/done-build.md:97–100` / `done-audit.md:67–70` | "Delete _build.md [SILENT]… **Only after everything above is complete.**" | SEQUENCING |
| `docs/done.md:192` | "The message file is writable at this step because the sub-doc deletes _build.md before reaching Commit… so the scope-lock isn't active on the project root here." | SEQUENCING |
| `docs-b/next.md:314–318` | "**At build completion the only valid next-step recommendation is /done** — never /next, never another build." | PROHIBITION |
| `docs-b/plugin-behaviour.md:858` | "**One build at a time.** Never start a second while _build.md exists." | PROHIBITION |
| `docs-b/setup.md:260–261` | "**Ask one question per message and stop after each.** Never bundle two questions into one message, even short ones." | SEQUENCING |
| `docs-b/next.md:226–239` | "Coming back from [a pause], ask **the one thing the pause was for**, and nothing else… The pull here is to bundle… Resist it." | SEQUENCING |

`docs/done.md:192` is the clearest evidence that sequencing here is not cosmetic:
step order is arranged *around* what the file-lock permits at each moment.

Root `SPEC.md:73` states the rationale for the whole tag system as a scope-lock
enabler: "Readable output is a control requirement, not a style preference. The
user keeps Claude aligned by reading and approving what it does, so output too
long to get through breaks that control."

**Portability:** *portable.* `[PROMPT]`/`[SEQUENCE]`/`[SILENT]` semantics lift
cleanly into any agent's response contract.

## 2.9 Prohibitions with named alternatives — the stated meta-rule

| Location | Quote | Function |
|---|---|---|
| `docs-b/plugin-behaviour.md:473–481` | "**The general form… wherever the method forbids something at a moment that creates real pressure, it names the legitimate alternative in the same breath.**" | ANTI-DRIFT (meta) |
| `docs-b/plan.md:140–145` | "A prohibition with no stated escape route reliably produces an invented one" | ANTI-DRIFT (meta, restatement) |
| `docs-b/plugin-behaviour.md:463–471` | "**Anti-invention guardrail.** Do not derive a fifth state, a new tag, or a new shelving category, however reasonable the felt need… Name that positive move whenever the pull appears; a prohibition on its own is what produces the invention." | ANTI-INVENTION |
| `docs-b/plugin-behaviour.md:450–454` | "**One shelf, one shelving move.** There is exactly ONE holding place for not-ready work — Unprocessed — and ONE shelving move… Below-the-line is **not** a second shelf." | ANTI-INVENTION |
| `docs-b/plugin-behaviour.md:456–461` | "**No dedicated-pass state.** There is no 'give this its own focused session' container — item size earns no new state. This is a **named anti-pattern**" | ANTI-INVENTION |
| `docs-b/plan.md:135–138` | "The bottom of Unprocessed is the **only** legitimate way to postpone something. Do not invent an alternative — a new state, a 'lift when you raise it' condition, a quiet shelf" | ANTI-INVENTION |
| `docs-b/plan.md:452–456` | "**The skipped record is the _plan.md slug and nothing else** — there is no durable queue marker, no 'parked' or 'dedicated-pass' tag written to QUEUE.md." | ANTI-INVENTION |
| `docs-b/plan.md:479–481` | "**There is no dedicated-pass state; the only defer is this skip.**" | ANTI-INVENTION |
| `docs-b/next-build.md:73–74` | "route it… — don't invent a deferral here." | ANTI-INVENTION |
| `docs-b/done.md:331–335` | "Nothing tracks it in a dedicated section, and **no LOG-only prose stands in for the queue line**" | ANTI-INVENTION |
| `docs-b/plugin-behaviour.md:677` | "**An item that can't state a lift-condition belongs in Unprocessed.**" | ANTI-INVENTION |
| `docs-b/done-plan.md:39–41` | "Do **not** reintroduce `Blocks:` / `Depends on:` headers or any dependency lint" | ANTI-INVENTION |

Docset A carries dated evidence for these — `docs/plugin-behaviour.md:192` "a
live /plan narrated the phantom container three times (2026-07-29)"; `:194` the
three dated fifth-shelf inventions. This is the plugin's own record that
scope-lock most often fails not by the agent doing a forbidden thing, but by the
agent *inventing a permitted-looking container* for it.

**Portability:** *fully portable*, and arguably the most valuable finding in this
audit for anyone building a different agent framework.

## 2.10 The `[user]` lifecycle — the most redundantly enforced prohibition

Six sites carry the no-completion-ask rule:

| Location | Quote |
|---|---|
| `docs-b/plugin-behaviour.md:635–639` *(canonical)* | "**A `[user]` line is walked through, and that is all.** There is **no completion ask anywhere in its lifecycle** — not at /next, not at /plan, not at /done, not leading, not trailing, not as a light aside." |
| `docs-b/next.md:70–74` | "**Never check whether a `[user]` item is already done.** Not up front, not in passing, not as a trailing note." |
| `docs-b/next.md:261–265` | "**No completion ask, anywhere in this branch — not leading, not trailing.**" |
| `docs-b/plan.md:99–103` | "**No completion sweep for `[user]` work.**… that ask is gone from the method entirely" |
| `docs-b/done.md:46` | "Detect a completed `[user]` item **from what the session can already see — never by asking.**" |
| `docs-b/done-plan.md:172–180` | "**never ask** whether any are done. There is no completion ask anywhere in a `[user]` item's life." |

And the clause that pre-empts its own repair — `docs-b/plugin-behaviour.md:656–660`:
"**The gap this leaves is deliberate: leave the item in place.**… This is written
down precisely so nobody later notices the hole and proposes an ask to fill it.
Don't." **ANTI-INVENTION**

Supporting rules — the matched pair at `docs-b/plugin-behaviour.md:359–375`:
"**Don't over-tag.** `[user]` is earned only by work Claude genuinely cannot
perform or witness… The test is 'can Claude do this at all?', not 'can Claude do
this right now?'" / "**Don't under-file.** Genuine user work MUST become a
`[user]` line — never a live chat question… The failure mode is **user-work
evaporation**." **CAPTURE + PROHIBITION**

And the live-drive rule, `docs-b/next.md:253–259`: "give the **first** concrete
step the item records, and **stop and wait**… Never say 'want me to walk you
through it?'" **SEQUENCING + PROHIBITION**

**Why this counts as scope lock:** a `[user]` item is work the agent is
*forbidden to do*. The tag is a boundary; the no-ask rule stops the agent
converting a boundary into a nag; the under-file rule stops the boundary
evaporating into an unrecorded chat aside.

**Portability:** *adaptable.* "Work the agent may not do becomes a tracked record
rather than a question" is portable; the specific lifecycle is not.

## 2.11 Red-flag gating — risk as a scope gate

| Location | Quote | Function |
|---|---|---|
| `docs-b/plugin-behaviour.md:526–528` | "Screen every session for anything that could expose the user's data… state the risk in plain English, surface it immediately" | CHECKPOINT |
| `docs-b/plugin-behaviour.md:539–542` | "**Never silently fix a security concern and ship past it**, and never build past one without surfacing it." | PROHIBITION |
| `docs-b/plugin-behaviour.md:566–571` | "An item reaches Processed only with its flag cleared… A flag that can't be cleared returns its item to the bottom of Unprocessed — never parked in Processed." | BOUNDARY |
| `docs-b/plan.md:80–83` | "**cleared** once the risk is designed out in-session, or the user is told it plainly and chooses to proceed" | CHECKPOINT |
| `docs-b/done.md:348–351` | "**Recording is unconditional once a flag clears** — the record never rides only in chat or on the marker" | CAPTURE |
| `docs-b/done-audit.md:58–61` | "**An audit doesn't clear red flags** — clearing happens at processing." | BOUNDARY |
| `docs-b/plugin-behaviour.md:590–597` | "When recording something in SPEC, QUEUE or a LOG entry, don't name third parties or their private circumstances." | PROHIBITION (write-time) |
| `docs-b/plugin-behaviour.md:626–628` | "**Deleting the text doesn't remove it from history.**… Never imply that an edit undoes the exposure." | PROHIBITION |

Risk here is a *readiness* condition: unresolved risk keeps work out of the
region `/next` may build from. Safety and scope lock are the same mechanism.

**Portability:** *adaptable.*

## 2.12 Anti-drift and verification

| Location | Quote | Function |
|---|---|---|
| `docs-b/done.md:17–19` | "**The _build.md read is unconditional.** When it exists, read it in full before the close-out runs, *regardless of how much of the session you remember*." | ANTI-DRIFT |
| `docs-b/done-build.md:56–58` / `done-audit.md:36–39` | "conversation memory -> a same-session BONUS pass, never a source this step depends on" | ANTI-DRIFT |
| `docs-b/done-plan.md:133–136` | "**Re-derive prerequisite state from LOG, not from memory.**" | ANTI-DRIFT |
| `docs-b/plan.md:261–262` | "re-read it from QUEUE.md to confirm the quote matches the file — this catches a context-drifted quote before it's discussed." | ANTI-DRIFT |
| `docs-b/plan.md:360–362` | "Report 'moved to Processed as [slug]' only after the Write succeeded and a re-read confirms it landed" | ANTI-DRIFT |
| `docs-b/plugin-behaviour.md:270–275` | "**'It ran' and 'it worked' are different claims — never accept one as evidence of the other.**" | ANTI-DRIFT |
| `docs-b/plugin-behaviour.md:946–956` | "Before raising a design question, run the why-pipeline retrieve… when the user proposes a change that would alter or reverse something the record already holds… run the retrieve *before agreeing*" | ANTI-DRIFT |
| `docs-b/plugin-behaviour.md:403–405` | "**Reference other queue items by slug, never by status.**" | ANTI-DRIFT |
| `docs-b/plugin-behaviour.md:911–915` | "**Stable slugs.** … Immutable… **queue position never encodes a relationship**" | ANTI-DRIFT |
| `docs-b/plugin-behaviour.md:496–519` | "Order alone does **not** express dependency… There are exactly three routes, and this is the whole set: Blocked by: [slug] / the push marker between items / a lift-condition in the item's prose" | BOUNDARY |
| `docs-b/next-build.md:188–196` | "the same error recurring / an empty diff… ~3 times -> STOP. Don't keep trying." then hand the user the decision | ANTI-DRIFT + CHECKPOINT |
| `docs-b/done.md:438–443` | "**Shipped-slug cross-check**… If a shipped slug is still sitting in Processed as active work, surface it… before committing." | ANTI-DRIFT |
| `docs-b/plan.md:122–133` | "asked about across MULTIPLE sessions and still not moving -> don't ask again. Propose returning it to the BOTTOM of Unprocessed" | ANTI-DRIFT + named alternative |
| `docs-b/plan.md:110–116` | "user-only -> DON'T ask per item. Gather every user-only condition into ONE consolidated question, asked once this session." | CHECKPOINT (anti-nag) |

The no-progress circuit breaker (`next-build.md:188–196`) is the specific guard
that makes unattended running safe — root `SPEC.md:61` names it as such: "a
no-progress stop… keeps a stuck item from thrashing unwatched."

**Portability:** *mostly portable.* The memory-is-never-a-source rule, the
ran-vs-worked distinction, the write-verify-point order and the repeat-failure
breaker all stand alone.

## 2.13 Mechanical operations preferred over agent retyping

| Location | Quote | Function |
|---|---|---|
| `docs-b/done-plan.md:70–73` | "**Use the mechanical mover — don't retype blocks.**… Only the *decision* — the desired order — passes through you; never the prose." | PROHIBITION |
| `docs/plan.md:91,99` | "run `python plugin/si-plugin/scripts/reorder_queue.py QUEUE.md Unprocessed --move <slug> BOTTOM`… hand-retyping it via Edit is pure corruption exposure" | PROHIBITION |
| `docs-b/done-plan.md:88–90` | "trust the self-check: exits non-zero -> NOTHING was written." | ANTI-DRIFT |
| `docs-b/migrate-checklist.md:89–92` | "**Method-shipped boilerplate is refreshed by re-copy, never regenerated from guesses.**" | PROHIBITION |
| `docs-b/migrate-checklist.md:111–113` | "each item's full rationale prose -> carried across verbatim… NEVER truncated" | ANTI-DRIFT |

A distinct and easily-missed form of scope lock: the agent is denied *authorship*
of content it is only meant to *move*. Every pass through the model is an
opportunity for unauthorized change.

**Portability:** *fully portable.*

## 2.14 Git and file safety in the docs (mirroring Layer 1)

`docs-b/plugin-behaviour.md:925–936`: "never git add -A / git add . -> stage
explicitly / never git push without asking -> and never --force / never git reset
--hard / always check for secrets before committing" **PROHIBITION**, and
"**Uncommitted changes you didn't make are the user's own work, not breakage.**…
Never report them as damage, and never try to undo or reset them." **PROHIBITION**

`docs-b/done.md:106–109` restates the same. `docs-b/done.md:466–489` adds the
test-build carve-out: "-> DON'T mention it. DON'T offer to stage it… Leave the
file dirty… the instruction is not 'don't ask', it is **leave it dirty and never
stage it**." **PROHIBITION**

`docs-b/done.md:516–523`: "**No pre-commit ask.** The commit always happens at
/done and its message was already approved… Only the push is optional… commit
first (the safe, local action), THEN gate the outward push on consent."
**CHECKPOINT** — consent is gated on the *outward* action, not the local one.

`docs-b/done.md:408–424`: "Offer to delete only files meeting **all** of these:
Claude created or wrote them THIS session… A file Claude did not create this
session is NEVER presumed rubbish" **BOUNDARY + PROHIBITION**

**Portability:** *fully portable.*

## 2.15 Consent for external and physical actions

| Location | Quote | Function |
|---|---|---|
| `docs-b/plugin-behaviour.md:939–943` | "Confirm before connecting to or acting on the user's physical device or external hardware… Ask, and wait for a yes." | CHECKPOINT |
| `docs-b/next-build.md:177–181` | "before using any connected device, ask permission — 'May I use your connected device to test this?' — then wait." | CHECKPOINT |
| `docs-b/plugin-behaviour.md:213–220` | "**Ask before spawning a subagent, and name the cost.**… get a yes first." | CHECKPOINT (doc mirror of the hook gate) |
| `docs-b/plugin-behaviour.md:237–239` | "name the candidate tool and what it does before using it (don't install blind); downloads, commands and device access stay under their existing confirm-first rules" | PROHIBITION |
| `docs-b/plugin-behaviour.md:896–898` | "**Claude drafts, the user sends.**… Never auto-submit" | PROHIBITION |

**Portability:** *fully portable.*

## 2.16 Operating-folder boundary

`docs-b/plugin-behaviour.md:165–177`: "Work on the project folder the session was
opened in and no other. Never scan parent or child folders to find a different
project, and never ask the user which project to work on." / "opened folder
contains nested SI projects -> say so plainly… Don't adopt the parent, don't scan
into a child." **BOUNDARY**

Paired with the hook-side detection at `session_start.py:470–518`.

**Portability:** *fully portable.*

---

# Layer 3 — Structural constraint (skill frontmatter)

The outermost lock, and the easiest to overlook: the model cannot enter any of
these modes on its own initiative.

| File | Line | Quote | Function |
|---|---|---|---|
| `skills/plan/SKILL.md` | 4–5 | `disable-model-invocation: true` / `user-invocable: true` | BOUNDARY |
| `skills/next/SKILL.md` | 4–5 | same | BOUNDARY |
| `skills/done/SKILL.md` | 4–5 | same | BOUNDARY |
| `skills/setup/SKILL.md` | 4–5 | same | BOUNDARY |
| `skills/next/SKILL.md` | 3 | "Pick the top queue entry and execute it — build or audit. One work item at a time, scope-locked." | BOUNDARY |
| `skills/plan/SKILL.md` | 3 | "All thinking work… No building happens here." | BOUNDARY |
| `skills/plan,next,done/SKILL.md` | 12 | "Plugin-wide behaviour rules at `${CLAUDE_PLUGIN_ROOT}/docs/plugin-behaviour.md` govern this skill at a level above the procedure below." | BOUNDARY (precedence) |

**`setup/SKILL.md` omits line 12.** See gap §7.4.

Every mode transition in this system requires a human typing a slash command.
Combined with §2.6, that means: the human chooses the mode, and the mode chooses
what decisions are available. Neither is the agent's to pick.

**Portability:** *fully portable*, given a host that supports invocation gating.

---

# Layer 4 — Seeded constraint (templates)

These write scope-lock rules into the consumer's own project, so the constraints
survive independent of the plugin's own docs — and give the user vocabulary to
hold the agent to them.

## 4.1 `plugin/si-plugin/templates/CLAUDE-TEMPLATE.md`

| Lines | Quote | Function |
|---|---|---|
| 3 / 58 | `<!-- ▼ PLUGIN-MANAGED — do not edit between these markers. ▼ -->` / `▲ … do not edit above this line. ▲` | BOUNDARY (inside the consumer's own config) |
| 60–64 | "## Project rules … This section is yours — the plugin won't touch it." | BOUNDARY (reciprocal — protects the human's space) |
| 24 | "**Only touch files listed in the active build scope. Halt and ask if you need more.**" | BOUNDARY + CHECKPOINT |
| 23 | "The safety check still blocks a build from editing SPEC unless that build lists it in its files, so a spec change never rides in silently." | BOUNDARY |
| 25 | "One build at a time. Never start a second build while _build.md exists" | PROHIBITION |
| 26 | "State problems plainly. Don't hide them or silently fix unrelated things." | PROHIBITION |
| 27 | "Route discoveries to QUEUE.md's Unprocessed section rather than acting on them immediately — a later /plan decides their fate." | CAPTURE |
| 10 | seeds the queue grammar the three hooks parse | BOUNDARY |

The two-sided marker at lines 3/58/60–64 is notable: the plugin declares a region
it owns *and* a region it will not touch. Scope lock runs in both directions.

## 4.2 `plugin/si-plugin/templates/faq-template.md` — user-facing articulation

| Line | Quote | Function |
|---|---|---|
| 224 | "Claude stops and asks. It stays within the work item's scope. If something else needs changing: 'I need to edit [file] because [reason]. Add to scope?'" | CHECKPOINT |
| 228 | "Before Claude connects to or tests on any device attached to your computer, it asks your permission first and waits" | CHECKPOINT |
| 237 | "a piece of work only becomes 'ready to build' once its flag is cleared… so a risk is never quietly shelved." | BOUNDARY |
| 249 | "before Claude starts one, the method stops and asks you first" | CHECKPOINT |
| 261 | "When /next runs several ready items in a row, it stops at this line… You don't manage the line; Claude does." | BOUNDARY |
| 279 | "Claude owns this ordering and does it on its own — it tells you what it moved and why, but doesn't ask permission." | OWNERSHIP |
| 297 | "it never deletes anything without your yes." | CHECKPOINT |
| `faq-index-template.md:48` | "What happens if Claude needs to touch something outside the current work item?" | — scope lock is a first-class user-facing concept |

**Why this is a mechanism and not documentation:** a constraint the user can
name is a constraint the user can notice being violated. The FAQ is the audit
surface for Layers 1–3.

**Portability:** *portable as a practice*, coupled in content.

---

# 5. Portability table

| Mechanism | Rating | Note |
|---|---|---|
| Git safety regexes (`pre_tool_use.py:38–58`) | **Portable** | Standalone; no SI concepts |
| Subagent cost ask-gate (`:310–326`) | **Portable** | Including the "declining is safe" framing |
| Approval attaches to shown text (`docs-b/plan.md:21–26`) | **Portable** | |
| Reversibility calculus for folding approval (`plan.md:309–314`) | **Portable** | |
| `[PROMPT]`/`[SEQUENCE]`/`[SILENT]` contract (`plugin-behaviour.md:186–201`) | **Portable** | |
| One-item-per-message + no previews (`:38–43`) | **Portable** | |
| Halt only when acting requires inventing scope (`next.md:130–134`) | **Portable** | |
| Anti-invention meta-rule (`:463–481`) | **Portable** | The most transferable finding here |
| Prohibition must name its alternative (`plan.md:140–145`) | **Portable** | |
| Explicit decision-rights split (`done-plan.md:66–68`) | **Portable** | |
| Memory is never a source; re-read the file (`done.md:17–19`) | **Portable** | |
| "It ran" ≠ "it worked" (`:270–275`) | **Portable** | |
| Write → verify → point (`:130–136`) | **Portable** | |
| Repeat-failure circuit breaker (`next-build.md:188–196`) | **Portable** | |
| Mechanical mover, not retyping (`done-plan.md:70–73`) | **Portable** | |
| Device/external-action consent (`:939–943`) | **Portable** | |
| Operating-folder boundary (`:165–177`) | **Portable** | |
| Uncommitted changes are the user's work (`:932–936`) | **Portable** | |
| Skill invocation gating (`SKILL.md:4–5`) | **Portable** | Needs host support |
| Declared file-list lock (`pre_tool_use.py:398–443`) | **Adaptable** | Needs any per-task file manifest |
| Exemption set (method docs, memory, research, scratchpad) | **Adaptable** | |
| Capture-instead-of-act (`next.md:135–144`) | **Adaptable** | Needs a backlog artifact |
| Advisory-not-blocking lint (`post_tool_use.py:36–42`) | **Adaptable** | |
| Seeded constraints in the consumer's config (`CLAUDE-TEMPLATE.md:24`) | **Adaptable** | |
| Build-stamp liveness (`session_start.py:590–601`) | **Adaptable** | |
| Cleared-to-run marker semantics (`next.md:20–35`) | **Coupled** | Requires the two-section ordered queue |
| Marker placement + unverified-dependency hold (`done-plan.md:101–131`) | **Coupled** | |
| Filing vs processing boundary (`:824–829`) | **Coupled** | Requires distinct modes |
| Red-flag lifecycle (`:526–575`) | **Coupled** | Requires the queue's state model |
| `[user]` lifecycle and no-completion-ask (`:635–660`) | **Coupled** | |
| Three-route dependency model (`:496–519`) | **Coupled** | |
| Docset routing (`session_start.py:279–323`) | **Coupled** | SI-specific |

---

# 6. What holds the property together

Four observations that only appear when the mechanisms are read as a set:

**6.1 Consent is concentrated, not diffused.** There is exactly one pre-run
approval (`next.md:78–104`) and it explicitly authorizes the whole run
(`:221–223`). The plugin then spends considerable effort *removing* asks — the
no-completion-ask rule, the consolidated below-line question, Claude-owns-
ordering — on the stated theory that too many low-value asks destroy the user's
ability to read and approve what matters (`SPEC.md:73`).

**6.2 Capture is the pressure valve that makes low halt-count safe.** Only two
conditions halt a run. Everything else routes to a queue line. Remove the capture
route and the halt-count would have to rise sharply.

**6.3 The plugin's own failure record says invention, not violation, is the
threat.** Docset A's dated stamps (`docs/plugin-behaviour.md:192,194`) record the
agent inventing containers — a "dedicated pass", a fifth state, a parked tag —
rather than doing forbidden things outright. Hence the anti-invention category
and the rule that every prohibition names its alternative.

**6.4 Only Layer 1 is unskippable.** Layers 2–4 are text. The hooks deny five
things: unlisted-file edits, four git patterns, and (softly) subagents. Everything
else in this audit is instruction.

---

# 7. Gaps — where scope can still leak

## 7.1 Shell writes bypass the file lock entirely
`hooks/pre_tool_use.py:391–396` — `if tool_name not in ("Edit", "Write",
"MultiEdit"): return 0`. The Bash/PowerShell path (`:348–386`) checks only git
patterns and never consults `build_files`. A `sed -i`, a redirect, `cp`, or
`Set-Content` reaches any file on disk during a locked build.
**Severity: high.** This is the largest hole in the only unskippable layer.
Mitigated in practice only by the user's global instruction never to write via
shell redirection — which is host-project guidance, not shipped enforcement.
*Filed 2026-08-04 as `[shell-writes-bypass-file-scope-lock]` in QUEUE.md's
Unprocessed section; see §8.1.*

## 7.2 The lock's authority file is inside its own blind spot
`pre_tool_use.py:206` lists `_build.md` as always editable. The file that defines
the scope is itself unscoped, so edit-`_build.md`-then-edit-the-file passes
mechanically. The only guard is prose in the denial strings ("with the user's
approval", `:426–427`, `:441–443`). Deliberate — the halt-and-add recovery
requires it — but it means Layer 1 cannot enforce Layer 1.

## 7.3 Fail-open on an absent `Files:` section
`pre_tool_use.py:404–405` — `if build_files is None: return 0`. A `_build.md`
written without a `Files:` line silently disables the lock for the whole session,
with no warning surfaced. The hardening at `:130–141` covers the *malformed*
section, not the *absent* one. A one-line advisory on this state would close it
without changing the fail-open behaviour.

## 7.4 `/setup` runs outside the behaviour rules
`skills/setup/SKILL.md` omits the precedence line that plan/next/done carry at
line 12, and `docs/setup.md:5` confirms it: "/setup runs before a project is
adopted, so the behaviour rules that define those tags aren't loaded yet."
`docs-b/setup.md:14–17` says the same. So the widest ungoverned window in the
method is the one skill that *adopts a folder and creates files*. `setup.md`
compensates with its own local rules (`:66–70` leave content untouched, `:151–152`
never overwrite, `:82–86` never blind-rename, `:299–312` use the user's words
verbatim) — but they are re-derived locally rather than inherited, so a future
behaviour-rule addition will not reach `/setup`.

## 7.5 No session-end or compaction guard
`hooks/hooks.json` registers `SessionStart`, `PreToolUse` and `PostToolUse` only.
There is no `Stop`, `UserPromptSubmit`, or `PreCompact` hook. "Nothing unrouted
survives a session" (`plugin-behaviour.md:857`) is therefore instruction with no
mechanical backstop, and context compaction mid-build can drop rules with nothing
detecting it. Notably, `done.md:17–19` already treats memory loss as the expected
case — the guard exists in prose but not in code.

## 7.6 Shipped docs diverge from root `SPEC.md`
Three places where the spec describes a different model than the package ships.
Flagged as observations; this audit changes nothing.

- **Completion mode.** `SPEC.md:41` says "The `Completion mode:` setting that
  governed the old question is retired." Both docsets still ship it —
  `docs/plugin-behaviour.md:42–49`, `docs-b/plugin-behaviour.md:138–145`,
  `docs-b/done.md`, `docs-b/done-plan.md`.
- **Push marker / `Blocked by:`.** `SPEC.md:45` specifies both; `docs-b/next.md:110–111`
  states "There is no blocker gate, push marker, or unpark/staleness scan — those
  belonged to the old model and are gone," while `docs-b/plan.md:373–375` and
  `done-plan.md:146–152` still place push markers. The marker constrains /plan's
  placement decisions but no longer bounds /next's run — a real asymmetry, not
  purely stale text.
- **Stale-item retirement.** `SPEC.md:49` describes a repeat-count mechanism; the
  docsets define the below-line revisit without one (`docs-b/plan.md:122–133`
  comes closest but keys on judgment, not a count).

## 7.7 Uncategorised residue
- The audit-contract halt (`docs-b/next-audit.md:21–33`) treats a *queue item
  itself* as potentially out of contract — the only place the agent is told to
  distrust an instruction the human authored. There is no equivalent check for a
  build item that names files inconsistent with its description.
- `docs-b/done.md:616–618` — "Do NOT skip the sub-doc's judgment steps even if the
  user says 'just commit.'" A prohibition that overrides an explicit in-the-moment
  user instruction. Correct here, but it is the one clause where scope lock
  constrains the human rather than the agent, and it is unpaired: nothing states
  the limit of that override.

---

# 8. Not yet implemented — scope-lock work sitting in QUEUE.md

Sections 1–4 inventory what the plugin *does*. This section inventories what it
has *decided or noticed but not built* — scope-lock mechanisms that exist today
only as queue items. Read alongside §7: the gaps there are holes nobody has
filed; the items here are holes already on the record, several with the design
work substantially done.

Position matters. An item in **Processed** has been discussed and agreed and is
waiting on ordering; an item in **Unprocessed** is a capture that has not yet
been weighed. Only the Processed items are decisions. Position is quoted for
each below.

## 8.1 The three holes in the mechanical layer — all now filed, none built

The file scope-lock engages only while `_build.md` exists
(`pre_tool_use.py:401`), and only for three tool names (`:391`). Three separate
queue items record the consequences, and they are the same hole seen from three
doors:

| Item | Section | The hole |
|---|---|---|
| `[shell-writes-bypass-file-scope-lock]` | Unprocessed | The lock is **on** but one tool class walks around it |
| `[plan-scope-lock-gap-and-emergency-path]` | Unprocessed | The lock is **off** during /plan |
| `[post-close-tail-state]` | Unprocessed | The lock is **off** after /done deletes `_build.md` |

`[plan-scope-lock-gap-and-emergency-path]` is the most developed and the most
consequential. Quoting it directly:

> "`pre_tool_use.py` sets `has_active_build = os.path.isfile(_build.md)`, so file
> containment engages only while a build is running. A planning session has no
> `_build.md`, so **any file in the repo is editable** — shipped hooks, procedure
> docs, templates, anything — with nothing noticing."

It also records that this audit's Layer-1 description is what SPEC already
overstates: "SPEC describes `pre_tool_use` as enforcing 'the scope-lock (which
governs SPEC.md like any other file)' with no hint that it is build-only. A
reader would reasonably conclude planning sessions are contained. They are not."

**The unbuilt mechanism it proposes is a paired one, and the pairing is the
interesting part.** A /plan whitelist ("a **whitelist, not a prohibition** —
/plan legitimately writes QUEUE.md, `_plan.md`, SPEC.md… and LOG at close") plus
an **emergency path** for acting on an actively-spreading risk, because "A
scope-lock in /plan would have *blocked* this session's scrub, so building it
without an emergency path makes the method worse at exactly the moment it
matters most."

The emergency path is specified as three parts — "a **narrow trigger** (what
qualifies), a **mandatory record** (what was changed and why, in the LOG), and a
**bound** so it never becomes a general licence to build during planning" —
with a distinction the method currently has no word for: "a risk **sitting
still** in the queue can wait for /next; a risk **actively spreading** —
published, installed, being served — cannot."

**Category:** boundary + a *sanctioned-override* pattern that does not yet exist
anywhere in the package. **Portability:** the trigger/record/bound triple is
fully portable and is the single most useful unbuilt idea in the queue.

`[post-close-tail-state]` covers the third door and reaches a different
conclusion — that it may be an advisory rather than a fix: "whether
scope-lock-off is a bug to fix (re-enable some lighter post-close protection) or
just to advise plainly."

## 8.2 The delivery gap — behaviour rules that no session actually receives

**Processed, top of the cleared region.**
`[session-start-payload-oversized-and-misordered]` is the most serious item on
this list, because it means much of Layer 2 is currently not reaching sessions
at all:

> "The payload delivered to this session was **54,886 bytes**. The harness
> truncated it to a ~2KB preview and persisted the remainder to a file… So the
> behaviour rules did not govern that session at all — only the docset directive
> and the state lines survived… **Every session in this project is currently
> running without its behaviour rules.**"

Every scope-lock clause inventoried in §2 from `plugin-behaviour.md` is, on the
current host, undelivered. The mechanism exists in the file and does not reach
the model. The fix is specified in three parts, of which part 3 is itself a
scope-lock mechanism: "**Carry detection with it.** A redirect that is skimmed
leaves a session governed by rules it never read, with nothing noticing."

Its sibling `[docset-routing-mechanism]` (**Processed**) builds that detection
for the docset directive — "Make the docset redirect self-verifying using the
docset stamp the docs already carry."

**Category:** a new one — *delivery verification*. Nothing in the shipped package
currently checks that a rule the agent is supposed to be governed by actually
arrived. **Portability:** fully portable, and a general lesson for any prompt-
delivered rule system.

`[faq-index-injected-as-session-start-bulk]` (**Unprocessed**) is the same
payload contended for by ~1.5KB of FAQ index sitting *ahead* of the rules block.

## 8.3 Unsanctioned-judgment items — the recurring shape

Three captures, all **Unprocessed**, record the same failure: Claude made a call
that was probably right and that no rule permitted.

- `[skill-docset-override-unsanctioned]` — "The skill stated a path; Claude read
  a different one… no rule permits it, nothing recorded it, and a session that
  made the opposite call would look equally reasonable." Open question: "follow
  the host, follow the project, or halt and ask."
- `[plan-skill-did-not-engage]` — "/plan ran this session by reading the
  procedure doc directly — the skill wrapper never engaged… the method's
  guarantees assume the skill engaged. Nothing detected that it hadn't."
- `[drive-testing-signals-skill-routing]` — structured `[user]` work driven
  informally in a loose tail: "not 'planning during execution,' but 'executing
  structured work with no skill around it.'"

Together with the emergency path in §8.1, these are four instances of one
missing mechanism: **the method has no way to sanction, bound and record a
deliberate departure from its own rules.** Today a departure is either a silent
violation or doesn't happen. That is arguably the largest conceptual gap in the
scope-lock design.

*Filed 2026-08-04 as `[sanctioned-override-mechanism]` in Unprocessed, naming the
shared mechanism without superseding the four local fixes. It generalises the
trigger/record/bound triple from `[plan-scope-lock-gap-and-emergency-path]`, and
flags one thing this reading had missed: two of the four cases are not chosen
departures at all — nothing noticed the skill hadn't engaged, or that the host's
routing and the project's model target disagreed. A sanctioned path helps only
where the session knows it is departing, so detection is a separate half and the
two should be scoped apart rather than conflated.*

`[plan-skill-did-not-engage]` adds a second missing check — nothing verifies that
Layer 3's invocation gate actually engaged. A procedure followed without its
skill around it is indistinguishable from one followed properly.

## 8.4 Audit-discipline rules — constraining the audit branch

Three **Unprocessed** captures would add boundaries to `[audit]` execution, which
today has an output contract (§2.6) but few input constraints:

- `[audit-must-reconcile-with-prior-verification]` — "Before reporting that an
  already-shipped deliverable is broken, check the LOG for a prior verification
  of it; if one exists and the finding contradicts it, reconcile." Recorded with
  its rejected broad form, and the reasoning is worth keeping: "a step that
  near-always no-ops gets skipped and then means nothing."
- `[audit-check-elsewhere-before-reporting-missing]` — "before reporting that a
  rule is absent, search the docset for it, and report what was found — absent
  entirely, or present elsewhere but not signposted."
- `[audit-findings-consolidate-destination]` — a **destination** rule for
  findings, noting the scope-lock cost of consolidation: "the Files list spans
  everything, so the scope-lock loosens."

That third one is a genuine trade this audit should flag: consolidating findings
into one work item is cheaper but *widens* the file scope the resulting build
runs under. Efficiency and containment pull opposite ways.

**Category:** anti-drift, applied to the audit branch. **Portability:** the first
two are fully portable rules for any review agent.

## 8.5 Staleness and record-integrity items

- `[unprocessed-blocker-claims-go-stale]` (**Unprocessed**) — recorded
  boundaries decay: "A blocker stated as prose inside an Unprocessed capture is
  re-read by nothing. Those claims are written at filing time, when they're true,
  and then quietly rot." Fix scoped to the moment of processing, deliberately
  not a sweep. This matters for scope lock because §2.4's whole premise is that a
  recorded decision is an enforceable boundary — a rotted record is a boundary
  that has quietly moved.
- `[decided-no-has-no-home-rule]` (**Unprocessed**) — no rule says where a
  decided-*no* lives. The proposed test: "does this decision merely need to *sit
  in the record*, or does it need to *stop something recurring*?" Directly
  relevant to §2.9, since the anti-invention clauses are exactly decided-nos that
  needed an active home.
- `[log-scope-adjacent-work]` (**Processed**, below the line, ready) — an
  artifact test for what the LOG records, chosen over a judged boundary
  specifically because a judged one leaks: "A boundary that asks Claude to judge
  'was that personal enough to leave out?' will eventually get it wrong and
  commit something private. The artifact test never asks that question."
- `[setup-as-migration-home]` (**Processed**, below the line, ready) — a
  format-epoch halt at session start. This is a new *sequencing* mechanism: it
  would stop a session proceeding on a stale project format, where today
  "migration only happens if the user thinks to run /setup."

## 8.6 Items that would loosen or reshape existing scope lock

Not every queued item tightens things. Three would trade containment away, and
each names the trade:

- `[approval-flow-token-doubling-simplification]` (**Unprocessed**) — flipping to
  write-first-then-approve would invert §2.5's canonical rule: "write-first means
  the file briefly holds unapproved content, so it leans on revert-on-reject —
  which is why the method currently shows-first." Gated on an external harness
  issue.
- `[next-per-item-queue-removal]` (**Unprocessed**) — per-item queue removal
  would weaken the destination-first guarantee cited at §2.8: it "means QUEUE.md
  and _build.md both hold the run's items during the build (a duplication
  window)."
- `[concurrent-session-support]` (**Unprocessed**) — a live/canonical queue with
  merge-at-close, where "Claude resolves the merge **silently**, surfacing to the
  user **only** when a conflict genuinely can't be resolved safely." A silent
  automatic merge of the artifact that *defines* scope is a meaningful expansion
  of agent authority over the boundary itself, and the item does not currently
  frame it that way.

`[write-first-link-dont-paste]` (**Processed**) sits in the same family — it
changes where approval-time text appears, though not whether approval happens.

## 8.7 Summary of the unbuilt

**18 queue items** bear on scope lock. Six are in Processed (agreed, awaiting
ordering); twelve are in Unprocessed (not yet weighed). Of those:

- **3** close mechanical-layer holes (§8.1) — none built, all now filed
- **3** concern rule *delivery* rather than rule content (§8.2)
- **5** describe unsanctioned-judgment episodes, plus the item that now names the
  mechanism they share (§8.3)
- **3** would constrain the audit branch (§8.4)
- **4** concern record decay and format staleness (§8.5)
- **3** would loosen existing containment as a deliberate trade (§8.6)

*(Counts overlap: several items appear under two headings.)*

**The two most consequential unbuilt mechanisms**, on this audit's reading:

1. **Delivery verification** (§8.2) — a rule that doesn't arrive isn't a rule,
   and right now nothing checks. This is currently *live*, not hypothetical.
2. **A sanctioned-override path** (§8.1, §8.3) — trigger, mandatory record,
   bound. Four captures circle it from different angles; a fifth now names it as
   one mechanism, so the open question has moved from "is this a thing?" to
   "does it generalise, or is it two mechanisms wearing one shape?"

**One thing conspicuously absent from the queue.** No item proposes extending
mechanical enforcement beyond file-edits and git — no check that a *build* stayed
inside its described work rather than merely inside its `Files:` list, which
`plugin-behaviour.md:769–777` explicitly says the hook cannot do ("passing the
hook never by itself makes work in-scope"). The plugin knows its mechanical layer
approximates the real boundary, and nothing queued closes that distance.

---

# 9. Summary

## Count

**41 distinct mechanisms**, after collapsing restatements onto their canonical
homes. By layer:

| Layer | Mechanisms |
|---|---|
| 1 — Hooks (mechanical) | 7 |
| 2 — Procedure docs | 16 |
| 3 — Skill frontmatter | 2 |
| 4 — Templates | 3 |
| Cross-cutting families (§2.11–2.16) | 13 |

By function tag (mechanisms often carry two; counted at their primary):

| Tag | Count |
|---|---|
| BOUNDARY | 11 |
| CHECKPOINT | 8 |
| ANTI-DRIFT | 6 |
| PROHIBITION | 6 |
| CAPTURE | 4 |
| ANTI-INVENTION | 3 |
| SEQUENCING | 2 |
| OWNERSHIP | 1 |

Underlying these are roughly 250 individual clauses; the six-site
no-completion-ask rule is the most redundantly enforced single prohibition in the
package.

## Coupled vs portable

**19 portable** — they work as standalone rules in any agent framework. These are
the git safety set, the subagent gate, approval-before-write with its
reversibility calculus, the response-shape tag contract, the single halt
condition, the anti-invention and named-alternative meta-rules, the decision-rights
split, the four verification rules (memory-is-not-a-source, ran≠worked,
write-verify-point, repeat-failure breaker), mechanical-mover-not-retyping,
consent for external actions, the folder boundary, uncommitted-changes-are-the-
user's, and invocation gating.

**6 adaptable** — need a file manifest or a backlog artifact, but not SI's
specific shape: the file-list lock, its exemption set, capture-instead-of-act, the
advisory lint posture, seeded constraints in the consumer's config, and build-stamp
liveness.

**7 coupled** — meaningless outside SI's queue and mode structure: the
cleared-to-run marker and its placement rules, the filing/processing boundary, the
red-flag lifecycle, the `[user]` lifecycle, the three-route dependency model, and
docset routing.

The portable set is larger than expected, and it clusters around *how consent and
verification are handled* rather than *what the boundaries are*. That is the
liftable part.

## Gaps

Six, ranked:

1. **Shell writes bypass the file lock** (`pre_tool_use.py:391`) — the only hole
   in the unskippable layer.
2. **`/setup` runs outside the behaviour rules** — the widest ungoverned window,
   and it is the skill that adopts folders.
3. **`_build.md` is unscoped** — Layer 1 cannot enforce Layer 1.
4. **Fail-open on an absent `Files:` section**, silently.
5. **No session-end or compaction hook** — "nothing unrouted survives" has no
   mechanical backstop.
6. **SPEC/docset divergence** on completion mode, push markers, and stale-item
   retirement.

## How the layers compose

The human types a slash command (Layer 3), which selects a mode whose authority is
bounded (Layer 2, §2.6). The mode reads a queue whose ready region the human set
at the previous close (§2.1), presents that region for one explicit consent
(§2.2), then writes a file manifest that the hooks enforce (Layer 1, §1.2).
Inside the run, every impulse toward unauthorized work is converted into a record
rather than an action (§2.4), and only two conditions stop the run outright
(§2.3). The same rules are written into the user's own project so they survive and
can be checked (Layer 4).

The property holds because those four layers are redundant rather than sequential:
a failure at any one is usually caught by another. Its two structural weaknesses
are that only one layer is mechanical, and that the mechanical layer covers file
edits but not shell writes.
