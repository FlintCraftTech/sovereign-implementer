# [HASH] — plan — the rezip archive takes the narrow carve-out now, because the release cycle is four days away

The archive step was refused on its first ever run: a rezip happens after a close, so the scope-lock reads the session as planning, and `plugin/rezip-archive/` is not on the planning writable list.

**Checked at processing, and it was worse than the item said: the folder does not exist at all.** The step has never once succeeded, so the release ritual's steps that read a build's commit from its archive readme and copy the archived zip currently point at nothing — with the weekly release due 2026-09-02.

**Settled as a sequence rather than a choice between the two candidate fixes.** This item takes the narrow carve-out; the general fix is [ritual-declares-writable-paths], designed without a deadline on it, and it evicts this carve-out when it lands. The general one cannot be designed, built, rezipped and restarted safely in four days.

**A fallback was written in so Wednesday is not blocked either way:** the archive readme is the channel post's own text, so a build's commit is readable from Discord and its zip rebuilds from that commit.

**One honesty note recorded rather than glossed:** the `plugin.json` carve-out this copies is deliberately ONE PATH, and its own comment records that a self-declared marker was refused as a full bypass. This permits a folder, which is a step beyond that precedent — defensible because the archive is gitignored build output rather than part of the package, and stated rather than passed off as the same move.

Rule gate: not needed — the shipped planning list in `plan.md` is untouched, exactly as the `plugin.json` carve-out left it, because a host-only path in shipped text would name a folder consumers do not have.

**Queue changes:** [rezip-archive-blocked-by-scope-lock] kept and cleared, first in the region on its deadline.
**Work processed:** kept — [rezip-archive-blocked-by-scope-lock].
