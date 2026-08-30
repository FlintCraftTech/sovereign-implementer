# [user] Post the 1.21.1-test1 entry to the nerds channel, with its archived zip [test-rezip-entry-1-21-1-test1]

Walk-through driven 2026-08-30 in a /next run, written as it went. The earlier record under this slug is the planning session that cleared the item, not a drive, so there was nothing to resume from.

## Step 1 — draft taken from the archive readme, not composed

The archive readme and the channel post are required to be the same text, so the draft is a byte-for-byte copy of `plugin/rezip-archive/throughliner-v1.21.1-test1.md` — copied rather than retyped, and the copy asserted identical before it was shown. 1,139 characters against the channel's 2,000 limit. Label, `Commit: 4efdcff` and version all match the readme, which is what step 1 asks to look for.

One thing was put to the user rather than changed: the entry's fourth paragraph explains an internal mishap (a scope-lock refusing the archive step), which the posting brief would normally keep out of a public post. She chose to post it as it stood. Changing it would have meant changing the readme in the same turn, since the two must match.

## The zip was checked before it was attached, and that check found something

Today's build of [zip-entries-use-backslash-separators] added a step to the release ritual: list a zip's entries and confirm none uses backslashes or names `__pycache__`. Run against this build's archived zip, and then against both others on disk:

```
throughliner-v1.21.1-test1.zip   38 entries, 0 backslash, 0 __pycache__
throughliner-v1.21.1-test2.zip   41 entries, 0 backslash, 0 __pycache__
plugin/throughliner.zip          35 entries, 0 backslash, 0 __pycache__
```

All conformant. **That contradicts the finding those builds were made from**, which is filed as [zip-backslash-finding-does-not-reproduce] rather than resolved here. It made this step safer rather than blocking it.

## Step 2 — posted

```
py resources/discord_post.py send --channel test-rezips-for-nerds \
   --body <draft> --attach-archived-zip 1.21.1-test1 --prune-to 15 \
   --rebump-welcome resources/nerds-welcome.md
```

On the user's explicit yes to the exact text shown above. Message id `1543588473271877744`, authored by "Throughliner Project", with `throughliner-v1.21.1-test1.zip` attached at 291,416 bytes. Read back from the channel afterwards and compared against the draft: **identical apart from the trailing newline, which Discord strips.** The prune removed nothing — the channel holds three entries, far short of fifteen.

## The welcome re-bump had a side effect nobody had met before

`--rebump-welcome` deletes the bot's previous copy of the welcome and reposts it, so the welcome always sits newest. It reported `no previous copy found` and posted a fresh one as `1543588493400350823`.

**The reason is that the existing welcome is the user's own post, and a bot cannot delete a user's message.** So the flag did half its job: the newest message is now a bot-authored welcome, and the user's original from 2026-08-26 is still sitting above the entry. The channel currently shows the welcome twice.

This is the same authorship constraint that [howto-posts-bot-authorship] exists for, met by accident in a channel nobody had thought about. Filed as [rebump-welcome-cannot-replace-a-user-post].

## Step 3 — register line written

In `INBOX/sent.md`, in the same turn as the approval, with the claim read off the text as posted.

## Step 4 — NOT done, and it is the user's

Posting this entry unlocks editing the previous one — the v1.21.0 post of 2026-08-26 — to add a testing-outcomes summary and a usability rating out of 5. That post is the user's own, so under the first-iteration note the backfill is hers to paste once. Nothing has been drafted for it here.
