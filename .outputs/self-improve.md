*Agent Self-Improvement — 2026-05-02*

Fixed heartbeat false positives for */N day-of-month cron schedules. The heartbeat skill correctly handled day-of-week patterns (Sundays, Mondays, etc.) but had no logic for */N day-of-month patterns used by self-improve, repo-actions, and repo-article.

Why: On even-numbered days (today is May 2), heartbeat would flag these three */2 skills as "missing" even though they only run on odd days. This generated noisy false-positive notifications every other day and triggered failed dispatch attempts.

What changed:
- skills/heartbeat/SKILL.md: Added */N day-of-month matching rule with formula (day - 1) % N == 0, plus POSIX cron OR behavior for combined day-of-month + day-of-week fields

Impact: Eliminates recurring false-positive alerts on ~15 days per month. Heartbeat reports become trustworthy — every flagged skill is genuinely missing, not just off-schedule.

PR: https://github.com/AITOBIAS04/miroshark-aeon/pull/3
