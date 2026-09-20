# SCHEMA - the graph model

## Files

| File | Written by | Holds |
|---|---|---|
| `graph/repos/<id>.yaml` | hand or `hub.py add / remove / surfaces` | one repository: node, surfaces, outgoing edges with evidence (no `from` key: the file's repository is the source). The commands rewrite the file canonically, so comments inside it are not kept |
| `graph/nodes.yaml` | hand | axes, lens, gates, artifacts |
| `graph/edges.yaml` | hand | edge types |
| `graph/routes.yaml` | hand; rewritten canonically by `hub.py remove` when a route loses a step | intent -> ordered reads -> gates |
| `graph/lock.yaml` | `hub.py lock` | per repository: url, branch, commit, nearest tag, blob of every referenced path |
| `ROUTES.md`, `SURFACES.md`, `llms.txt`, `nodes/*.md`, `graph/hub.json`, `graph/hub.graphml`, route table in `AGENTS.md` | `hub.py build` | renderings; never hand-edited |

One fact has one home. If a fact appears in a generated file and is wrong, fix the YAML.

## Node kinds

| Kind | Id form | Meaning |
|---|---|---|
| `HUB` | `hub:main.hub` | this repository |
| `AXIS` | `axis:<id>` | one kind of question; held by exactly one repository |
| `REPO` | `<repository name>` | a public repository; `class` is `axis`, `linked` or `catalog` |
| `GATE` | `gate:<id>` | a rule defined in some repository that work must pass. `TG-RFG-01` is the target's own id; the other gate ids are labels coined by this hub for a rule the target defines |
| `ARTIFACT` | `artifact:<id>` | one thing with more than one public copy; names its source of truth |
| `ROUTE` | `route:<id>` | an intent and the reading path that serves it |
| `LENS` | `lens:<id>` | Step 0: the reading every route is preceded by. Each facet must be stated by a source file with a checked quotation; the facet label is the hub's paraphrase of that sentence and is not machine-verified. The ordering itself is the hub's own rule |
| `SURFACE` | `surface:<repo>:<kind>:<path>` (plus `:<plugin>` only when one manifest carries several plugins) | a skill, plugin, prompt packet, MCP server, API, CLI or package a repository ships, as a pinned file; plugin and marketplace names are verified against the pinned manifest |

## Admission rule for a repository

`hub.py add` writes a repository as `catalog` with `draft: true`: `check` warns until a person has
written its role / is / is_not from the repository's own README and removed the flag.

A repository becomes a node only if it is public. Its class follows from evidence, not opinion:

- `axis` - a policy or map file in a public repository names it as the source of record for an axis;
- `linked` - at least one edge with verified evidence touches it;
- `catalog` - neither. It is discoverable here, and nothing more is claimed.

The checker enforces that every axis node carries an `authority-for` edge, and both directions of the catalog rule: a non-catalog node without an edge fails, and a catalog
node with an edge fails.

## Edge evidence

```yaml
# in graph/repos/<from>.yaml - the file's repository is the source, so there is no `from` key
edges:
  - type: <one of edges.yaml `types`>
    to: <node id>
    evidence: {in: <repo, defaults to this file's repository>, path: <file>, match: "<literal text in that file>"}
```

`match` is a case-sensitive substring that must occur **exactly once** in the pinned blob, be at
least 12 characters long and not be a bare repository name. Choose text that states the relation,
not a word that merely co-occurs. When `in` names a third repository the relation is reported by a
neighbour, not by the repository itself; the node card shows where the evidence lives. Evidence shows the relation is *stated*; it cannot show the
statement is *right*. That limit is permanent and is why independent review still matters.

## Edge type decision rubric

Which of `graph/edges.yaml`'s 16 declared types to use for a new edge - one line each: the type's own
description (from `edges.yaml`), a real matching pair already in `graph/repos/*.yaml`, and one
non-matching (would-be-wrong) case. Where a real past mistake in `logbook.jsonl` is on point for a
type, it is used and named by its `result_of` decision id; every other non-matching example is
**illustrative only** - a plausible mistake, not a recorded one - and is marked as such.

- **`authority-for`** - a policy or map file names the repo as the source of record, or the primary
  lens, for an axis. Matching: `toledo` -> `axis:mathematics`, evidence in `glosa`/`docs/ECOSYSTEM.md`
  naming toledo the "Equation source of record". Non-matching (illustrative): a repository that merely
  *uses* Toledo codes internally, with no map file anywhere naming it the source of record for an
  axis - that repository is a consumer, not an authority, and gets no `authority-for` edge at all.

- **`registers-into`** - repo carries its equations under Toledo codes. Matching:
  `information-discrete-math` -> `toledo`, evidence in `docs/TOLEDO_CODES.md`: "was registered into
  Toledo". Non-matching (illustrative): a repository whose README merely *mentions* Toledo in passing
  ("see also Toledo") without stating that its own equations carry Toledo codes - that is a pointer,
  not a registration, and would need a different type or no edge.

- **`prescribes-registration-in`** - repo's method tells its users to register equations in the
  target. Matching: `glosa` -> `toledo`, evidence in `methodology/P19_registration.md`'s registration
  table naming Toledo. Non-matching (illustrative): a repository that itself registers equations into
  Toledo (that is `registers-into`, the direction is reversed: the repo is the object being registered,
  not the method telling others to register).

- **`requires-gate`** - repo's agent file makes the named gate mandatory or names it as required
  reading. Matching: `information-discrete-math` -> `gate:TG-RFG-01`, evidence in `AGENTS.md`: "##
  Mandatory Toledo-Genesis reuse-first gate". Non-matching (illustrative): a repository whose README
  merely explains what a gate is, in prose, without its own agent file making that gate mandatory for
  work done in the repository - explaining a rule is not the same as being bound by it.

- **`defers-status-to`** - repo does not decide theorem status or provenance itself; the target does.
  Matching: `readout_genesis` -> `toledo`, evidence in `AGENTS.md`: "Toledo records status/provenance".
  Non-matching (illustrative): a repository that both cites Toledo *and* independently labels its own
  results "proven" or "theorem" in its own files - if a repo asserts status on its own authority
  anywhere, it has not deferred that status to the target, whatever else it also says.

- **`delegates-proof-to`** - repo states that generic finite kernels are proved in the target.
  Matching: `readout_genesis` -> `information-discrete-math`, evidence in `AGENTS.md`: "IDM proves
  generic finite kernels". Non-matching (illustrative): a repository that merely *reuses* a proved
  kernel's conclusion without stating that the proof itself lives in the target - reuse of a result is
  not the same claim as delegation of the proof obligation.

- **`checks-ontology-against`** - repo checks ontology compatibility against the target. Matching:
  `readout-problem-navier-stokes` -> `readout_genesis`, evidence in `AGENTS.md`: "is checked next for
  ontology". Non-matching: this is exactly the mistake independent review caught in the reused
  `dual-lane-epistemic-harness` -> `readout_universe` edge (`result_of: D21`, logbook line 39): the
  target's own text called the borrowed material "a borrowed/analogue vocabulary", not an ontology
  compatibility check, so `checks-ontology-against` (or `builds-on`) would have been the wrong type;
  the edge was retyped to the type below instead.

- **`imports-coq-from`** - target's Coq sources are imported with a provenance manifest. Matching:
  `toledo` -> `readout_genesis`, evidence in `coq/readout_genesis/PROVENANCE.json`: "Files are imported
  as public GitHub source". Non-matching (illustrative): a repository that cites another repository's
  theorem in prose, with no `PROVENANCE.json`-style manifest and no Coq files actually copied in - a
  citation is not an import, and this type is reserved for a real, checkable provenance record.

- **`builds-on`** - a file states that the repo rests on the target's foundation or floor. Matching:
  `readout_universe` -> `information-discrete-math`, evidence in `philosophy.md`: "The mandatory floor
  for this". Non-matching: independent review dropped a `builds-on` edge from
  `task-conditioned-6d-pose-stop` to `information-discrete-math` (`result_of: D20`, logbook line 37)
  because the only evidence was "one thin, non-central parenthetical clause" - a passing mention is not
  the same claim as resting on a foundation, and a thin clause does not carry the weight `builds-on`
  asserts.

- **`reads-shared-math-from`** - repo's agent file sends shared mathematics work to a document in the
  target. Matching: `readout-problem-navier-stokes` -> `information-discrete-math`, evidence in
  `AGENTS.md`: "If working on shared bridge mathematics, read". Non-matching (illustrative): a
  repository whose agent file sends readers to the target for *ontology* questions, not shared
  mathematics - that relation is `checks-ontology-against`, not this type; the target of the sentence
  matters as much as the target repository.

- **`declares-lineage-from`** - repo names the target at a pinned commit as the source lineage of a
  component it ships; the component itself need not exist in the target. Matching: `birca` ->
  `readout_genesis`, evidence in `compute/README.md`: "`morrocwi/readout_genesis`, pinned commit".
  Non-matching (illustrative): a repository that imports the target's actual Coq files verbatim with a
  provenance manifest - that stronger, file-for-file claim is `imports-coq-from`, not a lineage
  declaration about a component that need not exist in the target.

- **`holds-synced-copy-from`** - ONE named file in the repo is a synced copy of a document in the
  target; the target holds the source of truth (says nothing about the rest of the repo). Matching:
  `readout_universe` -> `readout_genesis`, evidence in
  `EQUATION_LIBRARY_ROOT_TO_SM_STREAM_synced_mirror.md`: "if a mismatch is ever found, Appendix C
  wins". Non-matching (illustrative): claiming this type for a whole repository because *one* file in
  it is a synced mirror - the type is scoped to the one named file; nothing about the rest of the
  repository follows from it.

- **`companion-of`** - a file (possibly in a third repository) describes the repo as a companion of
  the target. Matching: `zero-readout-certifies` -> `information-discrete-math`, evidence in
  `glosa`/`docs/ECOSYSTEM.md`: "zero-readout-certifies (public)<br/>Coq companion to IDM". Non-matching
  (illustrative): two repositories that merely cite each other's results without any file anywhere
  describing them as companions - a mutual citation is not, by itself, a stated companion relation.

- **`cites-proposal-from`** - repo names a Toledo proposals-lane entry as the derivation behind a
  specific mechanism it runs; the proposal is not yet a Toledo theorem. Matching:
  `task-conditioned-6d-pose-stop` -> `toledo`, evidence in `README.md`: "Toledo proposal
  `PROP-DECAY-01`". Non-matching (illustrative): a repository that cites a Toledo entry which is
  already a registered theorem (not a proposal) - that is ordinary equation reuse under the `equation`
  route, not this type, which exists specifically for the proposals lane.

- **`logged-diagnosis-in`** - repo records a diagnosis of one of its own findings as a project in the
  target's case system. Matching: `task-conditioned-6d-pose-stop` -> `glosa`, evidence in `README.md`:
  "A diagnosis recorded in glosa". Non-matching (illustrative): a repository whose README merely
  recommends using glosa's methodology for future diagnoses, without a diagnosis of one of its own
  findings actually existing there yet - a recommendation to use a case system is not a record filed in
  it.

- **`borrows-vocabulary-from`** - repo reuses a target's typed vocabulary by declared analogy, without
  depending on the target's mechanism. Matching: `dual-lane-epistemic-harness` -> `readout_universe`,
  evidence in `README.md`: "readout_universe`'s evidence-tier discipline" - this is the very edge
  independent review retyped away from `builds-on` (`result_of: D21`, logbook line 39), because the
  target's own text named the reuse a borrowed/analogue vocabulary rather than a structural dependency.
  Non-matching: reusing this type for `readout_universe` -> `information-discrete-math`'s "mandatory
  floor" language (logbook line 39's own point) would be wrong in the other direction - that edge
  states a structural dependency, so it correctly stays `builds-on`.

## Pins

`lock` pins the public default-branch state (`origin/<branch>`), never local work, so a pin is
always reachable by anyone. A repository without a release tag is pinned by commit alone and its
card says so. `check --heads` warns when a default branch has moved past its pin.

## Checks (`hub.py check`)

0. input safety - owner and host are an allow-list in code; every id, path, url, tag, commit and blob in
   `graph/*.yaml` and `graph/lock.yaml` is validated before any command uses it; symbolic links and
   unexpected executable bits fail;
1. structure - ids, endpoints, edge types, class rules, one holder per axis, routes resolve;
2. pins - every referenced path is pinned, its blob still matches, and the pinned commit is on the
   repository's public default branch, not merely served by its URL (`--workspace` or `--remote`);
3. evidence - every `match` text occurs exactly once in its pinned blob;
4. lens and surfaces - every lens facet is stated by a source, sources span at least two repositories,
   and each plugin surface's marketplace and plugin names equal the pinned manifest (`--workspace` or `--remote`);
5. generated - every generated file equals a fresh render;
6. leak scan - no local path, private address, internal ticket or session id, mail address,
   credential-shaped string, or tool / vendor attribution in any tracked file. Organisation-specific
   forbidden names go in the untracked `.leakpatterns.local`, one regular expression per line.

Without `--workspace` or `--remote` (the mode the pre-commit hook runs), pins, evidence and plugin
manifests are NOT re-verified, and the summary line says so. Free-text fields are validated as one
printable line without markup or links, but what they say is reviewed by hand: a plain-prose
instruction would pass the validator.
