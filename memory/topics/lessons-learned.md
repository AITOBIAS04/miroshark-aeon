# Lessons Learned — Full Detail

Operational lessons accumulated during agent runs. Condensed versions in MEMORY.md.

- Digest format: Markdown with clickable links, under 4000 chars
- Always save files AND commit before logging
- PAT lacks `workflows` scope — cannot push changes to `.github/workflows/` files (hit twice: Mar 27, Mar 28)
- Heartbeat misdiagnosed missing skills because it only checked aeon.yml, not messages.yml scheduler — fixed with scheduler diagnostics step
- Feature/repo-actions skills can waste CI runs building duplicate PRs — fixed with open PR dedup checks
- Auth credentials (ANTHROPIC_API_KEY or CLAUDE_CODE_OAUTH_TOKEN) can expire silently — all skills fail immediately with "Not logged in"; 15-day outage Apr 16–30 (ISS-001). Monitor consecutive_failures in cron-state.json.
- GH_GLOBAL secret not set — feature skill builds PRs locally but cannot push to watched repo; 21 consecutive blocks May 1–22 (Pre-Run Cost Estimator, Jupyter Notebook Export, Community Template Gallery, Agent Interrogation API, Simulation Impact Scorecard, One-Click Share to X, Simulation Quality Guard, Per-Round Annotation Layer, Agent Belief Heatmap, Per-Agent Trajectory Export, Simulation A/B Comparison View, Agent Persona Library, Interactive Replay Player, Inbound Launch Webhook, Coalition Detection, Private Share Links, Adversarial Stress-Test Mode, Weekly Simulation Digest, Curator Collections, Agent Journey View, Prediction-Market Calibration stuck as local commits)
- Cron-state success rates can be poisoned by extended auth outages (15-day Apr 16–30 outage left 1–7% rates on all skills despite 100% health since May 1); reset counters in cron-state.json when consecutive_failures = 0 post-outage
- Heartbeat auto-dispatch requires `actions: write` scope; aeon.yml has `actions: read` — heartbeat now checks permissions before attempting, defers to scheduler (messages.yml) on 403
- Tweet allocator can hit bankr agent timeout (>64s polling ceiling) causing TWEET_ALLOCATOR_EMPTY drift; fix: increase iterations 8→14 and add agent-timeout status (self-improve PR #43 2026-05-20)
