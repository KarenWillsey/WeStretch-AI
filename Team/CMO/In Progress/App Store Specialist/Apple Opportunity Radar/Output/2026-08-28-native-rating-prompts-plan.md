# Native Rating Prompts; Implementation Plan

**Backlog item:** Wire up native rating prompts after positive moments (completed routines, streak milestones), respecting the 3-prompts/365-day cap.
**Date:** 2026-08-28
**Produced by:** app-store-specialist-nightly-action (scheduled run)

## Why this matters

Ranked #1 in the Knowledge Base's "Highest-Priority Actions for WeStretch."
Ratings and review count/velocity are a direct App Store ranking and
conversion factor, and Apple's own guidance is explicit that the request
should land right after a positive moment, not during onboarding or a
frustrating flow.

## What I cannot verify

This repo has no native iOS/mobile app source (per root `CLAUDE.md`: "no
application source code"). `Team/CXO/In Progress/Westretch-UX` is a React/
Vite web demo, not the shipping app, and `Team/CMO/Ready/website-repo` is
the marketing site; neither is where StoreKit code would live. I cannot
confirm what's currently wired up, whether `SKStoreReviewController` (or
`StoreKit`'s `requestReview()` for SwiftUI) is already imported anywhere,
or what event system the app uses for routine-completion/streak logic.
Nothing below is "done"; this is an implementation-ready spec for whoever
owns the native app codebase.

## The API (per Apple's current guidance)

- **API to call:** `StoreKit`'s `AppStore.requestReview(in:)` (SwiftUI,
  iOS 16+) or `SKStoreReviewController.requestReview(in:)` (UIKit). Do
  **not** call a review-request API more than once in the same short
  session even after multiple qualifying moments, the system throttles
  independently of app logic, but the code should still be well-behaved
  and not spam the call.
- **Apple enforces the cap, not the app.** Per the Knowledge Base: the
  native pop-up shows **at most 3 times per user per 365 days**, and Apple
  decides silently whether to actually display it each time the API is
  called; the app has no way to detect whether the prompt was shown.
  Because of this, the app-side logic should track "moments we *asked*,"
  not "moments we *showed the prompt*" (that distinction doesn't exist
  from the app's point of view).
- **Never build a custom pre-prompt "are you enjoying the app?" gate that
  routes only happy users into the native prompt.** That pattern (review
  gating) violates App Store Review Guideline 2.3.13-adjacent
  "manipulating" rules and Apple's own ratings guidance; call
  `requestReview` directly at the qualifying moment, unconditionally, and
  let Apple's system decide who sees it.

## Recommended trigger points

Per Knowledge Base guidance ("after positive moments... completed
routines or streak milestones," never during onboarding or a frustrating
experience), in priority order:

1. **Streak milestone reached**: e.g. 7-day, 30-day streak (align exact
   thresholds with whatever streak milestones already exist in-app,
   e.g. any tied to the "7-Day Mobility Challenge" In-App Event backlog
   item). This is the strongest signal of a satisfied, engaged user.
2. **Nth completed routine**, not the first, e.g. after the 3rd or 5th
   completed session, once the user has enough data points to have
   formed a real opinion of the app. Do not trigger on routine #1.
3. **Do not trigger on:** onboarding completion, paywall/purchase flow,
   app launch, after an error or a skipped/abandoned routine, or
   immediately after a subscription charge.

## Implementation checklist (for the native app engineer)

1. Add a lightweight local counter/flag store (e.g. `UserDefaults` or
   equivalent) tracking: `lastReviewRequestDate`, `reviewRequestCount`
   (informational only; Apple enforces the real cap, but useful for
   internal analytics on how often the app *asks*), and whichever
   milestone/completion counters don't already exist.
2. At each qualifying moment (streak milestone hit, Nth routine
   completed), call `AppStore.requestReview(in:)` from the current
   `UIWindowScene` (SwiftUI) or `SKStoreReviewController.requestReview(in:)`
   (UIKit); must be called from an active foreground scene, not a
   background task.
3. Debounce app-side: don't call it more than once per app session, and
   space qualifying-moment triggers out (e.g. don't fire again within the
   same week even if two milestones are hit close together); keeps
   behavior sane even though Apple's cap is the real backstop.
4. **Do not show any custom UI** ("Enjoying WeStretch? Rate us!") before
   calling the API; call it directly.
5. Log each call (not each display: the app can't know if it displayed)
   to analytics, so WeStretch can correlate request timing with actual
   App Store rating trends over time.
6. Test via Xcode's StoreKit configuration file / sandbox, which lets the
   review prompt display every time in debug builds (production respects
   the real cap and won't reliably show for manual QA).

**Pass looks like:** `requestReview` is called at streak-milestone and
Nth-routine-completion moments, never during onboarding/paywall/error
flows, with no custom pre-prompt gate, and call events are logged for
internal tracking.

## Recommended next step

Hand this spec to whoever owns the native iOS app codebase (not present in
this repo). This is a small, self-contained change (a few call sites plus
a counter), good candidate for a fast follow once the streak-milestone
and routine-completion event hooks are confirmed to exist in the current
app architecture.
