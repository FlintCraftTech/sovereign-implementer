---
name: rescan
docset: current
note: >
  /rescan procedure. Split out of done.md's wind-down re-scan on 2026-08-15 so
  the step has its own trigger and can run repeatedly in one chat.
  Register: structure in typed blocks, everything else in prose, tags inline.
---

# /rescan procedure

/rescan exists because a conversation ends and takes everything unwritten with
it — filing is how a decision outlives the chat that made it. Look back over
the conversation for things decided, noticed or asked for that
were never written into a file, and file them.

## What it does, and the one thing it does not

**Route what it finds by the standard three-way triage**, rather than filing
everything as a capture:

```
reveals work still to do          ->  a capture in QUEUE.md Unprocessed
what already HAPPENED             ->  appended to THIS chat's LOG entry, as a
    — including work done after       marked tail
    the close
evidence a future chat must       ->  a durable file under resources/
    re-read word for word
```

```
/rescan  ->  FILES what it finds, by that triage
         ->  never ROUTES it (keep / delete / where it sits)
         ->  never BUILDS it
         ->  never COMMITS. The tail rides the next close's commit.
```

**The tail is what makes this the one-word route for post-close work**, which is
common and otherwise has to be asked for in prose every time. Mark it as a tail
rather than blending it in, so what was recorded at the close stays visible as
what the close recorded.

**Committing nothing is what keeps this from being a second close under another
name**, and it is also why nothing has to judge when the tail has ended: the skill
can be run as many times as the tail has parts.

Filing is capture-making and is open to every skill. Routing and building are
/plan's and /next's, and this skill stays on the filing side of that line.

**It does not build, and the reason is worth keeping.** The complaint that
produced this skill is a real one: a finding about the machinery being used right
now waits for a /plan to process it, a /next to build it, and a reinstall before
it is live. Building on the spot would not answer that, because the installed
plugin is a frozen copy — a fix made now does not reach the chat that made it
until the plugin is reinstalled and the app restarted. And a skill that could
route and build would let any chat change the project without the user having
agreed to the work.

## Step 1: Find the stopping point  [SILENT]

Scan back only as far as the last /rescan in this chat, not to the beginning.
That is what lets the skill run several times in one chat without re-surfacing
what it already surfaced.

```
/rescan already ran in this chat  ->  scan back to where it stopped
first /rescan of the chat         ->  scan the whole conversation
can't tell (the conversation      ->  read the captures filed earlier today and
  has been summarised)                use those as the boundary
```

**The stopping point is held in the conversation, and nothing is written to a
file for it.** A durable marker was weighed and refused: it is a new artifact,
and this method deletes the state files it invents. Where the conversation has
been summarised the memory of it is gone — and that is undetectable from the
inside, exactly as a compaction is — so the fallback is the captures already
filed. A stretch that yielded nothing yields nothing again, so the cost of
re-reading it is re-reading, not duplicate items.

## Step 2: File what you find  [BRIEF]

**Sort each candidate by the triage above before writing anything** — work still
to do, or something that already happened. Both get written; they go to different
files.

**Work still to do → Unprocessed** [PROMPT]. Show the candidate set as ONE
numbered message before anything is written, and wait. The user contests by
number or says go, and a contested item is dropped or reworked one at a time.
**What happens then depends on the answer:**

```
answered FILE          ->  the capture is written, exactly as now
answered PROCESS NOW   ->  NOTHING is written. The item enters the planning
                           loop and is written once, as a work item, after
                           the interview — plan.md's process-now rule
```

  Writing a capture first and then processing it spends a write that is thrown
  away, and process-now is the common answer. The offer below is what asks.

Placement is the standing one — appended to the bottom of Unprocessed, no
judgment, no narration of the mechanics.

**Where /plan was invoked earlier in this chat, the same message also offers to
process the surfaced items now, one at a time** — entering plan.md's ordinary
present-and-interview loop on the user's yes. In any other chat the offer is not
made and this skill files only.

**What already happened → this chat's LOG entry, as a marked tail.** Append rather
than rewrite, under a heading that says what it is:

```
## After the close

<what was done, and why — the same authoring standard as the entry above it>
```

**Where this chat has no LOG entry yet**, there is nothing to append to: the work
is recorded by the close when it runs, so say that and file only the captures.

**Nothing is committed here.** The tail rides the next close's commit. Say so when
reporting, so the user is not left thinking the record is saved.

**Where a candidate is genuinely both** — work that was done AND revealed more to
do — write both, each carrying its own half: the tail records what happened, the
capture records what is left.

**State this sentence, as written, the first time this session says it; where the
session has already stated it, restate the operative fact in one clause instead —
"again, only what was still in view".** The full sentence teaches the limit and
the clause carries it; a session that repeats the whole lesson three times is
spending the user's attention on something they were told at the first statement.

> I can't tell whether any of our earlier conversation has dropped out of view,
> so this is what I could still see rather than a guarantee I've caught
> everything.

**Say it as written rather than conveying its sense, and name no observable
proxy** — length, duration, message count. Each stands in for the thing that
actually decides the result — whether the conversation has been summarised —
which is not observable at all, and each invites the user to discount the result
by a factor that is fictional.

**Nothing found is a result, and it takes one line.**

> Read back over our discussion — nothing came up that isn't already captured.

## Step 3: Say what happens next, then hand back  [BRIEF]

Name what the captures are waiting for — **the planning run this chat is in,
where one is running, and otherwise the next one.** Processing a capture is
exactly what /plan does, so a session still open can settle what was just filed.
Say it once, plainly.

**Then resume whatever was running and carry on from where it was.** A scan run
inside a build or a planning run interrupts that work and returns it; the
hand-back is a return, not a close, and nothing has to be restarted — the skill's
instructions are still in the conversation.

**Recommend nothing else.** This skill exists partly because close machinery
accumulating at the end of a chat pulls the whole chat toward ending. A /rescan
that finishes by suggesting the close would rebuild that pull at a new site.
