*Agent Self-Improvement — 2026-04-30*

Post-outage cron-state recovery: after the 15-day auth outage (ISS-001), every skill success_rate in cron-state.json was permanently stuck at 0-1% — poisoned by 200-300 phantom failures from a single root cause. This adds automatic recovery detection and metric reset.

Why: ISS-001 auth outage (Apr 16-30) left all 14 skills with success_rate of 0% despite now running perfectly. The health guard (PR #1) and any future monitoring would operate on meaningless data — a skill succeeding 100% of the time since recovery would still show 1% overall.

What changed:
- scripts/prefetch-cron-recovery.sh (new): Detects outage recovery (all skills recovered but success_rate < 10%), resets counters to clean baseline, fires once via marker file
- memory/issues/ISS-001.md: Closed — auth restored, all skills succeeding
- memory/issues/INDEX.md: ISS-001 moved to Resolved
- memory/MEMORY.md: Updated tracking

Impact: Clean metrics baseline for all monitoring and reporting. ISS-001 formally closed. The agent can now accurately track its own health going forward instead of being haunted by a 15-day ghost in the data.

PR: https://github.com/AITOBIAS04/miroshark-aeon/pull/2
