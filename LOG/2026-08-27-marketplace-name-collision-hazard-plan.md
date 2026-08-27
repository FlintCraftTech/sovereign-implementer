# d31b553 — Marketplace collision confirmed by research; flag cleared by a standing rule

The feared behaviour is the real one: web research at the decision step confirmed `marketplace add` silently overwrites a same-name registration — open Claude Code bug #44042 — so the beta install command on the rezip machine would silently repoint `flintcraft` to GitHub. Finding filed at `resources/research/marketplace-name-collision.md` with its index line.

Cleared as designed out: a build item writes one guard sentence into CLAUDE.md's Rezip section (never add the GitHub marketplace on a machine using the local directory marketplace), testers are unaffected (no local marketplace to collide with), and the residue — the bug itself — is stated. Refused: a distinctly named beta marketplace, because the beta branch fast-forwards from main and cannot carry a divergent marketplace name. Rule gate: run — amendment to the Rezip section, derivation named, nothing evicted.

**Queue changes:** [marketplace-name-collision-hazard] rewritten with build block and moved Unprocessed → Processed, cleared.
**Work processed:** kept — [marketplace-name-collision-hazard].
