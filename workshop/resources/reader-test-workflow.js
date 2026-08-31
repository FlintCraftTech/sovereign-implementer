export const meta = {
  name: 'reader-test',
  description: 'Test plugin doc comprehension via simulated bookshelf tracker project',
  phases: [
    { title: 'Simulate', detail: 'Three agents simulate /plan, /next, /done' },
    { title: 'Verify', detail: 'Audit each simulation against procedures' },
    { title: 'Questions', detail: 'Answer and score 5 user questions' },
    { title: 'Synthesize', detail: 'Categorize findings for routing' },
  ],
}

// ── Plugin doc paths ──

const P = 'C:/Users/Alex/Desktop/Taskflow Planning/No code method/plugin/throughliner'
const TEMPLATE = P + '/templates/CLAUDE-TEMPLATE.md'
const BEHAVIOUR = P + '/docs/plugin-behaviour.md'
const PLAN_DOC = P + '/docs/plan.md'
const NEXT_DOC = P + '/docs/next.md'
const DONE_DOC = P + '/docs/done.md'

// ── Fake project: Bookshelf Tracker (mid-project) ──

const FAKE_SPEC = `# SPEC — Bookshelf Tracker

## What it is
A personal book-tracking app. Local-first, stores data in a JSON file. No accounts, no cloud sync.

## Who it's for
A single user who wants to track what they're reading and what they want to read next.

## How it works
- Add books with: title, author, status (want-to-read / reading / read), optional notes
- View all books in a flat list, sorted by date added (newest first)
- Status is the primary organizer — filter by want/reading/read
- Data lives in data/books.json in the project directory

## Constraints
- No database — flat JSON file only
- No network requests — fully offline
- No categories or shelves — just one flat list with status filtering
- Vanilla JavaScript, no frameworks or build tools`

const FAKE_QUEUE = `# QUEUE

## Batches

Worked top to bottom. Each batch of changes or tests is one /next session of either type:

- build session where changes are applied, then claude runs all tests it is able to do itself
- test session where the user runs any testing only they can do

**Search and filter** **[search-and-filter]**

Build:
- Add search bar that filters by title or author (case-insensitive substring match)
- Add status filter dropdown (all / want-to-read / reading / read)

Test:
- Verify search narrows the list in real-time as you type
- Verify status filter works alone and combined with search

**Export to CSV** **[export-csv]**

Build:
- Add export button that writes all books to a CSV file (title, author, status, notes, date added)

Test:
- Verify exported CSV has correct headers and all book data

### Parked

## Captures

Captured outside /plan. Picked up and routed during the next /plan session. Processed captures (slug assigned, dependencies scanned) sit above the \`---\` divider; unprocessed raw captures collect below.

---

- Could add a "favorites" tag to quickly find top picks
- The book list doesn't show the date a book was added — would be useful for tracking reading pace
- Should the JSON file stay as one big file or split per status? Currently it's one file but as the list grows it might get slow

### Parked`

const FAKE_LOG = `# LOG

Full session entries, newest first. Each entry is written by /done.

## b3f4e2a — /next [add-book-form]: book entry form with status field and auto-save

Added the add-book form as a separate component. Four fields: title (required), author (required), status (dropdown, defaults to want-to-read), and notes (optional textarea). Form validates that title and author are non-empty before saving. On submit, storage.js appends the new book to data/books.json and the list re-renders with the new entry at the top. Kept the form minimal — no edit mode, no delete, no confirmation dialog. Those are future scope if needed.

**Files touched:**
- src/addBook.js: created form component (title, author, status dropdown, notes textarea), 62 lines
- src/storage.js: added writeBook() function alongside existing readBooks()
- src/app.js: added route for add-book view, wired navigation

## e8c1d9f — /next [initial-scaffold]: app shell, book list, and storage layer

First build. Set up the project structure: app shell with a header and two views (list and add), book list rendering from JSON, and the storage layer that reads data/books.json. Books display as cards with title, author, and a coloured status badge. List is sorted newest-first by date added. No filtering or search yet — flat list only.

**Files touched:**
- src/app.js: created app shell with header and view routing, 40 lines
- src/bookList.js: created book list component with status badges, 55 lines
- src/storage.js: created readBooks() with JSON file I/O, 25 lines
- src/styles.css: global layout, card styles, status badge colours
- data/books.json: created with 3 seed books for testing`

const FAKE_BUILD = `# Active Build

Entry: **Search and filter** **[search-and-filter]**

Build:
- Add search bar that filters by title or author (case-insensitive substring match)
- Add status filter dropdown (all / want-to-read / reading / read)

Test:
- Verify search narrows the list in real-time as you type
- Verify status filter works alone and combined with search

Index entry candidate: src/search.js and src/bookList.js — added search bar (case-insensitive title/author substring match) and status filter dropdown; wired into book list view.

Progress:
- [x] Add search bar — done
- [x] Add status filter dropdown — done

Changes:
- src/search.js: created search component with text input and status dropdown, 85 lines
- src/bookList.js: added import for search component, wired filter logic into list rendering`

const FAKE_CLAUDE_MD = `# CLAUDE.md

<!-- ▼ PLUGIN-MANAGED — do not edit between these markers. Updated on /setup and plugin reinstall. ▼ -->

This project uses the Throughliner method.

## Project docs

- **SPEC.md** — product truth. What it is, who it's for, how it works.
- **QUEUE.md** — work queue, top-to-bottom. Batches (Build/Test subheadings), Captures (split by \`---\` — processed above with slugs, raw appended below). Items removed from active flow carry \`Blocked by:\` (trigger-based) or \`Parked:\` (indefinite) headers.
- **LOG/** — session records: what was built, tested, decided.

## Workflow

- \`/setup\` — scaffold project docs (done if you're reading this).
- \`/plan\` — queue management, captures, design questions.
- \`/next\` — execute the top batch.
- \`/done\` — record, update docs, commit.

## Rules for Claude

- SPEC.md is a normal doc, changed only through a planned spec-edit batch that /next executes and that lists SPEC.md in its Files — not edited inline during /plan, and not touched by a feature build.
- Only touch files listed in the active build scope. Halt and ask if you need more.
- One build at a time. Finish and /done before starting another.
- State problems plainly. Don't hide them or silently fix unrelated things.
- Route discoveries to QUEUE.md rather than acting on them immediately.

## Language

Language: English

<!-- ▲ PLUGIN-MANAGED — do not edit above this line. ▲ -->

## Project rules

- This is a vanilla JavaScript project. No frameworks, no build tools.
- JSON file lives at data/books.json in the project root.
- Keep the UI simple — no animations or transitions.`

// Session-start hook outputs

const SESSION_NO_BUILD = `[Throughliner] Project is set up.
  SPEC.md: found
  QUEUE.md: found

Ready. Run /plan to manage the queue, or /next to start the top batch.`

const SESSION_ACTIVE_BUILD = `[Throughliner] Project is set up.
  SPEC.md: found
  QUEUE.md: found

ACTIVE BUILD in progress (_build.md exists). Run /next to resume, or /done if the work is complete.`

// ── Schemas ──

const SIM_SCHEMA = {
  type: 'object',
  properties: {
    simulatedResponse: {
      type: 'string',
      description: 'The complete simulated interaction — what Claude would say/do, including assumed user responses at PROMPT stops'
    },
    stepsFollowed: {
      type: 'array',
      items: { type: 'string' },
      description: 'Procedure steps followed, in order (e.g. "Step 1: Read current state")'
    },
    fileChanges: {
      type: 'array',
      items: { type: 'string' },
      description: 'File modifications that would be made (e.g. "QUEUE.md: removed 3 captures")'
    },
    uncertainties: {
      type: 'array',
      items: { type: 'string' },
      description: 'Places where the docs were unclear or ambiguous'
    }
  },
  required: ['simulatedResponse', 'stepsFollowed', 'fileChanges', 'uncertainties'],
  additionalProperties: false
}

const VERIFY_SCHEMA = {
  type: 'object',
  properties: {
    phase: { type: 'string' },
    overallScore: { type: 'number', description: '0-10 procedure compliance score' },
    correct: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          aspect: { type: 'string' },
          detail: { type: 'string' }
        },
        required: ['aspect', 'detail']
      }
    },
    deviations: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          aspect: { type: 'string' },
          expected: { type: 'string' },
          actual: { type: 'string' },
          severity: { type: 'string', enum: ['minor', 'major'] }
        },
        required: ['aspect', 'expected', 'actual', 'severity']
      }
    },
    docGaps: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          description: { type: 'string' },
          whichDoc: { type: 'string' }
        },
        required: ['description', 'whichDoc']
      }
    },
    confusions: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          description: { type: 'string' },
          cause: { type: 'string' }
        },
        required: ['description', 'cause']
      }
    }
  },
  required: ['phase', 'overallScore', 'correct', 'deviations', 'docGaps', 'confusions'],
  additionalProperties: false
}

const ANSWERS_SCHEMA = {
  type: 'object',
  properties: {
    answers: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          question: { type: 'string' },
          answer: { type: 'string' },
          confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
          docsUsed: { type: 'array', items: { type: 'string' }, description: 'Which doc sections informed this answer' }
        },
        required: ['question', 'answer', 'confidence', 'docsUsed']
      }
    }
  },
  required: ['answers'],
  additionalProperties: false
}

const SCORE_SCHEMA = {
  type: 'object',
  properties: {
    scores: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          question: { type: 'string' },
          answerCorrect: { type: 'boolean' },
          answerComplete: { type: 'boolean' },
          docsCoverage: { type: 'string', enum: ['fully-covered', 'partially-covered', 'not-covered'] },
          gaps: { type: 'string', description: 'What the docs are missing or could explain better' }
        },
        required: ['question', 'answerCorrect', 'answerComplete', 'docsCoverage', 'gaps']
      }
    }
  },
  required: ['scores'],
  additionalProperties: false
}

const SYNTHESIS_SCHEMA = {
  type: 'object',
  properties: {
    faqFindings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          question: { type: 'string', description: 'A question users would naturally ask' },
          suggestedAnswer: { type: 'string', description: 'The answer based on current docs' },
          sourcePhase: { type: 'string' },
          confidence: { type: 'string', enum: ['high', 'medium', 'low'] }
        },
        required: ['question', 'suggestedAnswer', 'sourcePhase', 'confidence']
      }
    },
    otherFindings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          title: { type: 'string' },
          description: { type: 'string' },
          category: { type: 'string', enum: ['doc-gap', 'procedure-bug', 'clarity-issue', 'missing-example', 'tone-issue'] },
          sourcePhase: { type: 'string' }
        },
        required: ['title', 'description', 'category', 'sourcePhase']
      }
    }
  },
  required: ['faqFindings', 'otherFindings'],
  additionalProperties: false
}

// ── Prompt builders ──

function projectState(includeBuild) {
  let state = `Here is the current state of the project files:

--- SPEC.md ---
${FAKE_SPEC}

--- QUEUE.md ---
${FAKE_QUEUE}

--- LOG/log.md ---
${FAKE_LOG}`

  if (includeBuild) {
    state += `

--- _build.md ---
${FAKE_BUILD}`
  }

  return state
}

function simPrompt(phase) {
  return `You are a fresh instance of Claude. The Throughliner plugin is installed in this session. You are working on a personal bookshelf tracker app for a non-coder user.

USE ONLY THE DOCS PROVIDED. Do not rely on any prior knowledge of the Throughliner plugin.

STEP 1 — Read the plugin docs. These are the docs you would receive in a real session:

A) Read the file at ${TEMPLATE}
   This is the project's CLAUDE.md (scaffolded by the plugin).

B) Read the file at ${BEHAVIOUR}
   These are the behaviour rules, loaded by the session_start hook.

C) Read the file at ${phase.procedureFile}
   This is the procedure doc for the skill the user just invoked.

The session_start hook also output:
${phase.sessionStart}

STEP 2 — Here is the project state:

--- Project CLAUDE.md (what the user sees) ---
${FAKE_CLAUDE_MD}

${phase.projectState}

STEP 3 — Simulate the interaction.

SCENARIO: ${phase.scenario}

Walk through the procedure doc step by step. For each step:
1. Name which step you are executing (e.g. "Step 1: Pre-flight checks")
2. Write the exact message you would show the user
3. Describe any file changes you would make
4. At [PROMPT] stops: show what you'd say, then assume the user gives a reasonable response (accepts recommendations, says "yes" to confirmations, gives pass/fail on tests) and continue
5. At [SEQUENCE] steps: process each item one at a time, clearly marking transitions
6. At [SILENT] steps: just describe the actions, don't narrate

If something in the docs is unclear, ambiguous, or seems to be missing, note it explicitly in your uncertainties.

Be thorough. Follow every step. The goal is to test whether these docs are clear enough for a fresh Claude to follow correctly.`
}

function verifyPrompt(simResult, phase) {
  return `You are a procedure auditor. Your job is to determine whether a simulated plugin session followed its procedure doc correctly.

Read the procedure doc at: ${phase.procedureFile}
Also read the behaviour rules at: ${BEHAVIOUR}

Here is what a fresh Claude produced when simulating a /${phase.name} session on a bookshelf tracker project. It was given the procedure doc, the behaviour rules, and the project state shown below.

SIMULATION OUTPUT:
${JSON.stringify(simResult, null, 2)}

PROJECT STATE:
${phase.projectState}

AUDIT CRITERIA — score each:

1. STEP COMPLIANCE: Did it follow each procedure step in the correct order? Were any steps skipped, reordered, or invented?
2. TAG COMPLIANCE: Did it respect response-shape tags ([SILENT], [BRIEF], [PROMPT], [SEQUENCE], [DISCUSS])? Check: was [SILENT] work narrated? Were [PROMPT] stops skipped? Were [SEQUENCE] items bundled?
3. DOC ROUTING: Did it route information to the correct project docs (SPEC.md, QUEUE.md, LOG/)?
4. RULE ADHERENCE: Did it follow the Rules section at the bottom of the procedure doc?
5. TONE AND STYLE: Was communication plain, direct, and non-jargon (per behaviour rules)?

For each criterion, note what was correct and what deviated. Rate deviations as:
- "minor" — stylistic or non-harmful; wouldn't confuse the user or break the workflow
- "major" — wrong action, skipped critical step, wrong file modified, would break the workflow

Also identify:
- DOC GAPS: places where the procedure doc was unclear, incomplete, or missing information the simulation needed
- CONFUSIONS: places where the simulation misunderstood something — what specifically caused it?

Be strict. The goal is to find doc improvements, not to be generous.`
}

const USER_QUESTIONS = [
  "What's the difference between the Captures section and the Batches section in QUEUE.md?",
  "I closed the app in the middle of a build. What happens when I reopen it?",
  "I noticed a problem in something I built last week, but I'm in the middle of a different build right now. What should I do?",
  "I just had an idea for a feature. How do I record it without losing my train of thought?",
  "The queue is empty. Does that mean the project is done?"
]

function answererPrompt() {
  return `You are a fresh instance of Claude. The Throughliner plugin is installed. A non-coder user is asking you questions about how the plugin workflow works.

USE ONLY THE DOCS PROVIDED. Do not rely on any prior knowledge of the Throughliner plugin.

Read these docs first:
1. ${TEMPLATE} — the project CLAUDE.md template
2. ${BEHAVIOUR} — behaviour rules
3. ${PLAN_DOC} — /plan procedure
4. ${NEXT_DOC} — /next procedure
5. ${DONE_DOC} — /done procedure

The user also has this project CLAUDE.md:
${FAKE_CLAUDE_MD}

Now answer each question using ONLY what you learned from those docs. For each answer, note which doc sections you drew from and your confidence level (high = docs clearly answer it, medium = docs partially cover it and you inferred the rest, low = docs don't really cover this).

Questions:
${USER_QUESTIONS.map(function(q, i) { return (i + 1) + '. ' + q }).join('\n')}`
}

function scorerPrompt(answers) {
  return `You are an evaluator checking whether a set of answers about the Throughliner plugin are correct and complete.

Read the authoritative docs:
1. ${TEMPLATE} — CLAUDE.md template
2. ${BEHAVIOUR} — behaviour rules
3. ${PLAN_DOC} — /plan procedure
4. ${NEXT_DOC} — /next procedure
5. ${DONE_DOC} — /done procedure

Here are the answers a fresh Claude gave to 5 user questions, based only on these docs:

${JSON.stringify(answers, null, 2)}

For each answer, evaluate:
1. CORRECT — is the answer factually accurate per the docs?
2. COMPLETE — does it cover everything the user would need to know?
3. DOCS COVERAGE — is this question fully-covered, partially-covered, or not-covered by the current docs?
4. GAPS — if the docs don't fully cover this, what specific information is missing or could be explained better?

Be strict. A "partially-covered" answer means the docs have some relevant info but the reader has to connect dots or infer. "Not-covered" means the docs don't address this at all.`
}

function synthesisPrompt(allFindings) {
  return `You are categorizing findings from a reader-test of the Throughliner plugin docs. The test simulated three skill sessions (/plan, /next, /done) and a questions panel against a fake bookshelf tracker project.

Here are all the findings:

SKILL SIMULATION VERIFICATIONS:
${JSON.stringify(allFindings.skillVerifications, null, 2)}

QUESTION SCORES:
${JSON.stringify(allFindings.questionScores, null, 2)}

Split ALL findings into two categories:

1. FAQ FINDINGS — things that should become entries in a user-facing FAQ or reference doc. These include:
   - Questions users would naturally ask (from the questions panel and from confusions in simulations)
   - Common misunderstandings revealed by the simulations
   - Workflow concepts that need plain-English explanation
   For each, write a suggested question and answer in plain, non-technical language.

2. OTHER FINDINGS — everything else. These include:
   - Doc gaps (missing information in procedure docs)
   - Procedure bugs (steps that don't work as described)
   - Clarity issues (wording that's confusing or ambiguous)
   - Missing examples (places where an example would help)
   - Tone issues (language that's too technical or alarming)
   For each, give a clear title, description, category, and which phase it came from.

Be thorough. Extract every actionable finding — don't summarize away useful detail. Group related items where it makes sense but don't merge distinct issues.`
}

// ── Skill phases ──

const SKILL_PHASES = [
  {
    name: 'plan',
    procedureFile: PLAN_DOC,
    sessionStart: SESSION_NO_BUILD,
    projectState: projectState(false),
    scenario: 'The user invokes /plan with no additional context. There are 3 items in the Captures section and 2 existing batches. Process the accumulated captures per the procedure.'
  },
  {
    name: 'next',
    procedureFile: NEXT_DOC,
    sessionStart: SESSION_NO_BUILD,
    projectState: projectState(false),
    scenario: 'The user invokes /next. There is no active build (_build.md does not exist). The top batch in QUEUE.md is "Search and filter." Walk through the full procedure from pre-flight checks through presenting the batch.'
  },
  {
    name: 'done',
    procedureFile: DONE_DOC,
    sessionStart: SESSION_ACTIVE_BUILD,
    projectState: projectState(true),
    scenario: 'The user invokes /done. The "Search and filter" build just completed — all items in _build.md are ticked. Walk through the full build close-out: tests, log entry, commit flow, and handoff.'
  }
]

// ── Execute ──

log('Starting reader test: 3 skill simulations + questions panel')

const [skillResults, questionsScored] = await parallel([
  () => pipeline(
    SKILL_PHASES,
    function(p) {
      return agent(simPrompt(p), {
        label: 'sim:' + p.name,
        phase: 'Simulate',
        schema: SIM_SCHEMA
      })
    },
    function(sim, p) {
      return agent(verifyPrompt(sim, p), {
        label: 'verify:' + p.name,
        phase: 'Verify',
        schema: VERIFY_SCHEMA
      })
    }
  ),
  async function() {
    const answers = await agent(answererPrompt(), {
      label: 'q:answer',
      phase: 'Questions',
      schema: ANSWERS_SCHEMA
    })
    return agent(scorerPrompt(answers), {
      label: 'q:score',
      phase: 'Questions',
      schema: SCORE_SCHEMA
    })
  }
])

log('All simulations and questions complete. Synthesizing findings.')

phase('Synthesize')

const allFindings = {
  skillVerifications: (skillResults || []).filter(Boolean),
  questionScores: questionsScored
}

const synthesis = await agent(synthesisPrompt(allFindings), {
  label: 'synthesize',
  schema: SYNTHESIS_SCHEMA
})

log('Synthesis complete: ' + synthesis.faqFindings.length + ' FAQ findings, ' + synthesis.otherFindings.length + ' other findings')

return synthesis
