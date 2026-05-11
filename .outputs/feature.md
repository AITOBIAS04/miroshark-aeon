🔬 Feature Built: Simulation A/B Comparison View

Today's feature adds a full comparison mode to MiroShark — pick any two simulations and see exactly how they differ.

What's new:

Backend: The /compare endpoint now returns belief drift trajectories, quality diagnostics, scenario text, and a scorecard object with 4 metrics (participation rate, stance diversity, convergence round, cross-platform rate). Each metric shows values for both sims plus a delta, and the scorecard highlights which metric diverges most.

ComparisonView: Complete rewrite (~640 lines). Two display modes for belief drift — side-by-side (independent charts per sim) or overlay (shared axis, Sim A in orange, Sim B in green, bearish lines dashed). A scorecard table color-codes each metric by quality tier with a Δ column. Health badges, scenario cards, and a share button round it out.

Gallery Compare Mode: Hover any card in the gallery and a compare checkbox appears. Select two sims → a floating banner slides up from the bottom with a 'Compare selected →' button. Third click replaces the oldest selection.

Also: 9 unit tests for scorecard diff logic, OpenAPI spec updates, bilingual docs (EN + ZH), README update.

8 files changed, 1,051 insertions. Branch: feat/ab-comparison-view.

⚠️ Push blocked — GH_GLOBAL secret not set (day 11). PR could not be opened. 11 features now waiting as local commits.
