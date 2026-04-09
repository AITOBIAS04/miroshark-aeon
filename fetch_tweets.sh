#!/bin/bash
FROM_DATE=$(date -u -d "7 days ago" +%Y-%m-%d 2>/dev/null || date -u -v-7d +%Y-%m-%d)
TO_DATE=$(date -u +%Y-%m-%d)

SEARCH_CONTENT="Find tweets about the \$MIROSHARK crypto token on Base chain (contract 0xd7bc6a05a56655fb2052f742b012d1dfd66e1ba3) AND/OR the MiroShark GitHub project at https://github.com/aaronjmars/MiroShark (a multi-agent simulation engine). Only return tweets genuinely about MIROSHARK cryptocurrency or the MiroShark open-source simulation project. Date range: ${FROM_DATE} to ${TO_DATE}. Return 10 tweets, prioritizing most interesting, insightful, or highly-engaged posts. For each tweet include: handle in x.com/handle format, full text, date posted, engagement stats (likes/retweets if available), and direct link as https://x.com/handle/status/ID. Return as a numbered list."

FULL_PAYLOAD=$(jq -n --arg content "$SEARCH_CONTENT" '{
  "model": "grok-3-fast",
  "input": [{"role": "user", "content": $content}],
  "tools": [{"type": "x_search"}]
}')

RESPONSE=$(curl -s -X POST "https://api.x.ai/v1/responses" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $XAI_API_KEY" \
  -d "$FULL_PAYLOAD")

TWEETS=$(echo "$RESPONSE" | jq -r '.output[] | select(.type == "message") | .content[] | select(.type == "output_text") | .text' 2>/dev/null)

if [ -z "$TWEETS" ]; then
  echo "EMPTY_OR_ERROR"
  echo "$RESPONSE" | head -c 1000
else
  echo "$TWEETS"
fi
