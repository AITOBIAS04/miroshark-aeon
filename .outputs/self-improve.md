*Agent Self-Improvement — 2026-05-14*

Completed heartbeat skill-name-to-log matching for all 14 enabled skills and fixed a broken matching strategy.

Why: The heartbeat health monitor only had explicit log-header mappings for 7 of 14 enabled skills (repo-pulse, project-lens, repo-actions, repo-article, weekly-shiplog, skill-leaderboard, and heartbeat itself were missing). Worse, the matching strategy said "replace hyphens with spaces" but some skills log with hyphens in their headers (e.g. fetch-tweets logs as "## fetch-tweets —"), so the space-only search misses them — causing false "missing skill" alerts and unnecessary CI auto-dispatches.

What changed:
- skills/heartbeat/SKILL.md: Added dual-search strategy (search for BOTH original kebab-case name AND space-separated version) and complete mappings for all 14 enabled skills with real log header examples from recent runs.

Impact: Heartbeat can now reliably detect whether any enabled skill has run, preventing false missing-skill alerts and wasted CI dispatches. This is a multiplier improvement — better health monitoring means faster detection of real issues across all skills.

PR: https://github.com/AITOBIAS04/miroshark-aeon/pull/8
