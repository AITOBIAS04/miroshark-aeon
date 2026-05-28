Feature Built — 2026-05-28

Agent Interaction Graph Export (GraphML)
MiroShark simulations now have a one-click GraphML export for the agent interaction network. Researchers can download the full directed graph — every agent as a node, every like/repost/quote/comment/follow as a weighted edge — and open it directly in Gephi, load it in NetworkX with one line of code, or import it into Cytoscape. Node attributes include stance, platform, degree centrality. Edge attributes include interaction weight and cross-platform flags.

Why this matters:
The interaction network visualized in the browser was one of MiroShark's most distinctive outputs, but until now it was trapped there. A network scientist who wanted to run PageRank, betweenness centrality, community detection (Louvain), or temporal graph analysis had to parse actions.jsonl manually and reconstruct the graph themselves. GraphML is the lingua franca of graph analysis tools — Gephi, NetworkX, Cytoscape, igraph all read it natively. This was the #2 idea from the May 24 repo-actions analysis and completes the researcher export stack alongside trajectory CSV, BibTeX citation, reproduce.json, and Jupyter notebook.

What was built:
- backend/app/services/graphml_export.py: Pure-stdlib GraphML 1.1 renderer using xml.etree.ElementTree. Parses twitter/reddit/polymarket action logs into directed graph. 7 node attributes (name, platform, platforms, stance, actions, in_degree, out_degree) and 3 edge attributes (weight, types, is_cross_platform). Same ±0.2 stance threshold as every other surface.
- backend/app/api/simulation.py: GET /api/simulation/<id>/network.graphml endpoint with publish gate, Content-Disposition attachment header, 5-minute cache, surface stat tracking.
- frontend/src/components/EmbedDialog.vue: New GraphML section with download button, copyable URL, and nx.read_graphml() quickstart snippet. Bilingual (EN/ZH).
- backend/app/services/archive_service.py: network.graphml included in the archive ZIP bundle alongside all other surfaces.
- backend/tests/test_unit_graphml_export.py: 24 unit tests covering data parsing, XML structure validation, stance mapping, cross-platform detection, empty/corrupt data handling, and static wiring guards.
- backend/openapi.yaml + docs/FEATURES.md: Full API documentation and feature writeup.

How it works:
The service reads the same action JSONL logs (twitter, reddit, polymarket) that power the browser visualization. It builds a directed graph where each agent is a node and each interaction event (like, repost, quote, comment, follow) creates or increments a weighted edge from the acting agent to the target. Self-interactions are filtered out. Stance is read from the last trajectory snapshot using the same ±0.2 threshold every other surface uses. The graph is serialized to GraphML 1.1 XML with full key declarations using Python's built-in xml.etree.ElementTree — zero new dependencies. The archive bundle service wraps it alongside the other 9 surfaces so a single ZIP download contains everything a researcher needs.

What's next:
Could add GEXF format support (Gephi's native dynamic graph format with temporal edges), or a DOT export for Graphviz rendering. The cross-platform edge flag enables multi-layer network analysis once more platforms are added.

Push blocked — GH_GLOBAL secret not set. Feature is code-complete on local branch feat/graphml-interaction-export (25th consecutive local build).
