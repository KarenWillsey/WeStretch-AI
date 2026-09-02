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
- [ ] Accessibility, account deletion, privacy disclosures, and subscription-clarity checklist. Six sections (accessibility in-app, Accessibility Nutrition Labels, privacy disclosures, ATT/SDK audit, account deletion, subscription clarity) for whoever owns App Store Connect + the iOS codebase to work through and check off — this automation has no access to verify any of it directly. Notes overlap with the separate SDK-fingerprinting-audit and iOS-18-deployment-target backlog items. (`Team/CMO/In Progress/App Store Specialist/Apple Opportunity Radar/Output/2026-08-31-accessibility-privacy-subscription-clarity-checklist.md`, flagged 2026-08-31, scheduled nightly-action run)
- [ ] Apple Featuring Nomination draft. Pitch copy for the "7-Day Mobility Challenge" In-App Event, mapped to Apple's stated evaluation criteria (innovation, UX, accessibility, localization, product page quality); explicitly flags accessibility and localization as design intent/partial-only, not compliance claims, until their own open backlog items close. Blocked on Karen picking the event start date before it's submission-ready. (`Team/CMO/In Progress/App Store Specialist/Apple Opportunity Radar/Output/2026-09-01-featuring-nomination-draft.md`, flagged 2026-09-01, scheduled nightly-action run)

## CMO: Apple Opportunity Radar monthly refresh
- [ ] **2026-09-01 (first scheduled run, fired 7:00 AM as registered):**
  Checked 13/13 tracked developer.apple.com URLs successfully, 0 failures.
  Found real updates in 10 of 16 sections. Added 5 new backlog items.
  Notable findings worth Karen/CMO attention specifically:
  - **New product-page feature, unused:** in-app purchase/subscription
    showcase (up to 20 items, custom order) — added to backlog.
  - **Timely:** In-App Events are now an explicit Apple Featuring
    Nomination pathway — WeStretch already has a drafted event ("7-Day
    Mobility Challenge," 2026-08-29) worth nominating now.
  - **PPO mechanics clarified:** only one A/B test at a time, up to 90
    days, needs 90% confidence, and icon-variant tests need all icon
    variants pre-shipped in the binary.
  - **Compliance:** Apple's "tracking" definition under ATT is broader
    than assumed — a third-party SDK combining data for ad
    targeting/measurement counts as tracking even if WeStretch doesn't use
    it that way, and in-app webviews need the same ATT prompt. Also:
    SDKs increasingly need privacy manifests/signatures. Folded into the
    existing SDK-audit backlog item rather than a new one.
  - **CTO-adjacent:** Small Business Program members under 2M first-time
    downloads get free Apple Foundation Models/Private Cloud Compute
    access — only relevant if WeStretch is using/planning on-device AI.
  - Found a better on-domain Apple Search Ads candidate URL
    (`developer.apple.com/app-store/promote/`) than the 2026-08-21 pass;
    needs human sanity-check before becoming a tracked Knowledge Base
    section (see `Implementation Spec.md` section 1).
  - Full detail: `Team/CMO/In Progress/App Store Specialist/Apple
    Opportunity Radar/Knowledge Base/apple-marketing-opportunities.md`
    changelog, and `state/monthly-refresh-log.json`.
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
- [ ] Generic drip-queue's 28 items exist only as one representative example screen (S29) in `KarensPlayground.json` — the other 27 aren't built as real screens yet. Drafted first-pass wording for all 28 (title/subtitle/2 buttons/hyperlink/X-close/wallpaper-top-layer-animation, same sheet format as the badge template) in the "Drip Slot Schedule" Artifact's new section 3a, for Karen to confirm before they get built out individually for testing. Uniform first-pass assumptions applied to all 28 (flagged in the Artifact, not yet Karen's call): Primary button = "Continue", no secondary/hyperlink/X-close, and all wallpaper/top-layer/animation entries are placeholder descriptions (no real art made yet). (`Team/CXO/In Progress/Westretch-UX`, flagged 2026-09-02)
- [ ] Variable/state testing structure v1 built 2026-08-29 (`src/data/variables.json`, `src/data/testPresets.json`, `chapters` on screens, `TestStatePanel` in the left panel). Only 3 of the ~35 `State-Variables.md` variables are wired in so far (`account_type`, `routines_completed`, `first_name`), and only `welcome-guest/free/pro` have example chapters. Grow the dictionary + chapters as Karen builds out more of `KarensPlayground.json`, per the workflow in that project's `Memory.md`. (`Team/CXO/In Progress/Westretch-UX`, flagged 2026-08-29)
- [ ] Unity migration handoff doc created for Jacque (`Team/CXO/In Progress/Westretch-UX/UNITY-HANDOFF.md`) explaining the `chapters`/`when` matching logic. **Open decision needed before migration starts:** this prototype's JSON shape does not match `DefaultRemoteConfig.v2.json`'s existing production shape. Karen and Jacque need to decide whether Jacque maps this content into the existing production shape, or the production config adopts this prototype's `chapters`/`when` pattern instead. (flagged 2026-08-29)
- [ ] S7 (`welcome-guest`) chapters: routines_completed 0-15 and 36-39 are exact chapters, sourced from `Copy Drafts/guest-welcome-onboarding-copy.csv`; routines_completed 16-35 now use a real rotation pool (`evergreen_pool_index`, a new randomizable test-state variable) instead of exact chapters, per Karen's 2026-08-29 request to build out the "evergreen randomization" her S7 `notes.uxNotes` field describes. Ids 36-39 (the CSV's "Alternate"/"Conditional" rows) are still exact chapters, deliberately left for later, not yet folded into the pool. Still open: whether this pool approach (vs. the note's "3-item pool" detail) is the final mechanic, and whether/when to extend it past routine 35 or copy the pattern to S10/S11 (welcome-free/pro). (`Team/CXO/In Progress/Westretch-UX/src/data/flows/KarensPlayground.json`, flagged 2026-08-29, updated 2026-08-29)
- [ ] Badge template infrastructure built 2026-08-30 (`component: "badge"` + `BadgeVisual` in `types.ts`/`BadgeScreen.tsx`, per Karen's field spec: title/subtitle/2 buttons/hyperlink/close, each with its own destination, plus wallpaper/top-layer/animation/widget), but **S32 `badges` itself was reverted 2026-08-31 per Karen to the real-screenshot version** (`New-PRO-user-finishes-first-routine_05.png`, no longer using the badge template) — see the git-restore item below. The template code is still in the codebase, just unused by any screen right now. New `badge-check` (S33) and `share-handoff` (S34) hand-off stubs still represent the backend badge check and native share sheet; `streak-progress` (S35) is still a bare placeholder Karen said she's building next. **Open, not Claude's call:** this prototype's hotspots can't route conditionally on a variable, so `badge-check` always continues to the badge screen even when `badges_earned_today` is 0, and only one example badge is shown (no real multi-badge loop). (`Team/CXO/In Progress/Westretch-UX`, flagged 2026-08-30, updated 2026-08-31)
- [ ] Pre/post-routine pain check-ins + speech screens inserted 2026-08-31, S30 re-scoped from "hit finish" stub to the pre-routine Ada-speech screen. `pre-routine-pain-check` (S36, background matches S8's `In-Gym-gradient.png` per Karen) and `post-routine-pain-check` (S37, keeps S30's `Start-Routine.png` background) each have a placeholder 0-10 pain-scale slider with a SKIP link below it (not a real interactive control yet); `post-routine-speech` (S38) shares S37's background photo. New `pain_rating` variable added to `variables.json`, reusing the name already established in `Onboarding UX Flow Spec/State-Variables.md`. **Open, not Claude's call:** (1) neither pain-check screen is actually gated yet — no variable tracks "chose a pain-focused routine" / "first pain routine," and the post-routine one's backend trigger schedule isn't designed; (2) `routines_completed`'s increment was moved from S30 onto `post-routine-pain-check` since S30 is pre-routine now — Claude's placement choice, not confirmed with Karen; (3) neither pre- nor post-routine Ada speech copy is written yet (account_type/routines_completed/first_name-driven); (4) `post-routine-speech` (S38, confirmed 2026-08-31 by Karen to be the end-of-routine brain-exercise video screen) has no video/animation asset supplied yet, so that layer isn't built. (`Team/CXO/In Progress/Westretch-UX`, flagged 2026-08-31)
- [ ] **S32 restored from conversation memory, not git — flag if this ever needs auditing.** Karen asked to restore S32's "different screen previously"; git history was checked thoroughly (all commits, reflog, all branches) and confirmed `badges`/S32 doesn't exist in any commit before this session's own single squashed commit, so nothing was git-recoverable. Restored instead from this session's own conversation record of the screen's prior state (the real-screenshot version, confirmed by Karen over the alternative bare-stub version) — worth knowing this wasn't a mechanical `git checkout`, in case the reconstruction missed something from the original. (`Team/CXO/In Progress/Westretch-UX`, flagged 2026-08-31)
- [ ] New `do-routine` (S39) screen inserted 2026-08-31 between the pre-routine speech (S30) and post-routine pain check-in (S37), representing the native guided-routine playback (Screen-Inventory row 15) with a baked-in "FINISHED" link, same pattern S30 itself used before its re-scope. Still a placeholder background (`Start-Routine.png`), no real guided-routine art yet. Same day: `post-routine-speech` (S38) got an `autoAdvance` (3000ms, Karen's given value, not tied to real Ada-audio timing) to `badge-check` alongside its manual Continue; `pre-routine-pain-check` (S36)'s slider moved down 5% and enlarged 30% (third layout pass same day). All verified via `npm run check`/`build` + CDP click/timing tests. (`Team/CXO/In Progress/Westretch-UX`, flagged 2026-08-31)
- [ ] S24 (`routine-end-drip-hub`) real sequencing logic built 2026-09-01, slot table corrected 2026-09-02: `resolveDrip.ts` (`advanceDrip`/`confirmDripShown`) plus two engine hotspot actions (`resolve-drip`, `confirm-drip-shown`) implement the slot 1-14 table, the every-6-slots 13/14 repeat past 14, the 3-drips/day cap, and the shown/not-shown catch-up Karen asked for (a chosen-but-unconfirmed slot stays pending and gets re-shown before anything newer if the app closes first). **2026-09-02 correction round** (Karen reviewed the case-order Artifact and sent back fixes by letter, overriding several 2026-09-01 picks): Guest slot 2 is now unconditional Rate Us; Guest 3/5/8/10/12 and Free 4/8/10/12 gained a "Rate Us while unrated" fallback; Guest slot 6 is now unconditional Sign Up (was Sign In 3/Rate Us fallback); Free slots 3/5 are now unconditional Paywall (the 2026-09-01 "falls back to Rate Us while unrated" was wrong); Free slot 6's Rate Us-while-unrated assumption was confirmed as-is (resolving the prior open flag); slot 7 (both tiers) keeps its screen type but gained copy direction (Guest: reward vs. guest-limits contrast; Free: "what Free looks like going forward" preview + Start Pro CTA — both still placeholder copy, not written). Verified both times with a pure-function test (55 checks after the correction) and a live CDP click-test against a production build (16 checks), all passing; also fixed a pre-existing gap where `TestStatePanel.tsx` never actually rendered a control for `type: "boolean"` variables. The case-order Artifact was updated in place (same link) to match. **Open, not Karen's call yet / flagged in S24's own `openQuestions`:** (1) the model assumes only one numbered slot (or the notification opt-in) can ever be pending at once — a new one is only chosen once the last is confirmed shown; if slots should keep advancing regardless (a real multi-item backlog), this needs a different data shape since `TestState` only holds flat values, no arrays; (2) slot 7's guest-limits list and Free's "going forward" preview content both need Karen's actual copy before they're more than placeholders; (3) Karen's correction list had a blank item "j" — asked her if there was more to add. **Same day, later:** added a one-time slot 0 (before slot 1 ever fires) — Guest gets a create-an-account prompt, Free a Paywall with a trial + bonus offer (content not written yet), Pro gets nothing; has its own independent pending/shown pair (`drip_slot0_pending`/`drip_slot0_shown`) so it doesn't consume slot 1's place, reuses the existing `drip-sign-in`/`drip-paywall-hub` screens and hotspots unchanged. Also removed the "corrected 2026-09-0X" changelog-style narration from `resolveDrip.ts`'s doc comments per Karen's request (that history belongs in this tracker/Memory.md, not in the code); the Artifact's flag-list was rewritten the same way. 27 new pure-function checks added (slot 0 fires first, survives a simulated close, never refires once shown, skipped for Pro, respects the daily cap), all passing alongside the existing suite; `npm run build` clean. Added a separate plain-language to-do (design the during-routine screen S39, design the Paywall S27, revisit the Rate Us sheet S25) to `Karens-TODO.md` per her ask — not listed here since that file is explicitly her own backlog, not a Claude-flagged open item. **Same day, later still:** reversed the "slot keeps climbing past 14" decision — Karen picked the day-based alternative instead, so past slot 14 the 13/14 pair now repeats on a real day cadence (`drip_days_since_slot14`, manually advanced) rather than a climbing slot count; `drip_slot_index` freezes at 14. Confirmed the slot-0 endless-retry-until-confirmed edge case works as intended (no change needed, added a test proving it). The 28-item generic queue no longer loops — once exhausted (`generic_queue_exhausted`), further unmarked slots (pre- or post-14) go to a new bare-placeholder `leaderboard` (S42) stub instead. 27 more pure-function checks added, all passing; `npm run build` clean; Artifact and S24/S29 notes updated to match. **Open, not Karen's call yet / flagged in S24's own `openQuestions`:** (1) the single-pending-thing model, now generalized to 4 kinds (numbered slot, notification, slot 0, post-14 repeat) — still assumes only one can ever be pending at a time; (2) slot 7's guest-limits list, Free's "going forward" preview, and slot 0's trial+bonus specifics all still need real copy; (3) `leaderboard` (S42) assumes "the leaderboard screen" means the app's real Leaderboard feature, not something new — flag if that's wrong; (4) Karen's earlier blank item "j" is still unresolved. **Same day, later still:** fixed a real drift risk found while confirming the never-loop behavior survives future growth — `resolveDrip.ts` had its own hardcoded `GENERIC_QUEUE_LENGTH = 28`, separate from `variables.json`'s `generic_queue_pointer.max: 28`; now `resolveDrip.ts` reads `max` directly, so growing the queue is a one-field change. Also found `DefaultRemoteConfig.v2.json` (the separate PRD-derived config for the real, non-prototype build) still said `"loop": true` and described wrapping back to item 1 — never updated when the never-loop/Leaderboard decision was made above; fixed there too (`loop: false`, explicit `onExhausted` → Leaderboard). **New: Pro now gets its own drip cycle**, per Karen's ask — Pro already meets the has-signed-in/is-Pro bar that Guest's Sign In/Sign Up and Free's Paywall slots exist to clear, so Pro never sees any of those three screens, but can still see Rate Us while unrated and shares the same generic education queue. Added `proCase()` to `resolveDrip.ts` (slots 2/4/6/8/10/12/13 gated on `rate_us_done`, all else generic; post-14's 14-case is generic instead of a Paywall) and a matching `"pro"` section in `DefaultRemoteConfig.v2.json`. The exact slots (2/4/6/8/10/12/13) chosen for Pro's Rate Us, mirroring Free's existing pattern, was Claude's assumption going in — **Karen confirmed it 2026-09-02**, no longer open. Verified with a 12-check standalone pure-function test against the real `resolveDrip.ts` (Pro's unrated/rated walks, post-14 cadence, Guest's Sign In recurrence unaffected, exhaustion tracking `variables.json`'s configured max) — all passing; `npm run check`/`build` clean. (`Team/CXO/In Progress/Westretch-UX`, flagged 2026-09-01, updated 2026-09-02)

