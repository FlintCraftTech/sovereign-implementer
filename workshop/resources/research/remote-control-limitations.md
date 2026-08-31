# Remote-control limitations and levers (researched 2026-07-06)

Two remote-control pain points came up in a /plan session while Alex was preparing to work chiefly from remote control for several days. Findings on each:

## 1. Claude regenerating self-authored verbatim text (rendering waste)

**The pain:** the method has Claude author text (a capture, batch, or log entry) and then reproduce it verbatim into the chat for approval — regenerating, token by token, what it just wrote. On desktop this is being designed out by view-in-doc (show the text in the open editor, not the chat). On remote control (phone) that doesn't work — viewing an edited file means navigating Google Drive and re-downloading it.

**Is it a Claude Code oversight? No — it's inherent to LLMs.** Any text the model outputs, it generates; there is no "emit a file's bytes without a model pass" mode for the model's own output. So the fix is architectural on our side (don't route the text through Claude — show it from the file), not a missing Claude Code feature.

**GitHub search (2026-07-06):** the precise ask — "surface self-authored text for user approval without a second model generation" — appears **un-raised**. Nearest in spirit: [#62593](https://github.com/anthropics/claude-code/issues/62593) (Claude regenerating whole files instead of surgical edits — token waste), but that's edit granularity, not show-for-approval. A different issue, [#39944](https://github.com/anthropics/claude-code/issues/39944), asks for on-demand display of an *existing* file's contents and was closed as duplicate — not our case. Conclusion: a narrowly-worded feature request would be novel, but low-urgency; the real fix is ours (view-in-doc + a remote-control rendering mode).

## 2. New remote session forks a worktree; random disconnections

**The pain:** starting a new session from remote control creates a whole new git worktree; merging it back from the desktop is painful. So Alex can only start new sessions from the desktop (using /clear), and pre-makes standby sessions for use at work — because sessions disconnect unpredictably (12–48+ hours, no pattern), after which they can't be continued.

**Lever found (verified against docs):** Claude Code has real **WorktreeCreate / WorktreeRemove hooks** ([worktrees docs](https://code.claude.com/docs/en/worktrees), feature [#27744](https://github.com/anthropics/claude-code/issues/27744)). The WorktreeCreate hook *replaces* the default git worktree logic entirely: it receives the worktree name on stdin and must print an absolute worktree path on stdout. So a hook could, in principle, point a new remote session at the existing working tree instead of forking a new one — which would let Alex (and consumers) start fresh sessions from remote control normally, sidestepping the fork-and-merge pain.

**Caveats:**
- Fixes only the worktree-forking half. The random **disconnections** are a separate platform issue no hook can touch. (Alex suspects disconnections may already be resolved; and if new sessions can start cleanly from remote, disconnection matters far less — you just start fresh.)
- It's a **global** behaviour change — Alex runs multiple projects on different plugin installs — so where it lives (SI plugin vs. a standalone user hook) and how consumers opt in matters. Alex is comfortable with it living in SI provided user permission is sought at the right moment (candidate: at /setup).
- Needs real host-side testing before trusting — replacing worktree creation could interact badly with Claude Code's session assumptions.

Both findings feed captures filed 2026-07-06: the remote-control rendering-mode design, and the worktree-override-hook design.
