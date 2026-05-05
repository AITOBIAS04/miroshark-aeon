*Feature Built — 2026-05-05*

Simulation Impact Scorecard
Every MiroShark simulation now produces a quantitative scorecard — four normalized metrics that turn qualitative simulation output into machine-comparable numbers. Users can see at a glance how polarized the agents became, whether a few voices dominated, how fast consensus formed, and how turbulent the belief shifts were.

Why this matters:
Until now, MiroShark simulations produced rich narrative output (articles, belief drift charts, leaderboards) but no numeric anchor for comparing runs. A researcher who ran 8 simulations had no way to say 'this one was more polarized than that one' without re-reading both articles. The Impact Scorecard solves the interpretation gap identified in community issue #70 (MiroResult) — but built directly into the product rather than requiring a separate scoring tool. It makes every simulation output programmatically comparable via a single API call.

What was built:
- backend/app/services/scorecard.py: Pure-stdlib computation engine — Gini coefficient for polarization, Herfindahl-Hirschman Index for influence concentration, first-consensus-round ratio for velocity, mean absolute belief-change for volatility. All normalized to 0–100 with tier labels.
- backend/app/api/simulation.py: New GET /api/simulation/:id/scorecard endpoint returning all four metrics with tier labels and hex colors. Returns 404 gracefully when trajectory data is insufficient.
- frontend/src/components/ScorecardPanel.vue: 2×2 metric card grid — each card shows metric name (bilingual zh-CN), large numeric score, color-coded tier badge (LOW/MODERATE/HIGH/CRITICAL), and a context-aware one-line interpretation. Collapsible header, dark theme, responsive.
- frontend/src/views/ExploreView.vue: Gallery cards now show a scorecard chip (e.g. 'Volatile' or 'Fast Consensus') based on the simulation's top-scoring metric — turns the gallery into a dynamics discovery surface.
- backend/openapi.yaml: Full schema documentation for the scorecard endpoint.

How it works:
The scorecard reads trajectory.json (the same file that powers belief drift charts, export CSVs, and share cards) and computes four independent metrics. Polarization uses the Gini coefficient of the final round's bullish/neutral/bearish distribution. Influence Concentration applies the HHI formula to post-share distribution among the top 10 agents in the final 3 rounds. Consensus Velocity finds the first round where any stance exceeds 50% and inverts the ratio against total rounds. Narrative Volatility averages the absolute per-agent belief change across all round transitions. Each is normalized to 0–100 and assigned a tier at 25-point thresholds. The computation is stateless and on-demand — no writes, no caching, no side effects.

What's next:
Inject scorecard context into the article generator prompt so generated articles use quantitative framing ('deeply divided' when polarization is HIGH, 'a small cluster dominated' when influence is CRITICAL). Once GH_GLOBAL is set, this PR along with 4 others will push and merge.

Status: Code complete, push blocked (GH_GLOBAL secret not configured — 5th consecutive feature waiting)
