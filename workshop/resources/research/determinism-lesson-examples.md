# Example bank for the determinism lesson video

Compiled 2026-08-29 during the planning session that processed
[determinism-lesson-video], at the user's direction. From Claude's own
knowledge, not a web search — offered and available to widen it. The video's
frame these serve: helping people identify how to ask and what to ask for —
more tools, or more AI — because the big waste is spending AI on work that
does not need it.

## The quadrant map

```
                     looks like AI            looks like a tool
deterministic        THE SURPRISES            everyday tools
probabilistic        AI's real home           THE OTHER SURPRISES
```

The lesson's work happens in the two surprise cells.

## Surprisingly deterministic — "it's magic, but it's a tool"

- **OCR** — the user's own example. Reads an image into text with no chatbot
  anywhere. Tesseract is free, local and repeatable: same scan in, same text
  out, every time. **The teaching nuance, worth keeping:** modern OCR engines
  have neural networks inside — "has ML in it" is not the test. The test is
  whether the output is fixed given the input and a tool exists to produce it.
- **Barcode and QR reading** — looks like vision, is a decoder.
- **EXIF metadata** — "when and where was this photo taken" sounds like a
  question for AI and is a field lookup (exiftool).
- **Document diffing** — "what changed between these two versions" feels like
  reading comprehension; `diff` answers it perfectly and identically forever.
- **Checksums / duplicate-finding** — "are these two files really the same" by
  hash, not by judgment.
- **Date and timezone arithmetic** — "what's 90 days before the hearing"
  has exactly one answer.
- **Unit conversion, sorting, counting, deduplication, regex extraction** —
  every email address in a folder is a pattern match, not a reading task.
- **Audio/video/image conversion** — ffmpeg and ImageMagick territory;
  resize, transcode, extract audio, merge PDFs.
- **Spell and grammar checking (rule-based)** — LanguageTool's core is rules;
  same text, same flags.

## Probabilistic but not AI — "randomness was always here"

Mostly GOOD practice: the randomness is the point.

- **Shuffle play** — random on purpose; a deterministic shuffle would be a
  playlist.
- **Dice, lotteries, card shuffling in games** — fairness IS the randomness.
- **Random sampling in surveys and audits** — sampling deterministically
  (say, every 10th) invites bias and gaming; random is the honest version.
- **A/B test assignment** — who sees which version must be random or the
  result is worthless.
- **Cryptographic key generation** — the unpredictability is the security;
  a predictable key is a broken one.
- **Fuzz testing** — feeding software random junk to find crashes; random
  reaches cases nobody would think to write.
- **Monte Carlo simulation** — rolling random numbers thousands of times to
  estimate what can't be computed directly (project risk, retirement odds).

## Deterministic work done WITH AI — mostly BAD practice, the money cell

Each costs tokens, runs slower, and can answer differently each time —
paying probabilistic prices for deterministic work.

- **Asking AI to add numbers or count words** — a calculator's job, done
  worse.
- **Alphabetising or sorting a list** — one command, zero variance.
- **Converting JSON to CSV, or reformatting data** — a script's job; AI can
  silently drop or invent a row.
- **Transcribing a screenshot again and again** — OCR once instead; AI may
  transcribe it slightly differently each run.
- **Extracting all phone numbers from a document** — regex, not reading.
- **THE BRIDGE, and the lesson's best good-practice example:** have the AI
  *build* the deterministic tool once — write the script, the regex, the
  ffmpeg command — then run the tool forever, free. AI's judgment is spent
  where it pays: once, on making the tool, not on every run.

## AI where it belongs — for the closing contrast

Drafting prose, summarising with judgment, naming things, weighing
trade-offs, rewriting tone: no tool imaginable produces the answer, which is
the user's own heuristic firing in reverse.

## Claims a script should re-verify before recording

That Tesseract is free/local/deterministic, and that LanguageTool's core is
rule-based — both stable, both worth a thirty-second check at drafting rather
than trusted from this file.
