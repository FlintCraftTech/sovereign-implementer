#!/usr/bin/env python3
"""Post to, and edit, this project's Discord channels from a session.

Host-only. Consumers of Throughliner have no bot and no server; this lives in
resources/ rather than the plugin's scripts/ folder for that reason.

## What this is for

Before this existed, every Discord post was copied across by hand. The route is
all that changes: nothing posts without the user seeing the exact text and
saying yes, which is the standing approval rule and is enforced by the session,
not by this script. A script cannot ask for consent, so it does not pretend to
— it takes a file that a human has already approved and sends its exact bytes.

## The token

Read from INBOX/.discord-bot-token.txt, which is outside git. The leading dot
is load-bearing: session_start's mail scan skips dot-files, so the credential
is never surfaced as unread mail or read into a session's chat. This script
never prints, echoes or logs the token, and an HTTP error body is passed
through untouched only after the Authorization header has been dropped from
anything reported.

## Standard library only

Per this project's scripting constraints: these scripts run on machines whose
interpreters nobody controls, so nothing is imported that pip would have to
supply. urllib does everything needed here.

## Routes used, verified against Discord's docs 2026-08-27

    POST   /channels/{channel_id}/messages              send
    PATCH  /channels/{channel_id}/messages/{message_id} edit (own messages only)
    DELETE /channels/{channel_id}/messages/{message_id} delete one
    GET    /channels/{channel_id}/messages              list, newest first
    GET    /users/@me/guilds                            find the server
    GET    /guilds/{guild_id}/channels                  resolve a channel name
    PATCH  /users/@me                                   set the bot's avatar

Bulk delete is deliberately NOT used. Its route refuses anything older than two
weeks, and the entries this prunes are older than that by definition, so it
would fail exactly where the prune is needed.
"""

import argparse
import base64
import json
import mimetypes
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid

# Copied from reorder_queue.py, which is the canonical copy. The duplication is
# deliberate: the hooks and these scripts run standalone and cannot import a
# shared module, which is also why a shared module was rejected. Without this,
# an unconfigured stderr on Windows falls back to the console's ANSI code page
# and any character outside it is replaced — and the echo confirming which
# message was posted prints the post's own text back, which routinely carries
# em-dashes.
for _stream in (sys.stderr, sys.stdout):
    try:
        _stream.reconfigure(encoding='utf-8', errors='replace')
    except (AttributeError, ValueError, OSError):
        # Python < 3.7, or a stream that cannot be reconfigured. Messages then
        # behave as before — degraded, never fatal.
        pass

API = "https://discord.com/api/v10"
TOKEN_PATH = os.path.join("INBOX", ".discord-bot-token.txt")

# Discord's own limit on a message body.
MESSAGE_LIMIT = 2000


class DiscordError(Exception):
    """An API call failed. The message is safe to print — no token in it."""


def read_token(project_root):
    path = os.path.join(project_root, TOKEN_PATH)
    if not os.path.exists(path):
        raise DiscordError(
            "No bot token found at %s. It is created by the Discord bot "
            "server setup and is deliberately outside git." % TOKEN_PATH
        )
    with open(path, encoding="utf-8") as handle:
        token = handle.read().strip()
    if not token:
        raise DiscordError("The bot token file at %s is empty." % TOKEN_PATH)
    return token


def request(token, method, path, body=None, multipart=None, query=None):
    """One API call. Returns the decoded JSON body, or None for 204."""
    url = API + path
    if query:
        url += "?" + urllib.parse.urlencode(query)

    headers = {
        "Authorization": "Bot " + token,
        "User-Agent": "ThroughlinerPoster (https://flintcraft.tech, 1.0)",
    }

    data = None
    if multipart is not None:
        boundary = uuid.uuid4().hex
        data = encode_multipart(multipart, boundary)
        headers["Content-Type"] = "multipart/form-data; boundary=" + boundary
    elif body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=data, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 204:
                return None
            raw = response.read()
            return json.loads(raw.decode("utf-8")) if raw else None
    except urllib.error.HTTPError as error:
        detail = ""
        try:
            detail = error.read().decode("utf-8", "replace")
        except Exception:
            pass
        # 429 carries a retry_after; one retry, then give up. A prune that
        # stops partway needs no recovery — the next post's prune picks up
        # whatever is left.
        if error.code == 429:
            try:
                wait = float(json.loads(detail).get("retry_after", 1.0))
            except Exception:
                wait = 1.0
            time.sleep(min(wait, 10.0) + 0.1)
            return request(token, method, path, body=body,
                           multipart=multipart, query=query)
        raise DiscordError(
            "%s %s failed: HTTP %s %s" % (method, path, error.code, detail)
        )
    except urllib.error.URLError as error:
        raise DiscordError("%s %s failed to connect: %s" % (method, path, error.reason))


def encode_multipart(fields, boundary):
    """Build a multipart/form-data body.

    `fields` is a list of (name, value) for text parts and
    (name, filename, bytes) for file parts — Discord wants the JSON body as a
    `payload_json` text part alongside `files[n]` file parts.
    """
    out = bytearray()
    sep = ("--" + boundary + "\r\n").encode("utf-8")
    for field in fields:
        out += sep
        if len(field) == 2:
            name, value = field
            out += ('Content-Disposition: form-data; name="%s"\r\n\r\n'
                    % name).encode("utf-8")
            out += value.encode("utf-8") + b"\r\n"
        else:
            name, filename, payload = field
            guessed = mimetypes.guess_type(filename)[0] or "application/octet-stream"
            out += ('Content-Disposition: form-data; name="%s"; filename="%s"\r\n'
                    % (name, filename)).encode("utf-8")
            out += ("Content-Type: %s\r\n\r\n" % guessed).encode("utf-8")
            out += payload + b"\r\n"
    out += ("--" + boundary + "--\r\n").encode("utf-8")
    return bytes(out)


# --- channel resolution -----------------------------------------------------
#
# Channel IDs are deliberately not kept on file: TOOLS.md is committed to a
# public repository, so a session that needs one looks it up through the bot.

def normalise_channel_name(name):
    """Reduce a channel name to the part a human would type.

    This server's channels are named with a leading emoji — '\N{NERD FACE}test-rezips-for-nerds',
    '\N{NEWSPAPER}announcements' — so an exact match on the typed name finds nothing.
    Keeping only ASCII letters, digits and dashes makes both sides comparable
    without anyone having to paste an emoji into a command line.
    """
    return "".join(
        char for char in name.lower()
        if char.isascii() and (char.isalnum() or char == "-")
    ).strip("-")


def resolve_channel(token, name):
    """Find a channel id by its name, across every guild the bot is in."""
    if name.isdigit():
        return name
    wanted = normalise_channel_name(name.lstrip("#"))
    matches = []
    for guild in request(token, "GET", "/users/@me/guilds") or []:
        channels = request(token, "GET", "/guilds/%s/channels" % guild["id"])
        for channel in channels or []:
            if normalise_channel_name(channel.get("name", "")) == wanted:
                matches.append((channel["name"], channel["id"]))

    if len(matches) == 1:
        return matches[0][1]
    if len(matches) > 1:
        raise DiscordError(
            "More than one channel matches %r: %s. Pass the channel id "
            "instead." % (name, ", ".join(m[0] for m in matches))
        )
    raise DiscordError(
        "No channel named %r found in any server the bot is in. The bot may "
        "not have been granted access to that channel." % name
    )


def whoami(token):
    return request(token, "GET", "/users/@me")


# --- the operations ---------------------------------------------------------

def read_text(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def check_length(text):
    if len(text) > MESSAGE_LIMIT:
        raise DiscordError(
            "The text is %d characters; Discord's limit is %d. Shorten the "
            "draft file and run again." % (len(text), MESSAGE_LIMIT)
        )


def send(token, channel, body_path, attach=None):
    """Post the exact contents of body_path, optionally with one file."""
    channel_id = resolve_channel(token, channel)
    text = read_text(body_path)
    check_length(text)
    path = "/channels/%s/messages" % channel_id

    if attach:
        with open(attach, "rb") as handle:
            payload = handle.read()
        fields = [
            ("payload_json", json.dumps({
                "content": text,
                "attachments": [{"id": 0, "filename": os.path.basename(attach)}],
            })),
            ("files[0]", os.path.basename(attach), payload),
        ]
        message = request(token, "POST", path, multipart=fields)
    else:
        message = request(token, "POST", path, body={"content": text})

    return message


def build_plugin_zip(project_root, out_dir):
    """Zip plugin/throughliner/ as it stands, for a test-rezips entry.

    Built at posting time and never kept locally: the release archive stays
    release-only, Discord holds the download, and the entry's Commit: line is
    what lets any build be rebuilt byte-for-byte from git.
    """
    import zipfile

    source = os.path.join(project_root, "plugin", "throughliner")
    if not os.path.isdir(source):
        raise DiscordError("No plugin folder at %s to zip." % source)

    target = os.path.join(out_dir, "throughliner.zip")
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for folder, _, names in os.walk(source):
            for name in names:
                full = os.path.join(folder, name)
                archive.write(full, os.path.relpath(full, os.path.dirname(source)))
    return target


def edit(token, channel, message_id, body_path):
    """Rewrite one of the bot's own messages.

    A bot can only edit messages it authored — nobody can edit anyone else's
    Discord message — so a post-post correction is always this call.
    """
    channel_id = resolve_channel(token, channel)
    text = read_text(body_path)
    check_length(text)
    return request(
        token, "PATCH",
        "/channels/%s/messages/%s" % (channel_id, message_id),
        body={"content": text},
    )


def fetch(token, channel, limit=50):
    """List recent messages, newest first."""
    channel_id = resolve_channel(token, channel)
    return request(
        token, "GET", "/channels/%s/messages" % channel_id,
        query={"limit": min(int(limit), 100)},
    ) or []


def fetch_all(token, channel_id, cap=300):
    """Page back through a channel's messages, newest first."""
    collected = []
    before = None
    while len(collected) < cap:
        query = {"limit": 100}
        if before:
            query["before"] = before
        batch = request(token, "GET", "/channels/%s/messages" % channel_id,
                        query=query) or []
        if not batch:
            break
        collected.extend(batch)
        before = batch[-1]["id"]
        if len(batch) < 100:
            break
    return collected


def prune(token, channel, keep=15, dry_run=False):
    """Delete the channel's older entries, under four bounds.

    1. Keep the newest `keep` of the bot's own entries.
    2. Delete only messages the BOT ITSELF authored, checked per message
       against the author id. The user's posts, other members' posts and the
       pin are untouchable by construction rather than by ordering luck.
    3. Skip pinned messages explicitly — a second, independent guard on the
       pin, so it survives even if the author check ever changed.
    4. On any error partway, stop and report, with no retries. Leftover old
       entries are picked up by the next post's prune, so nothing needs
       recovering.

    Bulk delete is not used: its route refuses anything older than two weeks,
    which is precisely the age of the entries this removes.

    One cost, stated: entries posted by hand before the bot existed can never
    be pruned by the bot, because it did not author them. Those are cleaned up
    by hand, once.
    """
    channel_id = resolve_channel(token, channel)
    me = whoami(token)["id"]

    messages = fetch_all(token, channel_id)
    mine = [m for m in messages
            if m.get("author", {}).get("id") == me and not m.get("pinned")]

    doomed = mine[keep:]          # the list is newest-first
    if not doomed:
        return 0, len(mine)

    deleted = 0
    for message in doomed:
        if dry_run:
            deleted += 1
            continue
        try:
            request(token, "DELETE",
                    "/channels/%s/messages/%s" % (channel_id, message["id"]))
        except DiscordError as error:
            raise DiscordError(
                "Prune stopped after %d deletion(s): %s\nNothing needs "
                "recovering — the next post's prune picks up what is left."
                % (deleted, error)
            )
        deleted += 1
        # Deletes are rate-limited more tightly than reads; a small pause
        # costs nothing on a prune of a handful of messages and keeps the
        # 429 path from doing the work.
        time.sleep(0.35)

    return deleted, len(mine)


def set_avatar(token, image_path):
    """Set the bot's own avatar. Outward-facing — the caller owns the consent."""
    with open(image_path, "rb") as handle:
        encoded = base64.b64encode(handle.read()).decode("ascii")
    mime = mimetypes.guess_type(image_path)[0] or "image/png"
    return request(token, "PATCH", "/users/@me",
                   body={"avatar": "data:%s;base64,%s" % (mime, encoded)})


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Post to and edit this project's Discord channels.")
    parser.add_argument("--project-root", default=".",
                        help="project root holding INBOX/ (default: .)")
    sub = parser.add_subparsers(dest="command", required=True)

    p_send = sub.add_parser("send", help="post the exact contents of a file")
    p_send.add_argument("--channel", required=True, help="channel name or id")
    p_send.add_argument("--body", required=True,
                        help="path to the approved text (sent verbatim)")
    p_send.add_argument("--attach", help="optional file to attach")
    p_send.add_argument("--attach-plugin-zip", metavar="DIR",
                        help="zip plugin/throughliner/ into DIR (use the "
                             "session scratchpad) and attach it — the "
                             "test-rezips entry's download")
    p_send.add_argument("--prune-to", type=int, metavar="N",
                        help="after posting, keep only the newest N of the "
                             "bot's own unpinned messages in this channel")

    p_edit = sub.add_parser("edit", help="rewrite one of the bot's own messages")
    p_edit.add_argument("--channel", required=True)
    p_edit.add_argument("--message-id", required=True)
    p_edit.add_argument("--body", required=True)

    p_list = sub.add_parser("list", help="list recent messages, newest first")
    p_list.add_argument("--channel", required=True)
    p_list.add_argument("--limit", type=int, default=50)

    p_avatar = sub.add_parser("set-avatar", help="set the bot's own avatar")
    p_avatar.add_argument("--image", required=True)

    p_prune = sub.add_parser(
        "prune", help="delete the bot's own older entries, keeping the newest N")
    p_prune.add_argument("--channel", required=True)
    p_prune.add_argument("--keep", type=int, default=15)
    p_prune.add_argument("--dry-run", action="store_true",
                         help="report what would go, delete nothing")

    sub.add_parser("whoami", help="report the bot's own account")

    args = parser.parse_args(argv)

    try:
        token = read_token(args.project_root)

        if args.command == "send":
            attachment = args.attach
            if args.attach_plugin_zip:
                attachment = build_plugin_zip(args.project_root,
                                              args.attach_plugin_zip)
                print("Built %s (%d KB)"
                      % (attachment, os.path.getsize(attachment) // 1024))
            message = send(token, args.channel, args.body, attachment)
            print("Posted to #%s — message id %s" % (args.channel, message["id"]))
            if args.prune_to is not None:
                removed, remaining = prune(token, args.channel, args.prune_to)
                print("Pruned %d old entr%s; %d of the bot's own remain."
                      % (removed, "y" if removed == 1 else "ies",
                         remaining - removed))

        elif args.command == "edit":
            edit(token, args.channel, args.message_id, args.body)
            print("Edited message %s in #%s" % (args.message_id, args.channel))

        elif args.command == "list":
            for message in fetch(token, args.channel, args.limit):
                first = (message.get("content") or "").splitlines()
                print("%s  %s  %s" % (
                    message["id"],
                    message.get("author", {}).get("username", "?"),
                    first[0][:80] if first else "(no text)",
                ))

        elif args.command == "prune":
            removed, mine = prune(token, args.channel, args.keep, args.dry_run)
            verb = "Would delete" if args.dry_run else "Deleted"
            print("%s %d of the bot's own unpinned message(s) in #%s; "
                  "%d newest kept. Pinned messages and anyone else's posts "
                  "were never candidates."
                  % (verb, removed, args.channel, min(args.keep, mine)))

        elif args.command == "set-avatar":
            set_avatar(token, args.image)
            print("Avatar updated.")

        elif args.command == "whoami":
            me = whoami(token)
            print("%s#%s (id %s)" % (me.get("username"),
                                     me.get("discriminator"), me.get("id")))

    except DiscordError as error:
        sys.stderr.write("%s\n" % error)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
