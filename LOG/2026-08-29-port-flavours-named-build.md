# [HASH] — The two port flavours get names: tracking and independent

Two flavours of port were already recognised and neither had a name, so nobody could say what a given port promised — including this project. A user choosing between ports could not tell whether the one they installed would follow the method or had gone its own way; a porter had no way to signal it; and this project could not tell which ports its changelog was even for.

The item supplied the definitions and left the naming to the build. **Tracking** takes this project's changes at face value and adds nothing beyond what its own system needed to fit; **independent** is its own thing and adopts only the changes it wants. Both are stated as welcome, in those words, because the point of naming them is legibility rather than ranking. A registry of who runs which stays refused: maintaining a list of other people's projects is an obligation this project cannot keep accurate, and being absent from it would read as disapproval.

The shipped home is a new `docs/ports.md`, chosen at build time as the item allowed — a porter reading the repository lands on README, which now names both flavours and links through.

Tick: done, confirmed — both flavours are defined in a shipped file and the README names them.

Depth: short.

Rule gate: run — admitted as a definition rather than a rule. It constrains no session's behaviour and adds nothing to the always-loaded set; it gives two things names, so a parent is not applicable and that is stated rather than a parent invented for form's sake.

**Files touched:** `plugin/throughliner/docs/ports.md` (created), `README.md`.

**Routed to Captures:** [spec-owes-port-flavour-names] — SPEC's ports paragraph describes both flavours without naming them, and a build does not write product truth, so the sentence is filed for the next planning session.
