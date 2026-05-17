# Skill Leaderboard — 2026-05-17

*105 active forks scanned (pushed in last 30 days) — aaronjmars/MiroShark*

> **Notification threshold not met** (requires ≥2 forks with readable `aeon.yml`; found 0).  
> Baseline preserved for future comparison.

---

## Top Skills Across the Fleet

| Rank | Skill | Forks Enabled | % of Fleet | Change |
|------|-------|---------------|------------|--------|
| — | *(no skills enabled — no fork carries an `aeon.yml`)* | 0 | 0% | — |

*105 MiroShark forks scanned. None contain an `aeon.yml` configuration — these are forks of the simulation tool, not the Aeon agent runtime.*

---

## Context: The Aeon Fleet (miroshark-aeon)

The `memory/watched-repos.md` primary target is `aaronjmars/MiroShark`, which produces 105 highly active forks. MiroShark forks fork the simulation UI — they have no `aeon.yml` because Aeon is a separate repo (`aaronjmars/miroshark-aeon`).

For skill-leaderboard purposes, the meaningful comparison is the `miroshark-aeon` fleet:

| Fork | Active? | aeon.yml | Enabled Skills |
|------|---------|----------|----------------|
| AITOBIAS04/miroshark-aeon | Yes (pushed 2026-05-17) | ✓ | 14 |

**AITOBIAS04 enabled skill stack (14 skills):**

| Rank | Skill | Category |
|------|-------|----------|
| 1 | token-report | Market & Social |
| 2 | fetch-tweets | Market & Social |
| 3 | repo-pulse | Market & Social |
| 4 | push-recap | Shipping & Content |
| 5 | project-lens | Shipping & Content |
| 6 | repo-actions | Content & Meta |
| 7 | repo-article | Content & Meta |
| 8 | self-improve | Content & Meta |
| 9 | weekly-shiplog | Weekly |
| 10 | hyperstitions-ideas | Weekly |
| 11 | feature | Build |
| 12 | heartbeat | Housekeeping |
| 13 | memory-flush | Housekeeping |
| 14 | skill-leaderboard | Meta |

---

## Consensus Skills (>50% of forks)

With one active aeon fork, all 14 enabled skills qualify at 100% adoption. The fleet's one running instance covers the full core stack across market tracking, content generation, build automation, and housekeeping.

---

## Adoption Gaps

Skills enabled in source (`aaronjmars/miroshark-aeon`) but absent in all forks — grew from 1 to 6 since last week:

| Skill | Added to Source | Setup Barrier |
|-------|-----------------|---------------|
| `tweet-allocator` | Before May 10 (re-enabled) | `XAI_API_KEY` required |
| `thread-formatter` | Since May 10 | Low — no external secrets |
| `operator-scorecard` | Since May 10 | Low — reads local memory |
| `ai-framework-watch` | Since May 10 | Low — WebSearch-based |
| `star-milestone` | Since May 10 | Low — GitHub API via `gh` |
| `star-momentum-alert` | Since May 10 | Low — reads repo-pulse history |

Five of the six gaps are low-friction additions that require no external API keys. The fork is lagging upstream by approximately one sync cycle.

---

## Week-over-Week

Compared to the 2026-05-10 leaderboard:

- **MiroShark fleet:** First time scanned — 105 active forks found, 0 with `aeon.yml` (no baseline to compare)
- **Aeon fleet size:** Unchanged — 1 fork (AITOBIAS04) with readable `aeon.yml`
- **AITOBIAS04 rank changes:** No changes — all 14 skills hold positions
- **New adoption gaps:** 5 new source skills added since May 10 (thread-formatter, operator-scorecard, ai-framework-watch, star-milestone, star-momentum-alert); fork hasn't synced
- **Notification status:** SKILL_LEADERBOARD_INSUFFICIENT_DATA for the second consecutive week (1 aeon fork, need ≥2)

The MiroShark fork explosion (+105 active forks of the sim tool) has not yet translated into Aeon agent forks. The adoption pathway is: fork MiroShark → discover Aeon → fork miroshark-aeon → configure aeon.yml. That middle step remains a gap.

---

## Fleet Summary

- **Target repo scanned:** aaronjmars/MiroShark
- **Active forks scanned:** 105 (pushed in last 30 days)
- **Forks with readable `aeon.yml`:** 0
- **Forks with no `aeon.yml`:** 105 (expected — sim tool forks)
- **Aeon fleet (miroshark-aeon) — active forks:** 1
- **Total skill slots enabled (aeon fleet):** 14
- **Unique skills seen (aeon fleet):** 14
- **Notification sent:** no (SKILL_LEADERBOARD_INSUFFICIENT_DATA)

---

*Source: GitHub API — forks of aaronjmars/MiroShark + aaronjmars/miroshark-aeon*  
*Notification skipped: SKILL_LEADERBOARD_INSUFFICIENT_DATA (0 readable aeon.yml in primary target, 1 in miroshark-aeon fleet — need ≥2)*
