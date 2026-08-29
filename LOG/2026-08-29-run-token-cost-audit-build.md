# [HASH] — Navigation is 22% of a run's tool calls, measured on two real runs

The MCP-server brief proposed purpose-built tools replacing read-find-parse-write with one structured call, and its own first step was to audit a real run. This is that step. Two runs were measured separately on the user's direction, because a build run and a planning run are characteristically different — and, as she noted at this run's off-ramp, they run on different models, so the figures are not interchangeable.

```
BUILD run    2026-08-28, on Opus 5
             417 tool calls — 91 navigation (22%), 271 work (65%)
PLANNING run 2026-08-28/29, on Fable
             254 tool calls — 57 navigation (22%), 159 work (63%)
```

Against the fixed read cost, which no transport changes: a run loads the always-loaded rules, the run docs, the close docs, SPEC and the cleared region of the queue — roughly a third of a megabyte — before it navigates anything. So the proposal's target is about a fifth of tool calls sitting on top of a fixed cost several times larger. That is not nothing, and it is not the picture the brief implied.

**A wrong number was produced first and is recorded rather than quietly replaced.** The first classification pass reported navigation at 5% in both runs. Nearly every command in these transcripts opens with `cd "<project path>" &&`, and the path contains spaces, so a pattern anchored to the real command matched nothing and a quarter of all calls fell into "unclassified". A plausible wrong figure is exactly what an audit must not hand onward.

Tick: captured — three findings.

Depth: full — reasoning contested, per the corrected pass above.

**Files touched:** none. The audit read two session transcripts and edited nothing.

**Routed to Captures:** [navigation-share-measured-at-22-percent], [scoping-beats-transport-on-measured-evidence], [build-runs-reread-files].
