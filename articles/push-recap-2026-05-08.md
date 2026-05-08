# Push Recap — 2026-05-08

## Overview
35 commits across 2 repos by 2 authors (@aaronjmars, aeonframework). The main thrust today was closing the reproducibility gap in MiroShark's share surface stack: PR #75 shipped a complete machine-readable export of every simulation parameter, turning published runs into citeable, reproducible research artifacts. On the harness side, the self-improve skill caught a critical memory bloat and filed a fix, while the daily skill cycle ran green across the board.

**Stats:** ~50 files changed, +3,770/-150 lines across 35 commits

---

## aaronjmars/MiroShark

### New Feature: Reproducibility Config Export (PR #75)
**Summary:** This is the capstone of the share surface multiplication arc. Six of MiroShark's ten share surfaces already made finished simulations citable (transcript, trajectory, thread, watch, GIF, share card), but none carried the parameters needed to actually reproduce the run. PR #75 closes that gap with a single JSON endpoint that exports every parameter — scenario text, agent count, rounds, platform toggles, time-config knobs, director events, and fork/counterfactual lineage — in a bytewise-stable, citation-hash-friendly format.

**Commits:**
- `92acb3d` — feat: reproducibility config export — citation primitive for share surfaces (#75)
  - New file `backend/app/services/repro_export.py` (+487 lines): Pure-stdlib service (json + os only, zero new dependencies). Composes the reproduction blob from `state.to_dict()`, `simulation_config.json`, and sim directory artifacts (counterfactual injection, director events in both JSONL and JSON formats). Key design choices: `SCHEMA_VERSION` constant locks the schema for downstream parsers, `REQUIRED_KEYS` frozenset pins every field so future refactors can't silently drop one, corrupt artifacts degrade to `null` instead of 500ing the export, `_safe_int()` and `_safe_str()` coerce hand-edited configs gracefully.
  - New file `backend/tests/test_unit_repro_export.py` (+480 lines): 22 offline unit tests covering schema invariants, scenario fallback paths, total_rounds derivation, lineage shapes (original/fork/counterfactual), corrupt-file degradation, director-events parsing across both storage formats, render bytes stability, and route + OpenAPI drift guards.
  - Changed `backend/app/api/simulation.py` (+108 lines): New `GET /<id>/reproduce.json` route behind the same publish gate as every other share surface. Pretty-printed output (indent=2, sort_keys=True) so curl exports are diff-friendly. 5-minute Cache-Control (longer than trajectory CSV's 60s because the blob is immutable once the sim reaches terminal state). Bilingual error messages (EN + zh-CN).
  - Changed `backend/openapi.yaml` (+249 lines): Full `ReproductionConfig` schema under components with per-field documentation. New path entry under "Publish & Embed" tag. Schema version enum, lineage sub-object, platforms sub-object, time_config sub-object all fully specified.
  - Changed `frontend/src/components/EmbedDialog.vue` (+484 lines): Collapsible "Reproducibility config" panel with microscope icon. Summary grid showing schema version, agents, rounds, active platforms, director event count, and lineage badge (Forked/Counterfactual with parent-id tooltip). Copy-ready curl snippet, Download reproduce.json button, Copy URL button, Refresh button. Resets on dialog open and on isPublic flip. Fully bilingual (EN + zh-CN).
  - Changed `frontend/src/api/simulation.js` (+44 lines): `getReproductionUrl()` and `getReproduction()` API helpers.
  - Changed `docs/FEATURES.md` (+30 lines), `docs/FEATURES.zh-CN.md` (+30 lines): Feature section between Surface Usage Analytics and Webhook Delivery Log.
  - Changed `docs/API.md` (+1 line), `docs/API.zh-CN.md` (+1 line): Endpoint documentation.
  - Changed `README.md` (+2 lines): Feature row added.

**Impact:** Researchers, quant analysts, and anyone citing a MiroShark simulation now have a one-click download of every parameter that shapes the run. The bytewise-stable output means the file hash itself serves as a citation key — two downloads of the same finished simulation produce identical files. This completes the arc from "shareable" to "reproducible" and positions MiroShark for academic citation workflows. The lineage block also enables future UI features (the lineage navigator from today's repo-actions batch) by putting fork/counterfactual parentage in a machine-readable format on disk.

---

## aaronjmars/miroshark-aeon

### Self-Improvement: Memory Index Compaction (PR #32)
**Summary:** The self-improve skill detected that `MEMORY.md` had bloated to 76 KB / 31K+ tokens — well past Claude's Read tool limit — because Skills Built and Recent Articles rows had grown into 5K+ character paragraphs. It filed PR #32 to compress the file to 9.4 KB (-87%) and add per-row character caps to the memory-flush skill so the bloat can't recur.

**Commits:**
- `aaefbe9` — chore(cron): self-improve success
  - Changed `memory/cron-state.json`: Updated self-improve to 14 runs / 14 successes, 100% success rate.
- PR #32 (open): `improve/project-lens-dedup` branch
  - Changed `skills/memory-flush/SKILL.md`: New step 5 enforcing per-row character caps on every flush (Skills Built <= 280 chars, Recent Articles <= 220, Recent Digests <= 180). Post-flush `wc -c` sanity check targets < 25 KB.
  - Changed `memory/MEMORY.md`: Condensed every row to a one-sentence summary plus PR number. Full descriptions preserved in daily logs and article files. File dropped from 76 KB to 9.4 KB.

**Impact:** Every Aeon skill reads MEMORY.md at task start. At 76 KB the file was hitting Read limits and burning context tokens. The fix restores reliable memory access and prevents future bloat via structural caps in the flush procedure.

### Per-Round Annotation Layer (Feature, Push Blocked)
**Summary:** The feature skill built a complete per-round annotation system for MiroShark simulations — the 9th consecutive feature built locally but blocked from push because GH_GLOBAL is not set. Annotations let researchers mark specific rounds with notes (e.g., "belief shift triggered here", "consensus formed at this point").

**Commits:**
- `3d0dab0` — chore(feature): auto-commit 2026-05-08
  - Built on `feat/per-round-annotations` branch (local commit `24ba8ce`):
    - New `backend/app/services/annotations.py`: CRUD service for round-level annotations
    - New `frontend/src/components/AnnotationPanel.vue`: Panel below belief drift chart
    - New `backend/tests/test_unit_annotations.py`: 22 unit tests
    - Modified `backend/app/api/simulation.py`: 3 annotation routes (GET/POST/DELETE) + annotated flag on gallery cards
    - Modified `frontend/src/components/BeliefDriftChart.vue`: Purple dashed annotation markers on chart
    - Modified `backend/openapi.yaml`: RoundAnnotation schema + 3 endpoints
    - +1,183 lines across 14 files

**Impact:** Adds a qualitative data layer to MiroShark's quantitative belief tracking. Researchers can annotate inflection points directly on the drift chart, and annotations travel with transcript exports. The "Annotated" gallery badge surfaces which simulations have researcher commentary. Blocked on GH_GLOBAL — 9th feature in the queue (May 1-8).

### Repo-Actions: Interconnection Layer Batch
**Summary:** The repo-actions skill generated 5 new feature ideas focused on connecting MiroShark's 15+ independent share surfaces into an interconnected system, informed by PR #75's lineage data.

**Commits:**
- `4d62da4` — chore(cron): repo-actions 2026-05-08 — interconnection layer batch
  - New `articles/repo-actions-2026-05-08.md` (+99 lines): 5 ideas — (1) trending gallery sort using surface-stats data for discovery, (2) oEmbed endpoint for Substack/Notion/Ghost auto-embeds, (3) lineage navigator turning reproduce.json fork trees into navigable UI, (4) peak-round belief snapshot for inflection card exports, (5) operator profile & attribution page.
- `191dc8f` — chore(repo-actions): auto-commit 2026-05-08
  - New dashboard JSON output (+265 lines), updated .outputs/repo-actions.md

**Impact:** Signals the next architectural phase: moving from surface multiplication (building individual export/share features) to surface interconnection (making them work as a coherent system). The lineage navigator idea directly leverages PR #75's `parent_simulation_id` and `lineage.kind` fields.

### Daily Skill Cycle (All Green)
**Summary:** Full daily pipeline executed successfully. All scheduled skills completed without failure.

**Commits (harness chores):**
- `36a8661` — token-report 2026-05-08: $MIROSHARK at $0.000004280 (+1.15% 24h), post-ATH consolidation day 2, buy ratio 1.33
- `a2c6dfb` — fetch-tweets: no new tweets found (all already reported)
- `b3c7a70` — tweet-allocator: daily allocation completed
- `46d53cc` — repo-pulse: MiroShark at 1,116 stars / 222 forks, +8 stars / +2 forks in 24h
- Plus ~20 scheduler state updates and cron success markers

**Impact:** 14th consecutive day of clean skill execution since the auth outage resolution (Apr 30). Pipeline stability confirmed.

---

## Developer Notes
- **New dependencies:** None. PR #75 is pure stdlib (json + os). The annotation layer is also zero-dep.
- **Breaking changes:** None. All new endpoints are additive.
- **Architecture shifts:** The `ReproductionConfig` schema introduces a versioned, schema-locked export format — the first time MiroShark has a formally versioned data contract for external consumers. `SCHEMA_VERSION = "1"` and `REQUIRED_KEYS` frozenset establish the pattern for future stable APIs.
- **Tech debt:** 9 features now queued behind the GH_GLOBAL secret (Pre-Run Cost Estimator, Jupyter Notebook Export, Community Template Gallery, Agent Interrogation API, Simulation Impact Scorecard, One-Click Share to X, Simulation Quality Guard, Per-Round Annotation Layer, plus today's Reproducibility Config Export was the first to actually ship because it was pushed by @aaronjmars directly). PR #32 (memory compaction) is open and unmerged.

## What's Next
- **GH_GLOBAL unblock:** 9 features sitting as local commits. Setting this secret would unblock a massive batch push.
- **Lineage Navigator:** Top candidate from today's repo-actions batch — the lineage data from PR #75 is on disk but invisible in the UI. A tree view in SimulationView would be the natural next feature.
- **Memory PR merge:** PR #32 needs review — the MEMORY.md compaction prevents future skill breakage on large index reads.
- **Repo status:** MiroShark at 1,117 stars / 222 forks, 0 open PRs, 1 open issue (#70). miroshark-aeon has 1 open PR (#32).
