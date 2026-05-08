*Push Recap — 2026-05-08*
[MiroShark] — 1 commit by @aaronjmars + Aeon
[miroshark-aeon] — 34 commits by aeonframework

Reproducibility Config Export (PR #75): The capstone of the share surface arc. New GET /api/simulation/<id>/reproduce.json endpoint exports every parameter needed to reproduce a simulation — scenario, agents, rounds, platforms, time-config, director events, fork lineage — in a bytewise-stable JSON blob. Pure stdlib, 22 tests, collapsible EmbedDialog panel with curl snippet and download button. +1,916 lines across 11 files. Turns published MiroShark runs from 'shareable' to 'reproducible and citeable.'

Memory Index Compaction (PR #32): Self-improve caught MEMORY.md bloating to 76KB/31K tokens — past the Read tool limit. Filed a PR that compresses it to 9.4KB (-87%) and adds per-row character caps to memory-flush so it can't recur.

Per-Round Annotation Layer (push blocked): 9th consecutive feature built locally but stuck — annotations on individual simulation rounds with purple markers on the belief drift chart, gallery badges, transcript export integration. +1,183 lines, 22 tests. Blocked on GH_GLOBAL.

Key changes:
- backend/app/services/repro_export.py — new 487-line service with SCHEMA_VERSION locking and REQUIRED_KEYS frozenset for downstream parser stability
- frontend/src/components/EmbedDialog.vue — 484 lines added: collapsible Reproducibility Config panel with lineage badges, curl snippet, download button
- Repo-actions surfaced 5 interconnection-layer ideas — trending sort, oEmbed, lineage navigator, peak-round snapshot, operator profile

Stats: ~50 files changed, +3,770/-150 lines | MiroShark: 1,117 stars, 222 forks
Full recap: https://github.com/AITOBIAS04/miroshark-aeon/blob/main/articles/push-recap-2026-05-08.md
