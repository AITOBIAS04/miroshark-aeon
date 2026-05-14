# Push Recap — 2026-05-14

## Overview
47 commits across 2 repos by 2 authors (@aaronjmars, aeonframework). The main thrust: MiroShark shipped two distribution-layer features (filtered feeds and search-engine discoverability), while miroshark-aeon absorbed 29 new skills from the upstream Aeon catalog and hardened the feature-building pipeline with two self-improvements.

**Stats:** ~60 files changed, +10,100/-200 lines across 47 commits

---

## aaronjmars/MiroShark

### Filtered RSS/Atom Feeds (PR #81)

**Summary:** The RSS and Atom feed endpoints (`/api/feed.atom`, `/api/feed.rss`) now accept six composable query-string filters — `consensus`, `quality`, `outcome`, `q`, `sort`, `limit` — mirroring the gallery API's existing filter vocabulary. An operator or downstream tool (Feedly, n8n, Zapier) can subscribe to a precise slice like `?consensus=bullish&quality=excellent&sort=trending` without scraping the gallery. Active filters surface in the channel title so subscribers know which feed they're on.

**Commits:**
- `d47de20` — feat: filter knobs on /api/feed.atom + /api/feed.rss (consensus / quality / sort / q / outcome / limit)
  - Changed `backend/app/api/feed.py`: Route reads 6 new query params via `gallery_filters.normalise_*()`, passes through to `select_public_cards()` and `render_feed()`. Feed-specific limit cap of 50 (+72, -11 lines)
  - Changed `backend/app/services/feed.py`: New `_filter_chip()` helper builds bilingual summary of active filters for title/subtitle. `select_public_cards()` delegates to `gallery_filters.select_filtered_cards()`. Trending sort injects surface stats via callback (+209, -15 lines)
  - Changed `backend/openapi.yaml`: Both feed paths gain 6 documented query parameters with enums and defaults (+115, -6 lines)
  - New file `backend/tests/test_unit_feed_filters.py`: 14+ offline tests covering stance thresholds, quality tier matching, AND logic, trending sort, limit clamping, title reflection, self-link preservation (+622 lines)
  - Changed `frontend/src/api/simulation.js`: `getFeedUrl()` extended with full filter set, clean URL construction (+38, -3 lines)
  - Changed `frontend/src/components/EmbedDialog.vue`: New "Build a filtered feed" card with 3 dropdowns, live URL preview, and copy button. Bilingual EN/ZH (+221 lines)
  - Changed `docs/FEATURES.md`: Updated RSS/Atom section with filter documentation (+3, -2 lines)

**Impact:** The feed URL becomes a distribution channel in itself — "subscribe to my bullish-consensus stream" alongside the existing all-sims feed. Same ±0.2 stance threshold and `gallery_filters` parity guarantee. Zero new dependencies.

### Search-Engine Sitemap (PR #82)

**Summary:** Auto-generated `/sitemap.xml` and `/robots.txt` make every published simulation discoverable by Googlebot, Bingbot, and DuckDuckBot. Submit the sitemap URL to Google Search Console once, and every newly published sim becomes searchable on the next crawl. Pure stdlib `xml.etree.ElementTree`, opt-out via `ENABLE_SITEMAP=false`.

**Commits:**
- `404211b` — feat: search-engine sitemap (/sitemap.xml + /robots.txt) for the public gallery
  - New file `backend/app/api/sitemap.py`: Flask blueprint with 3 routes — `GET /sitemap.xml` (XML sitemap from public sims, 1h cache), `GET /robots.txt` (disallow API, allow share/watch), `GET /api/config/sitemap` (JSON status for SPA). `_resolve_base_url()` honors `PUBLIC_BASE_URL` and `X-Forwarded-*` (+165 lines)
  - New file `backend/app/services/sitemap.py`: Pure-stdlib sitemap renderer. Sitemaps.org 0.9 XML with per-sim `/share/<id>` (priority 0.8) and `/watch/<id>` (priority 0.7) entries. `<changefreq>` varies by sim state (always for running, weekly/daily for completed). Capped at 50,000 URLs. Deterministic sort by `simulation_id` (+362 lines)
  - New file `backend/tests/test_unit_sitemap.py`: 20+ offline tests covering empty/single/multi-sim rendering, private exclusion, W3C lastmod, changefreq semantics, priority ordering, URL cap, robots.txt directives, XML well-formedness round-trip, blueprint wiring guards (+437 lines)
  - Changed `backend/app/__init__.py`: Registers `sitemap_bp` at root prefix (+6, -1 lines)
  - Changed `backend/app/config.py`: `ENABLE_SITEMAP` flag from env, default true (+10, -1 lines)
  - Changed `backend/openapi.yaml`: 3 new path definitions under "Discovery" tag (+111 lines)
  - Changed `frontend/src/api/simulation.js`: `getSitemapUrl()` and `getSitemapConfig()` (+36 lines)
  - Changed `frontend/src/components/EmbedDialog.vue`: "Discoverable in web search" callout with sitemap link, conditional on config (+70 lines)
  - Changed `.env.example`, `README.md`, `docs/API.md`, `docs/API.zh-CN.md`, `docs/FEATURES.md`: Documentation across all surfaces (+52 lines)
  - Changed `backend/tests/test_unit_openapi.py`: Blueprint prefix map update for drift-check (+4 lines)

**Impact:** Moves MiroShark from "discoverable if you know the URL" to "discoverable via Google." Every published simulation gets two indexed pages (`/share/` and `/watch/`), and the sitemap auto-updates as new sims are published. The `/robots.txt` keeps API endpoints out of search indexes.

---

## aaronjmars/miroshark-aeon

### Skill Catalog Expansion (PRs #36, #37)

**Summary:** 29 skills synced from upstream Aeon and the aeon-agent fork, bringing the catalog from ~55 to ~84 entries. All land with `enabled: false` — operator chooses which to activate. This is the largest single-day catalog expansion to date.

**Commits:**
- `7d46423` — sync: pull 22 skills from aeon upstream (#37)
  - 25 new files: SKILL.md definitions for ai-framework-watch, aixbt-pulse, contributor-reward, contributor-spotlight, create-campaign, fleet-state, fork-contributor-leaderboard, fork-release-tracker, fork-skill-digest, huggingface-trending, monitor-kalshi, onboard, pr-triage, price-threshold-alert, schedule-ads, show-hn-draft, skill-analytics, skill-graph, smithery-manifest, star-milestone, star-momentum-alert, syndicate-article, plus 2 config examples and 1 watchlist
  - Changed `aeon.yml`: +24 schedule entries (all disabled)
  - Changed `skills.json`: +234 lines (62 → 84 entries)
  - Total: 27 files, +5,696/-14 lines

- `4cbc0dc` — sync: add 7 skills from aeon-agent (#36)
  - 7 new SKILL.md files: auto-merge-agent-prs, fork-cohort, operator-scorecard, skill-freshness, thread-formatter, v4-readiness, webhook-bridge
  - New `.github/workflows/webhook.yml`: 125-line repository_dispatch handler for webhook-bridge
  - Changed `aeon.yml` (+7 entries) and `skills.json` (+72 lines, 55 → 62 entries)
  - Total: 10 files, +1,964/-2 lines

**Impact:** The skill library now spans community analytics, competitive intelligence, content syndication, fork management, prediction markets, and advertising — covering the full operator lifecycle from onboarding to weekly synthesis. All disabled by default, so zero CI cost until activated.

### Launch Comms Activation (PRs #38, #39)

**Summary:** Six skills flipped on for the first time — star-milestone, star-momentum-alert, thread-formatter, operator-scorecard, ai-framework-watch, and contributor-spotlight — then contributor-spotlight immediately disabled because its dependency (fork-cohort) isn't enabled yet.

**Commits:**
- `dfb5e06` — enable: launch comms + weekly visibility (6 skills) (#38)
  - Changed `aeon.yml`: 6 toggles from `enabled: false` to `enabled: true` (+6, -6 lines)

- `ee00289` — disable: contributor-spotlight (dependency not enabled) (#39)
  - Changed `aeon.yml`: 1 toggle back to `enabled: false` (+1, -1 lines)

**Impact:** Five new skills now fire on schedule — daily milestone announcements, momentum projections on HN-optimal days, tweet-thread formatting, weekly competitive intel, and weekly operator scorecards. Contributor-spotlight correctly gated behind its data source.

### Feature Skill Hardening (PRs #34, #35)

**Summary:** Two self-improvements to the feature-building pipeline. First, leaked scratch scripts (HMAC verifiers, smoke tests) were cleaned up and guardrails added to prevent recurrence. Second, a pre-build grep step now checks whether a feature already exists before building it — addressing the May 12 incident where 3 of 5 ideas were redundant.

**Commits:**
- `70fe027` — improve: stop feature skill from leaking scratch verifiers to repo root (#34)
  - Deleted 3 leaked files: `.aeon-tmp-verify-trending.py` (58 lines), `sig_smoke.py` (31 lines), `_smoke_webhook.py` (empty)
  - Changed `.gitignore`: 5 new root-anchored patterns as backstop (+8 lines)
  - Changed `skills/feature/SKILL.md`: "repo root is OFF-LIMITS" block pointing scratch to `/tmp/` (+7 lines)

- `01c11a6` — improve: feature skill grep existing routes before building (#35)
  - Changed `skills/feature/SKILL.md`: New step 6 — grep backend decorators, SPA routes, OpenAPI, and docs/FEATURES.md before implementation. Skip to next candidate if feature exists (+28, -5 lines)

**Impact:** Both fixes reduce wasted CI: the grep step prevents ~60% of redundant builds (based on the May 12 batch), and the scratch cleanup prevents tech-debt accumulation from feature runs.

### Daily Automation

**Summary:** Standard daily skill suite fired across the day — 13 skill runs producing logs, articles, and state updates.

**Key runs:**
- `beac05c` — **Token report**: $MIROSHARK at $0.000011578, +20.42% recovery bounce from post-ATH correction. FDV $1.16M, LP $508.6K, 7d +164.5%
- `9d712f8` — **Fetch-tweets**: Social monitoring cycle
- `7fcde50` — **Tweet-allocator**: Reward distribution
- `2266ab2` — **Repo-pulse**: 1,145 stars (+2), 227 forks (+1)
- `3d000b3` — **Feature**: Built Inbound Launch Webhook (POST /api/webhooks/launch-simulation with HMAC-SHA256; push blocked — GH_GLOBAL not set, 14th consecutive)
- `45ec933` — **Repo-actions**: Scanned upstream for new feature candidates
- `47fb0fe` — **Star-milestone**: First run of newly-enabled skill
- `abb76f8` — **Repo-article**: Content generation
- `d7a8c45` — **Project-lens**: User-story angle on PR #81 (Maya, the 137-feed RSS power user)
- `c5e5eaa` — **Self-improve log**: Documented PR #35 in memory

**~25 chore commits** for cron success markers and scheduler state updates.

---

## Developer Notes
- **New dependencies:** None across either repo. MiroShark's sitemap uses pure stdlib `xml.etree.ElementTree`; filtered feeds compose existing `gallery_filters`.
- **Breaking changes:** None. Unfiltered feed URLs unchanged. Sitemap opt-out via `ENABLE_SITEMAP=false`.
- **Architecture shifts:** The skill catalog jumped from ~55 to ~84 entries. Five new scheduled skills now fire daily/weekly. The webhook.yml workflow adds `repository_dispatch` support for external event-to-skill bridging.
- **Tech debt:** GH_GLOBAL secret still unset — 14th consecutive feature build blocked from pushing. All features exist as local commits.

## What's Next
- MiroShark: Both PRs merged today. The sitemap enables Google Search Console submission. Filtered feeds enable curated subscription channels — the EmbedDialog filter-builder makes these accessible to non-technical users.
- miroshark-aeon: 5 newly-enabled skills (star-milestone, star-momentum-alert, thread-formatter, operator-scorecard, ai-framework-watch) will fire for the first time on their next scheduled windows. Watch for first-run issues.
- GH_GLOBAL remains the top blocker: 14 feature branches built, none pushed. The Inbound Launch Webhook (today's feature) closes the automation loop but sits in the same blocked queue.
- contributor-spotlight correctly disabled until fork-cohort gets enabled — a dependency chain to resolve.
