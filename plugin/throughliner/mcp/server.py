#!/usr/bin/env python3
"""Throughliner state — a read-only MCP server answering four live questions.

Slice one of the MCP helper. It is deliberately **read-only**: it opens no file
for writing and runs no command that changes anything, so it proves the
plumbing — a server registered, trusted, connected, its tools reachable from a
session — without any risk that a bug in the plumbing costs a file. The writing
slice is designed only once this one has been proven in real sessions.

**Every tool wraps a calculation existing code already performs.** Nothing here
invents an answer: the queue counts and the next pick come from
`scripts/queue_digest.py`, the cycle facts and the content stamp from
`hooks/session_start.py`. That is what keeps the server's answers and the
session opening's answers the same answer rather than two implementations that
drift.

**Registration is project-scoped.** This file travels inside the plugin package
but nothing in the package registers it; the registration is a `.mcp.json` at
the development project's own root, so slice one reaches that project only. To
consumers it is an inert passenger until it is promoted, which is a separate
decision and a separate build.

Standard library only, like every script in this project — it runs on machines
whose interpreters nobody here controls.
"""

import datetime
import importlib.util
import json
import os
import sys

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
SERVER_VERSION = "0.1.0"

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
