# Push Recap — 2026-03-26

## Overview
A massive day of development: 10 commits by 2 authors (Aaron Elijah Mars and github-actions[bot]). The headline is a monumental integration of Wonderwall — a bundled Polymarket prediction market simulation — as the third platform in MiroShark, turning it from a dual-platform social simulator into a full multi-platform agent environment. Meanwhile, the agent repo (miroshark-aeon) saw a burst of new skills and rapid iteration on repo-pulse observability.

**Stats:** ~108 files changed, +9,771/-1,901 lines across 10 commits

---

## aaronjmars/MiroShark

### Wonderwall: Polymarket Prediction Market Integration
**Summary:** This single, massive commit bundles an entire simulation framework — Wonderwall (an OASIS fork) — directly into the MiroShark backend, adding Polymarket as a third simulation platform alongside Twitter and Reddit. Agents can now create prediction markets, trade on outcomes via an AMM (automated market maker), manage portfolios, and see their activity across all three platforms through a new cross-platform digest system.

**Commits:**
- `452abd2` — feat: integrate Wonderwall (Polymarket) as third simulation platform
  - **New package `backend/wonderwall/`** (75+ new files): A complete social simulation engine bundled directly rather than installed as a pip dependency. Includes:
    - `social_agent/` — Agent logic: `agent.py` (355 lines) for agent behavior, `agent_action.py` (758 lines) for action execution, `agent_graph.py` (292 lines) for relationship graphs, `agents_generator.py` (649 lines) for profile generation
    - `social_platform/` — Platform infrastructure: `platform.py` (1,642 lines) implementing the full social media platform DB operations, `recsys.py` (797 lines) for recommendation system, `database.py` (223 lines) for SQLite-backed storage
    - `simulations/polymarket/` — Polymarket-specific simulation: `platform.py` (412 lines) with market creation/resolution/trading, `amm.py` (165 lines) implementing a constant-product AMM for price discovery, `actions.py` (142 lines) for trade/comment/create-market actions, SQL schemas for markets, trades, positions, portfolios, and comments
    - `simulations/social_media/` — Social media simulation base with prompts and schemas
    - `clock/`, `environment/`, `testing/` — Supporting infrastructure for simulation time, environment state, and debugging
  - **Modified `backend/scripts/run_parallel_simulation.py`** (+472/-59): Extended the parallel runner to orchestrate Twitter + Reddit + Polymarket simulations concurrently, with new `--enable-polymarket` and `--cross-platform` flags
  - **New `backend/scripts/cross_platform_digest.py`** (+231): Generates digests that let agents see their activity on other platforms — e.g., a Twitter agent can see what their persona did on Polymarket
  - **New `backend/scripts/test_polymarket.py`** (+182): Integration test for the Polymarket simulation pipeline
  - **Modified `backend/app/services/simulation_runner.py`** (+89/-22): Backend service now handles Polymarket simulation lifecycle, IPC race condition fix with PID tracking in `env_status`
  - **Modified `backend/app/services/oasis_profile_generator.py`** (+77): Added `risk_tolerance` field to agent profiles, `to_polymarket_format()` converter, and `_infer_risk_tolerance()` from personality traits
  - **Modified `backend/app/api/simulation.py`** (+12/-7): New `enable_polymarket` parameter, renamed `OASIS_SIMULATION_DATA_DIR` to `WONDERWALL_SIMULATION_DATA_DIR`
  - **Modified `backend/app/config.py`** (+11/-7): Config references updated from OASIS to Wonderwall
  - **Modified `backend/app/services/simulation_ipc.py`** (+14/-3): Fixed report interviews hanging when simulation is completed — skips IPC and falls back to LLM
  - **Modified `frontend/src/components/Step3Simulation.vue`** (+293/-119): Complete UI overhaul — 3-row platform status display (X/Reddit/Polymarket), platform filtering dropdown, new trade cards for Polymarket actions, fixed empty cards for mute/dislike actions
  - **Modified `backend/uv.lock`** (-1,518): Removed the old `camel-oasis` pip dependency since Wonderwall is now bundled
  - **Modified `backend/pyproject.toml`** (+3/-2) and `backend/requirements.txt`** (+3/-3): Dependency updates reflecting the OASIS→Wonderwall switch

**Impact:** MiroShark is no longer just a social media simulator — it's now a multi-platform agent environment where AI agents can simultaneously post on Twitter, discuss on Reddit, and trade on prediction markets. The cross-platform awareness means agents develop coherent personas across platforms, and the bundled Wonderwall package gives the project full control over the simulation engine rather than depending on an external pip package. This is a major architectural evolution.

---

## aaronjmars/miroshark-aeon

### New Agent Skills: Repo-Pulse, Hyperstitions, Self-Improve
**Summary:** Three new skills were added to the Aeon agent framework, expanding its autonomous capabilities from content generation into observability (repo-pulse), creative ideation (hyperstitions-ideas), and meta-improvement (self-improve). Telegram message polling was also disabled to reduce noise.

**Commits:**
- `e02f7d7` — feat: add repo-pulse, hyperstitions-ideas, self-improve skills + disable TG polling
  - New `skills/repo-pulse/SKILL.md` (+77): Daily stars/forks/traffic tracking for watched repos with delta calculations and notifications
  - New `skills/hyperstitions-ideas/SKILL.md` (+81): Generates prediction market ideas from live project signals — designed as coordination tools to rally community action
  - New `skills/self-improve/SKILL.md` (+85): Agent self-improvement skill that analyzes daily logs to find patterns and suggest improvements
  - Modified `.github/workflows/aeon.yml` (+3): Added workflow triggers for new skills
  - Modified `.github/workflows/messages.yml` (+20/-23): Disabled Telegram inbound polling (outbound notifications still work)
  - Modified `aeon.yml` (+6/-1): Added schedule entries for all three new skills
  - Modified `memory/watched-repos.md` (+1): Added miroshark-aeon itself to watched repos for self-monitoring

**Impact:** The agent now monitors its own repo ecosystem, generates creative content tied to the project's real state, and has a feedback loop for self-improvement. This moves Aeon from a pure content engine toward an autonomous operator that can observe, reflect, and adapt.

### Repo-Pulse Bug Fixes & Iteration
**Summary:** A rapid burst of 4 fixes to repo-pulse within hours of its first deployment, addressing issues with star counting accuracy, time window calculations, output formatting, and agent repo filtering. A classic ship-then-fix cycle that hardened the skill considerably.

**Commits:**
- `9371563` — fix: repo-pulse pagination + hyperstitions rename
  - Modified `skills/repo-pulse/SKILL.md` (+56/-40): Added `--paginate` for stargazers API, fixed delta calculation logic, refined notification format
  - Modified `skills/hyperstitions-ideas/SKILL.md` (+34/-26): Major rewrite — shifted from generic prediction markets to project-specific coordination mechanisms, added concrete good/bad examples, linked to hyperstitions.com

- `a1d8320` — fix: repo-pulse checks new stargazers, not net total delta
  - Modified `skills/repo-pulse/SKILL.md` (+8/-5): Fixed a bug where unstars were canceling out new stars (net delta=0 even with new stargazers). Now checks for any stargazer with `starred_at` in last 24h regardless of net change.

- `5af5d60` — fix: repo-pulse uses 24h cutoff, not midnight; skip agent repos
  - Modified `skills/repo-pulse/SKILL.md` (+18/-13): Changed time filter from "since midnight" to "exactly 24 hours ago" for accurate rolling window. Added logic to skip agent/monitoring repos (aeon-agent, miroshark-aeon) from pulse tracking.

- `f2371cb` — fix: repo-pulse remove traffic, cleaner format
  - Modified `skills/repo-pulse/SKILL.md` (+23/-34): Stripped traffic data, watchers, and open issues from notifications. Stargazers and forks now displayed on single lines separated by `|` instead of one-per-line. Empty sections omitted entirely.

**Impact:** Repo-pulse went from a first draft to a production-hardened skill in one day. The final version accurately detects new stars using the GitHub API's `starred_at` timestamps, handles unstars gracefully, uses proper 24h rolling windows, and produces clean, concise notifications.

### Scheduling & Automated Operations
**Summary:** Schedule adjustments and routine automated commits from the agent's heartbeat and repo-pulse skills.

**Commits:**
- `f2f874e` — chore: schedule repo-pulse at 20:00 UTC for testing
  - Modified `aeon.yml` (+1/-1): Moved repo-pulse from 10:00 UTC to 20:00 UTC schedule for immediate testing

- `115121d` — chore(heartbeat): auto-commit 2026-03-26
  - Modified `memory/logs/2026-03-26.md` (+6): First heartbeat log entry for the day

- `d73c7bd` — chore(heartbeat): auto-commit 2026-03-26
  - Modified `memory/logs/2026-03-26.md` (+8/-1): Second heartbeat noting 10 skills didn't run, identifying missing cron trigger in aeon.yml

- `e3c376e` — chore(repo-pulse): auto-commit 2026-03-26
  - Modified `memory/logs/2026-03-26.md` (+6): Logged repo-pulse results — MiroShark at 281 stars (+13 new), 46 forks (+3 new)

**Impact:** The agent is now self-monitoring and logging its own operational state, catching issues like the missing cron trigger that prevented daily skills from running.

---

## Developer Notes
- **New dependencies:** Wonderwall simulation engine bundled at `backend/wonderwall/` (replaces `camel-oasis` pip package)
- **Breaking changes:** `OASIS_SIMULATION_DATA_DIR` renamed to `WONDERWALL_SIMULATION_DATA_DIR` in config — any external references to the old name will break
- **Architecture shifts:** MiroShark moved from 2-platform (Twitter + Reddit) to 3-platform (+ Polymarket) simulation. The simulation engine is now vendored rather than installed as an external dependency, giving full control over the codebase.
- **Tech debt:** The Wonderwall package is a large vendored dependency (~8,000+ lines) that will need ongoing maintenance as it diverges from upstream OASIS

## What's Next
- The Polymarket simulation needs real-world testing with agent runs — the test script exists but end-to-end validation with the frontend is likely next
- Cross-platform digest feature opens the door to agents that strategically coordinate across platforms (e.g., create a market on Polymarket, then promote it on Twitter)
- The heartbeat identified that daily skills aren't running due to missing cron triggers in the GitHub Actions workflow — fixing the scheduler is a priority
- Repo-pulse is stable and running; next iteration might add trending/velocity metrics
- Self-improve skill hasn't run yet — first execution will set the baseline for agent self-analysis
