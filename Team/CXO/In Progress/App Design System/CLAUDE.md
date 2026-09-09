# App Design System (CXO)

Owner: CXO. This is the **in app UI kit**. It covers what the user sees inside
the WeStretch app and nothing else.

It is **not** the brand. The brand core lives with the CMO at
`Team/CMO/In Progress/Brand System/core/`. This folder imports it and never
redefines a brand colour or font.

## Structure

```
tokens/app-tokens.css   App scale, spacing, touch targets, panel and CTA recipes
components/             Component previews, synced to claude.ai/design
```

## The rules that make this an app kit rather than a poster kit

1. **Minimum touch target 48px.** The audience is 50 to 65. Do not go smaller.
2. **Minimum body text 16.5px.** Same reason.
3. **One red button per screen.** The primary action is the big Fire Red button.
   Dismiss and Not now are small hyperlinks, never a second coloured button.
4. **Panels float.** 2D containers over the 3D gym background, 6% layer blur,
   `#1F1F1F` at 99% with a 1pt white 20% inner stroke.
5. **Corner radius is 10% of container width.** Use the `--app-radius-*` steps.

## Relationship to the Westretch-UX prototype

`Team/CXO/In Progress/Westretch-UX/` is the live React prototype. Its
`src/styles/global.css` currently uses a **green** palette that does not match
the brand guideline. That conflict is unresolved and logged in `Memory.md` and
`WORK-TRACKER.md`. Do not silently align one to the other. Ask Karen.

## Producing work

| Job | Use | Model |
|---|---|---|
| Screen mockup, flow, new UI render | `/design` canvas | Sonnet 5 |
| Push the kit to claude.ai/design | `/design-sync` | Sonnet 5 |
| Bulk variants, states, resizing | `ws-design-bulk` subagent | Haiku 4.5 |
| Changing tokens or component architecture | `ws-brand-architect` subagent | Opus 5 |
