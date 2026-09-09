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

3. **OPEN CONFLICT: the Westretch-UX prototype does not use the brand palette.**
   - `Team/CXO/In Progress/Westretch-UX/src/styles/global.css` defines a green
     system (`--variant-accent: #178f78`, `--variant-dark: #0b5f51`,
     `--variant-soft: #dff6ef`) and a different red (`#ff3946`, `#e8423a`),
     none of which appear in the brand guideline.
   - **Not resolved.** Karen has to decide: is the prototype green an
     intentional new direction that should be promoted into the brand core, or
     is it drift that should be corrected back to Fire Red?
   - Tracked in `WORK-TRACKER.md`.
