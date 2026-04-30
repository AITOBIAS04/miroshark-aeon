Feature Built — 2026-04-30

Atom Feed for Completed Simulations (/feed.xml)

MiroShark now publishes an Atom (RFC 4287) feed at /feed.xml listing the last 20 completed simulations. Teams subscribe via Feedly, n8n, Zapier, Slack RSS app, or any standard feed reader and get notified whenever a simulation completes — zero config, zero new dependencies.

Why it matters: Every other output surface (share cards, transcripts, embeds) requires someone to visit the app. The feed flips it — simulations come to you. Wire it into n8n → Discord and your channel gets a post every time a sim finishes. Subscribe in Feedly and browse results over coffee. It's the missing push layer for teams that run MiroShark unattended.

What was built:
• backend/app/api/feed.py — New Flask blueprint, stdlib XML, zero deps
• backend/app/__init__.py + api/__init__.py — Blueprint registration
• frontend/index.html — <link rel="alternate"> feed autodiscovery
• frontend/src/views/Home.vue — RSS icon in navbar
• frontend/src/components/HistoryDatabase.vue — Subscribe button (copies feed URL)
• frontend/vite.config.js — Dev proxy for /feed.xml
• backend/openapi.yaml — Endpoint documentation
• README.md — New Integrations section + Features table row
• docs/FEATURES.md — Full feature documentation

How it works: GET /feed.xml returns valid Atom XML. Each entry carries the scenario text, agent count, round count, total events, quality data, and a direct link. Public sims link to /share/<id>; private ones link to the internal view. 60s cache header keeps feed readers from hammering the endpoint.

Branch: feat/atom-feed (commit 1a78a0f)
Status: Code complete — push blocked (GH_GLOBAL secret not set; GITHUB_TOKEN lacks cross-repo push). PR will be created once the secret is available.
