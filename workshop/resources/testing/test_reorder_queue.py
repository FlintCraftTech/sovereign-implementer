#!/usr/bin/env python3
"""Regression tests for plugin/throughliner/scripts/reorder_queue.py.

Host-only dev artifact — not shipped in the plugin package.

Run:  python resources/testing/test_reorder_queue.py

No test framework required, deliberately: this project has no test runner and
adding one to guard a single script would cost more than it protects. Each test
writes a small QUEUE.md into a temp dir, runs the mover as a subprocess exactly
the way /plan drives it, and asserts on the resulting file.

The headline case is `marker above all items`. That shape made the mover refuse
EVERY reorder of Processed — not just the greenlighting move — because the
marker scan started at the first `####` item and so never matched a marker
sitting above them all. The defect is a scan-range off-by-one, which is easy to
reintroduce, so it gets a permanent case here.
"""

import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT = os.path.join(ROOT, "plugin", "throughliner", "scripts", "reorder_queue.py")

MARKER = "--- Cleared to run above this line ---"

_failures = []


def build_queue(processed_body, unprocessed_body="#### Later thing [later]\nSome rationale.\n"):
    return (
        "# QUEUE\n\n"
        "Intro prose that must survive untouched.\n\n"
        "## Processed\n\n"
        + processed_body
        + "\n## Unprocessed\n\n"
        + unprocessed_body
    )


def run(text, *args):
    """Write `text` to a temp QUEUE.md, run the mover, return (rc, stderr, new_text)."""
    d = tempfile.mkdtemp(prefix="reorder-test-")
    path = os.path.join(d, "QUEUE.md")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    proc = subprocess.run(
        [sys.executable, SCRIPT, path] + list(args),
        capture_output=True, text=True,
    )
    with open(path, "r", encoding="utf-8", newline="") as f:
        return proc.returncode, proc.stderr, f.read()


def check(name, condition, detail=""):
    if condition:
        print("  ok   " + name)
    else:
        print("  FAIL " + name + ("\n       " + detail if detail else ""))
        _failures.append(name)


def order_of(text, section="## Processed"):
    """Slugs, in file order, within a section — plus MARKER where it sits."""
    out = []
    inside = False
    for line in text.splitlines():
        if line.startswith("## "):
            inside = line.strip() == section
            continue
        if not inside:
            continue
        if line.strip() == MARKER:
            out.append(MARKER)
        elif line.startswith("#### "):
            out.append(line.rstrip().rsplit("[", 1)[1].rstrip("]"))
    return out


# --- --replace-in ([pointer-drift-unfixable-at-a-build-close]) ---------------

REPLACE_QUEUE = (
    "#### First thing [first]\n"
    "Rationale naming resources/research/old-name.md once.\n\n"
    "#### Second thing [second]\n"
    "Rationale also naming resources/research/old-name.md — a different entry.\n"
)


def test_replace_in_fires():
    rc, err, out = run(build_queue(REPLACE_QUEUE),
                       "--replace-in", "first",
                       "--old", "resources/research/old-name.md",
                       "--new", "resources/research/new-name.md")
    check("replace-in succeeds", rc == 0, err)
    check("target entry updated",
          "Rationale naming resources/research/new-name.md once." in out, out)
    check("other entry untouched",
          "Rationale also naming resources/research/old-name.md" in out, out)
    check("replacement reported", "replaced in [first]" in err, err)


def test_replace_in_refuses_non_unique():
    text = build_queue(
        "#### First thing [first]\n"
        "Names old-name.md twice: old-name.md again.\n"
    )
    rc, err, out = run(text, "--replace-in", "first",
                       "--old", "old-name.md", "--new", "new-name.md")
    check("non-unique refuses", rc != 0, err)
    check("non-unique changes nothing", "old-name.md twice: old-name.md" in out)


def test_replace_in_refuses_absent_match():
    rc, err, out = run(build_queue(REPLACE_QUEUE),
                       "--replace-in", "first",
                       "--old", "not-in-the-entry.md", "--new", "x.md")
    check("absent match refuses", rc != 0, err)
    check("absent match changes nothing",
          "resources/research/old-name.md once." in out)


def test_replace_in_refuses_unknown_slug():
    rc, err, out = run(build_queue(REPLACE_QUEUE),
                       "--replace-in", "no-such-slug",
                       "--old", "a", "--new", "b")
    check("unknown slug refuses", rc != 0, err)


def test_replace_in_reaches_unprocessed():
    rc, err, out = run(build_queue(REPLACE_QUEUE),
                       "--replace-in", "later",
                       "--old", "Some rationale.", "--new", "Fresh rationale.")
    check("unprocessed entry reachable", rc == 0, err)
    check("unprocessed entry updated", "Fresh rationale." in out, out)


# --- the regression case ------------------------------------------------------

def test_marker_above_all_items():
    """Marker sitting above every item must not block a plain reorder."""
    body = (
        MARKER + "\n\n"
        "#### First item [alpha]\nRationale for alpha.\n\n"
        "#### Second item [beta]\nRationale for beta.\n"
    )
    rc, err, new = run(build_queue(body), "Processed", "beta", "alpha")
    check("marker-above-all: exits 0", rc == 0, err)
    check("marker-above-all: no self-check failure", "self-check failed" not in err, err)
    check("marker-above-all: no bogus 'no marker' warning",
          "section has no marker" not in err, err)
    check("marker-above-all: items swapped, marker still at top",
          order_of(new) == [MARKER, "beta", "alpha"], repr(order_of(new)))
    check("marker-above-all: marker appears exactly once",
          new.count(MARKER) == 1, str(new.count(MARKER)))
    check("marker-above-all: block text preserved byte-for-byte",
          "#### First item [alpha]\nRationale for alpha." in new
          and "#### Second item [beta]\nRationale for beta." in new)
    check("marker-above-all: other section untouched", "#### Later thing [later]" in new)


def test_marker_above_all_explicit_placement():
    """With the marker above all items, --marker-after must still be honoured."""
    body = (
        MARKER + "\n\n"
        "#### First item [alpha]\nRationale for alpha.\n\n"
        "#### Second item [beta]\nRationale for beta.\n"
    )
    rc, err, new = run(build_queue(body), "Processed", "alpha", "beta",
                       "--marker-after", "alpha")
    check("marker-above-all + --marker-after: exits 0", rc == 0, err)
    check("marker-above-all + --marker-after: marker moved below alpha",
          order_of(new) == ["alpha", MARKER, "beta"], repr(order_of(new)))


def test_marker_above_all_move_mode():
    """--move mode hits the same split_blocks path and must work too."""
    body = (
        MARKER + "\n\n"
        "#### First item [alpha]\nRationale for alpha.\n\n"
        "#### Second item [beta]\nRationale for beta.\n"
    )
    rc, err, new = run(build_queue(body), "Processed", "--move", "beta", "TOP")
    check("marker-above-all + --move: exits 0", rc == 0, err)
    check("marker-above-all + --move: beta on top, marker still at top",
          order_of(new) == [MARKER, "beta", "alpha"], repr(order_of(new)))


# --- the shapes that already worked, kept so the fix doesn't break them --------

def test_marker_between_items():
    body = (
        "#### First item [alpha]\nRationale for alpha.\n\n"
        + MARKER + "\n\n"
        "#### Second item [beta]\nRationale for beta.\n"
    )
    rc, err, new = run(build_queue(body), "Processed", "alpha", "beta")
    check("marker-between: exits 0", rc == 0, err)
    check("marker-between: marker keeps its relative spot",
          order_of(new) == ["alpha", MARKER, "beta"], repr(order_of(new)))


def test_marker_below_all_items():
    body = (
        "#### First item [alpha]\nRationale for alpha.\n\n"
        "#### Second item [beta]\nRationale for beta.\n\n"
        + MARKER + "\n"
    )
    rc, err, new = run(build_queue(body), "Processed", "beta", "alpha")
    check("marker-below-all: exits 0", rc == 0, err)
    # Documented behaviour with no --marker-after: the marker keeps its RELATIVE
    # spot — immediately after whichever slug it currently follows (beta), which
    # after this swap is no longer the bottom.
    check("marker-below-all: marker follows the slug it followed before",
          order_of(new) == ["beta", MARKER, "alpha"], repr(order_of(new)))
    rc, err, new = run(build_queue(body), "Processed", "beta", "alpha",
                       "--marker-after", "BOTTOM")
    check("marker-below-all + BOTTOM: pinned to the bottom",
          rc == 0 and order_of(new) == ["beta", "alpha", MARKER],
          err + repr(order_of(new)))


def test_section_with_no_marker():
    body = (
        "#### First item [alpha]\nRationale for alpha.\n\n"
        "#### Second item [beta]\nRationale for beta.\n"
    )
    rc, err, new = run(build_queue(body), "Processed", "beta", "alpha")
    check("no-marker: exits 0", rc == 0, err)
    check("no-marker: no marker invented", MARKER not in new)
    check("no-marker: reordered", order_of(new) == ["beta", "alpha"], repr(order_of(new)))


def test_no_marker_with_marker_after_warns():
    body = (
        "#### First item [alpha]\nRationale for alpha.\n\n"
        "#### Second item [beta]\nRationale for beta.\n"
    )
    rc, err, new = run(build_queue(body), "Processed", "beta", "alpha",
                       "--marker-after", "alpha")
    check("no-marker + --marker-after: still succeeds", rc == 0, err)
    check("no-marker + --marker-after: warns and ignores",
          "section has no marker" in err, err)


def test_slug_set_mismatch_refuses():
    body = (
        "#### First item [alpha]\nRationale for alpha.\n\n"
        "#### Second item [beta]\nRationale for beta.\n"
    )
    original = build_queue(body)
    rc, err, new = run(original, "Processed", "beta")
    check("mismatch: exits non-zero", rc != 0, err)
    check("mismatch: file unchanged", new == original)


# --- the delete operation -----------------------------------------------------

def test_delete_clean():
    """A plain delete removes exactly one block and leaves the rest byte-exact."""
    body = (
        "#### First item [alpha]\nRationale for alpha.\n\n"
        "#### Second item [beta]\nRationale for beta.\n\n"
        + MARKER + "\n\n"
        "#### Third item [gamma]\nRationale for gamma.\n"
    )
    rc, err, new = run(build_queue(body), "--delete", "beta", "Processed")
    check("delete-clean: exits 0", rc == 0, err)
    check("delete-clean: item gone", "[beta]" not in new, repr(order_of(new)))
    check("delete-clean: its rationale gone too", "Rationale for beta." not in new)
    check("delete-clean: order otherwise intact",
          order_of(new) == ["alpha", MARKER, "gamma"], repr(order_of(new)))
    check("delete-clean: surviving blocks byte-for-byte",
          "#### First item [alpha]\nRationale for alpha." in new
          and "#### Third item [gamma]\nRationale for gamma." in new)
    check("delete-clean: other section untouched", "#### Later thing [later]" in new)
    check("delete-clean: names the heading it removed",
          "First item" not in err and "Second item [beta]" in err, err)


def test_delete_unknown_slug_refuses():
    """An unresolvable slug changes nothing and exits non-zero."""
    body = "#### First item [alpha]\nRationale for alpha.\n\n" + MARKER + "\n"
    text = build_queue(body)
    rc, err, new = run(text, "--delete", "nosuchthing", "Processed")
    check("delete-unknown: exits non-zero", rc != 0, err)
    check("delete-unknown: file unchanged", new == text)
    check("delete-unknown: says it refuses rather than guessing",
          "refuses rather than guessing" in err, err)


def test_delete_last_item_in_section():
    """Deleting the only item leaves a valid, empty section with its marker."""
    body = "#### Only item [solo]\nRationale for solo.\n\n" + MARKER + "\n"
    rc, err, new = run(build_queue(body), "--delete", "solo", "Processed")
    check("delete-last: exits 0", rc == 0, err)
    check("delete-last: item gone", "[solo]" not in new)
    check("delete-last: marker survives", new.count(MARKER) == 1, str(new.count(MARKER)))
    check("delete-last: intro prose untouched",
          "Intro prose that must survive untouched." in new)


def test_delete_marker_anchor_reanchors():
    """Deleting the item the marker sits after must not lose the marker.

    The dangerous case: the marker is anchored to the deleted item, so a naive
    rebuild drops it — and a queue with no marker reads as nothing cleared,
    silently unclearing every item above the line.
    """
    body = (
        "#### First item [alpha]\nRationale for alpha.\n\n"
        "#### Second item [beta]\nRationale for beta.\n\n"
        + MARKER + "\n\n"
        "#### Third item [gamma]\nRationale for gamma.\n"
    )
    rc, err, new = run(build_queue(body), "--delete", "beta", "Processed")
    check("delete-anchor: marker survives", new.count(MARKER) == 1, str(new.count(MARKER)))
    check("delete-anchor: marker keeps its position",
          order_of(new) == ["alpha", MARKER, "gamma"], repr(order_of(new)))


def test_move_marker_anchor_does_not_drag_the_marker():
    """Moving the item the marker sits after must NOT drag the marker with it.

    The observed failure, 2026-08-06: `--move <anchor> AFTER <shelved-item>`
    with no --marker-after given. The marker is stored as an anchor slug rather
    than a position, so it followed its anchor down the section and a
    deliberately-shelved item ended up ABOVE the line — cleared for an
    unattended run nobody had authorised. The script reported only
    "marker placed".

    delete_item() had carried a re-anchor branch since it was written; the
    reorder path (used by --move and the full-slug-list form) did not. The
    discriminator is whether the moved item is the marker's anchor, NOT which
    command name was used — a `--move-section` call can hit it too.
    """
    body = (
        "#### First item [alpha]\nRationale for alpha.\n\n"
        "#### Second item [beta]\nRationale for beta.\n\n"
        + MARKER + "\n\n"
        "#### Third item [gamma]\nDeliberately shelved.\n\n"
        "#### Fourth item [delta]\nRationale for delta.\n"
    )
    rc, err, new = run(build_queue(body),
                       "Processed", "--move", "beta", "AFTER", "gamma")
    check("move-anchor: exits 0", rc == 0, err)
    check("move-anchor: marker survives", new.count(MARKER) == 1,
          str(new.count(MARKER)))
    check("move-anchor: marker holds its position, gamma stays shelved",
          order_of(new) == ["alpha", MARKER, "gamma", "beta", "delta"],
          repr(order_of(new)))
    check("move-anchor: the crossing is reported, not silent",
          "crossed the readiness line" in err and "beta" in err, err)
    check("move-anchor: the message states the marker's real position",
          "above the line" in err, err)


def test_move_non_anchor_leaves_marker_alone():
    """A move that doesn't touch the anchor must leave the marker exactly where
    it was — the negative half, so the re-anchor branch can't over-fire."""
    body = (
        "#### First item [alpha]\nRationale for alpha.\n\n"
        "#### Second item [beta]\nRationale for beta.\n\n"
        + MARKER + "\n\n"
        "#### Third item [gamma]\nRationale for gamma.\n"
    )
    rc, err, new = run(build_queue(body),
                       "Processed", "--move", "gamma", "TOP")
    check("move-nonanchor: exits 0", rc == 0, err)
    check("move-nonanchor: marker still sits after beta",
          order_of(new) == ["gamma", "alpha", "beta", MARKER],
          repr(order_of(new)))


def test_move_explicit_marker_after_still_wins():
    """An explicit --marker-after is the caller asking for the marker to move,
    so the re-anchor branch must not override it."""
    body = (
        "#### First item [alpha]\nRationale for alpha.\n\n"
        "#### Second item [beta]\nRationale for beta.\n\n"
        + MARKER + "\n\n"
        "#### Third item [gamma]\nRationale for gamma.\n"
    )
    rc, err, new = run(build_queue(body), "Processed",
                       "--move", "beta", "BOTTOM", "--marker-after", "alpha")
    check("move-explicit-marker: exits 0", rc == 0, err)
    check("move-explicit-marker: honoured over the re-anchor",
          order_of(new) == ["alpha", MARKER, "gamma", "beta"],
          repr(order_of(new)))


def test_delete_first_item_when_marker_anchored_to_it():
    """Deleting the only item above the marker re-anchors the marker to TOP."""
    body = (
        "#### First item [alpha]\nRationale for alpha.\n\n"
        + MARKER + "\n\n"
        "#### Second item [beta]\nRationale for beta.\n"
    )
    rc, err, new = run(build_queue(body), "--delete", "alpha", "Processed")
    check("delete-first: exits 0", rc == 0, err)
    check("delete-first: marker survives at the top",
          order_of(new) == [MARKER, "beta"], repr(order_of(new)))


def test_delete_block_containing_heading_like_lines():
    """A block whose rationale contains #### text must delete whole and alone."""
    body = (
        "#### First item [alpha]\n"
        "Rationale mentioning a heading shape: '#### Not a real item [fake]'.\n"
        "More rationale.\n\n"
        "#### Second item [beta]\nRationale for beta.\n\n"
        + MARKER + "\n"
    )
    rc, err, new = run(build_queue(body), "--delete", "beta", "Processed")
    check("delete-headinglike: exits 0", rc == 0, err)
    check("delete-headinglike: beta gone", "[beta]" not in new)
    check("delete-headinglike: alpha's heading-shaped prose survives",
          "'#### Not a real item [fake]'" in new)


def test_delete_from_unprocessed():
    """The other section works the same way — /plan's most frequent delete."""
    rc, err, new = run(
        build_queue("#### Kept [alpha]\nRationale.\n\n" + MARKER + "\n"),
        "--delete", "later", "Unprocessed",
    )
    check("delete-unprocessed: exits 0", rc == 0, err)
    check("delete-unprocessed: item gone", "[later]" not in new)
    check("delete-unprocessed: Processed untouched",
          order_of(new) == ["alpha", MARKER], repr(order_of(new)))


def test_move_section_after_last_cleared_reports_below():
    """AFTER the marker's own anchor item lands the block BELOW the marker —
    the observed 2026-08-07 defect. The mover now REPORTS which side the item
    ended on, so the ambiguity is visible at the moment it happens."""
    rc, err, new = run(
        build_queue("#### Kept [alpha]\nRationale.\n\n" + MARKER + "\n"),
        "--move-section", "later", "Unprocessed", "Processed",
        "--position", "AFTER", "alpha",
    )
    check("move-section-after-anchor: exits 0", rc == 0, err)
    check("move-section-after-anchor: lands below the marker",
          order_of(new)[:3] == ["alpha", MARKER, "later"], repr(order_of(new)))
    check("move-section-after-anchor: reports BELOW",
          "BELOW the cleared-to-run marker" in err, err)


def test_move_section_top_reports_above():
    """--position TOP lands above the marker and the mover says so."""
    rc, err, new = run(
        build_queue("#### Kept [alpha]\nRationale.\n\n" + MARKER + "\n"),
        "--move-section", "later", "Unprocessed", "Processed",
        "--position", "TOP",
    )
    check("move-section-top: exits 0", rc == 0, err)
    check("move-section-top: reports ABOVE",
          "ABOVE the cleared-to-run marker" in err, err)


def test_delete_reports_inbound_citations():
    """A delete names the items whose prose still cites the deleted slug.

    Until this printed, those were found by grepping afterwards — one delete
    left five citing items, repaired across three passes, the first incomplete
    because the grep output was truncated.
    """
    text = build_queue(
        "#### The one being deleted [alpha]\nRationale.\n\n"
        "#### A citing item [beta]\nThis builds on [alpha].\n\n"
        + MARKER + "\n"
    )
    rc, err, _ = run(text, "--delete", "alpha", "Processed")
    check("delete with citations: exits 0", rc == 0, err)
    check("delete reports the citing item", "[beta]" in err and "cite" in err, err)
    check(
        "delete does not assert the citation is wrong",
        "often correct as written" in err,
        err,
    )


def test_delete_reports_nothing_when_uncited():
    """The other half — a report that fires on every delete is one people skip."""
    text = build_queue(
        "#### The one being deleted [alpha]\nRationale.\n\n"
        "#### An unrelated item [beta]\nNothing to do with it.\n\n"
        + MARKER + "\n"
    )
    rc, err, _ = run(text, "--delete", "alpha", "Processed")
    check("delete without citations: exits 0", rc == 0, err)
    check("no citation note when nothing cites it", "cite" not in err, err)


def main():
    print("reorder_queue.py regression tests")
    for fn in (
        test_marker_above_all_items,
        test_marker_above_all_explicit_placement,
        test_marker_above_all_move_mode,
        test_marker_between_items,
        test_marker_below_all_items,
        test_section_with_no_marker,
        test_no_marker_with_marker_after_warns,
        test_slug_set_mismatch_refuses,
        test_delete_clean,
        test_delete_unknown_slug_refuses,
        test_delete_last_item_in_section,
        test_delete_marker_anchor_reanchors,
        test_move_marker_anchor_does_not_drag_the_marker,
        test_move_non_anchor_leaves_marker_alone,
        test_move_explicit_marker_after_still_wins,
        test_delete_first_item_when_marker_anchored_to_it,
        test_delete_block_containing_heading_like_lines,
        test_delete_from_unprocessed,
        test_move_section_after_last_cleared_reports_below,
        test_move_section_top_reports_above,
        test_delete_reports_inbound_citations,
        test_delete_reports_nothing_when_uncited,
        test_replace_in_fires,
        test_replace_in_refuses_non_unique,
        test_replace_in_refuses_absent_match,
        test_replace_in_refuses_unknown_slug,
        test_replace_in_reaches_unprocessed,
    ):
        print(fn.__name__)
        fn()
    print()
    if _failures:
        print("%d check(s) FAILED: %s" % (len(_failures), ", ".join(_failures)))
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
