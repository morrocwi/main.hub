# AGENTS.md - main.hub

You are an AI agent. This repository is the single entry point to the public repositories of the
Human-AI Readout Programme (author: Yaoharee Lahtee). It holds **pointers and edges only**. It
tells you where to go; the repository you arrive at tells you what is true there.

## Protocol (step 0, then five steps, in order)

0. **Lens first - an ordering rule.** Before you commit to a classification, decomposition,
   hypothesis, route or solution, open `ROUTES.md` at **Step 0** and read the files listed under
   "Read first"; each states, in its own repository's words and for its own scope, how input is to
   be read. Then write a short lens note on the raw input, answering what those files ask for, and
   keep it with your work. Naming the problem type ("an equation problem", "a conflict") is recorded
   after the note, not before. Applying this before every route is this hub's routing decision
   (`logbook.jsonl`, D10); what the lens says is defined only in those files.
1. **Pick your intent** in the route table below. Beyond Step 0, do not browse the repositories first.
2. **Open `ROUTES.md` at that route** and read the listed files in the listed order. Every step
   has a commit-pinned raw URL: fetch the file directly, do not clone a whole repository to read
   three files. Stated exceptions: the `equation` route (lookup needs a clone and a build) and any step
   whose `why` warns that the file is large - use `materialize` there, not a truncating fetch. If you need a working tree, run `python scripts/hub.py materialize --dest DIR`
   (partial + sparse clone of exactly the pinned entry files).
3. **Pass the gates named by the route** before you write anything. The gate is defined in the
   target repository, not here; `ROUTES.md` links its definition.
4. **Treat every pin as a readout of one moment.** `graph/lock.yaml` records when it was taken.
   Before relying on a pin for anything that matters, compare it with the live default branch
   (`python scripts/hub.py check --remote --heads`). When the hub and a repository disagree,
   **the repository wins** and the hub is stale - say so, do not paper over it.
5. **Never copy content into this hub.** No equation, theorem statement, claim text or section of
   another repository belongs here. An equation is cited by its Toledo code from the place that
   uses it; this hub only says that Toledo is where to look.

## Route table

<!-- BEGIN GENERATED: routes -->
| If you are about to... | Go to | Gates |
|---|---|---|
| **Anything at all - before you commit to a classification or a route** | [Step 0: Lens first - an ordering rule](ROUTES.md#step-0) | - |
| You need a tool rather than a text: a skill to load, an MCP server, an API, a CLI or a package | [SURFACES.md](SURFACES.md) | - |
| You are about to write, derive, cite or reuse ANY equation, definition or theorem. | [`toledo`](ROUTES.md#equation) | TG-RFG-01 |
| You need to say what an object IS, which domain it belongs to, or how two domains relate. | [`readout_genesis`](ROUTES.md#ontology) | TG-RFG-01 |
| You are about to call something proven, verified, settled, open or hard. | [`readout_universe`](ROUTES.md#claim-strength) | TIER-TAGGING |
| You are about to use a number, limit, continuum object, angle, derivative or operator. | [`information-discrete-math`](ROUTES.md#discrete-math) | TG-RFG-01 |
| You are producing a claim, a paper, a review, or anything that will be released. | [`glosa`](ROUTES.md#write-and-release) | GLOSA-PUBLISH-GATE, TIER-TAGGING |
| You want the root to Standard-Model stream, the universe read out step by step. | [`readout_genesis`](ROUTES.md#universe-step-by-step) | TG-RFG-01, TIER-TAGGING |
| You want the prose map of who holds which role and who calls whom. | [`glosa`](ROUTES.md#map-of-the-programme) | - |
| You are evaluating or installing the birca health-information skill. (A person in an emergency needs emergency services, not a repository.) | [`birca`](ROUTES.md#health) | BIRCA-SAFETY-GATE |
| The task touches the Navier-Stokes readout problem or the finite-bridge programme. | [`readout-problem-navier-stokes`](ROUTES.md#navier-stokes) | TG-RFG-01, TIER-TAGGING |
| The task touches reading a sensor estimate (pose, or anything read out step by step toward a threshold) and asks when it is safe to stop reading and act. | [`task-conditioned-6d-pose-stop`](ROUTES.md#pose-stop) | TIER-TAGGING |
| The task must decide what a system may generate versus what it may present as established, especially when evidence is currently insufficient. | [`dual-lane-epistemic-harness`](ROUTES.md#epistemic-control) | TIER-TAGGING, TG-RFG-01 |
| You are analysing an incident, complaint, conflict, anomaly or decision. | [`skillme`](ROUTES.md#issue-analysis) | - |
<!-- END GENERATED: routes -->

## Which repository answers which question

| Axis | Question | Source of record |
|---|---|---|
| mathematics | Does this object already exist, under which code, at which tier? | `toledo` |
| mathematical-floor | How is this number or operator built as a finite discrete readout? | `information-discrete-math` |
| ontology | What is this object in the one-root picture? | `readout_genesis` |
| epistemology | How strong is this claim, which tier may it carry? | `readout_universe` |
| method | How do a human and an AI produce, check and release it? | `glosa` |

No axis outranks another and none certifies another. Holding an axis means being the place where
that kind of question is answered, nothing more. One card per repository: `nodes/<id>.md`.

## Rules for changing this hub

- One repository is one file: `graph/repos/<id>.yaml` (node, surfaces, outgoing edges). Use
  `python scripts/hub.py add | remove | surfaces` rather than editing by hand where you can. Axes, lens,
  gates and artifacts are in `graph/nodes.yaml`, edge types in `graph/edges.yaml`, routes in
  `graph/routes.yaml`. Edit only those and the hand-written prose files. `ROUTES.md`, `llms.txt`, `nodes/`, `graph/hub.*` and the table above are generated.
- **An edge is admitted only with evidence**: a file in a public repository that contains the
  literal `match` text. The checker re-reads the pinned blob. No evidence, no edge.
- A repository with no verified edge is `class: catalog` - listed for discovery, not claimed to
  be connected. Do not upgrade it by assertion.
- After any edit: `python scripts/hub.py lock --workspace <dir with the clones>`, then `build`,
  then `check --workspace <dir>`. All three must pass before a commit. `SCHEMA.md` has the detail.
- Only public repositories are nodes. Never name, describe or link a non-public repository,
  a local path, a host, a session or an internal ticket. The checker's leak scan enforces this;
  put organisation-specific forbidden names in the untracked file `.leakpatterns.local`.
- Commits carry no tool or vendor attribution trailer (`githooks/commit-msg` rejects them).
- Record what you decided and what you rejected in `logbook.jsonl`, while working.
