*Push Recap — 2026-04-30*
MiroShark — 3 commits by @aaronjmars | miroshark-aeon — 1 commit by @aeonframework

Chinese (zh-CN) Localization (PR #61): Full opt-in Chinese locale across the entire SPA — 1,300+ strings wrapped in 30 Vue components, backend locale resolution via X-MiroShark-Locale header, 6 preset templates with embedded zh-CN blocks, bilingual README. A 中/EN toggle in the navbar persists in localStorage. Makes MiroShark accessible to the largest non-English developer audience.

RSS/Atom Syndication Feeds (PR #60): /api/feed.atom and /api/feed.rss serve the public gallery as standard syndication feeds with share-card PNG and replay GIF as media enclosures. Subscribe in Feedly, Readwise, Obsidian, or any RSS reader. 17 offline unit tests, zero new dependencies (stdlib XML). Converts the pull-based gallery into a push channel.

Wonderwall Endpoint Override (PR #59): WONDERWALL_BASE_URL + WONDERWALL_API_KEY let operators route the 850+ agent-action calls to a self-hosted vLLM/Modal/fine-tune without touching other model slots. Cloud preset refreshed to Mimo V2 Flash + Grok-4.1 Fast (~$1/run). Best preset dropped.

Heartbeat Day-of-Week Fix (PR #27): Shell-computed weekday replaces LLM-inferred value after Apr 29 hallucinated "Tuesday" for a Wednesday. Schedule checks now deterministic.

Key changes:
- 44 files touched for i18n — recursive apply_i18n() merges embedded locale blocks at read time
- 584-line Atom/RSS renderer with stance threshold matching consistent across all share surfaces
- .env.example restructured: cloud-first default, Ollama moved to commented alternatives

Stats: ~79 files changed, +4,048/-1,758 lines
Full recap: https://github.com/AITOBIAS04/miroshark-aeon/blob/main/articles/push-recap-2026-04-30.md
