import urllib.request
import urllib.error
import json
import os
import sys

api_key = os.environ.get("XAI_API_KEY", "")
if not api_key:
    print("ERROR: XAI_API_KEY not set")
    sys.exit(1)

payload = {
    "model": "grok-3-fast",
    "input": [
        {
            "role": "user",
            "content": (
                "Find tweets about MIROSHARK crypto token on Base chain "
                "(contract 0xd7bc6a05a56655fb2052f742b012d1dfd66e1ba3) and/or the MiroShark GitHub project "
                "https://github.com/aaronjmars/MiroShark (a multi-agent simulation engine). "
                "Only return tweets genuinely about MIROSHARK cryptocurrency or the MiroShark open-source simulation project. "
                "Date range: 2026-04-02 to 2026-04-09. "
                "Return up to 10 tweets, prioritizing most interesting or highly-engaged posts. "
                "For each tweet include: handle in x.com/handle format, full text, date posted, "
                "engagement stats (likes/retweets), and direct link as https://x.com/handle/status/ID. "
                "Return as a numbered list."
            )
        }
    ],
    "tools": [{"type": "x_search"}]
}

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://api.x.ai/v1/responses",
    data=data,
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=120) as resp:
        body = resp.read().decode("utf-8")
    print("HTTP 200 OK", file=sys.stderr)
except urllib.error.HTTPError as e:
    body = e.read().decode("utf-8")
    print(f"HTTP Error {e.code}: {e.reason}", file=sys.stderr)

with open("/tmp/grok_response.json", "w") as f:
    f.write(body)

print(f"Response saved ({len(body)} bytes)", file=sys.stderr)

try:
    parsed = json.loads(body)
    found = False
    for item in parsed.get("output", []):
        if item.get("type") == "message":
            for part in item.get("content", []):
                if part.get("type") == "output_text":
                    found = True
                    print(part.get("text", ""))
    if not found:
        print("No output_text found in response.", file=sys.stderr)
        print("Raw response (first 3000 chars):", file=sys.stderr)
        print(body[:3000], file=sys.stderr)
except Exception as ex:
    print(f"Parse error: {ex}", file=sys.stderr)
    print(body[:3000], file=sys.stderr)
