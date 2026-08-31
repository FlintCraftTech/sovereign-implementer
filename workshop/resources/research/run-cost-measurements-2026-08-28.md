# Run-cost measurements — navigation share, scoping vs transport, re-reads

From the run-token-cost audit of 2026-08-29 over the raw transcripts of
2026-08-28's build run and planning run; moved here from three queue captures
2026-08-30 at processing, numbers carried verbatim. This is the evidence base
for the MCP question, which the user has had to push for across sessions.

## Navigation is 22% of tool calls in both runs

Classified by tool and by command after stripping the `cd "<path>" &&` prefix
every command carries — a first pass that missed the prefix put a quarter of
calls into "unclassified" and reported navigation at 5%, kept as a warning.

```
BUILD run   2026-08-28 05:53 -> 14:10, on Opus 5
            417 tool calls — 91 navigation (22%), 271 work (65%)
            of the navigation: 71 searches and shell reads, 20 re-reads of a
            file the run had already read

PLANNING    2026-08-28 13:30 -> 2026-08-29 00:58, on Fable
run         254 tool calls — 57 navigation (22%), 159 work (63%)
            of the navigation: 53 searches and shell reads, 4 re-reads
```

The two runs are on different models and are stated separately — the user's
instruction. It is coincidence, not a finding, that both land on 22%.

**Against the fixed read cost, which no transport changes:** a build run loads
roughly a third of a megabyte before navigating anything (always-loaded rules
78KB, run docs 55KB, close docs 73KB, SPEC 91KB, the cleared region of a 125KB
queue); a planning run pays `plan.md` (86KB) instead of the run docs. So the
MCP proposal's target is about a fifth of tool calls sitting on a fixed cost
several times larger — not nothing, and not the picture the original brief
implied. Whether a fifth is worth a server is a decision, not a conclusion the
numbers make.

## Scoping beat transport, on this project's own evidence

The digest's `--next` mode answered one question in 1,652 characters against
the full print's 16,959 — a saving of roughly a tenth, from scoping alone,
needing a script flag and no new transport. Half the MCP brief's proposed tool
table already exists as scripts (the digest returns structured facts in one
call; the mover moves byte-for-byte), so the delta a server adds is
script-versus-tool, not tool-versus-nothing — and the brief's write-side tools
are the exact shape the safety hook refuses. **No transport comparison was
run**: a fair one needs the same scoped question asked both ways, counted the
same way, and nothing here did that, so no claim is made either direction.

**Unverified, still to check before any MCP build is scoped:** that a plugin
may define an MCP server in `.mcp.json` at its root, that Claude Code starts
it automatically when the plugin is enabled, and the tool-naming shape.

## Build runs re-read; planning runs barely do

20 re-reads in the build run's 417 calls against 4 in the planning run's 254 —
same project, adjacent days. Plausible shape rather than defect: a build
returns to files it edited; planning works inside the queue. Why it matters:
a re-read is the one navigation class where the session already had the
content — a memory/working-file question no transport touches. The design
question it raises is filed as [build-working-file-records-touches].

## Validity assessment (per [research-validity-criteria], in force from its decision)

- **Time range of the product:** measurements are of two specific runs on the
  named builds; drift as the method changes — dated for that reason.
- **People involved:** measures Claude's tool use, the right subject for a
  cost question; says nothing about the user's session experience.
- **Relevance in time:** re-measure after any change to what runs load
  (e.g. the workshop restructure); the fixed-cost figures are the perishable
  half.
- **Alternatives researched and ruled out:** scoping was measured and won on
  this evidence; MCP transport was NOT ruled out — explicitly unverified above.
- **Risk if wrong:** months of tooling work aimed at the wrong cost — the
  user's stated exposure; mitigated by the unverified list being explicit.
