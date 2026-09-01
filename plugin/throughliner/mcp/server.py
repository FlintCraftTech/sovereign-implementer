#!/usr/bin/env python3
"""Throughliner state — an MCP server answering four live questions, plus one
structured write.

Slices one and two of the MCP helper. Slice one is the four read-only tools,
which proved the plumbing — a server registered, trusted, connected, its tools
reachable from a session — with no risk that a bug in the plumbing costs a
file. Slice two adds the first write, `file_capture`, which starts where the
writes are most frequent: filing a capture. It refuses only what is checkably
wrong, echoing the reason so the retry is instant, and appends to the bottom
of Unprocessed and nowhere else, so placement cannot go wrong by construction.

**Every tool wraps a calculation or a write path existing code already
performs.** Nothing here invents an answer or a second write mechanism: the
queue counts and the next pick come from `scripts/queue_digest.py`, the cycle
facts and the content stamp from `hooks/session_start.py`, and the capture
append goes through `scripts/reorder_queue.py`'s own append path. That is what
keeps the server's answers and the session opening's answers the same answer
rather than two implementations that drift.

**Registration is project-scoped.** This file travels inside the plugin package
but nothing in the package registers it; the registration is a `.mcp.json` at
the development project's own root, so slice one reaches that project only. To
consumers it is an inert passenger until it is promoted, which is a separate
decision and a separate build.

Standard library only, like every script in this project — it runs on machines
whose interpreters nobody here controls.
"""

import contextlib
import datetime
import importlib.util
import io
import json
import os
import re
import sys
import tempfile

# UTF-8 on both streams, copied from reorder_queue.py, which is the canonical
# copy. The duplication is deliberate: this file may run standalone from a
# copied plugin cache and cannot rely on importing a shared module.
for _stream in (sys.stderr, sys.stdout):
    try:
        _stream.reconfigure(encoding='utf-8', errors='replace')
    except (AttributeError, ValueError, OSError):
        # Python < 3.7, or a stream that cannot be reconfigured (redirected to
        # a pipe or replaced by a test harness). Messages then behave as before
        # — degraded, never fatal.
        pass

PROTOCOL_VERSION = "2024-11-05"
SERVER_NAME = "throughliner-state"
SERVER_VERSION = "0.2.0"

# This file sits at <plugin-root>/mcp/server.py, so the plugin root is its
# grandparent. Derived rather than hardcoded, per the working conventions.
PLUGIN_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def project_root():
    """The project whose state is being reported.

    Taken from the environment or the working directory rather than guessed
    from this file's own location: the plugin package can be installed anywhere,
    and the project it reports on is wherever the session is open.
    """
    return os.path.abspath(
        os.environ.get("THROUGHLINER_PROJECT_ROOT") or os.getcwd())


def _load(name, path):
    """Import a module by path. Returns None where the file is absent."""
    if not os.path.isfile(path):
        return None
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        return None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _digest():
    return _load("throughliner_queue_digest",
                 os.path.join(PLUGIN_ROOT, "scripts", "queue_digest.py"))


def _session_start():
    return _load("throughliner_session_start",
                 os.path.join(PLUGIN_ROOT, "hooks", "session_start.py"))


def _mover():
    return _load("throughliner_reorder_queue",
                 os.path.join(PLUGIN_ROOT, "scripts", "reorder_queue.py"))


def _queue_path(root):
    return os.path.join(root, "QUEUE.md")


# --------------------------------------------------------------------------
# The four tools. Each returns a plain string — what the caller reads.
# --------------------------------------------------------------------------

def tool_queue_checkpoint_counts(_arguments):
    """How much work is ready to build, and how much is left to process."""
    root = project_root()
    digest = _digest()
    if digest is None:
        return "Cannot read the queue: queue_digest.py is not where this " \
               "server expects it (%s)." % PLUGIN_ROOT
    path = _queue_path(root)
    try:
        items = digest.parse(path)
    except OSError as error:
        return "Cannot read %s: %s" % (path, error)

    processed = [i for i in items if i["section"] == "Processed"]
    ready = [i for i in processed if i["cleared"]]
    held = [i for i in processed if not i["cleared"]]
    unprocessed = [i for i in items if i["section"] == "Unprocessed"]

    return "\n".join([
        "Ready to build (Processed, above the cleared-to-run line): %d"
        % len(ready),
        "Held below the line: %d" % len(held),
        "Left to process (Unprocessed): %d" % len(unprocessed),
        "",
        "Counts only. What to do with them is planning work.",
    ])


def tool_queue_next_pick(arguments):
    """Which item the ordering ladder picks next, and why that rung."""
    root = project_root()
    digest = _digest()
    if digest is None:
        return "Cannot read the queue: queue_digest.py is not where this " \
               "server expects it (%s)." % PLUGIN_ROOT
    path = _queue_path(root)
    try:
        items = digest.parse(path)
    except OSError as error:
        return "Cannot read %s: %s" % (path, error)

    skip = arguments.get("skip") or []
    if isinstance(skip, str):
        skip = [s for s in skip.split(",") if s]
    try:
        picked = int(arguments.get("picked") or 0)
    except (TypeError, ValueError):
        picked = 0

    return digest.render_whats_next(items, root, path, skip=skip,
                                    picked=picked)


def tool_cycles_state(_arguments):
    """Each cycle definition's cadence and what its observable currently reads.

    Named for what it returns. The hook reports these facts and the skills
    compute due-ness from them — so this tool stops where the hook stops, and
    turning a cadence and an observable into due-or-not stays the reader's
    step. Reporting a verdict here would put a second due-ness implementation
    in the project, which is the drift the reuse rule exists to prevent.
    """
    root = project_root()
    hooks = _session_start()
    if hooks is None:
        return "Cannot read the cycles doc: session_start.py is not where " \
               "this server expects it (%s)." % PLUGIN_ROOT
    if not os.path.isfile(os.path.join(root, "CYCLES.md")):
        return "No CYCLES.md in this project — nothing is on a cycle, and " \
               "nothing is owed here."

    lines = []
    for slug, description, cadence, observable, last_date in \
            hooks.cycles_facts(root):
        lines.append("[%s] %s" % (slug, description))
        lines.append("  cadence:    %s" % (cadence or "(none stated)"))
        lines.append("  observable: %s" % (observable or "(none stated)"))
        if last_date:
            lines.append("  latest date in that observable: %s" % last_date)
        lines.append("")

    rituals = hooks.rituals_facts(root)
    if rituals:
        lines.append("Rituals (fired by a word, never due):")
        for slug, description, trigger in rituals:
            lines.append("  [%s] %s — %s" % (slug, description, trigger))
        lines.append("")

    lines.append("Facts as the definitions state them. Due-ness is computed "
                 "by the skill reading this, not here.")
    return "\n".join(lines)


def _installed_snapshot():
    """The newest plugin snapshot the CLI has written, or (None, None).

    The CLI copies each installed build into
    `~/.claude/plugins/cache/flintcraft/throughliner/<version>/` and does not
    touch it again, so the newest directory by modification time is the one
    most recently installed. Degrades to nothing found rather than guessing:
    a wrong answer here would be read as evidence that the host is current.
    """
    cache = os.path.join(os.path.expanduser("~"), ".claude", "plugins",
                         "cache", "flintcraft", "throughliner")
    if not os.path.isdir(cache):
        return None, None
    entries = []
    for name in os.listdir(cache):
        full = os.path.join(cache, name)
        if os.path.isdir(full):
            try:
                entries.append((os.path.getmtime(full), name, full))
            except OSError:
                continue
    if not entries:
        return None, None
    entries.sort()
    _when, version, full = entries[-1]
    return version, full


def tool_host_currency(_arguments):
    """Whether the installed host carries the source's current files."""
    root = project_root()
    hooks = _session_start()
    if hooks is None:
        return "Cannot compute a stamp: session_start.py is not where this " \
               "server expects it (%s)." % PLUGIN_ROOT

    source = os.path.join(root, "plugin", "throughliner")
    if not os.path.isdir(source):
        return "No plugin source at %s — this tool answers only in the " \
               "project that develops the plugin." % source

    source_stamp = hooks.content_stamp(source)
    version, installed_dir = _installed_snapshot()
    if installed_dir is None:
        return "Source stamp: %s\nNo installed snapshot found in the plugin " \
               "cache, so there is nothing to compare against." % source_stamp

    installed_stamp = hooks.content_stamp(installed_dir)
    when = hooks.install_date(installed_dir)

    lines = [
        "Installed version: %s%s" % (version,
                                     " (installed %s)" % when if when else ""),
        "Installed stamp:   %s" % installed_stamp,
        "Source stamp:      %s" % source_stamp,
    ]
    if installed_stamp == source_stamp:
        lines.append("Stamps MATCH — the installed host carries the current "
                     "source files, so a host-side change is live.")
    else:
        lines.append("Stamps DIFFER — the host has not been reinstalled since "
                     "the most recent host-side change, so host-side tests "
                     "are not live yet.")
    lines.append("")
    lines.append("The stamp hashes plugin.json with its version key dropped, "
                 "so a -testN suffix or a pure release bump does not move it.")
    return "\n".join(lines)


SLUG_SHAPE = re.compile(r'^[a-z0-9][a-z0-9-]*$')


def tool_file_capture(arguments):
    """File one capture at the bottom of Unprocessed, refusing what is
    checkably wrong.

    The tool composes the canonical entry itself and appends it through
    reorder_queue.py's own append path, so no second write mechanism exists.
    Placement is not a parameter: the bottom of Unprocessed is the only
    destination, which is the Captures placement rule by construction.

    It refuses only what is checkably wrong, echoing the reason so the retry
    is instant. Body prose, length and structure pass untouched — the lint
    stays advisory, and a tool that enforced more of it would turn advice
    into a gate nobody agreed to.
    """
    root = project_root()
    queue = _queue_path(root)
    mover = _mover()
    if mover is None:
        return "Cannot write: reorder_queue.py is not where this server " \
               "expects it (%s)." % PLUGIN_ROOT
    if not os.path.isfile(queue):
        return "Cannot write: no QUEUE.md at %s." % queue

    heading = (arguments.get("heading") or "").strip()
    slug = (arguments.get("slug") or "").strip()
    body = (arguments.get("body") or "").strip()
    blocked_by = arguments.get("blocked_by") or []
    if isinstance(blocked_by, str):
        blocked_by = [s.strip() for s in blocked_by.split(",") if s.strip()]
    blocked_by = [s.strip().strip("[]") for s in blocked_by]
    not_before = (arguments.get("not_before") or "").strip()
    cycle = (arguments.get("cycle") or "").strip().strip("[]")

    problems = []

    if not heading:
        problems.append("heading is missing — the entry's one-line "
                        "description, distinguishing words first.")
    else:
        first_word = heading.split()[0].lower().rstrip(",.:;")
        if first_word in ("a", "an", "the"):
            problems.append(
                "heading leads with %r — the queue is read through an "
                "outline that truncates each heading, so put the "
                "distinguishing words first and drop the leading article."
                % heading.split()[0])

    if not slug:
        problems.append("slug is missing — kebab-case, e.g. "
                        "'lint-cries-wolf-on-prose'.")
    elif not SLUG_SHAPE.match(slug):
        problems.append("slug %r is malformed — lowercase letters, digits "
                        "and hyphens only, starting with a letter or digit."
                        % slug)

    if not body:
        problems.append("body is missing — the rationale prose, in plain "
                        "short sentences.")

    with open(queue, 'r', encoding='utf-8', newline='') as f:
        queue_lines = f.read().splitlines(keepends=True)
    existing = (mover.section_slugs(queue_lines, 'Processed')
                | mover.section_slugs(queue_lines, 'Unprocessed'))

    if slug and slug in existing:
        problems.append("slug %r is already taken by an entry in the queue — "
                        "pick another, or edit the existing entry instead."
                        % slug)

    for b in blocked_by:
        if b not in existing:
            problems.append("blocked_by names [%s], which is not an entry in "
                            "the queue — a blocker must resolve to a real "
                            "entry." % b)

    if not_before:
        try:
            datetime.date.fromisoformat(not_before)
        except ValueError:
            problems.append("not_before %r is not a real date — YYYY-MM-DD."
                            % not_before)

    if cycle:
        hooks = _session_start()
        cycle_slugs = []
        if hooks is not None and os.path.isfile(
                os.path.join(root, "CYCLES.md")):
            cycle_slugs = [row[0] for row in hooks.cycles_facts(root)]
        if cycle not in cycle_slugs:
            problems.append(
                "cycle names [%s], which matches no definition in the "
                "project's cycles doc — a typo at write time is refused even "
                "though a later-deleted cycle correctly releases its "
                "material.%s" % (cycle,
                                 " Definitions on file: %s."
                                 % ", ".join("[%s]" % c for c in cycle_slugs)
                                 if cycle_slugs else
                                 " This project has no cycle definitions."))

    if problems:
        return "Refused — nothing was written:\n" + \
               "\n".join("- " + p for p in problems)

    entry = ["#### %s [%s]\n" % (heading, slug), body.rstrip() + "\n"]
    if blocked_by:
        entry.append("Blocked by: %s\n"
                     % ", ".join("[%s]" % b for b in blocked_by))
    if not_before:
        entry.append("Not before: %s\n" % not_before)
    if cycle:
        entry.append("Cycle: [%s]\n" % cycle)

    # The append goes through the mover's own path. Its refusals call
    # sys.exit via die(), which must not kill the server — so the call runs
    # under a captured stderr and a caught SystemExit, and a refusal comes
    # back as this tool's answer instead.
    tmp = tempfile.NamedTemporaryFile('w', encoding='utf-8', suffix='.md',
                                      delete=False)
    try:
        tmp.write("".join(entry))
        tmp.close()
        captured = io.StringIO()
        try:
            with contextlib.redirect_stderr(captured), \
                    contextlib.redirect_stdout(captured):
                mover.append_item(queue, 'Unprocessed', tmp.name)
        except SystemExit:
            return "Refused by the queue tool — nothing was written:\n" + \
                   captured.getvalue().strip()
    finally:
        try:
            os.unlink(tmp.name)
        except OSError:
            pass

    return "Filed at the bottom of Unprocessed: #### %s [%s]" \
           % (heading, slug)


TOOLS = [
    {
        "name": "queue_checkpoint_counts",
        "description":
            "How many queue items are ready to build, held below the "
            "cleared-to-run line, and still waiting to be processed. Counts "
            "only — never a recommendation about what to do with them.",
        "inputSchema": {"type": "object", "properties": {}},
        "handler": tool_queue_checkpoint_counts,
    },
    {
        "name": "queue_next_pick",
        "description":
            "Which item the ordering ladder picks next, which rung it fell "
            "to, where that item starts in QUEUE.md, and the item's own text. "
            "Optionally takes the slugs set aside this session and how many "
            "picks have already been made, which the ladder's alternating "
            "rung needs.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "skip": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description":
                        "Slugs set aside for this session, which the script "
                        "cannot see for itself.",
                },
                "picked": {
                    "type": "integer",
                    "description":
                        "How many picks have been made this session. The "
                        "fourth rung alternates on this parity.",
                },
            },
        },
        "handler": tool_queue_next_pick,
    },
    {
        "name": "cycles_state",
        "description":
            "Every cycle definition's cadence and what its observable "
            "currently reads, plus any rituals and their firing words. Facts "
            "as written — computing due-ness from them is the reader's step, "
            "exactly as it is at a session opening.",
        "inputSchema": {"type": "object", "properties": {}},
        "handler": tool_cycles_state,
    },
    {
        "name": "host_currency",
        "description":
            "Whether the installed plugin snapshot carries the current source "
            "files: the installed version and stamp, the source stamp, and "
            "whether they match. A match means host-side changes are live.",
        "inputSchema": {"type": "object", "properties": {}},
        "handler": tool_host_currency,
    },
    {
        "name": "file_capture",
        "description":
            "File one capture at the bottom of the queue's Unprocessed "
            "section. Takes a heading, a slug, the body prose, and optional "
            "blocked_by, not_before and cycle fields; composes the canonical "
            "entry and appends it through the queue tool's own append path. "
            "Refuses only what is checkably wrong — a missing, malformed or "
            "taken slug, a blocker resolving to no entry, an unreal date, a "
            "cycle naming no definition, a heading led by A/An/The — echoing "
            "the reason so the retry is instant. Body prose passes untouched.",
        "inputSchema": {
            "type": "object",
            "required": ["heading", "slug", "body"],
            "properties": {
                "heading": {
                    "type": "string",
                    "description":
                        "One-line description, distinguishing words first, "
                        "without the [slug] — the tool appends it.",
                },
                "slug": {
                    "type": "string",
                    "description": "Kebab-case slug, unique in the queue.",
                },
                "body": {
                    "type": "string",
                    "description":
                        "The rationale prose, passed through untouched.",
                },
                "blocked_by": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description":
                        "Slugs of entries this capture waits on. Each must "
                        "resolve to a real entry in the queue.",
                },
                "not_before": {
                    "type": "string",
                    "description":
                        "YYYY-MM-DD — do not offer this capture again "
                        "before the date. Needs the user's approval, per "
                        "the capture rules.",
                },
                "cycle": {
                    "type": "string",
                    "description":
                        "Slug of a cycle definition this capture is "
                        "material for. Must name a definition in the "
                        "project's cycles doc.",
                },
            },
        },
        "handler": tool_file_capture,
    },
]

HANDLERS = {tool["name"]: tool["handler"] for tool in TOOLS}


def _advertised_tools():
    return [{k: v for k, v in tool.items() if k != "handler"}
            for tool in TOOLS]


def handle(message):
    """One request in, one response out — or None for a notification."""
    method = message.get("method")
    request_id = message.get("id")

    # A notification carries no id and is never answered.
    if request_id is None:
        return None

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {}},
                "serverInfo": {"name": SERVER_NAME,
                               "version": SERVER_VERSION},
            },
        }

    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": request_id,
                "result": {"tools": _advertised_tools()}}

    if method == "tools/call":
        params = message.get("params") or {}
        name = params.get("name")
        arguments = params.get("arguments") or {}
        handler = HANDLERS.get(name)
        if handler is None:
            return {"jsonrpc": "2.0", "id": request_id,
                    "error": {"code": -32602,
                              "message": "No such tool: %r" % name}}
        try:
            text = handler(arguments)
        except Exception as error:  # noqa: BLE001 — reported, never raised out
            return {"jsonrpc": "2.0", "id": request_id,
                    "result": {"isError": True,
                               "content": [{"type": "text",
                                            "text": "%s failed: %s"
                                                    % (name, error)}]}}
        return {"jsonrpc": "2.0", "id": request_id,
                "result": {"content": [{"type": "text", "text": text}]}}

    return {"jsonrpc": "2.0", "id": request_id,
            "error": {"code": -32601,
                      "message": "Method not found: %r" % method}}


def main():
    """Read newline-delimited JSON-RPC from stdin, answer on stdout."""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            message = json.loads(line)
        except json.JSONDecodeError:
            # A malformed line has no id to answer against, so it is dropped
            # rather than answered wrongly.
            continue
        response = handle(message)
        if response is not None:
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
