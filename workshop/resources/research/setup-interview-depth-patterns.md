# Deep-interview patterns for /setup (research, 2026-07-29)

Filed while designing [setup-interview-depth]. Informs how /setup's interview becomes freer, deeper, and adaptive without overwhelming a non-coder.

## What the search found

**Adaptive, not branching (the AI-interview-agent pattern).** Modern AI interview agents read each answer, reason about what is still uncovered or unexplained, and generate the next question accordingly — explicitly *not* a fixed survey with branching logic. This validates making /setup's five questions an **example bank** Claude draws on rather than a fixed script: the questions asked are generated from what's still unclear, not read off a list.

**Semi-structured is the sweet spot.** Requirements-elicitation guidance splits interviews into structured (fixed questions) vs unstructured (no format). The productive middle is semi-structured: prepared topics/objectives, but questions tailored live to the interviewee's role and expertise. For SI that role is always "non-coder," so tailoring means: no jargon, recommend an answer to each question, one at a time.

**5 Whys gives a stopping condition.** The 5-Whys technique probes beneath surface statements — "when you get an answer to all your Whys, you are done with your interview." This is the concrete answer to the "relentless vs overwhelm" tension: the interview isn't endless, it stops when probing bottoms out into a shared, buildable understanding. The user can also call "enough" at any point.

**Preparation + objectives per topic.** Good elicitation defines the objective of each line of questioning before asking. For /setup that maps to walking the design tree one branch at a time and resolving dependencies between decisions before moving on.

## Design implications taken into [setup-interview-depth]

- Five fixed questions → optional example bank / prompts to draw on.
- Interview is adaptive: reason about what's still unclear, generate the next question, recommend an answer, ask one at a time.
- Stopping rule: probe until a shared buildable understanding is reached (5-Whys "all Whys answered"), not until every branch is exhausted; user can end it anytime with "build from what we have."
- "Explore the codebase instead of asking" → "explore whatever already exists" (non-coders are often greenfield).

## Sources
- [Requirements Elicitation guide (Jama)](https://www.jamasoftware.com/requirements-management-guide/requirements-gathering-and-management-processes/a-guide-to-requirements-elicitation-for-product-teams/)
- [Requirements Elicitation (GeeksforGeeks)](https://www.geeksforgeeks.org/software-engineering/software-engineering-requirements-elicitation/)
- [Interview-Informed Generative Agents for Product Discovery (arXiv/CHI 2026)](https://arxiv.org/html/2603.29890v1)
- [Product Discovery Questions 2026 (Perspective AI)](https://getperspective.ai/blog/product-discovery-questions-2026-what-to-ask-every-stage)
