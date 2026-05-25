*Push Recap — 2026-05-25*
MiroShark — 3 commits by 2 authors | miroshark-aeon — ~47 commits (cron cycle)

oEmbed Auto-Unfurl (PR #107): Share links now auto-unfurl into rich preview cards on Notion, Ghost, Substack, and WordPress. These writing platforms read oEmbed discovery tags, not Open Graph — so every organic citation was degrading to a bare URL. Pure-stdlib provider (oembed_service.py) parses sim IDs from share/embed/simulation URLs with host allow-listing, builds a type:rich payload with the existing share-card thumbnail + /embed iframe. 21st surface key. 18 tests.

Platform Stats API + Badge (PR #105): The first endpoints describing MiroShark itself, not individual sims. GET /api/stats collapses every public, completed sim into one envelope — total count, consensus distribution, avg confidence, surface views, unique projects, newest sim. GET /api/stats/badge.svg renders a Shields.io pill (platform-blue #0ea5e9) for any README. ETag/304 support, 60s cache, 27 tests. Zero new deps (32-PR streak).

gitignore Cleanup (PR #104): Void Freud collapsed the explicit .env profile list into .env.* wildcard — one line absorbs future profiles.

miroshark-aeon: bankr-prefetch EXIT trap (PR #45) stamps crashed status so tweet-allocator can diagnose silent prefetch failures. ai-framework-watch flagged RELEASE WEEK — pydantic-ai shipped V2 beta (b1/b2/b3) alongside stable v1.102; langgraph 1.2.1; crewai 1.14.5; mastra core 1.35.0. Aeon +76 stars (+20.8%) leads cohort by % growth.

Key changes:
- /oembed endpoint (root-mounted, oEmbed 1.0) — Notion/Ghost/Substack/WordPress auto-unfurl
- /api/stats + /api/stats/badge.svg — platform-level aggregate + Shields.io pill
- prefetch-bankr.sh EXIT trap — crash vs never-ran disambiguation

Stats: ~30 files changed, +2,390/-8 lines (MiroShark); ~47 cron commits (miroshark-aeon)
Repo: 1,195 stars (+1), 248 forks (+1)
Full recap: https://github.com/AITOBIAS04/CHORUS/blob/main/articles/push-recap-2026-05-25.md
