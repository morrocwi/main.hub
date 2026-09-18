# Surfaces

GENERATED from `graph/repos/` by `python scripts/hub.py build` - do not hand-edit.
Callable and loadable things the public repositories already ship. Every entry is a pinned file in its
repository; plugin and marketplace names are checked against the pinned marketplace manifest. The hub ships
none of these itself: install and run them from their own repository, under that repository's licence and rules.
Apply Step 0 (`ROUTES.md`) and the gates of your route before using any of them.

## Installable plugins (skill bundles)

- **glosa plugin** (`glosa`) - Installs the glosa method skills. File: [`.claude-plugin/marketplace.json`](https://github.com/morrocwi/glosa/blob/106acb3ee985f91511a61f31840e046fb1e76034/.claude-plugin/marketplace.json). Gates: GLOSA-PUBLISH-GATE
  install: `/plugin marketplace add morrocwi/glosa` then `/plugin install glosa@yaoharee-lahtee-glosa` (or as that repository's README states; a plugin installs from the ref its manifest names, which can differ from the file pinned here)
- **information-discrete-math plugin** (`information-discrete-math`) - Installs the discrete-math skill. File: [`.claude-plugin/marketplace.json`](https://github.com/morrocwi/information-discrete-math/blob/e4932afee144484759f0f3275e69fc923b80d091/.claude-plugin/marketplace.json). Gates: TG-RFG-01
  install: `/plugin marketplace add morrocwi/information-discrete-math` then `/plugin install information-discrete-math@yaoharee-lahtee-math` (or as that repository's README states; a plugin installs from the ref its manifest names, which can differ from the file pinned here)
- **readout-universe plugin** (`readout_universe`) - Installs the evidence-tier tagging skill. File: [`.claude-plugin/marketplace.json`](https://github.com/morrocwi/readout_universe/blob/68863dfefc32cdbc4d97871633e36aec3c8b8018/.claude-plugin/marketplace.json). Gates: TIER-TAGGING
  install: `/plugin marketplace add morrocwi/readout_universe` then `/plugin install readout-universe@yaoharee-lahtee-readout` (or as that repository's README states; a plugin installs from the ref its manifest names, which can differ from the file pinned here)
- **skillme plugin** (`skillme`) - Installs the issue-analysis skill. File: [`.claude-plugin/marketplace.json`](https://github.com/morrocwi/skillme/blob/232cc8d2025cdec64cc77ad8ec2fceb17639f0e0/.claude-plugin/marketplace.json)
  install: `/plugin marketplace add morrocwi/skillme` then `/plugin install skillme@yaoharee-lahtee-skillme` (or as that repository's README states; a plugin installs from the ref its manifest names, which can differ from the file pinned here)
- **seth plugin** (`seth-skill`) - Installs the social-enterprise analysis skill. File: [`.claude-plugin/marketplace.json`](https://github.com/morrocwi/seth-skill/blob/4e8e9e7708078aec672304f46c99b946e13fc43c/.claude-plugin/marketplace.json)
  install: `/plugin marketplace add morrocwi/seth-skill` then `/plugin install seth@yaoharee-lahtee-seth` (or as that repository's README states; a plugin installs from the ref its manifest names, which can differ from the file pinned here)

## Skill files (plain Markdown, any agent can read them)

- **glosa master skill** (`glosa`) - Entry point to the method skills - claim card, blackbox note, independent check, literature review, publish gate, project advisor. File: [`plugins/glosa/skills/glosa/SKILL.md`](https://github.com/morrocwi/glosa/blob/106acb3ee985f91511a61f31840e046fb1e76034/plugins/glosa/skills/glosa/SKILL.md). Gates: GLOSA-PUBLISH-GATE
- **glosa-blackbox-note skill** (`glosa`) - Blackbox note - verbatim dialogue lines, cooking log, lens_used block, hypothesis signature. File: [`plugins/glosa/skills/glosa-blackbox-note/SKILL.md`](https://github.com/morrocwi/glosa/blob/106acb3ee985f91511a61f31840e046fb1e76034/plugins/glosa/skills/glosa-blackbox-note/SKILL.md). Gates: GLOSA-PUBLISH-GATE
- **glosa-claim-card skill** (`glosa`) - Five-questions claim card (stub or full). File: [`plugins/glosa/skills/glosa-claim-card/SKILL.md`](https://github.com/morrocwi/glosa/blob/106acb3ee985f91511a61f31840e046fb1e76034/plugins/glosa/skills/glosa-claim-card/SKILL.md). Gates: GLOSA-PUBLISH-GATE
- **glosa-deliver skill** (`glosa`) - Delivery skill of the glosa method; read the file for its scope. File: [`plugins/glosa/skills/glosa-deliver/SKILL.md`](https://github.com/morrocwi/glosa/blob/106acb3ee985f91511a61f31840e046fb1e76034/plugins/glosa/skills/glosa-deliver/SKILL.md). Gates: GLOSA-PUBLISH-GATE
- **glosa-independent-check skill** (`glosa`) - Independent check - maker, checker and approver kept separate; independence ladder. File: [`plugins/glosa/skills/glosa-independent-check/SKILL.md`](https://github.com/morrocwi/glosa/blob/106acb3ee985f91511a61f31840e046fb1e76034/plugins/glosa/skills/glosa-independent-check/SKILL.md). Gates: GLOSA-PUBLISH-GATE
- **glosa-literature-review skill** (`glosa`) - Literature review in six stages with two exit gates. File: [`plugins/glosa/skills/glosa-literature-review/SKILL.md`](https://github.com/morrocwi/glosa/blob/106acb3ee985f91511a61f31840e046fb1e76034/plugins/glosa/skills/glosa-literature-review/SKILL.md). Gates: GLOSA-PUBLISH-GATE
- **glosa-obsidian skill** (`glosa`) - Obsidian vault skill of the glosa method; read the file for its scope. File: [`plugins/glosa/skills/glosa-obsidian/SKILL.md`](https://github.com/morrocwi/glosa/blob/106acb3ee985f91511a61f31840e046fb1e76034/plugins/glosa/skills/glosa-obsidian/SKILL.md). Gates: GLOSA-PUBLISH-GATE
- **glosa-project-advisor skill** (`glosa`) - Post-release advisor for a project's next conversion step. File: [`plugins/glosa/skills/glosa-project-advisor/SKILL.md`](https://github.com/morrocwi/glosa/blob/106acb3ee985f91511a61f31840e046fb1e76034/plugins/glosa/skills/glosa-project-advisor/SKILL.md). Gates: GLOSA-PUBLISH-GATE
- **glosa-publish-gate skill** (`glosa`) - Publish gate - release rules, leak scan, knowledge-state semantics. File: [`plugins/glosa/skills/glosa-publish-gate/SKILL.md`](https://github.com/morrocwi/glosa/blob/106acb3ee985f91511a61f31840e046fb1e76034/plugins/glosa/skills/glosa-publish-gate/SKILL.md). Gates: GLOSA-PUBLISH-GATE
- **glosa-render skill** (`glosa`) - Rendering skill of the glosa method; read the file for its scope. File: [`plugins/glosa/skills/glosa-render/SKILL.md`](https://github.com/morrocwi/glosa/blob/106acb3ee985f91511a61f31840e046fb1e76034/plugins/glosa/skills/glosa-render/SKILL.md). Gates: GLOSA-PUBLISH-GATE
- **information-discrete-math skill** (`information-discrete-math`) - The operational floor to load before writing mathematics, physics or geometry. File: [`plugins/information-discrete-math/skills/information-discrete-math/SKILL.md`](https://github.com/morrocwi/information-discrete-math/blob/e4932afee144484759f0f3275e69fc923b80d091/plugins/information-discrete-math/skills/information-discrete-math/SKILL.md). Gates: TG-RFG-01
- **readout-universe skill** (`readout_universe`) - Tag every claim with the tier its evidence earns; usable in any domain. File: [`plugins/readout-universe/skills/readout-universe/SKILL.md`](https://github.com/morrocwi/readout_universe/blob/68863dfefc32cdbc4d97871633e36aec3c8b8018/plugins/readout-universe/skills/readout-universe/SKILL.md). Gates: TIER-TAGGING
- **birca skill** (`birca`) - Discovery surface of the health-information skill; the skill names SYSTEM_PROMPT.md as its single source of truth. File: [`SKILL.md`](https://github.com/morrocwi/birca/blob/4459977909911d5faadec778c460d3acfdda170c/SKILL.md). Gates: BIRCA-SAFETY-GATE. Note: educational and research use only; not diagnostic, no treatment selection, and not clinically safety-audited
- **skillme skill** (`skillme`) - The operational protocol - two-question intake gate, moves in order, hard invariants. File: [`plugins/skillme/skills/skillme/SKILL.md`](https://github.com/morrocwi/skillme/blob/232cc8d2025cdec64cc77ad8ec2fceb17639f0e0/plugins/skillme/skills/skillme/SKILL.md)
- **seth skill** (`seth-skill`) - Non-negotiable rules, workflow and failure codes of the calculation contract. File: [`plugins/seth/skills/seth/SKILL.md`](https://github.com/morrocwi/seth-skill/blob/4e8e9e7708078aec672304f46c99b946e13fc43c/plugins/seth/skills/seth/SKILL.md)

## Vendor-neutral prompt packets

- **glosa prompt packet** (`glosa`) - The same method as a vendor-neutral prompt for agents without a plugin system. File: [`plugins/glosa/PROMPT_PACKET.md`](https://github.com/morrocwi/glosa/blob/106acb3ee985f91511a61f31840e046fb1e76034/plugins/glosa/PROMPT_PACKET.md). Gates: GLOSA-PUBLISH-GATE
- **birca system prompt** (`birca`) - The instruction block itself; follow it exactly and in full, with LEGAL_DISCLAIMER.md shipped unmodified. File: [`SYSTEM_PROMPT.md`](https://github.com/morrocwi/birca/blob/4459977909911d5faadec778c460d3acfdda170c/SYSTEM_PROMPT.md). Gates: BIRCA-SAFETY-GATE. Note: educational and research use only; not diagnostic, no treatment selection, and not clinically safety-audited

## MCP servers

- **glosa MCP server** (`glosa`) - One tool per kernel function - validate cards, notes and reports, gate a release; stdlib-only, stdio. File: [`mcp/README.md`](https://github.com/morrocwi/glosa/blob/106acb3ee985f91511a61f31840e046fb1e76034/mcp/README.md). Gates: GLOSA-PUBLISH-GATE
- **Toledo MCP server** (`toledo`) - Verdict-aware equation lookup, lineage and status over stdio; the lookup tool the source policy prefers. File: [`mcp/README.md`](https://github.com/morrocwi/toledo/blob/d46a9aab6c22be391fc8b2486d9b101443ae158e/mcp/README.md), client config: [`.mcp.json`](https://github.com/morrocwi/toledo/blob/d46a9aab6c22be391fc8b2486d9b101443ae158e/.mcp.json). Gates: TG-RFG-01
- **birca MCP server** (`birca`) - Serves the prompt, spec and disclaimer and a deterministic English-only regex check that narrows but does not close the gap; also exposes research-mode compute tools; calls no model itself. File: [`mcp_server/README.md`](https://github.com/morrocwi/birca/blob/4459977909911d5faadec778c460d3acfdda170c/mcp_server/README.md). Gates: BIRCA-SAFETY-GATE. Note: educational and research use only; not diagnostic, no treatment selection, and not clinically safety-audited

## Library and service APIs

- **idm library and REST service** (`information-discrete-math`) - Python library, REST service and CLI entry point; every answer is a tier-tagged finite readout. File: [`API.md`](https://github.com/morrocwi/information-discrete-math/blob/e4932afee144484759f0f3275e69fc923b80d091/API.md). Gates: TG-RFG-01
- **idm capability manifest** (`information-discrete-math`) - Machine-readable list of interfaces and problem kinds. File: [`capabilities.json`](https://github.com/morrocwi/information-discrete-math/blob/e4932afee144484759f0f3275e69fc923b80d091/capabilities.json). Gates: TG-RFG-01

## Static read APIs (no MCP client needed)

- **Toledo static read API** (`toledo`) - Periodic JSON mirror for callers with no MCP or stdio access; it can lag the registry and is corroboration, never a substitute for a live lookup. File: [`mcp/docs/STATIC_API.md`](https://github.com/morrocwi/toledo/blob/d46a9aab6c22be391fc8b2486d9b101443ae158e/mcp/docs/STATIC_API.md), endpoint: <https://morrocwi.github.io/toledo/>. Gates: TG-RFG-01

## Command-line tools

- **glosa CLI** (`glosa`) - check, self-test and literature-review commands over the same kernel. File: [`cli/README.md`](https://github.com/morrocwi/glosa/blob/106acb3ee985f91511a61f31840e046fb1e76034/cli/README.md). Gates: GLOSA-PUBLISH-GATE
- **toledo CLI** (`toledo`) - find, show and ancestry over the built library; run scripts/toledo_build.py first. File: [`scripts/toledo`](https://github.com/morrocwi/toledo/blob/d46a9aab6c22be391fc8b2486d9b101443ae158e/scripts/toledo). Gates: TG-RFG-01
- **skillme protocol kernel** (`skillme`) - Stdlib-only validator of a run record; VALID means well-formed, not correct. File: [`skillme_protocol_kernel.py`](https://github.com/morrocwi/skillme/blob/232cc8d2025cdec64cc77ad8ec2fceb17639f0e0/skillme_protocol_kernel.py)

## Installable packages

- **idm Python package** (`information-discrete-math`) - Installable package behind the idm library, REST service and CLI; install from the repository. File: [`pyproject.toml`](https://github.com/morrocwi/information-discrete-math/blob/e4932afee144484759f0f3275e69fc923b80d091/pyproject.toml). Gates: TG-RFG-01
- **fra Python package** (`finite-readout-acceleration`) - Stdlib-only library - cost model, break-even guard, cache-safety audit, eviction policy; install from the repository. File: [`pyproject.toml`](https://github.com/morrocwi/finite-readout-acceleration/blob/82bd6f307a34916241190b5fe86d588ed6789dd0/pyproject.toml)
