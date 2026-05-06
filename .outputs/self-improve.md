*Agent Self-Improvement — 2026-05-06*

Push-Access Pre-Flight Guard
The feature and external-feature skills now check for push access to the target repo before doing any work. If GH_GLOBAL isn't set, they exit immediately instead of spending 10-30 minutes building code that can't be delivered.

Why: The feature skill ran 6 consecutive days (May 1–6), each time building a complete implementation (~1000+ lines), only to fail at the push step because the GH_GLOBAL secret isn't configured. Six features are stuck as local commits — Pre-Run Cost Estimator, Jupyter Notebook Export, Community Template Gallery, Agent Interrogation API, Simulation Impact Scorecard, and One-Click Share to X.

What changed:
- skills/feature/SKILL.md: Added step 2 — verify push access via gh api repos/.../permissions.push before picking features, cloning repos, or writing code
- skills/external-feature/SKILL.md: Added step 3 — same push-access guard before cloning or implementing

Impact: Prevents wasting compute and tokens on features that can't be pushed. Until GH_GLOBAL is set, these skills will exit cleanly in seconds instead of running full build cycles. Once the secret is configured, the guard passes and skills resume normal operation.

PR: https://github.com/AITOBIAS04/miroshark-aeon/pull/5
