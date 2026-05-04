*Feature Built — 2026-05-04*

Programmatic Agent Interrogation API
MiroShark's most distinctive feature — the Trace Interview, where you cross-examine a simulated agent on its actual posts and stance changes — was locked inside the browser UI. The Agent Interrogation API breaks it open for automation. Four new endpoints let any pipeline list agents, fetch full profiles with per-round belief trajectories, and ask agents trace-grounded questions programmatically with multi-turn session support.

Why this matters:
The completion webhook (PR #46) and OpenAPI spec opened MiroShark to programmatic use, but the feature that makes MiroShark unique — interrogating agents about their reasoning — had no API surface. Researchers running batch studies had to click through the UI agent by agent. n8n and Zapier workflows could trigger simulations and get final results but couldn't ask 'Why did the top agent flip bearish at round 7?' This was the #3 idea from repo-actions (May 2) and the highest-leverage small-effort addition: one API surface unlocks the most differentiated capability for the entire automation audience.

What was built:
- backend/app/api/simulation.py: 4 new endpoints — GET /agents (list all agents with metadata, stance, influence rank), GET /agents/<name>/profile (full bio + per-round belief history from trajectory.json), POST /agents/<name>/query (trace-grounded interrogation with server-side session management and rate limiting), GET /interview-sessions (list all saved sessions)
- backend/openapi.yaml: New 'Agent Interrogation' tag with full request/response schemas, 8 example questions in the spec
- frontend/src/api/simulation.js: 4 new API functions (listSimulationAgents, getAgentProfile, queryAgent, listInterviewSessions)
- docs/API.md + docs/API.zh-CN.md: New section with curl examples
- docs/FEATURES.md + docs/FEATURES.zh-CN.md: Feature documentation
- README.md: Added to features table

How it works:
The /query endpoint reuses the exact context-building logic from the UI trace interview: it loads the agent's profile from reddit_profiles.json, the simulation scenario from config, and builds a complete round-by-round trace from the JSONL action logs. The agent responds in character, citing specific posts and round numbers. Server-side sessions (via session_id parameter) persist the last 4 Q&A pairs on disk for multi-turn dialogue — callers don't need to manage history. Rate limiting (20 queries per simulation per 5 minutes) prevents cost explosions from automation loops. All queries are also saved to the shared interview transcript, so UI and API interrogations appear in the same history.

What's next:
GH_GLOBAL secret still not set — this is the 4th consecutive feature blocked from pushing (May 1–4). Once the secret is configured, 4 PRs ship immediately. Next feature candidates: Fork/Counterfactual Diff View, Mid-Run Belief Threshold Alert Webhooks, Simulation Series Tracker.

Branch: feat/agent-interrogation-api (push blocked — GH_GLOBAL not set)
