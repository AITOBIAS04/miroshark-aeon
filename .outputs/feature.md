*Feature Built — 2026-05-14*

Inbound Launch Webhook
MiroShark can now be triggered by external systems. A new authenticated endpoint — POST /api/webhooks/launch-simulation — lets Zapier workflows, n8n automations, GitHub Actions jobs, cron scripts, or any custom tooling start a simulation remotely without opening a browser. The caller signs the request body with a shared secret using HMAC-SHA256 (the same scheme the outbound completion webhook uses, reversed), and MiroShark returns a 202 with the watch URL, SSE event stream URL, and whether a completion callback will fire.

Why this matters:
The completion webhook (PR #46) and HMAC verification (PR #79) let MiroShark call out when a simulation finishes. But the automation loop only went one direction — external systems could react to completed sims but had no way to start them. A trading-signal operator watching Reddit for volatility spikes had no programmatic way to trigger "simulate how the community reacts to this." The inbound webhook is the missing half. Now the full cycle works: external event → trigger simulation → monitor via SSE → receive completion callback. For the n8n/Zapier/GitHub Actions audience who already built outbound integrations, this is the inbound counterpart they need.

What was built:
- backend/app/services/launch_webhook_service.py: HMAC-SHA256 request verification using the existing verify_signature helper. Late-binding secret resolution from Config.LAUNCH_WEBHOOK_SECRET. Cryptographic secret generation (64 hex chars).
- backend/app/api/launch_webhook.py: POST /api/webhooks/launch-simulation route. Verifies signature, validates simulation_id/platform/max_rounds/force params, checks simulation state, delegates to existing SimulationRunner.start_simulation. Returns 202 with sim_id, watch_url, events_url, completion_webhook_will_fire.
- backend/app/api/settings.py: POST /api/settings/generate-launch-secret endpoint. Settings snapshot now exposes launch_webhook.configured/has_secret/endpoint.
- frontend/src/components/SettingsPanel.vue: New "Launch Webhook" section with endpoint display, secret Generate/Regenerate button, and collapsible usage examples (curl, GitHub Actions, Python).
- backend/tests/test_unit_launch_webhook.py: 22 unit tests covering HMAC verification, request validation, simulation state checks, settings endpoints, and drift guards.
- OpenAPI spec: LaunchWebhookRequest/LaunchWebhookResponse schemas, new Webhooks tag.
- Docs: WEBHOOKS.md + zh-CN — full "Inbound — Launch Trigger" section with schema, auth, error codes, end-to-end example, signing snippets (Python, Node.js, GitHub Actions, curl). FEATURES.md + zh-CN, API.md + zh-CN, README.md (EN + zh-CN), .env.example.

How it works:
The endpoint reads the raw request body and X-MiroShark-Signature header, verifies the HMAC-SHA256 digest against LAUNCH_WEBHOOK_SECRET using constant-time comparison (hmac.compare_digest), then parses the JSON body. It validates the simulation_id exists and is in READY state (or can be force-restarted), then delegates to the same SimulationRunner.start_simulation code path the browser UI uses. The response includes absolute URLs when PUBLIC_BASE_URL is set, and completion_webhook_will_fire reflects whether the outbound WEBHOOK_URL is configured — so the caller knows the full loop will close. The secret is configurable via .env, the Settings modal, or the generate-launch-secret API endpoint.

What's next:
Could extend the webhook to accept full creation params (scenario, n_agents, model) for end-to-end sim launch from a single POST — but the current design of wrapping the existing start endpoint is the most reliable first step. The remaining repo-actions candidates: Agent Conversation Thread View, Multi-Model Race Mode, Research Export Bundle.

PR: push blocked — GH_GLOBAL secret not set (14th consecutive local commit)
