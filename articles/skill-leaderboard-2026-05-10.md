# Skill Leaderboard — 2026-05-10

*1 active fork scanned (pushed in last 30 days) — aaronjmars/miroshark-aeon*

> **Notification threshold not met** (requires ≥2 forks with readable `aeon.yml`; found 1).  
> Baseline preserved for future comparison.

## Top Skills Across the Fleet

| Rank | Skill | Forks Enabled | % of Fleet | Change |
|------|-------|---------------|------------|--------|
| 1 | token-report | 1 | 100% | — |
| 2 | fetch-tweets | 1 | 100% | — |
| 3 | repo-pulse | 1 | 100% | — |
| 4 | push-recap | 1 | 100% | — |
| 5 | project-lens | 1 | 100% | — |
| 6 | repo-actions | 1 | 100% | — |
| 7 | repo-article | 1 | 100% | — |
| 8 | self-improve | 1 | 100% | — |
| 9 | weekly-shiplog | 1 | 100% | — |
| 10 | hyperstitions-ideas | 1 | 100% | — |
| 11 | feature | 1 | 100% | — |
| 12 | heartbeat | 1 | 100% | — |
| 13 | memory-flush | 1 | 100% | — |
| 14 | skill-leaderboard | 1 | 100% | **NEW** |

*Scanned fork: AITOBIAS04/miroshark-aeon (last push: 2026-05-10)*

## Consensus Skills (>50% of forks)

All 14 enabled skills qualify at 100% adoption — the fleet's one active fork runs the full core stack.

**Market & Social:** `token-report`, `fetch-tweets`, `repo-pulse`  
**Shipping & Content:** `push-recap`, `project-lens`, `repo-actions`, `repo-article`, `self-improve`  
**Weekly:** `weekly-shiplog`, `hyperstitions-ideas`  
**Build:** `feature`  
**Housekeeping:** `heartbeat`, `memory-flush`  
**Meta:** `skill-leaderboard` *(newly adopted this week)*

## Adoption Gaps

Skills enabled in the source repo (`aaronjmars/miroshark-aeon`) but absent in all forks:

- **`tweet-allocator`** — re-enabled in the source (schedule: `0 8 * * *`). This skill was previously listed as removed in the May 3 leaderboard; it has since returned to active status in the source. The fork hasn't synced the addition. Requires `XAI_API_KEY` and token config, so setup friction is the likely barrier even once synced.

## Week-over-Week

Compared to the 2026-05-03 leaderboard:

- **Fleet size:** unchanged — 1 fork with a readable `aeon.yml` (AITOBIAS04)
- **New entry:** `skill-leaderboard` (rank 14) — was the adoption gap last week; fork has since synced and enabled it
- **Resolved adoption gap:** `skill-leaderboard` — now running in the fork on the same Sunday 17:00 UTC schedule as the source
- **New adoption gap:** `tweet-allocator` — re-enabled in source since May 3; fork hasn't pulled the update
- **No dropouts, no rank swaps** — all 13 prior skills hold their positions

The fork is tracking the source closely. The main divergence is `tweet-allocator`, which requires external secrets and is not a pure drop-in. The broader catalogue of disabled skills in the source continues to grow — when forks sync, they'll inherit a richer menu of opt-in skills.

## Fleet Summary

- **Active forks scanned:** 1 (of 1 total fork)
- **Total skill slots enabled (across all forks):** 14
- **Unique skills seen:** 14
- **Forks with no `aeon.yml`:** 0
- **Notification sent:** no (SKILL_LEADERBOARD_INSUFFICIENT_DATA)

---
*Source: GitHub API — forks of aaronjmars/miroshark-aeon*  
*Notification skipped: SKILL_LEADERBOARD_INSUFFICIENT_DATA (1 readable aeon.yml, need ≥2)*
