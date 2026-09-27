# Marketing Formats

Canvas sizes for every marketing surface. Use these exact dimensions when
asking for a render so nothing has to be re-cropped later.

## Paid social and ads

| Format | Size (px) | Notes |
|---|---|---|
| Meta feed square | 1080 x 1080 | Safe area 8% inset |
| Meta feed portrait | 1080 x 1350 | Best performing feed size |
| Story / Reel / TikTok | 1080 x 1920 | Keep copy out of top 250px and bottom 350px |
| Google Display leaderboard | 728 x 90 | Logo plus one line only |
| Google Display MPU | 300 x 250 | Logo plus one line plus CTA |
| Google Display half page | 300 x 600 | |
| Google Display responsive | 1200 x 628 and 1200 x 1200 | Both required |
| YouTube thumbnail | 1280 x 720 | Face plus 3 to 5 words max |

## News portal display (Pattison Media)

Responsive HTML5 units that run on Pattison Media news portals. One HTML5 file
per unit reflows across every screen size, so each unit is supplied as a set of
key formats, not a single flattened image. The program fills the in-between
sizes itself once the key formats exist.

| Unit | Key formats (px) | Where it sits |
|---|---|---|
| Mid content | 1940 x 535, 1920 x 1080, 1200 x 1200 | Inside the main article content |
| Sticky box | 1200 x 1200, 1940 x 535, 1920 x 1080 | Right sidebar |
| Full page | 1920 x 1080, 768 x 1024, 320 x 568 | Middle of the page, revealed by scrolling |
| Full width bookend | 2560 x 180, 1940 x 535, 1200 x 1000 | Top and bottom of the site |

Supply all three key formats for a unit. Missing one leaves the builder
guessing at the sizes between.

### What Pattison needs from us

1. **Every element as its own file.** Logo, background, photograph, headline
   text, button and video each ship separately, so they can be moved
   independently at each size. A flattened export of a finished layout cannot be
   made responsive and will be sent back.
2. **Asset formats:** high resolution PNG or JPG for graphics, MP4 for video, or
   a YouTube or Vimeo link.
3. **Working files, accepted and preferred:** PDF, PSD, AI, EPS or SVG.

House rules for these units, on top of the universal rules below:

- 2560 x 180 bookend is a 14:1 strip. Logo, 4 words, CTA. Nothing else fits.
- 320 x 568 is the phone full page. Same message as 1920 x 1080 with the
  headline cut to one line.
- The 1200 x 1200 and 1920 x 1080 layouts reuse the Meta square and the web hero
  art. Build those first and the rest are crops.

Contact for spec questions: Pattison Media, 250.372.3322, info@pattisonmedia.com.
Source: `Knowledge Base/Pattison Media Responsive Ads Size Guide.pdf`.

## Organic social

| Format | Size (px) |
|---|---|
| Instagram post | 1080 x 1350 |
| Instagram carousel slide | 1080 x 1350 |
| Facebook post | 1200 x 630 |
| LinkedIn post | 1200 x 627 |
| Pinterest pin | 1000 x 1500 |

## Email

| Element | Spec |
|---|---|
| Body width | 600px |
| Hero image | 1200 x 600 (retina, displayed at 600 x 300) |
| Minimum body text | 16px |
| CTA button | Fire Red, minimum 44px tall, full width on mobile |
| Dark mode | Test both. Logo needs a light and dark variant. |

## Out of home

| Format | Size | Ratio | Rule |
|---|---|---|---|
| Billboard (bulletin) | 14 x 48 ft | 1:3.43 | 7 words maximum |
| Digital billboard | 1400 x 400 px | 3.5:1 | 6 words maximum, no fine print |
| Transit shelter | 47 x 68 in | portrait | Read from 15 ft |
| Poster | 24 x 36 in at 300 dpi | | Print files use the CMYK values in brand-core.json |

## Web

| Element | Spec |
|---|---|
| Hero | 1920 x 1080 art, content safe to 1440 |
| Section image | 1200 x 800 |
| Open Graph | 1200 x 630 |
| Favicon | 512 x 512 source |

## Universal rules

1. Logo clearance is the width of the `w` on every side. Never tighter.
2. The primary action is always the Fire Red button. Never a second colour.
3. Print uses the CMYK hex values, screens use the web hex values. They differ. See `core/brand-core.json`.
4. Work Sans Bold for display headlines. Inter for everything else.
5. Photography: adults 50 to 65, warm, photorealistic, optimistic. Healthy and active, not athletes or fitness models. See the CMO image brief.
