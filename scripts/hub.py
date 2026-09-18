#!/usr/bin/env python3
"""main.hub -- build, pin and verify the routing graph.

    python scripts/hub.py lock  --workspace DIR   pin every referenced file (commit + blob)
    python scripts/hub.py build                   regenerate nodes/, ROUTES.md, llms.txt, graph/hub.*
    python scripts/hub.py check [--workspace DIR | --remote] [--heads]
    python scripts/hub.py materialize --dest DIR  partial + sparse clone of the pinned entry files

Source of truth: graph/nodes.yaml, graph/edges.yaml, graph/routes.yaml (hand-edited) and
graph/lock.yaml (written by `lock`). Everything else is generated; `check` fails when a generated
file is out of date, when a pinned blob no longer matches, or when an edge's evidence text is gone.
Only dependency: PyYAML.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

import yaml

ROOT = Path(__file__).resolve().parent.parent
GRAPH = ROOT / "graph"
BEGIN, END = "<!-- BEGIN GENERATED: routes -->", "<!-- END GENERATED: routes -->"
CLASSES = {"axis", "linked", "catalog"}
ID_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")
SHA_RE = re.compile(r"[0-9a-f]{40}")
MIN_MATCH = 12
PATH_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._/-]*")
DOT_PATHS = {".mcp.json", ".claude-plugin/marketplace.json"}      # the only dot-paths a graph file may name
SURFACE_KINDS = {"plugin", "skill", "mcp", "api", "cli", "package", "static-api", "prompt"}
BAD_TEXT = ("\n", "\r", "|", "<", ">", "](", "://", "`", "<!--")


def ok_path(p):
    return isinstance(p, str) and (p in DOT_PATHS or (PATH_RE.fullmatch(p) and ".." not in p.split("/")))


def ok_text(t, cap=400):
    """Free text that is rendered into agent-facing Markdown: one line, no markup, no links."""
    return isinstance(t, str) and 0 < len(t) <= cap and t.isprintable() and not any(b in t for b in BAD_TEXT)
OWNER, HOST = "morrocwi", "https://github.com"     # allow-list: never taken from a pull request


def safe_graph(d):
    """graph/*.yaml is pull-request data: validate shape, ids, paths and every rendered text before ANY command uses them."""
    def need(cond, msg):
        if not cond:
            sys.exit(f"graph: {msg}")
    n, routes = d["nodes"], d["routes"]
    need(isinstance(n, dict) and n.get("owner") == OWNER and n.get("host") == HOST, f"nodes.yaml owner/host must be {OWNER} / {HOST}")
    for key in ("axes", "repos", "gates", "artifacts"):
        need(isinstance(n.get(key), list) and all(isinstance(x, dict) for x in n[key]), f"nodes.yaml {key} must be a list of mappings")
    need(isinstance(routes, dict) and isinstance(routes.get("routes"), list) and all(isinstance(x, dict) for x in routes["routes"]),
         "routes.yaml routes must be a list of mappings")
    lens = n.get("lens")
    need(isinstance(lens, dict), "nodes.yaml lens must be a mapping (Step 0)")
    need(isinstance(lens.get("facets"), list) and lens["facets"] and all(isinstance(x, dict) for x in lens["facets"]), "lens.facets must be a non-empty list of mappings")
    need(isinstance(lens.get("sources"), list) and lens["sources"] and all(isinstance(x, dict) for x in lens["sources"]), "lens.sources must be a non-empty list of mappings")
    every = ([("repository", r.get("id")) for r in n["repos"]] + [("axis", a.get("id")) for a in n["axes"]]
             + [("gate", g.get("id")) for g in n["gates"]] + [("artifact", a.get("id")) for a in n["artifacts"]]
             + [("route", r.get("id")) for r in routes["routes"]] + [("lens", lens.get("id"))]
             + [("lens facet", f.get("id")) for f in lens["facets"]])
    for kind, i in every:
        need(isinstance(i, str) and ID_RE.fullmatch(i) and ".." not in i, f"unsafe {kind} id {i!r}")
    for kind in ("repository", "route", "lens facet", "gate", "axis", "artifact"):
        ids_k = [i for k, i in every if k == kind]
        need(len(ids_k) == len(set(ids_k)), f"duplicate {kind} id")
    need(not any(i.lower() in ("step-0", "gates") for k, i in every if k == "route"), "route ids step-0 and gates are reserved headings")
    ids = {r["id"] for r in n["repos"]}
    axis_ids = {a["id"] for a in n["axes"]}
    for r in n["repos"]:
        need(r.get("class") in CLASSES, f"{r['id']}: class must be one of {sorted(CLASSES)}")
        need(r.get("axis") is None or r["axis"] in axis_ids, f"{r['id']}: unknown axis {r.get('axis')!r}")
        need(isinstance(r.get("gates", []), list) and all(isinstance(g, str) and ID_RE.fullmatch(g) for g in r.get("gates", [])), f"{r['id']}: gates malformed")
    ed = d["edges"]
    need(isinstance(ed, dict) and isinstance(ed.get("types"), dict) and isinstance(ed.get("edges"), list), "edges.yaml needs types and edges")
    for k, v in ed["types"].items():
        need(isinstance(k, str) and ID_RE.fullmatch(k), f"edge type name {k!r} malformed")
        need(ok_text(v), f"edge type {k} description: must be one line of plain text")
    node_ref = re.compile(r"(axis:|gate:|hub:)?[A-Za-z0-9][A-Za-z0-9._-]*")
    for e in ed["edges"]:
        for key in ("from", "to"):
            need(isinstance(e.get(key), str) and node_ref.fullmatch(e[key]), f"edge endpoint {e.get(key)!r} malformed")
        need(e.get("type") in ed["types"], f"edge type {e.get('type')!r} is not declared")
    facet_ids = {f["id"] for f in lens["facets"]}
    # every text that is rendered into Markdown an agent will read
    texts = [("lens.name", lens.get("name")), ("lens.instruction", lens.get("instruction")), ("lens.then", lens.get("then"))]
    texts += [(f"lens facet {f['id']} label", f.get("label")) for f in lens["facets"]]
    texts += [(f"axis {a['id']} question", a.get("question")) for a in n["axes"]]
    for g in n["gates"]:
        texts += [(f"gate {g['id']} name", g.get("name")), (f"gate {g['id']} summary", g.get("summary"))]
    for a in n["artifacts"]:
        texts += [(f"artifact {a['id']} name", a.get("name"))]
    for r in n["repos"]:
        texts.append((f"{r['id']} role", r.get("role")))
        if r.get("surface_note") is not None:
            texts.append((f"{r['id']} surface_note", r["surface_note"]))
        for key in ("is", "is_not"):
            need(isinstance(r.get(key), list), f"{r['id']} {key} must be a list")
            texts += [(f"{r['id']} {key}", t) for t in r[key]]
        need(isinstance(r.get("enter"), list) and r["enter"], f"{r['id']} enter must be a non-empty list")
        need(r.get("doi") is None or (isinstance(r["doi"], str) and re.fullmatch(r"10\.\d{4,9}/[A-Za-z0-9._-]+", r["doi"])), f"{r['id']} doi malformed")
        for sf in r.get("surfaces", []) or []:
            need(isinstance(sf, dict) and sf.get("kind") in SURFACE_KINDS, f"{r['id']} surface kind must be one of {sorted(SURFACE_KINDS)}")
            texts += [(f"{r['id']} surface name", sf.get("name")), (f"{r['id']} surface use", sf.get("use"))]
            for key in ("marketplace", "plugin", "config"):
                need(sf.get(key) is None or (key == "config" and ok_path(sf[key])) or (key != "config" and isinstance(sf[key], str) and ID_RE.fullmatch(sf[key])),
                     f"{r['id']} surface {key} malformed")
            need(sf.get("url") is None or (isinstance(sf["url"], str) and re.fullmatch(rf"https://{OWNER}\.github\.io/{re.escape(r['id'])}/", sf["url"])),
                 f"{r['id']} surface url must be the repository's own pages site")
            need((sf["kind"] == "plugin") == bool(sf.get("marketplace") and sf.get("plugin")), f"{r['id']} plugin surfaces need marketplace and plugin names")
    for r in routes["routes"]:
        need(isinstance(r.get("steps"), list) and r["steps"] and isinstance(r.get("gates"), list), f"route {r['id']} needs steps and gates")
        texts += [(f"route {r['id']} when", r.get("when")), (f"route {r['id']} then", r.get("then"))]
        texts += [(f"route {r['id']} why", st.get("why")) for st in r["steps"] if isinstance(st, dict)]
    for where, t in texts:
        need(ok_text(t), f"{where}: must be one line of plain text (no markup, links, pipes or backticks; at most 400 characters)")
    for s_ in lens["sources"]:
        need(s_.get("facet") in facet_ids, f"lens source {s_.get('repo')}:{s_.get('path')}: unknown facet {s_.get('facet')!r}")
        need(s_.get("read") in ("first", "also"), f"lens source {s_.get('repo')}:{s_.get('path')}: read must be first or also")
    for repo, path, match, label in references(d):
        need(repo in ids, f"{label}: unknown repository {repo!r}")
        need(ok_path(path), f"{label}: unsafe path {path!r}")
        need(match is None or (isinstance(match, str) and match.isprintable()), f"{label}: evidence text must be a single-line printable string")


def safe_lock(d):
    """lock.yaml is data from a pull request: validate every field before it reaches git, a URL or a card."""
    ids = [r["id"] for r in d["nodes"]["repos"]]
    L_all = d["lock"].get("repos") if isinstance(d["lock"], dict) else None
    if not isinstance(L_all, dict) or sorted(L_all) != sorted(ids):
        sys.exit("lock.yaml: repository keys must be exactly the node ids - run `lock`")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(d["lock"].get("generated_on"))):
        sys.exit("lock.yaml: generated_on must be an ISO date")
    for rid, L in L_all.items():
        ok = (isinstance(L, dict) and L.get("url") == f"{HOST}/{OWNER}/{rid}"
              and SHA_RE.fullmatch(str(L.get("commit"))) and PATH_RE.fullmatch(str(L.get("branch")))
              and (L.get("tag") is None or (isinstance(L["tag"], str) and PATH_RE.fullmatch(L["tag"])))
              and (L.get("commits_after_tag") is None or type(L["commits_after_tag"]) is int)
              and isinstance(L.get("paths"), dict))
        if not ok:
            sys.exit(f"lock.yaml: unsafe or malformed entry for {rid!r}")
        for p, blob in L["paths"].items():
            if not ok_path(p) or not SHA_RE.fullmatch(str(blob)):
                sys.exit(f"lock.yaml: unsafe path or blob {p!r} in {rid}")




def no_symlinks():
    """Refuse to run on a tree that contains a symbolic link: nothing here needs one and a link redirects writes and deletes."""
    for p in ROOT.rglob("*"):
        if ".git" in p.relative_to(ROOT).parts[:1]:
            continue
        if p.is_symlink():
            sys.exit(f"refusing to run: {p.relative_to(ROOT)} is a symbolic link")
    for d_ in ("nodes", "graph", "scripts", "githooks"):
        if (ROOT / d_).is_symlink():
            sys.exit(f"refusing to run: {d_} is a symbolic link")


# ---------------------------------------------------------------- loading
def load():
    no_symlinks()
    d = {n: yaml.safe_load((GRAPH / f"{n}.yaml").read_text(encoding="utf-8"))
         for n in ("nodes", "edges", "routes")}
    lock_file = GRAPH / "lock.yaml"
    d["lock"] = yaml.safe_load(lock_file.read_text(encoding="utf-8")) if lock_file.exists() else None
    for e in d["edges"]["edges"]:
        if not all(isinstance(e.get(k), str) for k in ("from", "type", "to")) \
                or not isinstance(e.get("evidence"), dict) or not {"path", "match"} <= set(e["evidence"]):
            sys.exit(f"edges.yaml: edge without evidence path/match: {e.get('from')} {e.get('type')} {e.get('to')}")
    safe_graph(d)
    if d["lock"]:
        safe_lock(d)
    return d


def repo_url(nodes, rid):
    return f"{nodes['host']}/{nodes['owner']}/{rid}"


def references(d):
    """Every (repo, path, match-or-None, label) the graph points at."""
    nodes, out = d["nodes"], []
    for r in nodes["repos"]:
        out += [(r["id"], p, None, f"node {r['id']} enter") for p in r["enter"]]
    for g in nodes["gates"]:
        e = g["defined_in"]
        out.append((e["repo"], e["path"], e.get("match"), f"gate {g['id']}"))
    for a in nodes["artifacts"]:
        for e in [a["source_of_truth"], *a.get("mirrors", []), a["codes_in"]]:
            out.append((e["repo"], e["path"], e.get("match"), f"artifact {a['id']}"))
    for e in d["edges"]["edges"]:
        ev = e["evidence"]
        out.append((ev.get("in", e["from"]), ev["path"], ev["match"], f"edge {e['from']} {e['type']} {e['to']}"))
    for r in d["routes"]["routes"]:
        out += [(s["repo"], s["path"], None, f"route {r['id']}") for s in r["steps"]]
    lens = nodes.get("lens") or {}
    out += [(s.get("repo"), s.get("path"), s.get("match"), f"lens source {s.get('repo')}:{s.get('path')}") for s in lens.get("sources", [])]
    for r in nodes["repos"]:
        for sf in r.get("surfaces", []) or []:
            out.append((r["id"], sf.get("path"), sf.get("match"), f"surface {r['id']} {sf.get('kind')} {sf.get('name')}"))
            if sf.get("config"):
                out.append((r["id"], sf["config"], None, f"surface {r['id']} config"))
    return out


# ---------------------------------------------------------------- git helpers
def git(repo_dir, *args, check=True):
    p = subprocess.run(["git", "-C", str(repo_dir), *args], capture_output=True, text=True)
    if check and p.returncode:
        raise RuntimeError(f"git {' '.join(args)} in {repo_dir}: {p.stderr.strip()}")
    return p.stdout.strip() if p.returncode == 0 else None


def http(url, raw=False):
    req = urllib.request.Request(url, headers={"User-Agent": "main.hub"})
    tok = os.environ.get("GITHUB_TOKEN")
    if tok and "api.github.com" in url:
        req.add_header("Authorization", f"Bearer {tok}")
    with urllib.request.urlopen(req, timeout=30) as r:
        body = r.read()
    return body.decode("utf-8", "replace") if raw else json.loads(body)


# ---------------------------------------------------------------- lock
def cmd_lock(args):
    d = load()
    ws = Path(args.workspace).resolve()
    wanted = {}
    for repo, path, _m, _l in references(d):
        wanted.setdefault(repo, set()).add(path)
    repos = {}
    for r in d["nodes"]["repos"]:
        rid, rdir = r["id"], ws / r["id"]
        head = git(rdir, "symbolic-ref", "--short", "refs/remotes/origin/HEAD", check=False) or "origin/main"
        origin = (git(rdir, "remote", "get-url", "origin") or "").removesuffix(".git").rstrip("/")
        if origin != repo_url(d["nodes"], rid):
            sys.exit(f"lock: {rid}: origin is not the public URL {repo_url(d['nodes'], rid)} - refusing to pin it as public")
        commit = git(rdir, "rev-parse", head)
        tag = git(rdir, "describe", "--tags", "--abbrev=0", commit, check=False)
        after = int(git(rdir, "rev-list", "--count", f"{tag}..{commit}")) if tag else None
        paths = {}
        for p in sorted(wanted.get(rid, ())):
            blob = git(rdir, "rev-parse", f"{commit}:{p}", check=False)
            if blob is not None and git(rdir, "cat-file", "-t", blob, check=False) != "blob":
                sys.exit(f"lock: {rid}:{p} is not a file")
            if blob is None:
                sys.exit(f"lock: {rid}:{p} does not exist at {head} ({commit[:12]})")
            paths[p] = blob
        repos[rid] = {"url": repo_url(d["nodes"], rid), "branch": head.split("/", 1)[1],
                      "commit": commit, "tag": tag, "commits_after_tag": after, "paths": paths}
    out = {"generated_on": date.today().isoformat(),
           "note": "Pins are the PUBLIC default-branch state (origin/<branch>), never local work.",
           "repos": repos}
    (GRAPH / "lock.yaml").write_text(yaml.safe_dump(out, sort_keys=False, width=120), encoding="utf-8")
    print(f"lock: pinned {sum(len(v['paths']) for v in repos.values())} files in {len(repos)} repositories")


# ---------------------------------------------------------------- build
def raw_url(d, repo, path):
    L = d["lock"]["repos"][repo]
    return f"https://raw.githubusercontent.com/{OWNER}/{repo}/{L['commit']}/{urllib.parse.quote(path)}"


def blob_url(d, repo, path):
    L = d["lock"]["repos"][repo]
    return f"{L['url']}/blob/{L['commit']}/{path}"


def render(d):
    """Return {relative path: text} for every generated file."""
    nodes, edges, routes, lock = d["nodes"], d["edges"]["edges"], d["routes"]["routes"], d["lock"]
    out, gates = {}, {g["id"]: g for g in nodes["gates"]}

    # --- ROUTES.md and the AGENTS.md block
    lens = nodes["lens"]
    facet_name = {f["id"]: f["label"] for f in lens["facets"]}
    table = ["| If you are about to... | Go to | Gates |", "|---|---|---|",
             f"| **Anything at all - before you commit to a classification or a route** | [Step 0: {lens['name']}](ROUTES.md#step-0) | - |",
             "| You need a tool rather than a text: a skill to load, an MCP server, an API, a CLI or a package | [SURFACES.md](SURFACES.md) | - |"]
    step0 = ["## Step 0", "", f"**{lens['name']} - mandatory, before any route below.** {lens['instruction']}", "",
             "What the lens says is defined only in the files below. Each line names a file and quotes a phrase that is",
             "checked to occur exactly once in the pinned file; the label before the quote is this hub's paraphrase and is",
             "not machine-verified. Applying the lens before every route is this hub's ordering rule.", ""]
    for title, tag in (("Read first", "first"), ("Also stated in (read the passage around the quoted phrase)", "also")):
        step0 += [f"**{title}**", ""]
        for i, s in enumerate([x for x in lens["sources"] if x["read"] == tag], 1):
            step0.append(f"{i}. `{s['repo']}` / [`{s['path']}`]({blob_url(d, s['repo'], s['path'])}) - {facet_name[s['facet']]}: \"{s['match']}\"  ")
            step0.append(f"   raw: <{raw_url(d, s['repo'], s['path'])}>")
        step0.append("")
    step0 += [f"**Then:** {lens['then']}", ""]
    body = []
    for r in routes:
        first = r["steps"][0]
        table.append(f"| {r['when']} | [`{first['repo']}`](ROUTES.md#{r['id']}) | {', '.join(r['gates']) or '-'} |")
        body += [f"## {r['id']}", "", f"**When:** {r['when']}", ""]
        for i, s in enumerate(r["steps"], 1):
            body.append(f"{i}. `{s['repo']}` / [`{s['path']}`]({blob_url(d, s['repo'], s['path'])}) - {s['why']}  ")
            body.append(f"   raw: <{raw_url(d, s['repo'], s['path'])}>")
        body += ["", f"**Gates:** {', '.join(r['gates']) or 'none'}", "", f"**Then:** {r['then']}", ""]
    gate_lines = ["## Gates", ""]
    for g in nodes["gates"]:
        e = g["defined_in"]
        gate_lines.append(f"- **{g['id']}** - {g['name']}: {g['summary']} Defined in `{e['repo']}` / "
                          f"[`{e['path']}`]({blob_url(d, e['repo'], e['path'])}).")
    out["ROUTES.md"] = "\n".join(
        ["# Routes", "", "GENERATED from `graph/routes.yaml` by `python scripts/hub.py build` - do not hand-edit.",
         f"Every link is pinned to the public commit recorded in `graph/lock.yaml` ({lock['generated_on']}).",
         "A pin is a readout of one moment: compare it with the live default branch before relying on it.",
         "", *table, "", *step0, *body, *gate_lines, ""])
    out["__routes_block__"] = "\n".join(table)

    # --- node cards
    for r in nodes["repos"]:
        L = lock["repos"][r["id"]]
        mine = [e for e in edges if e["from"] == r["id"] or e["to"] == r["id"]]
        c = [f"# {r['id']}", "", "GENERATED from `graph/nodes.yaml` and `graph/edges.yaml` - do not hand-edit.", "",
             f"- **Repository:** <{L['url']}>",
             f"- **Class:** {r['class']}" + (f" - axis `{r['axis']}`" if r.get("axis") else ""),
             f"- **Role:** {r['role']}",
             f"- **Is:** {'; '.join(r['is'])}",
             f"- **Is not:** {'; '.join(r['is_not'])}",
             f"- **Pinned:** `{L['commit'][:12]}` on `{L['branch']}`" + (f", {L['commits_after_tag']} commits after tag `{L['tag']}`" if L["tag"] else ", no release tag"),
             ]
        if r.get("doi"):
            c.append(f"- **Concept DOI:** {r['doi']}")
        if r.get("gates"):
            c.append(f"- **Gates:** {', '.join(r['gates'])}")
        mine_lens = [s for s in lens["sources"] if s["repo"] == r["id"]]
        if r.get("surfaces"):
            c.append("- **Surfaces:** " + "; ".join(f"{sf['kind']} [{sf['name']}]({blob_url(d, r['id'], sf['path'])})" for sf in r["surfaces"]) + " (see `SURFACES.md`)")
        if mine_lens:
            c.append("- **Lens source (Step 0):** " + "; ".join(f"[`{s['path']}`]({blob_url(d, s['repo'], s['path'])})" for s in mine_lens))
        c += ["", "## Read in this order", ""]
        c += [f"{i}. [`{p}`]({blob_url(d, r['id'], p)})" for i, p in enumerate(r["enter"], 1)]
        c += ["", "## Verified edges", ""]
        if not mine:
            c.append("None. This repository is listed for discovery only; no cross-repository relation is claimed.")
        for e in mine:
            ev = e["evidence"]
            src = ev.get("in", e["from"])
            c.append(f"- `{e['from']}` **{e['type']}** `{e['to']}` - evidence: `{src}` / "
                     f"[`{ev['path']}`]({blob_url(d, src, ev['path'])}) contains \"{ev['match']}\"")
        repo_ids = {x["id"] for x in nodes["repos"]}
        near = sorted({x for e in mine for x in (e["from"], e["to"]) if x in repo_ids and x != r["id"]})
        if near:
            c += ["", "## Neighbour cards", "", " · ".join(f"[[{x}]]" for x in near)]
        out[f"nodes/{r['id']}.md"] = "\n".join(c) + "\n"

    # --- SURFACES.md: skills, plugins, MCP servers, APIs, CLIs, packages
    order = ["plugin", "skill", "prompt", "mcp", "api", "static-api", "cli", "package"]
    title = {"plugin": "Installable plugins (skill bundles)", "skill": "Skill files (plain Markdown, any agent can read them)",
             "prompt": "Vendor-neutral prompt packets", "mcp": "MCP servers", "api": "Library and service APIs",
             "static-api": "Static read APIs (no MCP client needed)", "cli": "Command-line tools", "package": "Installable packages"}
    sv = ["# Surfaces", "", "GENERATED from `graph/nodes.yaml` by `python scripts/hub.py build` - do not hand-edit.",
          "Callable and loadable things the public repositories already ship. Every entry is a pinned file in its",
          "repository; plugin and marketplace names are checked against the pinned marketplace manifest. The hub ships",
          "none of these itself: install and run them from their own repository, under that repository's licence and rules.",
          "Apply Step 0 (`ROUTES.md`) and the gates of your route before using any of them.", ""]
    for k in order:
        rows = [(r, sf) for r in nodes["repos"] for sf in (r.get("surfaces") or []) if sf["kind"] == k]
        if not rows:
            continue
        sv += [f"## {title[k]}", ""]
        for r, sf in rows:
            line = f"- **{sf['name']}** (`{r['id']}`) - {sf['use']} File: [`{sf['path']}`]({blob_url(d, r['id'], sf['path'])})"
            if sf.get("config"):
                line += f", client config: [`{sf['config']}`]({blob_url(d, r['id'], sf['config'])})"
            if sf.get("url"):
                line += f", endpoint: <{sf['url']}>"
            if r.get("gates"):
                line += f". Gates: {', '.join(r['gates'])}"
            if r.get("surface_note"):
                line += f". Note: {r['surface_note']}"
            sv.append(line)
            if k == "plugin":
                sv.append(f"  install: `/plugin marketplace add {OWNER}/{r['id']}` then `/plugin install {sf['plugin']}@{sf['marketplace']}` (or as that repository's README states; a plugin installs from the ref its manifest names, which can differ from the file pinned here)")
        sv.append("")
    out["SURFACES.md"] = "\n".join(sv)

    # --- llms.txt
    t = ["# main.hub", "",
         "> One entry point for an AI agent: which public repository of the readout programme answers which",
         "> question, which file to read first, and which gate applies. Pointers and edges only, no content.", "",
         "## Start", "- ROUTES.md#step-0 : read first - the lens every route is preceded by", "- AGENTS.md : the protocol and the route table",
         "- SURFACES.md : skills, plugins, MCP servers, APIs, CLIs and packages the repositories ship", "- ROUTES.md : every route with commit-pinned raw URLs",
         "- graph/hub.json : the whole graph, machine-readable", "- graph/lock.yaml : commit and blob pins", "", "## Repositories"]
    t += [f"- {r['id']} ({r['class']}) : {r['role']} {repo_url(nodes, r['id'])}" for r in nodes["repos"]]
    out["llms.txt"] = "\n".join(t) + "\n"

    # --- hub.json / hub.graphml
    ge_surface = []
    gn = [{"id": "hub:main.hub", "kind": "HUB"}]
    gn += [{"id": f"axis:{a['id']}", "kind": "AXIS", "question": a["question"]} for a in nodes["axes"]]
    gn += [{"id": r["id"], "kind": "REPO", "class": r["class"], "axis": r.get("axis"), "role": r["role"],
            "url": lock["repos"][r["id"]]["url"], "commit": lock["repos"][r["id"]]["commit"],
            "tag": lock["repos"][r["id"]]["tag"], "enter": r["enter"]} for r in nodes["repos"]]
    gn += [{"id": f"gate:{g['id']}", "kind": "GATE", "name": g["name"]} for g in nodes["gates"]]
    gn += [{"id": f"artifact:{a['id']}", "kind": "ARTIFACT", "name": a["name"]} for a in nodes["artifacts"]]
    gn.append({"id": f"lens:{lens['id']}", "kind": "LENS", "name": lens["name"]})
    for r in nodes["repos"]:
        for sf in r.get("surfaces") or []:
            sid = f"surface:{r['id']}:{sf['kind']}:{sf['path']}"
            gn.append({"id": sid, "kind": "SURFACE", "surface": sf["kind"], "name": sf["name"], "path": sf["path"],
                       "marketplace": sf.get("marketplace"), "plugin": sf.get("plugin"), "url": sf.get("url")})
            ge_surface.append({"source": sid, "target": r["id"], "type": "provided-by"})
    ge = [{"source": e["from"], "target": e["to"], "type": e["type"],
           "evidence": {"repo": e["evidence"].get("in", e["from"]), "path": e["evidence"]["path"],
                        "match": e["evidence"]["match"]}} for e in edges]
    ge += ge_surface
    for a in nodes["artifacts"]:
        ge.append({"source": f"artifact:{a['id']}", "target": a["source_of_truth"]["repo"], "type": "source-of-truth-in"})
        ge += [{"source": f"artifact:{a['id']}", "target": m["repo"], "type": "mirrored-in"} for m in a.get("mirrors", [])]
    ge += [{"source": f"lens:{lens['id']}", "target": s["repo"], "type": "stated-in", "facet": s["facet"],
            "evidence": {"repo": s["repo"], "path": s["path"], "match": s["match"]}} for s in lens["sources"]]
    for r in d["routes"]["routes"]:
        gn.append({"id": f"route:{r['id']}", "kind": "ROUTE", "when": r["when"]})
        ge.append({"source": f"route:{r['id']}", "target": f"lens:{lens['id']}", "type": "preceded-by"})
        ge += [{"source": f"route:{r['id']}", "target": s["repo"], "type": "reads", "order": i, "path": s["path"]}
               for i, s in enumerate(r["steps"], 1)]
        ge += [{"source": f"route:{r['id']}", "target": f"gate:{g}", "type": "passes"} for g in r["gates"]]
    out["graph/hub.json"] = json.dumps({"generated_from_lock": lock["generated_on"], "nodes": gn, "edges": ge},
                                       indent=1, ensure_ascii=False) + "\n"
    x = ['<?xml version="1.0" encoding="UTF-8"?>', '<graphml xmlns="http://graphml.graphdrawing.org/xmlns">',
         '<key id="kind" for="node" attr.name="kind" attr.type="string"/>',
         '<key id="type" for="edge" attr.name="type" attr.type="string"/>', '<graph id="main.hub" edgedefault="directed">']
    x += [f'<node id={quoteattr(n["id"])}><data key="kind">{escape(n["kind"])}</data></node>' for n in gn]
    x += [f'<edge source={quoteattr(e["source"])} target={quoteattr(e["target"])}><data key="type">{escape(e["type"])}</data></edge>'
          for e in ge]
    out["graph/hub.graphml"] = "\n".join(x + ["</graph>", "</graphml>"]) + "\n"
    return out


def agents_with_block(block):
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    if BEGIN not in text or END not in text:
        sys.exit("AGENTS.md lost its GENERATED markers")
    return text[: text.index(BEGIN) + len(BEGIN)] + "\n" + block + "\n" + text[text.index(END):]


def cmd_build(_args):
    d = load()
    if not d["lock"]:
        sys.exit("build: run `lock` first")
    problems = []
    check_structure(d, problems.append)
    if problems:
        sys.exit("build: refusing to render an invalid graph:\n  " + "\n  ".join(problems))
    files = render(d)
    block = files.pop("__routes_block__")
    files["AGENTS.md"] = agents_with_block(block)
    keep = {f"{r['id']}.md" for r in d["nodes"]["repos"]}
    nodes_dir = (ROOT / "nodes")
    for stale in nodes_dir.glob("*.md"):
        if stale.name not in keep and not stale.is_symlink() and stale.resolve().parent == nodes_dir.resolve() == ROOT / "nodes":
            stale.unlink()
    for rel, text in files.items():
        raw = ROOT / rel
        if raw.is_symlink() or any(q.is_symlink() for q in raw.parents if ROOT in q.parents or q == ROOT):
            sys.exit(f"build: refusing to write through a symbolic link: {rel}")
        p = raw.resolve()
        if ROOT not in p.parents:
            sys.exit(f"build: refusing to write outside the repository: {rel}")
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    print(f"build: wrote {len(files)} files")


# ---------------------------------------------------------------- check
LEAKS = [r"/home/[a-z]", r"/Users/[A-Za-z]", r"[A-Za-z]:\\\\Users", r"\b192\.168\.\d", r"\b10\.\d+\.\d+\.\d+\b",
         r"\b172\.(1[6-9]|2\d|3[01])\.\d", r"\b127\.0\.0\.1\b", r"localhost:\d", r"(^|[\s`'\"(])~/", r"/root/",
         r"(?<![\w./])[a-z0-9-]+\.(local|lan|internal)\b", r"\b[A-Z]{2,4}-\d{8}-\d+", r"\bDEC-[a-z]", r"\bBBL-\d", r"\bsession_[0-9A-Za-z]{6}",
         r"[\w.+-]+@[\w-]+\.[a-z]{2,}", r"(?i)co-authored-by", r"(?i)\b(claude|anthropic|openai|chatgpt|gemini|codex)\b",
         r"(?i)(password|passwd|secret|api[_-]?key|token)\s*[:=]\s*(?!\$\{\{)\S"]
LEAK_SKIP = {"scripts/hub.py", "githooks/commit-msg"}   # these files DEFINE the patterns


def check_structure(d, err):
    nodes = d["nodes"]
    ids = [r["id"] for r in nodes["repos"]]
    if len(ids) != len(set(ids)):
        err("duplicate repository id")
    known = set(ids) | {f"axis:{a['id']}" for a in nodes["axes"]} | {f"gate:{g['id']}" for g in nodes["gates"]} | {"hub:main.hub"}
    types, touched = d["edges"]["types"], set()
    for e in d["edges"]["edges"]:
        for end in (e["from"], e["to"]):
            if end not in known:
                err(f"edge endpoint unknown: {end}")
        if e["type"] not in types:
            err(f"edge type unknown: {e['type']}")
        if not e.get("evidence", {}).get("match"):
            err(f"edge without evidence text: {e['from']} {e['type']} {e['to']}")
        touched |= {e["from"], e["to"]}
    for r in nodes["repos"]:
        if r["class"] not in CLASSES:
            err(f"{r['id']}: class {r['class']}")
        if r["class"] != "catalog" and r["id"] not in touched:
            err(f"{r['id']}: class {r['class']} but no verified edge - make it `catalog` or add evidence")
        if r["class"] == "catalog" and r["id"] in touched:
            err(f"{r['id']}: has a verified edge, so it is `linked`, not `catalog`")
        for g in r.get("gates", []):
            if f"gate:{g}" not in known:
                err(f"{r['id']}: unknown gate {g}")
    for r in nodes["repos"]:
        if r["class"] == "axis" and not any(e["from"] == r["id"] and e["type"] == "authority-for"
                                            and e["to"] == f"axis:{r.get('axis')}" for e in d["edges"]["edges"]):
            err(f"{r['id']}: class axis but no authority-for edge to axis:{r.get('axis')}")
    axes_held = [r.get("axis") for r in nodes["repos"] if r["class"] == "axis"]
    for a in nodes["axes"]:
        if axes_held.count(a["id"]) != 1:
            err(f"axis {a['id']} must be held by exactly one repository")
    for r in d["routes"]["routes"]:
        for s in r["steps"]:
            if s["repo"] not in ids:
                err(f"route {r['id']}: unknown repository {s['repo']}")
        for g in r["gates"]:
            if f"gate:{g}" not in known:
                err(f"route {r['id']}: unknown gate {g}")
    for repo, _path, match, label in references(d):
        if repo not in ids:
            err(f"{label}: unknown repository {repo}")
        bare = match is not None and re.sub(r"[`*|#\s/]|github\.com|" + OWNER, "", match) in set(ids) | {""}
        if match is not None and (len(match) < MIN_MATCH or match in ids or bare):
            err(f"{label}: evidence text too weak (shorter than {MIN_MATCH} characters or a bare repository name): \"{match}\"")
    for rid in ids:
        if not ID_RE.match(rid):
            err(f"repository id not safe as a directory name: {rid}")
    lens = nodes.get("lens") or {}
    facets = {f["id"] for f in lens.get("facets", [])}
    srcs = lens.get("sources", [])
    if not facets or not srcs:
        err("lens: nodes.yaml must define lens.facets and lens.sources (Step 0)")
    for s in srcs:
        if s.get("facet") not in facets:
            err(f"lens source {s.get('repo')}:{s.get('path')}: unknown facet {s.get('facet')}")
        if not s.get("match"):
            err(f"lens source {s.get('repo')}:{s.get('path')}: no evidence text")
    for f in facets - {s.get("facet") for s in srcs}:
        err(f"lens facet {f} is stated by no source - the hub may not assert a facet on its own")
    if len({s.get("repo") for s in srcs}) < 2:
        err("lens: sources must come from at least two repositories")


def check_pins(d, err, warn, workspace, remote, heads):
    lock = d["lock"]["repos"]
    trees, raws = {}, {}
    for repo, L in lock.items():       # a commit served by the URL may live in a fork: require the default branch
        if workspace:
            rdir = Path(workspace).resolve() / repo
            default = git(rdir, "symbolic-ref", "--short", "refs/remotes/origin/HEAD", check=False) or "origin/main"
            if default != f"origin/{L['branch']}":
                err(f"{repo}: pinned branch {L['branch']} is not the default branch ({default})")
            p = subprocess.run(["git", "-C", str(rdir), "merge-base", "--is-ancestor", L["commit"],
                                f"refs/remotes/origin/{L['branch']}"], capture_output=True)
            if p.returncode:
                err(f"{repo}: pinned commit {L['commit'][:12]} is not on origin/{L['branch']}")
        elif remote:
            try:
                info = http(f"https://api.github.com/repos/{OWNER}/{repo}")
                cmp_ = http(f"https://api.github.com/repos/{OWNER}/{repo}/compare/{L['commit']}...{urllib.parse.quote(L['branch'])}")
                if info.get("default_branch") != L["branch"] or info.get("private") or cmp_.get("status") not in ("ahead", "identical"):
                    err(f"{repo}: pinned commit {L['commit'][:12]} is not on the public default branch")
            except Exception as e:                                   # noqa: BLE001 - any failure is a failed check
                err(f"{repo}: cannot confirm the pinned commit is on the default branch ({e})")
    for repo, path, match, label in references(d):
        L = lock.get(repo)
        if not L or path not in L["paths"]:
            err(f"{label}: {repo}:{path} is not pinned - run `lock`")
            continue
        if workspace:
            rdir = Path(workspace).resolve() / repo
            blob = git(rdir, "rev-parse", f"{L['commit']}:{path}", check=False)
            text = git(rdir, "show", f"{L['commit']}:{path}", check=False) if match else None
        elif remote:
          try:
            if trees.get(repo) == "failed":
                continue
            if repo not in trees:
                t = http(f"https://api.github.com/repos/{OWNER}/{repo}/git/trees/{L['commit']}?recursive=1")
                trees[repo] = None if t.get("truncated") else {i["path"]: i["sha"] for i in t["tree"]}
            if trees[repo] is None:
                c = http(f"https://api.github.com/repos/{OWNER}/{repo}/contents/{urllib.parse.quote(path)}?ref={L['commit']}")
                blob = c["sha"] if isinstance(c, dict) else None   # a directory cannot be verified this way: fail
            else:
                blob = trees[repo].get(path)
            if match and (repo, path) not in raws:
                raws[(repo, path)] = http(raw_url(d, repo, path), raw=True)
            text = raws.get((repo, path)) if match else None
          except Exception as e:                                     # noqa: BLE001
            if trees.get(repo, 0) != "failed":
                err(f"{repo}: cannot read from GitHub ({e}) - set GITHUB_TOKEN if this is a rate limit")
            trees[repo] = "failed"
            continue
        else:
            continue
        if blob != L["paths"][path]:
            err(f"{label}: {repo}:{path} blob {str(blob)[:12]} != pinned {L['paths'][path][:12]}")
        if match and (text is None or match not in text):
            err(f"{label}: evidence text not found in {repo}:{path}: \"{match}\"")
        elif match and text.count(match) != 1:
            err(f"{label}: evidence text occurs {text.count(match)} times in {repo}:{path}, must be exactly 1: \"{match}\"")
    if heads:
        for repo, L in lock.items():
            out = subprocess.run(["git", "ls-remote", "--", L["url"], f"refs/heads/{L['branch']}"], capture_output=True, text=True).stdout
            live = out.split()[0] if out.split() else None
            if live and live != L["commit"]:
                warn(f"{repo}: default branch moved {L['commit'][:12]} -> {live[:12]} since {d['lock']['generated_on']} - re-run `lock`")


EXECUTABLE = {"scripts/hub.py", "githooks/commit-msg", "githooks/pre-commit"}


def check_modes(err):
    for line in (git(ROOT, "ls-files", "-s") or "").splitlines():
        mode, _sha, _stage, rel = line.split(None, 3)
        if mode == "120000":
            err(f"{rel}: symbolic links are not allowed in this repository")
        elif mode == "100755" and rel not in EXECUTABLE:
            err(f"{rel}: unexpected executable bit")
    for p in ROOT.rglob("*"):
        if ".git" not in p.parts and p.is_symlink():
            err(f"{p.relative_to(ROOT)}: symbolic links are not allowed in this repository")


def check_plugins(d, err, workspace, remote):
    """A plugin surface names a marketplace and a plugin: both must be what the pinned manifest says."""
    for r in d["nodes"]["repos"]:
        for sf in r.get("surfaces") or []:
            if sf["kind"] != "plugin" or not (workspace or remote):
                continue
            L = d["lock"]["repos"][r["id"]]
            try:
                raw = (git(Path(workspace).resolve() / r["id"], "show", f"{L['commit']}:{sf['path']}", check=False) if workspace
                       else http(raw_url(d, r["id"], sf["path"]), raw=True))
                m = json.loads(raw or "")
                names = [p.get("name") for p in m.get("plugins", []) if isinstance(p, dict)]
                if m.get("name") != sf["marketplace"] or sf["plugin"] not in names:
                    err(f"surface {r['id']} plugin: manifest says marketplace {m.get('name')!r} plugins {names}, graph says {sf['marketplace']!r} / {sf['plugin']!r}")
            except Exception as e:                                   # noqa: BLE001
                err(f"surface {r['id']} plugin: cannot read the pinned manifest ({e})")


def check_generated(d, err):
    files = render(d)
    files["AGENTS.md"] = agents_with_block(files.pop("__routes_block__"))
    for rel, text in files.items():
        p = ROOT / rel
        if not p.exists() or p.read_text(encoding="utf-8") != text:
            err(f"generated file out of date: {rel} - run `build`")
    for card in (ROOT / "nodes").glob("*"):
        if f"nodes/{card.name}" not in files:
            err(f"nodes/{card.name} is not a generated card - remove it")


def check_leaks(err):
    """Returns the number of organisation-specific patterns that were available."""
    pats = list(LEAKS)
    local = ROOT / ".leakpatterns.local"          # untracked: names that must never appear, one regex per line
    if local.exists():
        extra = [ln.strip() for ln in local.read_text(encoding="utf-8").splitlines() if ln.strip() and not ln.startswith("#")]
        for p in extra:
            try:
                re.compile(p)
            except re.error as e:
                sys.exit(f".leakpatterns.local: bad regex {p!r}: {e}")
        pats += extra
    n_local = len(pats) - len(LEAKS)
    meta = git(ROOT, "log", "--format=%an%n%ae%n%B", check=False) or ""
    tracked = git(ROOT, "ls-files", "--cached", "--others", "--exclude-standard").splitlines()
    for rel in tracked:
        if rel in LEAK_SKIP:
            continue
        try:
            text = (ROOT / rel).read_text(encoding="utf-8")
        except FileNotFoundError:
            continue
        except UnicodeDecodeError:
            err(f"leak scan: {rel} is not UTF-8 text and cannot be scanned")
            continue
        for n, line in enumerate(text.splitlines(), 1):
            if len(line) > 4000 and not rel.startswith("graph/hub."):
                err(f"leak scan: {rel}:{n} is longer than 4000 characters and cannot be scanned safely")
                continue
            for p in pats:
                if "@" in p and "@" not in line:
                    continue
                probe = re.sub(r"\.claude-plugin/(marketplace|plugin)\.json", "", line[:20000]) if "claude" in p else line[:20000]
                if re.search(p, probe):   # the manifest path is a standard file name, not a credit
                    err(f"leak scan: {rel}:{n} matches /{p}/")
    body = git(ROOT, "log", "--format=%B", check=False) or ""
    for p in [q for q in LEAKS if "@" not in q]:
        if re.search(p, body):
            err(f"leak scan: a commit message matches /{p}/")
    for p in pats[len(LEAKS):] + [r"(?i)co-authored-by", r"(?i)noreply@anthropic|noreply@openai"]:
        if re.search(p, meta):
            err(f"leak scan: commit history (author / message) matches /{p}/")
    return n_local


def cmd_check(args):
    d, errors, warnings = load(), [], []
    if not d["lock"]:
        sys.exit("check: run `lock` first")
    safe_lock(d)
    check_structure(d, errors.append)
    check_pins(d, errors.append, warnings.append, args.workspace, args.remote, args.heads)
    check_plugins(d, errors.append, args.workspace, args.remote)
    check_generated(d, errors.append)
    check_modes(errors.append)
    n_local = check_leaks(errors.append)
    if args.strict:
        errors += [f"(strict) {w}" for w in warnings]
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("FAIL ", e)
    mode = "workspace" if args.workspace else "remote" if args.remote else "structure-only (pins NOT re-verified)"
    n_e = len(d["edges"]["edges"])
    print(f"check[{mode}]: {len(d['nodes']['repos'])} repositories, {n_e} edges, {len(d['routes']['routes'])} routes, "
          f"{len(errors)} failures, {len(warnings)} warnings; leak scan used {n_local} organisation-specific patterns"
          + ("" if n_local else " (generic patterns only)"))
    sys.exit(1 if errors else 0)


# ---------------------------------------------------------------- materialize
def cmd_materialize(args):
    d, dest = load(), Path(args.dest).resolve()
    safe_lock(d)
    dest.mkdir(parents=True, exist_ok=True)
    for repo, L in d["lock"]["repos"].items():
        rdir = dest / repo
        if not rdir.exists():
            subprocess.run(["git", "clone", "--filter=blob:none", "--no-checkout", "--quiet", "--", L["url"], str(rdir)], check=True)
        top = git(rdir, "rev-parse", "--show-toplevel", check=False)
        origin = (git(rdir, "remote", "get-url", "origin", check=False) or "").removesuffix(".git")
        if top is None or Path(top).resolve() != rdir.resolve() or origin != L["url"]:
            sys.exit(f"materialize: {rdir} exists but is not a clone of {L['url']} - remove it or choose another --dest")
        git(rdir, "sparse-checkout", "set", "--no-cone", *[f"/{p}" for p in L["paths"]])
        git(rdir, "checkout", "--quiet", L["commit"])
        print(f"materialize: {repo} @ {L['commit'][:12]} ({len(L['paths'])} paths)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("lock"); p.add_argument("--workspace", required=True); p.set_defaults(fn=cmd_lock)
    p = sub.add_parser("build"); p.set_defaults(fn=cmd_build)
    p = sub.add_parser("check"); p.add_argument("--workspace"); p.add_argument("--remote", action="store_true")
    p.add_argument("--heads", action="store_true", help="also warn when a default branch moved past its pin")
    p.add_argument("--strict", action="store_true", help="treat warnings as failures")
    p.set_defaults(fn=cmd_check)
    p = sub.add_parser("materialize"); p.add_argument("--dest", required=True); p.set_defaults(fn=cmd_materialize)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
