*Push Recap — 2026-04-15*
MiroShark — 3 commits by 2 authors | miroshark-aeon — 17 commits by 2 authors

Browser Push Notifications (MiroShark PR #30): Full Web Push implementation shipped and merged. Users toggle a 🔔 during simulation runs and get a browser notification when it finishes — even with the tab backgrounded. VAPID key generation, subscription persistence, pywebpush dispatch, service worker, and cleanup on log deletion. Zero external services. Aaron hardened it with fcntl file locking and VAPID key security notes before merge.

Full Architecture Upgrade (miroshark-aeon): Single 130-file commit synced the upstream Aeon framework — 40+ new skill templates (deep-research, fleet-control, auto-merge, vuln-scanner, deploy-prototype, etc.), a chain-runner workflow for multi-step skill pipelines with output passing, MCP and A2A servers, a completely rewritten dashboard with component architecture, a Jekyll docs site, and six new utility scripts. The skill input in aeon.yml changed from a fixed dropdown to free-form string. This is the biggest commit in the repo's history.

README & Branding: Rewritten with "The most autonomous agent framework" tagline and refreshed visual assets. Bug fix: reactive trigger parser regex fixed (bash syntax). Heartbeat dispatch test confirmed auto-trigger works, then reverted.

Key changes:
- chain-runner.yml enables skill chaining with parallel execution + output passing between steps
- 40+ new skill templates staged (disabled by default, ready for configuration)
- Push notification toggle integrated into Step3Simulation.vue events-summary bar
- Dashboard page.tsx gutted from 1,531 lines to 93 — replaced by 15 focused components

Stats: ~170 files changed, +15,100/-2,520 lines across 20 commits
Full recap: https://github.com/aaronjmars/miroshark-aeon/blob/main/articles/push-recap-2026-04-15.md
