# toledo

GENERATED from `graph/repos/` and `graph/nodes.yaml` - do not hand-edit.

- **Repository:** <https://github.com/morrocwi/toledo>
- **Class:** axis - axis `mathematics`
- **Role:** Permanent coded registry of the programme's equations, with parents, tier, lineage and a Coq file where one exists.
- **Is:** equation source of record; lookup gate (registry JSON, CLI, MCP, static site)
- **Is not:** a home for papers, prose or ontology; a place where a proposal counts as a theorem
- **Pinned:** `ada5edd783fd` on `main`, 155 commits after tag `v1.8.0`
- **Concept DOI:** 10.5281/zenodo.22537318
- **Gates:** TG-RFG-01
- **Surfaces:** mcp [Toledo MCP server](https://github.com/morrocwi/toledo/blob/ada5edd783fde58d9478b2ef3bcd9520b967270a/mcp/README.md); static-api [Toledo static read API](https://github.com/morrocwi/toledo/blob/ada5edd783fde58d9478b2ef3bcd9520b967270a/mcp/docs/STATIC_API.md); cli [toledo CLI](https://github.com/morrocwi/toledo/blob/ada5edd783fde58d9478b2ef3bcd9520b967270a/scripts/toledo) (see `SURFACES.md`)

## Read in this order

1. [`AGENTS.md`](https://github.com/morrocwi/toledo/blob/ada5edd783fde58d9478b2ef3bcd9520b967270a/AGENTS.md)
2. [`EQUATION_SOURCE_POLICY.md`](https://github.com/morrocwi/toledo/blob/ada5edd783fde58d9478b2ef3bcd9520b967270a/EQUATION_SOURCE_POLICY.md)
3. [`registry/SCHEMA.md`](https://github.com/morrocwi/toledo/blob/ada5edd783fde58d9478b2ef3bcd9520b967270a/registry/SCHEMA.md)
4. [`registry/CANONICAL.json`](https://github.com/morrocwi/toledo/blob/ada5edd783fde58d9478b2ef3bcd9520b967270a/registry/CANONICAL.json)
5. [`registry/genesis_root.json`](https://github.com/morrocwi/toledo/blob/ada5edd783fde58d9478b2ef3bcd9520b967270a/registry/genesis_root.json)
6. [`scripts/toledo_build.py`](https://github.com/morrocwi/toledo/blob/ada5edd783fde58d9478b2ef3bcd9520b967270a/scripts/toledo_build.py)
7. [`scripts/toledo`](https://github.com/morrocwi/toledo/blob/ada5edd783fde58d9478b2ef3bcd9520b967270a/scripts/toledo)

## Verified edges

- `dual-lane-epistemic-harness` **builds-on** `toledo` - evidence: `dual-lane-epistemic-harness` / [`README.md`](https://github.com/morrocwi/dual-lane-epistemic-harness/blob/1507931b96456e4dd983adfde0637b1c6bc48fca/README.md) contains "The lens layer is grounded in Toledo's Readout Bridge"
- `glosa` **prescribes-registration-in** `toledo` - evidence: `glosa` / [`methodology/P19_registration.md`](https://github.com/morrocwi/glosa/blob/cf1c96a433dda38878ec8a85ca099657d761ec64/methodology/P19_registration.md) contains "| An **equation** (new, revised, or reused in a new domain) | **Toledo**"
- `information-discrete-math` **registers-into** `toledo` - evidence: `information-discrete-math` / [`docs/TOLEDO_CODES.md`](https://github.com/morrocwi/information-discrete-math/blob/33c54bb2512cf2c129feef928eb64977bb420b57/docs/TOLEDO_CODES.md) contains "was registered into Toledo"
- `readout-problem-navier-stokes` **defers-status-to** `toledo` - evidence: `readout-problem-navier-stokes` / [`README.md`](https://github.com/morrocwi/readout-problem-navier-stokes/blob/a048171bcfbd805b453cbcd1c31f8623d64ac698/README.md) contains "proposal/equation provenance and tier/status"
- `readout_genesis` **defers-status-to** `toledo` - evidence: `readout_genesis` / [`AGENTS.md`](https://github.com/morrocwi/readout_genesis/blob/416fd7b9de0f056d82d078dcc2232e9b36498f3a/AGENTS.md) contains "Toledo records status/provenance"
- `task-conditioned-6d-pose-stop` **cites-proposal-from** `toledo` - evidence: `task-conditioned-6d-pose-stop` / [`README.md`](https://github.com/morrocwi/task-conditioned-6d-pose-stop/blob/176881a6476d28da18177c6638c982e50370776a/README.md) contains "Toledo proposal `PROP-DECAY-01`"
- `toledo` **authority-for** `axis:mathematics` - evidence: `glosa` / [`docs/ECOSYSTEM.md`](https://github.com/morrocwi/glosa/blob/cf1c96a433dda38878ec8a85ca099657d761ec64/docs/ECOSYSTEM.md) contains "| Equation source of record + lookup gate"
- `toledo` **imports-coq-from** `readout_genesis` - evidence: `toledo` / [`coq/readout_genesis/PROVENANCE.json`](https://github.com/morrocwi/toledo/blob/ada5edd783fde58d9478b2ef3bcd9520b967270a/coq/readout_genesis/PROVENANCE.json) contains "Files are imported as public GitHub source"
- `toledo` **imports-coq-from** `readout_universe` - evidence: `toledo` / [`coq/readout_universe/PROVENANCE.json`](https://github.com/morrocwi/toledo/blob/ada5edd783fde58d9478b2ef3bcd9520b967270a/coq/readout_universe/PROVENANCE.json) contains "Imported under the MIT terms already granted by the upstream repository"
- `toledo` **imports-coq-from** `information-discrete-math` - evidence: `toledo` / [`coq/information-discrete-math/PROVENANCE.json`](https://github.com/morrocwi/toledo/blob/ada5edd783fde58d9478b2ef3bcd9520b967270a/coq/information-discrete-math/PROVENANCE.json) contains "Copied verbatim (byte-for-byte diff against the upstream commit above is empty"
- `toledo` **imports-coq-from** `zero-readout-certifies` - evidence: `toledo` / [`coq/zero-readout-certifies/PROVENANCE.json`](https://github.com/morrocwi/toledo/blob/ada5edd783fde58d9478b2ef3bcd9520b967270a/coq/zero-readout-certifies/PROVENANCE.json) contains "Copied verbatim (byte-for-byte diff against the upstream commit above is empty"
- `toledo` **imports-coq-from** `finite-readout-acceleration` - evidence: `toledo` / [`coq/finite-readout-acceleration/PROVENANCE.json`](https://github.com/morrocwi/toledo/blob/ada5edd783fde58d9478b2ef3bcd9520b967270a/coq/finite-readout-acceleration/PROVENANCE.json) contains "Copied verbatim (byte-for-byte diff against the upstream commit above is empty"

## Neighbour cards

[[dual-lane-epistemic-harness]] · [[finite-readout-acceleration]] · [[glosa]] · [[information-discrete-math]] · [[readout-problem-navier-stokes]] · [[readout_genesis]] · [[readout_universe]] · [[task-conditioned-6d-pose-stop]] · [[zero-readout-certifies]]
