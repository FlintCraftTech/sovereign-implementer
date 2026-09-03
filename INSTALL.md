# Install guide — Throughliner

**What this is.** A step-by-step guide to installing the Throughliner plugin for Claude Code. You paste this guide into a chat at claude.ai, and Claude reads it and walks you through the install one step at a time — you don't have to figure anything out on your own.

**Who it's for.** Anyone who wants to use Throughliner and is new to this. No coding or terminal experience is needed. Everything happens in apps you click through, not a command line.

**What to expect.** Claude will ask you a couple of quick questions to find out where you're starting from, then guide you through getting Claude Code (if you don't have it), making sure you're on a paid plan, and adding the plugin. It goes one step at a time and waits for you at each one.

**Already have Claude Code and a paid plan?** You can skip the opening questions below. Still do the quick app check in [Step 1 — Opening interview](#step-1--opening-interview) to confirm you're actually in Claude Code (not the Claude chat app), then jump straight to [Branch B — Install the Throughliner plugin](#branch-b--install-the-throughliner-plugin). Branch B installs by asking Claude Code to add the plugin's marketplace and install it — Claude runs the commands for you, so you never type in a terminal.

**How you can tell Claude actually read this guide.** Claude's first message to you should open with this exact line:

> Throughliner install guide loaded — I'll take you through it one step at a time.

If Claude starts improvising install advice without saying that, it is working from the link's title rather than the guide. Ask it to read the guide at the link in full and start again.

**For Claude (the assistant reading this):** your operating instructions are at the end of this file, in the "Instructions for Claude" section. Read that section before you start walking the user through anything.

## Before you start — you'll need a paid Claude plan

Claude Code only runs on a paid Claude plan. **A Claude Pro subscription is enough — you do not need Max.** (Pay-as-you-go API credit also works, but for most people a Pro subscription is the simpler path.)

There's no fixed dollar figure here on purpose, because prices change — check Anthropic's current pricing, which you'll find at claude.ai under **Settings > Plans & Billing**.

What "within plan limits" means in plain terms: a Pro subscription includes a set amount of Claude Code usage in each period. If you reach that limit, Claude Code pauses until your usage resets — it's a wait, not a surprise charge. (Only pay-as-you-go API credit can run up an open-ended bill, which is why a subscription is the easier choice to start with.)

If a paid plan isn't something you can do right now, this is the moment to stop — the rest of the guide needs one.

## Step 1 — Opening interview

Before recommending anything, find out where the user is. Ask these questions **one at a time** (see the pacing rules in the Instructions for Claude section — do not bundle them). Wait for an answer before the next.

1. **Which operating system are you on?** Windows, macOS, or Linux?

2. **Let's confirm which app you have open.** There are two different Anthropic apps and they're easy to mix up: **Claude Code** (what we need) and the **Claude chat app** at claude.ai (not what we need for this). So that we route you correctly, tell me what you actually see:
   - What does the title bar or window say?
   - Does the window have a **Code** area / a place that looks like a developer workspace, or is it just a **chat box** where you type messages?

   Use the answer to decide:
   - **They describe Claude Code** (a developer/Code workspace, "Claude Code" in the title) → they have the right app. Continue.
   - **They describe the Claude chat app** (just a chat interface, claude.ai) → they don't have Claude Code yet. Tell them plainly: Claude Code is a separate desktop app from the Claude chat app — it's the one that can build projects on their computer, and it's what this plugin runs inside. Then route them to **Branch A** to install it.
   - **They're not sure / haven't installed anything** → treat it as "no Claude Code" and route to **Branch A**.

Based on the answers, route them:

- **No Claude Code installed (or wrong app)** → Branch A, then Branch B.
- **Claude Code installed** → Branch B. (The paid-plan requirement was already covered above — confirm they're set rather than re-asking it as a fresh question.)

## Branch A — Install Claude Code (desktop app) and set up a paid plan

### A.1 — Install the desktop app

Walk them through downloading and installing the Claude Code desktop app for their OS. Web-search for the current official download page before sending them anywhere — don't guess URLs. The download is an installer they run like any other app; there is no terminal step required to get the app onto their machine.

After install: have them open the app once and sign in with their Anthropic / Claude account.

### A.2 — Paid plan

Claude Code requires a paid plan (covered in "Before you start" above). Be honest about this — don't soften it. The options are:

- **Claude Pro or Max subscription** (monthly) — covers Claude Code usage within plan limits. Manage at claude.ai under Settings > Plans & Billing. Pro is enough.
- **API pay-as-you-go** — top up credit at console.anthropic.com. Used when subscription limits are exceeded or for usage outside a subscription.

Recommend the subscription path for a non-coder unless they already have API credit set up. Walk them through upgrading at claude.ai if needed, then return to the desktop app and confirm it recognises the plan (they should be able to start a session without a billing error).

## Branch B — Install the Throughliner plugin

Once Claude Code is installed and the user is on a paid plan, the plugin installs from its marketplace on GitHub. The good news for a non-coder: **Claude Code runs the install commands for you** — you ask it, in plain English, and it does the rest. You never type in a terminal.

**This still hands off.** You (Claude, in the claude.ai chat) cannot run the install from here — you have no access to the user's machine. The install happens inside **Claude Code**, driven by the Claude Code agent there. Your job in this chat is to tell the user exactly what to ask Claude Code to do, then wait for them to report back. Never pretend this chat can run the install itself.

**Prerequisite — Python 3, installed and on the path.** The plugin's safety checks and its session-opening facts are small Python scripts that Claude Code runs for you; without Python they silently do nothing, and the plugin reports success anyway. Before installing, have the user ask Claude Code to run `python --version`. It must print a version number. On a fresh Windows machine it may instead print "Python was not found; run without arguments to install from the Microsoft Store" — that is a placeholder, not Python. Install Python from python.org (ticking "Add python.exe to PATH" in the installer), fully restart Claude Code, and check again before going on.

### B.1 — Ask Claude Code to install the plugin

The install uses Claude Code's plugin marketplace. It's two commands — but the user does **not** have to type them. Instead, have them open a chat **inside Claude Code** and ask the Claude Code agent, in plain words, to install the plugin. Give them this to paste or say:

> Please add the plugin marketplace `FlintcraftTech/throughliner#beta` and then install the `throughliner@flintcraft` plugin from it.

The `#beta` on the end matters: it points at the tested weekly pick rather than the day-to-day development line, so the user installs a version that has been checked over. Keep it exactly as written.

The Claude Code agent will run the two commands itself:

```
claude plugin marketplace add FlintcraftTech/throughliner#beta
claude plugin install throughliner@flintcraft
```

(If the user would rather run them by hand, those are the commands — but the default and easiest path is to let Claude Code run them.)

**The repository and the plugin now share the name `throughliner`.** If the user is coming from the plugin's old name, Sovereign Implementer, Claude Code follows the old name automatically but still needs to fetch the plugin under the new one — so the install above is run once, then the app is fully restarted.

After both succeed, the plugin activates on a full restart of Claude Code. Have the user fully quit and reopen the app, then run the smoke test in B.2 to confirm it took. If the marketplace-add or install errors — for example, the marketplace can't be found — have them tell the Claude Code agent the exact error and work it from there; the agent can retry or diagnose.

### B.2 — Smoke test — confirm the plugin works

This is just a quick check that the install took. It doesn't need a real project.

- Have them make a new empty folder anywhere (e.g. on the Desktop, call it `si-test`).
- In Claude Code, open that folder via **File > Open Folder** (or the app's equivalent "open folder" action) so there's a folder open to work in.
- Click into the **chat box** (where you'd normally type a message) and start typing `/setup`. As they type, a menu of available commands appears.
- **Success looks like:** a command for setup shows up in that menu. It may appear as `/setup`, or namespaced as `/throughliner:setup` — either form means the plugin is installed. Have them select it and press **Enter** to run it. (For the smoke test, seeing the command appear is already enough; they don't have to finish a real setup here.)
- **Failure looks like:** they type `/setup` and **no matching command appears** in the menu at all. That means the plugin isn't registered yet.

If it fails, work through these in order — don't jump straight to reinstalling:
1. **Fully quit and reopen the app** — not just a new session. Plugin commands register when the app launches, and on Windows a normal "quit" can leave the app running in the background, so a new chat or even a normal close-and-reopen may not pick them up. Quit the app, then on Windows confirm the process has actually exited (check Task Manager and end it if it's still there) before reopening. Then try `/setup` again.
2. If it still doesn't show, have the user ask the Claude Code agent to confirm the plugin is installed and enabled (the agent can list installed plugins), and to reinstall it with `claude plugin install throughliner@flintcraft` if needed. Then fully restart again.

A note for real use later: `/setup` is also the command that sets up a real project once the plugin is confirmed working — that's a separate step you'll do in your own project folder, not part of this test.

### Updating later

To update, have the user ask the Claude Code agent to run `claude plugin update throughliner@flintcraft` (Claude Code runs it — no terminal typing), then fully restart the app so the new version loads. Because the marketplace is pinned to `#beta`, each update brings the newest tested weekly pick rather than whatever is on the development line that day.

## Step 2 — First-run pointer

Once the plugin is installed and the `/setup` command is recognised, tell the user:

> You're set up. To start a real project, open its folder in Claude Code (**File > Open Folder**, or create a new empty folder for it first) and run `/setup` to scaffold the method docs. From there, `/plan` to scope your first batch and `/next` to start building.

Do not run /setup for them in this chat — they need to do it in their own desktop app, in their own project folder.

That's the end of the install guide — Throughliner is installed and your project is ready to start.

---

## Instructions for Claude (you can skip this section)

This section is for the assistant reading the guide, not for the human installer. If you're the person installing, you can stop above — everything you need is in the steps.

**Note to Claude:** You are reading this guide on a user's behalf. They have opened a fresh chat at claude.ai and pasted this link because they want to install the Throughliner plugin for Claude Code. Follow the instructions in this file to walk them through it.

**Open with the verification line, before anything else.** Your first message to the user starts with exactly:

> Throughliner install guide loaded — I'll take you through it one step at a time.

Then go to the opening interview. The line is how a non-coder can tell a guide that was read from advice that was improvised, and it is stated near the top of this file so they know to look for it. Say it only when you have actually read this guide.

**Ground rules:**
- Assume the user has zero terminal experience and is mildly allergic to terminals. Use the Claude Code **desktop app** at all times. The plugin install (Branch B) uses `claude plugin ...` commands, but the user does not type them — the Claude Code agent runs them on the user's behalf. Frame it that way: they ask Claude Code in plain English and it runs the commands. Don't have the user open or type into a terminal, and don't suggest unrelated CLI workflows (`claude --version`, `/config` in a terminal, etc.).
- You don't have access to their machine from this chat. You're giving them instructions to follow in their own desktop app and browser. Wait for them to report back at each step.
- If you need a current download URL or up-to-date install instructions for Claude Code itself, do a web search rather than guessing — official pages change.
- The pacing rules below are mandatory. Read them before you start the walkthrough.

**Pacing rules (mandatory).** These are the user's own communication preferences, embedded verbatim. Follow them for the entire walkthrough.

> One item at a time. Any time my next action depends on you finishing the previous one, give me only one item per message. This covers — not exhaustively — questions needing my answer, items needing my approval, steps in a procedure I have to execute, and tests I have to run sequentially. The test is not "is this a question?" — it is "does what I do next depend on the result of this one?" If yes, separate.
>
> Open the sequence by stating the count. "Three steps coming. First: ..." Then stop. Do not preview steps 2 and 3 in the same message, even briefly — previewing is bundling.
>
> The pull to bundle is strongest at close-outs and walkthroughs. When you have a multi-step procedure ready (commit instructions, a smoke-test plan, an audit checklist), the natural pull is to dump the whole thing for completeness. Don't. Completeness comes from getting through cleanly, not from showing every step upfront.
>
> One inversion: alternatives for me to choose between. Comparisons need everything visible at once because the choice is between them. For alternatives: short comparison table, or recommend one with an escape line. Default to the escape-line form.
