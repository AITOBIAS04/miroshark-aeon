*Agent Self-Improvement — 2026-05-24*

Fixed heartbeat false positives and Discord truncation.

The heartbeat skill was incorrectly flagging self-improve and repo-actions as "missed" on odd days (May 21, 23) because it did not understand that */2 DOM patterns use modulo arithmetic (fires only on even days). Also added Discord 2000-char content limit truncation to the notify script to prevent silent delivery failures.

Why: Heartbeat logs from May 21 and May 23 both show false positive alerts — skills marked as missing on days their schedule does not match. This created noise in ~50% of all heartbeat runs.

What changed:
- skills/heartbeat/SKILL.md: Added explicit timing rule explaining */N DOM modulo arithmetic with worked example
- notify: Added 1950-char truncation guard for Discord webhook content (matching existing Telegram 4096-char guard)

Impact: Eliminates false "missing skill" alerts from every other heartbeat run. Prevents future silent notification failures when Discord is configured.

PR: https://github.com/AITOBIAS04/CHORUS/pull/11
