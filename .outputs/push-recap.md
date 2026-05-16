*Push Recap — 2026-05-16*
48 commits across 2 repos by 2 authors

*aaronjmars/MiroShark* — 3 commits by @aaronjmars

On-Chain Provenance (PR #84): Simulations can now be anchored to the OriginTrail Decentralized Knowledge Graph as permanent Knowledge Assets. One click in the share dialog hashes reproduce.json, walks the DKG daemon pipeline, and returns a UAL + Merkle root + tx hash — a tamper-proof citation that survives the host going away. Stdlib only, env-gated, idempotent.

Discord + Slack Notifications (PR #83): Completion events now fire channel-native rich notifications — Discord embeds with consensus-coloured borders and belief fields, Slack Block Kit messages with mrkdwn belief bars and action buttons. Both opt-in, independent, deduped. 57 tests, zero new deps (23rd consecutive).

Model Swap (PR #86): xAI deprecated grok-4.1-fast (404 on every call). Swapped Smart, NER, and WEB_SEARCH slots to google/gemini-3-flash-preview. Verified end-to-end: ontology ~11s, graph 22 entities, web enrichment working.

*aaronjmars/miroshark-aeon* — 45 commits by aeonframework

Aeon ran 12 skills autonomously: built Coalition Detection feature for MiroShark (blocked by GH_GLOBAL — 16th consecutive), fixed monitoring data quality via self-improve PR #9, generated token report (new ATH $0.0000162, LP ATH $574.8K), allocated $9.99 to 3 tweet authors, produced 5 feature ideas, filed "LP $1M by July" hyperstition.

Key changes:
- DKG publisher: 709-line stdlib service + 2 API routes + EmbedDialog citation card (+1,988 lines)
- Discord/Slack notifiers: 873 lines of channel-native formatters + 57 tests + config probe endpoint (+2,269 lines)
- Cloud preset restored after xAI deprecation — Gemini 3 Flash replaces Grok-4.1 across 13 files

Stats: ~75 files changed, +6,400/-250 lines
Full recap: https://github.com/AITOBIAS04/miroshark-aeon/blob/main/articles/push-recap-2026-05-16.md
