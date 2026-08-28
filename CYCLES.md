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

**One turn produces two events, in this order.** The week's pick becomes the new
**beta**, and last week's beta — which has now had its week of soak — promotes to
**stable** and is released. So a build is never released in the same turn that
selects it: the soak sits between the two events, and it is the whole reason the
turn has two halves rather than one.

**Steps of one turn.**
1. Check the branch is `main` — a release never runs from anywhere else.
2. **Promote last week's beta to stable.** The `beta` branch tip as it stands
   *before* this turn touches it is the build being released — it has had its
   week. Read its commit; that is what the release ships.
3. Run the release ritual in `resources/release-ritual.md` end to end against
   that commit — the version bump, the consistency sweep, the repackage, the
   GitHub pre-release, the host reinstall.
4. **Pick this week's beta: the most recent rezip labelled stable on the
   test-rezips-for-nerds list.** The pick is mechanical and takes no judgment on
   the day — the label was applied when that rezip was posted, describing a
   build that already existed, so the turn reads a recorded state rather than
   asking "is this good enough?" That prospective readiness question stays
   banned, which is what the 2026-08-09 decision was protecting.
5. **Fast-forward the `beta` branch to that rezip's commit**, read from its entry
   in the rezip archive. Testers installing from `FlintcraftTech/throughliner#beta`
   pick it up on their next update. Where the pick is not a descendant of the
   current beta tip, stop and say so rather than forcing the branch.
6. Offer the beta announcement, filled in from
   `resources/beta-offer-announcement-template.md`. It goes out through the bot
   on the user's explicit yes to the exact text, and gets its line in
   `INBOX/sent.md` in the same turn.
7. Record the turn in `LOG/` under this cycle's slug — both events, with the two
   commits named.

**Refused, and recorded so it is not re-proposed:** choosing among candidate
rezips each Wednesday on the day's judgment. The selector is mechanical — most
recent stable label wins. Also refused: a separate beta cycle with its own
cadence — one cycle, beta as a step inside its turn, the user's call 2026-08-22.

**Superseded selector, kept because the reasoning is cited elsewhere:** the
original pick rule was "newest rezip at least a week old". Its week-old property
now lives in the promotion step above rather than in the pick — step 2 releases a
build that has had exactly that week, so the property is enforced by the turn's
shape instead of by the selector reading a date.
