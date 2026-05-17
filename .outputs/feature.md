*Feature Built — 2026-05-17*

Private Share Links with Expiry
MiroShark simulations can now be shared privately — without publishing to the gallery. Operators generate a time-limited URL that lets a specific collaborator view the full simulation results (belief drift, agent network, quality report, everything) without the simulation appearing in the public gallery, sitemap, or RSS feed. Each link is a standalone bearer token: share it with one person, set an expiry (24 hours, 7 days, or never), and revoke it individually if shared in error.

Why this matters:
Until now, sharing a simulation was all-or-nothing: either it's gallery-indexed and discoverable by anyone, or it's completely invisible. No middle ground. A consultant running a scenario for a client, a researcher wanting peer review before publication, a team testing internally — all had to choose between full publicity or zero sharing. This was the #1 remaining gap identified in the May-14 repo-actions batch (noted explicitly as the 'Private Share Link — not yet built' item from the chart SVG PR). With 1,166 stars and growing institutional interest, the practitioner use case demands this.

What was built:
- backend/app/services/share_links.py: Pure-stdlib share link service — atomic JSON persistence, os.urandom token generation, hmac.compare_digest timing-safe validation, expiry management (24h/7d/never), revocation
- backend/app/api/simulation.py: Three admin-gated endpoints (POST/GET/DELETE share-links) + share_link_count on GET /<id> + share-token bypass helper for publish gates
- backend/app/api/share.py: GET /share/private/<token> landing route — scans sims or uses ?sim= hint, validates token, renders OG-tagged HTML with share_token SPA URL, increments private_share surface stat
- backend/app/services/surface_stats.py: Added private_share to SURFACE_KEYS
- frontend/src/components/EmbedDialog.vue: Full 'Private link' section — generate button with expiry dropdown, copyable URL, managed link list with masked tokens and revoke buttons
- frontend/src/api/simulation.js: createShareLink, getShareLinks, revokeShareLink API functions
- backend/tests/test_unit_share_links.py: 20 unit tests covering token generation, expiry, validation, revocation, atomic writes, corrupt file handling, timing safety
- backend/openapi.yaml: Three endpoints under new 'Private Sharing' tag
- docs/FEATURES.md + docs/FEATURES.zh-CN.md: Bilingual documentation

How it works:
POST /api/simulation/<id>/share-links creates a 32-character hex token (os.urandom) stored in <sim_dir>/share_links.json alongside its expiry timestamp. The /share/private/<token> route validates the token with hmac.compare_digest (timing-safe), then renders the same OG-tagged landing page the public share route uses — but with a share_token query parameter that the SPA passes to all subsequent API calls. Data endpoints check this parameter against share_links.json to bypass the is_public gate. Each private link access increments a private_share surface stat counter. The whole system is stdlib-only — no new dependencies, keeping the zero-new-deps streak at 24 PRs.

What's next:
Per-link access logging (who viewed, when) and rate limiting on private share link generation. Could also add a password-protected variant for extra-sensitive simulations.

PR: BLOCKED — GH_GLOBAL not set (16th consecutive block). Branch: feat/private-share-links (commit a078574)
