# toledo

GENERATED from `graph/repos/` and `graph/nodes.yaml` - do not hand-edit.

- **Repository:** <https://github.com/morrocwi/toledo>
- **Class:** axis - axis `mathematics`
- **Role:** Permanent coded registry of the programme's equations, with parents, tier, lineage and a Coq file where one exists.
- **Is:** equation source of record; lookup gate (registry JSON, CLI, MCP, static site)
- **Is not:** a home for papers, prose or ontology; a place where a proposal counts as a theorem
- **Pinned:** `a21d76461a9c` on `main`, 150 commits after tag `v1.8.0`
- **Concept DOI:** 10.5281/zenodo.22537318
- **Gates:** TG-RFG-01
- **Surfaces:** mcp [Toledo MCP server](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/mcp/README.md); static-api [Toledo static read API](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/mcp/docs/STATIC_API.md); cli [toledo CLI](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/scripts/toledo) (see `SURFACES.md`)

## Read in this order

1. [`AGENTS.md`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/AGENTS.md)
2. [`EQUATION_SOURCE_POLICY.md`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/EQUATION_SOURCE_POLICY.md)
3. [`registry/SCHEMA.md`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/registry/SCHEMA.md)
4. [`registry/CANONICAL.json`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/registry/CANONICAL.json)
5. [`registry/genesis_root.json`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/registry/genesis_root.json)
6. [`scripts/toledo_build.py`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/scripts/toledo_build.py)
7. [`scripts/toledo`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/scripts/toledo)

## Verified edges

- `dual-lane-epistemic-harness` **builds-on** `toledo` - evidence: `dual-lane-epistemic-harness` / [`README.md`](https://github.com/morrocwi/dual-lane-epistemic-harness/blob/579d670f93499c3596f8127a868f40b3350fba9e/README.md) contains "The lens layer is grounded in Toledo's Readout Bridge"
- `glosa` **prescribes-registration-in** `toledo` - evidence: `glosa` / [`methodology/P19_registration.md`](https://github.com/morrocwi/glosa/blob/cf1c96a433dda38878ec8a85ca099657d761ec64/methodology/P19_registration.md) contains "| An **equation** (new, revised, or reused in a new domain) | **Toledo**"
- `information-discrete-math` **registers-into** `toledo` - evidence: `information-discrete-math` / [`docs/TOLEDO_CODES.md`](https://github.com/morrocwi/information-discrete-math/blob/33c54bb2512cf2c129feef928eb64977bb420b57/docs/TOLEDO_CODES.md) contains "was registered into Toledo"
- `readout-problem-navier-stokes` **defers-status-to** `toledo` - evidence: `readout-problem-navier-stokes` / [`README.md`](https://github.com/morrocwi/readout-problem-navier-stokes/blob/82262e19c85eebaafba3bc8391e8ac953aa2f704/README.md) contains "proposal/equation provenance and tier/status"
- `readout_genesis` **defers-status-to** `toledo` - evidence: `readout_genesis` / [`AGENTS.md`](https://github.com/morrocwi/readout_genesis/blob/864bb85950deec943517b102bd33cf8ff101da15/AGENTS.md) contains "Toledo records status/provenance"
- `task-conditioned-6d-pose-stop` **cites-proposal-from** `toledo` - evidence: `task-conditioned-6d-pose-stop` / [`README.md`](https://github.com/morrocwi/task-conditioned-6d-pose-stop/blob/176881a6476d28da18177c6638c982e50370776a/README.md) contains "Toledo proposal `PROP-DECAY-01`"
- `toledo` **authority-for** `axis:mathematics` - evidence: `glosa` / [`docs/ECOSYSTEM.md`](https://github.com/morrocwi/glosa/blob/cf1c96a433dda38878ec8a85ca099657d761ec64/docs/ECOSYSTEM.md) contains "| Equation source of record + lookup gate"
- `toledo` **imports-coq-from** `readout_genesis` - evidence: `toledo` / [`coq/readout_genesis/PROVENANCE.json`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/coq/readout_genesis/PROVENANCE.json) contains "Files are imported as public GitHub source"
- `toledo` **imports-coq-from** `readout_universe` - evidence: `toledo` / [`coq/readout_universe/PROVENANCE.json`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/coq/readout_universe/PROVENANCE.json) contains "Imported under the MIT terms already granted by the upstream repository"
- `toledo` **imports-coq-from** `information-discrete-math` - evidence: `toledo` / [`coq/information-discrete-math/PROVENANCE.json`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/coq/information-discrete-math/PROVENANCE.json) contains "Copied verbatim (byte-for-byte diff against the upstream commit above is empty"
- `toledo` **imports-coq-from** `zero-readout-certifies` - evidence: `toledo` / [`coq/zero-readout-certifies/PROVENANCE.json`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/coq/zero-readout-certifies/PROVENANCE.json) contains "Copied verbatim (byte-for-byte diff against the upstream commit above is empty"
- `toledo` **imports-coq-from** `finite-readout-acceleration` - evidence: `toledo` / [`coq/finite-readout-acceleration/PROVENANCE.json`](https://github.com/morrocwi/toledo/blob/a21d76461a9ca64259e830d5456312e9b1e2e686/coq/finite-readout-acceleration/PROVENANCE.json) contains "Copied verbatim (byte-for-byte diff against the upstream commit above is empty"

## Neighbour cards

[[dual-lane-epistemic-harness]] · [[finite-readout-acceleration]] · [[glosa]] · [[information-discrete-math]] · [[readout-problem-navier-stokes]] · [[readout_genesis]] · [[readout_universe]] · [[task-conditioned-6d-pose-stop]] · [[zero-readout-certifies]]
