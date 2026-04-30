# Repo Action Ideas — 2026-04-30

**Repo:** [aaronjmars/MiroShark](https://github.com/aaronjmars/MiroShark)
**Snapshot:** 886 stars · 171 forks · 4 contributors · 0 open issues · 0 open PRs
**Recent activity (since Apr 15):** Director Mode event injection (PR #31), Simulation Quality Diagnostics (PR #32), Agent Interaction Network Graph (PR #33), Embeddable Widget (PR #34), Agent Demographic Breakdown (PR #35), parallel report generation 5× speedup (PR #36), Agent Counterfactual Explorer "What If?" (PR #37), Scenario Auto-Suggest (PR #39), Trending Topics Auto-Discovery (PR #40), Social Share Card / OG Image (PR #42), Public /explore Gallery (PR #43), MCP Onboarding Panel (PR #44), OpenAPI 3.1 + Swagger UI (PR #45), Completion Webhooks for Slack/Discord/Zapier (PR #46), Predictive Accuracy + /verified Hall (PR #47), Admin Auth on publish/resolve (PR #49), Animated Belief-Replay GIF (PR #50), Langfuse Observability Integration (PR #51), Simulation Transcript Export MD+JSON (PR #57), per-slot Wonderwall override (PR #59).

## Ecosystem Context

MiroShark's 15-day burst from 692 → 886 stars produced one of the densest feature sprints in any open-source multi-agent simulation project: a public /explore gallery, completion webhooks for Slack/Discord/Zapier, OpenAPI 3.1 spec with Swagger UI, Langfuse observability integration, animated belief-replay GIFs, embeddable widgets, an MCP onboarding panel, an agent counterfactual explorer, social share cards with OG image generation, and a verified-prediction hall of fame. The project has crossed from "impressive demo" into a recognizable simulation platform with a discoverable community, outbound integration hooks, and an observable agent runtime.

The feature gaps that matter at 886 stars are different from what mattered at 692. The community is now large enough that some users are running MiroShark repeatedly — as researchers, as automated pipeline operators, and as teams sharing results with each other. That means the bottlenecks are no longer "can it do X?" but "can I trust X to be stable, reproducible, and portable across workflows?"

Three structural gaps remain open:

- **Statistical validity:** All outputs are still single-run point estimates. A belief drift that shows "73% YES consensus by round 8" could be seed-dependent. OASIS, SOTOPIA, and every peer-reviewed social simulation paper run ensembles. MiroShark needs batch mode to be citable.

- **Reliability under load:** Cloud-hosted 50-agent, 15-round simulations cost $0.10–$0.30 per run and take 8–15 minutes. There is still no crash recovery — a container restart on Railway or Render loses all intermediate state and all API spend. The checkpoint/resume primitive has been on the roadmap since the first feature batch; it still isn't built.

- **Portability for researchers:** The transcript export (PR #57) outputs Markdown and JSON — human-readable but not analysis-ready. Researchers who want to run t-tests, regression, or network centrality analysis on simulation data need pre-loaded DataFrames in a runnable Python environment. A Jupyter notebook export with pre-written analysis cells is the last mile for academic adoption.

Two new angles this batch also surfaces:

- **Narrative competition is the missing experimental primitive:** Every simulation in MiroShark starts from a single source document. But the most interesting real-world dynamics involve competing narratives: bull and bear cases for the same asset, two sides of a regulatory debate, or parallel media framings of the same event. Feeding agents different information diets in the same simulation is a new capability class.

- **Automation integration has just become possible:** With OpenAPI spec (PR #45) and completion webhooks (PR #46), MiroShark can now be triggered and consumed programmatically. A GitHub Actions composite action that runs a simulation from a workflow file and posts results as a PR comment would bring MiroShark into CI/CD pipelines — turning it into a content-layer verification tool for teams publishing research, proposals, or forecasts.

These 5 ideas are distinct from all open PRs (none) and replace the Apr 14/Apr 15 lists (both >7 days old with partial execution — Director Mode, Demographic Breakdown, and Browser Push Notifications from those lists are now built).

---

### 1. Statistical Batch Runs with Aggregate Dashboard

**Type:** Feature
**Effort:** Medium (1–2 days)
**Impact:** A single simulation run produces one market outcome, one leaderboard, one belief drift curve — a point estimate. For any result used in a research or analytical context ("agents predicted YES with 73% confidence"), the credibility question is immediate: is that result stable, or did it happen to come out that way once? Batch mode runs the same configuration N times (3, 5, or 10 runs) with different random seeds, then presents an aggregate dashboard: mean market final price with ±1 standard deviation error bars, belief drift consensus round as a histogram across N runs, leaderboard stability score (% of runs where the same agent ranked #1), and a robustness rating (Low/Medium/High based on SD relative to mean). This is the single feature that makes MiroShark outputs statistically defensible. At 886 stars, the user base now includes researchers who want to publish — "we ran 5 trials; 4 predicted rejection with mean YES price 0.28 ± 0.06" is publishable. OASIS ran 100+ ensemble experiments; even 5 runs with variance data clears the credibility bar.
**How:**
1. Add a "Run as Batch" toggle to the simulation launch UI. When enabled, show a radio group: "Runs: 3 / 5 / 10". On submit, `POST /api/batch` creates N simulation entries with the same config, incrementing a `seed_offset` field and tagging each with a shared `batch_id`. Return `{ batch_id, simulation_ids: [...] }`. Enqueue runs sequentially via the existing simulation runner. Store batch metadata in a new `batches` SQLite table (`batch_id`, `config_hash`, `run_count`, `status`, `created_at`).
2. Add `GET /api/batch/:batch_id` that returns status and, once all runs are `completed`, computes aggregate stats: for each run, extract `final_yes_price`, `belief_drift_consensus_round` (from existing belief drift endpoint), and `top_agent_id` (rank 1 from influence leaderboard). Compute `mean`, `std`, `min`, `max` for continuous values; `mode` for categorical. Return the full aggregate object and store it in `<batch_dir>/aggregate.json`.
3. Add a `BatchResultsView.vue` component that opens as an overlay when all batch runs complete. Show: (a) a market price distribution chart (box plot: `final_yes_price` across N runs), (b) a consensus round histogram (which round produced consensus in each run), (c) a leaderboard stability section (top 3 agents most consistently ranked #1 across runs with % stability), (d) a Robustness badge: High (SD < 10% of mean), Medium (10–25%), Low (>25%). Include a "View individual run" drill-through for each of the N simulations. Add a "Download batch CSV" that exports all N results as a flat file with one row per run.

---

### 2. Multi-Document Cross-Narrative Simulation

**Type:** Feature
**Effort:** Medium (1–2 days)
**Impact:** Every current MiroShark simulation starts from a single source document — a shared informational reality that all agents process. But the most analytically interesting dynamics involve competing narratives: a bull case and a bear case for the same asset, a government press release and an opposition rebuttal, two media framings of the same event. Feeding agents different information diets in the same simulation surfaces the most research-valuable questions: "Which narrative cohort flips first? How does exposure to the minority view affect consensus formation? When do information-siloed agents converge and when do they calcify?" This is the multi-document simulation primitive — upload 2–4 competing documents, assign agent cohorts by archetype or demographic to different primary sources, and observe belief formation under narrative competition in the same shared simulation round. No other multi-agent social simulation tool in the open-source space offers this out-of-the-box.
**How:**
1. Extend the simulation config to accept `documents: [{ text_or_url, label, cohort_assignment }]` where `cohort_assignment` is one of: `by_platform` (e.g., "Reddit agents get doc A, Twitter agents get doc B"), `by_type` (institutional vs. individual), `by_region`, or `random_split`. In the frontend Step 1, add a "Add competing document" button that opens a second document upload field with a label input (e.g., "Bull Case") and a cohort assignment dropdown. Cap at 4 documents. When the config is sent to the backend, each agent's persona record receives a `primary_document` field pointing to the document assigned to its cohort.
2. In `simulation_runner.py`, modify the per-agent context construction to inject the agent's `primary_document` as its primary briefing, plus a short "You are aware that an alternative view exists but have not read it" prompt for agents not in the primary cohort. At round N+1 onwards, optionally "cross-expose" agents to 20% of the other document's framing (configurable as a `cross_exposure_rate` setting) to model information leakage across cohorts. Write the document assignment map to `<sim_dir>/context/narrative_map.json`.
3. Add a "Narrative Split" tab to the simulation results view (alongside Belief Drift and Leaderboard). Show: (a) a stacked belief drift chart with separate lines per document cohort (e.g., "Bull cohort stance" vs. "Bear cohort stance" over rounds), (b) a "Convergence round" metric — the first round where the two cohort belief means cross within ±0.1 — highlighted on the chart, (c) a "Narrative divergence score" (mean belief delta between cohorts at each round). Include narrative assignment details in the article generator prompt so generated articles can describe the competing-narrative setup.

---

### 3. Simulation Checkpoint & Resume

**Type:** DX Improvement
**Effort:** Medium (1–2 days)
**Impact:** Cloud-hosted simulations — 50 agents, 15 rounds, GPT-4o — take 8–15 minutes and cost $0.10–$0.30 per full run. Network instability, Railway/Render container restarts, and browser-forced page unloads can kill a simulation mid-run. Currently the only recovery is restart, losing all intermediate state, all generated posts, all belief state evolution, and all API spend from completed rounds. A checkpoint file written atomically after each round (one JSON write = negligible overhead) enables resume from round N+1 rather than round 1. For a 10-round simulation that dies at round 7, checkpoint/resume saves 70% of the API spend and preserves all intermediate analysis. For researchers running 200-agent experiments or deliberately pausing to inject an event (Director Mode, PR #31), checkpoint/resume is the reliability primitive that makes long-form simulation trustworthy. This feature has been on the roadmap since April 14; it remains the highest-value unbuilt DX improvement.
**How:**
1. After each round completes in `simulation_runner.py`, write a checkpoint atomically to `<sim_dir>/checkpoint.json` via a write-then-rename pattern (`checkpoint.tmp` → `checkpoint.json`). Contents: `{ "last_completed_round": N, "agent_belief_states": {...}, "market_state": {...}, "round_memory": {...}, "events_injected": [...], "checkpoint_at": "<ISO8601>" }`. Add a `checkpoint_at` field to the simulation's metadata record. On SIGTERM, write `"interrupted"` to the simulation `status` field before exiting.
2. Add `status: "interrupted"` to the simulation state machine (alongside `pending`, `running`, `completed`, `failed`). A startup health check in `app.py` scans all simulations stuck in `"running"` at boot (indicating an unclean shutdown) and transitions them to `"interrupted"`. Add a `POST /api/simulation/:id/resume` endpoint that reads `checkpoint.json`, validates the simulation is `"interrupted"`, restores all state, and re-queues the runner starting from `last_completed_round + 1`.
3. In the simulation history view, show a "Resume" button on `interrupted` simulation cards alongside the existing "Fork" and "Share" buttons. Style the card with an orange "Interrupted at round N" badge. In Settings, add an "Auto-resume interrupted simulations at startup" toggle (default: on). Add the `checkpoint_at` timestamp and `last_completed_round` to the `GET /api/simulation/:id` response so the UI can surface "Resumed from round N" in the simulation header.

---

### 4. Agent Persona Library

**Type:** Feature
**Effort:** Small (hours)
**Impact:** Every simulation in MiroShark generates agent personas from scratch — stochastically, from the knowledge graph build phase. For a one-off simulation this is fine. But researchers running multi-simulation studies (e.g., "how do the same 10 agents respond to 5 different market scenarios?") need consistent, reusable personas across runs. Currently there is no way to "pin" a persona — each simulation gets a fresh stochastic draw. An Agent Persona Library lets users save any agent persona card to a persistent library, name it ("JPMorgan Desk Analyst", "Reddit Retail Skeptic"), and inject saved personas into any future simulation as fixed participants. The rest of the simulation generates normally around them. For research reproducibility, it's the difference between "50 random agents said X" and "the same 10 calibrated agents said X across 5 scenarios." At 886 stars with a growing academic cohort, this is the reuse primitive that supports longitudinal or multi-scenario research designs.
**How:**
1. Add a "Save to Library" button to each agent profile card in the simulation results view (the expandable card that shows biography, platform, archetype, belief history). On click, the agent's full persona JSON (name, biography, demographics, initial belief state, platform, archetype type) is saved to a `personas` SQLite table with a user-assigned label field. Add a `GET /api/personas` list endpoint, `POST /api/personas` (save), `DELETE /api/personas/:id` (remove), and `GET /api/personas/:id/export` (download as JSON). Add a "Persona Library" page in Settings that shows saved personas as cards with their label, key demographics, and archetype — sortable by date saved or label.
2. In the simulation launch flow (Step 1), add an optional "Fixed Personas" section below the agent count slider. Users click "Add from library" to select saved personas; selected personas appear as locked cards (up to 10). When the simulation starts, the config includes a `fixed_personas: [...]` array. In `simulation_runner.py`, inject fixed personas directly as pre-built agent nodes in the ICP graph, bypassing the stochastic generation phase for those agents. Remaining agent slots fill stochastically as normal.
3. Add `GET /api/personas/export-pack` that bundles all saved personas into a single JSON file for sharing or backup. Add `POST /api/personas/import-pack` that accepts a persona pack JSON and merges it into the local library (deduplication by `persona_hash`). Add a prominent "Share persona pack" button on the Library page that copies a download link or opens a file-save dialog. In the README, add a "Persona Library" section in the Usage docs explaining the workflow for multi-scenario research studies.

---

### 5. GitHub Actions Composite Action

**Type:** Integration / Growth
**Effort:** Small (hours)
**Impact:** MiroShark now has a full programmatic interface: OpenAPI 3.1 spec (PR #45), completion webhooks for Slack/Discord/Zapier (PR #46), and admin auth on key endpoints (PR #49). The missing piece is a drop-in GitHub Actions workflow integration. A ready-to-use composite action packaged in the MiroShark repo lets any team trigger a simulation from their CI/CD pipeline — via `uses: aaronjmars/MiroShark/.github/actions/run-simulation@main` — and receive results as a formatted PR comment. Use cases: a research team that publishes weekly forecasts runs a simulation on every PR against their forecast document; a DeFi team validates their market thesis by running agents on every governance proposal PR; an AI safety org runs adversarial agent debates on every policy draft. This is both a growth lever (every CI run is a discovery moment for the repo) and a composability unlock that extends MiroShark's reach into developer workflows without requiring any additional MiroShark UI work.
**How:**
1. Create `.github/actions/run-simulation/action.yml` as a composite action with inputs: `miroshark_url` (base URL of a self-hosted MiroShark instance), `api_key` (the key from Settings > Developer), `document` (text or URL), `scenario` (scenario prompt string), `agent_count` (default: 20), `rounds` (default: 5), `timeout_seconds` (default: 600). Steps: (a) POST to `/api/run` with the config and `webhook_url` omitted (polling mode), (b) poll `GET /api/simulation/:id/status` every 15 seconds until `completed` or timeout, (c) fetch the final result from `GET /api/simulation/:id`, (d) format a markdown summary as a GitHub step output variable.
2. Add a `post-to-pr-comment` sub-step using the `gh` CLI to post the formatted result as a PR comment. Comment format: "**MiroShark Simulation Result** · [scenario text]\n| Metric | Value |\n|---|---|\n| Final YES | {final_yes_price}% |\n| Consensus round | {consensus_round} |\n| Top agent | {top_agent_name} |\n| Rounds | {rounds} |\n\n[View full simulation →]({share_url})". If `share_url` is not available, link to the instance's `/history` page.
3. Add a `docs/github-actions.md` page documenting the composite action with a full example workflow file (simulate on every PR that modifies `docs/thesis.md` or `proposals/*.md`) and a quickstart checklist: (1) deploy MiroShark, (2) generate API key, (3) add `MIROSHARK_API_KEY` as a repo secret, (4) copy the workflow YAML. Add a "GitHub Actions" entry in the README integrations table (alongside MCP, Zapier, Slack, n8n) with a one-line description and link to the docs page.

---

## Selection Rationale

After the 15-day feature burst (PRs #31–#59), MiroShark's remaining gaps are about depth, reliability, and composability rather than breadth:

- **Batch Runs** (#1) — The research credibility gap. 886 stars means academic users; single-run point estimates aren't publishable. Batch mode with variance data is the feature that turns MiroShark outputs from "interesting" into "citable."
- **Cross-Narrative Simulation** (#2) — The next-level experimental primitive. Single-document simulations test one information reality; multi-document simulations test narrative competition — the most important dynamic in financial markets, political discourse, and disinformation research.
- **Checkpoint & Resume** (#3) — The reliability gap. $0.30 cloud runs that die at round 7 lose everything. One JSON write per round; resume from N+1. The cost of not having this compounds with every expensive simulation that users restart from scratch.
- **Persona Library** (#4) — The longitudinal research primitive. Researchers running multi-scenario studies need consistent agent identities across runs. Currently every simulation draws fresh stochastic personas. A save/inject library makes repeat-study research designs possible.
- **GitHub Actions Action** (#5) — The composability unlock. OpenAPI spec + webhooks are live; a drop-in GitHub Actions action is the last meter of the integration that puts MiroShark in developer CI/CD workflows and compounds discovery through every repo that uses it.

Each idea is scoped for autonomous implementation by the `feature` skill — clear inputs/outputs, no ambiguous design decisions, no external approvals needed.
