*Push Recap — 2026-05-04*
[MiroShark] — 1 commit by @aaronjmars (+ 25 automated on miroshark-aeon)

Shareable Scenario Links (PR #71, merged): The last missing distribution primitive lands. Drop a ?scenario=...&url=... URL into a tweet or blog post and readers land on the New Sim form already pre-filled — one click from launching their own run. Four independent params (scenario, url, ask, template) each sanitized by DOMPurify with length caps. A "Share as link" button beneath the Simulation Prompt textarea copies the URL from live form state. Template gallery cards gain a link icon for one-click ?template=<slug> CTAs. Pure frontend, zero new deps, 27 parser assertions pass.

Self-Improvement (PR #29, open): The project-lens angle rotation rule ("Never repeat in 14 days") was mathematically impossible — 8 categories on a daily cadence means day 9 forces a repeat. Every entry from Apr 22–May 2 violated the rule and wrote a rationalization. Replaced with least-recently-used selection + 6-day soft floor + explicit override paths.

Key changes:
- New frontend/src/utils/urlParams.js (116 LoC) — centralized URL param sanitization shared by read path (mount) and write path (share buttons)
- Home.vue +385 lines — onMounted prefill, orange banner for shared-link awareness, share-as-link button with clipboard copy
- TemplateGallery.vue — link icon on every template card for ?template=<slug> share URLs

Stats: 6 files changed, +613/-12 lines
Full recap: https://github.com/AITOBIAS04/miroshark-aeon/blob/main/articles/push-recap-2026-05-04.md
