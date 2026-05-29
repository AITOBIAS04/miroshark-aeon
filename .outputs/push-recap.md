*Push Recap — 2026-05-29*
MiroShark — 7 commits by 2 authors (@aaronjmars, DYAI2025)

Dark-Space-Violet Reskin: The entire frontend has been rewritten from the light Evangelion/Hyperstitions theme into the MiroShark visual language — deep-space radial gradients, glossy violet panels, chrome-shimmer accents across all 36 Vue files (+3,716/-3,452 lines). Every view from Home to Replay now lives in the same dark design system. TemplateGallery and HistoryDatabase reskinned and reinstated on Home.

Belief Volatility Analytics (25th Surface): New GET /volatility endpoint quantifies how contested the path to consensus was — mean/std-dev/max of round-over-round swings, a normalized 0-100 volatility index, and a stable/converging/contested trend label. Completes the three-factor analytical view alongside signal.json (direction) and peak-round (when). 18 unit tests, zero new deps.

Production Deployment Hardening: Auth guard now fail-closes on Railway/Cloud Run even when FLASK_DEBUG is left at its default (security fix — previously would serve /api/* openly). Switched from Flask dev server to gunicorn (1 worker, 8 threads). DYAI2025 contributed Cloud Run deploy infra (cloudbuild.yaml + deploy script). hmac.compare_digest for constant-time key comparison.

Key changes:
- PR #122: 36-file frontend reskin — every component from Home to Step3 to EmbedDialog rebuilt in glossy violet
- PR #124: volatility_service.py (206 LoC) + route + EmbedDialog section with gradient bar + 18 tests
- PR #125: Fail-closed auth guard + gunicorn — real security hardening for deployed instances
- PR #123: Locale negotiation protocol documented in API.md (en, zh-CN, precedence chain)
- PR #126: x402books wallet declaration for on-chain identity verification

Stats: ~60 files changed, +5,047/-3,489 lines
Stars: 1,209 (+2) · Forks: 257
Full recap: https://github.com/AITOBIAS04/CHORUS/blob/main/articles/push-recap-2026-05-29.md
