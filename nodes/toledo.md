# toledo

GENERATED from `graph/repos/` and `graph/nodes.yaml` - do not hand-edit.

- **Repository:** <https://github.com/morrocwi/toledo>
- **Class:** axis - axis `mathematics`
- **Role:** Permanent coded registry of the programme's equations, with parents, tier, lineage and a Coq file where one exists.
- **Is:** equation source of record; lookup gate (registry JSON, CLI, MCP, static site)
- **Is not:** a home for papers, prose or ontology; a place where a proposal counts as a theorem
- **Pinned:** `d46a9aab6c22` on `main`, 147 commits after tag `v1.8.0`
- **Concept DOI:** 10.5281/zenodo.22537318
- **Gates:** TG-RFG-01
- **Surfaces:** mcp [Toledo MCP server](https://github.com/morrocwi/toledo/blob/d46a9aab6c22be391fc8b2486d9b101443ae158e/mcp/README.md); static-api [Toledo static read API](https://github.com/morrocwi/toledo/blob/d46a9aab6c22be391fc8b2486d9b101443ae158e/mcp/docs/STATIC_API.md); cli [toledo CLI](https://github.com/morrocwi/toledo/blob/d46a9aab6c22be391fc8b2486d9b101443ae158e/scripts/toledo) (see `SURFACES.md`)

## Read in this order

1. [`AGENTS.md`](https://github.com/morrocwi/toledo/blob/d46a9aab6c22be391fc8b2486d9b101443ae158e/AGENTS.md)
2. [`EQUATION_SOURCE_POLICY.md`](https://github.com/morrocwi/toledo/blob/d46a9aab6c22be391fc8b2486d9b101443ae158e/EQUATION_SOURCE_POLICY.md)
3. [`registry/SCHEMA.md`](https://github.com/morrocwi/toledo/blob/d46a9aab6c22be391fc8b2486d9b101443ae158e/registry/SCHEMA.md)
4. [`registry/CANONICAL.json`](https://github.com/morrocwi/toledo/blob/d46a9aab6c22be391fc8b2486d9b101443ae158e/registry/CANONICAL.json)
5. [`registry/genesis_root.json`](https://github.com/morrocwi/toledo/blob/d46a9aab6c22be391fc8b2486d9b101443ae158e/registry/genesis_root.json)
6. [`scripts/toledo_build.py`](https://github.com/morrocwi/toledo/blob/d46a9aab6c22be391fc8b2486d9b101443ae158e/scripts/toledo_build.py)
7. [`scripts/toledo`](https://github.com/morrocwi/toledo/blob/d46a9aab6c22be391fc8b2486d9b101443ae158e/scripts/toledo)

## Verified edges

- `glosa` **prescribes-registration-in** `toledo` - evidence: `glosa` / [`methodology/P19_registration.md`](https://github.com/morrocwi/glosa/blob/106acb3ee985f91511a61f31840e046fb1e76034/methodology/P19_registration.md) contains "| An **equation** (new, revised, or reused in a new domain) | **Toledo**"
- `information-discrete-math` **registers-into** `toledo` - evidence: `information-discrete-math` / [`docs/TOLEDO_CODES.md`](https://github.com/morrocwi/information-discrete-math/blob/e4932afee144484759f0f3275e69fc923b80d091/docs/TOLEDO_CODES.md) contains "was registered into Toledo"
- `readout-problem-navier-stokes` **defers-status-to** `toledo` - evidence: `readout-problem-navier-stokes` / [`README.md`](https://github.com/morrocwi/readout-problem-navier-stokes/blob/e2027c98edf94f5eee04119aeacad9dbcd9378f5/README.md) contains "proposal/equation provenance and tier/status"
- `readout_genesis` **defers-status-to** `toledo` - evidence: `readout_genesis` / [`AGENTS.md`](https://github.com/morrocwi/readout_genesis/blob/1ca99bacc77624f75dd4c5752cbe20a0c9907618/AGENTS.md) contains "Toledo records status/provenance"
- `toledo` **authority-for** `axis:mathematics` - evidence: `glosa` / [`docs/ECOSYSTEM.md`](https://github.com/morrocwi/glosa/blob/106acb3ee985f91511a61f31840e046fb1e76034/docs/ECOSYSTEM.md) contains "| Equation source of record + lookup gate"
- `toledo` **imports-coq-from** `readout_genesis` - evidence: `toledo` / [`coq/readout_genesis/PROVENANCE.json`](https://github.com/morrocwi/toledo/blob/d46a9aab6c22be391fc8b2486d9b101443ae158e/coq/readout_genesis/PROVENANCE.json) contains "Files are imported as public GitHub source"
- `toledo` **imports-coq-from** `readout_universe` - evidence: `toledo` / [`coq/readout_universe/PROVENANCE.json`](https://github.com/morrocwi/toledo/blob/d46a9aab6c22be391fc8b2486d9b101443ae158e/coq/readout_universe/PROVENANCE.json) contains "Imported under the MIT terms already granted by the upstream repository"
- `toledo` **imports-coq-from** `information-discrete-math` - evidence: `toledo` / [`coq/information-discrete-math/PROVENANCE.json`](https://github.com/morrocwi/toledo/blob/d46a9aab6c22be391fc8b2486d9b101443ae158e/coq/information-discrete-math/PROVENANCE.json) contains "Copied verbatim (byte-for-byte diff against the upstream commit above is empty"
- `toledo` **imports-coq-from** `zero-readout-certifies` - evidence: `toledo` / [`coq/zero-readout-certifies/PROVENANCE.json`](https://github.com/morrocwi/toledo/blob/d46a9aab6c22be391fc8b2486d9b101443ae158e/coq/zero-readout-certifies/PROVENANCE.json) contains "Copied verbatim (byte-for-byte diff against the upstream commit above is empty"
- `toledo` **imports-coq-from** `finite-readout-acceleration` - evidence: `toledo` / [`coq/finite-readout-acceleration/PROVENANCE.json`](https://github.com/morrocwi/toledo/blob/d46a9aab6c22be391fc8b2486d9b101443ae158e/coq/finite-readout-acceleration/PROVENANCE.json) contains "Copied verbatim (byte-for-byte diff against the upstream commit above is empty"

## Neighbour cards

[[finite-readout-acceleration]] · [[glosa]] · [[information-discrete-math]] · [[readout-problem-navier-stokes]] · [[readout_genesis]] · [[readout_universe]] · [[zero-readout-certifies]]
