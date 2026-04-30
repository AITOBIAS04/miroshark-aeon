⚠️ HEARTBEAT ALERT — 2026-04-30

All skills have been failing for ~15 days (since 2026-04-16) with 'Not logged in · Please run /login'. Root cause: ANTHROPIC_API_KEY or CLAUDE_CODE_OAUTH_TOKEN expired or was removed from GitHub Actions secrets.

cron-state.json confirms 200–313 consecutive failures per skill, all with 0 tokens used. No memory logs since 2026-04-15.

This heartbeat (10:09 UTC) is running — auth may have just been restored. Auto-dispatch of missed skills was blocked (GITHUB_TOKEN lacks actions:write).

Action needed: confirm the API secret is valid in Settings → Secrets → Actions, then manually re-run today's skills: token-report, fetch-tweets, repo-pulse, repo-actions, repo-article, push-recap, feature. Filed ISS-001 in memory/issues/.
