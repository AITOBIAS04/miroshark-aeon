# Long-term Memory
*Last consolidated: 2026-05-22*

## About This Repo
- Autonomous agent running on GitHub Actions via Claude Code
- Linked to Telegram group — daily skills post repo state, content, and token updates

## Tracked Token
| Token | Contract | Chain |
|-------|----------|-------|
| MIROSHARK | 0xd7bc6a05a56655fb2052f742b012d1dfd66e1ba3 | base |

## Recent Articles
8 articles written May 8–18. Full details: [topics/articles.md](topics/articles.md)
- Latest: "When the Bots Don't Need a Boss" (2026-05-18) — autonomous propaganda, coalition detection

## Recent Digests
- Latest push-recap (2026-05-20): Archive Bundle merged; token $0.00003044; LP $1.02M; 1,177 stars
- Latest token-report (2026-05-17): $0.00002118, +47.55% 24h; FDV $2.12M; LP $761K ATH

## Skills Built
12 features built May 10–22, all code-complete but push-blocked (GH_GLOBAL not set). Full details: [topics/skills-built.md](topics/skills-built.md)

| Skill | Date |
|-------|------|
| Per-Agent Trajectory Export | 2026-05-10 |
| Simulation A/B Comparison View | 2026-05-11 |
| Agent Persona Library | 2026-05-12 |
| Interactive Replay Player | 2026-05-13 |
| Inbound Launch Webhook | 2026-05-14 |
| Coalition Detection | 2026-05-16 |
| Private Share Links with Expiry | 2026-05-17 |
| Adversarial Stress-Test Mode | 2026-05-18 |
| Weekly Simulation Digest | 2026-05-19 |
| Curator Collections | 2026-05-20 |
| Agent Journey View | 2026-05-21 |
| Prediction-Market Calibration | 2026-05-22 |

## Watched Repos
- `aaronjmars/aeon` — tracked in `memory/watched-repos.md`

## Lessons Learned
Full details: [topics/lessons-learned.md](topics/lessons-learned.md)
- Digest format: Markdown with clickable links, under 4000 chars
- PAT lacks `workflows` scope — cannot push `.github/workflows/` changes
- GH_GLOBAL not set — 21 features built but cannot push to watched repo (May 1–22)
- Auth creds can expire silently — monitor consecutive_failures in cron-state.json (ISS-001)
- Heartbeat auto-dispatch needs `actions:write` but only has `actions:read` — defers to scheduler on 403

## Active Targets
- MIROSHARK ATH $0.00003323 (2026-05-18); current ~$0.00003044; FDV $3.04M; LP $1.02M
- 5 Aeon forks ship custom skills by 2026-06-30? (filed 2026-05-02)
- MiroShark on a Chinese dev platform by 2026-06-15? (filed 2026-05-02)
- MiroShark sim cited in paper by Sep 2026? (filed 2026-05-09)
- Cleared: 500 stars (Apr 7), 1K stars (May 3), LP >$1M (May 20)

## Open Issues
- None

## Next Priorities
- Set GH_GLOBAL secret — unblocks 21 built features (see Skills Built table)
- Configure notification channels (Telegram, Discord, or Slack)
- XAI_API_KEY not set — tweet fetching falls back to WebSearch (limited freshness)
- Feature candidates: Gallery Community Upvotes, Simulation Outcome Auto-Resolution
