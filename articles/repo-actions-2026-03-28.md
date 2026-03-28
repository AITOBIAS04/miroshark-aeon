# Repo Action Ideas — 2026-03-28

**Repo:** [aaronjmars/MiroShark](https://github.com/aaronjmars/MiroShark)
**Stars:** 322 | **Forks:** 53 | **Language:** Python + Vue.js
**Description:** Universal Swarm Intelligence Engine — multi-agent social simulation with Twitter, Reddit, and Polymarket platforms

## Current State

MiroShark has seen intense development over the past two weeks: 34 commits, a full rebrand from MiroFish, cross-platform simulation engine (Twitter + Reddit + Polymarket running simultaneously), Evangelion-inspired Hyperstitions Design System v2.0, graph reasoning tools (centrality, community detection, bridge entities), a 416-line round analyzer, 7 test scripts, and 4 distinct setup paths (Cloud API, Docker, Manual Ollama, Claude Code CLI). Two open PRs add simulation data export (#1) and preset templates (#2). The contributor base is small (3 contributors, with 666ghj leading at 219 commits), and there are zero open issues — the project is developer-driven with no external feature requests yet.

The ecosystem is moving fast: OASIS supports 1M-agent simulations, PolicySim introduced proactive policy optimization at ACM Web 2026, and AI agents now represent ~18% of prediction market volume. MiroShark occupies a unique niche — it's the only accessible tool combining social media simulation with prediction market dynamics — but needs to capitalize on that positioning before larger frameworks absorb the use case.

---

### 1. API Webhook & Callback System for Simulation Events

**Type:** Feature
**Effort:** Medium (1-2 days)
**Impact:** Enables external integrations without polling. Developers can hook into simulation milestones (round complete, belief shift, market price change) to build dashboards, alerting pipelines, or chain simulations together. This is the foundation for MiroShark becoming a platform rather than a standalone tool.

**How:**
1. Add a webhook registration endpoint (`POST /api/webhooks`) that accepts a callback URL and a list of event types (e.g., `round.complete`, `market.price_change`, `belief.shift`).
2. Fire async HTTP POST requests to registered webhooks at each simulation event, with a JSON payload containing the event type, timestamp, and relevant data (round number, agent actions, market state).
3. Add a webhook management UI panel in the frontend settings to register, test, and delete webhooks.

---

### 2. Simulation Comparison / A-B Testing Mode

**Type:** Feature
**Effort:** Medium (1-2 days)
**Impact:** Lets users run the same document through two different configurations (e.g., different agent counts, model tiers, or platform mixes) and compare outcomes side-by-side. This is a killer feature for researchers and policy analysts who need to test how parameter changes affect emergent behavior — directly aligned with the PolicySim trend of proactive policy optimization.

**How:**
1. Add a "Compare" mode in the frontend that lets users select two completed simulations and renders their timelines, belief trajectories, and market prices in a split-view layout.
2. Create a backend endpoint (`GET /api/simulations/compare?ids=A,B`) that returns normalized data for both simulations — aligned by round number, with delta calculations for key metrics (sentiment drift, market divergence, consensus formation rate).
3. Add a summary panel that highlights the top 3 differences between runs (e.g., "Run B reached consensus 4 rounds earlier", "Market diverged by 23% after round 6").

---

### 3. Embeddable Simulation Widget (iframe / Web Component)

**Type:** Growth / Integration
**Effort:** Medium (1-2 days)
**Impact:** Lets journalists, researchers, and bloggers embed a live or completed MiroShark simulation in their articles. This is the single highest-leverage growth move: every embedded simulation becomes a demo that drives traffic back to the repo. Similar to how Observable notebooks spread d3.js adoption.

**How:**
1. Create a lightweight read-only Vue component (`SimulationEmbed.vue`) that renders a simulation timeline, key agent posts, and market chart — no controls, just visualization. Bundle it as a standalone JS file via Vite library mode.
2. Add an embed endpoint (`GET /api/simulations/:id/embed`) that returns the necessary data in a compact format, with CORS headers for cross-origin embedding.
3. Add a "Share / Embed" button in the simulation results UI that generates an `<iframe>` snippet or Web Component tag users can copy.

---

### 4. Simulation Replay & Playback Speed Control

**Type:** DX Improvement
**Effort:** Small (hours)
**Impact:** Currently, simulations run forward and results are viewed statically. A replay mode with speed controls (1x, 2x, 5x, pause) lets users watch the simulation unfold step-by-step, seeing how agents react, beliefs shift, and markets move in real time. This dramatically improves the demo experience — a recorded replay is far more compelling than static screenshots for onboarding new users and creating content.

**How:**
1. Store round-by-round snapshots (already available in the simulation data) and build a frontend playback controller component with play/pause, speed slider, and round scrubber.
2. Animate the Twitter/Reddit/Polymarket feeds to show posts appearing in sequence within each round, with belief state and market price updating in sync.
3. Add a "Record GIF" or "Export Video" button that captures the playback as a shareable clip (using html2canvas or a similar library for frame capture).

---

### 5. Public Simulation Gallery & Community Showcase

**Type:** Community / Growth
**Effort:** Medium (1-2 days)
**Impact:** MiroShark has zero open issues and no community contribution pathway. A public gallery where users can share their simulation results (document + config + key findings) creates a reason for people to come back, learn from each other's experiments, and showcase interesting emergent behaviors. This is how tools like Hugging Face Spaces and Observable grew their communities — by making outputs shareable and discoverable.

**How:**
1. Add a `POST /api/gallery/submit` endpoint that accepts a simulation ID, a title, a short description, and optional tags. Store submissions in a JSON file or lightweight SQLite database (no new infra needed).
2. Build a `/gallery` page in the frontend that displays submitted simulations as cards (title, document type, agent count, key finding, thumbnail of the market chart). Include sort/filter by recency, popularity, and document type.
3. Add a "Publish to Gallery" button on the simulation results page. Include a disclaimer that published simulations are public. Seed the gallery with 3-5 example simulations covering different document types (policy, financial, tech press release).

---

## Ecosystem Context

These ideas are informed by the current landscape:
- **OASIS** (camel-ai) supports 1M agents but lacks prediction market integration — MiroShark's cross-platform engine is a differentiator worth doubling down on.
- **PolicySim** (ACM Web 2026) introduced proactive policy optimization via simulation — the A/B comparison feature positions MiroShark for this use case.
- **AI prediction market agents** now handle 18% of volume on Polymarket — MiroShark's simulated Polymarket is a safe sandbox for testing strategies before deploying real capital.
- The 2026 MABS workshop (May 26, Cyprus) represents a venue where MiroShark could be presented as a practical tool for social simulation research.
