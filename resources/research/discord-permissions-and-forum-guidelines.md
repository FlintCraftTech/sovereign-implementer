# Discord: thread permissions, and whether forum guidelines are visible

Researched 2026-08-29, in a planning session, because both findings changed a
server setting on the spot. Filed because either would otherwise be re-derived
from scratch, and one of them contradicts the documentation.

## Threads can be open while the channel stays locked

**"Send Messages in Threads" is independent of "Send Messages".** Discord's
Threads Moderation FAQ states that the Send Messages permission "will no longer
have any direct effect on Threads behavior anymore". So a member who cannot post
in a channel can still reply inside a thread there, if granted the threads
permission.

**Creating a thread is a third permission** — "Create Public Threads" (or the
private equivalent). Leaving it off while granting "Send Messages in Threads"
produces exactly one conversation: nobody can start new threads, and everyone
replies in the thread that exists.

**Applied the same day** to the Throughliner `#announcements` channel, which is
locked to @everyone: a single **Ports — feedback** thread was created on the
ports announcement, and the post edited to point at it. Before that the post's
closing ask pointed at two routes that were both shut — a forum needing a role,
and a channel nobody may write in.

Sources: <https://support.discord.com/hc/en-us/articles/4404809613847-Threads-Moderation-FAQ>,
<https://support.discord.com/hc/en-us/articles/10543994968087-Channel-Permissions-Settings-101>

## Forum post guidelines: documented behaviour and observed behaviour disagree

**Documented:** guidelines appear while a member composes a post. Discord's own
forum-channels announcement says "While you're crafting a new post, be sure to
check that channel's Post Guidelines", and secondary write-ups describe a panel
shown every time someone clicks **New Post**, plus a panel on the left when
entering the forum.

**Observed, 2026-08-29, by the server owner on her own client:** the guidelines
panel does **not** appear on clicking New Post, and the text is reachable only
through channel settings.

**The disagreement is the finding.** Do not plan on the documented behaviour for
this server. Two candidate explanations were raised and neither was tested: the
left panel collapsing on a narrow window or on mobile, and the guidelines field
having been cleared — a member had accidentally edited it earlier that day, which
means someone held a channel-management permission they should not have.

**What was decided because of it:** the guidelines become a pinned forum post,
bot-authored so they stay editable, with the settings field cut to a pointer.
That is blocked on [bot-cannot-create-forum-topics] — the bot cannot create a
forum topic at all, `POST /channels/<forum>/messages` returning HTTP 400
`code 50008, "Cannot send messages in a non-text channel"`.

Source: <https://discord.com/blog/forum-channels-space-for-organized-conversation>
