# [HASH] — Beta channel wired into the weekly release: a two-event Wednesday turn, a README section, and the announcement as cycle material

Built in the 30-item run of 2026-08-28. The three-channel model settled on this item across a week of planning became the release cycle's own shape: one Wednesday turn now promotes last week's beta to stable first, then picks this week's beta (the most recent stable-labelled rezip) and fast-forwards the `beta` branch to it. A build is never released in the turn that selects it — the soak sits between the two events, which is why the turn has two halves. The announcement was authored as a reusable template with a delete-after-first-use launch paragraph, per the user's 2026-08-28 amendment that drafting is only worth doing as cycle material; README gained a "What the beta channel is" section written honestly early. The install half ([beta-branch-install-pin]) and the smoke test had already shipped, so this build was the cycle wiring alone, reconciled against them.

Tick: done, confirmed — the cycles parser reads the amended definition whole; the `beta` branch exists; the smoke test ran 2026-08-27, so no untested-route caveat is owed.
Files touched: CYCLES.md, README.md, resources/beta-offer-announcement-template.md (created).
Rule gate: not needed — no method rule authored; the files are this project's own cycle materials.
