# Routes

GENERATED from `graph/routes.yaml` by `python scripts/hub.py build` - do not hand-edit.
Every link is pinned to the public commit recorded in `graph/lock.yaml` (2026-09-18).
A pin is a readout of one moment: compare it with the live default branch before relying on it.

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
| You are analysing an incident, complaint, conflict, anomaly or decision. | [`skillme`](ROUTES.md#issue-analysis) | - |

## Step 0

**Lens first - an ordering rule - mandatory, before any route below.** Before you commit to a classification, a decomposition, a hypothesis, a route or a solution, read the files under Read first. Then write a short lens note on the raw input, answering what those files ask for, and keep it with your work.

What the lens says is defined only in the files below. Each line names a file and quotes a phrase that is
checked to occur exactly once in the pinned file; the label before the quote is this hub's paraphrase and is
not machine-verified. Applying the lens before every route is this hub's ordering rule.

**Read first**

1. `readout_universe` / [`plugins/readout-universe/skills/readout-universe/SKILL.md`](https://github.com/morrocwi/readout_universe/blob/1a72ccd13c7a07d10fe519037132fcb44e426084/plugins/readout-universe/skills/readout-universe/SKILL.md) - there is no truth-behind-the-claim to read off directly; what you have, when you assert something, is a finite readout (stated there as a stance, tier Dr): "There is no truth-behind-the-claim waiting to be read off directly"  
   raw: <https://raw.githubusercontent.com/morrocwi/readout_universe/1a72ccd13c7a07d10fe519037132fcb44e426084/plugins/readout-universe/skills/readout-universe/SKILL.md>
2. `readout_universe` / [`plugins/readout-universe/skills/readout-universe/SKILL.md`](https://github.com/morrocwi/readout_universe/blob/1a72ccd13c7a07d10fe519037132fcb44e426084/plugins/readout-universe/skills/readout-universe/SKILL.md) - name which kind of readout you have, and never let the label creep stronger than its evidence: "name which kind of readout you have"  
   raw: <https://raw.githubusercontent.com/morrocwi/readout_universe/1a72ccd13c7a07d10fe519037132fcb44e426084/plugins/readout-universe/skills/readout-universe/SKILL.md>
3. `glosa` / [`methodology/P00_lens.md`](https://github.com/morrocwi/glosa/blob/cf1c96a433dda38878ec8a85ca099657d761ec64/methodology/P00_lens.md) - before touching evidence for any claim, translate the problem into the readout vocabulary, analyse there, then translate back (a rule that file marks tier Dr): "never analyse a problem directly in world-language and call the result rigorous"  
   raw: <https://raw.githubusercontent.com/morrocwi/glosa/cf1c96a433dda38878ec8a85ca099657d761ec64/methodology/P00_lens.md>
4. `skillme` / [`plugins/skillme/skills/skillme/SKILL.md`](https://github.com/morrocwi/skillme/blob/208e76dfae692396fbf54ae64119978020275044/plugins/skillme/skills/skillme/SKILL.md) - separate what difference is retained, from what state, under what context/query/resolution: "what difference is retained, from what state"  
   raw: <https://raw.githubusercontent.com/morrocwi/skillme/208e76dfae692396fbf54ae64119978020275044/plugins/skillme/skills/skillme/SKILL.md>

**Also stated in (read the passage around the quoted phrase)**

1. `information-discrete-math` / [`plugins/information-discrete-math/skills/information-discrete-math/SKILL.md`](https://github.com/morrocwi/information-discrete-math/blob/33c54bb2512cf2c129feef928eb64977bb420b57/plugins/information-discrete-math/skills/information-discrete-math/SKILL.md) - everything an agency reads is a finite retained difference - a readout (stated there as a stance, tier Dr): "Everything an agency ever reads is a finite retained difference"  
   raw: <https://raw.githubusercontent.com/morrocwi/information-discrete-math/33c54bb2512cf2c129feef928eb64977bb420b57/plugins/information-discrete-math/skills/information-discrete-math/SKILL.md>
2. `readout_genesis` / [`README.md`](https://github.com/morrocwi/readout_genesis/blob/864bb85950deec943517b102bd33cf8ff101da15/README.md) - readout-not-truth - verified structure is not physical truth, and every claim carries a tier: "Verified structure is not physical truth"  
   raw: <https://raw.githubusercontent.com/morrocwi/readout_genesis/864bb85950deec943517b102bd33cf8ff101da15/README.md>
3. `glosa` / [`plugins/glosa/skills/glosa-blackbox-note/SKILL.md`](https://github.com/morrocwi/glosa/blob/cf1c96a433dda38878ec8a85ca099657d761ec64/plugins/glosa/skills/glosa-blackbox-note/SKILL.md) - every hypothesis statement carries a signature line naming the lens its lens_ref points at: "Every hypothesis statement carries a signature line naming the lens `lens_ref` points at"  
   raw: <https://raw.githubusercontent.com/morrocwi/glosa/cf1c96a433dda38878ec8a85ca099657d761ec64/plugins/glosa/skills/glosa-blackbox-note/SKILL.md>

**Then:** Record the problem type after the lens note, not before, and only then pick a route. If a later step contradicts the note, revise the note in the open.

## equation

**When:** You are about to write, derive, cite or reuse ANY equation, definition or theorem.

1. `toledo` / [`EQUATION_SOURCE_POLICY.md`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/EQUATION_SOURCE_POLICY.md) - the binding order of work  
   raw: <https://raw.githubusercontent.com/morrocwi/toledo/a21d76461a9ca64259e830d5456312e9b1e2e686/EQUATION_SOURCE_POLICY.md>
2. `toledo` / [`README.md`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/README.md) - the lookup surfaces: MCP server (toledo_check, the verdict-aware tool the policy prefers), CLI (find / show / ancestry), static read API for callers that cannot clone, static site, registry files  
   raw: <https://raw.githubusercontent.com/morrocwi/toledo/a21d76461a9ca64259e830d5456312e9b1e2e686/README.md>
3. `toledo` / [`scripts/toledo_build.py`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/scripts/toledo_build.py) - lookup needs a full clone of toledo (the one route where reading three files is not enough): run this build script first, it generates the library the CLI reads  
   raw: <https://raw.githubusercontent.com/morrocwi/toledo/a21d76461a9ca64259e830d5456312e9b1e2e686/scripts/toledo_build.py>
4. `toledo` / [`scripts/toledo`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/scripts/toledo) - then look the object up with the CLI: find / show / ancestry  
   raw: <https://raw.githubusercontent.com/morrocwi/toledo/a21d76461a9ca64259e830d5456312e9b1e2e686/scripts/toledo>
5. `toledo` / [`registry/SCHEMA.md`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/registry/SCHEMA.md) - how a code, parents and tier are read  
   raw: <https://raw.githubusercontent.com/morrocwi/toledo/a21d76461a9ca64259e830d5456312e9b1e2e686/registry/SCHEMA.md>
6. `toledo` / [`registry/CANONICAL.json`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/registry/CANONICAL.json) - fallback only: the full registry is several megabytes, fetch it when a clone and build are not possible  
   raw: <https://raw.githubusercontent.com/morrocwi/toledo/a21d76461a9ca64259e830d5456312e9b1e2e686/registry/CANONICAL.json>

**Gates:** TG-RFG-01

**Then:** Usable match (read the statement, a keyword hit is not a match): cite its code, reuse its statement. Ambiguous, superseded or conflicting: HOLD, do not guess. Not found: check Genesis compatibility, derive only the missing piece, label it PROPOSAL.

## ontology

**When:** You need to say what an object IS, which domain it belongs to, or how two domains relate.

1. `readout_genesis` / [`AGENTS.md`](https://github.com/morrocwi/readout_genesis/blob/864bb85950deec943517b102bd33cf8ff101da15/AGENTS.md) - what Genesis may and may not decide  
   raw: <https://raw.githubusercontent.com/morrocwi/readout_genesis/864bb85950deec943517b102bd33cf8ff101da15/AGENTS.md>
2. `readout_genesis` / [`README.md`](https://github.com/morrocwi/readout_genesis/blob/864bb85950deec943517b102bd33cf8ff101da15/README.md) - knowledge-graph map of the canon  
   raw: <https://raw.githubusercontent.com/morrocwi/readout_genesis/864bb85950deec943517b102bd33cf8ff101da15/README.md>
3. `readout_genesis` / [`READOUT_GENESIS_CORE.md`](https://github.com/morrocwi/readout_genesis/blob/864bb85950deec943517b102bd33cf8ff101da15/READOUT_GENESIS_CORE.md) - the canon; contains its own reading order for a fresh session  
   raw: <https://raw.githubusercontent.com/morrocwi/readout_genesis/864bb85950deec943517b102bd33cf8ff101da15/READOUT_GENESIS_CORE.md>

**Gates:** TG-RFG-01

**Then:** State the gate / section the object instantiates; theorem status still comes from Toledo.

## claim-strength

**When:** You are about to call something proven, verified, settled, open or hard.

1. `readout_universe` / [`README.md`](https://github.com/morrocwi/readout_universe/blob/1a72ccd13c7a07d10fe519037132fcb44e426084/README.md) - the tier vocabulary  
   raw: <https://raw.githubusercontent.com/morrocwi/readout_universe/1a72ccd13c7a07d10fe519037132fcb44e426084/README.md>
2. `readout_universe` / [`claims.md`](https://github.com/morrocwi/readout_universe/blob/1a72ccd13c7a07d10fe519037132fcb44e426084/claims.md) - how a claims register is kept  
   raw: <https://raw.githubusercontent.com/morrocwi/readout_universe/1a72ccd13c7a07d10fe519037132fcb44e426084/claims.md>
3. `readout_universe` / [`plugins/readout-universe/skills/readout-universe/SKILL.md`](https://github.com/morrocwi/readout_universe/blob/1a72ccd13c7a07d10fe519037132fcb44e426084/plugins/readout-universe/skills/readout-universe/SKILL.md) - the operational tier-tagging discipline, where the gate is defined  
   raw: <https://raw.githubusercontent.com/morrocwi/readout_universe/1a72ccd13c7a07d10fe519037132fcb44e426084/plugins/readout-universe/skills/readout-universe/SKILL.md>
4. `readout_universe` / [`scope_correction.md`](https://github.com/morrocwi/readout_universe/blob/1a72ccd13c7a07d10fe519037132fcb44e426084/scope_correction.md) - worked example: a proposed (not applied) correction that brings an overstated pull-request title down to what the file actually shows  
   raw: <https://raw.githubusercontent.com/morrocwi/readout_universe/1a72ccd13c7a07d10fe519037132fcb44e426084/scope_correction.md>

**Gates:** TIER-TAGGING

**Then:** Tag the claim with the tier that matches what was actually checked, never higher.

## discrete-math

**When:** You are about to use a number, limit, continuum object, angle, derivative or operator.

1. `information-discrete-math` / [`AI_START_HERE.md`](https://github.com/morrocwi/information-discrete-math/blob/33c54bb2512cf2c129feef928eb64977bb420b57/AI_START_HERE.md) - shortest orientation  
   raw: <https://raw.githubusercontent.com/morrocwi/information-discrete-math/33c54bb2512cf2c129feef928eb64977bb420b57/AI_START_HERE.md>
2. `information-discrete-math` / [`plugins/information-discrete-math/skills/information-discrete-math/SKILL.md`](https://github.com/morrocwi/information-discrete-math/blob/33c54bb2512cf2c129feef928eb64977bb420b57/plugins/information-discrete-math/skills/information-discrete-math/SKILL.md) - the operational floor: contaminated-concept table, pre-write checklist, number ladder  
   raw: <https://raw.githubusercontent.com/morrocwi/information-discrete-math/33c54bb2512cf2c129feef928eb64977bb420b57/plugins/information-discrete-math/skills/information-discrete-math/SKILL.md>
3. `information-discrete-math` / [`llms.txt`](https://github.com/morrocwi/information-discrete-math/blob/33c54bb2512cf2c129feef928eb64977bb420b57/llms.txt) - file map for agents  
   raw: <https://raw.githubusercontent.com/morrocwi/information-discrete-math/33c54bb2512cf2c129feef928eb64977bb420b57/llms.txt>
4. `information-discrete-math` / [`docs/TOLEDO_CODES.md`](https://github.com/morrocwi/information-discrete-math/blob/33c54bb2512cf2c129feef928eb64977bb420b57/docs/TOLEDO_CODES.md) - which Toledo codes this repository carries  
   raw: <https://raw.githubusercontent.com/morrocwi/information-discrete-math/33c54bb2512cf2c129feef928eb64977bb420b57/docs/TOLEDO_CODES.md>

**Gates:** TG-RFG-01

**Then:** Work on the discrete floor; equation codes are still looked up in Toledo.

## write-and-release

**When:** You are producing a claim, a paper, a review, or anything that will be released.

1. `glosa` / [`llms.txt`](https://github.com/morrocwi/glosa/blob/cf1c96a433dda38878ec8a85ca099657d761ec64/llms.txt) - file map for agents  
   raw: <https://raw.githubusercontent.com/morrocwi/glosa/cf1c96a433dda38878ec8a85ca099657d761ec64/llms.txt>
2. `glosa` / [`plugins/glosa/skills/glosa/SKILL.md`](https://github.com/morrocwi/glosa/blob/cf1c96a433dda38878ec8a85ca099657d761ec64/plugins/glosa/skills/glosa/SKILL.md) - master entry point of the method  
   raw: <https://raw.githubusercontent.com/morrocwi/glosa/cf1c96a433dda38878ec8a85ca099657d761ec64/plugins/glosa/skills/glosa/SKILL.md>
3. `glosa` / [`plugins/glosa/skills/glosa-publish-gate/SKILL.md`](https://github.com/morrocwi/glosa/blob/cf1c96a433dda38878ec8a85ca099657d761ec64/plugins/glosa/skills/glosa-publish-gate/SKILL.md) - the release gate as a skill (a pointer)  
   raw: <https://raw.githubusercontent.com/morrocwi/glosa/cf1c96a433dda38878ec8a85ca099657d761ec64/plugins/glosa/skills/glosa-publish-gate/SKILL.md>
4. `glosa` / [`methodology/P10_publish_gate.md`](https://github.com/morrocwi/glosa/blob/cf1c96a433dda38878ec8a85ca099657d761ec64/methodology/P10_publish_gate.md) - the full text of the gate the skill points to  
   raw: <https://raw.githubusercontent.com/morrocwi/glosa/cf1c96a433dda38878ec8a85ca099657d761ec64/methodology/P10_publish_gate.md>

**Gates:** GLOSA-PUBLISH-GATE, TIER-TAGGING

**Then:** Maker is not checker: obtain an independent check before release.

## universe-step-by-step

**When:** You want the root to Standard-Model stream, the universe read out step by step.

1. `readout_genesis` / [`READOUT_GENESIS_CORE.md`](https://github.com/morrocwi/readout_genesis/blob/864bb85950deec943517b102bd33cf8ff101da15/READOUT_GENESIS_CORE.md) - source of truth for the stream: the LAST appendix lettered C, titled APPENDIX C (SM DOMAIN EQUATION STREAM ...), near the end of a file of about half a megabyte - use materialize, not a truncating fetch; an earlier Appendix C (reading order) is a different section  
   raw: <https://raw.githubusercontent.com/morrocwi/readout_genesis/864bb85950deec943517b102bd33cf8ff101da15/READOUT_GENESIS_CORE.md>
2. `toledo` / [`registry/genesis_root.json`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/registry/genesis_root.json) - the root codes every other code descends from  
   raw: <https://raw.githubusercontent.com/morrocwi/toledo/a21d76461a9ca64259e830d5456312e9b1e2e686/registry/genesis_root.json>
3. `readout_universe` / [`EQUATION_LIBRARY_ROOT_TO_SM_STREAM_solver_arc_private.md`](https://github.com/morrocwi/readout_universe/blob/1a72ccd13c7a07d10fe519037132fcb44e426084/EQUATION_LIBRARY_ROOT_TO_SM_STREAM_solver_arc_private.md) - synced mirror; on mismatch the source of truth wins  
   raw: <https://raw.githubusercontent.com/morrocwi/readout_universe/1a72ccd13c7a07d10fe519037132fcb44e426084/EQUATION_LIBRARY_ROOT_TO_SM_STREAM_solver_arc_private.md>

**Gates:** TG-RFG-01, TIER-TAGGING

**Then:** Cite stream items by Toledo code and carry the tier the source states.

## map-of-the-programme

**When:** You want the prose map of who holds which role and who calls whom.

1. `glosa` / [`docs/ECOSYSTEM.md`](https://github.com/morrocwi/glosa/blob/cf1c96a433dda38878ec8a85ca099657d761ec64/docs/ECOSYSTEM.md) - the earlier prose map this hub descends from  
   raw: <https://raw.githubusercontent.com/morrocwi/glosa/cf1c96a433dda38878ec8a85ca099657d761ec64/docs/ECOSYSTEM.md>

**Gates:** none

**Then:** Use this hub for pinned, machine-checked routing; use that document for narrative.

## health

**When:** You are evaluating or installing the birca health-information skill. (A person in an emergency needs emergency services, not a repository.)

1. `birca` / [`README.md`](https://github.com/morrocwi/birca/blob/225c3f57bd9972cab0d01e42f55517352b490a61/README.md) - what has and has not been validated; which safety audits are still open  
   raw: <https://raw.githubusercontent.com/morrocwi/birca/225c3f57bd9972cab0d01e42f55517352b490a61/README.md>
2. `birca` / [`LEGAL_DISCLAIMER.md`](https://github.com/morrocwi/birca/blob/225c3f57bd9972cab0d01e42f55517352b490a61/LEGAL_DISCLAIMER.md) - scope, prohibited uses, the disclaimer that must ship unmodified, the deployer's own legal-review duty, liability  
   raw: <https://raw.githubusercontent.com/morrocwi/birca/225c3f57bd9972cab0d01e42f55517352b490a61/LEGAL_DISCLAIMER.md>
3. `birca` / [`SKILL.md`](https://github.com/morrocwi/birca/blob/225c3f57bd9972cab0d01e42f55517352b490a61/SKILL.md) - the fixed layer order; the immediate safety gate precedes any interpretation  
   raw: <https://raw.githubusercontent.com/morrocwi/birca/225c3f57bd9972cab0d01e42f55517352b490a61/SKILL.md>
4. `birca` / [`SYSTEM_PROMPT.md`](https://github.com/morrocwi/birca/blob/225c3f57bd9972cab0d01e42f55517352b490a61/SYSTEM_PROMPT.md) - the instruction set the skill itself names as its single source of truth; holds the rule not to delay the safety screen with extensive history-taking  
   raw: <https://raw.githubusercontent.com/morrocwi/birca/225c3f57bd9972cab0d01e42f55517352b490a61/SYSTEM_PROMPT.md>

**Gates:** BIRCA-SAFETY-GATE

**Then:** The emergency screen precedes any interpretation and cannot be skipped. Educational and research use only; never diagnostic, never treatment selection; the repository states its clinical-safety audit is still open.

## navier-stokes

**When:** The task touches the Navier-Stokes readout problem or the finite-bridge programme.

1. `readout-problem-navier-stokes` / [`AGENTS.md`](https://github.com/morrocwi/readout-problem-navier-stokes/blob/82262e19c85eebaafba3bc8391e8ac953aa2f704/AGENTS.md) - the mandatory reading order and the non-negotiable rules  
   raw: <https://raw.githubusercontent.com/morrocwi/readout-problem-navier-stokes/82262e19c85eebaafba3bc8391e8ac953aa2f704/AGENTS.md>
2. `readout-problem-navier-stokes` / [`CLAY_READ_FIRST.md`](https://github.com/morrocwi/readout-problem-navier-stokes/blob/82262e19c85eebaafba3bc8391e8ac953aa2f704/CLAY_READ_FIRST.md) - first item of that reading order  
   raw: <https://raw.githubusercontent.com/morrocwi/readout-problem-navier-stokes/82262e19c85eebaafba3bc8391e8ac953aa2f704/CLAY_READ_FIRST.md>
3. `readout-problem-navier-stokes` / [`CLAY_MULTI_PROBLEM_FINITE_BRIDGE_PROGRAM.md`](https://github.com/morrocwi/readout-problem-navier-stokes/blob/82262e19c85eebaafba3bc8391e8ac953aa2f704/CLAY_MULTI_PROBLEM_FINITE_BRIDGE_PROGRAM.md) - second item of that order  
   raw: <https://raw.githubusercontent.com/morrocwi/readout-problem-navier-stokes/82262e19c85eebaafba3bc8391e8ac953aa2f704/CLAY_MULTI_PROBLEM_FINITE_BRIDGE_PROGRAM.md>
4. `readout-problem-navier-stokes` / [`CLAY_RESEARCH_TODO.md`](https://github.com/morrocwi/readout-problem-navier-stokes/blob/82262e19c85eebaafba3bc8391e8ac953aa2f704/CLAY_RESEARCH_TODO.md) - third item of that order  
   raw: <https://raw.githubusercontent.com/morrocwi/readout-problem-navier-stokes/82262e19c85eebaafba3bc8391e8ac953aa2f704/CLAY_RESEARCH_TODO.md>
5. `readout-problem-navier-stokes` / [`CLAIMS.md`](https://github.com/morrocwi/readout-problem-navier-stokes/blob/82262e19c85eebaafba3bc8391e8ac953aa2f704/CLAIMS.md) - fourth item: what is and is not claimed  
   raw: <https://raw.githubusercontent.com/morrocwi/readout-problem-navier-stokes/82262e19c85eebaafba3bc8391e8ac953aa2f704/CLAIMS.md>

**Gates:** TG-RFG-01, TIER-TAGGING

**Then:** The Clay problem stays open; never phrase a finite result as a resolution.

## pose-stop

**When:** The task touches reading a sensor estimate (pose, or anything read out step by step toward a threshold) and asks when it is safe to stop reading and act.

1. `task-conditioned-6d-pose-stop` / [`README.md`](https://github.com/morrocwi/task-conditioned-6d-pose-stop/blob/176881a6476d28da18177c6638c982e50370776a/README.md) - the ACT / CONTINUE / HOLD rule and the certificate-hitting-time distinction from a bare pose estimate  
   raw: <https://raw.githubusercontent.com/morrocwi/task-conditioned-6d-pose-stop/176881a6476d28da18177c6638c982e50370776a/README.md>
2. `task-conditioned-6d-pose-stop` / [`CLAIMS.md`](https://github.com/morrocwi/task-conditioned-6d-pose-stop/blob/176881a6476d28da18177c6638c982e50370776a/CLAIMS.md) - which of its own claims are supported, refuted or still open - several real-sensor claims here are refuted  
   raw: <https://raw.githubusercontent.com/morrocwi/task-conditioned-6d-pose-stop/176881a6476d28da18177c6638c982e50370776a/CLAIMS.md>
3. `task-conditioned-6d-pose-stop` / [`RESEARCH_QUESTION.md`](https://github.com/morrocwi/task-conditioned-6d-pose-stop/blob/176881a6476d28da18177c6638c982e50370776a/RESEARCH_QUESTION.md) - the single testable question, and the falsifiers that would settle it  
   raw: <https://raw.githubusercontent.com/morrocwi/task-conditioned-6d-pose-stop/176881a6476d28da18177c6638c982e50370776a/RESEARCH_QUESTION.md>

**Gates:** TIER-TAGGING

**Then:** HOLD when no certificate exists within budget; a terminal HOLD is never relabelled as a certificate. Read CLAIMS.md before repeating any of this repository's own numbers as settled.

## issue-analysis

**When:** You are analysing an incident, complaint, conflict, anomaly or decision.

1. `skillme` / [`AI_START_HERE.md`](https://github.com/morrocwi/skillme/blob/208e76dfae692396fbf54ae64119978020275044/AI_START_HERE.md) - the discovery order  
   raw: <https://raw.githubusercontent.com/morrocwi/skillme/208e76dfae692396fbf54ae64119978020275044/AI_START_HERE.md>
2. `skillme` / [`plugins/skillme/skills/skillme/SKILL.md`](https://github.com/morrocwi/skillme/blob/208e76dfae692396fbf54ae64119978020275044/plugins/skillme/skills/skillme/SKILL.md) - the operational protocol: two-question intake gate, moves in order, hard invariants  
   raw: <https://raw.githubusercontent.com/morrocwi/skillme/208e76dfae692396fbf54ae64119978020275044/plugins/skillme/skills/skillme/SKILL.md>

**Gates:** none

**Then:** Do not name a cause before a finite retained difference has been found.

## Gates

- **TG-RFG-01** - Toledo-Genesis reuse-first gate: Toledo lookup, Genesis compatibility, reuse the existing object, derive only the missing piece, mark PROPOSAL. Defined in `toledo` / [`EQUATION_SOURCE_POLICY.md`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/EQUATION_SOURCE_POLICY.md).
- **TIER-TAGGING** - Evidence-tier tagging: A claim's stated strength never exceeds what was actually checked, measured or declared. Defined in `readout_universe` / [`plugins/readout-universe/skills/readout-universe/SKILL.md`](https://github.com/morrocwi/readout_universe/blob/1a72ccd13c7a07d10fe519037132fcb44e426084/plugins/readout-universe/skills/readout-universe/SKILL.md).
- **GLOSA-PUBLISH-GATE** - glosa publish gate: Release gate with leak scan and knowledge-state semantics; maker is not checker. Defined in `glosa` / [`methodology/P10_publish_gate.md`](https://github.com/morrocwi/glosa/blob/cf1c96a433dda38878ec8a85ca099657d761ec64/methodology/P10_publish_gate.md).
- **BIRCA-SAFETY-GATE** - birca immediate safety gate: An emergency and red-flag screen runs before any interpretation, cannot be skipped by user request or claimed consent; unknown safety status counts as unresolved; the skill's system prompt adds that it must not be delayed by extensive history-taking. The skill is not a substitute for emergency services or a clinician. Defined in `birca` / [`SKILL.md`](https://github.com/morrocwi/birca/blob/225c3f57bd9972cab0d01e42f55517352b490a61/SKILL.md).
