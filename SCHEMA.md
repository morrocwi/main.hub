# SCHEMA - the graph model

## Files

| File | Written by | Holds |
|---|---|---|
| `graph/nodes.yaml` | hand | axes, repositories, gates, artifacts |
| `graph/edges.yaml` | hand | edge types and edges, each with evidence |
| `graph/routes.yaml` | hand | intent -> ordered reads -> gates |
| `graph/lock.yaml` | `hub.py lock` | per repository: url, branch, commit, nearest tag, blob of every referenced path |
| `ROUTES.md`, `llms.txt`, `nodes/*.md`, `graph/hub.json`, `graph/hub.graphml`, route table in `AGENTS.md` | `hub.py build` | renderings; never hand-edited |

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

## Admission rule for a repository

A repository becomes a node only if it is public. Its class follows from evidence, not opinion:

- `axis` - a policy or map file in a public repository names it as the source of record for an axis;
- `linked` - at least one edge with verified evidence touches it;
- `catalog` - neither. It is discoverable here, and nothing more is claimed.

The checker enforces that every axis node carries an `authority-for` edge, and both directions of the catalog rule: a non-catalog node without an edge fails, and a catalog
node with an edge fails.

## Edge evidence

```yaml
- from: <node id>
  type: <one of edges.yaml `types`>
  to: <node id>
  evidence: {in: <repo, defaults to `from`>, path: <file>, match: "<literal text in that file>"}
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
4. generated - every generated file equals a fresh render;
5. leak scan - no local path, private address, internal ticket or session id, mail address,
   credential-shaped string, or tool / vendor attribution in any tracked file. Organisation-specific
   forbidden names go in the untracked `.leakpatterns.local`, one regular expression per line.

Without `--workspace` or `--remote`, checks 2 and 3 verify only that pins exist, and the summary
line says so.
