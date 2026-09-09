# Brand System (CMO)

Owner: CMO. This folder is the **single source of truth for the WeStretch brand**.

Extracted from `Knowledge Base/Brand Guildeline.pdf` (47 pages, the official
brand book). If this folder and the PDF ever disagree, the PDF wins and this
folder gets corrected.

## Structure

```
core/            Shared brand truth. Both skins build on this. Never bypass it.
  tokens.css       Colour, type and shape as CSS variables
  brand-core.json  The same values as data, for tools and renderers
  voice.md         Copy rules that constrain design output
marketing/       The marketing skin
  marketing-tokens.css  Scale and spacing for ads, email, print, web
  formats.md            Exact canvas sizes for every surface
components/      Marketing component previews, synced to claude.ai/design
```

The **app skin** lives in `Team/CXO/In Progress/App Design System/` and imports
`core/tokens.css` from here. That is deliberate. One core, two skins.

## How to work in this folder

- **Changing a brand colour, font or the logo rule** means editing `core/`.
  That change ripples into the app. Flag it to Karen before doing it.
- **Changing an ad size, a spacing scale or a marketing layout** means editing
  `marketing/`. That is safe, it does not touch the app.
- **Making a new piece of creative** does not mean editing this folder at all.
  Read the tokens, then use the `/design` skill or a Higgsfield skill to produce it.

## Producing creative

| Job | Use | Model |
|---|---|---|
| Ad layout, poster, social graphic, email design | `/design` canvas | Sonnet 5 |
| Photoreal image, video, billboard art | `higgsfield-generate` | Sonnet 5 |
| Full visual identity extension, brandbook pages | `higgsfield-brandkit` | Sonnet 5 |
| Bulk copy variants, resizing, alt text | `ws-design-bulk` subagent | Haiku 4.5 |
| Changing `core/`, brand architecture decisions | `ws-brand-architect` subagent | Opus 5 |

## Syncing to claude.ai/design

`/design-sync` pushes `components/` up to a Claude Design project so the
marketing kit is visible as cards. The repo stays the source of truth.
Never edit on claude.ai and expect it to come back down.
