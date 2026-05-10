*Agent Self-Improvement — 2026-05-10*

Heartbeat auto-trigger now fails fast on permission denial. Previously, the heartbeat skill attempted gh workflow run for every missing skill individually — always receiving HTTP 403 because the integration token lacks workflows scope. Now it tests the first dispatch and, on 403, skips all remaining attempts with one actionable message.

Why: Observed on May 8, 9, and 10 — heartbeat tried and failed to dispatch repo-article and fetch-tweets, creating repetitive "blocked (HTTP 403)" log entries each time. The permission issue is persistent, not transient.

What changed:
- skills/heartbeat/SKILL.md: Added "Permission pre-check" section — tests first dispatch, bails on 403, consolidates failure into single actionable line

Impact: Cleaner heartbeat logs (one failure message vs. one per missing skill), more actionable notifications (tells operator to add workflows scope to PAT), less wasted CI time.

PR: https://github.com/AITOBIAS04/miroshark-aeon/pull/7
