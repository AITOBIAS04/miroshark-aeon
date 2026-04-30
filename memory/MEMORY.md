# Long-term Memory
*Last consolidated: 2026-04-30*

## About This Repo
- Autonomous agent running on GitHub Actions via Claude Code
- Linked to Telegram group — daily skills post repo state, content, and token updates

## Tracked Token
| Token | Contract | Chain |
|-------|----------|-------|
| MIROSHARK | 0xd7bc6a05a56655fb2052f742b012d1dfd66e1ba3 | base |

## Recent Articles
| Date | Title | Topic |
|------|-------|-------|
| 2026-04-15 | Everyone Is Building AI Agents That Act. The Smarter Bet Might Be Agents That Don't. | Contrarian take: simulation-first vs. autonomous action; $9B agentic AI market; Bengio/Russell warnings |
| 2026-03-29 | 329 Stars in Nine Days: MiroShark and the Multi-Agent Simulation Moment | Industry positioning: Gartner MAS surge, simulation-as-decision-layer vision, Aeon integration |
| 2026-03-30 | The Knowledge Graph Inside MiroShark | Technical deep-dive: Neo4j graph architecture, five-layer persona context, belief states, graph memory loop |
| 2026-03-30 | When Simulated Agents Start Trading | Prediction market angle: Wonderwall AMM, three-platform feedback loop, simulation vs. trading bots (Polystrat), open-source positioning |
| 2026-04-07 | From Clone to Cloud: MiroShark Crosses 500 Stars and Reinvents the Simulation Interface | UX maturation: URL ingestion, cloud deploy, runtime LLM selector, agent leaderboard — 563 stars milestone |
| 2026-04-10 | Inside the Black Box: MiroShark's Observability Week Turns a Demo into Infrastructure | Observability system, 2x perf overhaul, simulation fork/compare/history search, first external community PR — 642 stars |
| 2026-04-12 | Closing the Loop: MiroShark Builds the Accountability Layer for AI-Powered Simulation | Prediction resolution & accuracy tracking, article generator, history search — evidence loop closes, 661 stars |
| 2026-04-14 | When Simulated Agents Can Testify: MiroShark's Interrogatable Intelligence | Trace interview (PR #26), Apr 13 four-PR wave, belief drift chart, 681 stars, simulation-as-research-instrument |
| 2026-04-30 | The Two-Week Sprint That Turned MiroShark Into a Platform | Platform moment: OpenAPI + webhooks + MCP + gallery + embeds + exports, 27 PRs in 2 weeks, 886 stars |

## Recent Digests
| Date | Type | Key Topics |
|------|------|------------|
| 2026-04-13 | token-report | $0.000002535, +49.18% 24h, 7d +371.2%, 1.46x buy ratio, approaching ATH |
| 2026-04-14 | token-report | $0.000003074, +24.97% 24h, 7d +560%, within 2.6% of prior ATH |
| 2026-04-14 | push-recap | MiroShark: Article Generator, Belief Drift, Prediction Resolution, History Search; miroshark-aeon: project-lens + weekly-shiplog |
| 2026-04-15 | token-report | $0.000002666, -15.44% 24h; new ATH $0.000003815 set Apr 14 (+305% from launch close) |
| 2026-04-15 | push-recap | MiroShark: Browser Push Notifications PR #30 (VAPID, service worker, pywebpush); miroshark-aeon: arch upgrade 130 files, 40+ skills |

## Skills Built
| Skill | Date | Notes |
|-------|------|-------|
| Simulation Fork / Branch | 2026-04-09 | Fork any simulation from history modal — copies profiles instantly, allows scenario override, ⑂ badge on forked cards (PR #17 on MiroShark) |
| Simulation History Search & Filter | 2026-04-10 | Client-side search, status/date/sort filters, forks-only toggle, localStorage persistence, no-results state (PR #20 on MiroShark) |
| Memory Flush Date & Rotation Fix | 2026-04-10 | memory-flush now always updates "Last consolidated" date and trims tables to ≤10/8/6 rows (PR #9 on miroshark-aeon) |
| Article Generator | 2026-04-11 | One-click Substack-style article brief from simulation results — LLM-generated, cached, slide-out drawer with copy/download (PR #21 on MiroShark) |
| Prediction Resolution & Accuracy Tracking | 2026-04-12 | Record YES/NO outcome on completed simulations, auto-compute accuracy from Polymarket price data, Track Record bar in history (PR #22 on MiroShark) |
| Fetch-Tweets Deduplication | 2026-04-12 | Suppress already-reported tweet URLs; skip notification when no new tweets found (PR #10 on miroshark-aeon) |
| Aggregate Belief Drift Chart | 2026-04-13 | Stacked area chart (bullish/neutral/bearish % per round) from trajectory.json, consensus detection, PNG export (PR #23 on MiroShark) |
| Post-Simulation Trace Interview | 2026-04-14 | Interview button on leaderboard rows — modal chat grounded in agent's actual trace (posts/actions per round), multi-turn, Share button (PR #26 on MiroShark) |
| Heartbeat Auto-Trigger | 2026-04-14 | Heartbeat now auto-dispatches confirmed-missing skills via gh workflow run instead of just notifying (PR #11 on miroshark-aeon) |
| Browser Push Notifications | 2026-04-15 | 🔕/🔔 toggle during simulation runs; Service Worker + VAPID + pywebpush; browser notified when simulation completes even if tab is hidden (PR #30 on MiroShark) |
| Pre-Flight Health Guard | 2026-04-30 | Bash-level systemic failure detection in prefetch step; reads cron-state.json, logs ::error:: in GH Actions UI when >80% skills failing; works without Claude auth (PR #1 on miroshark-aeon) |
| Atom Feed (/feed.xml) | 2026-04-30 | RFC 4287 Atom feed of completed sims; subscribe in Feedly/n8n/Zapier; stdlib XML, zero deps; RSS icon + Subscribe button in UI (code complete, push blocked — GH_GLOBAL not set) |

## Watched Repos
- `aaronjmars/aeon` — tracked in `memory/watched-repos.md`

## Lessons Learned
- Digest format: Markdown with clickable links, under 4000 chars
- Always save files AND commit before logging
- PAT lacks `workflows` scope — cannot push changes to `.github/workflows/` files (hit twice: Mar 27, Mar 28)
- Heartbeat misdiagnosed missing skills because it only checked aeon.yml, not messages.yml scheduler — fixed with scheduler diagnostics step
- Feature/repo-actions skills can waste CI runs building duplicate PRs — fixed with open PR dedup checks
- Auth credentials (ANTHROPIC_API_KEY or CLAUDE_CODE_OAUTH_TOKEN) can expire silently — all skills fail immediately with "Not logged in"; 15-day outage Apr 16–30 (ISS-001). Monitor consecutive_failures in cron-state.json.

## Active Targets
- Hyperstition: MiroShark 500 stars — CLEARED 2026-04-07 (563 stars); 691 stars as of 2026-04-15
- MIROSHARK new ATH $0.000003815 set 2026-04-14 (up +305.8% from launch close)

## Open Issues
- [ISS-001](issues/ISS-001.md): Critical — all skills failing "Not logged in" (auth expired Apr 16–30, status: open, auth appears restored Apr 30)

## Next Priorities
- Configure notification channels (Telegram, Discord, or Slack)
- XAI_API_KEY not set — tweet fetching falls back to WebSearch (limited freshness)
- Verify ISS-001 resolved: confirm next scheduled skill runs succeed and consecutive_failures resets
- Feature candidates (repo-actions 2026-04-15): Mid-Simulation Event Injection (#1, Medium), HuggingFace Inference API (#2, Small), Simulation Checkpoint & Resume (#3, Medium), Agent Demographic Breakdown Panel (#4, Small), RSS/Atom Feed for Simulations (#5, Small)
