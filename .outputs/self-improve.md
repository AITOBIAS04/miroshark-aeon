*Agent Self-Improvement — 2026-04-30*

Pre-flight health guard added to detect systemic skill failures (like the 15-day auth outage) at the bash level — before Claude even starts. This means future outages will surface as ::error:: annotations in GitHub Actions UI even when Claude itself cannot authenticate.

Why: From Apr 16–30, all skills failed silently for 15 days because ANTHROPIC_API_KEY expired. The heartbeat skill (the existing detection layer) could not catch this because it also requires Claude auth to run. The outage was only discovered when auth was manually restored.

What changed:
- scripts/prefetch-health-guard.sh (new): Reads cron-state.json before every skill run. When >80% of tracked skills show 10+ consecutive failures, logs prominent error annotations in the GitHub Actions workflow UI with root cause hint and remediation steps.
- skills/heartbeat/SKILL.md: Added cron-state analysis as step 0 — classifies failures as systemic (auth/infra) vs individual, detects recovery mode, integrates with issue tracker.

Impact: Future auth or infrastructure outages will be visible in the GitHub Actions UI within hours instead of going undetected for weeks.

PR: https://github.com/AITOBIAS04/miroshark-aeon/pull/1
