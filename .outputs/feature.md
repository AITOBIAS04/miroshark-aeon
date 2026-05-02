Feature Built — 2026-05-02

Jupyter Notebook Export
MiroShark simulations can now be exported as runnable Jupyter notebooks. One click downloads a complete .ipynb file with all simulation data pre-loaded and six analysis sections ready to execute — belief drift charts, individual agent trajectories, an interaction network graph, engagement plots, and summary statistics. Open in Jupyter, Google Colab, or VS Code and run all cells.

Why this matters:
Until now, MiroShark's transcript and trajectory exports gave researchers data in raw form — Markdown for reading, CSV for spreadsheets. But a researcher who wants to run a t-test on belief drift, compute network centrality from the interaction graph, or produce publication-ready figures had to write all the analysis code from scratch. This was the #1 idea from repo-actions and closes the last mile between "I ran a simulation" and "I can publish this." Academic users can now export to a notebook and cite the methodology directly. OASIS and AgentSim produce analysis-ready artifacts; MiroShark now does too.

What was built:
- backend/app/services/notebook_export.py: New pure-stdlib service that builds an nbformat-4 Jupyter notebook from trajectory.json, agent profiles, and the post SQLite databases. Data is encoded as base64 for safe embedding — no injection risks from post content containing special characters.
- backend/app/api/simulation.py: New GET /<id>/notebook.ipynb endpoint that reads on-disk artifacts and serves the generated .ipynb as an attachment download.
- frontend/src/components/Step4Report.vue: "Notebook" export button with a Jupyter-orange accent, placed alongside the existing JSON/CSV export buttons in the simulation results toolbar.
- frontend/src/components/EmbedDialog.vue: Download section in the share/embed panel with a description and one-click download link.
- frontend/src/api/simulation.js: exportNotebook() function for the Step4 button + getNotebookUrl() helper for the embed dialog.

How it works:
The backend reads trajectory.json (per-round belief snapshots), reddit_profiles.json (agent metadata), and the Twitter/Reddit SQLite databases (post content and reply chains). It flattens trajectory data into a per-agent-per-round DataFrame with columns for round, agent_id, avg_position, and stance. All data is serialized as base64-encoded JSON and embedded directly in the notebook cells — this avoids any escaping issues with post content. The notebook has six sections: (1) setup and data loading, (2) stacked area chart of bullish/neutral/bearish % per round, (3) individual agent belief trajectory lines, (4) a networkx directed graph of reply interactions with degree centrality sizing, (5) summary statistics with stance volatility and change detection, and (6) post volume and engagement bar charts per round.

What's next:
Could add Google Colab one-click open (a URL that auto-loads the .ipynb from a gist or signed URL), or a pre-computed statistical summary cell with p-values for stance convergence.

Note: Code complete. Push to aaronjmars/MiroShark blocked — GH_GLOBAL token not configured.
