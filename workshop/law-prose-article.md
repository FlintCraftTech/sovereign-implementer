# Rules Written as Statute

*I'm a no-code developer. I spent months writing rules for an AI and getting worse
results the harder I tried — until I stopped writing prose and started writing law.*

Alex Wilder · Flintcraft

---

Everything below comes out of building **Throughliner**, a Claude Code plugin that
gives no-code developers a structured way to build things with an AI — software,
and a good deal that isn't.

Which sounds easy, and is not. Writing rules a model actually follows turned out to
be the hardest part of the whole project, and I got there by failing at it twice
first.

## 1. More words, less obedience

My first instinct was the obvious one: if the model isn't doing what I want, explain
harder. So I wrote prose. Paragraphs of it. Every rule came with its reasoning
attached, because I assumed that a model which understood *why* would apply the rule
more sensibly at the edges.

What I got was a document nobody could hold in their head, including the machine.
Rules contradicted each other in ways I couldn't see, because the contradictions were
four hundred words apart. Behaviour drifted, and I'd add another paragraph to correct
the drift, which made the document longer, which made the drift worse.

> The reasoning I attached to every rule was not free. It was the thing crowding out
> the rules.

Three things were going wrong at once, and it took me a long time to separate them:

- **A rule with its justification attached is longer** — often three or four times
  longer than the instruction inside it.
- **A model follows fewer of its instructions reliably as they lengthen.** Attention
  is finite. Every sentence competes.
- **Near-identical rules degrade one another.** Two rules saying almost the same
  thing in slightly different words are perfect distractors — the model has to decide
  which one it's in, and it can pick wrong.

## 2. Pseudocode, and why it broke

So I went the other way. If prose was too loose, I'd write something tighter — rules
shaped like code, with conditions and branches, because that's what precision looks
like when you've been reading a lot of code.

It was shorter. It was also brittle in a way I hadn't anticipated. Pseudocode is good
at cases you have already thought of and silent about everything else. Real sessions
are almost entirely made of situations I had not thought of, and the model, meeting a
case my branches didn't cover, had nothing to reason from. Prose at least degraded
gracefully. Pseudocode just stopped.

There was a second problem, subtler. An `if` assumes you can tell whether its
condition holds at the moment you check it. That's fine for "is the file there".
It is not fine for what my rules actually turn on — whether a change is
significant, whether a reason is genuinely needed to apply a rule, whether this
is a moment to ask a person. Those are judgements, and writing them as branches
doesn't remove the judgement. It hides it. The branch form *looks* mechanical,
so the reader stops weighing and starts matching, which is the wrong move on a
condition that was a judgement call all along. Legal drafting keeps it in plain
sight: "where the change is significant" sits in the open as a standard the
reader knows they have to apply.

## 3. The form that already existed

The thing that finally worked wasn't my idea. It's a few hundred years old, and it's
how legislation is drafted.

Legal drafting solved this problem long before anyone needed to instruct a machine:
how do you write a rule that a stranger will apply correctly, without you there to
explain it, in circumstances you didn't foresee? The conventions that come out of that
are remarkably specific — and every one of them turned out to matter.

One thing to be clear about before the list. These documents are read by a machine
almost every time — that is their job — but they need to be legible to humans, too. 

### State the action, not the prohibition

This was the biggest single change. If a rule is written as "don't do X", the thing to
actually do has never been stated. The model has to infer it, and inference is where
behaviour goes strange. Anything described in terms of what not to do is a signal that
the real rule was never written down.

| Before | After |
|---|---|
| Do not open QUEUE.md | Leave QUEUE.md closed |
| never auto-send | every send waits for approval |
| a build never writes product truth | product truth is written at planning time, before any build starts |

The first two are inversions. The action was already sitting inside the
negative, and turning it round costs nothing — which is the common case. The
commonest shape in my documents was "do X, never Y", where X already states the
action and the negative tail is pure decoration. Those restyle and shorten in
the same move.

The third is the hard kind, and the one that actually changed behaviour. "A
build never writes product truth" tells you where something must not happen and
leaves you with no idea where it does. The replacement names the moment —
planning, before any build starts — and that is a fact the prohibition never
contained. So the tell for a rule worth rewriting isn't that it's phrased
negatively. It's that the positive version carries information the negative one
couldn't.

Cutting the negative also saved real space.
Almost everything in those documents was stated twice over — once as the action,
once as the prohibition, side by side in the same sentence. Being free to keep
only the positive half took a great many of them down to their operative line.
The restyling and the shortening turned out to be the same edit, done once.

Whilst I can't put a figure on that, I'd say the text got shorter. Claude loves disambiguating statements by addition of negatives, probably because it makes instructions clearer for humans. But this common convention doesn't work for efficiency. 

### Main clause first, conditions after

"Where the queue is empty and no work is cleared, ask the user what to do" buries the
instruction behind two conditions the reader must hold in mind before they learn what
they're holding them for. Put the action first. The conditions still bind; they just
stop obstructing.

While the evidence might not necessarily bear out for this one with AI, this one certainly makes our rules easier on the human eye. 

### Carry qualifications in structure, not explanation

Legal drafting has cheap machinery for this — *subject to*, *except that*, *unless*,
*so long as* — short connectives that attach a qualification without arguing for it. We
had been writing a sentence of explanation where a two-word connective would do.

### One idea per provision

If you put
two instructions in one sentence, the model does the first and drops the second —
not every time, but often enough to matter.

Mine was filing research. One rule said to write the finding to a file *and* add
a line for it to the index. The findings got written. The index lines mostly
didn't, and I ended up with a folder of notes no later session could find,
because nothing pointed at them — a write path with no read path. Splitting it
into two provisions fixed it. Almost the same words; two separate things to be
done, and each one now visibly either done or not. 

## 4. What the numbers actually said

I rewrote the always-loaded rules to that standard and counted before and after,
expecting a fall.

| Figure | |
|---|---|
| **299** | rule statements before the rewrite |
| **299** | rule statements after it |
| **61 → 9** | uses of one ambiguous word, "session" |

Dead flat — and flat by composition rather than by nothing happening. Statements
came out; and four statements that had *always* been rules became countable for
the first time, because their formatting had run past the point where my counting
script could see them.

Note what that number is and isn't. It counts *rules*, not words. The text got
shorter — dropping the duplicated negatives did that — while the number of rules
held. Two different measures, and a flat one beside a falling one is the whole
story rather than a disappointment: the corpus didn't lose rules, it lost the
second copy of each one. And the counter started telling the truth.

The figure I'd actually point at is the third one. "Session" meant four different
things across those documents — a chat, a run, a machine's notion of a session, a UI
label. Nine survivors, each unambiguous.

Then the same pass ran across the whole corpus: fourteen documents, just under three
hundred prohibitions, restyled into the action each one required. One document needed
nothing at all.

## 5. What I deliberately left alone

This is my favourite part, and it's the part a purely mechanical pass would have
destroyed.

Three kinds of negative statement survived, because in each case the negative *is* the
content:

- **Contrast pairs.** A block showing the right form beside the wrong one teaches
  faster than either alone.
- **Statements of what a mechanism does not cover.** "The harness never merges a
  session's branch back" is a fact about a tool, not an instruction to anybody.
- **Honest limits.** The ones I'd defend hardest.

Throughliner screens every session for anything that might expose the user's data, and
the rule governing it ends: *never a guarantee that every risk present has been found.*

> That is not a prohibition failing the standard. It is the tool refusing to
> over-claim, and rewriting it into a positive would have been a lie told for the sake
> of consistency.

A style rule that can't tell those apart isn't a style rule, it's a find-and-replace.
Deciding which kind a sentence is takes reading the provision around it — which is
exactly why this was a job of work and not a script.

## 6. What I can't claim

Three limits, and I'd rather state them than have someone find them.

**Limit one.** The rewrite covered the findings I had, the terminology, and what a full
read of each file surfaced. It is not a claim that all 299 statements now conform to
the standard.

**Limit two.** A flat count cannot detect a rewrite that changed a rule's meaning. The
count told me the corpus hadn't grown. It could not have told me if I'd altered what a
rule required while tidying it, and nothing else was watching for that either.

**Limit three.** Targets were found by searching for known phrasings. A prohibition
written in wording I didn't think to search for was never seen — so every pass records
what it covered, rather than implying the corpus is clean.

And the largest caveat of all: this is one project's experience, measured on its own
documents. I have a corpus, a set of before-and-after behaviours, and a strong
conviction. I don't have a controlled experiment.

## 7. Take the method

None of this is specific to Throughliner, or to Claude, or to any particular tool. If
you are writing instructions that a model has to follow — a system prompt, a rules
file, an agent's standing orders — the conventions transfer directly, because they were
never about AI in the first place.

So the drafting rules ship with this article as a free resource: a plain prompt you can
paste into whatever you're using, which applies the same standard to your own
instructions. No install, no dependency, nothing to sign up for.

It is, after all, a form the legal profession worked out a long time ago and left lying
around. I just noticed it applied to machines.

---

*Throughliner is a Claude Code plugin for no-code developers. It is in active testing.*

*Draft — not yet published.*
