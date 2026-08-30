# [HASH] — plan — the pytest-cache finding disproven twice by inspection and deleted

Both halves fell to reading the actual folder: its files date from 25 May 2026 — a week before this repository's rebuild — and name a pre-rebuild layout, so nothing here ever ran pytest and no habit exists to hunt; and pytest writes its own ignore file inside the cache, which git honours (confirmed with `git check-ignore`), so the claimed one-blanket-add exposure never existed. The folder is removed as a fossil by the cleanup build, with no `.gitignore` entry needed. A finding disproven by inspection closes by recording the inspection, which this entry is.

**Queue changes:** [pytest-cache-at-the-root] deleted; the fossil's removal folded into [repo-cleanup-product-forward].
**Work processed:** deleted — [pytest-cache-at-the-root].
