# Billing Grace Period & App Store Server Notifications; Checklist

**Backlog item:** Enable Billing Grace Period and subscription-status notifications (App Store Server Notifications).
**Date:** 2026-08-21
**Produced by:** app-store-specialist-nightly-action (first scheduled run)

## Why this matters

This is Apple's #2 highest-priority action for WeStretch (see Knowledge
Base "Highest-Priority Actions for WeStretch"). It's involuntary-churn
recovery: when a subscriber's card fails at renewal, a Billing Grace
Period keeps their access active for a few extra days while Apple retries
the charge, instead of cutting them off and losing them immediately.
App Store Server Notifications is the mechanism that tells WeStretch's
backend *when* that happens (and when renewals, cancellations, refunds,
and offer redemptions happen generally), so the app can react, e.g. show
"update your payment method" messaging instead of silently locking a
paying customer out.

Per the Knowledge Base: neither a grace-period recovery window nor a
renewal-date extension counts against the subscriber's continuous
one-year tenure that determines the 85%-proceeds/15%-commission rate, so
this costs WeStretch nothing on the commission side, it's pure retention
upside.

## What I cannot verify

This skill has no App Store Connect access and this repo has no
application/backend source code (per root `CLAUDE.md`: "no application
source code, build system, test suite"). I cannot confirm whether the
grace period is currently enabled, whether a notifications endpoint
already exists, or what the backend currently does with subscription
events. Nothing below is "done"; it's two checklists, split by who needs
to act.

## Part 1; App Store Connect config (Account Holder / Admin)

**Who:** Account Holder or Admin with access to app subscription settings.

1. Sign in to [App Store Connect](https://appstoreconnect.apple.com) →
   the WeStretch app → **Subscriptions** (or **Features → Subscription
   Grace Period**, depending on current UI).
2. Enable **Billing Grace Period**.
3. Choose a grace period length: **3, 16, or 28 days** (per Knowledge
   Base). Recommendation: start with **16 days**, long enough to catch
   most card-decline retries without extending a lapsed subscriber's free
   access for a full month; revisit after a quarter of real data.
4. Confirm this applies to all active subscription groups (WeStretch may
   have more than one; check each).
5. Separately, under **App Store Server Notifications** (App Information
   or Subscriptions settings), register a **Production Server URL** (and
   Sandbox URL for testing): this is the endpoint from Part 2 below. Also
   generate/confirm a **signing key** for verifying notification
   authenticity (App Store Connect → Users and Access → Integrations →
   Keys → In-App Purchase, or the newer Server Notifications key flow).

**Pass looks like:** Billing Grace Period shows "Enabled" with a chosen
duration for every subscription group; a Production Server URL is
registered under App Store Server Notifications.

## Part 2; Backend engineering work (not verifiable or doable from this repo)

This repo (`Team/CMO/Ready/website-repo`, the Astro marketing site) is
**not** the app backend; App Store Server Notifications requires a
webhook endpoint on WeStretch's actual mobile-app backend, which lives
outside this repo. Handing this to whoever owns that codebase:

1. Stand up an HTTPS endpoint that accepts Apple's `POST` notification
   payloads (signed JWS format, App Store Server Notifications **V2**).
2. Verify each notification's signature against Apple's public keys
   (Apple publishes a verification library/spec; don't skip signature
   verification, or a spoofed request could fake a subscription event).
3. Handle at minimum these notification types relevant to retention (per
   Knowledge Base "Billing Recovery and Subscriber Retention"):
   - `DID_FAIL_TO_RENEW`: failed renewal / grace period entered.
   - `DID_RENEW`: recovered successfully (including after grace period).
   - `EXPIRED`: grace period exhausted, subscription actually lapsed.
   - `DID_CHANGE_RENEWAL_STATUS`: user turned auto-renew off (a
     retention-messaging opportunity before they actually lose access).
   - `REFUND`, `OFFER_REDEEMED`, for accurate revenue/retention tracking.
4. On `DID_FAIL_TO_RENEW`, trigger the retention messaging path: "update
   your payment method" prompt, ideally in-app and via a reminder
   notification; this is the actual point of building this, not just
   logging the event.
5. Track voluntary cancellations (`DID_CHANGE_RENEWAL_STATUS` with
   auto-renew off) separately from involuntary/failed-payment churn, the
   Knowledge Base calls this out explicitly since the two need different
   responses (win-back offer vs. payment-fix prompt).
6. Test end-to-end against the **Sandbox** server URL before relying on
   Production.

**Pass looks like:** a registered endpoint receiving and correctly
verifying real Sandbox notifications; failed-renewal events visibly
trigger a payment-fix prompt to the affected user; cancellation reason
(voluntary vs. involuntary) is distinguishable in whatever analytics/CRM
WeStretch uses.

## Recommended next step

Two separate people likely need to act: the App Store Connect Account
Holder for Part 1 (quick, ~15 minutes), and whoever owns the app backend
for Part 2 (a real engineering task, not a quick config change). Part 1
can and should happen immediately regardless of Part 2's timeline; Apple
retries failed renewals automatically once grace period is enabled, so
WeStretch gets some retention benefit even before the notifications
endpoint exists to add in-app messaging on top.
