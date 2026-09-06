# Is SPEC used as a source of truth, or maintained dead weight? Sixteen consumer transcripts scored

Audit run 2026-09-06 inside the build run, from [spec-usage-versus-maintenance-audit], processed the same day on the user's question. Two consumer projects, this project excluded on the user's reasoning that building the method here supplies too much context prompting a SPEC read.

## Selection

From each project's transcript folder under the Claude projects directory, the four most recent build sessions and the four most recent planning sessions by file modification time, a session's kind read from which skill its transcript invoked (`<command-name>` blocks: `next` → build, `plan` → plan). Hexboard: 28 transcripts, 8 builds and 10 plans found, 4 and 4 taken. Taskflowapp: 18 transcripts, 5 builds and 9 plans found, 4 and 4 taken. Sixteen sessions.

## Method

A script in the session scratchpad (`spec_events.py`) stripped each `.jsonl` to its SPEC events — every tool call whose path or command names `SPEC.md`, and every thinking block or assistant reply naming SPEC, with 300 characters either side — per this project's transcript-reading rule (the raw file is the evidence; preprocess, then read the slim file). Each session's SPEC reads were then scored by hand on the agreed scale: **0** opened and never referred to again; **1** referred to in reasoning but nothing decided on it; **2** a decision, halt or edit that cites a SPEC sentence. A session is scored at its highest read.

**Stated limit, as the item required.** Extended thinking was on in every one of the sixteen sessions (49 to 171 thinking blocks each), so no session scores from tool calls and replies alone. But thinking blocks named SPEC in only two places across all sixteen sessions (both in Hexboard plan 981017f8). Reasoning that draws on SPEC shows up in the replies — "SPEC requires exports to carry the completion date, adding it" — not in the thinking, so the scoring below reads replies as the reasoning channel and the thinking-block column is present but nearly empty of signal.

## Per-session table

| Project | Kind | Session | Date | SPEC tool calls | Thinking hits | Reply hits | Score | SPEC edited | Thinking present |
|---|---|---|---|---|---|---|---|---|---|
| Hexboard | build | 340d0d6b | 2026-09-02 | 1 | 0 | 0 | 0 | no | yes |
| Hexboard | build | 800b82ed | 2026-09-02 | 1 | 0 | 5 | 1 | no | yes |
| Hexboard | build | 9422f77e | 2026-09-04 | 2 | 0 | 3 | 2 | no | yes |
| Hexboard | build | 8cc818e9 | 2026-09-05 | 2 | 0 | 2 | 2 | no | yes |
| Hexboard | plan | 981017f8 | 2026-09-02 | 10 | 2 | 17 | 2 | yes | yes |
| Hexboard | plan | 2cdc3206 | 2026-09-02 | 8 | 0 | 22 | 2 | yes | yes |
| Hexboard | plan | c53bb8d6 | 2026-09-03 | 6 | 0 | 17 | 2 | yes | yes |
| Hexboard | plan | 74595ae3 | 2026-09-04 | 17 | 0 | 31 | 2 | yes | yes |
| Taskflowapp | build | fec9a248 | 2026-08-31 | 12 | 0 | 15 | 2 | yes | yes |
| Taskflowapp | build | 91c12720 | 2026-09-04 | 1 | 0 | 0 | 0 | no | yes |
| Taskflowapp | build | 6008c631 | 2026-09-05 | 2 | 0 | 1 | 0 | no | yes |
| Taskflowapp | build | ace4cfb7 | 2026-09-05 | 2 | 0 | 0 | 0 | no | yes |
| Taskflowapp | plan | 4a159824 | 2026-09-02 | 3 | 0 | 6 | 2 | yes | yes |
| Taskflowapp | plan | 310a86d0 | 2026-09-03 | 17 | 0 | 30 | 2 | yes | yes |
| Taskflowapp | plan | 46f614bf | 2026-09-05 | 2 | 0 | 2 | 2 | no | yes |
| Taskflowapp | plan | 431e4d78 | 2026-09-05 | 4 | 0 | 9 | 2 | yes | yes |

## The two ratios, per project

Usage is the share of sessions scoring 2; maintenance is the share of sessions that edited SPEC.

| Project | Builds scoring 2 | Builds editing SPEC | Plans scoring 2 | Plans editing SPEC |
|---|---|---|---|---|
| Hexboard | 2 of 4 | 0 of 4 | 4 of 4 | 4 of 4 |
| Taskflowapp | 1 of 4 | 1 of 4 | 4 of 4 | 3 of 4 |

Read together: every planning session in the sample decided something on a SPEC sentence, and seven of eight also edited SPEC — planning both uses and maintains it, in the same sessions. Builds split: three of eight decided or filed on a SPEC sentence, one referred to it, four opened it at run start and never touched it again. No build edited SPEC except the one whose item listed SPEC.md as a file.

## What scored 2 — the passages, quoted

Builds:
- Hexboard 9422f77e: "Building the emoji panels turned up something SPEC doesn't cover, so I've filed it rather than writing SPEC myself: the five panels hold 250 emoji and Unicode's list has 3,781 ... SPEC promises 'content taken from the Unicode standard's own publ[ished list]'" — a build halting on a SPEC sentence and filing, the shipped rule performed.
- Hexboard 8cc818e9: "Ten proper nouns leaked into the ordinary-words category ... Place names, in the list SPEC says carries none" — a defect found against a SPEC sentence during the build.
- Taskflowapp fec9a248: "SPEC requires exports to carry the completion date, and the task table has no such column — adding it"; "Keeps dragging the task itself, which is what SPEC describes"; "it's a SPEC edit rather than a code tweak, because SPEC quotes that exact string in two places" — three decisions each citing a sentence.

Planning (one per session, the sample has dozens):
- Hexboard 981017f8: "The overflow rule is written into SPEC to bind every language, so this is product truth, not a Russian detail."
- Hexboard 2cdc3206: "SPEC promises five emoji panels reached by a downward swipe, and nothing implements them ... SPEC's two sentences about emoji can't both stand as written."
- Hexboard c53bb8d6: "SPEC's predictive-text principle carries three bounding rules, and the first is 'a word already in the dictionary is never corrected.' 'its' is a real word, so the engine as designed would never touch it."
- Hexboard 74595ae3: "SPEC says a language's layout 'is confirmed by someone who reads the language before it ships'. Right now the Russian co[nfig] ..." — leading to the sentence's removal and a held item losing its purpose.
- Taskflowapp 4a159824: "SPEC says nothing about colour anywhere, so whichever way it goes it owes SPEC a sentence."
- Taskflowapp 310a86d0: "SPEC gains the sentence, since back behaviour is product truth and SPEC currently says nothing about it"; later "So I was wrong to call SPEC ambiguous. SPEC has said Strategy is the spine's right end twice, consistently. The divergence is a build-time [choice]."
- Taskflowapp 46f614bf: "a comment from the original build reserves the top-right for the drag-to-delete target that SPEC §Drag-target icons puts in the upper-right corner. That reservation is why 'just put Share in the header' isn't [the answer]."
- Taskflowapp 431e4d78: "SPEC contradicts itself in one word. §Settings lists ... AI tier. §Side menu says the drawer's pinned bottom section carries ... 'Turn on AI'" — corrected at the decision step.

## What the sample says about the user's own hypothesis

The user's view at processing was that SPEC's one redeeming feature may be carrying long-term direction no queue item yet holds. The sample shows that role at work: Hexboard's SPEC held predictive text "until after the first working keyboard", and that deferral gated three queue items across two planning sessions until the condition was met and the sentence rewritten (74595ae3). It also shows the cost of that role: the same session found "twice today a SPEC sentence has turned out to rest on something we'd since removed", corrected to one genuine miss — the predictive-text deferral, whose condition was met by the 2026-09-02 install and whose sentence stood until 2026-09-04.

## Frame assessment

- **TIME RANGE** — the sample is the most recent week of two live projects (2026-08-31 to 2026-09-05), which is the period the shipped read-SPEC-at-build-time rule has been in force; nothing earlier was sampled, so it says nothing about SPEC use before builds read it.
- **PEOPLE** — one user, both projects hers; the sessions are Claude's, so this measures Claude's use of SPEC under the method, not a population of no-code developers.
- **FRESHNESS** — transcripts are fixed artifacts; the finding does not age, but the method's SPEC rules changed within the sampled week (the build-files-rather-than-writes rule), so a later sample would measure a different method.
- **RISK IF WRONG** — a wrong "dead weight" verdict would remove the document every planning session in the sample decided against; a wrong "source of truth" verdict keeps a document four of eight builds only opened. Neither warrants a red flag; the numbers are small (sixteen sessions) and the scoring is one reader's.
- **ALTERNATIVES** — reading every transcript (45, about 140MB) was the user's call to refuse; scoring by thinking blocks was the item's proposal and turned out not to be the channel (two hits in sixteen sessions); scoring replies was the substitute, stated above rather than silently adopted.
