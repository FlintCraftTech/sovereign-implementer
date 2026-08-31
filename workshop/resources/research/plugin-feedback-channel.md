# How Claude Code plugins collect user feedback

Research filed 2026-06-22 to tee up the [consumer-plugin-feedback-channel] design session — giving consumers a way to report plugin/method issues back to the author, without polluting their own project's queue.

## The decision this informs

A consumer's Claude (or the consumer themselves) hits a plugin/method problem. There's nowhere right to put it: the consumer's QUEUE is for their own app, so plugin feedback either gets dropped or pollutes their queue (the near-miss that filed this item). Need: a defined channel + report format.

## What the research found

### 1. Claude Code already has `/bug` — but it does NOT cover third-party plugins

Claude Code ships a built-in `/bug` command that reports issues from within Claude Code, capturing session context. **But `/bug` reports problems with Claude Code itself — it routes to Anthropic, not to a third-party plugin author.** So `/bug` is the wrong channel for SI-specific feedback: it would send an SI method complaint to Anthropic, where it dies. This is the key distinction the design must encode — a consumer's Claude must NOT reach for `/bug` for an SI issue.

(Security vulnerabilities are a further special case in Claude Code: those go through Anthropic's HackerOne program, not `/bug`, Issues, or Discord. SI's own red-flag mechanism is the in-method analogue.)

### 2. GitHub Issues is the standard plugin/extension feedback channel

Both Claude Code and VS Code route plugin/extension bug reports and feature requests to **GitHub Issues** (plus Discussions/Discord for community). It's the zero-infrastructure standard. SI already has a repo — `FlintCraftTech/sovereign-implementer` — so a GitHub issue path needs nothing built: a consumer's Claude drafts the issue body, the user pastes it into the repo's Issues page.

### 3. A direct author↔consumer loop is worth building deliberately

VS Code's own feedback work concluded that a direct channel between authors and "most-likely consumers" produces better, faster, more collaborative feedback than generic channels. Supports building a dedicated SI feedback path rather than leaning on Claude Code's generic `/bug`.

### 4. Privacy/scrubbing is well-supported best practice — matches the constraint already noted

The design constraint Alex already recorded (the report must be minimal and scrubbed — describe the plugin issue, never dump the consumer's project or secrets) is squarely standard practice: redact credentials, tokens, and PII before any report leaves the environment; data-minimization (include only what's needed to reproduce). The drafted report should be scrubbed *by construction* — the format describes the issue, not the project.

## How this bears on the SI decision (for the design session)

- **Primary channel: GitHub Issues on the SI repo.** Zero infrastructure, standard, already exists. A consumer's Claude drafts a scrubbed issue body; the user pastes/files it.
- **Fallback: the contact-form-paste idea** Alex floated — for users not on GitHub. Needs Alex to host a form, so it's the heavier option; likely a phase-2.
- **Hard distinction to encode in the method:** SI feedback routes to the SI repo/author, NOT to Claude Code's `/bug` (which goes to Anthropic). The consumer's Claude needs to know the difference.
- **The deliverable is the report format** — a scrubbed, minimal plugin-issue template that's safe to paste, plus the instruction that tells a consumer's Claude when and how to use it (the near-miss showed the consumer's Claude correctly *recognised* a plugin issue but had nowhere to route it).
- **Two entry paths, one format** (already in the capture): Claude-noticed plugin issue, and user-initiated (a question the FAQ doesn't answer, a bug). Both produce the same scrubbed report.
- This is likely a **shipped feature** (consumer Claudes need the instruction + the format), so it touches SPEC and the plugin docs — a spec-edit plus build, as the capture already flags.

## Sources

- [Providing Feedback & Reporting Issues — anthropics/claude-code (DeepWiki)](https://deepwiki.com/anthropics/claude-code/2.4-providing-feedback-and-reporting-bugs) — `/bug`, GitHub Issues, Discord, HackerOne for security
- [anthropics/claude-code (GitHub)](https://github.com/anthropics/claude-code) — the repo where Claude Code's own issues are filed
- [Feedback Channels — microsoft/vscode Wiki](https://github.com/microsoft/vscode/wiki/Feedback-Channels) and [Proposal for a better feedback loop with extension authors (#91714)](https://github.com/microsoft/vscode/issues/91714) — GitHub Issues as the standard; the author↔consumer loop argument
- [Bug report templates / privacy practices (Screendesk)](https://blog.screendesk.io/bug-report-example/) — redact credentials/tokens/PII; data minimization in user-submitted reports
