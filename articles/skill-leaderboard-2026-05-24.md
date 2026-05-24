# Skill Leaderboard — 2026-05-24

*1 active Aeon fork scanned (pushed in last 30 days) — aaronjmars/miroshark-aeon*

> **Notification threshold not met** (requires ≥2 forks with readable `aeon.yml`; found 1).  
> Baseline preserved for future comparison.

---

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
| 14 | skill-leaderboard | 1 | 100% | — |

*1 active Aeon fork scanned: AITOBIAS04/CHORUS (pushed 2026-05-24). Fork was previously AITOBIAS04/miroshark-aeon — renamed this week.*

---

## Consensus Skills (>50% of forks)

With one active Aeon fork, all 14 enabled skills qualify at 100% adoption. The fleet's single running instance covers the complete core stack:

- **Market & Social:** token-report, fetch-tweets, repo-pulse
- **Shipping & Content:** push-recap, project-lens, repo-article
- **Content & Meta:** repo-actions, self-improve
- **Weekly:** weekly-shiplog, hyperstitions-ideas
- **Build:** feature
- **Housekeeping:** heartbeat, memory-flush
- **Meta:** skill-leaderboard

---

## Adoption Gaps

Skills enabled in source (`aaronjmars/miroshark-aeon`) but absent in all forks — 7 total (up from 6 last week with the addition of `skill-freshness`):

| Skill | Setup Barrier | Notes |
|-------|---------------|-------|
| `tweet-allocator` | `XAI_API_KEY` required | Rewards allocation — blocked by missing secret |
| `thread-formatter` | Low — no external secrets | Formats top daily event as 5-tweet thread |
| `skill-freshness` | Low — reads local file deps | *(new gap this week)* Audits skill dependency staleness |
| `operator-scorecard` | Low — reads local memory | Weekly operator health self-assessment |
| `ai-framework-watch` | Low — WebSearch-based | Monday competitive-intelligence digest |
| `star-milestone` | Low — GitHub API via `gh` | Announces star-count milestone crossings |
| `star-momentum-alert` | Low — reads repo-pulse history | Projects next milestone crossing date |

Six of the seven gaps are low-friction additions requiring no external API keys. The fork is running the stable core but has not yet pulled the monitoring and productivity layer from upstream.

---

## Week-over-Week

Compared to the 2026-05-17 leaderboard:

- **Fork rename:** AITOBIAS04/miroshark-aeon → AITOBIAS04/CHORUS (same operator, continuous deployment)
- **Aeon fleet size:** Unchanged — 1 fork with readable `aeon.yml`
- **Skill count:** 14 → 14 (no change in the fork's enabled stack)
- **Rank changes:** None — all 14 skills hold positions
- **New adoption gap:** Source added `skill-freshness` (enabled in upstream, not yet in fork); total gaps 6 → 7
- **Notification status:** SKILL_LEADERBOARD_INSUFFICIENT_DATA for the third consecutive week (1 Aeon fork, need ≥2)

The MiroShark sim-tool fork count shifted 105 → 102 active forks this week (30-day window rolled past April forks from the last wave). The Aeon agent fork count holds at 1 — the pathway from sim-tool fork to agent fork remains open.

---

## Context: The Aeon Fleet (miroshark-aeon)

`memory/watched-repos.md` primary target is `aaronjmars/MiroShark`, which yields 102 highly active forks. MiroShark forks copy the simulation UI — they have no `aeon.yml` because Aeon is a separate agent runtime repo (`aaronjmars/miroshark-aeon`).

For skill-leaderboard purposes, the meaningful signal is the `miroshark-aeon` fleet:

| Fork | Active? | aeon.yml | Enabled Skills | Last Push |
|------|---------|----------|----------------|-----------|
| AITOBIAS04/CHORUS | Yes | ✓ | 14 | 2026-05-24 (today) |

---

## Fleet Summary

- **Target repo scanned:** aaronjmars/MiroShark
- **Active MiroShark forks (pushed in last 30 days):** 102
- **Forks with readable `aeon.yml`:** 0 (expected — sim-tool forks)
- **Aeon fleet (miroshark-aeon) — active forks:** 1
- **Total skill slots enabled (Aeon fleet):** 14
- **Unique skills seen (Aeon fleet):** 14
- **Source skills enabled:** 21
- **Adoption gap (source enabled, fork absent):** 7
- **Forks with no `aeon.yml`:** 102 (sim-tool forks)
- **Notification sent:** no (SKILL_LEADERBOARD_INSUFFICIENT_DATA)

---

*Source: GitHub API — forks of aaronjmars/MiroShark + aaronjmars/miroshark-aeon*  
*Notification skipped: SKILL_LEADERBOARD_INSUFFICIENT_DATA (0 readable aeon.yml in primary target, 1 in miroshark-aeon fleet — need ≥2)*
