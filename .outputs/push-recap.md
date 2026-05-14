*Push Recap — 2026-05-14*
47 commits across 2 repos by @aaronjmars + aeonframework

MiroShark Distribution Layer: Two PRs merged that extend reach — PR #81 adds 6 composable query-string filters (consensus, quality, outcome, q, sort, limit) to RSS/Atom feeds so operators and tools like Feedly/n8n can subscribe to precise slices ("bullish + excellent + trending"). PR #82 ships auto-generated /sitemap.xml and /robots.txt so Googlebot indexes every published simulation — submit once to Search Console and new sims become searchable on next crawl.

Skill Catalog Expansion: 29 new skills synced from upstream Aeon (#36, #37), bringing the catalog from ~55 to ~84 entries. Spans competitive intel, community analytics, content syndication, prediction markets, fork management. All disabled by default. Five launch-comms skills (star-milestone, star-momentum-alert, thread-formatter, operator-scorecard, ai-framework-watch) flipped on for the first time (#38).

Feature Skill Hardening: Two self-improvements — a pre-build grep step now checks if features already exist before building (#35, prevents ~60% redundant builds), and scratch verifier scripts cleaned up with .gitignore backstops (#34).

Key changes:
- /sitemap.xml: pure-stdlib XML sitemap with per-sim /share/ and /watch/ pages, 50K URL cap, changefreq by sim state (+1,197 lines, 20 unit tests)
- Filtered feeds: same gallery_filters parity on RSS/Atom, EmbedDialog filter-builder UI with live URL preview (+1,280 lines, 14+ unit tests)
- 29 skill SKILL.md files landed — largest single-day catalog expansion

Stats: ~60 files changed, +10,100/-200 lines
Full recap: https://github.com/AITOBIAS04/miroshark-aeon/blob/main/articles/push-recap-2026-05-14.md
