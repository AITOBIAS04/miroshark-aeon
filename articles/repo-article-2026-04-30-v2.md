# 906 Stars and a New Language: MiroShark's Quiet Bet on Distribution

Most open-source AI projects die the same way: they ship impressive features, collect stars, and plateau when the people who would actually use them never find out they exist. MiroShark appears to be building against that failure mode — and the last 48 hours show how.

## What Just Happened

Two pull requests landed on April 30 that don't look like headline features but may matter more than anything shipped this month.

**PR #61 added full Chinese localization.** Not a machine-translated README addendum — a proper i18n layer spanning 1,300 user-visible strings across 30 Vue components, a backend locale resolver that negotiates via query parameter, custom header, and Accept-Language, and all six preset simulation templates carrying embedded `zh-CN` blocks that swap gallery cards on the fly. A toggle in the navbar lets users flip between English and Chinese, persisted in localStorage. The bilingual README now opens with a complete Chinese quick-start guide, feature table, and documentation index.

**PR #60 added RSS and Atom feeds.** Every newly published simulation now surfaces in `/api/feed.atom` and `/api/feed.rss` — valid syndication feeds that Feedly, Readwise, Inoreader, NetNewsWire, Obsidian RSS, n8n, and Zapier can subscribe to without authentication. Media thumbnails (share-card PNGs and belief-replay GIFs) are embedded as enclosures. A `?verified=1` parameter filters to predictions that were resolved against real outcomes. The frontend added auto-discovery tags and a Subscribe chip in the gallery.

Neither feature changes what MiroShark *does*. Both change who finds it and how.

## Why Chinese, Why Now

The timing is not accidental. Chinese open-source AI models now account for roughly 30% of the global working AI market, according to MIT Technology Review. GLM-5, Qwen 3.5, and DeepSeek-V3 are setting benchmarks. The Chinese-speaking developer community is the fastest-growing segment of the open-source AI ecosystem, and MiroShark already supports these models natively through OpenRouter — it ships a "Cheap" preset built on Qwen, DeepSeek, and Grok.

Adding Chinese localization isn't just a UX nicety. It removes the friction that keeps the largest non-English developer population from evaluating the tool. MiroShark's simulation engine is language-agnostic — agents already post in whatever language the LLM produces — but the *interface* was English-only until today. That mismatch is now fixed.

## The Distribution Stack

Zoom out and the pattern becomes clear. Over the past two weeks, MiroShark assembled what amounts to a complete distribution infrastructure:

- **Discovery**: Public gallery at `/explore`, verified predictions at `/verified`, RSS/Atom feeds for passive subscription
- **Shareability**: Open Graph share cards, animated belief-replay GIFs, iframe embeds, transcript exports in Markdown and JSON
- **Integration**: OpenAPI 3.1 spec with Swagger UI, completion webhooks for Slack/Discord/Zapier/n8n, MCP integration for Claude Desktop and Cursor
- **Accessibility**: Chinese localization covering the full UI and template library

Each layer solves a different distribution problem. The gallery lets browsers stumble onto simulations. RSS lets curators subscribe without checking back. Share cards make simulations unfurl natively on Twitter, Discord, and LinkedIn. Webhooks let automation pipelines react to completed runs. MCP lets AI tools invoke simulations programmatically. And now Chinese localization removes the language barrier for the world's largest open-source AI community.

## 906 Stars, 177 Forks, Zero Open Issues

The numbers as of today: 906 GitHub stars (up from 691 six weeks ago — a 31% increase), 177 forks, zero open issues, zero open PRs. The project has merged 61 pull requests since launch on March 20, averaging more than one per day for 41 days straight.

The 1,000-star mark is within reach. At the current pace of roughly 15 stars per day, it lands sometime in the first week of May. Whether that happens depends less on the next feature and more on whether the distribution infrastructure just shipped actually works — whether Chinese developers find the localized README, whether RSS subscribers share what surfaces in their readers, whether embedded share cards convert impressions into clicks.

## What It Means

There is a version of MiroShark that stays a niche simulation tool used by the people who already know about it. And there is a version that becomes the default way to stress-test a narrative before it hits the real world — the way people simulate PR crises, policy reactions, market moves, and historical counterfactuals.

The difference between those two outcomes is not the simulation engine. The engine is already good. The difference is distribution. And that is exactly what MiroShark just built.

---
*Sources: [MiroShark GitHub](https://github.com/aaronjmars/MiroShark), [What's Next for Chinese Open-Source AI — MIT Technology Review](https://www.technologyreview.com/2026/02/12/1132811/whats-next-for-chinese-open-source-ai/), [RSS and Atom Feeds: Sustainable Content Distribution](https://dasroot.net/posts/2026/03/rss-atom-feeds-sustainable-content-distribution/), [Supercharging AI Agents with RSS, Atom & JSON Feeds](https://medium.com/@richardwooding/supercharging-ai-agents-with-rss-atom-json-feeds-a-developers-guide-to-feed-mcp-7da545669f96), [@aaronjmars on X](https://x.com/aaronjmars/status/2045134558186664267)*
