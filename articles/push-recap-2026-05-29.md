# Push Recap — 2026-05-29

## Overview
7 commits by 2 authors across aaronjmars/MiroShark today, headlined by a full dark-space-violet frontend reskin that touches 36 Vue files — the entire app now lives in the MiroShark visual language instead of the legacy light Hyperstitions theme. Alongside the reskin, a new Belief Volatility analytics surface ships as the 25th share surface, and the backend gets serious production hardening with a fail-closed auth guard and a real WSGI server. No substantive changes in miroshark-aeon (automated cron housekeeping only).

**Stats:** ~60 files changed, +5,047/-3,489 lines across 6 unique commits (+ 1 merge commit)

---

## aaronjmars/MiroShark

### Full Dark-Space-Violet Frontend Reskin
**Summary:** The entire MiroShark frontend has been rewritten from the light orange/green Hyperstitions (Evangelion-inspired) theme into a deep-space purple visual language matching miroshark.xyz. This is not a CSS variable swap — it's a ground-up restyle of every view, component, and interactive surface across 36 Vue files, with new Geist/Geist Mono fonts alongside the existing Young Serif/Space Mono.

**Commits:**
- `5535432` — frontend: rewrite Home view in real MiroShark visual language (#122)
  - Changed `frontend/src/views/Home.vue` (+996/-1,237): From-scratch rebuild — deep-space radial-gradient body with twinkling stars, chrome-shimmer headline, floating shark hero, glossy violet console with the full file/Just Ask/URL/Trending/Scenario/Launch pipeline
  - Changed `frontend/src/App.vue` (+28/-18): Legacy `--color-*` CSS tokens remapped onto the MiroShark palette (orange → bright violet, green → soft violet, white → deep glossy-panel base, black → light foreground text); `--background` flipped to `#05030a` (deep space)
  - Changed `frontend/src/views/ExploreView.vue` (+106/-81): Navbar rewritten as sticky dark glassmorphic bar with nav-link pill family; all hard-coded `rgba(10,10,10,X)` text flipped to `rgba(244,241,255,X)` for readability on dark
  - Changed `frontend/src/components/SettingsPanel.vue` (+134/-107): Modal overlay → deep-space wash with backdrop-blur; glossy violet panel base with chrome "⚙ SETTINGS" label
  - Changed `frontend/src/components/Step3Simulation.vue` (+317/-235): Full reskin of action toolbar (glossy violet nav-pills), platform status tabs (glossy cards with hover lift + glow halo), timeline cards (per-platform accent rail), avatar placeholders, system logs
  - Changed `frontend/src/components/Step4Report.vue` (+310/-307): Brand-color swap across the report view
  - Changed `frontend/src/components/Step5Interaction.vue` (+185/-182): Interaction surfaces reskinned
  - Changed `frontend/src/components/EmbedDialog.vue` (+130/-116): Overlay → deep-space wash; dialog → glossy violet panel; title icon → violet metal pill
  - Changed `frontend/src/components/GraphPanel.vue` (+84/-99): Deep-space graph canvas with violet grid + glossy nav-pill tool buttons; orange/green corner stripes removed
  - Changed `frontend/src/components/HistoryDatabase.vue` (+152/-156): Project cards reskinned to glossy family; gradient overlay edges flipped from light to deep-space wash
  - Changed `frontend/src/components/TemplateGallery.vue` (+133/-76): Glossy violet panel wrap; cards with left accent rail; difficulty colours remapped (easy=violet, medium=amber, hard=fuchsia); reinstated on Home
  - Changed `frontend/src/components/TrendingTopics.vue` (+90/-47): Glossy violet wrap; chrome label dot; dark glossy cards with left violet accent rail
  - Changed `frontend/src/components/ScenarioSuggestions.vue` (+128/-71): Smart Setup reskinned — bull/bear/neutral cards keep semantic colour cues but remapped to the dark surface
  - Changed `frontend/src/components/LocaleToggle.vue` (+31/-19): EN/中 toggle reskinned to match glossy violet nav-pill
  - Changed `frontend/src/components/ZhWarningBanner.vue` (+101/-65): Chinese-mode warning dialog reskinned to glossy violet modal
  - Changed `frontend/src/views/MainView.vue` (+65/-37), `ReportView.vue` (+41/-19), `SimulationView.vue` (+41/-19), `SimulationRunView.vue` (+41/-19), `InteractionView.vue` (+42/-20), `ReplayView.vue` (+66/-58), `ComparisonView.vue` (+93/-55): Deep-space radial bg + glossy glassmorphic header + chrome-text MIROSHARK brand + nav-pill switch buttons
  - Fixed invisible header text — `.switch-btn.active` had dark-on-dark colours; rebuilt as glossy violet pill
  - Fixed `#0A0A0A` literal across 13 files — legacy "dark ink" was invisible on the new dark surface; flipped to `#f4f1ff` (light foreground)
  - Changed `frontend/index.html`: Added Geist + Geist Mono fonts alongside existing font stack
  - New file `frontend/public/shark.webp`: Floating shark hero asset

**Impact:** The app now has a cohesive, distinctive dark-space visual identity matching the miroshark.xyz brand. Every view — Home, Explore, the 5-step simulation flow, Report, Replay, Comparison, Embed, Settings — lives in the same glossy violet design system. The Evangelion/Hyperstitions legacy theme is fully retired. TemplateGallery and HistoryDatabase are reskinned and reinstated on Home, restoring the "quick start" and "your runs" surfaces.

---

### New Feature: Belief Volatility Analytics (25th Share Surface)
**Summary:** A new analytics endpoint that quantifies how contested the path to consensus was — the turbulence counterpart to signal.json (direction) and peak-round (when). A quant tool can now tell a high-volatility Bullish result (agents swung repeatedly before aligning) from a low-volatility one where consensus formed early and held.

**Commits:**
- `822c3db` — feat: belief-volatility analytics surface (/volatility) (#124)
  - New file `backend/app/services/volatility_service.py` (+206 lines): Pure-stdlib service (`json` + `os` + `math`). Computes mean, population std dev, and max of round-over-round `|Δbullish| + |Δneutral| + |Δbearish|` swings. Normalized 0-100 `volatility_index = min(std_dev × 5, 100)`. Trend classifier: `stable` (std dev < 3), `converging` (second-half calmer), `contested` (otherwise). Reuses `peak_round.load_trajectory_rounds` so numbers match existing surfaces exactly.
  - Changed `backend/app/api/simulation.py` (+84): `GET /<id>/volatility` endpoint with publish gate, pretty-printed JSON, 5-min cache, Content-Disposition, surface-stat increment
  - Changed `backend/app/services/surface_stats.py` (+1): Registered `volatility` in `SURFACE_KEYS`
  - Changed `backend/openapi.yaml` (+143): `/volatility` path + `VolatilityResponse` schema with 10 required fields
  - New file `backend/tests/test_unit_volatility.py` (+285 lines): 18 offline tests covering boundary cases (empty/single-round → None, two-round well defined), arithmetic (mean/max/std dev/max_delta_round = peak-round's most_volatile_round), index normalization, trend buckets, on-disk loading, and route/schema wiring guards
  - Changed `backend/tests/test_unit_surface_stats.py` (+1): Added `volatility` to the SURFACE_KEYS invariant set
  - Changed `frontend/src/api/simulation.js` (+49): `getVolatilityUrl()` and `getVolatility()` helpers with 403/404 → null contract
  - Changed `frontend/src/components/EmbedDialog.vue` (+219): 📈 Belief volatility section — live preview with volatility index gradient bar (green ≤33 / amber 34-66 / red ≥67), max swing + round, mean swing, std dev, trend chip, copyable URL + curl snippet. Loads on dialog open + publish-gate flip.
  - Changed `docs/API.md` (+1): `/volatility` row in the Analytics table with curl example
  - Changed `docs/FEATURES.md` (+35): Belief Volatility Score section with full schema example and field documentation

**Impact:** Completes the three-factor analytical view — `signal.json` for *direction*, `peak-round` for *when*, `volatility` for *how contested*. A downstream position-sizing model finally has the turbulence dimension it needs alongside direction and confidence. Zero new dependencies.

---

### Production Deployment Hardening
**Summary:** Two independent contributions hardening MiroShark for production deployment on Railway and Google Cloud Run — a security-critical auth guard fix and the switch from Flask dev server to gunicorn.

**Commits:**
- `375ef84` — fix: harden internal-auth guard + run production WSGI server (#125) — by Aaron Elijah Mars
  - Changed `backend/app/__init__.py` (+33/-8): Auth guard now fail-closes when managed-platform env vars (`RAILWAY_ENVIRONMENT`, `K_SERVICE`, etc.) are present, regardless of `FLASK_DEBUG`. Previously a deploy that forgot both the key and `FLASK_DEBUG=false` would serve `/api/*` openly because `FLASK_DEBUG` defaults to `"true"`. Also: `hmac.compare_digest` for constant-time key comparison; CORS preflight (OPTIONS) exempted from 401.
  - Changed `Dockerfile.railway` (+22/-3): Switched from `python backend/run.py` (Flask dev server) to gunicorn with `gthread` worker class (1 worker / 8 threads by default, tunable via env). Shell-form CMD with `exec` for clean SIGTERM handling.
  - Changed `backend/pyproject.toml` (+2): Added `gunicorn>=22.0.0` dependency
  - Changed `backend/uv.lock` (+15/-1): Locked gunicorn 26.0.0
  - Changed `backend/tests/test_unit_internal_auth.py` (+64/-17): Added `autouse` fixture to restore mutated global state; new regression test for fail-closed on deploy platform with DEBUG=true
  - Changed `railway.env.example` (+8/-5): Removed hardcoded `PORT=8080` (platform injects it); documented why `FLASK_DEBUG=false` is mandatory
  - New file `cloudrun.env.yaml.example` (+41): Template for Cloud Run env vars with inline security notes

- `36dab7e` — fix: use .venv/bin/python in CMD + add Cloud Run deploy infra — by DYAI2025
  - Changed `Dockerfile.railway` (+3/-3): Fixed `ModuleNotFoundError` by using explicit `.venv/bin/python` path instead of system python
  - New file `cloudbuild.yaml` (+18): Google Cloud Build config with Docker build step
  - New file `scripts/deploy_cloudrun.sh` (+39): One-command deploy script for Cloud Run (europe-west1 / bazodiac project)
  - Changed `.gitignore` (+1): Added `cloudrun.env.yaml` to prevent credential commits

**Impact:** The Flask dev server no longer runs in production. The auth guard now fail-closes even when `FLASK_DEBUG` is left at its default — a real security fix for any deployed instance. Google Cloud Run is now a first-class deploy target alongside Railway, with a build config and deploy script.

---

### API Documentation & Registry
**Summary:** Two documentation improvements — the locale negotiation protocol is now discoverable, and MiroShark's treasury wallets are declared for the x402books registry.

**Commits:**
- `3ce49e9` — docs: document the locale-negotiation protocol on the HTTP API surface (#123)
  - Changed `docs/API.md` (+21): New "Localization" section documenting the `?lang=` > `X-MiroShark-Locale` > `Accept-Language` > `en` precedence chain, supported locales (`en`, `zh-CN`), what gets localized, and curl examples for both header-driven and query-pinned patterns
  - Changed `docs/API.zh-CN.md` (+21): Mirrored section in Chinese

- `4a71e20` — Add .x402books/wallets.json to declare agent wallets (#126)
  - New file `.x402books/wallets.json` (+19): Declares MiroShark treasury (`0x7753...`) and deployer (`0x6cab...`) wallets on Base for x402books registry verification

**Impact:** SDK authors and third-party integrators can now discover and opt into localized API responses without reading the source. The x402books wallet declaration enables external registry verification of MiroShark's on-chain identity.

---

## aaronjmars/miroshark-aeon

No substantive code changes. ~20 automated commits: cron-state updates, skill auto-commits (repo-pulse, token-report, star-momentum-alert, feature, star-milestone, thread-formatter, heartbeat, push-recap). All routine housekeeping from the CI/CD scheduler.

---

## Developer Notes
- **New dependencies:** `gunicorn>=22.0.0` added to backend (production WSGI server)
- **Breaking changes:** None. The auth guard is stricter (fail-closed on platform deploys), but this fixes a security gap rather than changing the intended contract
- **Architecture shifts:** The frontend has fully transitioned from the light Hyperstitions (Evangelion) theme to the dark MiroShark space-violet design system. All CSS tokens are remapped — no dual-theme support remains
- **New fonts:** Geist + Geist Mono added to the font stack (Home and future views); Young Serif + Space Mono retained for backwards compatibility
- **New deploy target:** Google Cloud Run is now supported via `cloudbuild.yaml` + `scripts/deploy_cloudrun.sh`
- **Tech debt:** Two components' comments note that `TemplateGallery` and `HistoryDatabase` were previously hidden from Home due to theme clashes — now reskinned and reinstated. The legacy CSS token names (e.g. `--color-orange`) are kept but remapped to violet values, which could confuse a new contributor reading the variable names

## What's Next
- The dark theme cascade is complete across all views, but some edge-case sub-components (e.g. community-contributed components, modals deep in the flow) may still have light-theme holdovers that surface under specific sim states
- DYAI2025's Cloud Run deploy infra is in place but the service hasn't been deployed yet (no `cloudrun.env.yaml` committed, by design)
- The 25th share surface (volatility) closes the analytical quadrant — next analytical surface would likely be correlation/cross-agent metrics
- 25 feature PRs remain push-blocked locally pending the `GH_GLOBAL` secret
- Stars: 1,209 (+2). Forks: 257 (+0)
