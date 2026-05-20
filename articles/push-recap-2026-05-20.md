# Push Recap — 2026-05-20

## Overview

51 commits by 3 authors across 2 repos. The main event: MiroShark shipped two new share surfaces in 24 hours — Trading Signal JSON (#91) and Simulation Archive Bundle (#92) — bringing the total to 12 publish-gated distribution surfaces. A first external security contribution landed (#89), and on the Aeon side, self-improve diagnosed a 3-day tweet-allocator drift and opened a fix.

**Stats:** ~80 files changed, +3,500/-60 lines across 51 commits

---

## aaronjmars/MiroShark

### New Surface: Simulation Archive Bundle (PR #92)

**Summary:** Every published share surface — share card, chart SVG, trajectory CSV/JSONL, transcript, thread, reproduce.json, notebook, signal.json — collapsed into a single timestamped ZIP download. The twelfth publish-gated surface, and the first one that composes all the others rather than adding a new data type.

**Commits:**
- `9b8449a` — feat: simulation archive bundle — one ZIP, every published surface inside (#92)
  - New `backend/app/services/archive_service.py` (506 LoC): Pure-stdlib ZIP builder using `zipfile` + `hashlib`. Calls every existing surface renderer (share_card, chart_svg, trajectory_export, repro_export, notebook_export, signal_service, transcript, thread_formatter) and assembles results into a ZIP. Best-effort: missing surfaces are omitted, not errors. Fixed `date_time=(1980,1,1,...)` on every ZipInfo for bytewise-stable archives across requests (+506 lines)
  - New `backend/tests/test_unit_archive_service.py`: 20 offline unit tests covering manifest schema validation, per-file SHA-256 correctness, graceful degradation when surfaces fail, deterministic timestamps (+465 lines)
  - Changed `backend/app/api/simulation.py`: New `GET /api/simulation/<id>/archive.zip` route behind the publish gate. Sets `Content-Disposition: attachment` with a `miroshark-{sim_id}-{timestamp}.zip` filename. HEAD requests return `X-MiroShark-Archive-Files` header with the count (+119 lines)
  - Changed `backend/app/services/surface_stats.py`: Added `archive_zip` counter to surface stats tracking (+3, -1 lines)
  - Changed `backend/openapi.yaml`: ArchiveManifest, ArchiveFile, ArchiveResponse schemas under new Archive tag (+187 lines)
  - Changed `frontend/src/components/EmbedDialog.vue`: New archive section with download button and manifest preview (+197 lines)
  - Changed `frontend/src/api/simulation.js`: `getArchiveUrl()` and `getArchiveManifest()` helpers (+62 lines)
  - Changed `README.md`: Archive Bundle row in features table (+2, -1 lines)
  - Changed `docs/FEATURES.md`: Archive Bundle section with manifest schema example (+44 lines)
  - Changed `backend/tests/test_unit_surface_stats.py`: archive_zip counter assertion (+2 lines)

**Impact:** Researchers and archivists can grab a complete simulation artifact in one HTTP request instead of chaining 10+ curl calls. The manifest.json pairs every file with its SHA-256, so citation hashes from the archive match the standalone routes byte-for-byte. This is the compositional capstone of the 12-surface distribution stack — every prior surface is now both individually addressable and collectively downloadable.

### New Surface: Trading Signal JSON (PR #91)

**Summary:** Machine-readable action primitive that collapses a simulation's final-round belief split and quality health into a signal a quant tool, Zapier workflow, or n8n pipeline can consume directly: direction (Bullish/Neutral/Bearish) + confidence_pct (0 = three-way split, 100 = unanimous) + risk_tier (low/medium/high from quality health) + the three component percentages.

**Commits:**
- `3fe86ea` — feat: trading signal JSON — machine-readable action primitive for quant tools (#91)
  - New `backend/app/services/signal_service.py` (241 LoC): Pure derivation from `_build_embed_summary_payload` — no new computation. Confidence formula: `(leading_pct - 33.333) / 66.667 * 100`. Quality-to-risk mapping defaults to high-risk for unknown/missing quality (cautious posture). Three-way tie-break order: bullish > bearish > neutral (+241 lines)
  - New `backend/tests/test_unit_signal_service.py`: 26 offline unit tests covering unanimous, split, edge-case, and quality-degraded signals. Midpoint confidence tolerance bumped to 0.2 to handle IEEE 754 rounding on one-decimal quantization (+380 lines)
  - Changed `backend/app/api/simulation.py`: New `GET /api/simulation/<id>/signal.json` route behind publish gate (+85 lines)
  - Changed `backend/app/services/surface_stats.py`: Added `signal_json` counter (+3, -1 lines)
  - Changed `backend/openapi.yaml`: TradingSignal and TradingSignalResponse schemas (+157 lines)
  - Changed `frontend/src/components/EmbedDialog.vue`: Signal JSON section with copy-URL and schema preview (+245 lines)
  - Changed `frontend/src/api/simulation.js`: `getSignalJson()` helper (+47 lines)
  - Changed `README.md`: Trading Signal JSON row in features table (+2, -1 lines)
  - Changed `docs/FEATURES.md`: Trading Signal JSON section (+35 lines)
  - Changed `backend/tests/test_unit_surface_stats.py`: signal_json counter assertion (+2 lines)

**Impact:** Closes the gap between "a simulation produces data" and "a simulation produces a signal." Quant tools that previously had to parse transcript prose or trajectory CSVs to extract a directional call now get it in one JSON field. This is the last-mile surface the quant audience needed — everything from Zapier to a custom Python alert can consume it as-is. 27-PR zero-new-deps streak preserved (now 28 with the archive bundle).

### Security Hardening: Neo4j Default Password Removal (PR #89)

**Summary:** First external security contribution. Removes the hardcoded Neo4j password "miroshark" from docker-compose.yml and .env.example — a real risk on any deployment where ports 7474/7687 are reachable (Railway/Render one-click deploys expose public HTTPS endpoints).

**Commits:**
- `d4a2256` — security: require explicit NEO4J_PASSWORD, remove hardcoded default (#89) — by Furin (@teifurin)
  - Changed `docker-compose.yml`: Both `NEO4J_AUTH` (neo4j service) and `NEO4J_PASSWORD` (miroshark service) now reference `${NEO4J_PASSWORD:?NEO4J_PASSWORD must be set in .env}` — fail-fast with a clear error if unset (+2, -2 lines)
  - Changed `.env.example`: Literal default replaced with `CHANGE_ME_GENERATE_A_RANDOM_PASSWORD` placeholder (+1, -1 lines)

**Impact:** Any deployment that naively copied .env.example no longer ships with a publicly-known database credential. The `?` syntax in the docker-compose variable reference means `docker compose up` will refuse to start if the password isn't set, catching the misconfiguration at launch rather than in production.

---

## aaronjmars/miroshark-aeon

### Self-Improvement: Bankr Agent Timeout Fix (PR #43)

**Summary:** Self-improve diagnosed a 3-day TWEET_ALLOCATOR_EMPTY drift (May 18–20) where previously-verified wallet handles silently returned null because the Bankr Agent's Max-Mode calls exceeded the 64-second polling ceiling. The fix distinguishes "agent timed out" from "agent found no wallet" — two very different failure modes that were previously indistinguishable.

**Commits:**
- `cd5698e` — log: self-improve PR #43 (bankr-prefetch agent-timeout distinction)
  - Changed `memory/MEMORY.md`: Added Skills Built entry for bankr-prefetch agent-timeout distinction (+1 line)
  - Changed `memory/logs/2026-05-20.md`: Detailed log of the self-improve run — root cause analysis, diff breakdown, impact assessment (+11 lines)

**Changes on branch `improve/bankr-prefetch-poll-timeout`:**
- `scripts/prefetch-bankr.sh`: Poll loop extended 8 → 14 iterations (~64s → ~112s window); submit max-time 30 → 45s; new `TIMED_OUT` counter; timed-out handles excluded from `verified-handles.json`; new `prefetch-status.json` field `timed_out`; new top-level status `"agent-timeout"`
- `skills/tweet-allocator/SKILL.md`: New step-4 branch routing `agent-timeout` → `TWEET_ALLOCATOR_ERROR` (alert) instead of silent `_EMPTY`

**Impact:** Future LLM-mode latency spikes surface as an explicit TWEET_ALLOCATOR_ERROR with a retry/credit hint, not a silent TWEET_ALLOCATOR_EMPTY that looks like "no one tweeted with a wallet." The doubled polling window should also rescue handles that previously timed out within the 64s budget.

### Feature Build: Curator Collections (local, push blocked)

**Summary:** Named, ordered lists of published simulations — a curation primitive for citation bundles, research tours, and community arguments. Code complete but push blocked (GH_GLOBAL not set, 20th consecutive block).

**Key components:**
- `collections.py` CRUD service: Atomic JSON writes, path-traversal validation, dedup, title/desc caps, sim removal propagation
- 5 REST endpoints at `/api/collections` (POST/GET/GET/:id/PATCH/DELETE), admin-gated mutations
- `GET /api/simulation/:id/collections` cross-link endpoint
- `CollectionsView.vue` + `CollectionDetailView.vue` with rank badges, consensus bars, scenario excerpts
- `/collections` and `/collections/:id` routes
- Collections chip on `/explore` gallery
- 22 unit tests, OpenAPI spec (6 schemas), bilingual docs

**Stats:** 15 files, +1,722 lines, zero new dependencies

### Daily Operations Cycle

**Summary:** Full Tuesday skill cycle executed — 10 skills ran successfully across the day. All operational metrics stable: token consolidating post-ATH, stars cooling from the May breakout pace.

**Key runs:**
- `8421d94` — Token report: $MIROSHARK at $0.00003044 (+0.83% 24h), FDV $3.04M, LP $1.02M (first time above $1M sustained). Volatile session — $0.0000348 high / $0.0000206 low, full recovery. 7d +215%, 30d +1,256%
- `b19b34a` — Repo pulse: 1,177 stars (+2 24h), 238 forks (+1). New fork by Artnocontra
- `1d9d48b` — Star momentum: 1,177 → 1,500 in ~67 days at current 4.86/day pace (cooled from 6.0/day). Out of Show HN launch window
- Feature auto-commit: Curator Collections build (see above)
- `fe692da` — Push recap for May 19: Documented Farcaster Frame v2 merge, Trading Signal JSON open, 40 commits across repos
- Cron bookkeeping: 32 scheduler/cron-state commits maintaining operational state

---

## Developer Notes

- **New dependencies:** None. Both MiroShark PRs maintain the zero-new-deps posture — streak now at 28 consecutive PRs (PR #57 → #92)
- **Breaking changes:** Neo4j deployments that relied on the hardcoded default password in docker-compose.yml will fail to start until NEO4J_PASSWORD is set in `.env`. This is intentional — the fail-fast is the fix
- **Architecture shifts:** The archive bundle is the first *compositional* surface — it calls every other surface renderer rather than introducing new computation. This is a design inflection: the surface stack is now self-referential
- **Tech debt:** 20 feature PRs remain push-blocked on GH_GLOBAL secret (Pre-Run Cost Estimator through Curator Collections). Self-improve PR #43 is open and awaiting review
- **External contributors:** @teifurin's Neo4j security fix is the first merged external contribution

## What's Next

- PR #43 (bankr-prefetch agent-timeout) needs merge — will fix the tweet-allocator drift that's been running since May 18
- GH_GLOBAL secret remains the single highest-leverage unblock: 20 feature PRs worth ~25,000+ lines of code are staged locally
- MiroShark is now at 0 open PRs and 12 publish-gated surfaces — the distribution stack is feature-complete for the current roadmap
- Star pace cooling (4.86/day vs 6.0/day) suggests the organic discovery wave from the May 12–18 ATH run is normalizing — the next catalyst likely needs to be external (Show HN, conference mention, or integration partner)
- LP holding above $1M for the first time — a psychological threshold that was an active hyperstition target
