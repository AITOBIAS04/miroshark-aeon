# Push Recap — 2026-04-07

## Overview
10 commits across 2 repos today, spanning a major new MiroShark UI feature and a cluster of CI/operational reliability fixes in miroshark-aeon. The big story: MiroShark now lets users switch LLM providers, models, and API keys at runtime from the UI — no `.env` edits, no server restarts. On the aeon side, three targeted fixes tightened Telegram delivery, GitHub social monitoring, and the CI push pipeline.

**Stats:** ~15 files changed, +870/-11 lines across 10 commits

---

## aaronjmars/MiroShark

### New Feature: Runtime LLM Provider & Model Selector

**Summary:** A full settings panel now lets users configure their LLM backend at runtime without touching environment variables. The panel supports OpenAI-compatible providers (including OpenRouter and Ollama) and the Claude Code local CLI. It loads OpenRouter's live model catalog on demand, groups models by price tier, and includes a built-in "Test Connection" flow that pings the configured endpoint and returns latency.

**Commits:**
- `6748c21` — feat: LLM provider and model selector UI
  - New file `backend/app/api/settings.py` (+134 lines): Full Flask blueprint with 3 endpoints — `GET /api/settings` returns masked config, `POST /api/settings` updates provider/base_url/model/api_key/Neo4j at runtime by mutating `Config.*` class attributes, `POST /api/settings/test-llm` makes a live call and returns model + latency_ms. API keys masked to last 4 chars on all responses.
  - Modified `backend/app/__init__.py` (+2,-1): Registered `settings_bp` blueprint at `/api/settings`.
  - Modified `backend/app/api/__init__.py` (+2): Declared `settings_bp` Blueprint and imported the new module.
  - New file `frontend/src/api/settings.js` (+24 lines): Three thin axios wrappers — `getSettings()`, `updateSettings(data)`, `testLlmConnection()`.
  - New file `frontend/src/components/SettingsPanel.vue` (+664 lines): Vue 3 Composition API component using `<Teleport>`. Features: provider dropdown (openai-compatible vs claude-code), conditional base URL + model + API key fields that hide for the local CLI provider, OpenRouter model list loader (fetches `/api/v1/models`, sorts by prompt price, groups into Fast/Standard/Capable tiers), password toggle, test connection button with live status badge, Neo4j URI/user/password section, save flow with error/success feedback.
  - Modified `frontend/src/views/Home.vue` (+21 lines): Added gear icon button `⚙` to the home navbar, imported `SettingsPanel`, wired `settingsOpen` ref to open/close the teleported modal.

**Impact:** Users can now try different models (GPT-4o, Claude, OpenRouter models, local Ollama) without restarting the server or editing `.env`. This dramatically lowers the barrier for non-technical users and makes MiroShark practical in environments where env vars aren't easily accessible. The OpenRouter model tier grouping turns a 300+ model list into a navigable picker.

### Merged PRs: Cloud Deploy + Config Recovery

Three PRs merged to main today (previously built features landing in the mainline):

- `776081c` — Merged PR #9: one-click cloud deploy (Railway + Render, railway.json + render.yaml, built 2026-04-03)
- `a8a5d14` — Merged PR #10: config generation timeout and error recovery (90s timeout, backend error surfacing, Retry Config button, built 2026-04-04)
- `765322f` — Merged PR #12: LLM provider and model selector UI (the commit above)

All three open feature branches are now merged, leaving MiroShark's main branch fully up to date.

---

## aaronjmars/miroshark-aeon

### CI/Operational Reliability Fixes

**Summary:** Three targeted fixes addressed known failure modes in the aeon pipeline: Telegram sometimes silently dropped Markdown-formatted messages, the commit step was exiting early when Claude had already committed during its run (leaving those commits unpushed), and the `fetch-tweets` skill was only watching for token mentions rather than also tracking GitHub repo activity.

**Commits:**

- `ccb509e` — fix: push unpushed commits from Claude's session
  - Modified `.github/workflows/aeon.yml` (+11, -2): The old commit step ran `git diff --staged --quiet && exit 0`, which exited immediately if there was nothing new to stage — even if Claude had already made commits during its run that were never pushed. The fix adds a `git rev-list origin/main..HEAD --count` check: if there are unpushed commits, it skips the new commit but still runs the push loop. This was causing Aeon's own work to silently disappear after each CI run.

- `01bb321` — fix: robust Telegram notification with status check and retry
  - Modified `.github/workflows/aeon.yml` (+9, -5): The previous implementation used `curl -sf` (fail-on-error) and ORed a retry. The problem: Telegram returns HTTP 200 with `{"ok": false, ...}` for Markdown parse errors — so `curl -sf` would succeed and the retry would never fire. The fix captures the full response body + HTTP status code, then checks both the HTTP code AND the JSON `.ok` field before deciding whether to retry without Markdown. Aligns with the aeon-agent reference implementation.

- `000f462` — fetch-tweets: also search for GitHub repo mentions
  - Modified `aeon.yml` (+1, -1): Updated the `fetch-tweets` skill `var` from `"MIROSHARK crypto token on Base chain"` to `"MIROSHARK crypto token on Base chain AND https://github.com/aaronjmars/MiroShark"`. This makes the weekly social monitoring scan also surface tweets that mention the GitHub repo directly, catching developer/builder mentions alongside token traders.

- `88063d5` — Merged PR #7: improve log-before-notify in push-recap and repo-article (previously stalled, now landed)
- `30647f6` — merge: resolve conflicts with main (keep both sides)
- `db8dbbf` — chore(heartbeat): auto-commit 2026-04-06 (routine)

**Impact:** Aeon's own commits no longer go missing after each CI run. Telegram Markdown parse failures now correctly fall back to plain text instead of silently succeeding. The social listening net is wider, catching GitHub-focused mentions alongside pure token talk.

---

## Developer Notes
- **New dependencies:** None (SettingsPanel uses existing Vue + axios setup; OpenRouter model list fetched directly from their public API)
- **Breaking changes:** None — settings API is additive; runtime config mutations apply in-memory only (no persistence across restarts yet)
- **Architecture shifts:** `Config.*` class attributes are now mutable at runtime — a departure from the previous read-once-at-startup pattern. Worth noting if a future change adds caching on top of Config values.
- **Tech debt:** Runtime settings aren't persisted to `.env` or a settings file — a server restart resets everything. Likely the next iteration.

## What's Next
- MiroShark settings persistence (write runtime config back to `.env` or a local config file)
- Aeon has no open PRs — clean slate for new feature targeting
- Hyperstitions article cycle is active (Saturdays); next fire: 2026-04-11
- Star tracker: approaching 400+ stars on MiroShark — watch for 500-star milestone (target: 2026-04-15)
