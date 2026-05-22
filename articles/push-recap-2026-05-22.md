# Push Recap — 2026-05-22

## Overview

3 significant commits across 2 repos by 2 authors (@aaronjmars, aeonframework). The main thrust: MiroShark's academic citation arc is now complete — a single `GET /cite.bib` call produces a BibTeX entry that drops into LaTeX, Zotero, and Mendeley with reproduce.json verification and on-chain provenance baked in. Meanwhile, the Aeon infrastructure got a prefetch bug fix and ran a full 13-skill daily cycle without issues.

**Stats:** ~13 files changed, +1,286/-2 lines across 3 significant commits (+ ~39 cron bookkeeping commits on miroshark-aeon)

---

## aaronjmars/MiroShark

### Academic Citation Arc: BibTeX Export (PR #96)
**Summary:** The final layer in MiroShark's four-part citation chain. `reproduce.json` (PR #79) carries the parameters, `notebook.ipynb` (PR #80) provides the analysis surface, the OriginTrail DKG citation (PR #84) anchors provenance on-chain, and now `cite.bib` adds the academic reference layer — a one-call BibTeX `@misc{…}` entry that a researcher can paste into a LaTeX bibliography, import via Zotero/Mendeley "Import from URL," or verify against the on-chain hash years later.

**Commits:**
- `4394d51` — feat: BibTeX academic citation export — close the citation arc (#96)
  - New file `backend/app/services/bibtex_service.py` (+338 lines): Pure-stdlib BibTeX builder with citation-key sanitization (BibTeX grammar-safe `[A-Za-z0-9_-]` only), seven-special-character escaping (`& % $ # _ ^ ~ { } \`), ISO-8601 date parsing with fallback, SHA-256 source precedence (DKG on-chain anchor > fresh hash > omit), OriginTrail UAL in `annote` field, bytewise-deterministic rendering across calls
  - Changed `backend/app/api/simulation.py` (+136 lines): `GET /<id>/cite.bib` route. `text/plain; charset=utf-8` for Zotero URL importer compatibility. `Content-Disposition: inline; filename="miroshark-<id12>.bib"` so `curl -OJ` saves a ready-to-include file. 5-minute cache matching the reproduce.json cadence. Same publish gate as all share surfaces. Reproduce.json bytes sourced through `repro_export.render_json_bytes` for byte-identical hashing
  - New file `backend/tests/test_unit_bibtex_service.py` (+466 lines): 27 offline unit tests covering 11 property groups — citation key shape, BibTeX escaping, year/month derivation, SHA-256 source precedence (DKG > fresh > omit), annote UAL handling, URL composition, author defaults, bytewise determinism, route/MIME wiring, surface_stats registration, defensive fallbacks
  - Changed `backend/openapi.yaml` (+94 lines): Full endpoint spec under Publish & Embed tag, `cite_bib` added to SurfaceStats enum with semantic description (tracks academic adoption — spike = paper draft citing the sim)
  - Changed `frontend/src/components/EmbedDialog.vue` (+118 lines): BibTeX citation section between notebook and DKG panels. Copyable cite.bib URL, curl snippet, deterministic `\cite{miroshark-...}` LaTeX reference, Download .bib button. Bilingual (EN/ZH)
  - Changed `frontend/src/api/simulation.js` (+26 lines): `getCiteBibUrl` helper
  - Changed `docs/FEATURES.md` (+32 lines): Full BibTeX Academic Citation section with example entry, field documentation, Zotero/Mendeley import workflow
  - Changed `docs/API.md` (+1 line): Routes table entry
  - Changed `backend/app/services/surface_stats.py` (+1 line): `cite_bib` added to SURFACE_KEYS
  - Changed `backend/tests/test_unit_surface_stats.py` (+1 line): Expected-set updated

**Impact:** MiroShark simulations are now citable in academic papers with a single URL. The citation carries cryptographic verification (SHA-256 of the reproduce.json blob, sourced from the on-chain DKG anchor when available) and imports cleanly into both major reference managers. This is the 14th publish-gated share surface and closes the gap identified in the 2026-05-20 repo-actions ideas batch. Turns "MiroShark is a research tool" from positioning into a verifiable citation chain.

---

## aaronjmars/miroshark-aeon

### Bankr Prefetch Hardening (PR #44)
**Summary:** Bug fix for wasted Bankr Agent Max-Mode calls caused by X.com reserved paths leaking into the handle candidate list.

**Commits:**
- `e662f9c` — improve: filter X.com reserved paths from Bankr lookup candidates (#44)
  - Changed `scripts/prefetch-bankr.sh` (+14, -2 lines): XAI annotation citations surface as `x.com/i/status/<id>` URLs (3-4/day in fetch-tweets output), so `i` was leaking in as a handle candidate. Each false positive consumed one Bankr Agent Max-Mode call (~16-112s polling budget) on a non-existent account. Added a `RESERVED_X_PATHS` exclusion list covering `i` plus the broader X.com URL surface (`home`, `explore`, `compose`, `intent`, `messages`, `settings`, `search`, `hashtag`, etc.) so non-handle paths never reach Bankr
  - Identified and fixed by self-improve skill; merged by @aaronjmars

**Impact:** Eliminates wasted Bankr API calls (1 per prefetch run) and prevents future X.com URL path fragments from polluting the handle lookup pipeline.

### Daily Skill Cycle & Token Report
**Summary:** Full 13-skill daily cycle completed successfully. Token report captured the ongoing post-ATH correction.

**Commits:**
- `3069798` — feat(token-report): $MIROSHARK daily report 2026-05-22
  - New file `articles/token-report-2026-05-22.md` (+45 lines): Price $0.00002141 (-23.85% 24h), FDV $2.14M, LP $809.5K, volume $318.3K (lowest since pre-breakout). Post-ATH correction at -50.9% from $0.0000436 ATH. Social sentiment still bullish — @GodCandleGroup alpha call (62L/9RT), @0xChenez conviction hold, @ChinaDegen Base ecosystem visibility
  - Updated `memory/logs/2026-05-22.md` (+14 lines): Full token data logged

- ~39 cron bookkeeping commits: token-report, fetch-tweets, tweet-allocator, star-momentum-alert, feature (Prediction-Market Calibration build), self-improve (PR #44), repo-actions, push-recap, star-milestone, project-lens, repo-article, heartbeat, thread-formatter — all scheduler state updates + auto-commits

**Impact:** All scheduled skills firing cleanly. The self-improve cycle detected the Bankr prefetch waste and shipped a fix (PR #44) within the same day.

---

## Developer Notes
- **New dependencies:** None — 30-PR zero-new-deps streak continues on MiroShark (now at PR #96)
- **Breaking changes:** None
- **Architecture shifts:** The BibTeX service completes MiroShark's citation quad: reproduce.json (parameters) → notebook.ipynb (analysis) → DKG citation (provenance) → cite.bib (academic reference). All four are pure-stdlib, bytewise-deterministic, and publish-gated
- **Tech debt:** None introduced. The Bankr filter fix (PR #44) actually reduces operational waste

## What's Next
- MiroShark now has 14 publish-gated share surfaces and 5 notification channels — the feature pipeline continues with candidates from today's repo-actions (MCP Tool Server, Simulation Tag System, Cross-Simulation Archetype Leaderboard, Discussion Threads, Recurring Simulation Series)
- Prediction-Market Calibration (built today on miroshark-aeon, push blocked) is the 22nd feature waiting on GH_GLOBAL secret to push to MiroShark
- Token in post-ATH correction territory ($0.00002141, -50.9% from ATH) — volume at 4-week low but LP holding at $809.5K
- 1,190 stars, 243 forks
