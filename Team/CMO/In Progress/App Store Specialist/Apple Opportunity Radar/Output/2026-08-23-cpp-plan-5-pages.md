# Custom Product Pages; Launch Plan (Back Pain, Stiffness, Mobility, Golf, Pickleball)

Addresses backlog item: "Create Custom Product Pages for back pain,
stiffness, mobility, golf, and pickleball."
Date: 2026-08-23 (nightly-action run)

This item spans two kinds of work. Part A (page structure, keyword
fields, promotional text, screenshot-1 direction, deep-link targets) is
drafted directly below; it's copy/planning work within this skill's
scope. Part B (the remaining 8 screenshots and app-preview video per
page) is asset/full-copy-loop work and is routed as a brief to the
existing `App Store Image Creation/` and `App Store Image Text
Copywriting/` pipelines rather than improvised here, per this skill's own
routing rule. Nothing here has been submitted to App Store Connect,
this is a plan for a human to execute.

## Source and constraints

Drawn from `Knowledge Base/apple-marketing-opportunities.md` → "Custom
Product Pages":
- Up to 70 custom pages allowed; each gets its own screenshots, previews,
  promotional text, and keyword targeting.
- Match each page to the searcher's intent; use unique URLs; can be
  submitted independently of app updates.
- Apple's own published stats: CPPs average +2.5pp conversion vs. the
  default page (156% relative lift); cited case studies up to +33%
  conversion.
- CPPs are compatible with Apple Search Ads (Search tab placements,
  `customProductPageIdentifier` on StoreKit-rendered ads), each page
  below should become the ad landing target for its matching search terms
  once Apple Search Ads work starts.
- Deep links into the app require iOS 18/iPadOS 18+. **Backlog already
  has an open item; "Confirm WeStretch's minimum iOS/iPadOS deployment
  target supports iOS 18+"; still not started.** This does not block
  creating the 5 pages themselves (screenshots, copy, keywords all work
  today); it only blocks the deep-link field on each page. Recommend
  resolving that backlog item before submitting deep links, and shipping
  these 5 pages without deep links in the meantime if a launch date
  matters more than waiting.
- App name/subtitle max 30 chars each (already set at app level, not
  re-litigated per page). Keyword field max 100 chars, comma-separated,
  no unnecessary spaces, no repeated/plural-only terms. Promotional text
  max 170 chars, no pricing.

Attribution guardrail applied throughout (per `westretch-core/references/
strategic-thesis.md` and the known failure pattern logged 2026-08-10):
licensed physiotherapists mapped the **general** safe-movement framework;
the algorithm does the **per-user personalization**. Every line below
keeps that split, none credit physiotherapists with personalizing to an
individual's pain, swing, or body.

## Open question for Karen/Manager before build

"Stiffness" and "mobility" overlap heavily in search intent and in the
app's own core message (the default page's whole thesis is personalized,
physiotherapist-mapped movement; which *is* the mobility/stiffness
pitch). Two options, not deciding this unilaterally:
1. Build both as separate pages anyway (more search-term coverage, more
   Apple Search Ads landing targets): the plan below does this.
2. Merge into one "mobility & stiffness" page and use the freed page slot
   for something with more distinct intent (e.g. desk workers, named
   explicitly in the Knowledge Base's own "Custom Product Pages" section
   alongside back pain, golf, and pickleball, but not in Karen's backlog
   wording).

Plan below builds all 5 as separate pages per the backlog's literal
wording; flag if you want to merge before handing Part B to the pipeline.

---

## Page 1; Back Pain

- **Search intent:** "back pain relief," "back pain stretches," "lower
  back pain app."
- **Keyword field (96/100):** `back pain,lower back,sciatica,spine
  health,physiotherapist,gentle stretch,posture,tension relief`
- **Promotional text (167/170):** "Tell WeStretch what hurts and it
  builds a routine around it. Movement mapped by licensed
  physiotherapists, personalized to your body, guided step by step, no
  guessing."
- **Screenshot 1; reuse existing graded copy (no new copy loop needed):**
  Title "Works around your problem areas" (31/42) / Subtitle "Tell it
  what hurts or what to avoid. It adjusts." (48/65); Screen 4 from
  `App Store Image Text Copywriting/Output/Default/app-store-copy-
  default-cold-audience.md`, already graded A- (3.82), exact intent
  match for this page.
- **Deep link target (pending iOS 18 confirmation):** body-area selector
  pre-filtered to back/lower back.

## Page 2; Stiffness

- **Search intent:** "morning stiffness," "tight muscles app," "stretch
  for stiffness."
- **Keyword field (97/100):** `stiffness,tight muscles,morning
  ache,flexibility,gentle stretch,loosen up,ease tension,joint care`
- **Promotional text (163/170):** "Wake up stiff? Ada guides you through
  gentle movement, mapped by licensed physiotherapists and personalized
  to your body, at your own pace, no timers, no guessing."
- **Screenshot 1, no strong existing transplant.** Nothing in the
  current graded copy bank targets morning stiffness specifically; the
  closest (card 5, "No sketch, no timer") is about guidance mechanics,
  not the stiffness trigger itself. **Needs a fresh run of the
  `app-store-copy` skill** (Chase → Expert → Marg loop) themed on
  stiffness; see Part B handoff.
- **Deep link target (pending iOS 18 confirmation):** routine builder
  with a "quick loosen-up" or short-session filter, if one exists;
  otherwise general routine builder.

## Page 3; Mobility

- **Search intent:** "mobility exercises," "improve range of motion,"
  "mobility app for aging."
- **Keyword field (93/100):** `mobility,range of motion,joint
  health,aging well,balance,independence,move better,flexibility`
- **Promotional text (161/170):** "Rebuild range of motion at your own
  pace. Movement mapped by licensed physiotherapists, personalized to
  your body and how you move today, not a generic template."
- **Screenshot 1; candidate transplant, needs re-grading against this
  page's specific intent:** Title "It evolves with you" (19/42) /
  Subtitle "Your routine adapts to your goals, your body, and your
  history." (63/65); Screen 7 from the default copy doc, graded A-
  (3.56). It's about long-term adaptation rather than literal
  range-of-motion, so treat as a starting draft for Marg to re-score
  against mobility search intent specifically, not a confirmed reuse
  like Page 1's.
- **Deep link target (pending iOS 18 confirmation):** general routine
  builder, mobility/range-of-motion category if one exists.

## Page 4; Golf

- **Search intent:** "golf mobility," "golf warm up app," "golf swing
  stretches."
- **Keyword field (87/100):** `golf,golf swing,shoulder turn,hip
  rotation,golfer,warm up,flexibility,injury prevention`
- **Promotional text (164/170):** "Golf warm-ups built on
  physiotherapist-mapped movement, personalized to your swing, hips, and
  shoulders, so you start strong and finish the round still moving
  well."
- **Screenshot 1, no existing transplant (new audience, no golf-specific
  copy exists anywhere in the project).** Needs a fresh `app-store-copy`
  run themed on golf; see Part B handoff.
- **Deep link target (pending iOS 18 confirmation):** routine builder,
  golf/sport-specific category if one exists; otherwise general routine
  builder. Flag for product/eng: does a golf-specific routine category
  exist today, or would this page be selling a use case the app doesn't
  yet explicitly categorize?

## Page 5; Pickleball

- **Search intent:** "pickleball warm up," "pickleball mobility,"
  "pickleball injury prevention."
- **Keyword field (99/100):** `pickleball,warm up,agility,quick
  feet,injury prevention,court ready,recovery,flexibility`
- **Promotional text (159/170):** "Get court-ready for pickleball.
  Guided warm-up routines, physiotherapist-mapped and personalized to
  your body, built for quick feet and fast direction changes."
- **Screenshot 1, no existing transplant (new audience, no pickleball-
  specific copy exists anywhere in the project).** Needs a fresh
  `app-store-copy` run themed on pickleball; see Part B handoff. Note:
  `App Store Image Creation/Knowledge files/01_Approved_Pickleball_
  Design.png` already exists, so visual direction may be partially
  underway even though copy isn't; check with whoever produced that
  asset before starting Part B for this page.
- **Deep link target (pending iOS 18 confirmation):** routine builder,
  pickleball/sport-specific category if one exists; same open flag as
  golf on whether that category exists.

---

## Part B; Handoff brief to the Image Creation + Copywriting pipelines

Each of the 5 pages above still needs screens 2 through up to 9 (or
however many the default page uses) plus its own app-preview video,
following the same structure as `App Store Image Text Copywriting/
Output/Default/app-store-copy-default-cold-audience.md`. Concretely:

1. **Stiffness, golf, and pickleball pages** need a full fresh
   `app-store-copy` skill run each (Chase → Expert → Marg loop, per
   `App Store Image Text Copywriting/SKILL.md`), since no existing graded
   copy targets those three intents. Back pain and mobility can start
   from the transplant candidates flagged above but still need the
   remaining screens written and graded per-theme, not just screenshot 1.
2. Once each page's copy is graded and approved, hand it to
   `App Store Image Creation/` for rendering, following that project's
   existing standing gates in its own `Memory.md` (spelling/grammar
   confirmation before render, pre-delivery review, calibrated
   typography specs), same as the 2026-08-22 PPO screenshot job.
3. **Suggested output structure**, matching this project's existing
   convention: one subfolder per page under `App Store Image Creation/
   Output/`, e.g. `Output/CPP - Back Pain/`, `Output/CPP - Stiffness/`,
   etc., each with its own `Run_01/` at both required export sizes.
4. **Localization note:** this plan is English-only. The backlog's next
   item, "Localize App Store assets for English, French, and Spanish,"
   is a separate not-started item, recommend finishing the English CPP
   copy/build first, then running that localization item against all 5
   finished pages plus the default page in one pass, rather than
   localizing each page as it's built.
5. **Compliance check before submission** (per Knowledge Base "App Review
   and Releases" metadata rejection table): no pricing on any page, no
   absolute/superlative claims ("best," "#1," "instant relief"), no
   competitor names, screenshots must show actual in-app functionality,
   and the physiotherapist attribution split above must hold in every
   line, same compliance bar as the default page.

## What this skill could not do

- Could not write or grade the full 8-remaining-screens-per-page copy set;
that's a multi-loop `app-store-copy` skill run per theme (3 fresh
  themes + 2 partial), sized for its own dedicated session, not a single
  nightly-action pass. Routed as a brief above (Part B, item 1).
- Could not render any screenshots: routed to `App Store Image
  Creation/` per this skill's own scope (asset-shaped work isn't
  improvised here).
- Could not confirm whether golf- or pickleball-specific in-app routine
  categories exist for deep-link targeting, flagged as an open question
  for product/eng in Pages 4 and 5 above.
- Could not submit anything to App Store Connect, no access from this
  skill, and live submission is explicitly out of scope regardless.
