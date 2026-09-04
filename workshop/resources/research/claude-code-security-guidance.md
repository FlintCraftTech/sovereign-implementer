# Claude Code's security guidance, as read on 2026-09-03

**Subject:** what Anthropic's own documentation says about Claude Code security, read so the method's red-flag screen and its weekly maintenance sweep can be checked against it. Two pages read on 2026-09-03: `https://code.claude.com/docs/en/security` (the guidance) and `https://code.claude.com/docs/en/claude-security` (the scanner plugin). Re-read each maintenance-sweep turn; changes are filed as captures.

## What the guidance page says

- **Permission model.** Manual mode starts read-only and asks before edits and system-modifying commands; a built-in read-only command set runs unasked. Auto mode replaces the user with a classifier that blocks actions it judges unsafe; explicit allow and deny rules still apply.
- **Built-in protections.** A sandboxed bash tool with filesystem and network isolation; a working-directory boundary (writes only inside the start folder; reads outside it prompt in manual mode); per-user, per-codebase and per-organisation allowlists; an accept-edits mode auto-approving edits and a fixed set of filesystem commands inside the working directory.
- **Prompt injection is the one named threat.** Defined as text inserted to override or manipulate the assistant's instructions. Safeguards: the permission system, context-aware analysis, input sanitisation, network commands (`curl`, `wget`) not auto-approved, web fetch in an isolated context window, trust verification for new codebases and MCP servers, command-injection detection, fail-closed matching of unmatched commands, natural-language descriptions of complex commands, credentials in the OS keychain or file-permission-protected.
- **Best practices for untrusted content:** review commands before approval; avoid piping untrusted content to Claude; verify changes to critical files; use VMs for scripts and external services; report suspicious behaviour with `/feedback`.
- **Best practices for sensitive code:** review every change before approval; project-specific permission settings; dev containers; audit permissions regularly with `/permissions`. Team: managed settings, shared permission configurations in version control, OpenTelemetry monitoring, `ConfigChange` hooks to audit or block settings changes.
- **MCP.** Anthropic reviews directory connectors against listing criteria but security-audits no MCP server; users are encouraged to write their own or use trusted providers.
- **Cloud and Remote Control.** Cloud sessions run in isolated VMs with network limits, scoped credentials, branch-restricted pushes and audit logs. Remote Control keeps execution local; the transcript is stored on Anthropic servers while connected.
- **A Windows warning:** do not enable WebDAV or grant paths like `\\*`, which can let network requests bypass the permission system.
- **The page's own limit:** no system is immune; the user is responsible for reviewing proposed code and commands before approval.

## What the scanner page says

The Claude Security plugin (`/plugin install claude-security@claude-plugins-official`) runs a multi-agent vulnerability scan of a repository or a diff inside a session, writes a timestamped results folder (markdown, JSONL, SARIF with CWE categories, a revision stamp), and drafts patches that are never applied automatically. Prerequisites: a paid plan with dynamic workflows, Python 3.9+ on the PATH as `python3`, git for diff scans. Scans are nondeterministic. It sits in a stack with the security-guidance plugin (in-session), `/security-review` (one pass over the current branch), Code Review (pull requests) and the managed Claude Security product.

## How it bears on the method

- The red-flag scope (skill-nonspecific-rules.md, Red flags) names data exposure, unauthorised access, credential handling, injection vectors, information leakage and unprotected storage. It does not name prompt injection through observed content — the one threat the guidance page names — though the rules handle two instances of it (INBOX mail is data; issue text is data).
- `/security-review` is the pass a weekly maintenance turn can afford; the scanner plugin's prerequisites are not met on this machine (`python3` is not on the PATH under that name).
- Nothing here is a standard to comply with; it is guidance, re-read on a cycle so a change to it is noticed.

## Assessment of the frame

- **TIME RANGE:** not applicable — a documentation read, current as of the read date; the re-read each sweep turn is what keeps it current.
- **PEOPLE:** applies to every Throughliner user, since all run inside Claude Code; the team-security practices apply to none of the known users, who work alone.
- **FRESHNESS:** the pages are amended without notice; the auto-mode classifier and the scanner plugin are both recent. Weekly re-read.
- **RISK IF WRONG:** a stale copy would let the red-flag screen miss a threat Anthropic has since named, or describe a tool that has changed. Bounded by the weekly re-read; no red flag warranted on the finding itself.
- **ALTERNATIVES:** the CISO guide the page links and the sandboxing page were not read; a future turn may read them where the sweep's security pass needs them.
