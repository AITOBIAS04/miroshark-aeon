#!/usr/bin/env bash
# Detect post-outage recovery and reset poisoned cron-state metrics.
# Runs as a prefetch script before every skill. Only fires once per recovery.
set -euo pipefail

STATE_FILE="memory/cron-state.json"
MARKER_DIR="memory"

[ -f "$STATE_FILE" ] || exit 0
jq empty "$STATE_FILE" 2>/dev/null || exit 0

# Already recovered?
for marker in "$MARKER_DIR"/.cron-recovered-*; do
  [ -f "$marker" ] && exit 0
done

# Check recovery condition: ALL tracked skills have consecutive_failures=0
# but success_rate < 0.10 (indicating bulk outage contamination).
TOTAL_SKILLS=$(jq 'keys | length' "$STATE_FILE")
[ "$TOTAL_SKILLS" -eq 0 ] && exit 0

RECOVERED=$(jq '[to_entries[] | select(.value.consecutive_failures == 0)] | length' "$STATE_FILE")
POISONED=$(jq '[to_entries[] | select(.value.success_rate < 0.10)] | length' "$STATE_FILE")

# Need ALL skills recovered AND majority poisoned
if [ "$RECOVERED" -ne "$TOTAL_SKILLS" ] || [ "$POISONED" -lt "$((TOTAL_SKILLS / 2))" ]; then
  exit 0
fi

echo "::notice::Outage recovery detected — resetting cron-state metrics for $TOTAL_SKILLS skills"

# Reset each skill to a clean baseline, preserving timestamps
jq 'to_entries | map(
  .value.total_runs = .value.total_successes |
  .value.total_failures = 0 |
  .value.success_rate = 1.0 |
  .value.last_error = null
) | from_entries' "$STATE_FILE" > "${STATE_FILE}.tmp" && mv "${STATE_FILE}.tmp" "$STATE_FILE"

# Write recovery marker
TODAY=$(date -u +%F)
echo "Recovered: $TODAY — reset $TOTAL_SKILLS skills from outage-contaminated metrics" \
  > "$MARKER_DIR/.cron-recovered-$TODAY"

echo "Cron-state reset complete. $TOTAL_SKILLS skills restored to clean baseline."
