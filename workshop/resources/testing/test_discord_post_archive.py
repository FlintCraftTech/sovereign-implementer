#!/usr/bin/env python3
"""Regression tests for discord_post.py's archived-zip lookup.

Host-only dev artifact — not shipped in the plugin package.

Run:  py workshop/resources/testing/test_discord_post_archive.py
(Plain script, never pytest — see CLAUDE.md's scripting constraints.)

[discord-post-archive-path-flat-only]: the posting script's
--attach-archived-zip looked only at the flat `plugin/rezip-archive/`, and
in the nested layout the archive sits under the inner repository, so the
first rezip from that layout was refused. The lookup now tries the inner
first and the flat path second, and the refusal names both. No token and no
network: the function is imported and called against temporary fixtures.
"""

import importlib.util
import os
import shutil
import sys
import tempfile

for _stream in (sys.stderr, sys.stdout):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError, OSError):
        pass

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SCRIPT = os.path.join(ROOT, "workshop", "resources", "discord_post.py")

spec = importlib.util.spec_from_file_location("discord_post", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

failures = []


def check(label, ok, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + label + ("" if ok else f" — {detail}"))
    if not ok:
        failures.append(label)


def archive_with_zip(folder, version):
    os.makedirs(folder)
    path = os.path.join(folder, "throughliner-v%s.zip" % version)
    with open(path, "wb") as f:
        f.write(b"PK\x03\x04 fixture")
    return path


def nested_project(visibility_line=True):
    d = tempfile.mkdtemp(prefix="dp-archive-nested-")
    inner = os.path.join(d, "product")
    os.makedirs(os.path.join(inner, ".git"))
    if visibility_line:
        with open(os.path.join(d, "CLAUDE.md"), "w", encoding="utf-8") as f:
            f.write("# CLAUDE.md\n\nVisibility: nested — the inner repository "
                    "(`product/`) holds the product.\n")
    return d, inner


# 1. Nested: the inner's archive is found.
d, inner = nested_project()
expected = archive_with_zip(os.path.join(inner, "plugin", "rezip-archive"),
                            "1.22.0-test2")
got = mod.archived_plugin_zip(d, "1.22.0-test2")
check("nested project returns the inner's zip",
      os.path.normcase(got) == os.path.normcase(expected), got)
got = mod.archived_plugin_zip(d)
check("nested project with no version returns the newest inner zip",
      os.path.normcase(got) == os.path.normcase(expected), got)
shutil.rmtree(d, ignore_errors=True)

# 2. Flat: the flat archive is found, unchanged behaviour.
d = tempfile.mkdtemp(prefix="dp-archive-flat-")
expected = archive_with_zip(os.path.join(d, "plugin", "rezip-archive"),
                            "1.21.0-test1")
got = mod.archived_plugin_zip(d, "1.21.0-test1")
check("flat project returns the flat zip",
      os.path.normcase(got) == os.path.normcase(expected), got)
shutil.rmtree(d, ignore_errors=True)

# 3. Nested with no Visibility line but one child holding .git: still found.
d, inner = nested_project(visibility_line=False)
expected = archive_with_zip(os.path.join(inner, "plugin", "rezip-archive"),
                            "1.22.0-test2")
got = mod.archived_plugin_zip(d, "1.22.0-test2")
check("one child holding .git and no Visibility line still resolves",
      os.path.normcase(got) == os.path.normcase(expected), got)
shutil.rmtree(d, ignore_errors=True)

# 4. Ambiguous nested folder — two children holding .git, no Visibility line,
# no flat archive: refused, naming the flat path tried (the inner is unknown).
d, inner = nested_project(visibility_line=False)
os.makedirs(os.path.join(d, "other", ".git"))
try:
    mod.archived_plugin_zip(d)
    check("ambiguous nested folder with no archive is refused", False,
          "no error raised")
except mod.DiscordError as e:
    msg = str(e)
    check("ambiguous nested folder with no archive is refused",
          "No rezip archive at" in msg
          and os.path.join(d, "plugin", "rezip-archive") in msg, msg)
shutil.rmtree(d, ignore_errors=True)

# 5. Nested, archive missing in both places: the refusal names both paths.
d, inner = nested_project()
try:
    mod.archived_plugin_zip(d)
    check("missing archive in a nested project is refused", False,
          "no error raised")
except mod.DiscordError as e:
    msg = str(e)
    check("the refusal names both paths tried",
          os.path.join(inner, "plugin", "rezip-archive") in msg
          and os.path.join(d, "plugin", "rezip-archive") in msg
          and " or " in msg, msg)
shutil.rmtree(d, ignore_errors=True)

print(f"\n{len(failures)} failure(s)" if failures else "\nall passed")
sys.exit(1 if failures else 0)
