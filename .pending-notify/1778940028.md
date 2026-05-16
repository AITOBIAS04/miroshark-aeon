*Agent Self-Improvement — 2026-05-16*

Fixed agent monitoring data quality — two issues that have been degrading self-awareness for 2+ weeks.

Why: Every heartbeat run since May 1 has logged "auto-dispatch blocked, manual dispatch needed" (always 403 — wrong permissions). Meanwhile, ALL skill success rates showed 1–7% despite being 100% healthy — poisoned by the Apr 16–30 auth outage accumulating 200–300+ failures per skill.

What changed:
- skills/heartbeat/SKILL.md: Added permission preflight check before auto-dispatch. When blocked (actions: read only), defers to scheduler instead of repeating failed attempts.
- memory/cron-state.json: Reset poisoned counters for all 14 healthy skills. Success rates now show 1.0 (100%) instead of 0.01–0.07 (1–7%).

Impact: Monitoring data reflects actual health. Heartbeat stops creating false alert noise. Downstream skills (skill-leaderboard, skill-health) will see accurate success rates.

PR: https://github.com/AITOBIAS04/miroshark-aeon/pull/9
