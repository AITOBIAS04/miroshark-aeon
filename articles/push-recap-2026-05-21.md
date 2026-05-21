# Push Recap — 2026-05-21

## Overview
4 commits by 2 authors (@aaronjmars, aeonframework) across 2 repos. Today's thrust: the notification and distribution stack got two major additions — Telegram Bot notifications and a Shields.io-style consensus badge — while miroshark-aeon shipped a reliability fix that closes a 3-day diagnostic hunt. The Aeon daily skill cycle ran all 13 scheduled skills successfully.

**Stats:** 20 files changed, +2,238/-40 lines across 4 significant commits (+ ~33 cron/scheduler bookkeeping commits on miroshark-aeon)

---

## aaronjmars/MiroShark

### Notification Stack: Telegram Bot — 5th Channel (PR #93)
**Summary:** Adds native Telegram Bot API integration as the fifth notification channel alongside Webhook, Discord, Slack, and SMTP. Two env vars (`TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID`) turn any private chat, group, or channel into a live simulation-completion firehose — covering the messaging surface where most of MiroShark's crypto/political audience already lives.

**Commits:**
- `aa448a5` — feat: Telegram Bot completion notifications (5th channel — sendMessage with HTML) (#93)
  - New file `backend/app/services/telegram_notify.py` (+556 lines): Bot API `sendMessage` call with `parse_mode=HTML` and a single-button `inline_keyboard` linking the share page. Stdlib only. Fire-and-forget daemon-thread dispatch with per-process `(sim_id, status)` dedup. Reuses `webhook_service.build_payload` for content formatting
  - Changed `backend/app/services/simulation_runner.py` (+33 lines): Wired Telegram dispatch into the three terminal-state call sites used by the other notification channels
  - Changed `backend/app/api/notifications.py` (+9/-7 lines): `GET /api/config/notifications` now surfaces `telegram_configured` boolean so the frontend can render a status chip
  - New file `backend/tests/test_unit_telegram_notify.py` (+442 lines): 36 unit tests covering message formatting, dedup, error handling, thread dispatch
  - Changed `backend/tests/test_unit_notifications_config.py` (+65/-1 lines): Extended for `telegram_configured` field + dedicated "both env vars required" test
  - Changed `.env.example` (+13 lines): Documented `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` with setup instructions
  - Changed `README.md` (+2 lines): Feature table row for Telegram Bot notifications
  - Changed `docs/NOTIFICATIONS.md` (+90/-21 lines): Full operator documentation with @BotFather setup walkthrough

**Impact:** Completes the notification quintet. Telegram is the natural home channel for the crypto-launch audience — operators who already have a bot token from Aeon's own notification stack can now reuse it for simulation completion alerts. Zero new dependencies, fire-and-forget architecture matches the other four channels.

---

### Distribution Surface #13: Consensus Status Badge SVG (PR #94)
**Summary:** A flat 20-pixel Shields.io-style SVG badge showing consensus direction and confidence percentage — embeddable in any GitHub README, Notion page, or Substack post with one line of Markdown. The 13th publish-gated share surface and the cheapest visible pointer back to a simulation.

**Commits:**
- `f2fea38` — feat: consensus status badge SVG — Shields.io-style distribution amplifier (#94)
  - New file `backend/app/services/badge_service.py` (+319 lines): Pure stdlib `xml.etree.ElementTree` SVG renderer. Pinned colour vocabulary (`#22c55e` Bullish / `#6b7280` Neutral / `#ef4444` Bearish) matches every other belief surface. Defensive on unknown direction (neutral grey + "Unknown" label), confidence clamped 0–100. Bytewise-stable output across calls with same inputs
  - Changed `backend/app/api/simulation.py` (+87 lines): `GET /<id>/badge.svg` endpoint with same publish gate as all other share surfaces. Returns 404 when no `belief.final` exists yet (broken-image placeholder rather than misleading "Unknown 0%"). `Cache-Control: public, max-age=60` so embedded badges track live sims within one poll cycle
  - Changed `backend/app/services/surface_stats.py` (+3/-1 lines): `badge_svg` added to `SURFACE_KEYS` for analytics
  - New file `backend/tests/test_unit_badge_service.py` (+329 lines): 22 unit tests covering SVG structure, aria-labels, direction-to-colour mapping for all three stances, confidence clamping (negative, >100, non-numeric, None), route decorator, mimetype, cache headers, surface_stats registration, bytewise determinism, rounded corners, 20px height, viewBox invariant
  - Changed `frontend/src/components/EmbedDialog.vue` (+129 lines): New badge section with live in-place preview + Copy URL / Copy Markdown / Copy HTML snippet buttons
  - Changed `frontend/src/api/simulation.js` (+29 lines): `getBadgeUrl` helper
  - Changed `backend/openapi.yaml` (+71 lines): `GET /<id>/badge.svg` docs + `badge_svg` added to `SimulationSurfaceStats` schema
  - Changed `docs/API.md` (+1 line): Endpoint row
  - Changed `docs/FEATURES.md` (+23 lines): Dedicated feature section
  - Changed `backend/tests/test_unit_surface_stats.py` (+1 line): Counter test

**Impact:** Inverts the distribution model — instead of waiting for readers to navigate to the share page, the badge brings the simulation to wherever the reader already is. A researcher's README with `![MiroShark](https://host/api/simulation/<id>/badge.svg)` becomes a live indicator. Same zero-deps posture as the previous 12 surfaces. 13 share surfaces now feature-complete.

---

## aaronjmars/miroshark-aeon

### Reliability Fix: Bankr Agent Timeout Detection (PR #43)
**Summary:** Three consecutive `TWEET_ALLOCATOR_EMPTY` runs (May 18/19/20) masked a real issue: the Bankr Agent API's Max-Mode (claude-sonnet-4.6) responses were taking longer than the 64-second polling window. The fix distinguishes "agent didn't finish in time" from "agent says no wallet exists."

**Commits:**
- `3d828d1` — improve: distinguish bankr agent-timeout from completed-no-wallets (#43)
  - Changed `scripts/prefetch-bankr.sh` (+33/-8 lines): Poll loop expanded 8→14 iterations (~112s window). Submit `max-time` raised 30→45s. New `TIMED_OUT` counter tracks jobs that never reached terminal state. Timed-out handles excluded from `verified-handles.json` entirely. New `prefetch-status.json` field `timed_out`. New top-level status `"agent-timeout"` when most lookups hit the poll-window ceiling
  - Changed `skills/tweet-allocator/SKILL.md` (+3/-2 lines): New step-4 branch for `"agent-timeout"` → `TWEET_ALLOCATOR_ERROR` (sends alert) instead of silently treating it as `_EMPTY`. Documents the three-way distinction: API unreachable vs. agent didn't finish vs. genuinely no wallet

**Impact:** Closes a 3-day diagnostic hunt. The silent data loss pattern — where `TWEET_ALLOCATOR_EMPTY` looked like "nobody has a wallet" but was actually "we didn't wait long enough for the LLM" — is now surfaced as a distinct error with its own alert. The wider polling window (112s vs 64s) also gives Max-Mode agent calls room to complete on slower days.

### Daily Aeon Skill Cycle
**Summary:** Full Wednesday skill cycle executed successfully across ~33 commits. All 13 scheduled skills ran and committed:

- **token-report** (06:34 UTC) — daily token price snapshot
- **fetch-tweets** (06:34 UTC) — tweet collection
- **tweet-allocator** (09:33 UTC) — allocation run
- **repo-pulse** (10:43 UTC) — repository health check (1,177→1,186 stars, +9)
- **star-momentum-alert** (10:45 UTC) — OUT_OF_WINDOW (1,186★ → 1,500★ in ~67d)
- **feature** (12:10 UTC) — Agent Journey View built (21st feature, push blocked by GH_GLOBAL)
- **star-milestone** (15:27 UTC) — milestone check
- **push-recap** (15:32 UTC) — previous day's recap
- **project-lens** (16:48 UTC, prev day) — project analysis
- **repo-article** (16:41 UTC, prev day) — article generation
- **thread-formatter** (17:50 UTC, prev day) — thread formatting
- **memory-flush** (18:44 UTC, prev day) — memory consolidation
- **heartbeat** (19:33 UTC, prev day) — system health check

---

## Developer Notes
- **New dependencies:** None. Both MiroShark PRs maintain the 30-PR zero-new-deps streak
- **Breaking changes:** None. Both PRs are additive and backward compatible
- **Architecture shifts:** The badge SVG introduces the pattern of returning non-JSON content from the simulation API (`Content-Type: image/svg+xml`) — first time a share surface endpoint returns a binary-ish format instead of JSON/HTML
- **Tech debt:** The GH_GLOBAL secret remains unset — 21 features now built locally but cannot be pushed to the watched repo. Agent Journey View is the latest addition to the blocked queue

## What's Next
- **Badge adoption:** With 13 share surfaces complete, the distribution stack is approaching maturity. The badge is the most viral surface yet — every README embed is a passive distribution point
- **GH_GLOBAL unblock:** 21 features spanning 6 weeks are waiting to be pushed. This is the single highest-leverage operational fix
- **Remaining repo-actions ideas:** Polymarket/Manifold Calibration, Gallery Community Upvotes, Academic Citation Generator, and Simulation Outcome Auto-Resolution from the May 20 batch
- **Star momentum:** 1,186 stars (+9 today), tracking toward 1,500 around July 27
