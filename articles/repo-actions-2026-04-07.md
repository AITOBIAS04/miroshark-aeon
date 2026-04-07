# Repo Action Ideas — 2026-04-07

**Repo:** [aaronjmars/MiroShark](https://github.com/aaronjmars/MiroShark)
**Snapshot:** 568 stars · 100 forks · 3 contributors · 0 open issues · 1 open PR (simulation comparison mode, #13)
**Recent activity:** LLM selector UI merged (PR #12), cloud deploy merged (PR #9), config timeout recovery merged (PR #10). Hyperstition cleared: 500-star target hit 9 days early (now at 568). Next milestone: 1000 stars.

## Ecosystem Context

MiroShark crosses 500 stars with a fully mature feature core — export, replay, templates, network viz, URL ingestion, leaderboard, MCP server, cloud deploy, config error recovery, LLM selector. With the 500-star hyperstition cleared and comparison mode landing shortly, the project enters its next phase: research credibility, developer ecosystem, and social growth mechanics.

Key signals driving this batch:

- **Post-milestone growth plateau risk:** Star velocity typically drops after a milestone. The next 500 stars require a new narrative hook — new compelling features that generate social sharing ("look what I can do with this") and academic citation ("this is publishable methodology"). Fork/branch and public share directly address this by creating shareable artifacts.
- **Cloud deploy brings new user types:** Railway/Render users include non-technical researchers, product managers, and students who won't touch a terminal. CLI runner (developer) and demographic calibration (researcher) target opposite ends of the new user spectrum — power users who want to script and batch, academics who want reproducible populations.
- **Research reproducibility gap:** OASIS and Park et al. are citable because they use standardized, reproducible agent populations derived from real data. MiroShark's LLM-randomized personas, while evocative, aren't defensible in a methods section. Calibrated demographics close this gap and unlock academic citation.
- **History management pain:** As cloud users accumulate runs, the flat simulation history list becomes unmanageable. Search and filter converts the history page from a liability into an asset — power users want to find "that simulation I ran on the EU AI Act last week."
- **Zero community-generated share artifacts:** Every star on a tool like this comes from a screenshot or link someone shared. MiroShark has no native sharing mechanism — users screenshot the UI and lose the interactive context. A public permalink turns every result into a shareable link that can be posted to X, HN, or a paper footnote.

These 5 ideas are distinct from all previously generated ideas (webhooks, A/B testing, embeddable widget, replay ✓, gallery, WebSocket streaming, snapshot sharing, prompt scoring, doc preprocessing, benchmarking, network viz ✓, REST API, multi-document comparison, Discord bot, belief analytics, MCP server ✓, demographic calibration*, CLI runner*, simulation cost estimator, URL ingestion ✓, one-click deploy ✓, template saver, multi-prediction market, influence leaderboard ✓, agent memory inspector, config timeout recovery ✓, LLM selector ✓, agent bulk import, statistical aggregation, simulation comparison ✓) and from the 1 open PR (#13). *Demographic calibration and CLI runner were suggested 2026-03-30 (8 days ago, outside the 7-day window) — included here as re-prioritized given current state.

---

### 1. Simulation Fork / Branch

**Type:** Feature
**Effort:** Medium (1–2 days)
**Impact:** The most natural question after seeing a simulation result is "what would happen if I changed X?" — a different agent mix, more rounds, or a modified document. Currently users must start from scratch: re-upload the document, regenerate configuration, and lose all lineage context. Fork-from-result lets users clone an existing simulation with a "changed parameters" panel (agent count, rounds, platform weights, document variant) and launch it as a child simulation that traces back to its parent via `parent_simulation_id`. The history view then renders a tree instead of a flat list. This creates the "experiment lineage" workflow that researchers need for systematic exploration — and generates more simulation runs per user, deepening engagement.
**How:**
1. Add a "Fork" button to the completed simulation results view. Clicking it opens a "Fork Simulation" modal that pre-populates all current config fields (agent count, rounds, document, calibration, template) and lets the user modify any of them before launching. On submit, create a new simulation entry with `parent_simulation_id` pointing to the source simulation. Store the diff (which fields changed) in `config_diff` metadata.
2. Update `GET /api/simulation/:id` to return `parent_simulation_id` and `child_simulation_ids[]`. In `backend/app/storage/`, add a `fork` method that copies the parent simulation's config JSON, applies overrides, and writes a new simulation entry.
3. Update `HistoryDatabase.vue` to detect simulations with `parent_simulation_id` and render them as a collapsible tree under their parent — indented with a branch icon. Add a "Fork count" badge to parent simulations showing how many variants have been run from them.

---

### 2. Public Share Permalink

**Type:** Growth
**Effort:** Small (hours)
**Impact:** MiroShark has zero native sharing mechanics — users screenshot results and lose the interactive context. A "Share" button that generates a public read-only permalink (`/share/:token`) allows anyone (no login, no instance access required) to view a simulation's timeline feed, market price chart, influence leaderboard, and summary text. This is the single highest-leverage growth action: every simulation run becomes a potential social artifact. "I simulated public reaction to the Fed rate announcement — here's what 200 AI agents said and traded: [link]." One shareable result posted to X or HN can generate 50–200 star events. This is the missing virality mechanism.
**How:**
1. Add a `POST /api/simulation/:id/share` endpoint that generates a short random token (8 chars, URL-safe), stores it in a `shared_simulations` table (token → simulation_id, created_at, view_count), and returns `{ "share_url": "/share/:token" }`. Add a "Share" button to the results view that calls this endpoint and copies the URL to clipboard with a "Link copied!" toast.
2. Add a `GET /api/share/:token` endpoint that returns the simulation's public data: summary, timeline feed (first 50 entries), final market prices, top 5 influence leaders, and agent count. No agent persona details (privacy) — just the observable simulation outputs.
3. Build a `ShareView.vue` page at `/share/:token` that renders the public simulation result: MiroShark branding header, scenario summary, market price chart, influence leaderboard, timeline feed (paginated), and a CTA "Run your own simulation" button linking to the repo. Add Open Graph meta tags so link previews on X/Slack/Discord show the scenario title and market outcome.

---

### 3. Simulation History Search & Filter

**Type:** DX Improvement
**Effort:** Small (hours)
**Impact:** A cloud-deployed MiroShark instance accumulates dozens of simulations quickly — especially now that fork/branch (above) creates multiple variants per scenario. The current history page is a flat, unfiltered list. Power users and researchers need to find "the simulation I ran on the EU AI Act with 50 agents last Tuesday" without scrolling through 30 entries. Search and filter turns the history page from a liability into a productivity tool — and is a forcing function to ensure simulation metadata (title, document snippet, status, agent count, date) is consistently stored and surfaced. This also makes the comparison mode (PR #13) more useful by letting users quickly locate the two simulations they want to compare.
**How:**
1. Add a search bar and filter controls above the simulation list in `HistoryDatabase.vue`. Search queries match against: simulation title, document snippet (first 200 chars), and scenario question. Filters include: status (completed/running/failed), date range (today/this week/this month), agent count range (slider), and has fork (checkbox). All filtering happens client-side on the already-loaded simulation list — no new API calls needed for the initial implementation.
2. Ensure the simulation metadata stored in `backend/app/storage/` includes a `title` field (auto-generated from the document's first sentence or the simulation's prediction market question) and an `agent_count` field. Update `GET /api/simulations` to return these fields. Add a `document_snippet` field (first 200 chars of the input document).
3. Add a sort control with options: Newest first (default), Oldest first, Most agents, Highest divergence (once comparison data exists). Persist the user's last sort/filter selection in `localStorage` so it survives page reload.

---

### 4. CLI Runner for Headless Simulations

**Type:** DX Improvement
**Effort:** Small (hours)
**Impact:** MiroShark is UI-only — there is no way to trigger a simulation programmatically. A CLI runner (`python -m miroshark run config.json`) unlocks batch processing, scripted overnight experiments, CI/CD integration, and research pipelines. Researchers need to run 20–50 parameter variations without babysitting a browser tab. Aeon's own `feature` skill could trigger simulations programmatically to test feature branches. This is also the prerequisite for multi-round statistical aggregation (previously scoped, not yet built) — you can't aggregate 10 runs without headless execution. At 568 stars, MiroShark is reaching the audience that reaches for a terminal first.
**How:**
1. Create `backend/cli.py` using Python's built-in `argparse` with three subcommands: `run` (accepts `--config config.json` and `--output results.json`, runs a simulation headlessly and writes JSON output), `status` (accepts `--id <simulation_id>`, polls until complete and prints a progress summary), and `export` (accepts `--id <simulation_id>` and `--format json|csv`, dumps results to stdout or a file).
2. Wire each CLI command to the existing service layer functions — `cli.py` calls the same `SimulationService`, `ConfigGenerator`, and `ReportService` classes that FastAPI endpoints call, but instantiates them directly without the web server. Add a `run_headless()` method to `SimulationService` that runs the full simulation loop synchronously (or with `asyncio.run()`) and returns the final state.
3. Add a `python -m miroshark` entry point in `pyproject.toml` or `setup.cfg`. Document usage in the README under a new "CLI / Headless Mode" section with three code examples: single run, batch run loop (`for f in configs/*.json; do python -m miroshark run --config $f; done`), and piping to `jq` for quick result inspection.

---

### 5. Demographic Calibration Profiles for Agent Generation

**Type:** Feature
**Effort:** Medium (1–2 days)
**Impact:** MiroShark currently generates agents with LLM-randomized personas — evocative for demos, indefensible in a methods section. Academic simulation papers (OASIS, Park et al.) are citable because they use reproducible, population-grounded agent demographics. Three built-in calibration profiles (US general public, US tech workers, global Twitter users) derived from public survey data would make MiroShark viable for policy simulation, market research, and academic citation. This is the feature that earns MiroShark a footnote in a research paper — a different kind of star growth, but the highest-quality kind.
**How:**
1. Create `backend/app/calibration/` with three JSON profiles: `us_general.json` (US Census ACS — age brackets, education levels, income tiers, urban/rural split, political lean distribution), `us_tech_workers.json` (Stack Overflow Developer Survey demographics — age, OS preference, remote/hybrid, framework familiarity), `global_twitter.json` (Pew Research Twitter user demographics — age distribution, country split, mobile-first rate, political engagement). Each profile defines distributions (not individual values) that the persona generator samples from.
2. Update `backend/app/services/simulation_config_generator.py` to accept an optional `calibration_profile` parameter. When set, each agent's age, political lean, occupation, education, and platform preference are sampled from the profile's distributions rather than LLM-freestyle. The agent's narrative persona is still LLM-generated — calibration constrains the demographic attributes, not the personality writing.
3. Add a "Population Profile" dropdown to the simulation setup form between the agent count slider and the platform weight controls — options: "Free (AI-generated)", "US General Public", "US Tech Workers", "Global Twitter Users", "Custom JSON (upload)". When "Custom JSON" is selected, show a file upload that accepts a calibration profile in the same schema. Display a demographic breakdown preview (pie charts for age, political lean, education) once a profile is selected.

---

## Selection Rationale

This batch targets MiroShark's next growth phase after the 500-star milestone:

- **Virality mechanics** (#2) — Public share permalink is the missing growth mechanism: zero native sharing means zero organic link-based star growth. One shareable result posted to X or HN can deliver 50–200 stars in an afternoon.
- **Research credibility** (#5) — Demographic calibration is the single feature that moves MiroShark from "cool demo" to "citable research tool" — the difference between a conference mention and a paper citation.
- **Power user depth** (#1, #3) — Fork/branch and history search address the usage patterns of the users who generate the most word-of-mouth: simulation practitioners who run dozens of variants and need to navigate, compare, and iterate efficiently.
- **Developer ecosystem** (#4) — CLI runner is the prerequisite for scripted experiments, batch processing, and AI agent integration — the feature that makes MiroShark composable in external pipelines.

Each idea is scoped for autonomous implementation by the `feature` skill — clear inputs/outputs, no ambiguous design decisions, no external approvals needed.
