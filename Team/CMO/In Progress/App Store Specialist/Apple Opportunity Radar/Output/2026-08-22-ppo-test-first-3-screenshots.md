# PPO Test Plan; First 3 Screenshots

Addresses backlog item: "Optimize the first three screenshots and set up a Product Page Optimization (A/B) test."
Date: 2026-08-22 (nightly-action run)

This item has two parts. Part A is a production brief for the existing
screenshot pipeline (asset-shaped, routed there rather than improvised
here). Part B is the actual Product Page Optimization test plan
(drafting-shaped, drafted in full below, ready for Karen/Manager review).
Nothing here has been submitted to App Store Connect; this is a plan for a
human to execute.

## Why screenshots 1–3 specifically

Per `Knowledge Base/apple-marketing-opportunities.md` ("Screenshots and
Videos" + "App Store A/B Testing"):
- Only screenshots 1–3 can surface in search results; they carry more
  weight than 4–10.
- Screenshot 1 should carry the single strongest customer benefit.
- Apple's own PPO guidance explicitly calls out testing different
  **first-screenshot headlines** as a standard, high-leverage test.

Current default set (`App Store Image Creation/Output/Default A/`, most
recent build `Run_02`) already has 3 delivered concepts (V1/V2/V3) built on
`App Store Image Text Copywriting/Output/Default/app-store-copy-default-cold-audience.md`.
That copy doc has already been through a full Chase → Expert → Marg
grading loop plus a human review pass (Kari, 2026-08-10); it's the
strongest existing copy asset and is used as the **control** below rather
than being rewritten from scratch.

## Part A; Brief for the Image Creation + Copywriting pipelines

Hand this to `App Store Image Creation/` (visuals) and
`App Store Image Text Copywriting/` (any new copy needed) as a new job.
This nightly-action skill does not generate final assets itself (per its
own scope); this is the spec for that pipeline to execute.

**Scope of the ask:** produce 3 alternative treatments for **screenshot 1
only**. Screenshots 2 and 3 stay as currently built (Default A / Run_02,
V1 and V2) in all 4 variants (control + 3 treatments); this isolates the
single highest-leverage variable (the opening headline/benefit) per
Apple's own recommended PPO practice, instead of re-testing the whole
3-screenshot set at once, which would make it impossible to tell which
change moved the number.

Each treatment reuses copy that has **already been graded** in the
existing copywriting doc, no new copywriting loop needed, just new
compositing:

| Variant | Screenshot 1 title | Screenshot 1 subtitle | Angle | Source |
|---|---|---|---|---|
| Control (current) | Not another one-size-fits-all fitness app | Answer a few questions. It builds a routine for your body. | Differentiation / belonging | Screen 2, existing default copy |
| Treatment 1 | Tell it what hurts. It works around it. | ((video card, no subtitle needed) reads standalone per copy doc's rule) | Safety / personalization | Video card 4, existing copy (already graded A-, flagged in copy doc as "transplant" candidate for exactly this kind of use) |
| Treatment 2 | Physio-informed, every pose | Licensed physiotherapists mapped safe movement for real joints. | Authority | Screen 3, existing default copy |
| Treatment 3 | You're not 20 anymore. Your app shouldn't pretend you are. | A routine for your body. Not a template for everyone. | Tribe / emotion | Video cards 1+2 combined, existing copy, strongest-graded opener (3.74, A-) in the whole doc, not yet tested as a still screenshot |

**Production notes for `App Store Image Creation/`:**
- Same source image/composition already used for the current screenshot 1
  (Default A) is fine to reuse across all 4 variants, only the
  title/subtitle text should change. This keeps the test to a pure
  copy/headline test, not a confounded photo+copy test.
- Follow the standing gates in that project's `Memory.md` as usual
  (spelling/grammar confirmation before render, pre-delivery review,
  calibrated title/subtitle typography specs). Treatment 1 has no
  subtitle; confirm the template's no-subtitle title placement rule
  (3-line title allowed only with no subtitle) is used, matching how the
  video card was designed to stand alone.
- Suggested output structure matching this project's existing convention:
  `Output/PPO Test - Screenshot 1 Headlines/Run_01/`, one screenshot-1
  PNG per treatment (Treatment 1/2/3), at both required export sizes.
  Control does not need re-rendering: it already exists in
  `Output/Default A/Run_02/`.

## Part B; Product Page Optimization test setup (App Store Connect)

Drafted directly from `Knowledge Base/apple-marketing-opportunities.md`
"App Store A/B Testing" section. To be entered into App Store Connect by
whoever holds that access; not something this skill can submit.

- **Test type:** Product Page Optimization (default product page test,
  not a Custom Product Page test).
- **Original:** current default page (screenshots 1–3 = Default A
  Run_02's V1/V2/V3, screenshot 1 = control copy above).
- **Treatments (up to 3, using Apple's full allowance):**
  - Treatment 1: screenshot 1 swapped to "Tell it what hurts" copy.
  - Treatment 2: screenshot 1 swapped to "Physio-informed, every pose" copy.
  - Treatment 3: screenshot 1 swapped to "You're not 20 anymore" copy.
  - Screenshots 2 and 3 identical across all 4 arms (see Part A rationale).
- **What's being isolated:** first-screenshot messaging angle only
  (differentiation vs. safety/personalization vs. authority vs.
  tribe/emotion), the four FATE-lever angles already identified in the
  copywriting project's Chase strategy work.
- **Traffic allocation:** even split across all 4 arms (App Store Connect
  default) unless Karen wants to weight it, no reason to deviate here
  since all 4 are pre-graded, viable candidates rather than a wild-card
  variant.
- **Primary metric:** product page conversion rate (App Store page view →
  download), per the Knowledge Base's Analytics section; this is the
  metric App Store Connect reports natively for PPO tests.
- **Duration:** run until statistical significance is reached in App Store
  Connect's own reporting; Apple does not guarantee a fixed timeline. Set
  a checkpoint to review results after ~2–3 weeks of live traffic rather
  than a hard stop date, since WeStretch's current install volume is
  unknown to this skill and duration needed for significance scales
  with it.
- **Winner handling:** apply the winning arm's screenshot 1 to the actual
  default product page once the test concludes (per Knowledge Base:
  "Apply the winning version to the default product page"). Do not treat
  a non-significant result as a loss, re-test with a new angle instead
  (per "Continue testing regularly").
- **Follow-on test (not this round):** once a screenshot-1 winner is
  locked in, a logical next PPO round is screenshot **order** (2 vs 3
  swapped) or testing the app icon, per the same Knowledge Base section (flagged here as a future backlog candidate, not added to `Backlog.md`
  automatically (per this skill's own scope) seeding new items is the
  monthly refresh's or Karen's job).

## What this skill could not do

- Could not create or submit the actual PPO test in App Store Connect (no
  access from this skill, and live submission is explicitly out of scope
  for this skill regardless).
- Could not render the 3 new screenshot-1 images, handed to
  `App Store Image Creation/` as a brief (Part A) per this skill's own
  routing rule for asset-shaped work.
