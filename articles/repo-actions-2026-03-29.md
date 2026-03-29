# Repo Action Ideas — 2026-03-29

**Repo:** [aaronjmars/MiroShark](https://github.com/aaronjmars/MiroShark)
**Snapshot:** 329 stars · 54 forks · 3 contributors · 0 open issues · 3 open PRs
**Recent activity:** 34 commits in 14 days — cross-platform engine, Polymarket integration, Hyperstitions Design System v2.0, graph reasoning tools, round analyzer, 7 test scripts

## Ecosystem Context

The multi-agent simulation space is heating up in 2026. CAMEL-AI's OASIS has 3.8k stars for million-agent social simulations. Artificial Societies raised $5.85M for enterprise social simulation (300–5,000 personas). MiroFish (the original Chinese project MiroShark forked from) has 16,000+ stars. Meanwhile, AI agents are actively trading on Polymarket — Polystrat executed 4,200+ trades in its first month with up to 376% returns on individual positions.

MiroShark's differentiator is its accessible, document-driven approach: upload any document, auto-generate hundreds of agents, simulate across Twitter + Reddit + Polymarket simultaneously. The cross-platform engine with belief state tracking and market-media bridge is unique in the open-source landscape.

With 3 pending PRs (export, preset templates, replay) about to land, the next wave of features should focus on **making simulation output actionable** and **enabling programmatic access** for integrations.

---

### 1. Agent Relationship Network Visualization

**Type:** DX Improvement
**Effort:** Medium (1–2 days)
**Impact:** Makes the simulation comprehensible at a glance — researchers and demo audiences can instantly see influence flows, opinion clusters, and belief shifts instead of reading through text logs. This is also the most "screenshot-worthy" feature for viral sharing.
**How:**
1. Add a new Vue component using vis.js or D3-force that renders agents as nodes and interactions (replies, reposts, trades) as edges, colored by sentiment/belief stance.
2. Animate the graph round-by-round — nodes shift color as beliefs change, edge thickness reflects interaction frequency, clusters emerge as communities form.
3. Wire it into the existing simulation view as a tab alongside the current timeline feed.

---

### 2. REST API for Simulation-as-a-Service

**Type:** Integration
**Effort:** Medium (1–2 days)
**Impact:** Unlocks programmatic access — external tools (Aeon, trading bots, research pipelines, CI/CD) can trigger simulations and consume results via HTTP. This is the foundation for the "simulation-as-decision-layer" vision and positions MiroShark as infrastructure, not just a UI tool.
**How:**
1. Add FastAPI endpoints: `POST /api/simulations` (create + start), `GET /api/simulations/{id}` (status + results), `GET /api/simulations/{id}/report` (generated report).
2. Return structured JSON with per-round agent actions, belief trajectories, and market prices — the same data the frontend already consumes, just exposed externally.
3. Add API key authentication via environment variable and rate limiting middleware.

---

### 3. Multi-Document Comparison Mode

**Type:** Feature
**Effort:** Medium (2–3 days)
**Impact:** Turns MiroShark into a decision-support tool — run the same agent pool against two documents (e.g., two policy drafts, two press releases, two product announcements) and see how simulated public reaction diverges. This is the use case enterprises and researchers will pay for.
**How:**
1. Add a "Compare" mode to the config generator that accepts two documents and creates two parallel simulation configs sharing the same agent pool.
2. Run both simulations (can reuse the same Neo4j graph build) and collect results side-by-side.
3. Build a comparison view showing divergent sentiment trajectories, different market prices, and which agents flipped stance between versions.

---

### 4. Discord Bot for Running Simulations

**Type:** Growth
**Effort:** Small (hours)
**Impact:** Viral distribution channel — users can run simulations directly from Discord with a slash command, get progress updates, and receive the report in-channel. Lowers the barrier to zero (no local setup, no Docker) and turns every Discord server into a potential MiroShark demo. Similar pattern to how Midjourney grew through Discord-native distribution.
**How:**
1. Create a lightweight Discord bot (discord.py) that accepts `/simulate <document_url_or_text>` and forwards it to the MiroShark backend (or a hosted instance).
2. Post round-by-round updates as embeds with agent counts, top posts, and market price movements.
3. When complete, post the final report with a link to the full web UI for detailed exploration.

---

### 5. Belief Trajectory Analytics Dashboard

**Type:** DX Improvement
**Effort:** Medium (1–2 days)
**Impact:** Transforms one-off simulation runs into a proper research tool. Researchers need to compare runs, track how parameter changes affect outcomes, and export publishable charts. This also makes MiroShark credible for academic use — every social simulation paper needs trajectory plots.
**How:**
1. Add a `/analytics` page that loads historical simulation results and renders: sentiment heatmaps (agents × rounds), belief convergence curves, platform activity breakdown (posts vs. comments vs. trades per round), and opinion polarization index over time.
2. Use Chart.js or Recharts for interactive plots with hover tooltips showing individual agent actions at each data point.
3. Add CSV/PNG export for each chart so researchers can drop them directly into papers or presentations.

---

## Selection Rationale

These 5 ideas complement the 10 generated on 2026-03-28 (webhooks, A/B testing, embeddable widget, replay, gallery, WebSocket dashboard, shareable snapshots, prompt scoring, document preprocessing, benchmarking). The focus this round is on:

- **Visualization** (#1, #5) — the simulation produces rich data but the UI doesn't yet surface it visually
- **Programmatic access** (#2) — unlocking the "platform" layer for integrations
- **Decision support** (#3) — the killer use case for enterprises and researchers
- **Distribution** (#4) — a zero-friction entry point that could drive organic growth

Each idea is scoped for autonomous implementation by the `feature` skill — clear inputs/outputs, no ambiguous design decisions, no external approvals needed.
