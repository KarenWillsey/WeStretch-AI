# App Design System, Memory

Durable facts for this folder only.

## Established 2026-09-09 (folder created)

1. **This folder is a skin, not a brand.**
   - **Why:** Karen asked whether in app UI should be kept separate from global
     branding. The decision was one shared brand core owned by the CMO, with an
     app skin here and a marketing skin under the CMO.
   - **How to apply:** `tokens/app-tokens.css` imports the CMO brand core. If you
     find yourself typing a hex code here, stop. It belongs in the core.

2. **Accessibility floors are set by the audience, not by convention.**
   Minimum 48px touch target and 16.5px body text, because the audience is
   adults 50 to 65. These are not negotiable per screen.

3. **OPEN CONFLICT: the Westretch-UX prototype palette is green, the brand is red.**
   - Prototype: `--variant-accent: #178f78`, `--variant-dark: #0b5f51`,
     `--variant-soft: #dff6ef`, plus reds `#ff3946` and `#e8423a`.
   - Brand guideline: Fire Red `#FC4850`, Midnight Grey `#1F1F1F`.
   - Neither is wrong yet. Karen decides whether green is a new direction to
     promote into the brand core, or drift to correct.
   - Same item is logged in the Brand System `Memory.md` and `WORK-TRACKER.md`.
