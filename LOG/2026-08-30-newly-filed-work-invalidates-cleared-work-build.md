# 778d6a3 — Digest flags a capture whose prose names an item already cleared to run

Raised by the user at the end of a /rescan on 2026-08-29: should there be a rule checking that what a scan files blocks nothing in the cleared region? Filed as the reworded version of that, on Claude's recommendation and her agreement.

**The rule as first put was refused, and the reason travels so it is not re-proposed.** A capture cannot block anything by construction — only a Processed item carrying `Blocked by:` holds work back, and /rescan files captures and nothing else. A check for that would never fire, which is worse than one that fires rarely: it would read as coverage while covering nothing.

The real risk is invalidation rather than blocking, and there is one recorded instance. Filing a capture about a bot limitation revealed that a cleared item could not be built as written. Nothing detected that; it was caught because one session happened to be holding both items in view, which is exactly the condition a fresh short session does not have.

Weighed as an amendment before anything freestanding was considered. The digest already reports placement contradictions, including an item whose own text says it must not be built — the same family, but reading the item's own words, where here the falsifying fact arrives in a *different* entry that never mentions it. The load-bearing question had a partial yes: the falsifying capture *named* the cleared item's slug, and the digest already extracts every slug an entry cites. Crossing those two facts is arithmetic on computed data, so the site is the digest and no rule was authored anywhere.

**The provision that binds the build, carried from the item unchanged: do not build a check that reports a clean pass.** It prints only when it finds something, because a clean result here would assert that no cleared item has been invalidated — which nothing can know. The block's partial-coverage note extends to it, and says both limits where it reports: a capture that invalidates without naming the slug is not reached, and nothing can tell whether a named one actually invalidates anything.

**Observable met:** two suite cases pass — a capture naming a cleared item is flagged, and a capture naming another capture is not, since captures cross-reference each other constantly and firing on that would make the flag noise by its second run.

**Depth:** full — alternative seriously weighed.
**Files touched:** `plugin/throughliner/scripts/queue_digest.py`, `resources/testing/test_queue_digest.py`.
**Routed to Captures:** none from this item.
