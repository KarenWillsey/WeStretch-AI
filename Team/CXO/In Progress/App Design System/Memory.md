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

3. **RESOLVED 2026-09-09: the prototype is on Fire Red, the green is gone.**
   - **Karen's call, verbatim: "red is right, green is drift. update everywhere."**
   - `Team/CXO/In Progress/Westretch-UX/src/styles/global.css` and
     `src/data/variants.json` were rewritten onto the brand palette.
     `npm run check` and `npm run build` both clean after the change.
   - Full before/after table lives in `Team/CXO/In Progress/Westretch-UX/Memory.md`.
   - **How to apply:** this kit and the prototype now agree. If they ever diverge
     again, the brand book wins, then this kit, then the prototype. Never the other way.

4. **Two colours in the prototype are intentionally off brand. Leave them.**
   - The badge screen brown gym backdrop (`#14100c`, `#2a2118`) is the 3D environment
     the brand book describes, not drift.
   - The reviewer hotspot debug highlight (`#14e39a` mint) is a dev-only overlay kept
     loud and off brand so it does not compete with the artwork. Turning it red would
     make it collide with every real Fire Red CTA.

## Website button alignment, 2026-09-12

5. **Primary buttons use the website CTA gradient.**
   - **Why:** Karen selected the website button as the sample for app design.
   - **How to apply:** use the shared core CTA token: `#FC4850` at 0%,
     `#FF5960` at 50% and `#E22931` at 100%. Keep the app's 48px minimum
     target and slight shadow. Fire Red remains `#FC4850`.
## Routine playback exception, 2026-09-13

Karen reported that the red Pause feels like quitting. Use neutral charcoal with white content for running-routine Pause, Resume and speed controls. At most one red CTA per screen is permitted, not required. Start and commit buttons retain the website gradient. Keep Exit separate and accessible. This supersedes any earlier mandatory-red interpretation for playback.
