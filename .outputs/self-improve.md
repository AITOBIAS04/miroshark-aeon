*Agent Self-Improvement — 2026-05-22*

MEMORY.md consolidated from 13KB to 2.8KB (79% reduction) by extracting verbose tables into topic files.

Why: Every skill run reads MEMORY.md. The Skills Built table had 21 entries with 100+ word descriptions, Recent Articles had 8 verbose entries, and Lessons Learned had 9 detailed bullets — all adding ~2,500 unnecessary tokens to every skill context window. CLAUDE.md specifies ~50 lines; MEMORY.md was 82 lines / 13KB.

What changed:
- memory/MEMORY.md: Compact summaries with links to topic files (82→64 lines, 13KB→2.8KB)
- memory/topics/skills-built.md: NEW — full Skills Built detail table
- memory/topics/articles.md: NEW — full Recent Articles table
- memory/topics/lessons-learned.md: NEW — full Lessons Learned with context

Impact: ~2,500 fewer tokens per skill run × 15+ daily runs = ~37,500+ tokens/day saved in context overhead. All detail preserved in topic files for skills that need it.

PR: https://github.com/AITOBIAS04/CHORUS/pull/10
