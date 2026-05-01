*Push Recap — 2026-05-01*
MiroShark — 7 commits by @aaronjmars

Chinese (zh-CN) Internationalization (PRs #61–#65): MiroShark now ships a complete Chinese localization stack — not just translated buttons, but localized simulation agent prompts, 138 backend error messages, 10 translated documentation files, and a prompt registry architecture that makes adding new languages a folder drop. The use_locale context manager propagates locale through Flask, threads, and subprocesses. A warning banner surfaces for first-time Chinese users explaining experimental prompt quality.

Belief Trajectory CSV / JSONL Export (PR #66): The fifth share/export surface — two new API endpoints serve per-round belief data (bullish/neutral/bearish %, agent counts, posts, engagements) as RFC 4180 CSV or newline-delimited JSON. Designed for pandas.read_csv() one-liner consumption. 17 unit tests, zero new dependencies.

Key changes:
- New prompt registry (app/prompts/) centralizes ~20 prompt sites into a locale-aware, cached, test-gated system — replaces 370 lines of hardcoded English strings across 8 service files
- trajectory_export.py uses the same ±0.2 stance threshold as every other surface — CSV numbers match what the gallery, share card, and webhook report
- contextvars-based locale propagation (use_locale) ensures Chinese mode works through async handlers, background threads, and simulation subprocesses

Stats: ~90 files changed, +8,055/-2,441 lines
Full recap: https://github.com/AITOBIAS04/miroshark-aeon/blob/main/articles/push-recap-2026-05-01.md
