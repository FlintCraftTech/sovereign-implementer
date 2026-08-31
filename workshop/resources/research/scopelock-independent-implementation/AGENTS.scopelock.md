<!-- scopelock fragment — append this to your project's AGENTS.md -->

## Scope discipline (scopelock)

This project runs a scope lock. File edits outside the `## Files` list in
`SCOPE.md` are denied by a hook. These rules cover what the hook cannot enforce:

**Capture instead of act.** When you notice something outside the current
scope that probably needs doing — a bug nearby, a refactor that would help, a
missing test — do not act on it and do not stop to ask about it. Append one
line to `BACKLOG.md` in the repo root (create it if absent) in this form:

```
- [ ] <what> — <where> — noticed while <current task>
```

Then continue with the task. Capturing is success, not failure: it converts an
out-of-scope impulse into a record the user can triage later.

**The halt rule.** There is exactly one situation where you stop instead of
capturing: when acting on the current task itself would require you to invent
scope the user never agreed to — the work item is too ambiguous to determine
which files it touches. In that case, halt and ask the user. Do not guess.
Everything else captures and continues.

**Scope expansion.** If the current task genuinely requires editing a file the
lock denies, first check whether it can go to `BACKLOG.md` instead. If it
truly cannot wait, tell the user which file you need and why, and once they
agree, add its path under `## Files` in `SCOPE.md`. The lock updates
immediately — no restart. Never expand scope silently: an unexplained
`SCOPE.md` edit defeats the purpose of the lock.

**Denied is not broken.** A denial from the scope lock is advice, not an
error. Read the reason — it names the legitimate alternative. Do not attempt
to route around a denial via shell redirection, `tee`, `sed -i`, or similar.
