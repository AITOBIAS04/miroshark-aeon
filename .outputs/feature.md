*Feature Built — 2026-05-30*

Operator Dashboard (All My Simulations)
MiroShark operators now have a dedicated command center at /my-simulations. Enter your admin token once and see every simulation on the deployment — published, private, running, or failed — in one sortable, filterable table with per-sim metadata and aggregate statistics. No more scrolling through the public gallery or remembering simulation IDs.

Why this matters:
Until now, operators who ran 30+ simulations over weeks had no inventory view of their own work. The public gallery only shows published runs, the History Database is a flat chronological list without status filtering or aggregate stats, and finding 'the 8-agent sim I ran two weeks ago on the ECB decision' required bookmarks or memory. This was idea #4 from repo-actions and directly addresses the blind spot operators hit when using MiroShark as a recurring production tool rather than a one-off research toy.

What was built:
- backend/app/services/operator_dashboard_service.py: Pure-stdlib scanner that reads state.json, simulation_config.json, confidence.json, and surface-stats.json for every sim directory. Returns enriched cards sorted by last-modified, plus aggregate stats (counts, avg confidence, most-embedded sim, highest-confidence sim).
- backend/app/api/operator.py: Flask blueprint with two admin-gated routes — GET /api/operator/simulations returns the full sim list with status counts, GET /api/operator/stats returns aggregate analytics. Both require Authorization: Bearer $MIROSHARK_ADMIN_TOKEN.
- frontend/src/views/OperatorDashboardView.vue: Full-page dashboard with auth gate (token stored in localStorage), 4 stat cards (Total/Published/Private/Running), status filter tabs, sort dropdown (Last Modified/Created/Confidence/Embed Hits), and a sortable simulation table with color-coded status chips, confidence badges, relative timestamps, and click-to-navigate.
- 12 unit tests, OpenAPI spec (Operator tag + schemas), API + FEATURES docs, /my-simulations route, Dashboard nav link.

How it works:
The dashboard scans every simulation directory on disk (not just public ones), reading the same artifact files the gallery card builder uses — state.json for status, simulation_config.json for scenario/rounds/model, confidence.json for trust score, surface-stats.json for embed hit counts. The frontend stores the admin token in localStorage after validation and sends it as a Bearer header on each dashboard request. Status tabs filter in real-time; sorting works across four dimensions. The auth gate validates the token by calling the stats endpoint — a successful response unlocks the view, a 401 shows an inline error.

What's next:
Could add per-sim action buttons (publish/unpublish, delete), a search bar over scenarios, or export the full sim inventory as CSV for external analysis.

Push blocked — GH_GLOBAL secret not set (26th consecutive block)
