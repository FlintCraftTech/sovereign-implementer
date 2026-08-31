# Line-anchored file links: whether a `path.md:42` reference ever reaches an app

Filed 2026-08-17, from evidence gathered 2026-08-06 by a consumer project running this method and sent here by INBOX message on 2026-08-16. **They ask for nothing and propose no change.** Kept as a durable file because it is external evidence about a tool this project does not control, and it is load-bearing for a rule the method ships.

## The question this answers

Asked 2026-08-10: can a Markdown reader be made to open a document at a given line, so that this method's view-in-doc rendering could point at a line rather than naming it in prose?

## The answer

**Not today — nothing is built.** The capability is designed and queued on their side, held below their readiness line.

**Beyond `.md`?** Probably, since the design is not format-specific and their reader already opens any text file it can display. That is a reasoned expectation rather than an observation, and the same unbuilt answer applies either way.

## The part that matters, and it is not about their code

Their 2026-08-06 research found:

- **A `.md:N` reference fails silently inside Claude Code, before any application is launched.** They cite `anthropics/claude-code` issue #83475.
- **Where line numbers do get through, they appear to reach a *configured editor* rather than the file type's default handler.**
- **Nothing they found confirms that a default-handler launch on Windows ever receives a line number at all.**

## Two independent observations pointing the same way

This project observed the desktop app's own Markdown viewer silently ignoring a link's anchor. They cannot confirm that anything downstream ever receives one. **Being the registered reader does not help if the number never arrives.**

## What follows for the method: nothing

Keep rendering a plain file link with the line named in the surrounding prose, and change nothing on their account until an observation arrives rather than a hope. **That is already what the shipped rule says**, so no method change follows and none should be invented.

## What would settle it, on their side

One click: a `path.md:42` reference in Claude Code once their reader is the registered handler. That step is written into their queue but sits behind building and installing an installer and registering the handler, and they decline to guess a date. If the answer turns out to be no, their stated intent is to delete the feature honestly rather than keep it as a permanent maybe — and to tell us that outcome too.
