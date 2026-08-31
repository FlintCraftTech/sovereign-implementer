# What LOG/index.md costs to read, measured 2026-08-24

Measured in the planning session that processed [log-retrieve-search-leg], to decide whether a search leg over `LOG/` was worth building — the project bans limits it cannot derive, so "the index is too long" was not a claim anyone could make until this existed.

## The figures

- `LOG/index.md`: **990 index lines** (1,229 file lines), **353,596 characters** — roughly **88,000 tokens** at ~4 characters per token if read in full.
- `LOG/` holds **1,007 records**; the index grows at this project's working pace of roughly ten-plus lines per working day.
- Median index line: **41 words** (shortest 4, longest 83) — per `measure_written_shape_length.py`, same run.

## What it settles

The always-loaded rules instructed that the index "is read in full, by Claude, on every retrieve, so its total length is a fixed toll." At ~88k tokens that is approaching half a working context per lookup. In practice sessions search the index rather than reading it whole (the measuring session itself did; past sessions could not be verified without a transcript audit — an inference from cost, not a checked fact). The measurement converted [log-retrieve-search-leg] into a build: search-first retrieval over the index, split per month, rollover at the close.

The per-line cap ([index-line-length-proportional-cap]) bounds the slope; nothing bounded the total until this. An age threshold for archiving was refused as an underivable bare number; calendar months supply the boundary with no threshold.

## How to re-measure

`wc -l LOG/index.md`, `wc -c LOG/index.md`, and `py <plugin-root>/scripts/measure_written_shape_length.py .` for the index-line distribution.
