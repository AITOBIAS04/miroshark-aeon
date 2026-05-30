*Push Recap — 2026-05-30*
aaronjmars/MiroShark — 3 commits by 1 author (@aaronjmars + Claude Opus 4.8)

Design System Port (PR #127): Ported the miroshark.xyz marketing-site aesthetic into the entire in-app frontend. Deep-space nebula background + animated star field behind every route. Branded boot splash with chrome shark that cross-fades on mount. New site footer. App.vue now exports reusable design-system classes (chrome-text, glossy-panel, metal pills). All views restyled.

Button & Typography Cleanup (PR #128): Caught everything the initial port missed. The Explore page — primary discovery surface — got a complete restyle: flat rectangles → glossy round pills, gallery cards → rounded panels, bullish/bearish green/red → violet/fuchsia. Purged all 73 stray Young Serif / Space Mono references. Dropped retired fonts from Google Fonts link.

Embed Dialog & Sentiment Palette (PR #129): The embed dialog was the last major light-themed widget inside the dark app — re-themed end-to-end. Unified the sentiment color palette across all charts and network graphs from teal/red to brand violet/fuchsia. Fixed the replay playback bar, which was entirely invisible (white bar, light text).

Key changes:
- App.vue (+419/-34): centralized design system with reusable CSS classes, global nebula/starfield, Geist typography
- ExploreView.vue (+172/-83): complete gallery page restyle, all controls → glossy pills
- EmbedDialog.vue (+188/-186): full dark retheme, invisible controls fixed, violet gradient buttons

Stats: 34 files changed, +1,750/-824 lines
Full recap: https://github.com/AITOBIAS04/CHORUS/blob/main/articles/push-recap-2026-05-30.md
