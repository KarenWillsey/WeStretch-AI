# Small Business Program Enrollment — Verification Checklist

**Backlog item:** Confirm enrollment in Apple's Small Business Program (15% commission rate).
**Date:** 2026-08-21
**Produced by:** app-store-specialist-nightly-action (manual test run)

## Why this matters

Apple's standard App Store commission is 30% of proceeds. Developers
enrolled in the Small Business Program pay **15%** instead — on any
meaningful subscription/IAP revenue, that's a direct, ongoing margin
improvement with no product or marketing work required. It is **not
automatic** — Apple requires proactive enrollment, and it doesn't apply
retroactively to revenue earned before enrollment is approved.

## Eligibility (per Apple, as of this Knowledge Base's baseline)

- Generally: no more than US$1,000,000 in App Store proceeds (developer's
  share, after Apple's cut) across all developer accounts associated with
  the business, in the prior calendar year.
- Applies per legal entity/developer account, not per app.

Source: `Knowledge Base/apple-marketing-opportunities.md` → "Revenue and
Apple Commissions" (developer.apple.com/app-store/small-business-program/).

## What I cannot verify

This skill has no App Store Connect or Apple Developer account access, so
it cannot confirm whether WeStretch is currently enrolled, whether it's
eligible, or what commission rate is actually being applied. Nothing below
should be read as "confirmed" — it's a checklist for whoever has account
access to actually run.

## Checklist — who should do this and how

**Who:** must be the App Store Connect **Account Holder** (or an Admin with
access to Agreements, Tax, and Banking) — enrollment requires accepting a
separate Apple Developer Program license agreement addendum, which only the
Account Holder role can do.

1. Sign in to [App Store Connect](https://appstoreconnect.apple.com) →
   **Agreements, Tax, and Banking**.
2. Look for a **"Small Business Program"** (or "App Store Small Business
   Program") section/agreement under available agreements.
   - If it shows as **already accepted/active** → note the effective date;
     no action needed, just confirm the rate is reflected correctly (next
     step).
   - If it's **available but not accepted** → this is the actual gap:
     WeStretch is eligible but not enrolled, and is very likely paying the
     full 30% commission unnecessarily.
   - If it **doesn't appear at all** → likely means WeStretch's prior-year
     proceeds already exceed the threshold (not eligible), or the account
     doesn't qualify for another reason — worth confirming with Apple
     Developer support if this is unexpected.
3. If eligible and not yet enrolled: read and accept the program agreement.
   Per Apple's process, this generally takes effect at the start of the
   following calendar year for existing developers (the current-year rate
   isn't retroactively changed) — confirm the exact effective date shown
   during enrollment, since this affects when the savings actually start.
4. After enrollment (or if already enrolled): verify the 15% rate is
   actually being applied — check a recent **Payments and Financial
   Reports** statement in App Store Connect and confirm the commission
   percentage on a transaction matches 15%, not 30%.
5. Re-check annually — the threshold is proceeds-based, so eligibility can
   change year to year as revenue grows; this Knowledge Base's monthly
   refresh only tracks Apple's *rules*, not WeStretch's actual proceeds, so
   this specific re-check has to be done by whoever owns App Store Connect
   access, not by this automation.

## What "pass" looks like

- App Store Connect shows the Small Business Program agreement as
  **accepted**, with an effective date.
- A recent financial report line item shows **15%** commission, not 30%.

## Recommended next step

Whoever holds the Account Holder role on WeStretch's App Store Connect
account should run steps 1–4 above and report back what they find. If
already enrolled, this item is fully resolved. If not enrolled and
eligible, enrolling is a low-effort, high-value action — worth doing
promptly since the effective date isn't retroactive.
