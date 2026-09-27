# Dark Mode support + Dark Mode screenshot

**Backlog item:** "Confirm whether WeStretch's app supports Dark Mode, and if
so add at least one Dark-Mode screenshot to the product page."
(added 2026-09-01 by the monthly-refresh run)

**Date:** 2026-09-08 (scheduled nightly run)
**Nothing was submitted or changed on Apple's side.**

---

## Bottom line

**The screenshot half of this item is already done, and nobody knew it.**

All 10 live iPhone screenshots (and all 10 iPad screenshots) already show a
dark app UI on a dark caption band. There is no "add at least one Dark-Mode
screenshot" work to do. The product page is 100% dark, not 10%.

**The item's premise is backwards.** It assumed WeStretch has a light
product page that might be missing a dark screenshot. The real situation is
the inverse: WeStretch appears to be a **dark-themed app**, and the open
question is whether it has a **Light Mode at all**.

That question has two possible answers, and they lead to opposite actions:

| If the app is... | Then... | Action |
|---|---|---|
| **Adaptive** (follows the system Light/Dark setting) | The product page shows only the Dark side. A user with their phone in Light Mode downloads and sees an app that doesn't match the screenshots. | Add at least one **Light Mode** screenshot — the reverse of what this item says. |
| **Fixed dark** (always dark, ignores the system setting) | Apple's "include a Dark Mode screenshot" guidance is satisfied trivially and there is nothing to add. | Nothing for the product page. Note the HIG gap (below) and move on. |

**I cannot tell which from outside the app.** That needs one line of the
Info.plist. The checklist is in section 3.

---

## 1. What I verified, and how

Reproducible without App Store Connect, using the public sources recorded in
this project's `Memory.md` (2026-09-06 note).

Read the live listing:

```
curl -s "https://itunes.apple.com/lookup?id=1458915362&country=us"
```

Live listing state as of tonight:

| Field | Value |
|---|---|
| App name | WeStretch: Custom Stretches |
| Version | 8.1.32 |
| Version released | 2026-09-03 |
| Minimum iOS | 15.2 |
| Rating | 4.45 (53 ratings) |

Then downloaded all 10 iPhone screenshots at 600px wide (swap the
`/320x480bb.jpg` suffix on the returned URLs for `/600x0w.png`), measured
mean luminance on each, and **visually inspected three of them** rather than
trusting the numbers alone — a dark *photo* is not the same as a dark *UI*.

### The 10 live iPhone screenshots

| # | Filename (Apple's, from the URL) | Mean luma (0-255) | App UI shown |
|---|---|---|---|
| 01 | `01_TL_LadieSitNeckStretch.png` | 94.0 | dark |
| 02 | `02_TL_PhysioAndLadie.png` | 112.5 | dark |
| 03 | `03_TL_PickleBallPlayer.png` | 79.4 | dark |
| 04 | `04_TL_LadieBirdDog.png` | 121.0 | dark |
| 05 | `05_RoutineTypes.png` | 70.6 | dark — **inspected** |
| 06 | `06_RoutineLength.png` | 65.5 | dark |
| 07 | `07_UniqueRoutine.png` | 88.9 | dark |
| 08 | `08_Walking_3_People.png` | 112.0 | dark |
| 09 | `09_RoutineFilters.png` | 112.3 | dark — **inspected** |
| 10 | `10_InAppProgress.png` | 76.4 | dark — **inspected** |

The mid-range luma values (02, 04, 08, 09) are bright *lifestyle photography*
with a dark app UI composited on top. #09 is the clearest example: a sunlit
living room with a near-black "Body Filter" sheet on the phone. So the luma
number understates how dark the UI is. Every single screen is dark.

What the three inspected screenshots actually show:

- **#05 Routine Types** — near-black modal sheet, white text, red selection
  outlines, on a dark caption band.
- **#09 Routine Filters** — dark "Body Filter" sheet, white labels, red
  anatomy figure, red Save button.
- **#10 In-App Progress** — dark streak/coins UI, white and gold text, red
  Continue button.

### Two corroborating signals that this is deliberate, not accidental

1. **The brand palette is dark.** `App Store Image Creation/Memory.md`
   records the approved palette as Fire Red #FC4850, White #FFFFFF, Midnight
   Grey #1F1F1F, with the screenshot caption band a charcoal gradient
   RGB(12,13,14) to RGB(30,30,31). The dark product page is on-brand by design.
2. **The redesign is dark too.** I sampled 12 of the 192 screen images in the
   CXO redesign prototype (`Team/CXO/In Progress/Westretch-UX/public/screens/westretch/`).
   11 of 12 are dark (mean luma 21-107). So there is **no risk of the
   redesign flipping the app to light and making the current screenshots
   stale** — a real risk I checked for and can rule out.

---

## 2. What this changes about the backlog item

Recommend the item be **closed as already satisfied**, and replaced with the
narrower question it actually surfaced:

> Does WeStretch respect the system Light/Dark appearance setting, or is it
> hard-locked to dark? If it is adaptive, the product page needs a Light Mode
> screenshot.

I have added that as a decision line in `WORK-TRACKER.md` rather than
inventing a new backlog item myself (seeding the backlog is the monthly
refresh's job, or Karen's/the Manager's).

---

## 3. Checklist — for whoever has the iOS project or App Store Connect

This skill has no access to the native app's source or build config, so I
cannot answer this myself. Five minutes for someone who does.

### Check A — the decisive one: Info.plist

**Where:** the iOS app target's `Info.plist` (or Xcode, target, Info tab).

**Look for the key** `UIUserInterfaceStyle`.

| What you find | What it means |
|---|---|
| Key is **absent** | App is **adaptive**. It follows the system setting and genuinely supports Dark Mode. Go to Check B. |
| `UIUserInterfaceStyle = Dark` | App is **hard-locked to dark**. It does not "support Dark Mode" in Apple's adaptive sense; it simply is dark. Go to Check C. |
| `UIUserInterfaceStyle = Light` | Would contradict the screenshots. If you see this, something is overriding it in code — search for `overrideUserInterfaceStyle`. |

**Also search the codebase for** `overrideUserInterfaceStyle` — a per-window
or per-view-controller override there can lock the appearance even when the
Info.plist key is absent. If the app is a Unity/hybrid build (there is a
`UNITY-HANDOFF.md` in the UX repo), the theme may be set on the Unity side
instead and this key will tell you nothing; in that case run Check B
empirically instead.

### Check B — only if the app is adaptive

**Where:** any iPhone or the iOS Simulator.

1. Settings, Display & Brightness, **Light**.
2. Open WeStretch. Walk: home, pick a routine, routine player, paywall,
   settings.

**Pass looks like:** a genuinely light UI — light backgrounds, dark text,
readable throughout, nothing washed out, no white-on-white text, no invisible
icons.

**If it passes:** the product page is misrepresenting the app for every
Light Mode user. Capture at least one Light Mode screenshot and add it to the
product page — route the request through
`Team/CMO/In Progress/App Store Specialist/App Store Image Creation/`, which
owns the screenshot build pipeline and the caption template. Note that the
approved caption band is charcoal, so a Light Mode screen will need a
template decision from that project, not just a new source image.

**If it fails** (light mode exists but looks broken): that is a bug, and a
worse one than the screenshot gap. Raise it to the CTO/CXO, not here.

### Check C — only if the app is hard-locked to dark

Nothing to do for the product page. Two things worth recording:

1. **Apple's guidance is satisfied.** The Knowledge Base line ("if the app
   supports Dark Mode, include at least one screenshot showing Dark Mode",
   `Knowledge Base/apple-marketing-opportunities.md`, source
   `developer.apple.com/app-store/product-page/`) is met — every screenshot
   is a Dark Mode screenshot.
2. **There is a HIG gap, but it is not a review risk.** Apple's Human
   Interface Guidelines expect apps to respect the system appearance. Apple
   does **not** reject apps for shipping a fixed dark theme, and a fixed-dark
   theme is a normal, defensible choice for a fitness/video app where the
   content is the focus. Treat this as design debt to decide on deliberately,
   not as something to fix reflexively.

---

## 4. Recommendation

1. **Do not commission a Dark Mode screenshot.** It already exists, ten times over.
2. **Run Check A.** It is one Info.plist key and it decides everything else.
3. **If the app turns out to be adaptive, the real work is a Light Mode
   screenshot** — the opposite of what the backlog item asked for — and it
   should go to the App Store Image Creation project with a template decision
   attached (the charcoal caption band was designed against dark source screens).
4. **If the app is fixed dark, close this line of work.** Record the
   fixed-dark decision in this project's `Memory.md` so a future monthly
   refresh does not re-raise the same Dark Mode item a third time.

---

## 5. What I did not do

- **Did not confirm Dark Mode support.** I have no access to the iOS project,
  Xcode, or a device running the app. Everything above about the app's *theme*
  is inferred from public screenshots; nothing above claims the app *supports*
  (adaptive) Dark Mode. That distinction is the whole point of Check A.
- **Did not touch the product page.** No screenshots uploaded, replaced, or
  reordered; no App Store Connect access and no live actions from this skill.
- **Did not produce any screenshot assets.** Per this skill's routing rule,
  asset work goes to `App Store Image Creation/` with a brief, which is what
  Check B hands over if it is triggered.
- **Did not add a backlog item.** Seeding the backlog is the monthly refresh's
  job; the follow-up question is on `WORK-TRACKER.md` as a decision for Karen
  instead.
