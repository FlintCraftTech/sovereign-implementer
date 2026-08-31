# Claude "copying" vs generating text — and what the view-in-doc fix really rests on

Filed from the [view-in-doc-remote-control-tension] capture (finding dated 2026-07-02; the write was blocked in its originating test session by the method-docs-only scope-lock, so it landed at the next /plan).

## The finding

Claude generates every token it emits. There is no clipboard or copy channel — even when it reproduces text "verbatim," it is regenerating that text through the model, not lifting bytes from a source. So the folk claim "Claude can't copy text" was never the real constraint:

- **Short-to-moderate blocks** reproduce reliably. For a queue line, a capture, a log entry, Claude reproduces the exact text dependably.
- **The real constraints are two, and neither is "can't copy":**
  1. **Fidelity drift on long blocks** — over a long enough passage, regeneration can introduce silent "helpful corrections" (a reworded clause, a tidied list), so the reproduced copy quietly diverges from the source.
  2. **Token cost** — re-emitting text the user could read in place spends output tokens on every render.

## Why this matters for the method

The view-in-doc pointer treatment ([view-in-doc-group-a], [capture-verbatim-first]) does **not** rest on an inability to copy. It exists because re-emitting doc-resident text is **lossy on long blocks and costly every time**, and pointing the user at the authoritative doc sidesteps both. So this finding does **not** license dropping the view-in-doc fix — if anything it sharpens the rationale (the fix targets drift + cost, not a copy limitation).

## Open tension this surfaced (carried separately in the queue)

The view-in-doc / read-it-in-a-separate-app workflow assumes a desktop editor open beside the chat. Under remote control (driving from a phone or a remote surface) the user can't easily open the doc alongside — a real counter-pressure on the view-in-doc direction. Tracked as a design item alongside the remote-control / [cruise-control] / editor-awareness cluster.
