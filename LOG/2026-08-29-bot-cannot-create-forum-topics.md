# [HASH] — plan — the bot cannot create a forum topic, found by trying, and it blocks two items already cleared

Attempting to post the showcase guidelines through the bot failed:

```
POST /channels/<forum id>/messages -> HTTP 400
{"message": "Cannot send messages in a non-text channel", "code": 50008}
```

A forum channel holds threads, not messages. Creating one is a different call carrying a title, and `discord_post.py`'s `send` has no title parameter — which is why the attempt was made rather than the outcome asserted either way. That choice is the item's own lesson applied: the same session had just admitted a rule about not asserting what an outside surface permits.

**It blocks work already cleared.** [ports-forum] cannot post its four topics. The guidelines cannot be bot-authored, so they stay either invisible or owned by the user — the exact unmaintainable shape [howto-posts-bot-authorship] exists to undo. **That item itself is probably unaffected**: re-homing posts into *existing* topics is posting into a thread, a different call again — untested, and deliberately not tested against the live onboarding forum.

**Filed rather than built**, because a planning session may not write `resources/`. The scope-lock refused it, correctly, and this is what the lock is for.

**The user chose to wait rather than post the guidelines herself**, on the ground that a self-posted copy is another stored text the bot cannot maintain, against a few hours of a quiet forum. Her approved text is carried on the item, since the scratchpad clears with the session and no destination for post drafts has been settled yet.

**Queue changes:** [bot-cannot-create-forum-topics] filed and cleared at the top of the region, ahead of the port items it blocks.
**Work processed:** kept — [bot-cannot-create-forum-topics].
