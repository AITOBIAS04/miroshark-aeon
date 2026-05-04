# Week in Review: MiroShark Crosses 1,000 Stars and Ships a Distribution Stack

*2026-05-04 — Weekly shipping update*

## The Big Picture

This was the week MiroShark stopped being a simulation engine and became a platform with a distribution strategy. Twenty PRs landed on MiroShark in seven days, building out a complete Chinese localization from UI to simulation prompts, seven distinct share surfaces for getting simulations in front of people, and a searchable gallery that turns the growing corpus of completed runs into a research tool. The 1,000-star milestone arrived on May 3 — not as a vanity number, but as a trailing indicator of a week where every commit pointed outward.

## What Shipped

### Full Chinese Localization — Not a Skin, a Stack

Five PRs (#61 through #65) delivered Chinese language support that goes deeper than any comparable open-source AI project. It started with UI strings — all 1,300+ user-visible labels across 30 Vue components wrapped in a `$tr()` system backed by localStorage and `X-MiroShark-Locale` headers. Then backend errors: 95 error sites across simulation, graph, report, and feed APIs, all routed through a locale resolver. Then documentation: 10 translated docs, a bilingual README with anchor switching, and a translated contributor guide.

But the real move was PR #65 — a locale-aware prompt registry that translates the simulation agent prompts themselves. MiroShark agents now think in Chinese when a Chinese-speaking researcher runs a simulation. The registry extracts ~370 lines of hardcoded prompts from 8 service files into `app/prompts/locales/`, cached and test-gated, with English fallback. A `use_locale` context manager propagates locale through Flask requests, background threads, and subprocess runners. An honest `ZhWarningBanner` warns users that prompt quality varies by LLM — a rare touch of epistemic humility in a space that usually ships "works perfectly" disclaimers.

This is a distribution bet. Chinese developers represent roughly 30% of the global AI open-source audience. MiroShark just became the first multi-agent simulation framework you can actually use in Chinese, end to end.

### Seven Share Surfaces — The Complete Distribution Stack

The week completed what amounts to a full media pipeline for simulation output. Each surface serves a different audience and consumption pattern, and they all draw from the same sim_dir folder using the same ±0.2 stance threshold:

1. **Share card PNG** — static preview for social embeds (shipped earlier)
2. **Replay GIF** (PR #50) — animated belief drift for visual social sharing
3. **Transcript export** (PR #57) — Markdown + JSON for readers and SDK consumers
4. **RSS/Atom feeds** (PR #60) — push-channel syndication for Feedly, Readwise, n8n, Zapier
5. **Trajectory CSV/JSONL** (PR #66) — quantitative data pipeline for pandas and DuckDB
6. **Live spectator watch page** (PR #67) — real-time broadcast with auto-updating belief bars, OG unfurling, SSR fallback, and graceful transition to final results
7. **Gallery with full-text search** (PR #69) — the corpus itself becomes navigable, filterable, and bookmarkable

The spectator watch page deserves special mention. It's a self-contained, server-rendered HTML page — no SPA dependency, no framework runtime, works behind strict CSP. Tweet a `/watch/<id>` URL mid-simulation and it unfurls as a 1200x630 card. The page polls every 15 seconds, backs off on failures, respects `prefers-reduced-motion`, and handles backgrounded tabs. When the sim finishes, CTAs appear for the full report and scenario forking. Zero new dependencies.

The gallery search (PR #69) transforms `/explore` from a reverse-chronological scroll into a queryable research corpus. Filter by consensus stance, quality tier, prediction outcome. Sort by date, rounds, or agent count. Every filter state lives in URL params — bookmarkable and shareable. Thirty-three unit tests cover threshold parity and filter composition.

### Performance and Infrastructure Hardening

Beneath the feature work, a layer of infrastructure improvements shipped quietly:

- **57% input-token compaction** (PR #55) — the agent environment wire format was rewritten to slash token consumption during the simulation loop's 850+ LLM calls per run
- **Langfuse observability** (PRs #51, #54) — every OpenRouter call now carries grouping metadata and the broadcast trace field is spec-compliant
- **Admin auth** (PR #49) — `/publish`, `/resolve`, and `/outcome` endpoints are now token-gated
- **Wonderwall endpoint override** (PR #59) — the simulation loop can now point at a self-hosted vLLM, Modal, or fine-tuned model independently of other slots, plus a simplified cloud-first `.env.example`

## Fixes & Improvements

- Stopped a tool retry loop that could burn tokens on repeated failures (PR #52)
- Templates UX polish: clickable history files, capped default rounds, NoneType guards (PR #53)
- Pagination integer coercion to prevent 500s from malformed query strings (PR #56)
- CI fix: split agent-env compaction helpers into a stdlib-only module for import compatibility (PR #58)
- Heartbeat day-of-week computation moved from LLM inference to shell — deterministic schedule classification (miroshark-aeon PR #27)
- Hyperstitions skill dedup backstop — catches content-without-header failure mode that caused silent duplicates (miroshark-aeon PR #28)
- Skill-leaderboard expanded to scan all watched repos, not just the first (miroshark-aeon PR #26)

## By the Numbers

- **Commits:** ~130 across 2 repos (20+ meaningful, rest automated skill cycle)
- **PRs merged:** 23 (20 on MiroShark, 3 on miroshark-aeon)
- **Files changed:** 234+ on MiroShark alone
- **Lines:** +17,558 / -3,065 on MiroShark
- **Stars:** ~886 → 1,062 (+176, crossed 1K on May 3)
- **Forks:** ~187 → 211 (+24)
- **Contributors:** @aaronjmars, @aeonframework (autonomous agent)
- **New dependencies added:** Zero (entire week is pure stdlib + existing stack)

## Momentum Check

This is the heaviest shipping week since MiroShark's launch sprint in late March. Twenty PRs merged on MiroShark alone — the previous high was the "platform week" (Apr 16–30) which shipped 27 PRs over two weeks. The difference this time is focus: every major PR points at distribution rather than core simulation mechanics. The i18n stack, the seven share surfaces, the searchable gallery — these are all plays to get simulation output in front of more people in more contexts. The zero-new-dependencies streak now spans 8+ consecutive PRs, which signals architectural maturity: the existing stack is flexible enough to absorb major features without new build complexity.

The 1K milestone arrived naturally, averaging ~25 stars per day through the week. Forks are growing proportionally (211, up from 187), though fork activation remains low — only 1 of 211 forks has a readable `aeon.yml`, a gap that the "5 active forks by June 30" hyperstition question is designed to probe. MiroShark is listed on [Trendshift](https://trendshift.io/repositories/24822), and the project continues generating social proof through Aaron's active Twitter presence.

## What's Next

Three features are code-complete but blocked on a missing `GH_GLOBAL` secret: Pre-Run Cost Estimator, Jupyter Notebook Export, and Community Template Gallery. Once that secret is set, 3 PRs and ~3,000 lines of tested code land immediately.

The Chinese localization opens the door to Chinese developer platform distribution — Juejin, CSDN, SegmentFault, OSChina. Whether MiroShark gets featured on one of these by June 15 is an open hyperstition question.

With seven share surfaces complete, the next likely direction is longitudinal: simulation series, statistical batch runs, and fork/counterfactual diff views from the May 2 repo-actions ideation. The distribution stack is built; now the question is what kind of research it enables at scale.

---
*Sources: [aaronjmars/MiroShark](https://github.com/aaronjmars/MiroShark), [aaronjmars/miroshark-aeon](https://github.com/aaronjmars/miroshark-aeon), [Trendshift](https://trendshift.io/repositories/24822)*
