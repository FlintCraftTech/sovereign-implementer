# [HASH] — The test-rezips entry posts at a close once the build has been exercised, and the archive folder is renamed to say what it holds

A rezip had gone unposted, and the capture proposed fixing it by posting at the rezip. The user redesigned it at processing, and the redesign is the substance: **an entry describes a build that has been exercised, not a fresh one.** So it posts at a **close**, and the readiness test is **sessions, not time** — at least one full /plan and one full /next run on the installed build since its rezip, read from `LOG/` records dated after the install date the session opening reports. Her words settling it: *"There's no timing to this."*

**The entry has a two-step lifecycle, which is what makes a rating honest.** A fresh entry carries one of the three labels, a `Commit:` line, the version and the zip — and **no rating**, because too new to rate is what "under testing" says. Posting the new entry unlocks editing the previous one, which gains a testing-outcomes summary from the LOG plus a usability rating out of 5 given by the user at that moment.

**The zip answers where a nerd's download comes from.** The posting step zips `plugin/throughliner/` as it stands into the temp scratchpad and attaches it, so every entry carries the exact build it describes. It is not kept locally: the release archive stays release-only and pruned to three, Discord holds the download, and the commit line lets any build be rebuilt byte-for-byte from git. Built and measured at **371 KB** against the item's estimate of ~270 KB — well under Discord's limit, so the design is unaffected, but the figure is recorded rather than left as the estimate.

**"Rezip builds no zip" was true and misleading, so it is widened rather than corrected.** A rezip still builds nothing; the entry *about* that build attaches one. Renaming the word was refused, and the reason is worth keeping: the channel name keeps "rezip" public, and docs saying "refresh" against a channel saying "rezips" would mislead more, not less.

**`plugin/zip-archive/` becomes `plugin/release-zip-archive/`** on the user's instruction, so its name says what it holds. Scope was traced by grepping `zip-archive` across the project rather than from the discussion, which found the two live sites the item predicted and confirmed the rest were dated records and LOG history, correctly left untouched.

**One part could not be built.** The install-from-zip route was to be described once in the pin — but the pin is the user's own post, and a bot can only edit messages it authored. Filed as [install-from-zip-route-described]; it is the same constraint the how-to re-homing exists to lift.

**Placement is host-only by construction**, in `CLAUDE.md` and never in the shipped close docs: consumers have neither the bot nor the channel.

**Files:** `CLAUDE.md`, `resources/release-ritual.md`, `resources/discord_post.py`.

Rule gate: run — amendment to CLAUDE.md's Discord posts section (host-only by residence); supersedes the capture's own rezip-sited suggestion on the user's redesign; the approval rule cited unchanged.

Routed to Captures: [install-from-zip-route-described]
