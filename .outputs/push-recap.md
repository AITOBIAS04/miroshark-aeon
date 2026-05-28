*Push Recap — 2026-05-28*
aaronjmars/MiroShark — 4 commits by 3 authors
aaronjmars/miroshark-aeon — PR #48 + housekeeping

Webhook Event Filtering (24th surface): PR #120 adds WEBHOOK_EVENTS, an optional allow-list that filters outbound webhooks before dispatch. Three token categories — direction (bullish/neutral/bearish), confidence (high/medium at 75%/50% thresholds), quality (excellent/good) — combine OR within categories, AND across them. Failed sims always bypass the filter. Integrators in ECOSYSTEM.md can now subscribe to only the slice of the simulation stream they care about. 237 lines of filtering logic + 454 lines of tests, zero new deps.

Community Ecosystem Growth: Noelclaw (PR #117) joins ECOSYSTEM.md as the 11th listed project — X handle, website, and MCP integration. 6th external contributor toward the August target of 10.

README Overhaul: PRs #118/#119 condensed every feature-table row from paragraph to one-liner, moved Use Cases above Features for narrative flow, and added 3 new diagrams (simulate-anything hero banner, agent grounding layers, graph memory pipeline).

Token Report Spam Filter: PR #48 (miroshark-aeon) tightened the Grok query so zero-engagement contract-drop spam stops landing in the Social Pulse section. Three explicit pre-filters before Grok picks results: zero-likes+zero-RT, contract-drop templates and clone domains, duplicate-template spam. Tomorrow's 06:00 UTC run validates.

Key changes:
- WEBHOOK_EVENTS dispatch filter — source-side subscription for 10+ integrators (24th share surface)
- README condensed to one-liner feature table + 3 architectural diagrams
- Grok spam filter eliminates scam contract drops from daily token report

Stats: ~17 files changed, +1,065/-49 lines
Full recap: https://github.com/AITOBIAS04/CHORUS/blob/main/articles/push-recap-2026-05-28.md
