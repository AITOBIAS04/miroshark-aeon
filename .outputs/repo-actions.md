*Repo Action Ideas — 2026-05-16*
Generated from analysis of aaronjmars/MiroShark (1,164 stars · 232 forks · 1 open PR).

1. Private Share Links with Expiry (Feature, Small)
   Token-signed, expiring URLs for sharing unpublished simulations privately — no gallery indexing, per-link revocation, configurable 24h/7d/never TTL.

2. Adversarial Stress-Test Mode (Feature, Small)
   Designate 1–3 agents as adversarial challengers; computes a consensus robustness verdict (HIGH/MEDIUM/LOW/COLLAPSE) showing whether the finding holds under direct rhetorical pressure.

3. Weekly Simulation Digest (Feature/Community, Small)
   Auto-generated /digest/latest page + GET /api/digest/weekly JSON — top 5 simulations by composite engagement score, plus an Atom digest-feed variant for RSS subscribers.

4. Curator Collections (Community/Feature, Small)
   Named, ordered lists of published simulations with shareable /collections/<id> URLs — lets researchers build citation bundles and curated arguments, not just browse the algorithmic feed.

5. Scenario Pre-flight Analyzer (DX, Small)
   Pure-heuristic GET /api/scenario/analyze endpoint analyzes scenario text before launch: controversy score, consensus lean, recommended agent count, and quality risk flags — zero LLM cost, instant feedback in the Step 1 UI.

Full details: https://github.com/AITOBIAS04/miroshark-aeon/blob/main/articles/repo-actions-2026-05-16.md
