# Install guide — Sovereign Implementer (OpenCode)

**What this is.** A step-by-step guide to installing the Sovereign Implementer workflow for OpenCode. You paste this guide into a chat with an AI assistant, and it walks you through the install one step at a time — you don't have to figure anything out on your own.

**Who it's for.** Anyone who wants to use Sovereign Implementer and is new to this. No coding or terminal experience is needed. Everything happens in the OpenCode terminal app or your browser.

**What to expect.** You'll be guided through installing OpenCode (if you don't have it), configuring a model provider, and adding the workflow. It goes one step at a time and waits for you at each one.

**Already have OpenCode with a model configured?** You can skip the install sections. Still confirm you can run OpenCode, then jump straight to [Branch B — Install the Sovereign Implementer workflow](#branch-b--install-the-sovereign-implementer-workflow).

## Before you start — you'll need an API key

OpenCode needs an API key from a model provider to work. The simplest paths:

- **Anthropic** (Claude models): get an API key at [console.anthropic.com](https://console.anthropic.com). Pay-as-you-go.
- **OpenAI** (GPT models): get an API key at [platform.openai.com](https://platform.openai.com). Pay-as-you-go.
- **Google** (Gemini models): get an API key at [aistudio.google.com](https://aistudio.google.com). Free tier available.

If a paid API key isn't something you can do right now, this is the moment to stop — the rest of the guide needs one.

## Step 1 — Opening interview

Before recommending anything, find out where the user is. Ask these questions **one at a time** (see the pacing rules in the Instructions for Claude section — do not bundle them). Wait for an answer before the next.

1. **Which operating system are you on?** Windows, macOS, or Linux?

2. **Do you already have OpenCode installed?** You can check by opening a terminal and typing `opencode --version`. If it shows a version number, OpenCode is installed. If the command isn't found, you don't have it yet.

Based on the answers, route them:

- **No OpenCode installed** → Branch A, then Branch B.
- **OpenCode installed** → Branch B.

## Branch A — Install OpenCode

Walk them through installing OpenCode for their OS. Web-search for the current official download page before sending them anywhere — don't guess URLs.

The easiest path is the install script:

**macOS / Linux:**
```
curl -fsSL https://opencode.ai/install | bash
```

**Windows (npm):**
```
npm install -g opencode-ai
```
(Recommended: use WSL on Windows for the best experience.)

Also available via Homebrew (`brew install anomalyco/tap/opencode`), Chocolatey (`choco install opencode`), and other package managers.

After install: have them open a terminal, navigate to a project folder, and run `opencode`. The first time it starts, it'll ask for a model provider — use the `/connect` command in the OpenCode TUI to configure one.

## Branch B — Install the Sovereign Implementer workflow

The workflow is installed by copying its files into your project's `.opencode/` directory.

### B.1 — Copy the workflow files

1. Download or clone this repository to your computer.
2. From the `open-si/` folder in the repo, copy these into your project's `.opencode/` folder (create it if it doesn't exist):
   - `commands/` → `.opencode/commands/`
   - `hooks/` → `.opencode/hooks/`
   - `plugin/si-plugin/` → `.opencode/plugin/si-plugin/`
3. Copy `opencode.json` to your project root (or add its contents to your existing `opencode.json`).

### B.2 — Build the plugin (TypeScript)

The hooks need to be compiled before they work:

```
cd .opencode/plugin/si-plugin
npm install
npm run build
```

### B.3 — Smoke test — confirm the workflow works

- In OpenCode, open your project folder.
- Type `/setup` and press Enter.
- **Success looks like:** `/setup` appears in the command menu and begins running.
- **Failure looks like:** `/setup` doesn't appear or isn't recognised.

If it fails:
1. Quit and reopen OpenCode — commands register at launch.
2. Check that the `commands/` and `plugin/` folders are in the right places.
3. Make sure `npm run build` completed without errors.

## That's it

Run `/setup` to scaffold your project docs, then work through your queue with `/plan`, `/next`, and `/done`.

---

## Instructions for the AI assistant (can skip)

**Note to the AI assistant:** You are reading this guide on a user's behalf. They have pasted this because they want to install the Sovereign Implementer workflow for OpenCode. Follow the instructions in this file to walk them through it.

**Ground rules:**
- Assume the user has zero terminal experience and is mildly allergic to terminals. Use the OpenCode terminal app.
- You don't have access to their machine from this chat. You're giving them instructions to follow. Wait for them to report back at each step.
- If you need a current download URL or up-to-date install instructions for OpenCode itself, do a web search rather than guessing — official pages change.

**Pacing rules (mandatory).** One item at a time. Any time the user's next action depends on you finishing the previous one, give them only one item per message. Open the sequence by stating the count. Do not preview upcoming items in the same message — previewing is bundling. One exception: alternatives the user is choosing between need everything visible at once.
