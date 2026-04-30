# Skill Leaderboard — 2026-04-30

*Fleet scan: aaronjmars/MiroShark (114 active forks) + aaronjmars/miroshark-aeon (1 active fork)*

> **Note:** This is the first leaderboard run — no prior data for week-over-week comparison.
> Notification threshold not met (requires ≥2 forks with readable `aeon.yml`; found 1).

## Top Skills Across the Fleet

*1 fork scanned with readable `aeon.yml` (AITOBIAS04/miroshark-aeon)*

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

## Consensus Skills (>50% of forks)

All 13 enabled skills qualify — the one fork running Aeon keeps the full core stack on:

**Market & Social:** `token-report`, `fetch-tweets`, `repo-pulse`  
**Shipping & Content:** `push-recap`, `project-lens`, `repo-actions`, `repo-article`, `self-improve`  
**Weekly:** `weekly-shiplog`, `hyperstitions-ideas`  
**Build:** `feature`  
**Housekeeping:** `heartbeat`, `memory-flush`

## Adoption Gaps

Skills enabled in the source repo (`aaronjmars/miroshark-aeon`) but absent in all forks:

- **`tweet-allocator`** — the token rewards allocator is live in the source but not picked up by the fork yet. Makes sense: it requires `XAI_API_KEY` and token-specific config. Discoverability is fine; friction is setup cost.

The ~50 other disabled-in-source skills (content digests, DeFi monitors, tweet writers, etc.) show zero adoption — expected, as they ship disabled by design.

## Week-over-Week

First leaderboard — no prior data. Baseline established for future runs.

## Fleet Summary

- **Active forks scanned:** 115 total (114 × MiroShark, 1 × miroshark-aeon)
- **Forks with readable `aeon.yml`:** 1
- **Total skill slots enabled (across all forks):** 13
- **Unique skills seen:** 13
- **Forks with no `aeon.yml`:** 114 (MiroShark forks are the simulation product, not Aeon agent deployments)

## Notes on Scan Scope

The watched-repos list leads with `aaronjmars/MiroShark`, which has 114 highly active forks — but MiroShark is the simulation tool itself, not an Aeon agent deployment, so none of those forks carry `aeon.yml`. The leaderboard is only meaningful against `aaronjmars/miroshark-aeon` forks (the actual Aeon agent instance), which currently has 1 active fork.

As miroshark-aeon gains more community forks, this leaderboard will become a real signal for which skills are being adopted vs. which need better docs or lower setup friction.

---
*Source: GitHub API — forks of aaronjmars/MiroShark + aaronjmars/miroshark-aeon*  
*Notification skipped: SKILL_LEADERBOARD_INSUFFICIENT_DATA (1 readable aeon.yml, need ≥2)*
