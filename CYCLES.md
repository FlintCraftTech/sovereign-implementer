# CYCLES

Recurring work this project has put on a cycle. Each definition names the
artifact, the steps of one turn, the cadence, and **the observable that marks a
completed turn** — position is never stored, so every check recomputes due-ness
from the observable. The openings and closes of /plan and /next read this file
and file one capture per due turn.

## Weekly release [weekly-release]

**Artifact:** the GitHub release of the Throughliner plugin.

**Cadence:** weekly on Wednesday, declared by the user 2026-08-22.

**Observable:** the published date of the latest GitHub release (`gh release list`).

Declared rather than derived from the record — the definition says which, and
this one is the user's decision. A turn is due when that published date falls
before the current Wednesday; the rezip list supplies the candidate build.

**Steps of one turn.**
1. Check the branch is `main` — a release never runs from anywhere else.
2. Pick the build: **the most recent rezip labelled stable on the
   test-rezips-for-nerds list.** The pick is mechanical and takes no judgment on
   the day — the label was applied when that rezip was posted, describing a
   build that already existed, so the turn reads a recorded state rather than
   asking "is this good enough?" That prospective readiness question stays
   banned, which is what the 2026-08-09 decision was protecting.
3. Run the release ritual in `resources/release-ritual.md` end to end — the
   version bump, the consistency sweep, the repackage, the GitHub pre-release,
   the host reinstall.
4. Record the turn in `LOG/` under this cycle's slug.

**Refused, and recorded so it is not re-proposed:** choosing among candidate
rezips each Wednesday on the day's judgment. The selector is mechanical — most
recent stable label wins.

**Superseded selector, kept because the reasoning is cited elsewhere:** the
original pick rule was "newest rezip at least a week old". Its week-old property
now lives in the promotion step of the three-channel model rather than in the
pick. That model — a Wednesday turn producing two events, this week's pick
becoming the new beta and last week's beta promoting to stable — is not yet
built; the steps above are the release half, which stands on its own. The
promotion step joins this definition when [beta-tester-pathway] ships.
