# What a SPEC should contain, how long it should run, and whether ours conforms to a standard

Researched 2026-08-12 during the /plan that processed [spec-is-write-only-during-builds]. Commissioned by the user, who asked whether SPEC runs too long, what it might contain, and whether any useful standard exists. Findings are Claude's.

## 1. There is no length standard, and every source says so explicitly

The product-requirements literature is unanimous and unhelpful on length: precision over quantity, tailored to the product and audience, no rigid figure. Nobody publishes a word count. So **"is 6,000 words too long?" cannot be answered by appeal to a standard** — it has to be answered by what the document is for and who reads it.

Sources: [chatprd.ai product spec template](https://www.chatprd.ai/learn/product-spec-template), [Fictiv on PRDs](https://www.fictiv.com/articles/prd-product-requirements-document), [Jama Software](https://www.jamasoftware.com/requirements-management-guide/writing-requirements/how-to-write-an-effective-product-requirements-document/).

## 2. There IS a standard for our actual case, and it is spec-driven development

By 2026 every major AI coding tool ships a flavour of SDD — GitHub Spec Kit, AWS Kiro, Cursor, OpenSpec, BMAD, Tessl, Google Antigravity. The shared definition: **an executable, version-controlled specification, not the code, is the single source of truth.** The pipeline is spec → plan → atomic tasks → implementation.

That is this method's pipeline with different names: SPEC → /plan → queue items → /next. So the method already conforms to SDD in shape, and the method's own documents already invoke SDD by name when justifying the spec-sync gate.

Sources: [Microsoft for Developers on SDD](https://developer.microsoft.com/blog/spec-driven-development-ai-native-engineering/), [thebcms SDD guide](https://www.thebcms.com/blog/spec-driven-development/), [DEV: SDD in 2026](https://dev.to/krlz/spec-driven-development-in-2026-what-it-is-the-tooling-and-how-teams-actually-use-it-2fk2).

## 3. The finding that bears hardest on the queue item

**In SDD the spec is read at implementation time — that is the entire point of calling it the source of truth.** A spec written to and never read during implementation is not performing the SDD role the method claims for it; it is documentation with a sync ritual attached.

This is direct evidence for the change decided at that /plan: /next reads SPEC at run start, and the close checks what was built *against* SPEC rather than syncing SPEC to match what was built. The second is the sharper point — a close-time sync on a doc the build never read can only ever record what the build did, which is a justification, not a check.

## 4. A structural distinction worth stealing

Spec Kit separates a **constitution** — durable project-level rules, "the system shall use TypeScript strict mode" — from the **spec**, which describes what is being built. This method already has that split: CLAUDE.md is the constitution, SPEC.md is the spec. The split is not the problem.

**What is worth examining is how much of our SPEC.md is neither.** Large stretches describe hook internals, marker-file JSON fields, reader policy, and version history — implementation description rather than product truth. SDD guidance is consistent that implementation detail belongs downstream of the spec, not inside it. The editing-state-signal contract is the clearest case: it is a published interface contract for another application, which is a real artifact that has to live somewhere, but "what this product is" is probably not it.

**This is an observation, not a recommendation to cut.** Deciding what leaves SPEC is a separate piece of work from deciding whether builds read it, and doing both at once would confuse a size problem with a role problem.

## 5. What this does not settle

Whether SPEC earns its keep in a project where the developer already holds the product truth in their head. No standard addresses that, because the standards assume a team. The method's own answer — a consumer six months in, and a fresh short session, hold no such copy — is unaffected by anything found here.
