*Feature Built — 2026-05-31*

Real-Time Simulation Progress via SSE

MiroShark simulations now push live progress to the browser. Instead of the old 2-second polling loop, the simulation runner writes events to a progress file as each round starts, completes, and as agents take notable actions — and a new Server-Sent Events endpoint streams those events directly to any connected client. The simulation page opens an EventSource on launch and shows a live activity feed: agent names, stance types, and platform badges flow in round by round, fading in with smooth CSS transitions.

Why this matters:
Until now, watching a running simulation meant polling two REST endpoints every 2–3 seconds and seeing numbers increment in batches. A 15-round, 30-agent simulation took several minutes, and the entire time the UI looked like a loading bar that updated in jumps. SSE replaces that with a push stream: the moment an agent posts on Twitter, the feed shows their name and action type. The moment a round completes on Reddit, the progress ticks up. The simulation feels alive — you watch agents act in real time instead of watching a number go up. This was idea #1 from yesterday's repo-actions (2026-05-30), selected as the highest-impact small-effort build: it transforms the creation experience rather than adding another post-hoc analytical surface.

What was built:
- backend/app/services/sse_progress_service.py: Pure-stdlib service that writes progress events to progress_events.jsonl and provides a file-tailing SSE generator with 15-second keepalive pings and 5-minute inactivity timeout
- backend/app/services/simulation_runner.py: Modified to emit round_start, round_complete, agent_action (for posts, comments, quotes, trades), platform_complete, simulation_complete, and simulation_error events during the monitor loop
- backend/app/api/simulation.py: New GET /api/simulation/<id>/events SSE endpoint with X-Accel-Buffering: no header for Cloud Run proxy compatibility
- frontend/src/components/Step3Simulation.vue: EventSource connection on simulation start/resume; live activity feed strip with TransitionGroup animations showing platform labels, agent names, and action badges; auto-cleanup on unmount; graceful fallback to existing polling on connection failure
- 12 unit tests, OpenAPI spec entry, bilingual docs (API.md + FEATURES.md, English + Chinese)

How it works:
The simulation runner already monitors per-platform actions.jsonl files every 2 seconds in a background thread. When it detects a round_start, round_end, or simulation_end event (or a high-signal agent action like CREATE_POST), it now also appends a progress event to progress_events.jsonl via the SSE service. The SSE endpoint opens that file, streams all existing lines immediately (so clients connecting mid-run catch up), then enters a 0.5-second tail-follow loop watching for new lines — the same pattern used by the existing observability SSE endpoint. Flask's native stream_with_context + Response(mimetype='text/event-stream') handles the long-lived connection. On the frontend, EventSource is native in every modern browser — zero new npm dependencies. The live feed keeps a sliding window of the 5 most recent entries with Vue's TransitionGroup providing enter/leave animations.

What's next:
The live feed currently shows text-only entries. Future iterations could include belief-position indicators (bullish/bearish chips) per agent action, a mini-chart that updates in real time, or a full-screen live mode designed for projection during workshops.

Push blocked — GH_GLOBAL secret not set (27th consecutive block). Local commit 805b4c9 on branch feat/sse-progress.
