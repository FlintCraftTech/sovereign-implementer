# [HASH] — A rezip guard against the marketplace name collision, resting on a confirmed CLI bug rather than a suspicion

The local `flintcraft` directory marketplace is what every rezip on this machine depends on, and this repository's committed `marketplace.json` declares the same name. The worry was that adding the GitHub marketplace would collide. It was deliberately never tested, because the test was the risk.

**The open question is answered rather than guessed, which is what makes this a guard and not a superstition.** Research at the decision step (`resources/research/marketplace-name-collision.md`) found that `claude plugin marketplace add` **silently overwrites** an existing registration of the same name — no warning, no error — and that this is an open, tracked Claude Code bug, anthropics/claude-code#44042. The feared case is the confirmed behaviour: the install command would repoint `flintcraft` at GitHub, and every later rezip would install the remote while reporting success.

So the build writes one sentence into CLAUDE.md's Rezip bullet: never run that command against the GitHub repository on a machine using the local directory marketplace, with the bug number and the research file named so the limit is traceable and revisable.

**What the guard does not do, stated because a guard that over-claims is worse than none.** The bug is outside this project's control, and a rule is a rule rather than a mechanical block — nothing stops the command being run. Its reach is also narrower than it might read: only this project's own machines are exposed, because testers have no local directory marketplace to collide with.

A distinctly named beta marketplace was refused. The beta branch fast-forwards from main and cannot carry a divergent `marketplace.json` name without giving up that design. Worth re-examining only if #44042 ships a fix.

**A live instance turned up hours later, in this same session.** The `#beta` install on the user's second machine registered under the name `flintcraft`. That machine is one of her own, so the "only testers are safe" reassurance does not cover it, and nothing checked whether a registration was overwritten there. Filed as [second-machine-marketplace-overwrite-check] — the guard's first real test, arriving the day it was written.

**Files:** `CLAUDE.md`.

**Red flag:** carried one, **cleared** at planning — designed out by the standing rule this build writes, plus the limited exposure above.

Rule gate: run — amendment to CLAUDE.md's Rezip section (a guard clause on the existing rezip instructions, naming its derivation: a verified external bug); nothing evicted, no freestanding rule added.

Routed to Captures: [second-machine-marketplace-overwrite-check]
