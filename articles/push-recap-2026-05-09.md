# Push Recap — 2026-05-09

## Overview

30 commits across two repos by a single author (aeonframework). The headline is MiroShark PR #76 — *Simulation Lineage Navigator* — a direct sequel to yesterday's PR #75 that turns the one-directional `parent_simulation_id` pointer into a navigable graph in both directions. The aeon repo ran a full daily skill cycle with no feature or fix work of its own; all 29 commits are routine chore auto-commits from the scheduled skill pipeline.

**Stats:** ~50 files changed, +3,428 / -100 lines across 30 commits (1 MiroShark feature commit + 29 aeon chore commits)

---

## aaronjmars/MiroShark

### New Feature: Simulation Lineage Navigator (PR #76, open)

**Summary:** Yesterday's PR #75 (Reproducibility Config Export) persisted `parent_simulation_id` + `lineage.kind` + counterfactual trigger metadata into every `reproduce.json`. The data was on disk but the lineage was one-directional — a child sim knew its parent, the parent had no view into its children. Run a base scenario, trigger three counterfactual branches, and there was no way to walk from the parent to "the three branches that diverged at round 12" without remembering each child sim id. PR #76 closes that gap by adding the reverse pointer.

**Commits:**

- `d6dd47c` — *feat: simulation lineage navigator — fork / counterfactual graph traversal* (+1,778 / -0 across 11 files)

  - **New file `backend/app/services/lineage_service.py`** (+390 LoC, pure stdlib): `MAX_CHILDREN = 50` literal cap with honest `total_children` count, `SCENARIO_PREVIEW_CHARS = 80`. Defensive disk readers (`_load_state`, `_load_config_scenario`, `_load_counterfactual`) swallow missing files, corrupt JSON, and mid-rewrite races — the navigator never crashes a parent's load on a single bad child. `_kind_for(state, cf)` discriminator: no parent → `"original"`, parent + counterfactual file → `"counterfactual"`, parent + no counterfactual → `"fork"`. `find_children(parent_id, data_dir)` scans the corpus for reverse pointers, skips self-pointers and private children, sorts oldest-first by `created_at`, caps at 50.

  - **Modified `backend/app/api/simulation.py`** (+101): `GET /api/simulation/<simulation_id>/lineage` route. Same publish gate as the other discovery endpoints; `Cache-Control: public, max-age=300`; delegates graph composition to `lineage_service.build_lineage_payload`.

  - **New file `backend/tests/test_unit_lineage.py`** (~501 LoC, 16 unit tests): pins every shape promise + degradation path — MAX_CHILDREN literal value pin, scenario preview truncation, original-with-no-children, fork carries parent, counterfactual carries `{trigger_round, label}`, three-branch discovery, private children excluded, oldest-first sort, corrupt child state silently skipped, max-children cap with honest total, self-pointer doesn't recurse, missing data dir doesn't crash, route-decorator presence guard, OpenAPI drift guard, module-import guard.

  - **Modified `backend/openapi.yaml`** (+189): new `/api/simulation/{simulation_id}/lineage` path under Analytics tag, `SimulationLineage` schema component with full per-field documentation.

  - **Modified `frontend/src/components/EmbedDialog.vue`** (+505): 🌳 Lineage panel between reproducibility config and verified-prediction sections. Shows only when `hasLineageGraph` is true — originals with no forks see no panel. Parent row with truncated 60-char scenario + "Open parent" link. Children list with 🪐 Forked (indigo) or 🔀 Counterfactual (orange) badges. Counterfactual rows surface trigger round + label inline ("At round 12 (ceo_resigns)") so each branch reads as the narrative event, not a slightly different scenario.

  - **Modified `frontend/src/api/simulation.js`** (+38): `getSimulationLineage(simId)` helper with full JSDoc.

  - **Modified `README.md`** (+2 lines, en + zh-CN): Lineage Navigator row in features table.

  - **Modified `docs/FEATURES.md` + `docs/FEATURES.zh-CN.md`** (+25 each): full feature section.

  - **Modified `docs/API.md` + `docs/API.zh-CN.md`** (+1 each): endpoint row in API reference table.

**Impact:**
- **Citation graph completeness.** PR #75 made finished sims citable via `reproduce.json`'s file hash. PR #76 makes the graph behind a citation navigable — a reader who lands on `/watch/<sim_id>` for a counterfactual branch can follow lineage back to the base scenario and forward to sibling branches.
- **Public-only filter is a privacy primitive.** Operators forking privately for in-progress work don't leak those branches into a tweeted parent's lineage view.
- **Defense-in-depth compounds.** Like PR #75, the implementation never raises on disk corruption or mid-write races. Combined with PR #75's bytewise-stable JSON, this is two consecutive PRs where the public discovery surface tolerates a single bad artifact without blanking out.

---

## aaronjmars/miroshark-aeon

### Content & Social Pipeline

**Summary:** The daily skill cycle ran a full pass producing articles, social monitoring, token analytics, tweet rewards, and a new hyperstition question. Two articles from late May 8 runs landed within the 24h window.

**Commits (representative auto-commits carrying skill output):**

- `4b5a717` — `chore(token-report): auto-commit 2026-05-09`
  - $MIROSHARK at $0.000005080 (+15.48% 24h), recovery from post-ATH dip. Liquidity at $290K (new post-ATH LP high). Buy ratio 1.24. Volume compressing post-ATH ($29.2K, down from $257K on May 6). 7d: +41.4%, 30d: +327%.
  - Created `articles/token-report-2026-05-09.md` (+44 lines), dashboard output JSON (+155 lines)

- `58e0364` — `chore(fetch-tweets): auto-commit 2026-05-09`
  - 10 new tweets found. Top signal: @soboltoshi citing MiroShark as peer-review layer for CancerHawk cancer research AI stack (18L/4RT). @aaronjmars announced the @aeonframework + @miroshark_ + @hyperstiti0ns trio (17L/6RT). @Mnosh06 published detailed adoption thread covering Revault integration, Grok #1 ranking, Umia #7 at $6M TPV (17L/6RT). Chinese-language tweet from @btcbabycow (9L/2RT).
  - Updated `memory/fetch-tweets-seen.txt` (+10 URLs), dashboard output JSON (+134 lines)

- `d0ec250` — `chore(tweet-allocator): auto-commit 2026-05-09`
  - $10 in $MIROSHARK allocated to 5 authors: @Mnosh06 ($3.40, score 35), @soboltoshi ($2.91, score 30), @btcbabycow ($1.46, score 15), @MrDegenWolf ($1.36, score 14), @bankrbot ($0.87, score 9). All pending manual send.
  - Created `articles/tweet-allocator-2026-05-09.md` (+22 lines), dashboard output JSON (+257 lines)

- `1628d9f` — `chore(hyperstitions-ideas): auto-commit 2026-05-09`
  - New question: "Will the Aeon agent framework be deployed by ≥1 external operator running publicly under their own project identity by June 30, 2026?" Reflexivity 4/5, Viral 4/5. Triggered by Aaron's tweet explicitly framing the @aeonframework / @miroshark_ / @hyperstiti0ns trio as canonical.

- `5f95a1c` — `chore(repo-article): auto-commit 2026-05-08`
  - Published "Eleven Surfaces, One File Hash: MiroShark Lands the Citation Primitive" — frames PR #75 as the piece tying the 11-surface arc into citable artifacts.

- `731cbac` — `chore(project-lens): auto-commit 2026-05-08`
  - Published "There Is No AI Reproducibility Crisis. There's a File-Saving Crisis." — contrarian take on NeurIPS/Thinking Machines nondeterminism discourse, framing PR #75's bytewise-stable JSON as the actual bottleneck fix.

### Community Growth

**Summary:** Steady growth continuing post-1K-stars milestone.

- `39bb0b0` — `chore(repo-pulse): auto-commit 2026-05-09`
  - 1,122 stars (+6 new: JustinASmith, Houman6460, LemonCANDY42, willlong, XucroYuri, yoganandkapgate-lab), 223 forks (+1: Jeremyliu-621)

### Steady-State Operations

**Summary:** All scheduled skills completed successfully. No regressions in the auto-commit chain. Agent Belief Heatmap built locally but push blocked (10th consecutive due to missing GH_GLOBAL secret).

- `a262539` — `chore(heartbeat): auto-commit 2026-05-08`
  - HEARTBEAT_OK. All 10 scheduled skills for Friday May 8 completed successfully. One open PR on miroshark-aeon (#32, not stalled).

- `4c2e626` — `chore(feature): auto-commit 2026-05-09`
  - Built Simulation Lineage Navigator (PR #76) for MiroShark and successfully pushed. Also logged Agent Belief Heatmap build (push blocked — GH_GLOBAL not set, 10th consecutive block).
  - Updated `memory/MEMORY.md` Skills Built table, `.outputs/feature.md`

- Plus 8 `chore(scheduler): update cron state` commits and 10 `chore(cron): <skill> success` commits tracking pipeline state.

**Open PR:** #32 (`improve/memory-md-row-caps`) opened May 8, unchanged.

---

## Developer Notes

- **New dependencies:** None on either repo. Zero-new-deps streak on MiroShark now spans 16 consecutive substantive PRs (#57 → #76).
- **Breaking changes:** None. PR #76 is a pure addition — new endpoint, new service module, new test file, new dialog panel; no existing route, schema, or component signature changed.
- **Architecture shifts:** `lineage_service` is the second pure-stdlib read-only service composed against PR #75's on-disk artifacts. The pattern is becoming load-bearing: PR #75 wrote the citation primitive to disk, PR #76 reads it back in a different shape. The next surface against the same artifacts only needs another ~390 LoC of read-only composition.
- **Tech debt:** None introduced. `MAX_CHILDREN = 50` cap is honest (`total_children` reflects uncapped scan total). Corrupt-state degradation is explicit. Public-only filter documented as a privacy primitive.
- **Tests:** +501 LoC of pure-stdlib unit tests on `test_unit_lineage.py`. Frontend build green (728 modules, vite v7.2.7).

## What's Next

- **PR #76 merge.** Branch `feat/simulation-lineage-navigator` is open on MiroShark; assuming the same same-day cadence as PR #74 / #75, expect merge within 24h.
- **Lineage as a discovery signal.** With `lineage_kind` + `total_children` available per-sim, the May 8 repo-actions idea #1 (Trending Simulations Sort) has a richer signal to draw on.
- **GH_GLOBAL still missing.** Agent Belief Heatmap is the 10th consecutive feature build blocked from pushing. 9 features remain as local commits.
- **Open PR #32 on aeon.** MEMORY.md row-size caps, now 24h+ with no follow-up.
- **Remaining May 8 ideas:** #1 Trending Sort, #2 oEmbed Endpoint, #4 Peak-Round Snapshot, #5 Operator Profile — four candidates for the next 4 days at 1-feature-per-day cadence.
- **External-operator hyperstition.** Today's new prediction market question asks whether anyone outside `aaronjmars/*` will stand up their own Aeon deployment by June 30.
