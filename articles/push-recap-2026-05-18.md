# Push Recap — 2026-05-18

## Overview

54 commits by 2 authors (@aaronjmars, aeonframework) across 2 repos. The main thrust: MiroShark merged two feature PRs completing the embeddable-visual arc (chart SVG) and the four-channel notification quadrant (SMTP email), while two new PRs landed — including the first external security contribution and a Farcaster Frame v2 for Warpcast distribution. On the aeon side, a full Sunday reporting cycle fired: weekly shiplog, operator scorecard, AI framework watch (cold start), and 5 new feature ideas.

**Stats:** ~80 files changed, +3,400/-35 lines across 54 commits

---

## aaronjmars/MiroShark

### Merged Features: Chart SVG + SMTP Email (Closing Two Arcs)

**Summary:** Two merged PRs close two independent capability arcs. PR #85 adds a pure-stdlib SVG renderer for belief trajectory charts — the last missing visual format, making every simulation embeddable as a plain `<img>` tag on any platform without JavaScript. PR #87 adds SMTP completion-email notifications, the 4th and final notification channel, completing the webhook → Discord → Slack → email quadrant. Both follow the zero-new-dependency pattern — the 24-PR streak is now at 25.

**Commits:**

- `0e5b84d` — feat: trajectory chart SVG — stdlib-rendered belief curves for `<img>` embeds (#85)
  - New file `backend/app/services/chart_svg.py` (+442 lines): Pure-stdlib SVG renderer using `xml.etree.ElementTree`. Renders bullish (#22c55e), neutral (#6b7280), bearish (#ef4444) polylines on an 800x400 viewBox with 5-line y-axis grid, round-number x-axis labels, three-swatch legend, and scenario title. Bytewise-deterministic output suitable as a cache key. Reuses `trajectory_export.build_rows` so trajectory schema changes flow through both surfaces.
  - Changed `backend/app/api/simulation.py` (+78 lines): New `GET /api/simulation/<id>/chart.svg` route handler. Publish-gated identically to trajectory CSV. Returns `image/svg+xml` with `Cache-Control: public, max-age=300` (5-min, matching watch-page poll cadence). Increments `chart_svg` surface stat. Returns 404 when trajectory is empty (mid-startup sims) so embedding sites can render their own placeholder.
  - New file `backend/tests/test_unit_chart_svg.py` (+384 lines): 17 offline unit tests covering viewBox lock, polyline count, stance-color preservation, y-axis inversion, 404-on-empty, malformed-input resilience, title truncation, single-round renders, deterministic byte output.
  - Changed `frontend/src/components/EmbedDialog.vue` (+103 lines): New "Trajectory chart (SVG)" section with lazy-loaded `<img>` preview, Download .svg anchor, copyable chart URL, and paste-ready `<img>` embed snippet. Bilingual (EN/ZH).
  - Changed `frontend/src/api/simulation.js` (+20 lines): `getChartSvgUrl()` helper function.
  - Changed `backend/app/services/surface_stats.py`, `backend/openapi.yaml`, `docs/FEATURES.md`, `docs/FEATURES.zh-CN.md`, `docs/API.md`, `docs/API.zh-CN.md`, `README.md`, `backend/tests/test_unit_surface_stats.py`: Surface stat registration, OpenAPI schema, bilingual docs, feature table entry.
  - **Total:** +1,099/-4 lines across 13 files

- `1d5ccad` — feat: SMTP completion-email notifications (4th channel — zero platform dependency) (#87)
  - New file `backend/app/services/email_notify.py` (+796 lines): Full SMTP notification service. `multipart/alternative` body — plain text with Unicode block bars (matching Slack format) + HTML with inline-CSS swatches matching Discord embed colors and a consensus-colored "View simulation" CTA. Auth-optional: blank `SMTP_USER`/`SMTP_PASSWORD` routes through unauthenticated relay (localhost:25, self-hosted Postfix). When credentials ARE set and STARTTLS is refused, the dispatcher refuses to send rather than leak the password in cleartext. Daemon-thread dispatch with per-process `(sim_id, status)` dedup. Subject line format: `[MiroShark] Bullish: <scenario>`.
  - Changed `backend/app/services/simulation_runner.py` (+33 lines): Fire-and-forget email dispatch path wired alongside existing Discord/Slack/webhook dispatchers.
  - Changed `backend/app/api/notifications.py` (+8/-5 lines): Updated notifications config endpoint to expose `email_configured` boolean. Docstring updated from "three channels" to "four channels". Added `email_notify` import.
  - New file `backend/tests/test_unit_email_notify.py` (+572 lines): Comprehensive unit tests for the email service.
  - Changed `backend/tests/test_unit_notifications_config.py` (+64/-1 lines): Extended notification config tests for email channel.
  - Changed `.env.example` (+24 lines): SMTP configuration variables (`SMTP_HOST`, `SMTP_PORT`, `SMTP_FROM`, `SMTP_TO`, `SMTP_USER`, `SMTP_PASSWORD`).
  - Changed `docs/NOTIFICATIONS.md` (+113/-16 lines): Full SMTP setup documentation with relay and authenticated configurations.
  - Changed `frontend/src/components/EmbedDialog.vue` (+17/-3 lines): Email channel status chip in notification config display.
  - Changed `docs/FEATURES.md`, `docs/FEATURES.zh-CN.md`, `backend/openapi.yaml`, `README.md`: Feature table, bilingual docs, OpenAPI schema.
  - **Total:** +1,661/-29 lines across 12 files

**Impact:** Chart SVG closes the last embeddable-visual gap — a reader on Notion, Substack, Ghost, LinkedIn, a GitHub README, or a LaTeX paper now sees the full belief journey with no JavaScript and no resolution choice. SMTP email means every operator can receive sim-completion summaries in their inbox with zero platform dependency — no Discord account, no Slack workspace, just a mailbox. The notification quadrant (webhook + Discord + Slack + email) is now complete.

### New PRs Opened: Farcaster Frame + Security Fix

**Summary:** Two new PRs opened today — one by @aaronjmars expanding distribution to Warpcast, one by external contributor @teifurin fixing a hardcoded database password.

- **PR #90** — feat: Farcaster Frame v2 — interactive belief-chart cards in Warpcast (by @aaronjmars, opened 2026-05-18)
  - First Farcaster-native distribution surface. Uses the chart SVG from PR #85 as the Frame image. Interactive belief-chart cards visible directly in Warpcast feeds. Extends MiroShark's reach beyond web/embed into the Farcaster social protocol.

- **PR #89** — security: require explicit NEO4J_PASSWORD, remove hardcoded default (by @teifurin, opened 2026-05-18)
  - First external security contribution. Removes a hardcoded Neo4j password default, requiring explicit configuration. Small but meaningful security hardening from a community member.

**Impact:** PR #90 represents MiroShark's first hop into a decentralized social protocol — simulations become native content in Warpcast feeds rather than external links. PR #89 is notable as the first external contributor security fix.

---

## aaronjmars/miroshark-aeon

### Self-Improvement: Skill Accuracy Fixes

**Summary:** Two merged PRs and one opened PR fix false positives and factual errors in aeon's monitoring and content skills.

**Commits:**

- `8e44147` — improve: skill-freshness handles every-N-day cron cadence (#41) — by @aaronjmars
  - Changed `skills/skill-freshness/SKILL.md` (+4/-2 lines): Added `every_Nd` cadence bucket for cron expressions with `*/N` day-of-month patterns. `*/2` now gets a 52h threshold instead of the 28h daily threshold. Fixes false `FRESHNESS_WARN` alerts firing every odd day on `repo-actions` and `self-improve` (which run on `*/2` cadence). Extended `MISSING`-eligible cadence set to include `every_Nd`.

- `6f0e7d6` — improve: project-lens must verify PR status before notify (#40) — by @aaronjmars
  - Changed `skills/project-lens/SKILL.md` (+3 lines): Added PR status verification guardrail — skill must now run `gh pr view --json state,mergedAt` before referencing any PR by number. Notification PR-status verbs must match article body word-for-word. Fixes the May 15 incident where the notification said "merged" while the article correctly said "opened."

- **PR #42** (opened today) — improve: have repo-pulse write `articles/repo-pulse-YYYY-MM-DD.md`
  - Addresses a gap where repo-pulse logged to memory but never wrote article files, breaking operator-scorecard's ability to source star/fork data from articles.

**Impact:** Eliminates two recurring false-alarm patterns (freshness warns on every-other-day skills, PR status verb mismatches in notifications) and fixes a data sourcing gap in the operator scorecard pipeline.

### Weekly Reporting Cycle (Sunday)

**Summary:** Full Sunday reporting battery fired: weekly shiplog, operator scorecard, AI framework watch (first run), skill leaderboard, and repo-actions idea generation. These are all aeonframework automated skill runs producing articles and state updates.

**Commits:**

- `28d420f` — weekly-shiplog: "Four Channels, One Citation Chain, First Hop Off-Host"
  - New file `articles/weekly-shiplog-2026-05-18.md` (+68 lines): Covers May 12-18. Nine MiroShark PRs merged (#79-#87), notification quadrant complete, DKG citation chain, first operational hotfix (#86), $MIROSHARK +447% week through four consecutive ATH sessions, FDV $3.32M.

- `e2acbc4` — feat(operator-scorecard): weekly scorecard 2026-05-18 — OK
  - New file `articles/operator-scorecard-2026-05-18.md` (+41 lines): All three lanes green. Agent health: 6/7 heartbeats clean. Community growth: +42 stars, +12 forks. Economic activity: $69.99 $AEON to 20 recipients, token +447% 7d, FDV $3.32M (crossed both $2M and $3M milestones within the window). Volume $1.18M/day at close vs $52.6K seven days prior.
  - New file `dashboard/outputs/operator-scorecard.json` (+44 lines): Dashboard render spec.

- `82e625f` — feat(ai-framework-watch): cold start — RELEASE WEEK, 6 frameworks, 16 releases
  - New file `articles/ai-framework-watch-2026-05-18.md` (+81 lines): First run of the framework watch skill. Tracked 9 frameworks: langgraph 1.2.0 (durable error-handler), pydantic-ai 1.97.0 (GoogleProvider split, MCPToolset), mastra 1.34.0 (ACP coding agents, xAI voice), crewAI 1.14.5 alpha, llamaindex 0.14.22, smolagents 1.25.0. All deltas baseline this run.
  - New file `memory/topics/framework-watch-state.json` (+133 lines): Persistent state for delta tracking.

- `62016de` — feat(skill-leaderboard): weekly fleet snapshot 2026-05-17
  - New file `articles/skill-leaderboard-2026-05-17.md` (+75 lines): 107 active forks scanned, 1 aeon instance (AITOBIAS04), 14 skills enabled, 5th consecutive week with zero config drift.

- `f3af50b` — feat(repo-actions): 2026-05-18 action ideas batch
  - New file `articles/repo-actions-2026-05-18.md` (+97 lines): Five ideas generated — Trading Signal JSON, Simulation Archive Bundle, Per-Agent Stance Sparklines, Scenario Clone Button, Chinese + Japanese README translations. Context: 4th consecutive ATH session ($0.0000377 intraday, FDV $3.32M), PR #90 Farcaster Frame just opened, international audience signals (CN tweet, JP coverage).

**Impact:** The weekly reporting cycle gives a comprehensive operational snapshot. Framework watch launching this week is well-timed — 16 releases across 6 frameworks, with pydantic-ai's provider API change being the most relevant to monitor.

### Content & Monitoring

**Summary:** Daily monitoring and content generation skills ran their regular cycles.

**Commits:**

- `363c098` — project-lens: historical parallel — HyperCard 1987 to Farcaster Frames
  - New file `articles/project-lens-2026-05-18.md` (+47 lines): Framing PR #90 (Farcaster Frame v2) as the network-native completion of Bill Atkinson's 1987 card-stack runtime. Charts SVG from PR #85 becomes the Frame image; meta-tag lineage traced through Open Graph → Twitter Cards → Facebook Platform 2007.

- `dfd97f9` — feat(repo-pulse): MiroShark daily repo pulse 2026-05-18 — 1,172 stars (+7), 236 forks (+1)
  - Memory log entry with daily star/fork counts.

- ~40 additional chore commits: scheduler state updates, cron success markers, auto-commits for each skill run (token-report, fetch-tweets, tweet-allocator, star-milestone, star-momentum-alert). These maintain the cron state machine but contain no substantive code changes.

**Impact:** 1,172 stars (+7 today, +42 this week) and 236 forks (+1 today). The project-lens article creates a narrative bridge between the newly-opened Farcaster Frame PR and the broader history of embeddable interactive content.

---

## Developer Notes
- **New dependencies:** None. The zero-new-dependency streak extended to 25 consecutive PRs (#57 through #90 candidate).
- **Breaking changes:** None on MiroShark main. Pydantic-ai 1.97.0 (tracked in framework watch) renamed Google provider IDs and deprecated `MCPServer*` — relevant if any downstream tool uses pydantic-ai.
- **Architecture shifts:** Chart SVG establishes a second stdlib XML renderer alongside the sitemap (PR #82), confirming the pattern of pure-stdlib rendering services with no external dependencies. SMTP email adds a 4th parallel notification dispatcher in `simulation_runner.py` following the same fire-and-forget daemon-thread pattern as Discord/Slack/webhook.
- **Tech debt:** The 17 locally-built feature PRs remain blocked on `GH_GLOBAL` secret (now 18th consecutive block with today's Adversarial Stress-Test Mode). Repo-pulse doesn't write article files (PR #42 opened to fix). The Adversarial Stress-Test Mode feature build completed today but couldn't push.

## What's Next
- **PR #90 (Farcaster Frame v2)** is open and ready for review — if merged, it becomes the first decentralized social protocol distribution surface.
- **PR #89 (Neo4j security fix)** from @teifurin is the first external security contribution — review and merge closes a hardcoded credential gap.
- **GH_GLOBAL secret** remains the single largest blocker — 18 feature PRs built locally but unable to push. Setting this secret would unblock the entire backlog in one action.
- The repo-actions batch generated 5 new ideas, with **Trading Signal JSON** and **Scenario Clone Button** as the lowest-effort, highest-impact candidates.
- **AI framework watch** is now baselined — next week's run will show actual 7d deltas and momentum picks.
- Token at $0.0000377 intraday high / $0.00003323 close, FDV $3.32M — four consecutive ATH sessions suggest momentum hasn't peaked.
