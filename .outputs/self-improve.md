*Agent Self-Improvement — 2026-05-08*

Enforced structured angle deduplication in the project-lens skill. The previous prompt told the model to "check recent articles and pick a different angle" without defining a strict procedure — dedup was best-effort. Now Step 2 is a mandatory 5-part checklist: read recent article files, cross-reference memory log angle categories, build an exclusion list, pick only from unused categories, and skip entirely if all 8 are exhausted.

Why: project-lens runs 3x/week with 8 angle categories. Without structured dedup, the model could repeat angles, producing repetitive articles. The vague instruction also had no fallback — if all angles were used, it would force a duplicate rather than gracefully skipping.

What changed:
- skills/project-lens/SKILL.md: Replaced Step 2 with structured 5-part dedup procedure (read articles + logs → build exclusion list → pick unused → skip if exhausted)
- Added PROJECT_LENS_SKIP log pattern for graceful exhaustion handling

Impact: More diverse articles across the 3x/week schedule. No more risk of repeating the same angle category within 14 days. Graceful degradation when the rotation is exhausted.

PR: https://github.com/AITOBIAS04/miroshark-aeon/pull/6
