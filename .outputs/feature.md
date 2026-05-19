*Feature Built — 2026-05-19*

Weekly Simulation Digest
MiroShark now has an auto-curated weekly highlights page. Every week, the digest surface scans all published simulations from the past 7 days, ranks them by a weighted engagement composite — views, shares, embeds, annotations, and coalition complexity — and surfaces the top 5 as a focused summary at /digest. Each featured simulation shows its scenario excerpt, consensus outcome, and the single most interesting metric from that run. Archive navigation lets visitors browse past weeks.

Why this matters:
The gallery at /explore now has over a thousand published simulations. The trending sort helps surface the most-distributed runs, but neither the chronological nor the trending view answers the simplest new-visitor question: "what happened on MiroShark this week?" The Weekly Digest is the editorial layer that fills this gap — five simulations in 60 seconds, pre-curated by engagement signal, no scrolling through the full corpus. For community members, it is a weekly pulse check. For new visitors arriving from search or social, it is a faster on-ramp than the full gallery.

What was built:
- backend/app/services/weekly_digest.py: Pure-stdlib digest service with ISO-week boundary filtering, weighted engagement scoring (watch_page × 3, share_card × 5, embed × 4, annotation × 2, coalition × 1), key-metric auto-selection from whichever signal is most extreme (consensus velocity, polarization gap, coalition count, annotation count, or agent count fallback), and atomic 6-hour on-disk cache per week
- backend/app/api/feed.py: Two new endpoints on the feed blueprint — GET /api/digest/weekly?week=YYYY-WNN returns the top 5 with engagement scores, GET /api/digest/archive returns every available digest week with sim counts for archive navigation
- frontend/src/views/DigestView.vue: Full digest page with ranked card list (orange rank badges, consensus split bars, key metric pills, engagement score chips), empty/loading/error states, archive grid for past weeks
- frontend/src/router/index.js: /digest (latest week) + /digest/week/:weekId (archive) routes
- frontend/src/views/ExploreView.vue: "Digest" navigation chip in the gallery header stats row for cross-discovery
- backend/tests/test_unit_weekly_digest.py: 18 offline unit tests covering engagement scoring formula, ISO-week boundary filtering, ranking and top-N, cache write/read/expiry, archive grouping, key metric selection, empty corpus, and edge cases
- backend/openapi.yaml: WeeklyDigestResponse, DigestSimulation, DigestKeyMetric, DigestArchiveResponse schemas under new "Digest" tag
- docs/FEATURES.md + README.md: Documentation section + features table row

How it works:
The digest endpoint scans all published simulations, filters them into the requested ISO-week window, then scores each simulation with a weighted engagement formula that prioritizes shares (×5) and embeds (×4) over raw page views (×3), with annotation and coalition counts as secondary signals. The top 5 by score form the digest. For each featured simulation, the service auto-selects the most interesting metric — whichever of consensus velocity, polarization gap, coalition count, or annotation count is highest. Results are cached on disk per-week with a 6-hour TTL so the page loads instantly for repeat visitors. The entire service is pure stdlib Python with atomic file writes — zero new dependencies, same posture as the prior 27 PRs.

What's next:
Curator Collections (named, ordered simulation lists for building arguments from curated selections) and Scenario Pre-flight Analyzer (heuristic feedback on scenario text before launching) are the remaining candidates from the May 16 repo-actions batch.

PR: push blocked — GH_GLOBAL secret not set (18th consecutive block since May 1). Code complete on feat/weekly-simulation-digest branch.
