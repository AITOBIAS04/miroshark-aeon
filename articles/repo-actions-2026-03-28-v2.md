# Repo Action Ideas — 2026-03-28 (Evening)

**Repo:** [aaronjmars/MiroShark](https://github.com/aaronjmars/MiroShark)
**Stars:** 325 | **Forks:** 54 | **Language:** Python + Vue.js
**Description:** Universal Swarm Intelligence Engine — multi-agent social simulation with Twitter, Reddit, and Polymarket platforms

## Current State

MiroShark has continued its aggressive development pace. Since the morning analysis: stars climbed from 322 to 325, forks from 53 to 54, and PR #3 (Simulation Replay with playback controls) was submitted — implementing one of the earlier action ideas within hours. The repo now has 3 open PRs (#1 simulation export, #2 preset templates, #3 replay), zero open issues, and 3 contributors.

Key recent additions include: Hyperstitions Design System v2.0 (Evangelion-inspired UI overhaul), graph reasoning tools (centrality, community detection, bridge entities), a 416-line round analyzer, cross-platform engine running Twitter/Reddit/Polymarket simultaneously, and 4 setup paths (Cloud API, Docker, Ollama, Claude Code CLI).

The competitive landscape is intensifying. MiroFish (the upstream project) has 32,300+ stars and $4.1M in funding. OASIS supports 1M-agent simulations. AI agents now represent 30%+ of Polymarket wallets. MiroShark's differentiation — the only fork with English-first UX, cross-platform prediction market integration, and Claude Code as a provider — needs deepening before MiroFish v2 catches up.

These 5 ideas are distinct from the earlier batch (webhook system, A/B testing, embeddable widget, replay, gallery) and focus on areas that compound MiroShark's unique positioning.

---

### 1. Real-Time Simulation Dashboard with WebSocket Streaming

**Type:** Feature
**Effort:** Medium (1-2 days)
**Impact:** Currently, users wait for simulations to complete before seeing results. Streaming round-by-round data to the frontend via WebSocket transforms the experience from "submit and wait" to "watch it unfold live." This makes demos dramatically more engaging and gives researchers the ability to spot emergent patterns in real time. Combined with the existing replay feature (PR #3), MiroShark would offer both live and historical viewing — a combination no competitor provides.

**How:**
1. Add a WebSocket endpoint (`/ws/simulation/{id}`) in the FastAPI backend that pushes events as each round completes: new posts, belief state updates, market price changes, and round summary.
2. Create a `LiveFeed.vue` component that connects to the WebSocket and renders incoming events as an animated feed — posts appear in real time, market charts update live, and belief trajectories draw as they happen.
3. Wire the existing `Step3Simulation.vue` to use the live feed during active simulations, falling back to the static view for completed ones.

---

### 2. Simulation Snapshot Sharing via Shareable Links (No Account Required)

**Type:** Growth / Community
**Effort:** Small (hours)
**Impact:** There's currently no way to share a simulation result with someone who doesn't have a running MiroShark instance. A one-click "Share" button that generates a static JSON snapshot and serves it at a unique URL turns every interesting simulation into a shareable artifact. This is the lowest-friction growth lever — users share links on Twitter/Discord/Reddit, recipients see the full simulation without installing anything.

**How:**
1. Add a `POST /api/simulations/{id}/snapshot` endpoint that serializes the complete simulation state (config, rounds, agent actions, market data, belief trajectories) into a single compressed JSON file, stores it in a `snapshots/` directory, and returns a unique slug.
2. Add a `GET /api/snapshots/{slug}` endpoint that serves the snapshot data, and a `SnapshotView.vue` page that renders it as a read-only simulation viewer (timeline, agent feed, market chart).
3. Add a "Share" button on the simulation results page that copies the snapshot URL to clipboard. Include Open Graph meta tags so the link unfurls nicely when pasted into social media.

---

### 3. Prompt Quality Scoring & Agent Coherence Metrics

**Type:** DX Improvement / Performance
**Effort:** Medium (1-2 days)
**Impact:** MiroShark generates hundreds of agent prompts per simulation, but there's no visibility into prompt quality or agent behavior coherence. A scoring system that evaluates each agent's output (on-topic rate, persona consistency, belief-action alignment) would help users tune their configurations and help the dev team identify where the prompt pipeline is weak. This is especially valuable as MiroShark supports multiple model tiers — users need guidance on which models produce coherent agents at each tier.

**How:**
1. Add a `prompt_scorer.py` module that evaluates agent outputs per round: persona adherence (does the agent stay in character?), topic relevance (does the post relate to the simulation document?), and belief-action consistency (does a bearish agent actually sell on Polymarket?). Score each 0-1 using lightweight heuristics (keyword overlap, sentiment alignment) rather than LLM calls.
2. Surface per-agent and per-round quality scores in the simulation results UI — add a "Quality" tab next to the existing round view that shows a heatmap of agent coherence over time.
3. Add aggregate metrics to the simulation report: average coherence, worst-performing agents, rounds where quality dropped (indicating prompt fatigue or context overflow).

---

### 4. Document Preprocessing Pipeline with Format Support Expansion

**Type:** Integration / DX
**Effort:** Medium (1-2 days)
**Impact:** MiroShark currently accepts document text as input, but users frequently have content in PDF, DOCX, or URL form. A preprocessing pipeline that handles format conversion, text extraction, and intelligent chunking would remove a major friction point in the workflow. Combined with URL fetching, users could paste a news article URL and start simulating immediately — dramatically lowering the barrier from "copy-paste text" to "paste link, click go."

**How:**
1. Add a `preprocessor.py` module with extractors for common formats: PDF (via `pymupdf` or `pdfplumber`), DOCX (via `python-docx`), HTML/URL (via `trafilatura` or `newspaper3k`), and plain text passthrough. Each extractor returns clean text with metadata (title, source, date).
2. Update the simulation config API to accept `source_type` (text, url, file) and `source_value`, routing through the appropriate extractor before graph construction begins.
3. Add a drag-and-drop file upload zone and URL input field to the frontend's simulation setup page, replacing the current text-only input.

---

### 5. Automated Simulation Benchmarking Suite

**Type:** Performance / Community
**Effort:** Large (2-3 days)
**Impact:** MiroShark has no published benchmarks comparing simulation quality across models, agent counts, or configurations. A benchmarking suite that runs standardized simulations and publishes results would serve three purposes: (1) help users pick the right model/config for their use case, (2) give the dev team regression data when changing the prompt pipeline, and (3) create a public leaderboard that attracts model developers and researchers. This directly addresses the MiroFish ecosystem's biggest gap — no published benchmarks comparing predictions to outcomes.

**How:**
1. Create a `benchmarks/` directory with 3-5 standardized test documents (policy draft, earnings report, crisis scenario, product launch, election debate) and expected outcome heuristics (e.g., "agents should form two opposing camps within 5 rounds").
2. Write a `run_benchmark.py` script that executes each scenario across multiple model configurations (GPT-4o-mini, DeepSeek-V3, Qwen, Ollama local) and collects metrics: time-to-completion, agent coherence scores, belief convergence rate, market price stability.
3. Output results as a markdown table and publish it in the repo's `docs/benchmarks.md`. Add a GitHub Actions workflow that re-runs benchmarks on each tagged release, creating a historical performance record.

---

## Ecosystem Context

These ideas are informed by the latest competitive signals:

- **MiroFish** (upstream) has 32,300+ stars and $4.1M funding — MiroShark must deepen its fork differentiation before MiroFish's v2 refactor absorbs the features that make MiroShark unique.
- **OASIS** supports 1M agents but has no user-facing product layer — MiroShark's full-stack approach (Vue frontend + FastAPI backend) is its moat, and ideas #1-2 widen it.
- **Polystrat** (Olas/Valory) and AI-Trader v2 show prediction market AI agents going mainstream — MiroShark's simulated Polymarket is a safe testing ground, and benchmarking (#5) would validate this use case.
- **SITGNet** introduced multi-stage RAG for social simulation — MiroShark's existing GraphRAG pipeline is competitive, but prompt quality scoring (#3) would demonstrate this rigor.
- The 2026 MABS workshop (May 26, Cyprus) and growing academic interest in LLM-based social simulation create demand for reproducible benchmarks — idea #5 positions MiroShark as a research tool, not just a demo.
