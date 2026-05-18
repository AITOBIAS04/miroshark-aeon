Feature Built — 2026-05-18

Adversarial Stress-Test Mode

MiroShark simulations can now include adversarial agents — contrarian participants deliberately programmed to argue against whatever consensus is forming. After the simulation completes, operators get a robustness report that shows whether the group's conclusion held up under pressure or collapsed. Think of it as a stress test for collective intelligence: did the swarm reach its conclusion because the evidence was strong, or because nobody pushed back?

Why this matters:
Every simulation platform can show you what a group concluded. Very few can tell you how fragile that conclusion was. In governance, forecasting, and policy simulation, the difference between "95% agreement" and "95% agreement that collapses when one agent dissents" is everything. This was the #2 priority from last week's repo-actions analysis — Private Share Links shipped yesterday, and Adversarial Mode was next. It directly supports MiroShark's positioning as a serious research tool, not a consensus echo chamber.

What was built:
- backend/app/services/adversarial.py: Pure-stdlib adversarial service — agent selection (top agent_ids, clamped at 3), contrarian prompt suffix injection, and robustness computation comparing halfway-point vs final consensus. Four robustness tiers: high (≤10% drift), medium (10-25%), low (>25%), collapse (direction reversed). Key moment detection flags rounds where consensus shifted >8%.
- backend/app/api/simulation.py: New GET /adversarial-report endpoint; create_simulation accepts adversarial_agent_count parameter; gallery cards include adversarial metadata.
- backend/app/services/simulation_manager.py: SimulationState extended with adversarial_agent_count field; Phase 4 in prepare_simulation selects adversarial agents and saves config.
- backend/app/services/gallery_filters.py: adversarial_only filter for the public gallery.
- frontend Step1GraphBuild.vue: Toggle checkbox + 1/2/3 agent count selector in simulation setup, styled with red accent.
- frontend Step3Simulation.vue: Expandable adversarial panel showing robustness verdict, drift metrics (pre vs post consensus), and a key moments timeline.
- frontend InteractionNetwork.vue: Adversarial nodes rendered with red dashed outlines + legend entry.
- frontend ExploreView.vue: Adversarial filter chip in gallery header + pill badge on cards.
- 16 unit tests covering agent selection, prompt building, all robustness tiers, persistence, and report structure.
- OpenAPI spec updated with AdversarialReport schema.

How it works:
When an operator enables adversarial mode in Step 1, the backend selects the top N agents by ID (up to 3) and injects a contrarian prompt suffix into their system prompts during simulation. The suffix instructs the agent to challenge the emerging consensus, present counter-evidence, and argue for minority positions. After the simulation completes, the robustness engine loads the trajectory, identifies the halfway snapshot, computes consensus at that midpoint and at the end, then measures the drift. If consensus direction flipped entirely, that's a collapse. The key moments detector scans every consecutive pair of snapshots for >8% consensus shifts. Everything is pure Python stdlib — no new dependencies, continuing the 28-PR zero-dependency streak.

What's next:
Follow-up improvements could include per-agent adversarial effectiveness scores, adversarial agent strategy variants (devil's advocate vs. concern troll vs. evidence skeptic), and cross-simulation robustness comparison in the A/B view.

PR: Push blocked — GH_GLOBAL secret not set. Code committed locally on feat/adversarial-stress-test (932 lines, 12 files).
