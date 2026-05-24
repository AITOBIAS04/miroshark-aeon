*Feature Built — 2026-05-24*

Simulation Tag System
MiroShark simulations now have semantic topic tags. Operators can label any published simulation with up to 5 free-text tags — 'governance', 'macro', 'elections', 'crypto', 'ai-regulation' — creating a vocabulary that makes the gallery navigable by topic rather than just by date or keyword search.

Why this matters:
The gallery had three discovery paths: recency, trending, and free-text scenario search. None supported semantic grouping. A researcher studying governance simulations had to search scenario text and hope the terminology was consistent. A curator building a citation bundle had to manually identify relevant sims. Tags add the missing semantic layer — filter by topic as a defined corpus, not a text-matching guess. For the weekly digest skill, tags enable structured reporting: '3 new governance simulations this week.' For the Aeon agent pipeline, tags are the first operator-defined metadata that travels with the simulation.

What was built:
- backend/app/services/tag_service.py: Pure-stdlib tag CRUD — validation (regex, length, array bounds), normalisation (lowercase, dedup), atomic JSON writes, aggregate corpus scan with 1-hour cache, trending detection (≥40% recent usage), gallery AND-filter logic
- backend/app/api/tags.py: 3 REST endpoints — POST /api/simulation/<id>/tags (admin-gated, 1–5 tags), GET /api/simulation/<id>/tags (public read), GET /api/tags (aggregate listing with counts + trending flags)
- backend/app/api/simulation.py: tags[] array added to every gallery card payload; ?tags=tag1,tag2 AND-filter on GET /api/simulation/public
- frontend/src/views/ExploreView.vue: Tag filter chip-group (horizontally scrollable, click to toggle AND-filter), tag chips on gallery cards (click to filter), Tags navigation chip linking to /tags
- frontend/src/views/TagsView.vue: Dedicated /tags browse page — grid of tag cards with counts, recent activity, and trending badges
- 14 unit tests + OpenAPI spec (Tags tag, 3 endpoints, TagEntry schema) + docs/FEATURES.md section

How it works:
Tags are stored as tags.json in each simulation's directory — one file per concern, matching the outcome.json/quality.json pattern. The tag service validates input (alphanumeric + hyphens, 1–32 chars, 1–5 per sim), normalises to lowercase, and writes atomically via tmp+rename. The aggregate GET /api/tags endpoint scans all published sim dirs, counts per-tag usage, and marks a tag as trending when ≥40% of its total usage falls within the last 30 days — cached for 1 hour. The gallery filter is AND logic: ?tags=crypto,governance returns only sims tagged with both. Zero new dependencies.

What's next:
Auto-suggest tags from scenario text via LLM at publish time. Tag-based digest sections in the weekly digest skill.

PR: push blocked — GH_GLOBAL secret not set (23rd consecutive feature blocked)
