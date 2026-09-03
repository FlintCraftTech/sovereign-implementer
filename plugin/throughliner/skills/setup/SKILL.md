---
name: setup
description: Set up a project folder with the Throughliner method. Scaffolds SPEC.md, QUEUE.md, and LOG/ then interviews the user to populate them.
disable-model-invocation: true
user-invocable: true
---

# /setup

The user wants to bring this folder under the Throughliner method.

**First, check this conversation for the `[Throughliner]` session-start lines.** Where none are present, the hooks did not run — usually because `python` is missing from the machine, or is the Windows Store placeholder that prints "Python was not found" and exits. Say so plainly, give the check (`python --version` must print a version, not "Python was not found"), and carry on with this skill: the procedure docs still govern, and only the safety checks and the session-start facts are absent.

Read and follow the procedure at `${CLAUDE_PLUGIN_ROOT}/docs/setup.md`. The file may be longer than one read returns; the read is complete only when the tool reports no further page.

Before writing anything, create an empty `.throughliner-setup-active` file in
this session's scratchpad directory, and delete it when the run ends — including
on the paths that end early. It tells the safety check this is a setup run;
without it, the files setup exists to write are refused.
