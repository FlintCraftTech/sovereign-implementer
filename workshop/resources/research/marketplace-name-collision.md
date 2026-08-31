# Marketplace name collision — `marketplace add` silently overwrites

Verified 2026-08-27 by web search, during the processing of
[marketplace-name-collision-hazard].

**The finding.** When two sources declare the same marketplace name in their
`marketplace.json`, `claude plugin marketplace add` for the second one
**silently overwrites** the first registration — no warning, no confirmation,
no error. The failure surfaces only later, when plugins from the overwritten
marketplace fail to load. This is a tracked, open Claude Code bug:
[anthropics/claude-code#44042](https://github.com/anthropics/claude-code/issues/44042).
Related: hierarchical namespacing requested in
[#45266](https://github.com/anthropics/claude-code/issues/45266).

**What it means here.** This repository's committed `marketplace.json` declares
`flintcraft`, the same name as the local directory-sourced marketplace every
rezip depends on. So running the beta install command
(`claude plugin marketplace add FlintcraftTech/throughliner#<ref>`) on the
rezip machine would silently repoint `flintcraft` from the working folder to
GitHub, and every later rezip would install the remote instead of local edits
while still reporting success.

**Decisions this informed (recorded on the queue item and its build):**
- a standing CLAUDE.md rule: never add the GitHub marketplace on a machine
  using the local `flintcraft` directory marketplace;
- testers are unaffected — only this project's own machines have a local
  directory marketplace to collide with;
- a distinctly named beta marketplace was considered and refused: the beta
  branch fast-forwards from main, so it cannot carry a divergent
  `marketplace.json` name without giving up the fast-forward design.

**Re-check trigger:** if #44042 ships a fix (a warning or coexistence), the
standing rule can be softened to "read the prompt".
