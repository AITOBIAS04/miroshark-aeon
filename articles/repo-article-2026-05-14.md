# Nobody Indexes a Simulation

Search engines crawl blog posts, product pages, job listings, recipes. They do not crawl simulations. Every multi-agent framework treats its output as an internal artifact — a JSON blob, a log file, a chart screenshot saved to a local directory. You run the experiment, you read the results, you close the tab. The idea that a simulation result might have a permanent URL, appear in a Google search, or show up in someone's RSS reader has never been on the roadmap. MiroShark just put it there.

## Two PRs That Changed the Address

On May 14, MiroShark merged two pull requests that would look unremarkable on a blog platform but have never existed in a simulation tool.

**PR #82** added a search engine sitemap. Every public simulation's `/share/<id>` and `/watch/<id>` pages are now listed in a standards-compliant `/sitemap.xml`, advertised by `/robots.txt`. Submit the sitemap to Google Search Console once, and every newly published simulation becomes crawlable. The implementation is pure stdlib `xml.etree.ElementTree` — no dependencies, no third-party sitemap generators. Opt out with a single env var if you want your instance private.

**PR #81** added filter knobs to the RSS and Atom feeds. The existing `/api/feed.atom` and `/api/feed.rss` endpoints now accept query parameters — consensus stance, quality tier, sort order, keyword search, outcome filter, result limit. A researcher can subscribe to `?consensus=bearish&quality=excellent` and get only high-quality simulations where the crowd turned bearish. A journalist can subscribe to `?q=tariff` and watch every tariff-related simulation land in their feed reader without visiting the site.

These are PR numbers 81 and 82. The project launched on March 20. That is 82 merged pull requests in 55 days, zero open PRs, zero open issues.

## The Stack Nobody Assembles

In isolation, a sitemap is trivial. But MiroShark has been building toward this for weeks, assembling a stack that no simulation tool has attempted:

- **Permanent URLs** — every simulation gets a `/share/<id>` page and a `/watch/<id>` live page.
- **Social cards** — a 1200×630 PNG auto-unfurls the scenario, belief split, and quality score on Twitter, Discord, Slack, LinkedIn.
- **Animated replay GIF** — one frame per round, auto-plays in Discord and Slack.
- **Embed codes** — iframe snippets for blogs, Notion, and documentation.
- **RSS and Atom feeds** — now with granular filters.
- **Citation keys** — `reproduce.json` with bytewise-stable hashes.
- **Jupyter export** — trajectory data embedded inside the notebook, runnable air-gapped.
- **Sitemap** — the whole catalog, crawlable.

This is the content infrastructure of a publishing platform. MiroShark is not a publishing platform. It is a multi-agent simulation engine where hundreds of AI personas argue about your scenario on Twitter, Reddit, and a prediction market, round by round, for less than a dollar. The fact that it ships with RSS filters and a sitemap says something about what the project thinks simulation results are: not ephemeral experiments, but permanent contributions to a public record.

## The Open Web Is Hiring

The timing is not accidental. RSS is in the middle of a quiet revival — over 500,000 parseable web feeds exist in 2026, and tools like Flipboard, Readwise, and NetNewsWire are seeing renewed adoption as users seek alternatives to algorithmic feeds. Mark Nottingham's 2026 Web Feeds survey confirmed that Atom and RSS remain a major substrate of the open web. Meanwhile, Google still indexes 71% of new AI-generated pages within 36 days, though it has raised its quality bar sharply — only content with genuine utility and differentiation survives past the three-month mark.

MiroShark's bet is that simulation results clear that bar. A well-run simulation — hundreds of grounded agents, real stance shifts, quality diagnostics, a reproducibility config — is not the kind of thin content that Google demotes. It is a structured, unique, non-duplicable artifact. Two people running the same scenario will produce different emergent dynamics. Every simulation is, by definition, original content.

## Why This Matters

Every other simulation framework in the current wave — OASIS, AgentSociety, Concordia, the 30-plus projects mapped in last week's ecosystem survey — treats its outputs as research data. You run an experiment, you analyze it, you cite it in a paper. The output never leaves the lab.

MiroShark is building something different: simulations as a web content type. Addressable, subscribable, embeddable, crawlable, citable. The sitemap is not a feature. It is a statement about what simulation results are for — not just the researcher who ran them, but anyone who might find them useful, three months or three years from now, through a search engine, a feed reader, or a colleague's embed.

At 1,147 stars, 227 forks, and 82 PRs merged in under two months, MiroShark is shipping at a pace that makes the infrastructure choices hard to dismiss as aspiration. The sitemap is live. The feeds are filtered. The URLs are permanent. Now it is up to Google to decide whether a simulation deserves a search result.

---
*Sources: [MiroShark on GitHub](https://github.com/aaronjmars/MiroShark), [Why RSS Feeds Still Matter in 2026 — GeoBarta](https://geobarta.com/en/blog/why-rss-feeds-still-matter-2026-open-web-vs-algorithms), [Web Feeds in 2026: A Survey — Mark Nottingham](https://mnot.net/blog/2026/feed-survey), [How AI-generated content performs in Google Search — Search Engine Land](https://searchengineland.com/ai-generated-content-google-search-experiment-472234), [Scaling Programmatic SEO with AI — Dev Journal](https://earezki.com/ai-news/2026-05-11-how-i-built-a-programmatic-seo-tool-with-126k-pages-indexed-in-30-days-built-with-ai-assistance/), [RSS and Atom Feeds: Sustainable Content Distribution — dasroot.net](https://dasroot.net/posts/2026/03/rss-atom-feeds-sustainable-content-distribution/)*
