*Push Recap — 2026-04-30*
MiroShark — 4 commits by @aaronjmars | miroshark-aeon — 1 commit by @aaronjmars

Simulation Transcript Export: MiroShark now exports per-round agent transcripts as Markdown (with YAML front matter for Notion/Obsidian/Substack) or structured JSON (for SDKs and LLM-as-judge pipelines). Completes the trio of share formats alongside share card and replay GIF. 615-line renderer, 493-line test suite, EmbedDialog integration, OpenAPI spec coverage.

Wonderwall Per-Slot Endpoint Override: The simulation loop (850+ calls/run) can now target a self-hosted vLLM, Modal deployment, or fine-tune via WONDERWALL_BASE_URL + WONDERWALL_API_KEY — without touching Default/Smart/NER slots. The "Best" preset (~$3.50/run) is retired; a single "Cloud" preset (Mimo V2 Flash + Grok-4.1 Fast, ~$1/run) is the new default.

Observability Hardening: Pagination endpoints no longer 500 on malformed query strings — Flask type=int coercion replaces raw int() casts.

Skill Leaderboard Fix: skill-leaderboard now scans all watched repos instead of just the first, so it actually reaches the aeon instance repo.

Key changes:
- New backend/app/services/transcript.py (615 lines) — pure-stdlib transcript renderer with ±0.2 stance threshold parity across all surfaces
- .env.example completely rewritten — Cloud preset is the active default, Ollama/Claude Code moved to Alternatives block
- backend/lib/env_compact.py — CI refactor splits compaction helpers out of wonderwall package to avoid numpy/torch imports in tests

Stats: ~40 files changed, +2,301/-418 lines
Full recap: https://github.com/AITOBIAS04/miroshark-aeon/blob/main/articles/push-recap-2026-04-30.md
