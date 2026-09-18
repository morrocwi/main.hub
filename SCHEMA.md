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
