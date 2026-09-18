#!/usr/bin/env python3
"""main.hub MCP server - the routing graph as tools, over stdio (JSON-RPC 2.0, MCP).

Read tools work on any clone. Write tools (add / remove a repository, register surfaces) edit the
working tree only - they never commit and never push - and are disabled unless the server is started
with MAIN_HUB_ALLOW_WRITE=1 and MAIN_HUB_WORKSPACE pointing at the directory that holds the sibling
clones. Dependencies: Python 3.9+, PyYAML, and the `git` binary for hub_check and the write tools. It calls no model and no network except what
`scripts/hub.py add` itself does (one GitHub API call to confirm a repository is public).
"""
import contextlib
import io
import json
import os
import sys
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import hub  # noqa: E402

PROTOCOL = "2025-06-18"
WRITE = os.environ.get("MAIN_HUB_ALLOW_WRITE") == "1"
WORKSPACE = os.environ.get("MAIN_HUB_WORKSPACE")


def graph():
    d = hub.load()
    if not d["lock"]:
        raise RuntimeError("graph/lock.yaml is missing - run `python scripts/hub.py lock --workspace DIR`")
    return d


def link(d, repo, path):
    return {"repo": repo, "path": path, "raw": hub.raw_url(d, repo, path), "web": hub.blob_url(d, repo, path)}


# ---------------------------------------------------------------- read tools
def t_start(_a):
    d = graph()
    lens = d["nodes"]["lens"]
    facet = {f["id"]: f["label"] for f in lens["facets"]}
    return {"protocol": ["0. lens first (hub_start gives it)", "1. pick a route (hub_routes / hub_route)",
                         "2. read the route's files in order", "3. pass the route's gates",
                         "4. a pin is a readout of one moment; the repository wins over the hub",
                         "5. never copy repository content into the hub"],
            "step0": {"name": lens["name"], "instruction": lens["instruction"], "then": lens["then"],
                      "note": "labels are the hub's paraphrase; only the quoted phrase is machine-checked",
                      "sources": [{**link(d, s["repo"], s["path"]), "read": s["read"], "label": facet[s["facet"]], "quote": s["match"]}
                                  for s in lens["sources"]]},
            "pinned_on": d["lock"]["generated_on"]}


def t_routes(_a):
    return [{"id": r["id"], "when": r["when"], "first_repo": r["steps"][0]["repo"], "gates": r["gates"]} for r in graph()["routes"]["routes"]]


def t_route(a):
    d = graph()
    r = next((r for r in d["routes"]["routes"] if r["id"] == a.get("id")), None)
    if not r:
        raise ValueError(f"unknown route {a.get('id')!r}; call hub_routes")
    gates = {g["id"]: g for g in d["nodes"]["gates"]}
    return {"id": r["id"], "when": r["when"], "then": r["then"], "preceded_by": "step 0 (hub_start)",
            "steps": [{**link(d, s["repo"], s["path"]), "why": s["why"]} for s in r["steps"]],
            "gates": [{"id": g, "name": gates[g]["name"], "summary": gates[g]["summary"],
                       "defined_in": link(d, gates[g]["defined_in"]["repo"], gates[g]["defined_in"]["path"])} for g in r["gates"]]}


def t_repos(_a):
    return [{"id": r["id"], "class": r["class"], "axis": r.get("axis"), "role": r["role"], "draft": bool(r.get("draft")),
             "url": f"{hub.HOST}/{hub.OWNER}/{r['id']}"} for r in graph()["nodes"]["repos"]]


def t_repo(a):
    d = graph()
    r = next((r for r in d["nodes"]["repos"] if r["id"] == a.get("id")), None)
    if not r:
        raise ValueError(f"unknown repository {a.get('id')!r}; call hub_repos")
    L = d["lock"]["repos"][r["id"]]
    edges = [e for e in d["edges"]["edges"] if r["id"] in (e["from"], e["to"])]
    return {"id": r["id"], "class": r["class"], "axis": r.get("axis"), "role": r["role"], "is": r["is"], "is_not": r["is_not"],
            "draft": bool(r.get("draft")), "gates": r.get("gates", []), "doi": r.get("doi"),
            "pinned": {"commit": L["commit"], "branch": L["branch"], "tag": L["tag"], "commits_after_tag": L["commits_after_tag"]},
            "read_in_order": [link(d, r["id"], p) for p in r["enter"]],
            "surfaces": surfaces_of(d, r),
            "edges": [{"from": e["from"], "type": e["type"], "to": e["to"],
                       "evidence": {**link(d, e["evidence"].get("in", e["from"]), e["evidence"]["path"]), "quote": e["evidence"]["match"]}} for e in edges]}


def surfaces_of(d, r):
    out = []
    for sf in r.get("surfaces") or []:
        item = {"repo": r["id"], "kind": sf["kind"], "name": sf["name"], "use": sf["use"], **{k: v for k, v in link(d, r["id"], sf["path"]).items() if k != "repo"},
                "gates": r.get("gates", []), "note": r.get("surface_note")}
        if sf["kind"] == "plugin":
            item["install"] = [f"/plugin marketplace add {hub.OWNER}/{r['id']}", f"/plugin install {sf['plugin']}@{sf['marketplace']}"]
        if sf.get("url"):
            item["endpoint"] = sf["url"]
        if sf.get("config"):
            item["client_config"] = link(d, r["id"], sf["config"])
        out.append(item)
    return out


def t_surfaces(a):
    d = graph()
    kind = a.get("kind")
    if kind is not None and kind not in hub.SURFACE_KINDS:
        raise ValueError(f"kind must be one of {sorted(hub.SURFACE_KINDS)}")
    return [s for r in d["nodes"]["repos"] for s in surfaces_of(d, r) if kind in (None, s["kind"])]


def t_search(a):
    q = str(a.get("query") or "").lower().split()
    if not q:
        raise ValueError("query is empty")
    d = graph()
    hay = []
    for r in d["routes"]["routes"]:
        hay.append(("route", r["id"], " ".join([r["id"], r["when"], r["then"], *[s["why"] for s in r["steps"]]])))
    for r in d["nodes"]["repos"]:
        hay.append(("repo", r["id"], " ".join([r["id"], r["role"], *r["is"], *r["is_not"]])))
        for sf in r.get("surfaces") or []:
            hay.append(("surface", f"{r['id']}:{sf['kind']}:{sf['path']}", " ".join([sf["name"], sf["use"], sf["kind"], r["id"]])))
    for g in d["nodes"]["gates"]:
        hay.append(("gate", g["id"], " ".join([g["id"], g["name"], g["summary"]])))
    scored = [(sum(w in text.lower() for w in q), kind, ident, text) for kind, ident, text in hay]
    return [{"kind": k, "id": i, "text": t[:240]} for s, k, i, t in sorted(scored, key=lambda x: -x[0]) if s][:12]


def run_hub(fn, **kw):
    """Run a hub.py command in-process, capturing what it prints; SystemExit becomes an error message."""
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            fn(SimpleNamespace(**kw))
        return {"ok": True, "output": buf.getvalue().strip().splitlines()}
    except SystemExit as e:
        return {"ok": e.code in (0, None), "output": buf.getvalue().strip().splitlines() + ([str(e.code)] if isinstance(e.code, str) else [])}


def t_check(_a):
    return run_hub(hub.cmd_check, workspace=WORKSPACE, remote=False, heads=False, strict=False)


# ---------------------------------------------------------------- write tools (working tree only)
def need_write():
    if not WRITE or not WORKSPACE:
        raise PermissionError("write tools are off: start the server with MAIN_HUB_ALLOW_WRITE=1 and MAIN_HUB_WORKSPACE=<dir of sibling clones>")


def changed():
    return (hub.git(ROOT, "status", "--short", check=False) or "").splitlines()


def t_add(a):
    need_write()
    res = run_hub(hub.cmd_add, repo=str(a.get("repo")), workspace=WORKSPACE)
    return {**res, "changed_files": changed(), "next": "review the draft node, then hub_check; this tool never commits or pushes"}


def t_remove(a):
    need_write()
    res = run_hub(hub.cmd_remove, repo=str(a.get("repo")), workspace=WORKSPACE)
    return {**res, "changed_files": changed(), "next": "review the diff, then hub_check; this tool never commits or pushes"}


def t_register(a):
    need_write()
    res = run_hub(hub.cmd_surfaces, repo=a.get("repo"), workspace=WORKSPACE)
    return {**res, "changed_files": changed(), "next": "sharpen the generic `use` texts from the repository's own files, then hub_check"}


STR = {"type": "string"}
TOOLS = {
    "hub_start": (t_start, "Call this first. Returns the protocol and Step 0: the files that state the readout lens, to read before classifying or routing any problem.", {}),
    "hub_routes": (t_routes, "List every route: the intent it serves, the first repository and its gates.", {}),
    "hub_route": (t_route, "One route in full: ordered files to read (commit-pinned raw URLs), why each, the gates and what to do after.", {"id": STR}),
    "hub_repos": (t_repos, "List the repositories with class, axis and one-line role.", {}),
    "hub_repo": (t_repo, "One repository: role, is / is not, reading order, surfaces, pinned commit and every verified edge with its quoted evidence.", {"id": STR}),
    "hub_surfaces": (t_surfaces, "Skills, plugins, prompt packets, MCP servers, APIs, CLIs and packages the repositories ship; optional kind filter.", {"kind": STR}),
    "hub_search": (t_search, "Keyword search over routes, repositories, surfaces and gates. A hit is a pointer to read, not an answer.", {"query": STR}),
    "hub_check": (t_check, "Run the hub's own checker (against the sibling clones when MAIN_HUB_WORKSPACE is set, structure-only otherwise).", {}),
    "hub_add_repo": (t_add, "WRITE (off by default): add a public repository as a draft catalog node with discovered surfaces. Edits the working tree only.", {"repo": STR}),
    "hub_remove_repo": (t_remove, "WRITE (off by default): remove a repository and every edge and route step that names it. Edits the working tree only.", {"repo": STR}),
    "hub_register_surfaces": (t_register, "WRITE (off by default): register newly shipped skills, plugins, MCP servers, APIs of one repository, or of all when repo is omitted.", {"repo": STR}),
}
REQUIRED = {"hub_route": ["id"], "hub_repo": ["id"], "hub_search": ["query"], "hub_add_repo": ["repo"], "hub_remove_repo": ["repo"]}


def handle(msg):
    if not isinstance(msg, dict):
        return {"jsonrpc": "2.0", "id": None, "error": {"code": -32600, "message": "a request must be a JSON object"}}
    method, mid = msg.get("method"), msg.get("id")
    if mid is None and method != "initialize":   # a notification: never executed, never answered
        return None
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": mid, "result": {"protocolVersion": PROTOCOL, "capabilities": {"tools": {}},
                "serverInfo": {"name": "main.hub", "version": "1.0.0"},
                "instructions": "Call hub_start first: the lens precedes routing. The hub holds pointers only; the repository wins over the hub."}}
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": mid, "result": {"tools": [
            {"name": n, "description": desc, "inputSchema": {"type": "object", "properties": props, "required": REQUIRED.get(n, []), "additionalProperties": False}}
            for n, (_f, desc, props) in TOOLS.items()]}}
    if method == "tools/call":
        p = msg.get("params")
        if not isinstance(p, dict) or not isinstance(p.get("name"), str):
            return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32602, "message": "params must be an object with a string `name`"}}
        name, args = p["name"], p.get("arguments")
        args = {} if args is None else args
        if name not in TOOLS:
            return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32602, "message": f"unknown tool {name[:80]!r}"}}
        if not isinstance(args, dict):
            return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32602, "message": "`arguments` must be an object"}}
        try:
            missing = [k for k in REQUIRED.get(name, []) if not isinstance(args.get(k), str)]
            if missing:
                raise ValueError(f"missing string argument(s): {missing}")
            data = TOOLS[name][0](args)
            err = isinstance(data, dict) and data.get("ok") is False      # a refused write or a failing check is an error
        except SystemExit as e:                  # hub.py refuses by exiting: report it, keep serving
            data, err = {"error": str(e.code)}, True
        except Exception as e:                   # noqa: BLE001
            data, err = {"error": f"{type(e).__name__}: {e}"}, True
        return {"jsonrpc": "2.0", "id": mid, "result": {"content": [{"type": "text", "text": json.dumps(data, ensure_ascii=False, indent=1)}], "isError": err}}
    if method == "ping":
        return {"jsonrpc": "2.0", "id": mid, "result": {}}
    return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": f"method not found: {method}"}}


def main():
    for raw in sys.stdin.buffer:                 # bytes in: a line that is not UTF-8 must not end the session
        line = raw.decode("utf-8", "replace").strip()
        if not line:
            continue
        if len(raw) > 1_000_000:
            reply = {"jsonrpc": "2.0", "id": None, "error": {"code": -32600, "message": "request too large"}}
        else:
            try:
                reply = handle(json.loads(line))
            except ValueError:
                reply = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "parse error"}}
            except BaseException as e:           # noqa: BLE001 - one bad request must not end the session
                if isinstance(e, KeyboardInterrupt):
                    raise
                reply = {"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": f"internal error: {type(e).__name__}"}}
        if reply is not None:
            sys.stdout.write(json.dumps(reply, ensure_ascii=True) + "\n")   # ASCII-safe: a lone surrogate cannot break the stream
            sys.stdout.flush()


if __name__ == "__main__":
    main()
