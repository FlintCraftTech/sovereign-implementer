# TOOLS.md — facts about this project's environment

Facts that are expensive to re-derive. Any session may append one the moment it
is learned; a build's environment check reads this before assuming a tool or
capability is absent.

## Discord bot (learned live 2026-08-27)

- The bot's token lives at `INBOX/.discord-bot-token.txt` — outside git (proved
  with `git check-ignore`). The leading dot is load-bearing: session_start's
  mail scan skips dot-files (the address book's own convention), so the
  credential is never surfaced as unread mail or read into a session's chat.
  Renamed from the dotless name 2026-08-27 for exactly that reason. It is used as an `Authorization: Bot <token>`
  header against `https://discord.com/api/v10`. Never quote, print or commit
  the token.
- The server is the project's own Discord server.
- Readable channels: **announcements** and **tips** worked with no per-channel
  setup; **test-rezips-for-nerds** returned HTTP 403 "Missing Access" until the
  bot was added to that channel's own permissions (a channel overwrite, not a
  missing scope); **main** returns 403 and stays that way deliberately — it is a Chagora testing channel, not a Throughliner posting target (the user's correction, 2026-08-27).
- **Reading a channel and posting to it are separate grants**, and the bot has
  them unevenly (measured 2026-08-27 by computing effective permissions from
  the guild roles plus each channel's overwrites — not by test-posting, which
  would send real messages). It **can** post to test-rezips-for-nerds,
  general-chat, give-and-get-support, and — since the user's grants of
  2026-08-27, both proven by real sends — **tips and announcements**. The how-to forum was the last gap (HTTP 403 at
  first send attempt); the user granted it 2026-08-28 and the grant was
  confirmed from the API — view, create posts and send in threads all true
  ([bot-needs-howto-send-permission], done). Reading
  a channel works even where posting is refused, which is why a send gap is
  invisible until a send is attempted.
- The bot's **edit path is proven** (2026-08-27): it edited its own v1.21.1
  announcement in #announcements (message 1542476078835175527) to fold in a
  link, on the user's yes, and the edited message read back in place. This was
  the first genuine edit, closing the question [bot-edit-path-unproven] carries.
- Channel IDs are deliberately not recorded here (this file is committed to a
  public repository — the user's decision, 2026-08-27). A session needing one
  looks it up through the bot's API in one call.
- Message Content Intent had to be enabled in the Developer Portal — without
  it, message text comes back as an empty string with no error.
- A bot can only EDIT messages it authored itself. `Manage Messages` allows
  deleting others' messages and pinning — never rewriting them.
- Posting is gated by the standing approval rule: nothing leaves the machine
  without the user seeing the exact text and saying yes.

## Discord server facts (learned live 2026-08-29)

- **The posting role for the showcase forum is `Throughliner expert`, granted by
  DMing the user.** Any walkthrough telling someone to post there has to say so.
- **The showcase forum is for ports of Throughliner AND for projects built with
  it** — the user's own definition, given when the bot could see no messages in
  the channel and could not tell what it was for.
- **The bot's known limits as of 2026-08-29:** it cannot create a forum topic
  outside the flow [bot-cannot-create-forum-topics] built, cannot read roles or
  channel permissions, has no pin command, and cannot delete or edit anyone
  else's messages.

## Desktop app (learned live 2026-08-29 and 2026-08-30)

- **Archiving AND deleting a session both leave its transcript on disk** —
  tested live 2026-08-30, one of each on this project: the `.jsonl` under
  `~/.claude/projects/<project>/` survived both, file count unchanged. So the
  method's transcript-reading evidence is safe either way. The difference is
  in-app: an archived session can be reopened from the Archived list; a
  deleted one is gone from the app. Best practice: archive to shorten a
  project's sidebar list (the workaround for issue #83699); delete only what
  you'd never reopen. Limit: this tested immediate behaviour — a later
  background cleanup was not ruled out.
- **The side panel cannot edit `.claude/settings.local.json`.** The user had to
  open it through File Explorer in Notepad. A walkthrough handing over a
  settings edit names the Notepad route from the start (right-click → Open
  with → Notepad) rather than assuming the sidebar can do it.

## Google Drive connection (learned live 2026-08-29)

- **It reads a Drive-hosted `.pptx` and returns its text.** Proved by reading
  `Throughliner.pptx` (an uploaded PowerPoint, not a native Slides file)
  through `read_file_content` after `get_file_metadata` confirmed the type. The
  next session wanting a deck's contents should not assume it cannot.

## Web endpoints (learned live 2026-08-28)

- **LinkedIn refuses the anonymous web fetcher** — HTTP 999 with no body. The
  route that works is the user's own logged-in Chrome (the Claude-in-Chrome
  tools), used with her direction for her own pages.
- **A raw Discord API call from a script needs a `User-Agent` header**
  (e.g. `DiscordBot (throughliner, 1.0)`) or it is refused with HTTP 403 before
  auth is even considered. `resources/discord_post.py` already sets its own;
  the trap is ad-hoc scripts, where a valid Bot token still 403s without it —
  cost one wrong diagnosis on 2026-08-28.

## Inkscape on this machine (learned live 2026-08-27)

- The CLI is at `C:\Program Files\Inkscape\bin\inkscape.exe`. It exports PNG
  (`--export-type=png`, `--export-area-drawing|page|<x0:y0:x1:y1>`) and fits a
  page to its art with
  `--actions="select-all;fit-canvas-to-selection;export-filename:<same file>;export-overwrite;export-do"`.
- **`--query-all` and `--export-area` report and take PIXELS, while path data in
  a mm-based document is in MILLIMETRES** — factor 3.7795 for a 96dpi document.
  Coordinates read from a query and pasted into a `d` attribute land off-canvas
  with no error; divide by 3.7795 first. This cost one wasted render.

## Python on this machine

- `python` resolves to Inkscape's bundled interpreter (first on PATH); use `py`
  to reach the user's own Python. Recorded in CLAUDE.md's scripting
  constraints; noted here because it is the canonical TOOLS.md-shaped fact.
