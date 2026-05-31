# Skill Leaderboard — 2026-05-31

*1 active Aeon fork scanned (pushed in last 30 days) — AITOBIAS04/CHORUS*

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

*1 active Aeon fork scanned: AITOBIAS04/CHORUS (pushed 2026-05-31). Unchanged from last week's 14-skill stack.*

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

Skills enabled in source (`aaronjmars/miroshark-aeon`) but absent in all forks — **4 total** (down from 7 last week):

| Skill | Setup Barrier | Notes |
|-------|---------------|-------|
| `thread-formatter` | Low — no external secrets | Formats top daily event as a 5-tweet thread ready to paste |
| `operator-scorecard` | Low — reads local memory | Weekly operator health self-assessment (Monday) |
| `star-milestone` | Low — GitHub API via `gh` | Announces star-count milestone crossings |
| `star-momentum-alert` | Low — reads repo-pulse history | Projects next milestone crossing date |

Three gaps closed this week: the source repo disabled `tweet-allocator`, `skill-freshness`, and `ai-framework-watch` (via PR #47 on 2026-05-27). All four remaining gaps are low-friction additions with no external secret requirements.

---

## Week-over-Week

Compared to the 2026-05-24 leaderboard:

- **Fork name:** AITOBIAS04/CHORUS — unchanged
- **Aeon fleet size:** Unchanged — 1 fork with readable `aeon.yml`
- **Skill count in fork:** 14 → 14 (no change)
- **Rank changes:** None — all 14 skills hold their positions
- **Adoption gaps:** 7 → 4 (−3)
  - *Closed:* `tweet-allocator` (source disabled), `skill-freshness` (source disabled), `ai-framework-watch` (source disabled via PR #47)
  - *Unchanged:* `thread-formatter`, `operator-scorecard`, `star-milestone`, `star-momentum-alert`
- **Source additions:** `operator-scorecard`, `star-milestone`, `star-momentum-alert`, `thread-formatter` remain enabled in source — these appeared as gaps in prior weeks and still haven't been adopted by the fork
- **MiroShark sim-tool forks (30d window):** 72 active (down from 102 — 30-day window rolled past the April fork wave)
- **Notification status:** SKILL_LEADERBOARD_INSUFFICIENT_DATA for the fourth consecutive week (1 Aeon fork, need ≥2)

---

## Context: The Aeon Fleet (miroshark-aeon)

`memory/watched-repos.md` primary target is `aaronjmars/MiroShark`, which yields 72 active sim-tool forks. MiroShark forks copy the simulation UI — they have no `aeon.yml` because Aeon is a separate agent runtime repo (`aaronjmars/miroshark-aeon`).

For skill-leaderboard purposes, the meaningful signal is the `miroshark-aeon` fleet:

| Fork | Active? | aeon.yml | Enabled Skills | Last Push |
|------|---------|----------|----------------|-----------|
| AITOBIAS04/CHORUS | Yes | ✓ | 14 | 2026-05-31 (today) |

---

## Fleet Summary

- **Target repo scanned:** aaronjmars/MiroShark
- **Active MiroShark forks (pushed in last 30 days):** 72
- **Forks with readable `aeon.yml`:** 0 (expected — sim-tool forks)
- **Aeon fleet (miroshark-aeon) — active forks:** 1
- **Total skill slots enabled (Aeon fleet):** 14
- **Unique skills seen (Aeon fleet):** 14
- **Source skills enabled:** 15
- **Adoption gap (source enabled, fork absent):** 4
- **Forks with no `aeon.yml`:** 72 (sim-tool forks)
- **Notification sent:** no (SKILL_LEADERBOARD_INSUFFICIENT_DATA)

---

*Source: GitHub API — forks of aaronjmars/MiroShark + aaronjmars/miroshark-aeon*  
*Notification skipped: SKILL_LEADERBOARD_INSUFFICIENT_DATA (0 readable aeon.yml in primary target, 1 in miroshark-aeon fleet — need ≥2)*
