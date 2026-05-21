*Feature Built — 2026-05-21*

Agent Journey View
MiroShark simulations now have a "detective mode" for individual agents. Instead of reading aggregate charts or scanning through entire conversation threads, you can select any agent and see their complete story: how their stance evolved round by round, what they posted, who influenced them (with post excerpts), and which other agents they swayed. Stance-flip moments get highlighted so you can instantly find the turning point in any agent's arc.

Why this matters:
Until now, answering "why did this Risk Manager flip from NO to YES in round 7?" required cross-referencing three panels — the belief drift chart, the interaction network, and the thread view. The Agent Journey View reconstructs that arc as a single vertical timeline. For researchers studying persuasion dynamics, this is the character-arc layer that makes individual narrative shifts legible. For anyone using MiroShark to illustrate how opinions change, the journey is the story you can quote from. This was the #1 ranked idea from yesterday's repo-actions analysis.

What was built:
- backend/app/services/agent_journey.py: Pure-stdlib service (366 LoC) that computes per-round stance arc, posts, influenced-by (top 3 per round with 80-char post excerpts), and influenced (with old→new stance transitions). Uses the same ±0.2 stance threshold as every other surface. Results cached per agent in agent_journey_cache/.
- backend/app/api/simulation.py: GET /agent-journey?agent_name endpoint. Without agent_name, returns the list of available agents (for the picker). With agent_name, returns the full journey. Path-traversal-safe caching.
- frontend/src/components/AgentJourneyView.vue: 610-line Vue component — searchable agent picker, vertical timeline with round cards, stance badges (bullish/neutral/bearish colors), belief values, post text with expand/collapse, influenced-by with clickable agent names, influenced with stance-shift dot indicators, flip-moment orange highlights, mini SVG sparkline header. Clicking any agent name in the influence list navigates to that agent's journey.
- frontend/src/components/InteractionNetwork.vue: "View journey →" link added to node tooltip — click any agent in the network graph to open their journey directly.
- 22 unit tests covering stance classification, archetype detection, journey structure, stance tracking, post truncation, influence capping, edge cases.

How it works:
The service reads three data sources per simulation: trajectory.json (belief positions per round per agent), profiles.json (agent ID↔name mapping + archetype), and platform action logs (twitter/reddit/polymarket actions.jsonl). For each round, it looks up the target agent's belief value, classifies their stance, finds their posts, identifies who they engaged with (influenced_by — likes, reposts, quotes, comments on others' content), and who engaged with them (influenced — with stance transition tracking). The timeline is assembled once and cached as immutable JSON per agent.

What's next:
Could extend with a "compare two agents" overlay, or integrate journey data into the article generator for richer narrative construction around flip moments.

PR: Push blocked — GH_GLOBAL secret not set (20th consecutive build). Feature is code-complete on local branch feat/agent-journey-view.
