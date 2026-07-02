# Sovereign Implementer

An OpenCode workflow that lets you build the project you have in mind — an app, a website, a tool, whatever you're making — without writing code yourself. You describe what you want; OpenCode builds it — and the workflow keeps the work organised across sessions so nothing drifts or gets lost.

## Install

OpenCode is a free, open-source terminal AI coding agent. Install it first, then add this workflow.

**Install OpenCode.** The easiest way is the install script:
```
curl -fsSL https://opencode.ai/install | bash
```
Or via npm: `npm install -g opencode-ai`. Full install options at [opencode.ai](https://opencode.ai/docs).

**Configure a model provider.** Run `/connect` in OpenCode to set up a model provider. OpenCode supports Claude, GPT, Gemini, Groq, and any OpenAI-compatible endpoint — bring your own API key.

**Add the workflow.** Create a folder called `.opencode/` in your project directory. Copy the `commands/` and `hooks/` folders (and the `plugin/` folder to `.opencode/plugin/`) from this repo into it. Then restart OpenCode.

Full step-by-step install guide: [INSTALL.md](INSTALL.md).

## Get notified of new versions

Want an email when a new version ships? GitHub can send you one. On this repo's GitHub page, click **Watch** (near the top right), choose **Custom**, tick **Releases**, and click **Apply**. From then on you get an email each time a new release is published. This needs a free GitHub account — signing up costs nothing.

## Who it's for

Non-coders who know what their project should do but need a framework to keep the AI coding agent on track through multi-session builds.

## What it does

The workflow splits your project into a build queue and walks you through it. It has four slash commands:

- `/setup` — asks a short questionnaire about your project and scaffolds everything
- `/plan` — organise the queue, capture ideas, resolve design questions
- `/next` — build the next item, scope-locked so the agent stays focused
- `/done` — record what happened, commit

Hooks run automatically in the background to enforce discipline — keeping your spec read-only during builds, locking scope to the current batch, and preventing unsafe git operations.

## How to use it

Run **/setup** once, when you first set up a project. After that you work in sessions, and every session ends the same way: **/done** to record what happened, then **/undo** to start fresh.

- **/plan** — think and organise: manage the queue, add ideas, resolve questions. Run it as often as planning needs; a long planning stretch is just /plan → /done → /undo, repeated.
- **/next** — build: it picks the top item and does it. You'll run /next many times, once per item, working down the queue.

The habit that matters: always /done before /undo, so each session is saved before the context resets.

## Operating conditions

**Prerequisites** — do these once per project:
- Run `/setup` in your project folder to scaffold the method docs

**Tested environment** — the workflow is developed and tested under these settings. Other configurations may work but aren't verified:
- Any capable model (Claude Opus 4 tested most thoroughly; GPT-4 works well; Gemini 2.5 Pro works well)
- Auto mode enabled — optional; it spares you approving each step by hand. Turn it off if you'd rather confirm each action.
- Start a fresh session after every `/done` (keeps each session's context clean)

## Getting started

Open any project folder in OpenCode and run `/setup`. The workflow asks a short questionnaire about what you're building, then scaffolds your project docs. When you're ready to build, run `/plan` to scope your first batch, then `/next` to start.

## License

See [LICENSE](LICENSE).
