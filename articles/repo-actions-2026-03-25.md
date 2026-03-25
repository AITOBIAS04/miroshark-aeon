# Repo Action Ideas — 2026-03-25

**Repo:** [aaronjmars/MiroShark](https://github.com/aaronjmars/MiroShark)
**Description:** Universal Swarm Intelligence Engine — multi-agent social simulation
**Stars:** 269 | **Forks:** 43 | **Open Issues:** 0 | **Language:** Python + Node.js

## Current State

MiroShark is a multi-agent simulation engine forked from MiroFish. Users upload documents (press releases, policy drafts, financial reports) and hundreds of AI agents with unique personalities simulate public reaction on social media — posts, arguments, opinion shifts — hour by hour.

Recent development has been active with 27+ commits covering:
- Claude Code CLI as an LLM provider option
- Smart model tier for routing intelligence-sensitive workflows to stronger models
- OpenRouter cloud support with detailed model recommendations
- Token-saving text filters in the preprocessor
- Full English i18n (originally Chinese codebase)
- Neo4j + Ollama local stack replacing Zep Cloud
- OpenRouter embeddings, simulation controls, and UX overhaul

The project has 3 contributors (666ghj with 219 commits, aaronjmars with 27, cursoragent with 1) and zero open issues — suggesting the project is in active development but not yet widely community-contributed.

---

## Action Ideas

### 1. Add Simulation Export to JSON/CSV

**Type:** Feature
**Effort:** Small (hours)
**Impact:** Users currently can only view simulation results in the web UI. Exporting simulation data (agent posts, sentiment timelines, opinion shifts) to structured JSON/CSV formats would unlock downstream analysis in Jupyter, Excel, or BI tools — a key ask for the PR crisis testing and trading signal use cases.
**How:**
1. Add an `/api/export` endpoint in the backend that serializes the simulation run's agent posts, sentiment scores, and timeline data from Neo4j into JSON and CSV formats.
2. Add a "Download Results" button in the frontend report view that calls this endpoint.
3. Include metadata (simulation config, document hash, timestamp) in the export header for reproducibility.

---

### 2. Add a Pre-Built Scenario Gallery

**Type:** DX Improvement
**Effort:** Medium (1-2 days)
**Impact:** New users currently need to bring their own document to try MiroShark, which raises the barrier to first meaningful use. A gallery of 3-5 pre-built scenarios (e.g., "Tech layoff press release," "New crypto regulation draft," "Product recall announcement") would let users run a simulation in under 60 seconds and immediately see the value. This directly improves onboarding and demo-ability, which drives GitHub stars and word-of-mouth.
**How:**
1. Create a `scenarios/` directory with 3-5 curated documents covering diverse use cases (PR crisis, financial news, policy, creative).
2. Add a "Try a Demo" section to the frontend landing page that lists available scenarios with one-click launch.
3. Include expected output previews or screenshots so users know what to expect before committing to a full simulation run.

---

### 3. GitHub Actions CI Pipeline with Docker Build Test

**Type:** Security / DX Improvement
**Effort:** Small (hours)
**Impact:** The repo has no CI pipeline. Adding a GitHub Actions workflow that builds the Docker image and runs basic smoke tests on every PR would prevent regressions in the Docker setup path (the most common onboarding method), catch dependency issues early, and signal project maturity to potential contributors. With 43 forks, regressions from external PRs are a real risk.
**How:**
1. Create `.github/workflows/ci.yml` with jobs for: Docker Compose build, Python linting (ruff), frontend lint + build, and a basic health check (start services, hit `/api/health`).
2. Add a `backend/tests/test_health.py` smoke test that verifies the API starts and responds.
3. Add the CI badge to the README to signal project quality.

---

### 4. Integrate Real-Time News Feed as Simulation Input

**Type:** Integration
**Effort:** Medium (1-2 days)
**Impact:** Currently users must manually paste documents. Adding an RSS/news API integration would let users point MiroShark at a live news feed and auto-trigger simulations on breaking stories — transforming it from a one-shot tool into a continuous monitoring system. This is especially valuable for the trading signal and PR crisis use cases where speed matters.
**How:**
1. Add a `news_ingestion` module in the backend that accepts an RSS feed URL or news API key (e.g., NewsAPI, Mediastack) and polls for new articles on a configurable interval.
2. When a new article arrives, auto-create a simulation run with the article text as the input document.
3. Add a "Watch Feed" UI in the frontend that lets users configure feeds and view a timeline of triggered simulations.

---

### 5. Add a Contributor Guide and "Good First Issue" Labels

**Type:** Community
**Effort:** Small (hours)
**Impact:** MiroShark has 43 forks but only 3 contributors and zero open issues. The project lacks a CONTRIBUTING.md, issue templates, and labeled issues — which means potential contributors have no entry point. Adding these community fundamentals would convert fork-watchers into active contributors, especially since the codebase was recently translated to English and is now accessible to a global audience.
**How:**
1. Create `CONTRIBUTING.md` covering: local dev setup, code style (Python/ruff, Node/ESLint), PR workflow, and architecture overview (backend/frontend/Neo4j/CAMEL-AI boundaries).
2. Create GitHub issue templates for bug reports and feature requests (`.github/ISSUE_TEMPLATE/`).
3. File 5-8 issues tagged "good first issue" covering small, well-scoped tasks (e.g., "Add loading spinner to simulation start," "Add unit tests for graph builder," "Improve error message when Neo4j is unreachable").
