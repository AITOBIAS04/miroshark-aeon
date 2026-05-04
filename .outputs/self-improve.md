*Agent Self-Improvement — 2026-05-04*

Fixed stale tweet resurfacing in fetch-tweets. The WebSearch fallback was reporting old founding tweets (March 20-21) as "new" because they fell outside the 3-day dedup window. Extended the window and added an age filter.

Why: May 4 fetch-tweets logged 2 March founding tweets as new — WebSearch surfaces high-engagement old content and the 3-day dedup window let them through.

What changed:
- skills/fetch-tweets/SKILL.md: dedup window 3d → 7d, added 14-day age filter for WebSearch fallback path, updated dedup-empty log message

Impact: Cleaner notifications — old founding/launch tweets won't resurface as "new" every few days when using the WebSearch fallback.

PR: https://github.com/AITOBIAS04/miroshark-aeon/pull/4
