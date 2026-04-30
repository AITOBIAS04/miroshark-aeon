#!/usr/bin/env bash
# Pre-flight health guard — detects systemic skill failures from cron-state.json
# and surfaces ::warning:: annotations in GitHub Actions UI.
#
# Runs before Claude starts, so it works even when auth is broken.
# Does NOT send notifications (no access to notification secrets in prefetch step).
# Instead, it creates ::warning:: and ::error:: annotations visible in the workflow UI.
set -euo pipefail

SKILL="${1:-}"
STATE_FILE="memory/cron-state.json"

[ ! -f "$STATE_FILE" ] || ! jq empty "$STATE_FILE" 2>/dev/null && exit 0

TOTAL=$(jq 'length' "$STATE_FILE")
[ "$TOTAL" -eq 0 ] && exit 0

FAILING=$(jq '[to_entries[] | select(.value.consecutive_failures >= 10)] | length' "$STATE_FILE")
THRESHOLD=$(( (TOTAL * 80 + 99) / 100 ))

if [ "$FAILING" -ge "$THRESHOLD" ]; then
  LAST_SUCCESS=$(jq -r '
    [to_entries[] | .value.last_success // null | select(. != null)] |
    sort | last // "unknown"
  ' "$STATE_FILE")

  SAMPLE_ERROR=$(jq -r '
    [to_entries[] | select(.value.last_error != null) | .value.last_error][0] // "no error captured"
  ' "$STATE_FILE" | head -c 150)

  MAX_CONSEC=$(jq '[to_entries[] | .value.consecutive_failures // 0] | max' "$STATE_FILE")

  echo "::error::HEALTH GUARD: Systemic failure — ${FAILING}/${TOTAL} skills have 10+ consecutive failures (max: ${MAX_CONSEC}). Last success: ${LAST_SUCCESS}. Check ANTHROPIC_API_KEY / CLAUDE_CODE_OAUTH_TOKEN in repo secrets."
  echo "::warning::Health guard sample error: ${SAMPLE_ERROR}"

  echo "health-guard: SYSTEMIC FAILURE DETECTED"
  echo "  Failing skills: ${FAILING}/${TOTAL}"
  echo "  Max consecutive failures: ${MAX_CONSEC}"
  echo "  Last successful run: ${LAST_SUCCESS}"
  echo "  Current skill: ${SKILL}"
  echo "  Likely cause: auth token expired or missing"
  echo "  Fix: Settings → Secrets and variables → Actions → Update ANTHROPIC_API_KEY or CLAUDE_CODE_OAUTH_TOKEN"
fi
