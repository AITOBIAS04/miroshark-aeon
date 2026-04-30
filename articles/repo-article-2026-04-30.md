# The Two-Week Sprint That Turned MiroShark Into a Platform

Somewhere between PR #31 and PR #59, MiroShark stopped being a simulation engine and became infrastructure.

Two weeks ago, the project was a compelling demo: drop in a document, watch AI agents argue about it on simulated social media, read the report. It already had 691 stars, a knowledge graph, belief drift charts, and trace interviews. But it was still a closed loop — you ran a simulation, you looked at the results, you moved on.

Since April 15, Aaron Mars and contributors have merged 27 pull requests and shipped roughly 67 commits. The result is a project that other tools can now build on top of.

## What Shipped

The most consequential additions aren't individual features — they're integration surfaces.

**A real API.** PR #45 added a full OpenAPI 3.1 spec with interactive Swagger UI at `/api/docs`. Every endpoint is documented, grouped by concern, and machine-readable. PR #46 followed with completion webhooks — point Slack, Discord, Zapier, n8n, or any custom endpoint at MiroShark and get a JSON payload the moment a simulation finishes. This isn't "we have an endpoint." This is "your automation pipeline can treat MiroShark as a service."

**MCP integration.** PR #44 added an AI Integration panel in Settings with auto-generated connection snippets for Claude Desktop, Cursor, Windsurf, and Continue. MiroShark now speaks Model Context Protocol natively, which means any MCP-compatible AI tool can invoke simulation runs, query results, and pull reports without writing a single line of glue code. This lands at exactly the moment MCP is becoming the industry standard for agent-to-tool communication.

**A public gallery.** PR #43 created `/explore` — a card grid of every published simulation, showing share cards, consensus splits, and quality health badges. PR #47 added `/verified`, a hall of predictions that were resolved against real-world outcomes with accuracy tracking. Together, they transform MiroShark from a private tool into a public record.

**Embeddable everything.** PR #34 shipped an iframe-embeddable simulation widget. PR #42 added Open Graph share cards — 1200x630 images that auto-unfurl on Twitter, Discord, Slack, and LinkedIn. PR #50 went further: animated belief-replay GIFs that show stance distributions shifting round by round, auto-playing in Discord and Slack. Simulations are now shareable artifacts, not just local outputs.

**Transcript export.** PR #57 added full per-round agent transcripts in both Markdown (with YAML front matter for Notion, Obsidian, and Substack) and structured JSON for SDK and LLM-as-judge pipelines. The simulation data is no longer locked inside MiroShark's UI.

## The Simulation Engine Got Sharper Too

While the integration layer was going up, the engine itself gained significant new capabilities. Director Mode (PR #31) lets you inject breaking news mid-simulation without forking — agents incorporate it in the next round. The "What If?" counterfactual explorer (PR #37) lets you fork a timeline and ask individual agents how they'd react to alternate scenarios. Trending topics auto-discovery (PR #40) solves the blank-page problem by surfacing live news items for one-click simulation seeding.

A deep codebase cleanup — circular dependency fixes, DRY consolidation, type strengthening, dead code removal — accompanied the feature push. Performance work included compacting the agent environment wire format (PR #55) to cut cross-round token bloat, and parallelizing report generation for a 5x speedup (PR #36, contributed by community member Muhammad Bin Sohail — one of the project's first external PRs).

## 886 Stars and Counting

The numbers tell the adoption story: 886 stars (up 28% from 691 two weeks ago), 171 forks (up 32% from 130). Zero open issues. Zero open PRs — everything merged, nothing stalled.

The growth coincides with a broader industry shift. 2026 is the year multi-agent systems moved from research demos to production infrastructure. Gartner, Salesmate, and MachineLearningMastery all identify multi-agent orchestration and API-first agent architecture as top trends. MiroShark is positioning itself at the intersection: not just a framework for building agents, but a simulation platform that other agent systems can query.

## Why This Matters

Most AI simulation projects follow a predictable arc: impressive demo, growing feature list, eventual plateau when the novelty fades. What happened to MiroShark in the last two weeks is different. The project didn't just add features — it added the surfaces that let other systems treat it as a dependency. An OpenAPI spec. Webhooks. MCP. Embeds. Exports. A public gallery with verified outcomes.

The gap between "tool" and "platform" is integration infrastructure. MiroShark just crossed it.

---
*Sources: [MiroShark GitHub](https://github.com/aaronjmars/MiroShark), [AgentOS comparison](https://docs.agentos.sh/blog/2026/04/13/mars-genesis-vs-mirofish-multi-agent-simulation), [Agentic AI Trends 2026](https://machinelearningmastery.com/7-agentic-ai-trends-to-watch-in-2026/), [Multi-Agent Frameworks 2026](https://www.adopt.ai/blog/multi-agent-frameworks), [@aaronjmars on X](https://x.com/aaronjmars/status/2045134558186664267)*
