# Getting Throughliner listed in the Claude marketplace — the two routes, verified 2026-08-22

Researched for the discussion of releasing Throughliner where users can browse for it inside the desktop app. Sources: the official docs page on discovering plugins (code.claude.com/docs/en/discover-plugins), the anthropics/claude-plugins-community repository, and search coverage of the submission guides.

## The two routes

**Official marketplace (`claude-plugins-official`).** Curated by Anthropic; inclusion is at Anthropic's discretion. This is the only marketplace Claude Code adds automatically on first interactive start — so it is the only route to being browsable in-app (the `/plugin` Discover tab, the desktop app's plugin browser, and claude.com/plugins) without the user adding anything. The docs state plainly that the in-app submission forms add plugins to the community marketplace, **not** the official one; there is no self-serve path in.

**Community marketplace (`anthropics/claude-plugins-community`).** Open to third parties via one route only: the submission form at clau.de/plugin-directory-submission (direct pull requests are auto-closed; the GitHub repo is a read-only mirror of Anthropic's internal review system, synced nightly). Submissions pass automated security scanning plus approval by Anthropic's review team. Each listed plugin is pinned to a specific commit SHA in the catalog. The catch for discoverability: users must add this marketplace manually (`/plugin marketplace add anthropics/claude-plugins-community`) — it is not present by default, so listing here is not yet "browse for it in the app" for an untouched install. Claude Cowork users can install community plugins directly from claude.com/plugins.

## Requirements and hazards worth knowing before submitting

- **The marketplace-entry name is an immutable slug.** Once published, the plugin name must never change — users hold installs under it, and a rename breaks them with plugin-not-found. The Throughliner name must be final before any submission.
- **Version consistency** between plugin.json, changelog and git tags is reported as the most common rejection cause in third-party guides.
- The in-app details pane shows a **context-cost estimate** (tokens the plugin adds per turn), a last-updated date, and a will-install component inventory — a listing makes the method's always-loaded cost visible to browsers before they install.
- Community listings are **pinned to a commit SHA**, so each update presumably re-submits or re-reviews; the current weekly-release cadence would interact with that.
- Independent distribution (the current committed-marketplace model) remains fully supported and unaffected.

## What this means for the path

The realistic sequence is community first — form submission, automated screening, human approval — which gets review experience and a public listing at claude.com/plugins, then official at Anthropic's discretion for true default in-app browsability. Nothing found documents criteria for official inclusion beyond "quality and security standards" and discretion.

## Listing updates re-enter review, and no cadence is documented — verified 2026-08-22

Researched for [marketplace-submission]. The community listing's commit pin **updates only after re-review** — every version bump goes back through Anthropic's internal pipeline, and the public catalog syncs nightly from it. No turnaround time is published anywhere found; one developer's question about review duration (anthropics/claude-plugins-official issue #597) sat over a week without an official answer, and Anthropic's only statement is that times vary with volume. Consequence for the release model: the weekly stable promotion cannot treat the listing as a push step. The realistic shape is the weekly stable channel living on this repo, with the listing updated on a slower rhythm — monthly, or when something worth announcing lands — worded in the cycle as "submit the update", landing whenever review clears it.

## Beta-channel install path — ref-pinned marketplace add, verified 2026-08-22

Researched for [beta-tester-pathway]. A marketplace-add can be pinned to a branch, tag or commit by appending `#ref` — `owner/repo#branch-name` shorthand, or full HTTPS/SSH URLs — per the official docs (code.claude.com/docs/en/plugin-marketplaces); settings-level pinning uses a `ref` field (and `sha` for an exact commit, which wins where both are set). So a beta channel needs no separate repo and no zip installs: keep a `beta` branch, fast-forward it to each Wednesday's week-old pick, and a tester adds `FlintcraftTech/throughliner#beta` via the same ask-Claude-runs-the-commands shape the README's install section already uses. Caveat: several of the search hits were open feature requests around ref handling (display of the configured ref, some pinning forms), so the tester walkthrough should be smoke-tested on a real second machine before it is offered to anyone.
