# Repo Action Ideas — 2026-04-30 (v2)

**Repo:** [aaronjmars/MiroShark](https://github.com/aaronjmars/MiroShark)
**Snapshot:** 904 stars · 175 forks · 4 contributors · 0 open issues · 0 open PRs
**New since this morning:** PR #60 (RSS/Atom feed) merged; +18 stars in ~8 hours.
**Context:** This is a second pass for Apr 30. The first run (see `repo-actions-2026-04-30.md`) generated 5 ideas around statistical batch runs, cross-narrative simulation, checkpoint/resume, persona library, and a GitHub Actions composite action. This pass targets five distinct angles not covered there.

## What Just Landed

PR #60 — RSS/Atom feeds for the public simulation gallery — merged this morning, closing the loop on integration-layer discoverability. MiroShark now has: public gallery (/explore), completion webhooks, OpenAPI 3.1 spec, MCP onboarding panel, animated belief GIF, transcript export, verified-prediction hall, Langfuse observability, and now RSS autodiscovery. The integration surface is arguably the most complete of any open-source multi-agent simulation project.

That stack raises the bar on what's actually missing. The platform layer is done. What remains is the research workflow layer — the affordances that let a researcher go from "I ran a simulation" to "I can publish this" — and the automation layer that lets teams build MiroShark into recurring processes rather than one-off runs. Those two themes shape this second batch.

---

### 1. Jupyter Notebook Export

**Type:** Integration
**Effort:** Small (hours)
**Impact:** The transcript export (PR #57) produces Markdown and JSON — human-readable but not analysis-ready. A researcher who wants to run a t-test on belief drift across agents, compute network centrality from the interaction graph, or visualize stance change distributions needs a runnable Python environment with data already loaded. A Jupyter notebook export takes the existing `trajectory.json`, `posts/`, and `leaderboard.json` produced by every simulation and packages them into a `.ipynb` file with pre-written analysis cells: a `pandas` DataFrame of agent stances per round, a `networkx` graph of the interaction network, `matplotlib` plots for the belief drift and price trajectory, and a summary statistics block. For any researcher who wants to publish simulation results, this is the last mile — "we exported our 50-agent simulation to a Jupyter notebook and ran the following statistical tests" is how academic methods sections read. OASIS and AgentSim both produce analysis-ready artifacts; MiroShark currently doesn't.
**How:**
1. Add `GET /api/simulation/:id/export/notebook` that reads `trajectory.json`, `<sim_dir>/posts/*.json`, and the leaderboard endpoint response, then constructs an `.ipynb` file using the standard Jupyter notebook JSON schema (no library dependency — it's just a dict with `nbformat: 4`). Cells: (a) imports and data loading (`import pandas as pd; import networkx as nx; ...`), (b) `stances_df` — a DataFrame with columns `[agent_id, round, stance, platform, archetype]` built from `trajectory.json`, (c) belief drift chart cell (`stances_df.groupby(['round','stance']).size().unstack().plot(kind='area')`), (d) interaction network cell (build a `networkx.DiGraph` from the posts' `mentions` and `replies` fields, compute `degree_centrality`, compare against leaderboard rank), (e) summary statistics cell (`stances_df.groupby('agent_id')['stance'].agg(['first','last','std'])`). Return as `Content-Disposition: attachment; filename="miroshark-{id}.ipynb"`.
2. Add an "Export Notebook" button to the simulation results toolbar alongside the existing "Download transcript" and "Export GIF" buttons. Style it with a Jupyter orange icon. On click, trigger `GET /api/simulation/:id/export/notebook`. In the article generator template, add a one-line footnote: "Simulation data available as a Jupyter notebook export via the Results toolbar."
3. Add a `docs/analysis.md` page with a quickstart (open notebook in Google Colab, Binder, or local Jupyter) and brief descriptions of each pre-written cell. Add a "Jupyter Export" row to the README integrations table. In the README's academic/research section (or create one), add: "For peer-reviewed use, export simulation data as a Jupyter notebook with pre-written analysis cells — ready for statistical testing, network analysis, and publication-ready figures."

---

### 2. Pre-Run Cost Estimator

**Type:** DX Improvement
**Effort:** Small (hours)
**Impact:** MiroShark now supports six LLM configurations spanning two orders of magnitude in cost: GPT-4o at ~$12 for a 50-agent/15-round run down to Qwen 2.5 72B at ~$0.80 via cheap preset. Users launching their first simulation don't know what they'll spend until the run completes — and with 50 agents × 15 rounds × ~2,000 tokens per agent per round, a GPT-4o run can surprise a new user. A cost estimator shown in the launch flow (before "Run Simulation" is clicked) computes estimated tokens, estimated cost in USD, and estimated wall-clock time based on `agent_count × rounds × avg_tokens_per_agent × price_per_1K_tokens`. This isn't just a nice-to-have: it's the difference between a user who understands the cost model and runs MiroShark confidently versus one who accidentally burns $12 on a test run, assumes the product is expensive, and churns. For academic users without corporate API budgets, the estimator is the feature that makes MiroShark accessible.
**How:**
1. Add a `/api/estimate-run` endpoint that accepts `{ provider, model, agent_count, rounds }` and returns `{ estimated_input_tokens, estimated_output_tokens, estimated_cost_usd, estimated_time_seconds, confidence: "rough" }`. Token estimate: `agent_count × rounds × 1800` (conservative input, based on ICP graph build + prior round summary) plus `agent_count × rounds × 300` (output). Cost: use a static lookup table of `price_per_1K_tokens` by `provider/model` (update it manually each release or load from a `costs.json` config file so it can be patched without a code deploy). Time estimate: `agent_count × rounds × 12` seconds (empirical rough average for async gather-based execution).
2. In the simulation launch UI, after the user fills in agent count, rounds, and selects their LLM, show a compact estimate block below the "Run Simulation" button: "**Estimated cost:** ~$0.32 (using GPT-4o Mini, 20 agents, 8 rounds) · **Estimated time:** ~3 min". Update the estimate reactively as users change those fields. Show in orange when cost > $1, red when > $5 to prompt consideration of a cheaper preset. Add a small "How is this calculated?" tooltip explaining the rough token model.
3. Add a `LAST_RUN_COST` field to completed simulation metadata, populated from the actual tokens billed (if the LLM provider returns usage data in the response) or estimated (if not). Surface this as "Actual cost: $0.29" in the simulation detail header and "Avg cost per run: $0.34" in cross-simulation analytics. This turns the estimator into a learning loop — the pre-run estimate gets calibrated against actuals that users can see.

---

### 3. Cross-Simulation Analytics Dashboard

**Type:** Feature
**Effort:** Medium (1–2 days)
**Impact:** Every simulation result currently lives in isolation in the history view. A user who has run 20 simulations has no way to ask cross-cutting questions: "Which topic classes produce the most volatile agent consensus? Do simulations with fewer agents converge faster? What's my average accuracy on completed predictions?" A cross-simulation analytics dashboard aggregates all completed simulations into meta-level patterns — the research-layer equivalent of what Langfuse does for per-run observability. At 904 stars with a growing cohort of repeat users (researchers, analysts, teams), the users who have run 10+ simulations have no analytical surface for the meta-question. The dashboard turns MiroShark from a one-run tool into a longitudinal research instrument.
**How:**
1. Add `GET /api/analytics/aggregate` that queries all completed simulations and computes: (a) `runs_by_week` — bar chart of simulation count over time, (b) `avg_final_yes_price` and `std_final_yes_price` by agent count bucket (10–20, 21–40, 41–60), (c) `consensus_round_distribution` — histogram of which round agents first reached >66% agreement, (d) `accuracy_rate` — percent of resolved simulations where final YES price correctly predicted the outcome (>0.5 = YES, <0.5 = NO), (e) `top_topics` — 10 most common keywords in scenario text across all simulations (simple tokenizer, stop-word removal). Store nothing new — derive everything from `<sim_dir>/metadata.json` and the existing prediction resolution records.
2. Add an `/analytics` page accessible from the main nav (icon: bar chart). Layout: a row of 4 KPI cards at top (total simulations, avg cost per run, prediction accuracy %, avg consensus round), then two charts side by side (consensus round histogram and final YES price by agent-count bucket), then a "Topic frequency" word cloud or ranked list below. If fewer than 5 completed simulations exist, show a "Run more simulations to unlock analytics" empty state with a "Launch simulation" CTA.
3. Add a "My track record" link from the analytics page to the `/verified` hall — bridging aggregate analytics to prediction-specific resolution data. Add a "Download report" button that exports the full aggregate JSON as a `.json` file or a flat summary as a `.csv`. In the article generator, inject the two most notable cross-simulation findings as a contextual footnote: "Historical note: across N simulations on this instance, avg consensus round is X; this run converged Y rounds faster than average."

---

### 4. Simulation Scheduling

**Type:** Feature
**Effort:** Small (hours)
**Impact:** MiroShark can now be triggered programmatically via the OpenAPI spec (PR #45) and integrated into automated workflows via completion webhooks (PR #46) and the RSS feed (PR #60). The missing piece in the automation story is time-based triggering: running a simulation at a specific time or on a recurring schedule. Use cases are immediate — "run a daily 20-agent simulation on today's top DeFi news at 8am", "schedule a weekly market debate simulation for every Monday", "trigger a simulation on the first of every month against our fund's strategy document." This doesn't require any external scheduler — an in-process APScheduler (or a simple cron thread) handles it with no new infrastructure. Combined with the existing webhook system, scheduled simulations form the backbone of a recurring research or monitoring workflow without any manual triggering.
**How:**
1. Add a `POST /api/schedules` endpoint that accepts `{ cron_expression, config: <same as /api/run>, label, notify_webhook_url }`. Store schedules in a new `schedules` SQLite table with `id, label, cron_expression, config_json, next_run_at, last_run_at, status (active/paused/deleted)`. Use APScheduler (`pip install apscheduler`) in `BackgroundScheduler` mode initialized at app startup. On receiving a new schedule, add an APScheduler job with the cron expression that calls `POST /api/run` internally at trigger time. If `notify_webhook_url` is set, fire it on each triggered run completion (reusing the existing webhook dispatch logic from PR #46).
2. Add a "Schedules" sub-tab under Settings (alongside Developer Keys). List active schedules as cards showing label, cron expression in human-readable form (e.g. "Daily at 08:00 UTC"), config preview (agent count, scenario excerpt), and next run time. Each card has Pause/Resume and Delete buttons. "Add schedule" opens a modal: label field, scenario text area, agent count slider, rounds slider, cron presets (Daily / Weekly / Monthly / Custom), and optional webhook URL. Show the next 3 scheduled run times as a preview.
3. Add `GET /api/schedules/:id/history` that returns the last 10 triggered runs from this schedule with their simulation IDs, outcomes, and completion times. Link each entry to the corresponding simulation in history. In the simulation history view, tag simulations triggered by a schedule with a small "Scheduled" chip showing the schedule label so users can distinguish manual from automated runs. Add a schedule health indicator: if a scheduled run fails, flag the schedule card with an orange "Last run failed" badge and show the error reason.

---

### 5. n8n / Zapier Integration Template Pack

**Type:** Integration / Growth
**Effort:** Small (hours)
**Impact:** MiroShark's integration surface is now complete: OpenAPI spec (PR #45), completion webhooks (PR #46), RSS feed (PR #60), MCP panel (PR #44), transcript export (PR #57), and a GitHub Actions composite action (proposed in today's v1 batch). The missing step is making this surface actually usable for non-developer users. Zapier has 7M+ users; n8n is the dominant self-hosted automation platform. Both can consume MiroShark's webhook + RSS + API stack — but only if someone has written and shared a working template. A set of 3–4 ready-to-import workflow templates, published in the `docs/` folder and linked from the README, turns "MiroShark has a webhook" from a feature footnote into a real integration that non-technical users can activate in 5 minutes. This also compounds discovery: every n8n forum post or Zapier community share that references MiroShark's template pack is an organic inbound link.
**How:**
1. Write 4 integration templates as downloadable files in `docs/integrations/`: (a) `n8n-simulation-to-discord.json` — n8n workflow that subscribes to the RSS feed (`/feed.xml`), filters for completed simulations with `final_yes_price > 0.6`, and posts a formatted Discord embed with scenario, consensus round, and share link; (b) `n8n-daily-digest.json` — n8n workflow triggered daily at 9am that calls `GET /api/simulations` for yesterday's runs and posts a digest card to Slack; (c) `zapier-webhook-to-sheet.json` / `zapier-template-link` — a webhook trigger that posts every completed simulation's metadata (scenario, final price, top agent, rounds, cost) as a row in a Google Sheet; (d) `n8n-schedule-and-notify.json` — an n8n workflow that runs a fixed simulation config on a cron, waits for completion via polling the simulation status, then posts results to Telegram. Each template is a real, importable JSON file tested against MiroShark's API.
2. Add a `docs/integrations/README.md` page documenting each template: a screenshot of the workflow, step-by-step import instructions (for n8n: Settings > Import workflow; for Zapier: use the template link), required configuration (webhook URL from MiroShark Settings, channel credentials), and a "What you'll see" screenshot of the output. Link this page from the main README's integrations table as "Integration Templates (n8n, Zapier)".
3. Post the n8n templates to the [n8n community forum](https://community.n8n.io/c/workflows/) and the Zapier template to the Zapier app directory (or a GitHub Gist shared in Zapier community). Add a "Share your automations" section to the MiroShark README's community section with a link to the docs page and an invitation to submit PRs adding new templates. This seeding in the n8n and Zapier communities generates inbound discovery from users who are already looking for AI simulation automation — zero ad spend.

---

## Selection Rationale

This second batch for Apr 30 is deliberately complementary to the morning run (batch analysis, cross-narrative, checkpoint, persona library, GitHub Actions action). Those five ideas addressed the statistical validity, experimental design, and CI/CD integration angles. These five address the **research-to-publication pipeline** and **non-developer automation**:

- **Jupyter Export** (#1) — The publication bottleneck. Transcript export gives data; a Jupyter notebook gives a working analysis environment. For researchers who want citable outputs, this is the final step.
- **Pre-Run Cost Estimator** (#2) — Converts the LLM cost model from opaque to transparent. Reduces new-user churn from sticker shock and makes MiroShark accessible to academic users without large API budgets.
- **Cross-Simulation Analytics** (#3) — The longitudinal research layer. Users with 10+ simulations have no meta-analysis surface. The dashboard turns MiroShark from a one-run tool into a platform for repeated study.
- **Simulation Scheduling** (#4) — Time-based automation without external infrastructure. Enables recurring monitoring and research workflows. Compounds the webhook + OpenAPI stack already in place.
- **n8n / Zapier Templates** (#5) — The non-developer integration layer. The API surface is live; templates make it accessible in 5 minutes. Organic discovery in the n8n and Zapier communities is a compounding growth lever.

Each idea is scoped for autonomous implementation by the `feature` skill — clear inputs/outputs, no ambiguous design decisions, no external approvals needed.
