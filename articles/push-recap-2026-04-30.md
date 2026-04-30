# Push Recap — 2026-04-30

## Overview
5 meaningful commits by @aaronjmars across both repos yesterday — the headline is a new simulation transcript export feature that gives MiroShark its third quote-friendly share format (text, alongside the share card for preview and replay GIF for motion). Alongside that, the Wonderwall simulation slot gained a per-endpoint override so operators can route the 850+ agent-action calls to a self-hosted vLLM or fine-tune without touching the other model slots. The "Best" preset was retired in favor of a single streamlined "Cloud" default.

**Stats:** ~40 files changed, +2,301/-418 lines across 5 commits (plus ~28 automated cron/scheduler commits on miroshark-aeon)

---

## aaronjmars/MiroShark

### New Feature: Simulation Transcript Export

**Summary:** MiroShark now exports simulation transcripts as both Markdown (with YAML front matter for Notion/Obsidian/Substack import) and structured JSON (for SDK consumers and LLM-as-judge pipelines). This completes the trio of share formats: share card (preview), replay GIF (motion), transcript (text). The feature ships with an 18-test suite, OpenAPI spec coverage, and full EmbedDialog integration.

**Commits:**
- `48b38f9` — feat: simulation transcript export (Markdown + JSON) (#57)
  - New file `backend/app/services/transcript.py`: 615-line pure-stdlib renderer. Reads trajectory.json, quality.json, resolution.json, outcome.json, and profile files. Builds per-round sections with agent posts as block quotes tagged with stance labels. Uses the same +/-0.2 stance threshold as every other surface (gallery, share card, webhook, replay GIF) so labels stay consistent. Markdown form opens with YAML front-matter block; JSON form is pretty-printed for curl-to-file readability. 80-round cap on Markdown with head/tail preservation and "skipped N rounds" annotation (+615 lines)
  - Changed `backend/app/api/simulation.py`: Added `_serve_transcript()` shared handler + two route handlers (`transcript.md` and `transcript.json`), both behind the same publish gate as share card (+86 lines)
  - New file `backend/tests/test_unit_transcript.py`: 493-line test suite — stance threshold parity, profile name resolution (reddit + polymarket), corrupt artifact graceful degradation, long-post excerpting, YAML front-matter escaping, per-round section emission, oversized trajectory truncation, JSON round-trip, route decorator presence guard (+493 lines)
  - Changed `backend/openapi.yaml`: Two new paths under Publish & Embed + `SimulationTranscript` schema with full per-round shape (+143 lines)
  - Changed `frontend/src/components/EmbedDialog.vue`: "Export transcript" section with Download .md / Download .json buttons, copyable Markdown URL, publish-gated empty state (+156 lines)
  - Changed `frontend/src/api/simulation.js`: `getTranscriptMarkdownUrl()` and `getTranscriptJsonUrl()` helpers (+33 lines)
  - Changed `docs/FEATURES.md`: "Simulation Transcript Export" section (+11 lines)
  - Changed `README.md`: Added Transcript Export to features table (+1 line)

- `cee23c7` — fix(ci): split agent-env compaction helpers into stdlib-only module (#58)
  - New file `backend/lib/env_compact.py`: Moved `_compact_post_for_agent`, `_compact_posts_for_agent`, `_compact_comment`, `_comment_score`, `_parse_ts`, `_MAX_COMMENTS_PER_POST` out of `wonderwall.social_agent.agent_environment` into a standalone module under `backend/lib/` (+120 lines)
  - Changed `backend/wonderwall/social_agent/agent_environment.py`: Replaced inline implementations with imports from `lib.env_compact` (-109, +8 lines)
  - Changed `backend/tests/test_unit_agent_env_compaction.py`: Updated import path (-1, +1 line)
  - The reason: the offline unit test suite was importing the compaction helpers from within the wonderwall package, which transitively pulls in CAMEL -> numpy -> torch and would force the CI dependency set to grow significantly. Moving them to a stdlib-only module keeps the test suite lean.

**Impact:** Simulations can now be cited in research papers, Substack posts, and Discord threads by linking the Markdown transcript URL or downloading the file directly. The YAML front matter means Notion and Obsidian recognize it as a structured document on import. The CI fix ensures the offline test suite stays fast by avoiding heavy ML framework imports.

### Config Overhaul: Wonderwall Per-Slot Endpoint + Cloud Preset Refresh

**Summary:** The Wonderwall simulation slot now accepts an independent endpoint override (`WONDERWALL_BASE_URL` + `WONDERWALL_API_KEY`) so operators can route the 850+ agent-action calls per run to a self-hosted vLLM, Modal deployment, or fine-tuned model without touching the Default/Smart/NER slots. The "Best" preset (Claude Haiku + Sonnet, ~$3.50/run) was retired — the new default is a single "Cloud" preset using Mimo V2 Flash + Grok-4.1 Fast at ~$1/run.

**Commits:**
- `2e782e0` — feat(wonderwall): per-slot endpoint override + cloud preset refresh (#59)
  - Changed `.env.example`: Complete rewrite — defaults to Cloud (OpenRouter) instead of local Ollama. Active LLM/Smart/NER/Wonderwall slots now use Mimo V2 Flash and Grok-4.1 Fast. Ollama and Claude Code modes moved to a commented "Alternatives" block. Wonderwall per-slot override documented (+91, -136 lines)
  - Changed `backend/app/config.py`: Added `WONDERWALL_API_KEY` and `WONDERWALL_BASE_URL` config fields. Updated default model names and comments from Cheap/Best to Cloud (+11, -7 lines)
  - Changed `backend/app/api/settings.py`: Removed the "best" preset entirely. Renamed "cheap" label to "Cloud". Settings API now accepts `wonderwall.base_url` and `wonderwall.api_key`. Snapshot includes Wonderwall endpoint info (+14, -27 lines)
  - Changed `backend/scripts/run_parallel_simulation.py`: `create_model()` now prefers `WONDERWALL_API_KEY` / `WONDERWALL_BASE_URL` over `LLM_*` for the simulation loop (+6, -4 lines)
  - Changed `backend/scripts/run_reddit_simulation.py` and `run_twitter_simulation.py`: Same WONDERWALL_* override pattern (+10, -7 each)
  - Changed `backend/app/services/simulation_runner.py`: Forwards runtime Config.WONDERWALL_* into subprocess env at spawn time, so Settings UI updates apply on next run without Flask restart (+10 lines)
  - Changed `backend/app/utils/run_summary.py`: Added Mimo V2 Flash and Grok-4.1 Fast to the pricing table (+4, -3 lines)
  - Changed `frontend/src/components/SettingsPanel.vue`: Wonderwall section now has Base URL and API Key fields alongside Model Name. Preset logic simplified (+31, -7 lines)
  - Changed `frontend/src/views/Home.vue`: "Cheap preset" -> "cloud preset" (+1, -1 line)
  - Changed `docs/CONFIGURATION.md`, `docs/MODELS.md`, `docs/INSTALL.md`, `docs/FEATURES.md`, `README.md`: Updated all documentation to reflect single Cloud preset, per-slot Wonderwall override, and new model lineup

**Impact:** Operators with a self-hosted GPU or custom fine-tune can now split their inference — keep graph build and reports on OpenRouter while the expensive simulation loop targets a local or private endpoint. The Cloud preset simplification (one preset instead of two) reduces setup friction for new users.

### Bug Fix: Observability Pagination Hardening

**Summary:** The observability event and LLM-call endpoints were calling `int()` directly on query string parameters, which raises `ValueError` on non-numeric input and causes a Flask 500. Now they use Flask's `type=int` coercion, which silently falls back to the default.

**Commits:**
- `02ff29a` — fix(observability): coerce pagination ints via Flask type= so bad input doesn't 500 (#56)
  - Changed `backend/app/api/observability.py`: Replaced `int(request.args.get(...))` with `request.args.get(..., type=int)` on `from_line`, `limit`, `agent_id`, `round_num` across both `/events` and `/llm-calls` endpoints (+10, -8 lines)
  - New file `backend/tests/test_unit_observability_routes.py`: 114-line test suite with stub Flask app — validates that garbage `from_line`, `limit`, `agent_id`, and `round_num` values return 200 instead of 500 (+114 lines)

**Impact:** Malformed query strings from bots, debugging tools, or copy-paste errors no longer 500 the observability endpoints. Defensive improvement for production readiness.

---

## aaronjmars/miroshark-aeon

### Improvement: Skill Leaderboard Multi-Repo Aggregation

**Summary:** The skill-leaderboard skill was only scanning the first entry in `watched-repos.md` for active forks. Since `aaronjmars/MiroShark` is an application repo (not an aeon instance), it found 107 forks but zero with `aeon.yml`. The actual aeon instance (`miroshark-aeon`) sat at position 2 and was never scanned.

**Commits:**
- `b910088` — improve: skill-leaderboard scans all watched repos (#26)
  - Changed `skills/skill-leaderboard/SKILL.md`: Step 1 now reads every entry from `watched-repos.md` into a `TARGET_REPOS` array. Step 2 iterates all repos, fetches active forks for each, and unions results deduped by `full_name`. Article footer and log entry record the full source-repo list (+9, -6 lines)
  - Changed `.outputs/self-improve.md`: Updated with the rationale for the fix (+8, -7 lines)
  - Changed `memory/MEMORY.md`: Added Skills Built entry for the multi-repo aggregation fix (+1 line)
  - Changed `memory/logs/2026-04-28.md`: Detailed log of the self-improve run (+11 lines)
  - Changed `memory/token-usage.csv`: Token usage entry for the self-improve run (+1 line)
  - New file `dashboard/outputs/self-improve-2026-04-28T13-21-20Z.json`: json-render dashboard spec (+179 lines)

**Impact:** The Sunday skill leaderboard run (May 3) can now find aeon forks across all watched repos, meeting the >=2-fork notification threshold as soon as a second aeon instance fork appears. Adding new repos to `watched-repos.md` automatically expands the leaderboard surface.

---

## Developer Notes
- **New dependencies:** None across both repos
- **Breaking changes:** The "Best" preset has been removed from MiroShark's Settings API — any client calling `POST /api/settings` with `preset: "best"` will get an error. The "cheap" preset key is unchanged but its label and model lineup have been updated.
- **Architecture shifts:** Compaction helpers moved from `wonderwall.social_agent.agent_environment` to `backend/lib/env_compact.py` — a new `backend/lib/` package for stdlib-only utilities that the test suite can import without heavy ML deps.
- **Tech debt:** None introduced — the CI refactor actively reduces test-time dependency bloat.

## What's Next
- The transcript export pairs naturally with a future **Simulation SDK/client library** — the JSON transcript endpoint is the first structured export endpoint purpose-built for programmatic consumers.
- The Wonderwall per-slot endpoint override sets up **fine-tune experimentation** — operators can now A/B test custom agent models against the stock OpenRouter lineup while holding everything else constant.
- The 15-day auth outage (Apr 16–30) means several scheduled skills haven't run in two weeks; the first successful heartbeat today confirmed auth is restored, so the backlog of scheduled skills should start clearing.
