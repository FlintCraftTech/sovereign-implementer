# 7b751b6 — plan — two port flavours named, so a port can say what it is

**The user's observation and her definitions**, from two people porting Throughliner to other harnesses: a port that *accepts changes at face value and adds no new ones of its own beyond what its system required to fit*, and a port that is *unique and special, which may or may not accept changes derived from the changelogs*.

**Her stated goal, which is why this is work rather than vocabulary:** people should have the **opportunity** to run a Throughliner led by the original project and carrying all its features so far as their setup allows — and diverging, renaming, developing it themselves is equally fine.

**Naming them is the work.** Today nobody can tell what a given port promises, including her. A user choosing between ports cannot tell whether the one they install follows the method; a porter cannot signal it; and she cannot tell which ports her changelog is even for.

**Rule gate: run — admitted as a definition rather than a rule.** It constrains no session's behaviour and adds nothing to the always-loaded set. No parent applies, and that is stated rather than a parent being invented for form.

**Refused: a registry of who runs which flavour.** Maintaining a list of other people's projects is a standing obligation this project cannot keep accurate, and absence from it would read as disapproval. The flavour is something a port declares about itself.

SPEC sentence written at the close's spec-sync gate, since SPEC mentioned porting nowhere and two cleared items now define product behaviour.

**Queue changes:** [port-flavours-named] filed and cleared, second of the four port items.
**Work processed:** kept — [port-flavours-named].
