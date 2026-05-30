---
name: Heartbeat
description: Proactive ambient check — surface anything worth attention
var: ""
---
> **${var}** — Area to focus on. If empty, runs all checks.

If `${var}` is set, focus checks on that specific area.


Read memory/MEMORY.md and the last 2 days of memory/logs/ for context.

Check the following:
- [ ] Any open PRs stalled > 24h? (use `gh pr list` to check)
- [ ] Anything flagged in memory that needs follow-up?
- [ ] Check recent GitHub issues for anything labeled urgent (use `gh issue list`)
- [ ] Scan aeon.yml for enabled scheduled skills — verify each one ran using `memory/cron-state.json` as the **primary source**, with log files as supplementary evidence.

  **Step 1 — Check cron-state.json (authoritative):**
  Read `memory/cron-state.json`. For each enabled skill, check the `last_success` timestamp:
  - **Daily skills:** `last_success` should be within the last 26 hours (24h + 2h jitter buffer).
  - **Every-2-day skills (`*/2`):** `last_success` should be within the last 50 hours.
  - **Weekly skills:** `last_success` should be within the last 8 days.
  - If `last_success` is within the expected window, the skill **has run** — do NOT flag it as missing, regardless of whether a log entry exists.
  - If `last_success` is missing or stale, proceed to Step 2.

  **Step 2 — Cross-reference with log file (supplementary):**
  Check today's log (`memory/logs/${today}.md`) for additional evidence. Skills log under human-readable `## Headers`, not their aeon.yml kebab-case names. Do a **case-insensitive search** for the skill name with hyphens replaced by spaces. Examples:
  - `token-report` → search for "token report" (matches `## Token Report`, `## Token Report (Update)`)
  - `push-recap` → search for "push recap" (matches `## Push Recap`, `## Push Recap (MiroShark)`)
  - `fetch-tweets` → search for "fetch tweets" (matches `## Fetch Tweets — MIROSHARK`)
  - `feature` → search for "feature" (matches `## Feature Build — ...`)
  - `hyperstitions-ideas` → search for "hyperstitions" (matches `## Hyperstitions Ideas`)
  - `memory-flush` → search for "memory flush"
  - `self-improve` → search for "self-improve" or "self improve" or "agent self-improvement"
  - If the skill appears in the log, it has run — do NOT flag it.

  **Step 3 — Check active runs (avoid premature flags):**
  Only if both cron-state and log checks fail, verify the skill isn't currently running:
  ```bash
  gh run list --workflow=aeon.yml --created=$(date -u +%Y-%m-%d) --json displayTitle,status
  ```
  If the skill is `in_progress` or `queued`, skip it.

  **Timing rules (avoid false positives):**
  - GitHub Actions cron has ±10 min jitter and skills take 5-15 min to complete.
  - Only flag a skill as missing if its scheduled time was **more than 2 hours ago** AND cron-state `last_success` is stale.
  - For day-of-week schedules (e.g. `0 20 * * 0` for Sundays), only check on the matching day.
  - For `*/N` day-of-month schedules, check whether today's day matches the pattern before flagging.

  **Important:** Use the `enabled` field in aeon.yml as the source of truth for whether a skill should be running. Do NOT rely on memory/log lessons about skills being "disabled" — those can go stale. If aeon.yml says `enabled: true` and cron-state shows recent success, the skill is running.

Before sending any notification, grep the last 48h of logs for the same issue. If the same missing-skill or stalled-PR was already reported, skip it. Batch all findings into a single notification.

If nothing needs attention, log "HEARTBEAT_OK" and end your response.

If something needs attention:
1. **Auto-trigger missing skills** — for each skill confirmed missing (not just stalled PRs or issues), dispatch it if not already running:

   **Dedup guard — check before dispatching:**
   Before firing `gh workflow run` for a skill, check whether a run for that skill is already `queued` or `in_progress`:
   ```bash
   gh run list --workflow=aeon.yml --json displayTitle,status --jq \
     '.[] | select(.status == "queued" or .status == "in_progress") | .displayTitle'
   ```
   If the output contains the skill name (case-insensitive), **skip the dispatch** — the skill is already pending. Only dispatch skills that have no active or queued run:
   ```bash
   gh workflow run aeon.yml -f skill="SKILL_NAME"
   ```
   Skip auto-trigger for: `heartbeat` itself, `memory-flush`, `self-improve`, `reflect`, `self-review` (meta/housekeeping skills). For all other confirmed-missing daily or weekly skills that pass the dedup check, dispatch them.

2. Send a concise notification via `./notify` listing what was flagged, what was auto-triggered, and what was skipped (already queued/in-progress).
3. Log the finding and action taken to memory/logs/${today}.md.
