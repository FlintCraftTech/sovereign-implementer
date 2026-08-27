# [HASH] — Posting gains a second kind: tips, with their own test, their own channel and a pipeline from rezip to post

The posting rule said the purpose was to announce new features, changes and improvements to Throughliner "and nothing else". The user's channel restructure splits that: some of what went to announcements is from now on a **tip**, announcements narrows to **news**, and old posts may be recycled.

**Two kinds, two tests, and neither is the other's fallback.** News asks *did Throughliner change?* — the test that already existed, and it stays exactly as it was, including its warning that a session which has just learned something useful feels like it has something to announce and that the feeling is not the criterion. A tip asks *does this explain one feature the plugin has?* — no release and no event required. The exclusion of general Claude Code tips survives both: a tip is about this plugin.

**The pipeline, the user's design in Claude's words.** Candidates are noticed at the **rezip**, the moment a feature lands in the installed build, and pooled in `ANNOUNCEMENT-IDEAS.md`. The **release** is what makes a candidate postable, so the ritual marks which pooled candidates its shipped features clear and leaves a note. The next **/plan** reads that note and files the cleared ones as dated post items on the one-a-day rhythm — new or updated features first, historical tips on slow news days.

**Two additions carry weight beyond their length.** The sent-register line now records **which channel** a post went to, which is what lets the existing repeal-grep tell a tip from an announcement from a rezip entry. And every outbound post checks the how-to topics for claims it touches, because those exist for welcoming and onboarding and **their number stays small enough to serve that purpose** — a bound stated without a figure, since a number here would have no derivation. A needed tweak is a bot edit of the bot's own how-to post, which is why the re-homing migration [howto-posts-bot-authorship] is named rather than assumed.

**Nothing is posted by either ritual step, and that is deliberate.** The rezip pools and the release marks; both report in one line, including when they found nothing. Posting stays where approval lives.

**The staleness the rule now creates is already covered**, which is why no new mechanism was added for it: a tip can be falsified by a later repeal exactly as an announcement can, and the existing repeal-grep over `INBOX/sent.md` reaches it now that the register records the channel.

**Files:** `CLAUDE.md`, `resources/release-ritual.md`. Reads but does not change: `ANNOUNCEMENT-IDEAS.md`, `INBOX/sent.md`.

**A claim in this build was asserted rather than checked**, and it bit the same day: the sentence saying the bot may post in tips, announcements and test-rezips was written from the design discussion, and the bot could in fact post only to the third. Filed as [claude-md-asserted-bot-posting-channels-unchecked].

Rule gate: run — amendment to CLAUDE.md's Discord posts section: the "and nothing else" clause reworded to carry the tips kind with its own test ("explains one Throughliner feature"); the did-Throughliner-change test stays for news; the exclusion of general Claude Code tips stands; nothing else evicted.

Routed to Captures: [claude-md-asserted-bot-posting-channels-unchecked], [one-post-a-day-is-per-channel], [tip-candidates-need-visibility-screen]
