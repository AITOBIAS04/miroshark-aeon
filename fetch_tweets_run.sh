#!/bin/bash
set -e

FROM_DATE=$(date -u -d "7 days ago" +%Y-%m-%d 2>/dev/null || date -u -v-7d +%Y-%m-%d)
TO_DATE=$(date -u +%Y-%m-%d)
echo "Date range: $FROM_DATE to $TO_DATE"

SEARCH_PROMPT="Search for recent tweets about the MIROSHARK crypto token on Base chain (contract 0xd7bc6a05a56655fb2052f742b012d1dfd66e1ba3) AND the MiroShark open-source multi-agent simulation project at github.com/aaronjmars/MiroShark. Only return tweets about these two topics from the last 7 days. Prioritize the most interesting, insightful, or highly-engaged posts. For each tweet include: the handle, the full text, date posted, engagement (likes/retweets if available), and the direct link (https://x.com/handle/status/ID). Return as a numbered list. Date range: ${FROM_DATE} to ${TO_DATE}. Return 10 tweets."

PAYLOAD=$(jq -n \
  --arg prompt "$SEARCH_PROMPT" \
  '{
    model: "grok-3-fast-beta",
    input: [{"role": "user", "content": $prompt}],
    tools: [{"type": "x_search"}]
  }')

RESPONSE=$(curl -s -X POST "https://api.x.ai/v1/responses" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $XAI_API_KEY" \
  -d "$PAYLOAD")

echo "=== RAW RESPONSE ==="
echo "$RESPONSE" | head -c 2000

echo ""
echo "=== PARSED TEXT ==="
echo "$RESPONSE" | jq -r '.output[] | select(.type == "message") | .content[] | select(.type == "output_text") | .text' 2>/dev/null || echo "jq parse failed"
