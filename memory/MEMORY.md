# Long-term Memory
*Last consolidated: 2026-05-10*

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
| 2026-04-30 | 906 Stars and a New Language: MiroShark's Quiet Bet on Distribution | Distribution angle: Chinese i18n (PR #61), RSS/Atom feeds (PR #60), distribution stack thesis, 906 stars, path to 1K |
| 2026-04-30 | When AI Simulations Need Receipts: MiroShark's Accountability Turn | Accountability angle: verified predictions (#47), Langfuse observability (#51/#54), 57% token compaction (#55), admin auth, 913 stars |
| 2026-05-01 | In 93 Days, Every AI Agent in Europe Needs a Paper Trail | Current events: EU AI Act Aug 2 deadline, agentic compliance gap, Article 12 logging mandates, MiroShark audit trail as regulatory template, 954 stars |
| 2026-05-02 | When Simulation Becomes a Spectator Sport: MiroShark's Bet on Live AI | Spectator watch page (PR #67), seven share surfaces, simulation-as-medium thesis, research export pipeline, 977 stars |
| 2026-05-04 | The Spreadsheet Killed the Mainframe Analyst. Social Simulation Is Next. | Industry comparison; VisiCalc → social simulation; democratizing what-if analysis |
| 2026-05-06 | Nobody Told the Agents to Agree | Emergent social conventions in LLM populations; Science Advances May 2025; intelligence as a social process |
| 2026-05-08 | AI's Reproducibility Crisis Isn't Technical. It's a Choice. | Contrarian take; NeurIPS MLRC 2026 official track; Thinking Machines Lab LLM non-determinism; 70% of AI researchers can't reproduce results |
| 2026-05-10 | Every Simulation Deserves a Citation Key | Reproducibility infrastructure: reproduce.json (PR #75) + Lineage Navigator (PR #76) as citation primitives; CHI 2026 PoliSim + Stanford CORES context; 1,127 stars |

## Recent Digests
| Date | Type | Key Topics |
|------|------|------------|
| 2026-05-08 | token-report | $0.000004280, +1.15% 24h; buy ratio 1.33; LP $259.3K; post-ATH consolidation day 2; 30d +819% |
| 2026-05-08 | push-recap | PR #75 Reproducibility Config Export merged (+1,916 lines); self-improve PR #32 MEMORY.md compaction |
| 2026-05-09 | token-report | $0.000005080, +15.48% 24h; buy ratio 1.24; LP $290.1K new post-ATH high; V-shaped recovery begins |
| 2026-05-09 | push-recap | PR #76 Simulation Lineage Navigator opened; Agent Belief Heatmap built (push blocked 9th); new hyperstition filed |
| 2026-05-10 | token-report | $0.000006488, +31.52% 24h; ATH near-retest (-6.3%); LP $337.6K all-time high; buy ratio 1.25 |
| 2026-05-10 | push-recap | PR #76 merged; PRs #77+#78 opened; Per-Agent Trajectory Export built (blocked 10th); 1,127 stars |

## Skills Built
| Skill | Date | Notes |
|-------|------|-------|
| Pre-Flight Health Guard | 2026-04-30 | Bash-level systemic failure detection in prefetch step; reads cron-state.json, logs ::error:: in GH Actions UI when >80% skills failing; works without Claude auth (PR #1 on miroshark-aeon) |
| Atom Feed (/feed.xml) | 2026-04-30 | RFC 4287 Atom feed of completed sims; subscribe in Feedly/n8n/Zapier; stdlib XML, zero deps; RSS icon + Subscribe button in UI (code complete, push blocked — GH_GLOBAL not set) |
| Pre-Run Cost Estimator | 2026-05-01 | Show estimated USD cost, tokens, and wall-clock time before simulation starts; built-in pricing table for 15+ models; colour-coded cost tier badge in Step 3 UI (code complete, push blocked — GH_GLOBAL not set) |
| Jupyter Notebook Export | 2026-05-02 | One-click .ipynb export with pre-written pandas, matplotlib, and networkx analysis cells — belief drift chart, agent trajectories, interaction network, summary statistics (code complete, push blocked — GH_GLOBAL not set) |
| Community Template Gallery | 2026-05-03 | /templates page with 10 domain-specific seed scenarios, CRUD API, tag filters, search, one-click launch, "Save as Template" from completed sims (code complete, push blocked — GH_GLOBAL not set) |
| Agent Interrogation API | 2026-05-04 | 4 endpoints: GET /agents, GET /agents/<name>/profile, POST /agents/<name>/query (rate-limited, session-based multi-turn), GET /interview-sessions; OpenAPI docs, frontend API, bilingual docs (code complete, push blocked — GH_GLOBAL not set) |
| Simulation Impact Scorecard | 2026-05-05 | 4 metrics (Polarization Index, Influence Concentration, Consensus Velocity, Narrative Volatility) from trajectory data; GET /scorecard endpoint; ScorecardPanel.vue 2x2 grid; gallery chip; OpenAPI spec (code complete, push blocked — GH_GLOBAL not set) |
| One-Click Share to X | 2026-05-06 | twitter.com/intent/tweet button in Embed dialog + hover X icon on gallery cards; auto-composes tweet from scenario excerpt, consensus summary, share URL; zh-CN localized; pure client-side, zero API keys (code complete, push blocked — GH_GLOBAL not set) |
| Simulation Quality Guard | 2026-05-07 | 4 per-round checks (dominance, stagnation, hard lock, neutral collapse); GET /quality-report endpoint; QualityReport panel in results view; Clean/Flagged gallery badges; clean_only gallery filter; 18 unit tests; OpenAPI spec (code complete, push blocked — GH_GLOBAL not set) |
| Per-Round Annotation Layer | 2026-05-08 | 3 API endpoints (GET/POST/DELETE annotations); AnnotationPanel.vue below drift chart; purple dashed markers on BeliefDriftChart; Annotated gallery badge; transcript export integration; 22 unit tests; OpenAPI spec (code complete, push blocked — GH_GLOBAL not set) |
| Agent Belief Heatmap | 2026-05-09 | GET /belief-heatmap endpoint; HeatmapView.vue per-agent stance grid; sort by influence/flip/name; compact mode >20 agents; 16 unit tests; OpenAPI spec (code complete, push blocked — GH_GLOBAL not set) |
| Per-Agent Trajectory Export | 2026-05-10 | GET /agent-trajectory.csv + .jsonl endpoints; one row per agent × round; belief_mean, stance, post_count, stance_changed, was_top_influencer; profile enrichment; EmbedDialog UI; 18 unit tests; OpenAPI spec; bilingual docs (code complete, push blocked — GH_GLOBAL not set) |

## Watched Repos
- `aaronjmars/aeon` — tracked in `memory/watched-repos.md`

## Lessons Learned
- Digest format: Markdown with clickable links, under 4000 chars
- Always save files AND commit before logging
- PAT lacks `workflows` scope — cannot push changes to `.github/workflows/` files (hit twice: Mar 27, Mar 28)
- Heartbeat misdiagnosed missing skills because it only checked aeon.yml, not messages.yml scheduler — fixed with scheduler diagnostics step
- Feature/repo-actions skills can waste CI runs building duplicate PRs — fixed with open PR dedup checks
- Auth credentials (ANTHROPIC_API_KEY or CLAUDE_CODE_OAUTH_TOKEN) can expire silently — all skills fail immediately with "Not logged in"; 15-day outage Apr 16–30 (ISS-001). Monitor consecutive_failures in cron-state.json.
- GH_GLOBAL secret not set — feature skill builds PRs locally but cannot push to watched repo; 10 consecutive blocks May 1–10 (Pre-Run Cost Estimator, Jupyter Notebook Export, Community Template Gallery, Agent Interrogation API, Simulation Impact Scorecard, One-Click Share to X, Simulation Quality Guard, Per-Round Annotation Layer, Agent Belief Heatmap, Per-Agent Trajectory Export stuck as local commits)

## Active Targets
- Hyperstition: MiroShark 500 stars — CLEARED 2026-04-07; 1K stars — CLEARED 2026-05-03 (1,022 stars)
- MIROSHARK ATH $0.000006926 set 2026-05-06 (surpassed old ATH $0.000004784 set Apr 26); $0.000006488 as of 2026-05-10 (-6.3% from ATH, near-full retest)
- Hyperstition: Will 5 independent Aeon forks ship custom skills by 2026-06-30? (filed 2026-05-02)
- Hyperstition: Will MiroShark be featured on a Chinese dev platform by 2026-06-15? (filed 2026-05-02)
- Hyperstition: Will a MiroShark simulation be cited in a peer-reviewed or pre-print paper by September 2026? (filed 2026-05-09)

## Open Issues
- None

## Next Priorities
- Set GH_GLOBAL secret — unblocks 10 built PRs (Pre-Run Cost Estimator, Jupyter Notebook Export, Community Template Gallery, Agent Interrogation API, Simulation Impact Scorecard, One-Click Share to X, Simulation Quality Guard, Per-Round Annotation Layer, Agent Belief Heatmap, Per-Agent Trajectory Export)
- Configure notification channels (Telegram, Discord, or Slack)
- XAI_API_KEY not set — tweet fetching falls back to WebSearch (limited freshness)
- Feature candidates (repo-actions 2026-05-10): Simulation Fork from Round, Agent Persona Library, Simulation A/B Comparison, Narrative Evolution Tracker, Gallery Creator Profiles
