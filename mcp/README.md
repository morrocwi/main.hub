# main.hub MCP server

The routing graph as MCP tools over stdio. Stdlib plus PyYAML (and the `git` binary for `hub_check` and the write tools); it calls no model.

```json
{ "mcpServers": { "main-hub": { "command": "python3", "args": ["mcp/server.py"] } } }
```

| Tool | What it returns |
|---|---|
| `hub_start` | **Call first.** The protocol and Step 0: the files that state the readout lens, with pinned raw URLs and the quoted phrases |
| `hub_routes` / `hub_route` | intents, then one route in full: ordered files, why each, gates, what to do after |
| `hub_repos` / `hub_repo` | repositories; one repository with reading order, surfaces, pinned commit and every edge with its quoted evidence |
| `hub_surfaces` | skills, plugins, prompt packets, MCP servers, APIs, CLIs, packages (optional `kind`) |
| `hub_search` | keyword search over routes, repositories, surfaces, gates - a hit is a pointer to read, not an answer |
| `hub_check` | the hub's own checker |
| `hub_add_repo`, `hub_remove_repo`, `hub_register_surfaces` | **write, off by default** |

Write tools need `MAIN_HUB_ALLOW_WRITE=1` and `MAIN_HUB_WORKSPACE=<directory holding the sibling clones>`
in the server's environment. They run the same code as `scripts/hub.py add | remove | surfaces`, edit
the working tree only, and never commit or push: a person reviews the diff.

Test: `python mcp/test_stdio.py` (a real stdio session; every line must print PASS).
