---
name: Heartbeat
description: Proactive ambient check — surface anything worth attention
var: ""
---
> **${var}** — Area to focus on. If empty, runs all checks.

If `${var}` is set, focus checks on that specific area.


Read memory/MEMORY.md and the last 2 days of memory/logs/ for context.

Check the following:

### 0. System health (cron-state analysis)
Read `memory/cron-state.json`. For each skill, note `consecutive_failures` and `last_error`.
- If **>80% of skills** have `consecutive_failures >= 10` with similar `last_error` signatures (e.g. all contain "Not logged in" or all show 0 tokens): this is a **systemic failure** (auth, infra, or config). Classify it as such — don't list individual skill failures. Report the root cause, when it started (`last_success` dates), and the remediation (e.g. "renew ANTHROPIC_API_KEY in repo secrets").
- If **this heartbeat succeeds after a systemic failure**: you're in **recovery mode**. Note how long the outage lasted, check `memory/issues/` for open issues matching this pattern, and update them. Log a RECOVERY event.
- If only **individual skills** are failing (1-3 skills, different errors): report them individually with their specific error.
- Check `memory/issues/INDEX.md` — if an open issue matches what you're seeing, update its status rather than filing a duplicate.

### 1. Standard checks
- [ ] Any open PRs stalled > 24h? (use `gh pr list` to check)
- [ ] Anything flagged in memory that needs follow-up?
- [ ] Check recent GitHub issues for anything labeled urgent (use `gh issue list`)
- [ ] Scan aeon.yml for enabled scheduled skills — cross-reference with today's log (`memory/logs/${today}.md`) to find any that haven't run when expected.

  **Matching skill names to log entries:**
  Skills log under human-readable `## Headers`, not their aeon.yml kebab-case names. To check if a skill ran, do a **case-insensitive search** of the log file for the skill name with hyphens replaced by spaces. Examples:
  - `token-report` → search for "token report" (matches `## Token Report`, `## Token Report (Update)`)
  - `push-recap` → search for "push recap" (matches `## Push Recap`, `## Push Recap (MiroShark)`)
  - `fetch-tweets` → search for "fetch tweets" (matches `## Fetch Tweets — MIROSHARK`)
  - `feature` → search for "feature" (matches `## Feature Build — ...`)
  - `hyperstitions-ideas` → search for "hyperstitions" (matches `## Hyperstitions Ideas`)
  - `memory-flush` → search for "memory flush"
  - `self-improve` → search for "self-improve" or "self improve" or "agent self-improvement"

  **Timing rules (avoid false positives):**
  - GitHub Actions cron has ±10 min jitter and skills take 5-15 min to complete.
  - Only flag a skill as missing if its scheduled time was **more than 2 hours ago**.
  - Also check `gh run list --workflow=aeon.yml --created=$(date -u +%Y-%m-%d) --json displayTitle,status` — if the skill is currently `in_progress` or `queued`, don't flag it.
  - For day-of-week schedules (e.g. `0 20 * * 0` for Sundays), only check on the matching day.

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
