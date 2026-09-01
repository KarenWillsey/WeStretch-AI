# Verify accessibility, account deletion, privacy disclosures, and subscription-clarity requirements

Backlog item addressed: "Verify accessibility, account deletion, privacy disclosures, and subscription-clarity requirements are met." (Highest-Priority Action #9)
Date: 2026-08-31 (scheduled nightly-action run)

This is a verification/compliance-shaped item. I have no App Store Connect
access and no access to the WeStretch iOS codebase (this repo contains no
application source code), so I cannot confirm any of this is actually met.
What follows is a checklist for whoever owns App Store Connect and the iOS
codebase — pass/fail is theirs to determine. Sourced from `Knowledge
Base/apple-marketing-opportunities.md` ("Accessibility" and "Privacy and
Customer Accounts" sections).

---

## A. Accessibility — check in the iOS codebase + a real device/simulator

- [ ] Dynamic Type: text scales correctly up to at least 200%, and the app
      is usable (no truncation, no overlapping controls) up to 310% with
      larger accessibility sizes enabled.
- [ ] Color contrast meets sufficient-contrast standards throughout the app.
- [ ] VoiceOver: every interactive control has a meaningful accessibility
      label (not just "button" or blank).
- [ ] Voice Control: important actions (start routine, complete stretch,
      skip pose, etc.) are reachable by Voice Control.
- [ ] No information is conveyed by color alone (e.g. pain/difficulty
      indicators need a shape/icon/text cue too, not just a color).
- [ ] Reduce Motion preference is respected where the app uses animation.
- [ ] Captions are provided for spoken instructions and any instructional
      video content.
- [ ] Controls are easy to read/operate for older adults specifically
      (larger tap targets, clear labeling) — this is a stated brand
      positioning point, not just a compliance checkbox.
- [ ] Verified on both iPhone and iPad, not just one form factor.

## B. Accessibility Nutrition Labels — check in App Store Connect

- [ ] Declare accessibility features truthfully in App Store Connect's
      Accessibility Nutrition Labels. Apple's 9 declarable categories:
      VoiceOver, Voice Control, Sufficient Contrast, Dark Interface, Larger
      Text, Differentiate Without Color Alone, Reduce Motion, Captions,
      Audio Descriptions.
- [ ] Only declare a category once section A above confirms it's actually
      true — a false declaration is worse than under-declaring.
- [ ] Given WeStretch's older-adult positioning, prioritize getting Larger
      Text, Sufficient Contrast, and VoiceOver genuinely true and declared —
      these are the ones an older-adult user is most likely to filter by.

## C. Privacy disclosures — check in App Store Connect ("App Privacy" section) + privacy policy

- [ ] Privacy policy is live, publicly accessible (not behind a login), and
      accurate as of today.
- [ ] Privacy policy explains what personal and health-related data is
      collected, why, and how it's used.
- [ ] Privacy policy identifies third-party services that receive
      WeStretch user data (analytics SDKs, ad SDKs, crash reporting, etc.
      — name them, don't just say "third parties").
- [ ] Privacy policy explains data retention and deletion practices.
- [ ] App Store Connect's own "App Privacy" nutrition-label disclosure
      matches the privacy policy and matches what the app's SDKs actually
      do — these two going out of sync is a common rejection/complaint
      trigger.
- [ ] Only permissions actually needed for real functionality are requested
      (camera, health, notifications, etc.) — no speculative permission asks.
- [ ] If Apple Health is accessed: the purpose string shown to the user
      explains why, specifically.

## D. App Tracking Transparency + SDK audit — check in iOS codebase

- [ ] ATT permission is requested before any tracking that requires it —
      not requested for ordinary app functionality that isn't tracking.
- [ ] Users who deny ATT are genuinely not tracked (not tracked-anyway via
      a workaround).
- [ ] Audit every ad/analytics SDK in the app against the device-
      fingerprinting prohibition: none may derive an identifier from
      browser properties, device configuration, location, or network
      connection to uniquely identify a device, and none may use hashed
      email/phone as a tracking identifier without ATT permission.
      (This is also its own separate backlog item — "Audit current
      ad/analytics SDKs against Apple's device-fingerprinting prohibition"
      — this checklist item can be closed out alongside that one rather
      than duplicated.)
- [ ] If IDFV is used for analytics, confirm it's scoped to WeStretch's own
      apps only and never combined with other data to track across
      third-party apps/websites (the one ATT-free exception Apple allows).

## E. Account deletion — check in iOS codebase (only applies if WeStretch has in-app accounts)

- [ ] In-app account deletion exists (not just "contact support to
      delete") if the app lets users create accounts.
- [ ] Account deletion works regardless of the customer's location.
- [ ] The account-deletion flow explains that deleting the account does
      NOT automatically cancel an Apple subscription.
- [ ] Where appropriate, the flow directs the user to subscription
      management before/alongside account deletion, so they don't end up
      deleted-but-still-billed.

## F. Subscription clarity — check in iOS codebase (paywall/subscription screens) + App Store Connect

- [ ] The sign-up screen clearly states which features are free and which
      require a subscription.
- [ ] Subscription price, billing interval, and renewal terms are shown
      **before** purchase.
- [ ] The full billed amount (e.g. "$59.99/year") is the most visually
      prominent price on the sign-up screen. A monthly-equivalent
      breakdown (e.g. "$4.99/mo, billed annually") may also be shown, but
      only in a visually subordinate position — it must not outshine the
      actual charged amount.
- [ ] If there's a free trial: the screen explains exactly when the trial
      ends and when billing begins.
- [ ] An obvious in-app subscription-management option exists.
- [ ] Cancellation is easy to locate from that management screen (or a
      clear link to Apple's own subscription management).
- [ ] Apple subscriptions are clearly distinguished from any website/Stripe
      subscription option, if WeStretch sells both.
- [ ] Somewhere reasonable (FAQ, cancellation flow, account settings), the
      app explains that deleting the app does not cancel an Apple
      subscription.
- [ ] Existing subscribers are never offered the same subscription again
      (e.g. a "subscribe" paywall shouldn't show to someone already
      subscribed).

---

## What "pass" looks like

Every box above is checked *and* verified true against the live app and
live App Store Connect config — not assumed. If any box can't be checked
(e.g. "WeStretch doesn't have in-app accounts, so section E doesn't
apply"), note that explicitly rather than leaving it silently unchecked.

## Note on scope overlap

Two other backlog items overlap with this one and can be closed together
if convenient: "Audit current ad/analytics SDKs against Apple's device-
fingerprinting prohibition" (covers section D in more depth) and "Confirm
WeStretch's minimum iOS/iPadOS deployment target supports iOS 18+" (a
Custom Product Pages item, unrelated to this checklist otherwise).

Nothing here was submitted or declared live to Apple — this is a checklist
for whoever owns App Store Connect and the iOS codebase to work through.
