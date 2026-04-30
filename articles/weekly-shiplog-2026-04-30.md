# Week in Review: The Week MiroShark Became a Platform

*2026-04-30 — Weekly shipping update*

## The Big Picture

MiroShark stopped being a tool this week and started being a platform. Sixteen PRs merged in seven days — a public gallery, a full OpenAPI spec with Swagger UI, completion webhooks for Slack/Discord/Zapier, an MCP onboarding panel, shareable belief-replay GIFs, a verified predictions hall, and simulation transcript export. Every one of these features exists to let something *else* plug into MiroShark. The simulation engine itself barely changed; what changed is how the rest of the world can reach it.

## What Shipped

### The Integration Surface

The single biggest theme: connective tissue. PR #45 added a complete OpenAPI 3.1 specification with interactive Swagger UI at `/api/docs` — 2,600 lines that formally describe every endpoint MiroShark exposes. PR #46 followed with completion webhooks: point a Slack channel, a Discord bot, a Zapier zap, or any custom URL at MiroShark and it will POST a payload when a simulation finishes. PR #44 built an MCP onboarding panel in Settings — a guided walkthrough for connecting MiroShark to Claude and other MCP-compatible AI agents. Together, these three PRs turn MiroShark from something you run in a browser tab into something you wire into a stack.

### The Public Gallery and Verified Predictions

MiroShark simulations used to be private by default — run one, read the results, close the tab. PR #43 shipped `/explore`, a public simulation gallery where published simulations are browsable by anyone. PR #47 added the Predictive Accuracy Ledger: a `/verified` hall that tracks which simulations called their outcomes correctly, with accuracy scores computed against real-world resolution data. PR #49 locked down the publish/resolve/outcome endpoints behind admin-token auth so only authorized users can curate what appears in the gallery. The result is a credibility loop — run simulations, publish the good ones, resolve them against reality, and build a public track record.

### Shareable Artifacts

Two features this week made simulation results portable. PR #50 added animated belief-replay GIFs — a server-side endpoint that renders how agent beliefs shifted round by round into a looping GIF, with an Embed dialog for dropping it into blog posts, tweets, or Notion pages. PR #57 shipped simulation transcript export in both Markdown and JSON formats, turning the raw conversation between agents into a document you can share, search, or feed into another system. These aren't vanity features. They're distribution mechanisms — every GIF shared is a demo of what MiroShark does.

### Performance: 57% Token Reduction

PR #55 was the week's sleeper hit. The agent environment wire format — the context payload passed between simulation rounds — was redesigned to be ~57% smaller in input tokens. That translates directly to faster simulations and lower API costs per run. The compact format was validated end-to-end and the helpers were split into a stdlib-only module (PR #58) to keep CI clean.

## Fixes & Improvements

- **Langfuse observability:** Every OpenRouter call now tagged with Langfuse-grouping metadata (PR #51), and the broadcast pass-through was fixed to use the spec-compliant `trace` field (PR #54). Full request tracing is now production-ready.
- **Tool retry loop fix:** Stopped an infinite retry pattern in research tool calls and bounded context size to prevent runaway token usage (PR #52).
- **Templates UX overhaul:** Clickable history files, capped default simulation rounds, NoneType guards across the board (PR #53).
- **Observability pagination hardening:** Bad query string parameters no longer cause 500 errors — Flask `type=` coercion handles them cleanly (PR #56).
- **Wonderwall per-slot endpoint override:** Cloud preset refresh and per-slot LLM endpoint configuration (PR #59).
- **Aeon agent improvements:** Fetch-tweets dedup switched from URL to tweet ID matching (PR #23), bankr prefetch failure-mode diagnostics improved (PRs #24, #25), skill-leaderboard expanded to scan all watched repos (PR #26).

## By the Numbers

- **Commits:** 114 across 2 repos (16 MiroShark, 98 miroshark-aeon)
- **PRs merged:** 20 (16 MiroShark, 4 miroshark-aeon)
- **Files changed:** 115+ (MiroShark alone)
- **Lines:** +13,600 / -620 (MiroShark); miroshark-aeon primarily automated operations
- **Contributors:** aaronjmars, aeonframework
- **Stars:** 886 (+63 this week, +195 since Apr 15)
- **Forks:** 171

## Momentum Check

This was MiroShark's highest-velocity week by every metric. For comparison, the April 15 recap covered 20 commits and one major feature (browser push notifications). This week shipped 16 PRs — each a distinct, mergeable feature or hardening pass — in the same timeframe. The project has shifted from building simulation capabilities to building platform capabilities. That's a maturation signal: the core is stable enough that the focus can move to surfaces, integrations, and distribution.

The star trajectory confirms this. Crossing 800 stars (823 on Apr 25, 886 today) with 171 forks puts MiroShark well into the territory where external contributors and integrations start appearing organically. The OpenAPI spec and MCP panel are precisely the on-ramps that make that possible.

## What's Next

Based on open branches, recent repo-actions output, and the direction of this week's work:

- **Statistical Batch Runs** — run the same simulation N times and get aggregate confidence intervals. The infrastructure for this exists now that the agent env format is compact.
- **REST API + Webhook ecosystem** — the OpenAPI spec is published, expect client SDK generation and third-party integrations to follow.
- **Chain orchestration** — miroshark-aeon's chain-runner workflow is staged but no chains are defined yet. Combining research → simulation → article workflows is the obvious first chain.
- **Gallery curation** — with `/explore` and `/verified` live, the next step is editorial tooling: featured simulations, topic tags, search.

---

*Sources: [aaronjmars/MiroShark](https://github.com/aaronjmars/MiroShark), [aaronjmars/miroshark-aeon](https://github.com/aaronjmars/miroshark-aeon), [AgentOS MiroShark coverage](https://docs.agentos.sh/blog/2026/04/13/mars-genesis-vs-mirofish-multi-agent-simulation)*
