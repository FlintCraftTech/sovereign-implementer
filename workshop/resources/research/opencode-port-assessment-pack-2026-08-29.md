# The OpenCode port assessment pack — verbatim snapshot, and what generalises to the next port

Sent 2026-08-29 to the maker of throughliner-opencode (Egnatia-OC on GitHub) as a zip of five files; register line in `INBOX/sent.md`, session record `LOG/2026-08-29-opencode-port-assessment.md`. Kept for two reasons: it is the verbatim record of what the pack claimed (the register's claims-checking needs the exact text), and it is the first data point of an ongoing line of research — how to support someone into self-hosting Throughliner, in whatever capacity — tracked by the queue capture [self-hosting-onboarding-research].

**What generalises to the next port, read out of this instance:**
- The assessment lenses: vendor fidelity and currency; shim-vs-hook contract correctness (payload fields, deny semantics, tool-name mapping reachability); the port's own declared gaps re-examined; docs audience fit; method wiring (rules-file loading, FAQ, INBOX); test-coverage honesty; license; self-hosting readiness; a completeness sweep.
- The delivery form: findings as a canonical QUEUE.md of captures, not a review doc — so the port develops itself with the method from day one.
- The bootstrap layer: self-hosting is gated behind a hand-run checklist proving the pillars in dependency order (commands load → context injects → guard denies with visible reason → lint and stop fire → /setup completes), because a queue only helps once /plan works.
- The cycle: an [upstream-catch-up] definition per port, observable = pin vs latest release, with the port-facing changelog named as coming soon and a diff fallback.
- The seed: the shipped self-hosting block hand-delivered wherever the port's vendored setup predates it, adapted to the harness's rules-file conventions.
- Honest limits stated throughout: read-from-code not observed; findings are material, never instructions.

Everything below is the pack's text as sent, verbatim, one section per file.

---

## File 1 — README-INJECTION.md

# From the canonical Throughliner project — an assessment of your port, packaged to run on itself

Hello — this folder comes from the Throughliner project
(github.com/FlintcraftTech/throughliner), sent by Alex. We read your
OpenCode port end to end on 2026-08-29 and were genuinely impressed: the
pristine vendoring is verified (we hashed all 34 vendored files against our
commit `743aa63` — byte-identical), the shim is careful, and your ANALYSIS.md
is more honest about its own gaps than most projects manage.

Rather than sending you a review document, we packaged the findings **as a
Throughliner queue**, so your port can be developed using the method on itself
— which is how the canonical project is built, and the strongest test a port
can run. Everything here is material for your own planning sessions to keep,
reshape or delete; findings, not instructions.

## What's in the folder

- **`BOOTSTRAP.md`** — start here. Nothing has verified your port can run the
  method on itself yet, so this is a hand-run checklist proving each pillar
  (commands load, context injects, the scope-lock denies, the lint and stop
  hook fire, /setup completes) in dependency order, in sessions you drive
  yourself. It ends with the gate for switching to self-hosting.
- **`QUEUE.md`** — every finding as a capture in the method's own format. The
  ones marked bootstrap-critical are the checklist's failure targets; the rest
  are ordinary work. One carries a red flag (the fail-open scope-lock) — that
  marker means a risk to your users' data that your planning session should
  weigh first.
- **`CYCLES.md`** — one recurring-work definition, `[upstream-catch-up]`,
  by which your port keeps up with ours: check the latest upstream release,
  look for the **port-facing changelog** (an upstream feature coming soon —
  the generator is built and wired into our release process; releases will
  begin carrying it, and it marks the host-only changes you must NOT port),
  fall back to diffing the shipped package until it appears, then re-vendor
  and file the mapping work as captures.
- **`AGENTS-self-hosting-block.md`** — the rule-authoring machinery the
  canonical project runs on (the rule gate, dispositions, host-versus-target),
  adapted for your setup. Merge it into whichever rules file OpenCode actually
  loads in your repo — AGENTS.md beats CLAUDE.md, first match wins, so merge
  rather than splitting across both.

## How to inject (after BOOTSTRAP.md's gate passes)

1. Copy `QUEUE.md` and `CYCLES.md` to your repository root.
2. Merge the AGENTS block into your winning rules file.
3. Run `/setup` — it adopts existing documents; it will interview you for
   SPEC.md and leave the queue's captures intact.
4. Run `/plan` — your first planning session processes the captures, and from
   there the method drives the port's own development.

## Honest limits

- Everything we report was **read from your code, not observed running** — we
  don't run OpenCode. Your bootstrap run is the real test, which is why it
  comes first.
- The port-facing changelog is described as coming soon, not as published.
- Your vendor pin is four commits behind us; the capture
  `[vendor-pin-behind]` in QUEUE.md carries exactly what those commits add
  (including `docs/ports.md`, which names your port's flavour — **tracking** —
  and the self-hosting seed this folder hand-delivers in the meantime).

Questions, corrections, or anything we got wrong about your code: the Discord
server, or an issue on the canonical repo. Thanks for building this.

---

## File 2 — QUEUE.md

# QUEUE

Two sections. **Processed** — agreed work, ordered top-to-bottom; /next builds from above the `--- Cleared to run above this line ---` marker. **Unprocessed** — captured, not yet processed; the next /plan weighs each item. Every entry in either section is a `#### ` heading (its description) with a `[slug]` at the end of that line and its rationale beneath; an entry in Unprocessed is a **capture**, and it becomes a **work item** when /plan keeps it into Processed. A leading `[audit]` / `[user]` tag names how it's executed; no tag means a build. An item carrying a security or privacy risk gets a `Red flag · State: …` marker — the flag rides the work.

Every capture below was filed by the canonical Throughliner project (github.com/FlintcraftTech/throughliner) on 2026-08-29, from a read-only assessment of this port at its then-current main. They are findings for your own planning sessions to weigh — keep, reshape or delete each on its merits. Claims about behaviour are read from code, not observed in a running OpenCode; your own test run is the real check. Items marked **bootstrap-critical** are the ones BOOTSTRAP.md orders — work them by hand before self-hosting.

## Processed

--- Cleared to run above this line ---

## Unprocessed

#### Hooks silently vanish wherever `python3` doesn't resolve [interpreter-python3-only]
Bootstrap-critical. `opencode/plugin.ts` spawns `process.env.THROUGHLINER_PYTHON ?? "python3"`. On many Windows machines `python3` is absent (the launcher is `py`, and a bare `python` can resolve to an unrelated application's bundled interpreter), and by the shim's own fail-open design a spawn failure degrades to "no Throughliner" with nothing visible to the user. So on such a machine every guard, the session orientation and the queue lint are simply off, and the session looks normal. Candidates: probe for a working interpreter at plugin init (`python3`, `python`, `py -3`) and log loudly when none is found; document `THROUGHLINER_PYTHON` in the README's install steps as the fix, not a footnote. The upstream hooks themselves are standard-library Python and reconfigure their own stdout/stderr to UTF-8, so the interpreter is the only obstacle.

#### The scope-lock can be off with no signal, because every hook error fails open [scope-lock-fail-open]
Red flag · State: uncleared
Bootstrap-critical. Fail-open is a deliberate and defensible design ("any error degrades to no Throughliner, never to a broken session"), but it means the one guard protecting a user's files from out-of-scope writes can be disabled by a crash, a timeout, or a missing interpreter, and nothing tells anyone. Combined with [interpreter-python3-only], a whole install can run permanently unguarded while appearing to work. The risk is to your users' data, which is why this carries a red flag rather than being a tuning note. Fail-open may stay the right default — the candidate change is loudness, not direction: surface a visible once-per-session warning when a hook errors (a line in the injected system context would reach the model; a stderr line reaches the user), and make the bootstrap smoke test in BOOTSTRAP.md a documented install step so "the guard actually denies" is proven once per machine.

#### Verify what the model actually sees when a write is denied [deny-reason-visibility]
Bootstrap-critical. The upstream hooks' deny messages are load-bearing: they teach the session what to do instead (write the scope file, use the queue tool, name each staged path). ANALYSIS.md §3 says a thrown error's text is "returned to model as tool result"; the shim wraps the reason in a `ToolDenied` error. If the full reason text reaches the model as the tool result, the method's self-correction works and this item closes as verified. If OpenCode truncates or generalises it, sessions will meet refusals they can't interpret and flail. Test: in a throwaway adopted project, have the model attempt an out-of-scope write and read the transcript for the deny text. Read-from-code either way — only the live run settles it.

#### System-context injection rides an experimental hook with no canary [context-injection-canary]
Bootstrap-critical. Session orientation, the always-loaded-rules directive and the brevity guide all reach the model through `experimental.chat.system.transform`. README already names the risk: an OpenCode update can rename or drop it and the port breaks silently — and by fail-open design, "breaks" looks like a clean session with no method in it. Candidates: a canary the user can see (BOOTSTRAP.md's pillar 2 is the manual form — make it a habit after every OpenCode update); pin the tested OpenCode version in README and CI; where OpenCode's event surface allows, detect that the transform never fired this session and log loudly.

#### Two block-counters guard the stop hook, and the shim's cap can eat a legitimate second block [stop-block-double-counting]
The vendored `stop.py` already limits itself: it blocks once per claimed slug per session, via marker files, then stands down for that claim. The shim keeps its own per-session counter on top and stops re-prompting after 2. Two *different* unfiled claims in one session is a legitimate double block upstream, and the shim's cap would swallow the second. Also worth settling in the same pass: the `session.idle` race under one-shot `opencode run` that ANALYSIS.md already records (the process can exit before the re-prompt posts). Candidate: trust the hook's own per-claim limiting and raise or drop the shim cap, keeping only a runaway-loop backstop.

#### Rules-file first-match: a project with AGENTS.md silently loses the method's CLAUDE.md [rules-file-first-match]
Bootstrap-critical. OpenCode loads rule files by first match — `AGENTS.md` wins over `CLAUDE.md`, and only one is used. `/setup` scaffolds the method's always-loaded project layer into `CLAUDE.md`. In any project that already has an `AGENTS.md` (common in OpenCode-land — it's the native convention), the method's project rules silently never load, which downstream looks like the model ignoring the method. This bites your own repo first: injecting the self-hosting block into `AGENTS.md` while `/setup` later writes `CLAUDE.md` splits the always-loaded layer across a winner and a loser. Candidates: document one rule ("the method's block lives in whichever file wins in your project — merge, never split"); or have the port's install/setup guidance append the CLAUDE-TEMPLATE block into an existing AGENTS.md instead of creating CLAUDE.md beside it; or list both in `opencode.json`'s `instructions` array, which loads files unconditionally.

#### Re-vendor: the pin is four commits behind and misses the upstream port machinery [vendor-pin-behind]
The vendored tree is verified faithful — all 34 files byte-identical to upstream commit `743aa63` (v1.21.1); the pristine-vendor claim holds. But upstream moved 1,796 insertions across 24 shipped files in the four commits since, including six artifacts that don't exist in this vendor tree at all: `docs/ports.md` (which names the two port flavours — this port is the **tracking** flavour and gains a name to declare by), `scripts/port_changelog.py` (the generator for the port-facing changelog described in CYCLES.md here), `templates/self-hosting-claude-block.md` (the upstream original of the AGENTS block in this folder — once re-vendored, `/setup` can seed it natively), `retired-artifacts.md`, and two smaller templates. `pre_tool_use.py` grew ~197 lines and `session_start.py` ~233. One heads-up worth planning around: upstream has queued a rename of consumer projects' `resources/` folder into `workshop/resources/`, which will bump the format epoch when it ships — a migration your own users' documents will need. Re-vendoring at the next upstream release is the natural first turn of the `[upstream-catch-up]` cycle.

#### Enumerate OpenCode's write-capable tools and map every one, or the scope-lock has gaps [unmapped-write-tools]
The shim maps `write`→Write, `edit`→MultiEdit, `bash`→Bash, `task`→Task, `skill`→Skill, and passes everything else through untouched (harness test 18 asserts exactly that). That is correct for read tools and fatal for any unmapped tool that can modify files — if the OpenCode version in use (or any co-installed plugin) exposes a patch/apply-style tool or another shell, writes through it bypass the scope-lock entirely. Worth one sweep per supported OpenCode version: list every tool that can touch the filesystem or run commands, and either map it to the nearest Claude name or deny it during an active build.

#### Skills persist in the global config dir with no uninstall or version story [skills-global-no-uninstall]
Plugin init materialises the five SKILL.md files into `~/.config/opencode/skills/` (or the env-var override) with absolute `${CLAUDE_PLUGIN_ROOT}` paths baked in. Consequences worth deciding on rather than inheriting: removing the plugin leaves five orphaned skills pointing at a tree that may be gone; moving or re-cloning the repo leaves them pointing at the old path until the next init rewrites them; and two checkouts (say, testing a branch) fight over the same global files. Candidates: project-level skills where OpenCode supports them, a version/path stamp in the materialised file plus a staleness check at init, and a documented uninstall step.

#### The vendored docs speak Claude Code, and a translation note is the cheap fix [docs-speak-claude-code]
The procedure docs are vendored pristine — rightly, that's this port's whole model — but they name surfaces an OpenCode user doesn't have: the desktop app and its side-panel `.txt` editing, PowerShell and the Windows `py` launcher in the scripting guidance, the plugin cache, output styles. A user following a walkthrough that says "open the file in the side panel and press save" stalls. Forking the docs would break pristine vendoring; the cheap fix is one short standing translation note in the port's own rules file (AGENTS block territory): a table mapping the recurring terms — side panel → your editor; PowerShell/py → your shell/python3; rezip/restart → re-vendor + plugin reload; desktop app → OpenCode TUI. Small, additive, and it lives in the port's own layer where pristine vendoring permits it.

#### One live smoke against a real OpenCode, scripted from the bootstrap checklist [live-smoke-missing]
The mocked harness is thorough (18 tests over injection, scope-lock, git safety, idle validation, materialisation, fail-open) and honest that it asserts plumbing, not output quality, and never drives a real OpenCode process. The gap that bit ANALYSIS.md's own risk list is exactly the live half: experimental hook renames, `session.idle` timing, real permission flows. BOOTSTRAP.md in this folder is a hand-run live smoke in dependency order — once it has been run once, its steps are a script waiting to be automated as a CI job against a pinned OpenCode version.

#### Gitignore the shim's trace files in adopted projects [trace-files-gitignore]
The shim writes `.throughliner/.shim-<sessionID>.jsonl` trace lines into the project; a README comment says to gitignore `.throughliner/` manually. Upstream's `/setup` maintains consumer `.gitignore` entries for its own artifacts, but its vendored version predates any knowledge of the shim's traces. Until re-vendor plus an upstream-side entry, the port's install steps should add the `.throughliner/` line themselves — a trace of tool calls in a public repo is a mild information leak as well as clutter.

#### License posture is compliant; making it machine-readable is optional polish [license-sharealike-compliant]
A positive finding, filed so it isn't re-investigated: upstream Throughliner is CC BY-NC-SA 4.0, and this port carrying the same license is exactly what ShareAlike requires — nothing to fix. GitHub shows "Other (NOASSERTION)" only because the LICENSE file isn't in a format its detector recognises; if the badge matters, add the canonical license text or an SPDX identifier. PROVENANCE.md's retention statement already says the right thing.

---

## File 3 — BOOTSTRAP.md

# BOOTSTRAP — prove the port can run the method before pointing it at itself

The chicken-and-egg problem this file exists for: the queue in this folder only
helps once `/plan` works, and nothing has yet verified that your port can run
the method on itself. So self-hosting comes second. First, ordinary OpenCode
sessions you drive yourself — no method command running — work through this
checklist by hand. In the method's own vocabulary that hand-driven work is
"freeform"; you don't need the vocabulary to do it.

Every step below is: **test something → what a pass looks like → which capture
in QUEUE.md covers a failure.** The steps are in dependency order — a later
pillar is meaningless while an earlier one fails. All of them were read from
your code by the upstream project, not observed running; this checklist run is
the actual test.

Use a **throwaway folder** for the guard tests, never a real project. (That
rule is upstream's own scar tissue: testing a guard by performing the guarded
action for real once destroyed a committed record, because the installed guard
was the old code.)

## Pillar 1 — the five commands exist and load

Test: open an OpenCode session in any folder and type `/setup` (don't run it to
completion yet — just confirm it's offered), then check the other four appear
the same way.
Pass: all five commands are visible and invokable by you.
Fail → the skills never materialised: check `~/.config/opencode/skills/` for
the five folders, then [interpreter-python3-only] and
[skills-global-no-uninstall].

## Pillar 2 — session context actually reaches the model

Test: start a fresh session in a folder and ask the model what Throughliner
told it at session start.
Pass: it can name the orientation it received (project state, the direction to
read the always-loaded rules).
Fail → the experimental injection hook is broken or the Python hooks aren't
running: [context-injection-canary], then [interpreter-python3-only].
**Re-run this pillar after every OpenCode update** — it is the piece that can
break silently.

## Pillar 3 — the scope-lock actually denies, and the reason reaches the model

Test: in a throwaway folder that has been through `/setup`, ask the session to
write a file that no scope permits (any path outside the method documents, with
no build running and no scope file written).
Pass: the write is refused, AND the model can tell you *why* — the deny message
naming what to do instead.
Fail on the refusal → the guard is off: [scope-lock-fail-open],
[interpreter-python3-only]. Fail on the why → the reason is being swallowed:
[deny-reason-visibility].
Also worth one probe here: try the same out-of-scope change through any other
tool that can touch files ([unmapped-write-tools]).

## Pillar 4 — the advisory lint and the stop hook fire observably

Test A: have the session append a malformed entry (a heading with no `[slug]`)
to the throwaway project's QUEUE.md.
Pass: the tool result comes back annotated with the lint's advisory note.
Test B: have the session *claim* in its reply that it filed a capture it never
wrote.
Pass: the session gets pulled back once to actually write it, and is not
re-prompted endlessly.
Fail → [stop-block-double-counting] (and for A, [interpreter-python3-only]).

## Pillar 5 — /setup completes end to end

Test: run `/setup` to completion in the throwaway folder.
Pass: SPEC.md, QUEUE.md and the method's project rules file exist; a fresh
session then reports the project as adopted.
Check while you're here: which rules file actually loaded — OpenCode uses
AGENTS.md over CLAUDE.md, first match wins. If the folder ended up with both,
that's [rules-file-first-match] biting.

## The gate

**You are ready to self-host when every pillar passes.** Then, in this
repository:

1. Drop `QUEUE.md` and `CYCLES.md` from this folder into the repo root.
2. Merge `AGENTS-self-hosting-block.md`'s block into whichever rules file wins
   in this repo (see [rules-file-first-match] — merge, never split).
3. Run `/setup` — it adopts existing documents rather than overwriting them.
4. Run `/plan` and let it process the captures. From there the method drives.

Until the gate: work the **bootstrap-critical** captures by hand in the pillar
order above. Once self-hosting works, anything still open is just queue work —
this checklist has done its job and retires; its pillars survive as the live
smoke test [live-smoke-missing] proposes automating.

---

## File 4 — CYCLES.md

# CYCLES

Recurring work this project has put on a cycle. Each definition names the
artifact, the steps of one turn, the cadence, and **the observable that marks a
completed turn** — position is never stored, so every check recomputes due-ness
from the observable. The openings and closes of /plan and /next read this file
and file one capture per due turn.

## Upstream catch-up [upstream-catch-up]

**Artifact:** the vendored tree at `vendor/throughliner/`, and the pin in
`tools/vendor.sh`.

**Cadence:** weekly — upstream releases on a weekly Wednesday cycle, so this
matches the rhythm of the thing it tracks. Yours to change; say so here if you
do.

**Observable:** the pinned SHA in `tools/vendor.sh` against the commit of the
latest release on github.com/FlintcraftTech/throughliner (`gh release list`,
or the releases page). A turn is due when they differ. Nothing is stored;
every check recomputes this.

**Steps of one turn.**

1. Read the latest upstream release.
2. **Look for the port-facing changelog published with it.** This is an
   upstream Throughliner feature **coming soon**: the generator exists upstream
   (`scripts/port_changelog.py`, shipped after this port's current pin) and is
   wired into their release process, but no release has published one yet.
   When it appears it gives you, per release: one entry per shipped change,
   which files it touched, the behavioural summary from the session record
   behind it, format-epoch bumps read from the diff — and, the part that
   matters most, **host-only changes marked**, meaning changes that belong to
   the upstream development project and must not be ported.
3. **Until the changelog appears, the fallback:** diff the shipped package
   between your pin and the release tag
   (`git diff <pin>..<tag> -- plugin/throughliner/`), and read the upstream
   session records for that range where a change's intent isn't clear from the
   diff. Treat anything those records mark as host-only as not-to-port.
4. Re-vendor per PROVENANCE.md: update the pin in `tools/vendor.sh`, re-run
   it, regenerate the manifest.
5. Run this port's test suite; fix the shim where the new tree broke a
   translation.
6. File one capture per upstream change that needs shim or mapping work beyond
   the mechanical re-vendor — each capture naming the upstream change and what
   this port must decide about it.
7. Record the turn in your session log under this cycle's slug.

**Three limits, stated by the changelog about itself and true of the fallback
too:** it says WHAT changed, never how to map it — the translating stays
yours; a change to a hook may have no equivalent on your side; and a
format-epoch bump means your own users' documents need migrating, which is
yours to handle.

---

## File 5 — AGENTS-self-hosting-block.md

(The shipped `templates/self-hosting-claude-block.md` — the rule gate's four
parts, the disposition riding the queue item, the required `Rule gate:` close
line, the honest limit, and host-versus-target — adapted in exactly three
ways: "CLAUDE.md" generalised to "whichever rules file OpenCode loads, merged
never split, AGENTS.md beating CLAUDE.md on first match"; "Claude" generalised
to "the model"; and host/target mapped to the port's shape — host = the
installed OpenCode plugin, materialised skills and vendored hooks as invoked;
target = the shim, vendor tree and repository; a target change goes live via
re-vendor or shim edit plus plugin reload. The template itself ships in this
repository at `plugin/throughliner/templates/self-hosting-claude-block.md`, so
its full text is not duplicated here; the three adaptations above are the
whole delta, plus a leading HTML comment telling the recipient how to merge
it.)
