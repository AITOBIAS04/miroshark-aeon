Feature Built — 2026-05-25

Simulation Confidence Score
MiroShark simulations now carry a single-number trust signal — a Confidence Score from 0 to 100 — that tells downstream tools, curators, and governance teams how much they can rely on a given simulation consensus. Instead of eyeballing a green/yellow/red quality badge, a quant pipeline can now filter by ?min_confidence=75 and only act on high-trust runs.

Why this matters:
MiroShark is becoming infrastructure that other tools consume (signal.json for trading bots, polymarket.json for prediction markets, the gallery API for dashboards). Those integrators need a finer-grained trust gate than the coarse quality_health label. The Confidence Score fills that gap: a score of 87 means the consensus stabilized, agents participated broadly, and the adversarial variant (if run) did not collapse it. A score of 23 means the run was noisy, split, or fragile. This is the signal that makes automated workflows production-safe rather than experimental.

What was built:
- confidence_service.py: Pure-stdlib service computing four components — Stability (did consensus hold in the second half?), Convergence (how decisive was the final outcome?), Participation (did agents actually post?), Robustness (did adversarial agents break it?) — each 0-25, summed to 0-100. Cached deterministically to confidence.json.
- GET /api/simulation/id/confidence: New analytics endpoint returning the score with full component breakdown. Same publish gate as every other surface.
- Gallery integration: confidence_score field on every gallery card, ?min_confidence filter with chips (60+/75+/90+) in the Explore view, and a blue confidence badge on cards scoring 70+.
- signal.json: confidence_score now rides inside the trading signal payload at zero additional API cost.
- EmbedDialog: Confidence section showing the 0-100 score with all four component bars.
- 14 unit tests, OpenAPI ConfidenceResponse schema, bilingual docs.

How it works:
The service reads trajectory.json and computes Stability as the inverse of round-over-round std dev in the second half of rounds, and Convergence as distance of the final bullish pct from 50 pct. Participation comes from quality.json participation_rate. Robustness checks adversarial_report.json first (mapping high/medium/low/collapse to 25/18/8/0), falls back to coalition modularity, or defaults to 15. All four components are clamped 0-25; sum clamped 0-100. Written atomically to confidence.json and never recomputed.

What is next:
Could add confidence-weighted trending sort or minimum confidence thresholds for automated webhook triggers.

(code complete, push blocked — GH_GLOBAL not set)
