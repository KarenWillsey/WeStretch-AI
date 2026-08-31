# Work Tracker

One place to see every open task across the whole repo, so nothing gets
lost across chats, roles, or people. The Manager (root `CLAUDE.md`) owns
this file.

## Rules
1. Any open item (decision needed, unfinished work, gap, blocked task)
   gets a line here **in the same session it's found**, same time it's
   noted in that project's own `Memory.md`.
2. Check this file at the start of any session before starting work.
3. Delete or check off a line the moment it's resolved. Don't let this
   file go stale; it's only useful if it's current.
4. Format: `- [ ] item (path/to/project, flagged YYYY-MM-DD)`
5. **`Ideas/` folders are excluded: never add items from there.** Not
   active work yet; the Manager surfaces those separately, on request,
   when looking for new work to start.
6. Items in a role's `Review ToDo/` folder go here too. Once Karen approves
   one, move it wherever it actually belongs (not always `Ready/`) and
   remove its line here.
7. Check every role's `Review ToDo/` folder at the start of any session
   (not just the ones already listed below); a file sitting there with no
   line here means this tracker has gone stale and rule 3 was missed.
8. **Scheduled-automation staleness check.** At the start of any session,
   check whether registered scheduled automations actually fired on
   schedule. Currently tracked: the daily brief (`state/last-run.log` under
   `Team/CEO/In Progress/Set Up Daily Housekeeping/`, expected every
   morning) and the Apple Opportunity Radar (`state/last-run.log` and
   `state/monthly-refresh-log.json` under `Team/CMO/In Progress/App Store
   Specialist/Apple Opportunity Radar/`, expected nightly + monthly once
   its scheduled tasks are registered; see that project's `CLAUDE.md` for
   whether that's confirmed yet). If a run is stale beyond its expected
   cadence, flag it to Karen immediately and offer to trigger a manual
   re-run in that session; don't wait for her to notice.

## CMO: website-repo
Sits in `Ready/` but has 4 open items in its own tracker (folder location
may need revisiting, Ready usually means done, this isn't). Full detail:
`Team/CMO/Ready/website-repo/USER_TODO.md`.
- [ ] Meta Conversions API access token needs a secure home (not this repo). No backend exists yet to hold it; **recommend rotating it**, since Karen shared it in chat rather than a secrets vault. Flagged 2026-08-21
- [ ] DNS/domain cutover plan + access. Karen confirmed 2026-08-21 this is easy and ready whenever needed; window still TBD
- [ ] Remove dev-site noindex block before going live (intentionally deferred to launch, not blocked)
- [ ] Final content review pass vs. live site

Resolved 2026-08-21 (contact form: keep mailto:, future swap to a
WeStretch webhook API once Karen builds it; analytics/GA4/Meta Pixel IDs
provided and wired; Stripe links confirmed live; `/signup/` now redirects
home; Sign In URL confirmed correct; social links confirmed; no video
needed) and 2026-08-28 (image self-hosting: all images self-hosted under
`public/images/`, duplicates deduped). See `USER_TODO.md` for detail,
removed from this list per rule 3.

## CMO: App Store Specialist pending Manager review
- [ ] Small Business Program enrollment checklist. Verifies WeStretch is actually enrolled for the reduced 15% App Store commission (vs. 30% standard); requires App Store Connect Account Holder access to actually check, which this automation doesn't have. (`Team/CMO/In Progress/App Store Specialist/Apple Opportunity Radar/Output/2026-08-21-small-business-program-checklist.md`, flagged 2026-08-21, manual test run of app-store-specialist-nightly-action)
- [ ] Billing Grace Period & App Store Server Notifications checklist. Split into a quick App Store Connect config step (Account Holder/Admin) and a real backend engineering task (webhook endpoint outside this repo's scope). (`Team/CMO/In Progress/App Store Specialist/Apple Opportunity Radar/Output/2026-08-21-billing-grace-period-and-server-notifications-checklist.md`, flagged 2026-08-21, first scheduled nightly-action run)
- [ ] PPO test plan for the first 3 screenshots. Brief for the Image Creation/Copywriting pipelines to produce 3 headline treatments for screenshot 1 (reusing already-graded copy), plus a full Product Page Optimization test setup ready for App Store Connect. (`Team/CMO/In Progress/App Store Specialist/Apple Opportunity Radar/Output/2026-08-22-ppo-test-first-3-screenshots.md`, flagged 2026-08-22, scheduled nightly-action run)
- [ ] Custom Product Pages plan (back pain, stiffness, mobility, golf, pickleball). 5 pages: keyword fields, promotional text, and screenshot-1 direction drafted for each (back pain reuses already-graded copy outright; mobility has a candidate transplant needing re-grading; stiffness/golf/pickleball need a fresh copy-loop run); plus an open question for Karen on whether to merge the stiffness and mobility pages given intent overlap. (`Team/CMO/In Progress/App Store Specialist/Apple Opportunity Radar/Output/2026-08-23-cpp-plan-5-pages.md`, flagged 2026-08-23, scheduled nightly-action run)
- [ ] Localize App Store assets (French, Spanish). French/Spanish translations of the screenshot and app-preview-video copy (the only English App Store asset copy that exists yet); flags that product page metadata (name/subtitle/keywords/description) has no English source to localize, and adds a new prerequisite backlog item to draft it. (`Team/CMO/In Progress/App Store Specialist/Apple Opportunity Radar/Output/2026-08-26-localize-app-store-assets-fr-es.md`, flagged 2026-08-26, scheduled nightly-action run)
- [ ] Native rating prompts implementation plan. StoreKit `requestReview` wired to streak-milestone and Nth-completed-routine moments (never onboarding/paywall/error flows), no custom pre-prompt gate, Apple enforces the 3-prompts/365-day cap silently; needs the native iOS app codebase (not in this repo) to actually implement. (`Team/CMO/In Progress/App Store Specialist/Apple Opportunity Radar/Output/2026-08-28-native-rating-prompts-plan.md`, flagged 2026-08-28, scheduled nightly-action run)
- [ ] **Reliability gap:** the 2026-08-24 and 2026-08-25 scheduled nightly runs both show a "Starting scheduled nightly-action run" line in `Apple Opportunity Radar/state/last-run.log` but no completion banner, no exit-code line, and no `Output/` file for either date; they appear to have started and then failed or hung silently. Needs investigation (check Windows Task Scheduler history for those two runs) before trusting the schedule unattended again.
- [ ] In-App Event draft: "7-Day Mobility Challenge." Full metadata draft (event name/short/long description, all under Apple's char limits), Challenge event type, compliance check against Apple's event-metadata restrictions, 7-day content concept guided by Ada, and an artwork brief routed to the Image Creation pipeline. Open items: exact start date, confirm the "Day N unlocks" mechanic is buildable, pick long-description option A/B. (`Team/CMO/In Progress/App Store Specialist/Apple Opportunity Radar/Output/2026-08-29-in-app-event-7-day-mobility-challenge.md`, flagged 2026-08-29, scheduled nightly-action run)
- [ ] Subscription offers (introductory/promotional/win-back) configuration checklist. Blocked on one open question first: does WeStretch's iOS app sell subscriptions via StoreKit/IAP at all, or only via the website's Stripe checkout (Monthly $9.99/mo, Annual $59.99/yr, both with a 7-day free trial)? If IAP exists, recommends mirroring the proven 7-day-free-trial as the introductory offer, a promotional offer for the cancel flow, and a win-back offer targeting lapsed Annual subscribers. (`Team/CMO/In Progress/App Store Specialist/Apple Opportunity Radar/Output/2026-08-30-subscription-offers-config-checklist.md`, flagged 2026-08-30, scheduled nightly-action run)

## CMO: Apple Opportunity Radar monthly refresh
- [ ] **2026-08-21 (manual test run, not scheduled):** Checked 13/13
  tracked developer.apple.com URLs successfully, 0 failures. Found real
  updates in 9 sections (not just wording: new stats, new rules, one hard
  compliance redline), expected for a first live pull, since the prior
  baseline was Karen's manual excerpt rather than a full page-by-page
  fetch. Added 4 new backlog items. Notable findings worth Karen/CMO
  attention specifically:
  - **Compliance redline:** device-sensor-only medical measurement claims
    (blood pressure, glucose, etc.) are flatly prohibited; never let copy
    imply this.
  - **New revenue lever:** EU alternative terms give 10% commission
    (vs. 15% Small Business Program); worth checking if EU is a
    meaningful market.
  - **New CPP fact:** deep-linked Custom Product Pages need iOS 18+.
  - 3 candidate source URLs found (TestFlight, App Clips, Apple Developer
    News) for future Knowledge Base sections; need a human sanity-check
    before being added as tracked "fact," per this skill's own caution
    rule (see `Implementation Spec.md` section 1).
  - Full detail: `Team/CMO/In Progress/App Store Specialist/Apple
    Opportunity Radar/Knowledge Base/apple-marketing-opportunities.md`
    changelog, and `state/monthly-refresh-log.json`.

## CMO: Apple Opportunity Radar (fully live 2026-08-21)

Resolved 2026-08-21: both skills built, wrapper scripts built, state files
initialized, Knowledge Base seeded with Karen's baseline, both Windows
Scheduled Tasks registered and `Ready` (monthly one needed a `.cmd`-batch-
file workaround for PowerShell quoting, see project `Memory.md` if it
ever needs redoing), Manager staleness-check rule wired into this file's
rule 8.

## CMO: Review ToDo/ (awaiting Karen's approval)
Pending: `male-actor-01-cat-pose-indoor.png`, generated by the new
`Team/CMO/skills/male-actor-01-image-generator/` skill (Male Actor 01,
outdoor pickleball-court reference, in a cat-pose stretch, indoor scene).
Awaiting Karen's sign-off before it moves out of `Review ToDo/`.

`female-actor-01-pigeon-pose-park.webp` and
`female-actor-01-pigeon-pose-park reversed.jpg` were exploratory variants
tried for the homepage hero and superseded, never separately approved,
no action needed on them.

Resolved 2026-08-21: homepage hero image locked in, three variants tried
(`female-actor-01-cobra-studio-hero.webp`, then the pigeon-pose park
photo, then `female-actor-01-pigeon-pose-warm-readable-hero.webp`), Karen
confirmed the warm-readable one is best. Deployed to
`public/images/hero-home.webp` in website-repo: cropped for tight
headroom, full width/full height kept (no bottom crop, per Karen's
instruction), resized ~7% to cover wide desktop viewports without a seam.
Text-shadow added to the overlaid hero text (`src/pages/index.astro`) for
legibility. Source files left in place in `Review ToDo/` as the CMO asset
archive copies.

## CXO: Westretch-UX
- [ ] Variable/state testing structure v1 built 2026-08-29 (`src/data/variables.json`, `src/data/testPresets.json`, `chapters` on screens, `TestStatePanel` in the left panel). Only 3 of the ~35 `State-Variables.md` variables are wired in so far (`account_type`, `routines_completed`, `first_name`), and only `welcome-guest/free/pro` have example chapters. Grow the dictionary + chapters as Karen builds out more of `KarensPlayground.json`, per the workflow in that project's `Memory.md`. (`Team/CXO/In Progress/Westretch-UX`, flagged 2026-08-29)
- [ ] Unity migration handoff doc created for Jacque (`Team/CXO/In Progress/Westretch-UX/UNITY-HANDOFF.md`) explaining the `chapters`/`when` matching logic. **Open decision needed before migration starts:** this prototype's JSON shape does not match `DefaultRemoteConfig.v2.json`'s existing production shape. Karen and Jacque need to decide whether Jacque maps this content into the existing production shape, or the production config adopts this prototype's `chapters`/`when` pattern instead. (flagged 2026-08-29)
- [ ] S7 (`welcome-guest`) chapters: routines_completed 0-15 and 36-39 are exact chapters, sourced from `Copy Drafts/guest-welcome-onboarding-copy.csv`; routines_completed 16-35 now use a real rotation pool (`evergreen_pool_index`, a new randomizable test-state variable) instead of exact chapters, per Karen's 2026-08-29 request to build out the "evergreen randomization" her S7 `notes.uxNotes` field describes. Ids 36-39 (the CSV's "Alternate"/"Conditional" rows) are still exact chapters, deliberately left for later, not yet folded into the pool. Still open: whether this pool approach (vs. the note's "3-item pool" detail) is the final mechanic, and whether/when to extend it past routine 35 or copy the pattern to S10/S11 (welcome-free/pro). (`Team/CXO/In Progress/Westretch-UX/src/data/flows/KarensPlayground.json`, flagged 2026-08-29, updated 2026-08-29)
- [ ] Badge template built 2026-08-30 (S32 `badges`, new `component: "badge"` + `BadgeVisual` in `types.ts`/`BadgeScreen.tsx`, per Karen's field spec: title/subtitle/2 buttons/hyperlink/close, each with its own destination, plus wallpaper/top-layer/animation/widget). New `badge-check` (S33) and `share-handoff` (S34) hand-off stubs represent the backend badge check and native share sheet; `streak-progress` (S35) is a bare placeholder Karen said she's building next. **Open, not Claude's call:** (1) real medallion/animation art still needed — S32 currently reuses the generic `In-Gym-gradient.png` wallpaper since the only reference is one flat baked screenshot; (2) close/Dismiss/post-share currently all route to the same `streak-progress` target, real per-destination behavior unconfirmed; (3) this prototype's hotspots can't route conditionally on a variable, so `badge-check` always continues to the badge screen even when `badges_earned_today` is 0, and only one example badge is shown (no real multi-badge loop). (`Team/CXO/In Progress/Westretch-UX`, flagged 2026-08-30)
- [ ] Pre/post-routine pain check-ins + speech screens inserted 2026-08-31, S30 re-scoped from "hit finish" stub to the pre-routine Ada-speech screen. New `pre-routine-pain-check` (S36) and `post-routine-pain-check` (S37) share a placeholder 0-10 pain-scale slider graphic composited onto S30's background (`public/screens/westretch/Start-Routine-pain-scale.png`), not a real interactive control yet; new `post-routine-speech` (S38) is a plain placeholder. New `pain_rating` variable added to `variables.json`, reusing the name already established in `Onboarding UX Flow Spec/State-Variables.md`. **Open, not Claude's call:** (1) neither pain-check screen is actually gated yet — no variable tracks "chose a pain-focused routine" / "first pain routine," and the post-routine one's backend trigger schedule isn't designed; (2) `routines_completed`'s increment was moved from S30 onto `post-routine-pain-check` since S30 is pre-routine now — Claude's placement choice, not confirmed with Karen; (3) neither pre- nor post-routine Ada speech copy is written yet (account_type/routines_completed/first_name-driven); (4) `post-routine-speech` (S38) confirmed 2026-08-31 by Karen to be the end-of-routine brain-exercise video screen, but no video/animation asset has been supplied yet, so that layer isn't built. (`Team/CXO/In Progress/Westretch-UX`, flagged 2026-08-31)

## CXO: Onboarding UX Flow Spec
- [ ] Karen to review proposed drip sequence (Claude's draft). (`Team/CXO/In Progress/Onboarding UX Flow Spec/Storyline.md`, flagged 2026-08-21)
- [ ] Goal 1 fix (leaderboard dead-end) not decided. (`Team/CXO/In Progress/Onboarding UX Flow Spec/Screens/Home.md`, flagged 2026-08-21)
- [ ] ~15 more small open questions (body_filter list, "too fast" stacking, etc.). See `Team/CXO/In Progress/Onboarding UX Flow Spec/Global-Goals.md` and `State-Variables.md`
