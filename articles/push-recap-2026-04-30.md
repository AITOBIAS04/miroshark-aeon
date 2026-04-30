# Push Recap — 2026-04-30

## Overview
6 meaningful commits across 2 repos by 2 authors (@aaronjmars, @aeonframework), plus ~28 automated cron/scheduler commits on miroshark-aeon. Today's headline is a complete Chinese (zh-CN) localization of the MiroShark UI touching all 30 Vue components and 1,300+ strings — making the simulation platform accessible to the largest non-English developer audience. Alongside that, RSS/Atom syndication feeds turned the public simulation gallery into a push channel, the Wonderwall simulation slot gained per-endpoint overrides for BYO inference, and the Aeon heartbeat hardened against weekday hallucination.

**Stats:** ~79 files changed, +4,048/-1,758 lines across 6 meaningful commits

---

## aaronjmars/MiroShark

### Internationalization: Chinese (zh-CN) Locale (PR #61)
**Summary:** A full opt-in Chinese locale has been added to the SPA and backend. English remains the default. Users flip via a 中/EN toggle button in the navbar (also accessible in SettingsPanel). The choice persists in localStorage and is forwarded to the backend on every API call via `X-MiroShark-Locale` and `Accept-Language` headers.

**Commits:**
- `0034053` — feat: Chinese (zh-CN) UI toggle + localized templates + bilingual README (#61)
  - New file `backend/app/utils/i18n.py`: 122-line locale helper — `get_locale(request)` resolves locale from `?lang=` > `X-MiroShark-Locale` header > `Accept-Language` > default. `apply_i18n(payload, locale)` recursively merges embedded `i18n.zh-CN` blocks into JSON responses at read time. `t(en, zh, locale)` for inline translations. (+122 lines)
  - New file `frontend/src/i18n.js`: Vue i18n system — reactive `locale` ref backed by localStorage, `tr(en, zh)` helper, `useI18n()` composable, `i18nPlugin` providing global `$tr` / `$isZh` / `$setLocale` / `$toggleLocale`. (+54 lines)
  - New file `frontend/src/components/LocaleToggle.vue`: Navbar toggle button with active state styling, aria labels, and bidirectional label swap (shows target locale, not current). Themed with MiroShark orange accent. (+63 lines)
  - Modified `frontend/src/api/index.js`: API interceptor now sends `X-MiroShark-Locale` and `Accept-Language` headers on every request (+8, -1 lines)
  - Modified 30 `.vue` files: ~1,300 user-visible strings wrapped with `$tr()` calls — from Step1 through Step5 pipeline headers, HistoryDatabase, SettingsPanel, EmbedDialog, ExploreView, InfluenceLeaderboard, GraphPanel, NetworkPanel, PolymarketChart, and all report/interaction views. Aggregate: +1,563, -1,260 lines
  - Modified 6 preset template JSON files (`campus_controversy`, `corporate_crisis`, `crypto_launch`, `historical_whatif`, `political_debate`, `product_announcement`): Each now carries an embedded `i18n.zh-CN` block with translated name, category, description, tags, and counterfactual labels. Gallery cards swap on the fly. (+96 total lines)
  - Modified `backend/app/api/templates.py`: `/api/templates/list` and `/<id>` now apply locale via `apply_i18n()` and `get_locale()`; error messages localized (+21, -15 lines)
  - Modified `README.md`: Bilingual structure — 中文 section at top right after badges with full quick-start, feature table, use cases, docs index, and license. English section follows under `## English` with top-of-page anchor links `English · 中文`. (+129, -10 lines)
  - Modified `frontend/src/main.js`: Registered `i18nPlugin` globally (+2 lines)

**Impact:** MiroShark is now accessible to Chinese-speaking users and researchers — a significant audience in the crypto/DeFi/AI simulation space. The i18n architecture (embedded `i18n` blocks in JSON, recursive merge on read) means adding a third locale later requires zero schema changes. Tier 3 (agent system prompts and report-writer prompts) remains English — simulation content language is unchanged.

**44 files changed, +2,047/-1,482 lines**

---

### Discovery & Distribution: RSS/Atom Feeds (PR #60)
**Summary:** Two syndication feeds — `/api/feed.atom` (Atom 1.0) and `/api/feed.rss` (RSS 2.0) — now serve the same cards the public gallery shows. Researchers using Feedly, Readwise, Inoreader, NetNewsWire, or Obsidian RSS can subscribe in their existing toolchain. Every newly published simulation lands in their reader without anyone curating it. Pure stdlib — zero new dependencies.

**Commits:**
- `91e22e4` — feat: RSS / Atom feeds for the public simulation gallery (#60)
  - New file `backend/app/services/feed.py`: 584-line Atom 1.0 + RSS 2.0 renderer using stdlib `xml.etree.ElementTree` + `html`. Includes share-card PNG and replay GIF as `<media:thumbnail>` / `<media:content>` / `<enclosure>`. Outcome and quality categories. Stance threshold matching (±0.2) consistent with every other surface. Scenario truncated to 100 chars. (+584 lines)
  - New file `backend/app/api/feed.py`: `feed_bp` blueprint at `/api` with `?verified=1` filter, `Cache-Control: public, max-age=300`, `PUBLIC_BASE_URL` / `X-Forwarded-Proto-Host` honored, fail-soft against SimulationManager errors. (+144 lines)
  - New file `backend/tests/test_unit_feed.py`: 17 offline unit tests covering Atom validity, RSS validity, share-link + media enclosures, summary stance split, scenario truncation, outcome+quality categorization, empty-feed handling, missing optional fields, self-link query string preservation, skips bad sims, RSS guid stability, RSS enclosure, dispatcher MIME, verified-only branch, selection helper filter+sort+limit+graceful-degradation. (+566 lines)
  - Modified `backend/app/__init__.py` + `backend/app/api/__init__.py`: Blueprint registration (+8, -1 lines)
  - Modified `frontend/index.html`: `<link rel="alternate" type="application/atom+xml">` for browser auto-discovery (address-bar globe icon). (+5 lines)
  - Modified `frontend/src/views/ExploreView.vue`: "Subscribe via RSS" chip in the header that mirrors the active filter (verified-only when toggled on). (+37 lines)
  - Modified `frontend/src/components/EmbedDialog.vue`: "Follow the gallery via RSS" callout with one-click Atom / RSS / Verified-only buttons. (+150 lines)
  - Modified `frontend/src/api/simulation.js`: `getFeedUrl({format, verified})` helper. (+25 lines)
  - Modified `backend/openapi.yaml`: Both endpoints documented under Publish & Embed. (+64 lines)
  - Modified `backend/tests/test_unit_openapi.py`: `feed_bp` registered with `/api` prefix so drift-detection test passes. (+1 line)
  - Modified `README.md` + `docs/FEATURES.md`: Feature row + full Public Gallery Feeds section. (+20 lines)

**Impact:** Closes the discovery loop opened by `/explore` gallery (PR #43), share cards (PR #42), replay GIF (PR #50), and transcript export (PR #57). Converts the pull-based gallery into a push channel for the research and DeFi-tooling audience. Same on-disk sim folder now has four orthogonal share surfaces: preview (PNG), motion (GIF), text (transcript), and syndication (RSS/Atom). Qualifies MiroShark for RSS directory listings and Zapier/n8n integrations.

**13 files changed, +1,604/-1 lines**

---

### Infrastructure Flexibility: Wonderwall Endpoint Override + Cloud Preset Refresh (PR #59)
**Summary:** The Wonderwall simulation slot can now target any OpenAI-compatible endpoint independently of the Default/Smart/NER slots via `WONDERWALL_BASE_URL` and `WONDERWALL_API_KEY`. The cloud preset has been refreshed to Mimo V2 Flash + Grok-4.1 Fast, and the "Best" preset was dropped entirely.

**Commits:**
- `2e782e0` — feat(wonderwall): per-slot endpoint override + cloud preset refresh (#59)
  - Modified `.env.example`: Complete restructure — cloud-first default (Mimo V2 Flash for Default+Wonderwall, Grok-4.1 Fast for Smart+NER+web search) with active slot blocks and API key placeholders. Local Ollama and Claude Code modes moved to a commented "Alternatives" block. Best preset removed. (+91, -136 lines)
  - Modified `backend/app/config.py`: New `WONDERWALL_API_KEY` and `WONDERWALL_BASE_URL` config fields. Default model updated from `qwen3.5-flash` to `mimo-v2-flash`. Smart model comment updated to `grok-4.1-fast`. (+11, -7 lines)
  - Modified `backend/app/services/simulation_runner.py`: Forwards runtime `Config.WONDERWALL_*` values into subprocess env at spawn time, so Settings UI updates apply on next run without Flask restart. (+10 lines)
  - Modified `backend/scripts/run_parallel_simulation.py`, `run_twitter_simulation.py`, `run_reddit_simulation.py`: Each subprocess reads `WONDERWALL_BASE_URL`/`WONDERWALL_API_KEY` at startup and prefers them over `LLM_*` equivalents. (+26, -18 lines total)
  - Modified `frontend/src/components/SettingsPanel.vue`: Wonderwall section gains Base URL and API Key input fields alongside Model Name. Password-type input with masked display of saved keys. Preset logic simplified — removed `best` references. (+31, -7 lines)
  - Modified `backend/app/api/settings.py`: POST accepts `wonderwall.base_url` and `wonderwall.api_key`. GET exposes them with key masking. Removed `best` preset. (+14, -27 lines)
  - Modified docs: `README.md`, `INSTALL.md`, `MODELS.md`, `CONFIGURATION.md`, `FEATURES.md` — all updated for single Cloud preset, per-slot override, and new model lineup.

**Impact:** Users can now point the 850+-call Wonderwall simulation loop at a self-hosted vLLM, Modal, fine-tuned model, or Ollama on a different host without affecting any other slot. The preset simplification (one instead of two) reduces setup friction. The .env.example restructure makes cloud the default experience for new installations.

**16 files changed, +267/-266 lines**

---

## aaronjmars/miroshark-aeon

### Agent Self-Repair: Heartbeat Day-of-Week Accuracy (PR #27)
**Summary:** The heartbeat skill was occasionally hallucinating the wrong weekday from the `${today}` date string, causing misclassification of scheduled vs. off-schedule skill runs. On Apr 29, the report labeled the day as "Tuesday" (it was Wednesday), which hid `memory-flush`'s on-schedule run as "off-schedule." The fix adds a deterministic Step 0 that computes the day-of-week from the shell.

**Commits:**
- `f5ff617` — improve(heartbeat): compute day-of-week from shell, not inference (#27)
  - Modified `skills/heartbeat/SKILL.md`: New Step 0 section — runs `date -u +%A` / `+%u` / `+%d` and uses shell output as the source of truth for every "is this skill scheduled today?" comparison. Adds explicit cron weekday translation note (`0=Sun` in cron vs. `7=Sun` in `date +%u`). Adds ground-truth guidance for every-other-day cron expressions (check `last_dispatch` history instead of guessing parity). (+20 lines)
  - Modified `.outputs/self-improve.md`: Updated output artifact with improvement description. (+7, -8 lines)
  - Modified `memory/MEMORY.md`: Skills Built table updated with the fix entry. (+1, -1 lines)
  - New file `dashboard/outputs/self-improve-2026-04-30T13-42-01Z.json`: json-render dashboard spec for the improvement. (+91 lines)
  - Modified `memory/logs/2026-04-30.md`: Detailed log entry with trigger, fix, PR link. (+10 lines)

**Impact:** Heartbeat report headers are now deterministic instead of inferred. "Scheduled today / not scheduled today" classifications stop drifting silently. A real day-bound outage (e.g., memory-flush failing to fire on its Wednesday schedule) would now surface correctly instead of being hidden behind a hallucinated weekday.

**6 files changed, +130/-9 lines**

---

## Developer Notes
- **New dependencies:** None across all PRs. RSS/Atom uses stdlib `xml.etree.ElementTree`. i18n is hand-rolled (no i18next/vue-i18n).
- **Breaking changes:** `.env.example` restructured in PR #59 — defaults are now cloud (OpenRouter) instead of local Ollama. Existing `.env` files are unaffected. The "best" preset has been removed from the Settings API.
- **Architecture shifts:** The i18n system (PR #61) introduces embedded `i18n` blocks in JSON payloads, merged recursively on read — a lightweight alternative to full gettext/i18next that scales to additional locales without schema changes. The feed system (PR #60) reuses `_build_gallery_card_payload` with zero new infrastructure.
- **Tech debt:** None introduced. PR #59 cleaned up `.env.example` by consolidating two presets into one.

## What's Next
- The Chinese locale (PR #61) explicitly scopes out Tier 3 — agent system prompts and report-writer prompts remain English. A follow-up could localize simulation output for Chinese-speaking research audiences.
- RSS/Atom feeds pair naturally with the webhook system (PR #46) and n8n/Zapier integration templates (repo-actions idea from today).
- The Wonderwall endpoint override (PR #59) unblocks fine-tuned model experiments — the simulation loop can now point at a domain-specific fine-tune while keeping reports on a general-purpose model.
- 28 automated cron commits confirm all Aeon skills are back online after the 15-day auth outage (ISS-001). First full day of successful operations since Apr 15.
