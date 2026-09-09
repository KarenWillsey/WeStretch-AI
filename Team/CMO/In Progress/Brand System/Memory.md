# Brand System, Memory

Durable facts for this folder only. Cross role facts go in the repo root `Memory.md`.

## Established 2026-09-09 (folder created)

1. **Architecture decision: one brand core, two skins.**
   - **Why:** Karen asked whether in app UI should be separate from global
     branding. Fully separate means the app and the ads drift apart. Identical
     means the app inherits billboard sized type. Two skins on one core is the fix.
   - **How to apply:** `core/` is shared and owned here by the CMO. The app skin
     lives under CXO and imports `core/tokens.css`. Never duplicate a colour or
     font value into a skin.

2. **Brand values are extracted from the official PDF, not invented.**
   - Source: `Knowledge Base/Brand Guildeline.pdf`, 47 pages.
   - Primary: Fire Red `#FC4850`, Midnight Grey `#1F1F1F`, Dark Grey `#4C4C4C`, White.
   - Secondary: Sunshine Gold `#FBBC05`, Lavender Blue `#667FD4`, Light Grey `#E4E4E4`, Medium Grey `#ADACAC`.
   - Type: Work Sans Bold for display, Inter Regular/SemiBold/Bold for everything else.
   - Print CMYK hex values differ from web hex values. Both are recorded in `core/brand-core.json`. Do not use web values on a print job.

3. **RESOLVED 2026-09-09: the app palette was drift, not a new direction.**
   - The Westretch-UX prototype had been running a green system
     (`--variant-accent: #178f78`, `--variant-dark: #0b5f51`, `--variant-soft: #dff6ef`)
     plus a slightly-off red (`#ff3946`, `#e8423a`). None of it appears in the brand book.
   - **Karen's call, verbatim: "red is right, green is drift. update everywhere."**
   - The prototype is now on Fire Red. Full change table is in
     `Team/CXO/In Progress/Westretch-UX/Memory.md`.
   - **How to apply going forward:** `Knowledge Base/Brand Guildeline.pdf` is the
     authority. If any surface disagrees with it, the surface is wrong. Do not treat
     a colour that shipped in a prototype as evidence that it is brand.

4. **The app's red was close but not exact, and that counted as drift too.**
   - The prototype CTA gradient was `#ff7b6b` to `#e8423a`. The brand ramp is
     `#FC7E84` to `#E24048`. Near enough to look right in isolation, wrong when
     placed next to a correctly built asset.
   - **How to apply:** never eyeball a brand colour. Copy the hex out of
     `core/brand-core.json` or `core/tokens.css`.

5. **Open, smaller: the Pro and Lite concept variants are still off brand on purpose.**
   `westretch-pro` uses purple `#7357d8`, `westretch-lite` uses coral `#e25d4f`.
   They are alternate product concepts for different audiences, so being visually
   distinct is the point. Left unchanged in the 2026-09-09 sweep. Karen has not
   said whether they should eventually come onto the brand core.
