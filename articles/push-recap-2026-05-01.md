# Push Recap — 2026-05-01

## Overview
7 commits by @aaronjmars across aaronjmars/MiroShark in the last 24 hours. The dominant thrust: completing a full Chinese (zh-CN) internationalization stack that goes far deeper than UI strings — all the way down to simulation prompts, backend error messages, and documentation. A new belief trajectory export feature rounds out the day, giving analysts a quantitative data pipeline alongside the existing qualitative exports.

**Stats:** ~90 files changed, +8,055/-2,441 lines across 7 commits (miroshark-aeon had only automated cron/scheduler commits)

---

## aaronjmars/MiroShark

### Full Chinese (zh-CN) Internationalization — From UI to Simulation Core
**Summary:** Five PRs (#61–#65) and a screenshot commit build out a complete Chinese localization stack. What started as a UI string pass in PR #61 deepened into backend error localization (#62), README restructuring (#63, #64), and culminated in a full prompt registry system (#65) that translates simulation agent prompts themselves — making MiroShark genuinely usable in Chinese, not just skinned.

**Commits:**

- `0034053` — feat: Chinese (zh-CN) UI toggle + localized templates + bilingual README (#61)
  - New file `frontend/src/i18n.js`: Locale ref, `tr(en, zh)` helper function, global `$tr` plugin — the i18n backbone for the entire frontend (+54 lines)
  - New file `frontend/src/components/LocaleToggle.vue`: 中/EN toggle button wired into navbar, settings panel, and 6 other views (+63 lines)
  - Modified 30+ `.vue` files: ~1,300 user-visible strings wrapped in `$tr()` calls across every step of the simulation pipeline (Step1–Step5), history database, embed dialog, graph panel, demographic breakdown, interaction network, all view components
  - New file `backend/app/utils/i18n.py`: Server-side locale resolution (`?lang=` → `X-MiroShark-Locale` → `Accept-Language` → default), `get_locale()`, `apply_i18n()`, `t()` helpers (+122 lines)
  - Modified `backend/app/api/templates.py`: Template gallery serves localized names, categories, descriptions, and tags from embedded `i18n.zh-CN` blocks (+21/-15 lines)
  - Modified 6 preset templates (`campus_controversy`, `corporate_crisis`, `crypto_launch`, `historical_whatif`, `political_debate`, `product_announcement`): Each gained a full zh-CN translation block with localized scenario names, descriptions, tags, and counterfactual labels
  - Modified `README.md`: Added a complete Chinese section (quick-start, feature table, use cases, docs index) with top-of-page 中文/English anchor switcher (+129/-10 lines)
  - Modified `frontend/src/api/index.js`: API interceptor now sends `X-MiroShark-Locale` and `Accept-Language` headers on every request (+8/-1 lines)

- `2d9f823` — feat(i18n): localize backend errors + bilingual docs (#62)
  - Modified `backend/app/api/simulation.py`: 58 user-facing error messages now go through `_t(en, zh, locale)` — every validation failure, 404, 403, and 500 the user can hit is localized (+516/-143 lines)
  - Modified `backend/app/api/graph.py`: 15 error sites localized (+51/-24 lines)
  - Modified `backend/app/api/report.py`: 22 error sites localized (+56/-22 lines)
  - Modified `backend/app/services/feed.py`: `render_feed()` now accepts a `locale` kwarg — `/api/feed.atom?lang=zh-CN` serves Chinese channel title and description; `/verified` maps to "MiroShark · 已验证预言" (+35/-12 lines)
  - New files: 10 translated docs (`docs/*.zh-CN.md`) covering API, Architecture, CLI, Configuration, Features, Install, MCP, Models, Observability, Webhooks — totaling ~1,580 lines of translated documentation
  - Each English doc gained a one-line `English · 中文` language switcher under the H1; Chinese docs have the reverse
  - Cross-doc links inside the Chinese set rewritten to point at Chinese siblings for internal consistency
  - New file `CONTRIBUTING.zh-CN.md`: Translated contributor guide (+30 lines)

- `441ba54` — docs(readme): put English section above Chinese (#63)
  - Modified `README.md`: Mechanical reorder placing the English block before the Chinese block; top-of-page anchor switcher and deep links preserved (+110/-109 lines)

- `28e3123` — docs(readme): move License + Star History below the Chinese section (#64)
  - Modified `README.md`: License and star-history chart moved to the very bottom with a bilingual "License · 许可证" header so they aren't duplicated between language sections (+8/-12 lines)

- `4c2e470` — feat(i18n): Chinese-mode simulation prompts + experimental warning (#65)
  - New file `backend/app/prompts/registry.py`: Locale-aware prompt loader with English fallback, thread-safe caching, `get_prompt(key, locale, **kwargs)` API, `list_keys()` and `missing_keys()` for test coverage enforcement (+159 lines)
  - New directory `backend/app/prompts/locales/en/`: English prompt templates extracted from 8 service files — `graph_tools.py` (114 lines), `social_simulations.py` (171 lines), `simulation_config.py` (70 lines), `ontology.py` (79 lines), `ner_extractor.py` (41 lines), `web_enrichment.py` (26 lines), `profile_generator.py` (21 lines)
  - New directory `backend/app/prompts/locales/zh_CN/`: Full Chinese translations of all 8 prompt modules plus `report_agent.py` (330 lines) — the largest translation, covering the multi-section simulation report generator
  - Modified 8 service files (`graph_tools.py`, `ontology_generator.py`, `report_agent.py`, `simulation_config_generator.py`, `simulation_runner.py`, `web_enrichment.py`, `wonderwall_profile_generator.py`, `ner_extractor.py`): Hardcoded English prompts replaced with `get_prompt()` calls, reducing inline string bloat by ~370 lines
  - Modified `backend/app/utils/i18n.py`: Added `contextvars`-based `_active_locale`, `use_locale` context manager for thread propagation, `get_active_locale()` / `set_active_locale()` / `reset_active_locale()` (+54/-2 lines)
  - Modified `backend/wonderwall/simulations/social_media/prompts.py` and `polymarket/prompts.py`: Twitter/Reddit/Polymarket persona prompts now route through the registry (~210 lines of hardcoded prompts removed)
  - Modified 3 CLI scripts (`run_parallel_simulation.py`, `run_reddit_simulation.py`, `run_twitter_simulation.py`): Each now reads `MIROSHARK_LOCALE` env var and applies `use_locale()` at bootstrap (+31 lines total)
  - New file `frontend/src/components/ZhWarningBanner.vue`: One-time modal warning when a user first toggles to Chinese — explains that simulation prompts are experimental, structured output quality varies by LLM, and provides a dismiss button (+230 lines)
  - New file `backend/tests/test_unit_prompt_registry.py`: 90-line test suite covering locale loading, English fallback, missing key detection, zh-CN coverage gating (+90 lines)

- `11b647a` — docs(readme): add Chinese UI screenshot to zh-CN section
  - New file `docs/images/miroshark-cn.jpg`: Screenshot of the Chinese UI
  - Modified `README.md`: Image reference added to the 中文 section (+4 lines)

**Impact:** MiroShark is now fully usable in Chinese — not just translated strings on buttons, but localized error messages, localized documentation, and localized simulation agent prompts. The prompt registry architecture (`app/prompts/`) is extensible: adding a new language means dropping a folder under `locales/` and tests automatically enforce coverage. The `use_locale` context manager ensures locale propagates correctly through Flask requests, background threads, and subprocess simulation runners. This is a serious distribution play targeting the Chinese open-source AI community.

---

### Belief Trajectory CSV / JSONL Export — The Quantitative Export Surface
**Summary:** PR #66 adds the fifth share/export surface alongside share cards (PNG preview), replay GIFs (motion), transcripts (Markdown prose), and transcript JSON (SDK consumption). This one covers the quantitative layer: a row-per-round table with bullish/neutral/bearish percentages, agent counts, post/engagement metrics, and quality health — the format a researcher pastes directly into a Pandas notebook.

**Commits:**

- `3a31d77` — feat: belief trajectory CSV / JSONL export (#66)
  - New file `backend/app/services/trajectory_export.py`: Pure stdlib implementation (csv + io + json) with `compute_stance_split()` using the same ±0.2 threshold as every other surface, `build_rows()` assembler, `render_csv()` and `render_jsonl()` emitters. Locked CSV column order (`round`, `round_timestamp`, `bullish_pct`, `neutral_pct`, `bearish_pct`, `participating_agents`, `total_posts`, `total_engagements`, `quality_health`, `participation_rate`) so downstream consumers don't break (+297 lines)
  - Modified `backend/app/api/simulation.py`: `_serve_trajectory()` shared handler + two route decorators (`GET /api/simulation/<id>/trajectory.csv` and `trajectory.jsonl`), same publish gate as transcripts and share cards, 60s cache, content-disposition attachment header (+93 lines)
  - New file `backend/tests/test_unit_trajectory.py`: 17 offline unit tests covering stance-threshold parity, boundary bucketing, corrupt/empty trajectory degradation, chronological ordering, missing quality.json fallback, locked CSV header order, csv.DictReader round-trip, JSONL field ordering (+402 lines)
  - Modified `frontend/src/components/EmbedDialog.vue`: New "Export trajectory data" section with Download .csv / .jsonl buttons, copyable CSV URL, and a `pd.read_csv()` quickstart snippet (+92 lines)
  - Modified `frontend/src/api/simulation.js`: `getTrajectoryCsvUrl()` and `getTrajectoryJsonlUrl()` helpers (+35 lines)
  - Modified `backend/openapi.yaml`: Both endpoints documented under Publish & Embed with `SimulationTrajectoryRow` schema (+107 lines)
  - Modified `docs/API.md`, `docs/FEATURES.md`, `README.md`: Features row, dedicated section, analyst quickstart with `pandas.read_csv()` + DuckDB `read_json_auto()` snippets (+41 lines)

**Impact:** Researchers can now pull simulation belief trajectories directly into their analysis tools without intermediate conversion. The CSV format is designed for `pandas.read_csv()` one-liner consumption. JSONL supports stream-processing pipelines and DuckDB. Combined with the webhook and Atom feed from last week, MiroShark now has a complete data pipeline: trigger via API → get notified via webhook → pull quantitative data via CSV/JSONL → pull qualitative data via transcript.

---

## Developer Notes
- **New dependencies:** None — both features use pure stdlib (csv, io, json, contextvars, importlib)
- **Breaking changes:** None — all new endpoints, Chinese is opt-in, English output is byte-for-byte unchanged
- **Architecture shifts:** The prompt registry (`app/prompts/`) is the biggest structural addition — it centralizes ~20 prompt sites that were previously hardcoded across 8 service files into a locale-aware, cached, test-gated system. The `use_locale` context manager + `MIROSHARK_LOCALE` env var establish the locale propagation pattern for all future I/O
- **Tech debt:** None introduced. The prompt extraction actually reduces tech debt by removing ~370 lines of inline prompt strings from service files

## What's Next
- The i18n stack is complete from UI to simulation core — next likely step is community feedback on Chinese prompt quality across different LLMs (the ZhWarningBanner explicitly flags this as experimental)
- The trajectory export completes the five-surface export matrix — Statistical Batch Runs (repeatedly mentioned in repo-actions ideas) would be the natural consumer, comparing trajectory CSVs across replicate runs
- With 913+ stars and now genuine Chinese accessibility, the path to 1,000 stars is wide open — Chinese developer communities on GitHub are a major growth vector
- No incomplete work or open branches visible in the diffs
