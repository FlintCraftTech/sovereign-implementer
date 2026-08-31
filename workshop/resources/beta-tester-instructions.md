# Standing instructions for a beta tester sending session data

What to give a beta tester at the end of a Throughliner session so their session
data reaches this project. Two prompts they paste into their own session, plus a
manual fallback for finding the files by hand.

**Not a plugin feature, and deliberately not.** Throughliner already has a
report route for "I think this is broken". This manual collection exists to get
richer data than that route returns while a tester is new — reporting will not
normally look like this.

## Why the earlier prompt had to be replaced

The first version asked for a "full transcript of this chat including thinking
processes". Two independent things were wrong with it.

**The safeguard refusal.** Opus 5's safeguards refuse a request for reasoning
outright (`[reasoning_extraction]`), and **not reliably** — the same prompt had
worked in an earlier chat. So a tester meets the refusal at random, with no way
to tell a safeguard from a broken instruction. Which clause exactly trips it was
never established and is not needed for the fix.

**The raw file is the evidence.** Asking Claude to write out the conversation is
what this project's own transcript-reading practice rules out: a regenerated
transcript is a lossy reconstruction with the tester's replies paraphrased,
while the raw `.jsonl` the app already saves is the primary record and needs no
cooperation from the model at all.

Three changes followed, each from an observed failure. The request for thinking
processes came out. The request for a transcript came out, replaced by attaching
the file the app already writes. And the email step split into its own message,
because the old prompt bundled the two and one refusal cost both.

## The end-of-session prompt

> I'm a beta tester for Throughliner and my session data is being collected as test data.
>
> Claude Code saves each session's conversation as a .jsonl file under %USERPROFILE%\.claude\projects, in a folder named after this project's path. Please find the file for THIS session — the most recently modified .jsonl in that folder — and tell me its full path.
>
> Then write a short plain-English record of this session: what I was trying to do, what happened, anything that went wrong or confused me, and anything that worked well. Base it only on our conversation. Don't try to include your own reasoning — that isn't retrievable, and asking for it gets the request blocked.

## The email prompt, sent separately once the first is done

> Please check my Outlook connection is working, then start a draft email to <address> with the session file attached and the session record in the body. Subject: Throughliner beta test — session record, <today's date>. Leave it as a draft; I'll read it and send it myself.

## The manual fallback

Where the tester finds the file themselves, the instruction must say: **that
folder holds sub-folders as well as files, and only the files matter** — sort by
Type, take everything whose type is JSONL, and ignore every folder.

The correction matters. The first version said "inside are one or more .jsonl
files", and the tester opened the sub-folders instead and reported dead ends,
because the `.jsonl` names are session ids and read as unopenable to anyone who
does not know that.

**Simplest instruction of all, and the one to prefer: attach every `.jsonl` in
the folder.** They run a few hundred KB each, and which session is which is
answerable at this end by reading them.

## What this rests on

- The safeguard behaviour as observed 2026-08-30: two runs of the old prompt,
  one blocked, one not.
- The desktop app saving sessions as `.jsonl` under
  `%USERPROFILE%\.claude\projects`, confirmed from the tester's own screenshots
  the same day.

Received transcripts are stored gitignored and unpublished — that decision and
its reasoning ride [tester-data-carries-employer-material].
