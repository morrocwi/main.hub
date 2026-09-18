#!/usr/bin/env python3
"""Real stdio round trip against mcp/server.py. Exit code 0 only if every expectation holds."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


import os

CLEAN = {k: v for k, v in os.environ.items() if not k.startswith("MAIN_HUB_")}   # never run write tools from a test


def session(requests, env=CLEAN):
    p = subprocess.run([sys.executable, str(ROOT / "mcp" / "server.py")], input="\n".join(json.dumps(r) for r in requests) + "\n",
                       capture_output=True, text=True, env=env, timeout=120)
    return [json.loads(line) for line in p.stdout.splitlines() if line.strip()]


def call(i, name, **args):
    return {"jsonrpc": "2.0", "id": i, "method": "tools/call", "params": {"name": name, "arguments": args}}


def body(reply):
    return json.loads(reply["result"]["content"][0]["text"]), reply["result"]["isError"]


out = session([
    {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}},
    {"jsonrpc": "2.0", "method": "notifications/initialized"},
    {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
    call(3, "hub_start"), call(4, "hub_routes"), call(5, "hub_route", id="equation"), call(6, "hub_repo", id="toledo"),
    call(7, "hub_surfaces", kind="mcp"), call(8, "hub_search", query="equation lookup"), call(9, "hub_route", id="no-such-route"),
    call(10, "hub_add_repo", repo="anything"), call(11, "hub_repo"), {"jsonrpc": "2.0", "id": 12, "method": "nope"},
    [1, 2], 42, {"jsonrpc": "2.0", "id": 13, "method": "tools/call", "params": ["x"]},
    {"jsonrpc": "2.0", "id": 14, "method": "tools/call", "params": {"name": ["x"]}},
    {"jsonrpc": "2.0", "id": 15, "method": "tools/call", "params": {"name": "hub_start", "arguments": "x"}},
    {"jsonrpc": "2.0", "method": "tools/call", "params": {"name": "hub_start"}},
    {"jsonrpc": "2.0", "id": 16, "method": "ping"},
])
by_id = {r.get("id"): r for r in out if r.get("id") is not None}
checks = {
    "initialize": by_id[1]["result"]["serverInfo"]["name"] == "main.hub",
    "notifications get no reply, bad lines get one each": len(out) == 18,
    "server survives malformed requests": by_id[16]["result"] == {},
    "malformed params are protocol errors": all(by_id[i]["error"]["code"] == -32602 for i in (13, 14, 15)),
    "tools listed": len(by_id[2]["result"]["tools"]) == 11,
    "start returns lens sources": len(body(by_id[3])[0]["step0"]["sources"]) >= 4,
    "routes listed": any(r["id"] == "equation" for r in body(by_id[4])[0]),
    "route has pinned raw urls": body(by_id[5])[0]["steps"][0]["raw"].startswith("https://raw.githubusercontent.com/morrocwi/toledo/"),
    "repo has quoted evidence": all(e["evidence"]["quote"] for e in body(by_id[6])[0]["edges"]),
    "surface filter": {s["kind"] for s in body(by_id[7])[0]} == {"mcp"},
    "search finds the equation route": body(by_id[8])[0][0]["id"] in ("equation", "toledo"),
    "unknown route is a tool error": body(by_id[9])[1] is True,
    "write tools are off by default": body(by_id[10])[1] is True and "write tools are off" in body(by_id[10])[0]["error"],
    "missing argument is a tool error": body(by_id[11])[1] is True,
    "unknown method is a protocol error": by_id[12]["error"]["code"] == -32601,
}
raw = subprocess.run([sys.executable, str(ROOT / "mcp" / "server.py")], env=CLEAN, capture_output=True, timeout=60,
                     input=b'{"jsonrpc":"2.0","id":1,"method":"ping"}\n\xff\xfe\n{"jsonrpc":"2.0","id":2,"method":"ping"}\n')
replies = [json.loads(x) for x in raw.stdout.decode().splitlines() if x.strip()]
checks["invalid UTF-8 gets a parse error and the session continues"] = (
    raw.returncode == 0 and [r.get("id") for r in replies] == [1, None, 2] and replies[1]["error"]["code"] == -32700)
for name, ok in checks.items():
    print("PASS" if ok else "FAIL", name)
sys.exit(0 if all(checks.values()) else 1)
