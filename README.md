# main.hub

**One entry point, many repositories.** A routing knowledge graph for the public repositories of
the Human-AI Readout Programme (author: Yaoharee Lahtee). An AI agent - or a person - lands here,
picks an intent, and is sent to the right repository, the right file and the right gate, at a
pinned commit.

It contains no research content: no equation, no theorem statement, no copied section. Pointers and edges only.

## Why it exists

The programme is split across repositories on purpose: one holds the equation registry, one the
mathematical floor, one the ontology, one the epistemology, one the method, and leaves apply
them. Each is the source of record for one kind of question. What was missing was a single,
machine-checkable answer to *"I am about to do X - where do I go, and what do I read first?"*

| You get | From |
|---|---|
| intent -> repository -> file -> gate | [`AGENTS.md`](AGENTS.md), [`ROUTES.md`](ROUTES.md) |
| Step 0: the lens every route is preceded by | [`ROUTES.md#step-0`](ROUTES.md#step-0) |
| skills, plugins, MCP servers, APIs, CLIs and packages the repositories ship | [`SURFACES.md`](SURFACES.md) |
| one card per repository: role, is / is not, reading order, verified edges | [`nodes/`](nodes/) |
| the whole graph, machine-readable | [`graph/hub.json`](graph/hub.json), [`graph/hub.graphml`](graph/hub.graphml) |
| commit + blob pins of every referenced file | [`graph/lock.yaml`](graph/lock.yaml) |

## What makes an edge true here

Every edge in [`graph/edges.yaml`](graph/edges.yaml) names a file in a public repository and a
literal text that file must contain. `scripts/hub.py check` re-reads the pinned blob and fails if
the text is gone or no longer unique. Each edge is therefore a quotation of what a repository says
about itself or about a neighbour. What the hub does author - one-line role strings, route wording,
gate summaries, gate ids other than `TG-RFG-01`, lens facet labels, the Step 0 instruction and the
one-line descriptions in `SURFACES.md` - are paraphrases of each repository's own files
and are not machine-verified; if one is wrong, the repository wins. A repository with no such evidence is
listed as `catalog` and explicitly not claimed to be connected.

This is a readout, not a declaration. Pins go stale; `check --remote --heads` reports which
default branches have moved since the lock was taken. When the hub and a repository disagree,
the repository wins.

## Use

```bash
pip install pyyaml
# optional: put a GitHub access credential in the GITHUB_TOKEN environment variable first;
# without one the remote check may hit GitHub's anonymous rate limit
python scripts/hub.py check --remote --heads     # pins resolve, evidence present; warns where a branch moved past its pin
python scripts/hub.py materialize --dest ./ws    # partial + sparse clone of the pinned entry files
```

Maintainers, with local clones of the repositories side by side in one directory:

```bash
git config core.hooksPath githooks               # once per clone
python scripts/hub.py lock  --workspace ..       # pin the public default-branch state
python scripts/hub.py build                      # regenerate ROUTES.md, nodes/, llms.txt, graph/hub.*
python scripts/hub.py check --workspace ..       # structure + pins + evidence + generated + leak scan
```

The history of `graph/lock.yaml` is the timeline of the whole programme: `git log -p graph/lock.yaml`
shows which commit of every repository was current on any date, and a tag on this hub is a
reproducible snapshot of all of them together.

**Obsidian.** The repository opens as a vault as it is: every card in `nodes/` links its neighbour
cards, so the graph view shows the verified edges between repositories. `.obsidian/` stays local.

## Lineage

The role table descends from the prose ecosystem map in `glosa` (`docs/ECOSYSTEM.md`) and from
the source policy in `toledo` (`EQUATION_SOURCE_POLICY.md`). This hub adds pins, verified edges,
routes and a checker; it does not replace either document. See [`SCHEMA.md`](SCHEMA.md) for the
graph model and [`GOAL.md`](GOAL.md) for what would count as this hub failing.

## Status and boundary

- Covers public repositories only, by design.
- Verifies that a relation is *stated* in a repository, not that the statement is *correct*.
- Licence: code MIT, graph data and documentation CC BY 4.0 (see [`LICENSE`](LICENSE)). Each target repository keeps its own licence.
