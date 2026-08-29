# [HASH] — plan — an MCP-server brief became an audit, because the fixed read cost dwarfs what MCP could save

The user brought in a build brief proposing a local MCP server shipped inside the plugin, giving Claude purpose-built tools for the method's file work. Her stated problem was the token cost of a run.

**Measured at processing, which decided the shape.** A `/next` run loads roughly a quarter of a megabyte before it edits anything — the always-loaded rules (76KB), `next.md` and `next-build.md` (55KB), the close docs (51KB), SPEC.md (83KB) and the cleared region of QUEUE.md. An MCP server touches none of it. And the one place structure could have replaced reading was deliberately refused on 2026-08-17, when the digest was stopped from standing in for the queue read.

**Half the brief's tool table already exists as scripts** — `queue_digest.py` returns the queue as structured facts in one call, `reorder_queue.py` does moves byte-for-byte — so the real delta is script-versus-tool, not tool-versus-nothing. And the write-side tools are the exact shape `pre_tool_use` refuses: a project file written through a script rather than the editing tools.

**So it could not pass the buildability check as a build**, and "research this, then build that" is the shape the decision step must refuse. It was kept as an `[audit]` scoped to measuring where a run's tokens actually go — with the honest limit written in, that the denominator was measured and the numerator was not.

**Amended later the same session on the user's direction:** it now measures a `/plan` run and a `/next` run separately, her reason being that they are characteristically different — a build reads once then edits, a planning run re-derives its ordering at every pick. Two data points from this session are recorded on it.

**Queue changes:** [run-token-cost-audit] filed and cleared; amended later the same session.
**Work processed:** kept — [run-token-cost-audit].
