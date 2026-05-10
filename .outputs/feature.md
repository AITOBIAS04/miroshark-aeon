*Feature Built — 2026-05-10*

Per-Agent Trajectory Export
MiroShark simulations now have individual-level data export. Researchers and analysts can download a CSV or JSONL file containing one row for every agent in every round — showing each agent's belief mean, stance label (BULLISH/NEUTRAL/BEARISH), how many posts they made that round, whether they changed stance, and whether they were the top influencer. This is the unit-record dataset that statistical tools actually need to operate on.

Why this matters:
The existing trajectory export (PR #66) is aggregate-only: one row per round with the overall bullish/neutral/bearish percentages. That's a summary — useful for charts, but insufficient for any individual-level analysis. Researchers doing influence attribution ("which agent caused the cascade?"), survival analysis ("when do different archetypes flip?"), or archetype clustering ("do traders behave differently from analysts?") need the per-agent rows. With 222 forks and a growing academic cohort, this closes the gap between MiroShark as an illustration tool and MiroShark as a primary research instrument. Directly addresses the criticism in 'Position: AI Agents Are Not (Yet) a Panacea for Social Simulation' about the absence of individual-level data export.

What was built:
- backend/app/services/agent_trajectory_export.py: New export service (237 lines). Reads trajectory.json + agent profiles (reddit_profiles.json / twitter_profiles.csv). Produces one row per agent × round. Same ±0.2 stance threshold as every other surface.
- backend/app/api/simulation.py: Two new endpoints — GET /agent-trajectory.csv and GET /agent-trajectory.jsonl. Same publish gate and caching as the aggregate trajectory export.
- frontend/src/components/EmbedDialog.vue: New 'Export per-agent trajectory' section with download buttons (.csv + .jsonl), copyable URL, and pandas quickstart snippet. Bilingual (EN + zh-CN).
- backend/tests/test_unit_agent_trajectory.py: 18 unit tests covering stance classification, stance-change tracking, post counts, top-influencer flagging, profile enrichment, CSV/JSONL rendering, degradation on missing data, and route decorator presence.
- backend/openapi.yaml: Full endpoint specs + AgentTrajectoryRow schema.
- docs + README: Bilingual documentation across API.md, FEATURES.md, and README.md.

How it works:
The service reads the same trajectory.json every other export surface uses, then expands each round's belief_positions map into individual rows. For each agent × round, it computes the mean belief across all tracked topics, classifies the stance using the standard ±0.2 threshold, counts posts from viral_posts, and flags stance transitions by comparing against the previous round. Agent names and archetypes are enriched from the profile files when available. The CSV renderer serializes booleans as 'true'/'false' strings for pandas compatibility. The JSONL form emits one JSON object per line with the same locked column order.

What's next:
Push is blocked — GH_GLOBAL secret still not set (10th consecutive block, May 1–10). Once the secret is configured, this PR and 9 others can be pushed and opened.

PR: push blocked — code complete on branch feat/per-agent-trajectory-export
