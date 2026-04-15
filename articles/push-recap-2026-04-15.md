# Push Recap — 2026-04-15

## Overview
20 commits across 2 repos by 2 authors (aaronjmars, Aeon). The headline: miroshark-aeon absorbed a massive upstream architecture sync — 130 files, 40+ new skills, chain-runner workflow, MCP/A2A servers, a full dashboard rewrite, and a docs site — while MiroShark shipped browser push notifications end-to-end via PR #30.

**Stats:** ~170 files changed, +15,100/-2,520 lines across 20 commits

---

## aaronjmars/MiroShark

### New Feature: Browser Push Notifications on Simulation Completion (PR #30)
**Summary:** Users can now opt in to browser notifications during a simulation run. When the simulation finishes — even if the tab is in the background or minimized — the browser fires a push notification with a summary of what happened. The entire Web Push stack is self-contained: VAPID key generation, subscription persistence, and push dispatch all run on the MiroShark backend with zero external services.

**Commits:**
- `3e6251d` — feat: browser push notifications on simulation completion (Aeon)
  - New `backend/app/services/push_notification_service.py` (+212 lines): Full VAPID key lifecycle — generates EC keys on first use, caches in `uploads/vapid_keys.json`, stores push subscriptions per simulation in JSON files. Sends notifications via `pywebpush` in a background daemon thread. Auto-prunes expired/unsubscribed endpoints (HTTP 404/410).
  - Modified `backend/app/api/simulation.py` (+130 lines): Three new endpoints — `GET /push/vapid-public-key` returns the applicationServerKey, `POST /push/subscribe` stores a browser subscription tied to a simulation ID with endpoint deduplication, `POST /push/test` fires an immediate test notification.
  - Modified `backend/app/services/simulation_runner.py` (+20 lines): Fires push notification in `_monitor_simulation()` when `exit_code == 0`. Notification body includes round count and total events.
  - Modified `backend/requirements.txt` (+4 lines): Added `pywebpush>=2.0.0` dependency.
  - New `frontend/public/sw.js` (+70 lines): Service worker that handles `push` events (shows browser notification) and `notificationclick` (focuses existing tab or opens new window, navigating to simulation results).
  - Modified `frontend/src/main.js` (+7 lines): Registers the service worker on app load.
  - Modified `frontend/src/components/Step3Simulation.vue` (+139/-1 lines): Added a toggle in the events-summary bar during active runs. Checks for Web Push API support (`Notification`, `serviceWorker`, `PushManager`). On toggle, requests permission, fetches VAPID key, subscribes via `pushManager.subscribe()`, and POSTs the subscription to the backend. Shows state: "Notify me" / "Notify on" / "Blocked". Resets on simulation restart.
  - Modified `frontend/src/api/simulation.js` (+24 lines): `getVapidPublicKey()`, `subscribePush()`, `testPushNotification()` API functions.

- `b96cd14` — fix: address push notification nits before merge (aaronjmars)
  - Modified `backend/app/services/push_notification_service.py` (+23/-14 lines): Added `fcntl` file locking around subscription read-write to prevent race conditions when multiple browser tabs subscribe concurrently. Added security comment about VAPID key exposure risk.
  - Modified `backend/app/services/simulation_runner.py` (+12 lines): `cleanup_simulation_logs()` now also deletes push subscription files and lock files for the simulation.
  - Modified `frontend/public/sw.js` (-2 lines): Removed unused `CACHE_NAME` constant.

- `33de5fe` — Merge pull request #30 from aaronjmars/feat/push-notifications-on-completion

**Impact:** Solves the "staring at a loading screen" problem for long simulations. Users toggle notifications once, walk away, and get pulled back when results are ready. No Firebase, no external push service — runs entirely on VAPID + pywebpush. The `fcntl` locking in the nits commit shows the maintainer hardening concurrent subscription writes before merge.

---

## aaronjmars/miroshark-aeon

### Full Architecture Upgrade — Upstream Boilerplate Sync
**Summary:** A single massive commit synced the miroshark-aeon fork with the upstream Aeon framework, adding chain-based skill orchestration, 40+ new skill templates, an MCP server, an A2A (Agent-to-Agent) server, a completely rewritten dashboard, a Jekyll-based docs site, and overhauled CI/CD workflows. This is the biggest single commit in the repo's history.

**Commits:**
- `47ff49f` — feat: sync boilerplate features — full architecture upgrade (aaronjmars)
  - Modified `.github/workflows/aeon.yml` (+473/-71 lines): Skill input changed from a fixed `choice` dropdown to a free-form `string` (any skill directory name now valid). Major workflow restructuring.
  - New `.github/workflows/chain-runner.yml` (+338 lines): Skill chaining workflow — runs multi-step chains defined in `aeon.yml`, saves outputs to `.outputs/{skill}.md`, injects prior outputs into downstream steps. Supports parallel and sequential execution.
  - Modified `.github/workflows/messages.yml` (+482/-208 lines): Renamed to "Messages & Scheduler" — now handles scheduled skill dispatch natively alongside message polling. Reactive trigger parser added.
  - Modified `CLAUDE.md` (+58/-9 lines): Documents chain syntax, `.outputs/` directory, and updated skill chaining instructions.
  - Modified `aeon.yml` (+70/-4 lines): New `chains:` section and expanded skill configuration options.
  - New `a2a-server/` (4 files, +612 lines): Agent-to-Agent protocol server in TypeScript — enables inter-agent communication.
  - New `mcp-server/` (3 files, +266 lines): Model Context Protocol server — exposes Aeon capabilities to Claude and other MCP clients.
  - New `dashboard/components/` (15 new files, ~1,100+ lines): Complete dashboard UI rewrite with `LeftSidebar`, `RightPanel`, `SkillDetail`, `ScheduleEditor`, `SecretsPanel`, `AuthModal`, `TopBar`, `HQOverview`, `TargetCursor`, and more. Analytics API endpoint added.
  - Modified `dashboard/app/page.tsx` (+93/-1,531 lines): Old monolithic page gutted and replaced with component-based architecture.
  - New `docs/` (14 files, ~800+ lines): Jekyll-based documentation site with layouts, data files (articles, logs, memory, topics), and initial posts.
  - New `scripts/` (6 new files): `generate-feed.sh`, `postprocess-replicate.sh`, `prefetch-xai.sh`, `skill-runs` (audit tool), `sync-site-data.sh`, `sync-upstream.sh`.
  - New `skills/` (40+ new skill templates): `deep-research`, `fleet-control`, `auto-merge`, `auto-workflow`, `deploy-prototype`, `vuln-scanner`, `cost-report`, `skill-evals`, `skill-repair`, `autoresearch`, `channel-recap`, `deal-flow`, `evening-recap`, `external-feature`, `farcaster-digest`, `fork-fleet`, `github-releases`, `last30`, `market-context-refresh`, `monitor-polymarket`, `narrative-tracker`, `reg-monitor`, `remix-tweets`, `repo-scanner`, `rss-feed`, `skill-leaderboard`, `skill-security-scan`, `spawn-instance`, `technical-explainer`, `telegram-digest`, `tool-builder`, `treasury-info`, `tweet-roundup`, `unlock-monitor`, `update-gallery`, `vercel-projects`, `vibecoding-digest`, `workflow-security-audit`, and more.
  - New `skills.json` (+557 lines): Full skill catalog with metadata.
  - New utility scripts: `add-a2a` (+193), `add-mcp` (+164), `export-skill` (+148), `generate-skills-json` (+177).
  - New `workflows/` (6 files): Pre-built workflow templates for changelog, code-health, issue-triage, PR review, security-digest.
  - New `soul/` files: `SOUL.md` and `STYLE.md` templates (empty — ready for identity configuration).

**Impact:** miroshark-aeon is no longer a lightweight wrapper around a few skills. It's now a full-featured Aeon instance with chain orchestration, 90+ total skills, server-mode interfaces (MCP + A2A), a componentized dashboard, and a documentation site. The `chain-runner.yml` workflow is the key new primitive — skills can now be composed into multi-step pipelines with output passing, parallel execution, and error handling.

### README & Branding Refresh
**Summary:** The README was rewritten to reflect the architecture upgrade, with a new tagline and refreshed visual assets.

**Commits:**
- `5efa8fc` — docs: sync README and assets from upstream aeon (aaronjmars)
  - Modified `README.md` (+172/-407 lines): New tagline: "The most autonomous agent framework." Restructured content around the expanded capability set. Net reduction of 235 lines — tighter, more focused copy.
  - Swapped assets: removed `aeon.gif` and `skills.jpg`, added `aeonframework.gif`, `architecture.jpg`, `autonomy.jpg`, `skill.jpg`.

**Impact:** Public-facing identity now matches the scale of the framework. The old README described a small agent; the new one describes a platform.

### Bug Fix: Reactive Trigger Parser
**Summary:** Fixed a bash regex syntax error that broke the reactive trigger parser in the scheduler workflow.

**Commits:**
- `843033b` — fix: bash syntax error in reactive trigger parser (aaronjmars)
  - Modified `.github/workflows/messages.yml` (+1/-1 line): Changed `! [[ "$line" =~ ^\ ]]` to `! [[ "$line" =~ ^[[:space:]] ]]` — the escaped space wasn't matching correctly in all bash versions.

**Impact:** Reactive triggers (skills that fire in response to events rather than cron) now parse correctly. This was a silent failure — triggers would be skipped without error.

### Heartbeat Dispatch Verification
**Summary:** Quick test cycle to verify that the heartbeat auto-dispatch feature (PR #11, merged Apr 14) actually works when triggered by the scheduler.

**Commits:**
- `30ba5e6` — test: schedule heartbeat at 19:20 UTC to verify dispatch (aaronjmars)
  - Modified `aeon.yml`: Temporarily changed heartbeat schedule from `0 19` to `20 19`.
- `7d7fd00` — revert: restore heartbeat schedule after dispatch test (aaronjmars)
  - Modified `aeon.yml`: Reverted to `0 19 * * *`.

**Impact:** Confirmed that heartbeat auto-dispatch works correctly. Clean revert — no lasting config changes.

### Automated Daily Operations
**Summary:** 12 auto-commits from Aeon covering the daily skill pipeline — token reports, tweet fetches, repo pulse, heartbeat checks, memory consolidation, and scheduler state updates.

**Commits:**
- `92d2d37` — chore(token-report): daily report 2026-04-15
- `f3b799c` — chore(fetch-tweets): daily tweet digest 2026-04-15
- `b4b0bf5` — chore(repo-pulse): daily repo pulse 2026-04-15
- `dea16d6` — chore(memory): log feature/push-notifications build — PR #30 on MiroShark
- `642ca00` — chore(heartbeat): auto-commit 2026-04-15 (first run)
- `7d0e4dc` — chore(cron): heartbeat success (first run)
- `9f4a5cd` — chore(scheduler): update cron state
- `584d578` — chore(memory-flush): auto-commit 2026-04-15
- `7a43171` — chore(cron): memory-flush success
- `3dea30c` — chore(heartbeat): auto-commit 2026-04-15 (second run)
- `95dafdc` — chore(cron): heartbeat success (second run)
- `eee07ce` — chore(heartbeat): auto-commit 2026-04-14 (tail-end of yesterday)

**Impact:** All daily skills ran on schedule. Heartbeat ran twice today due to the dispatch verification test. Memory flush consolidated 3 days of logs. Standard operations healthy.

---

## Developer Notes
- **New dependencies:** `pywebpush>=2.0.0` added to MiroShark backend for VAPID push notifications.
- **Breaking changes:** miroshark-aeon's `aeon.yml` skill input changed from fixed `choice` list to free-form `string` — any skill directory name is now accepted. Old manual dispatch bookmarks targeting the `choice` dropdown will still work but the UI is different.
- **Architecture shifts:** Three major new primitives — chain-runner (multi-step skill pipelines), MCP server (Model Context Protocol interface), A2A server (Agent-to-Agent protocol). Dashboard moved from a monolithic page to component architecture.
- **Tech debt:** The architecture sync commit (`47ff49f`) is a single 130-file commit rather than a series of incremental PRs. Makes bisection harder if issues surface later. The 40+ new skill templates are upstream defaults — most are disabled and need configuration before use.

## What's Next
- The 40+ new skills added from the upstream sync are templates — expect a follow-up to enable and configure the ones relevant to MiroShark (deep-research, auto-merge, deploy-prototype).
- Chain definitions in `aeon.yml` are empty — first chains to be defined, likely combining research + feature + article workflows.
- The docs site (`docs/`) has initial posts from March but needs content from April's extensive build cycle to be synced.
- MCP and A2A servers are added but not yet wired into any workflow or deployment — infrastructure is staged, activation pending.
- With push notifications merged, the next MiroShark feature candidates from repo-actions are: Statistical Batch Runs, Jupyter Notebook Export, REST API + Webhook, or Hall of Fame page.
