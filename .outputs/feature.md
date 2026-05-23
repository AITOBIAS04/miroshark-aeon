## Summary

**Feature built: MCP Simulation Tools** for `aaronjmars/MiroShark`

Added 5 simulation tools to the existing MCP server, extending it from knowledge-graph-only (8 tools) to a complete MiroShark proxy (13 tools). AI assistants using Claude Desktop, Cursor, Windsurf, or Continue can now:

| Tool | What it does |
|---|---|
| `search_gallery` | Search published simulations by keyword, consensus, quality, sort |
| `get_simulation` | Full simulation details: status, scenario, config, timestamps |
| `get_run_status` | Real-time progress: round count, percent complete, action totals |
| `get_agent_stats` | Per-agent statistics: posts, engagement, follows |
| `get_simulation_posts` | Read what agents wrote during a simulation |

**Files modified (9 files, +699 lines):**
- `backend/mcp_server.py` — 5 Tool definitions + HTTP client via `urllib.request`
- `backend/app/api/mcp.py` — tool catalog synced (13 total)
- `backend/tests/test_unit_mcp_simulation.py` — 18 offline unit tests
- `docs/MCP.md` — simulation tools table, example prompts, troubleshooting
- `docs/FEATURES.md` — feature section
- `.env.example` — `MIROSHARK_API_URL` documented
- `backend/openapi.yaml` — McpStatus description updated
- `frontend/src/api/simulation.js` — `getMcpStatus` helper
- `frontend/src/components/EmbedDialog.vue` — MCP tools chip section

**Zero new dependencies** (streak: 32 PRs). Branch `feat/mcp-simulation-tools` committed locally — push blocked by missing `GH_GLOBAL` secret (22nd consecutive block).
