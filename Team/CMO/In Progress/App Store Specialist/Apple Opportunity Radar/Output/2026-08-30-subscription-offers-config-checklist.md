# Introductory, Promotional, and Win-Back Subscription Offers — Configuration Checklist

**Backlog item:** Configure introductory, promotional, and win-back subscription offers.
**Date:** 2026-08-30
**Produced by:** app-store-specialist-nightly-action (scheduled run)

## Why this matters

This is Apple's #8 highest-priority action for WeStretch (see Knowledge
Base "Highest-Priority Actions for WeStretch"). Per the Knowledge Base
("Subscriptions and Free Trials" / "Billing Recovery and Subscriber
Retention"): introductory offers convert new trial users, promotional
offers retain or recover existing subscribers, and win-back offers
re-acquire lapsed ones — three distinct levers Apple exposes natively
inside App Store Connect subscription configuration, separate from
whatever pricing/checkout WeStretch runs on the web.

## What I cannot verify or configure

This skill has no App Store Connect access, and this repo (per root
`CLAUDE.md`) contains no application source code — it's the marketing/
business-planning layer, not the iOS app or its backend. I cannot confirm
whether WeStretch's iOS app currently sells subscriptions via Apple's
in-app purchase (StoreKit) system at all, what subscription group(s)
exist, or what offers (if any) are already configured. Nothing below is
"done" — it's a checklist for whoever holds App Store Connect access.

**Open question that blocks everything else below:** does the WeStretch
iOS app actually transact subscriptions through StoreKit/In-App Purchase,
or only through the website's Stripe Payment Links (`src/data/site.ts` in
`website-repo` shows real live Stripe links: Monthly $9.99/mo and Annual
$59.99/yr, both with a "$0 for 7 days" trial)? Apple's offer system
(introductory/promotional/win-back) only applies to subscriptions sold
through Apple's own IAP — it has no effect on external Stripe checkout.
If the app doesn't yet sell IAP subscriptions, this item can't be
configured yet; it becomes "add StoreKit subscription support" (a real
engineering task) before any offer can exist. Whoever owns the iOS
codebase should confirm this first.

## Part 1 — App Store Connect config (Account Holder / Admin), assuming IAP subscriptions exist

**Who:** Account Holder or Admin with access to app subscription settings.

1. Sign in to [App Store Connect](https://appstoreconnect.apple.com) → the
   WeStretch app → **Subscriptions** → the relevant subscription group.
2. **Introductory offers** (for eligible new subscribers who've never had
   this subscription before):
   - Under each subscription product → **Subscription Prices → Introductory
     Offer**, add a free trial or discounted intro price.
   - Recommendation: mirror what's already proven on the web checkout — a
     **7-day free trial**, then full price (Monthly $9.99/mo or Annual
     $59.99/yr) — so the iOS pricing story matches what's already live and
     tested on westretch.ca, rather than inventing a new offer structure.
   - Set eligibility to "new subscribers" (Apple's default) so existing/
     returning subscribers can't re-trigger it — matches the Knowledge
     Base rule "avoid offering existing subscribers the same subscription
     again."
3. **Promotional offers** (to retain or recover *current* subscribers,
   e.g. before a renewal or right after a cancellation attempt):
   - Under **Subscription Prices → Promotional Offers**, create one or
     more offer codes/prices (e.g. a discounted rate for the next 1-3
     billing cycles).
   - These require your app to call Apple's `requestPromotionalOffer`/
     StoreKit signing flow at the moment of presenting the offer (e.g. on
     a cancellation-intent screen) — this is an app-code integration, not
     just an App Store Connect toggle. Flag to iOS engineering.
   - Recommendation: hold a modest discount (e.g. 50% off for 2 months) in
     reserve for a "before you go" screen in the cancel flow, gated on the
     subscriber not having redeemed one before.
4. **Win-back offers** (to re-acquire subscribers whose subscription has
   already fully lapsed):
   - Under **Subscription Prices → Win-Back Offers** (Apple's newer,
     App-Store-Connect-managed win-back tooling — no client-side signing
     needed, Apple surfaces it directly in the App Store/App Store
     Connect UI to eligible lapsed users).
   - Recommendation: target lapsed subscribers with a time-limited
     discount on the Annual plan specifically (the plan with more margin
     to give up, and the one WeStretch already discounts 50% vs. monthly
     on the web).
5. **Offer codes** (for campaigns/partnerships, distinct from the above
   three): under **Subscription Prices → Offer Codes**, generate codes if
   WeStretch wants to run an external campaign (e.g. an influencer
   partnership or a win-back email with a redeemable code).
6. Set up **tracking**: per Knowledge Base, "track which offers produce
   paid conversions and long-term retention" — confirm App Store Connect's
   subscription reports (or whatever analytics/CRM WeStretch uses,
   fed by App Store Server Notifications' `OFFER_REDEEMED` events — see
   the 2026-08-21 grace-period checklist for that integration) capture
   offer redemption and downstream conversion.

**Pass looks like:** at least one active introductory offer configured on
each subscription product, matching the proven 7-day-free-trial structure
already live on the web; a promotional offer defined and ready for the
iOS app's cancel flow to call; a win-back offer active for lapsed
subscribers; a way to measure redemption-to-paid-conversion for each.

## Part 2 — iOS engineering work (not verifiable or doable from this repo)

1. Confirm StoreKit/IAP subscription integration exists in the app at
   all (see "open question" above) — if not, this is the actual
   prerequisite task.
2. Wire the promotional-offer signing flow (`requestPromotionalOffer` or
   StoreKit 2 equivalent) into the cancellation flow so the offer from
   Part 1 step 3 can actually be presented and redeemed.
3. Confirm the app doesn't need any code changes for win-back offers
   specifically — Apple's current win-back offer mechanism is largely
   server/App-Store-Connect-managed and surfaces automatically, but verify
   against the current StoreKit documentation version the app targets.
4. Make sure whatever "offer redeemed" handling exists on the backend
   (App Store Server Notifications' `OFFER_REDEEMED` type) actually
   updates the subscriber's entitlement/analytics record.

**Pass looks like:** a lapsed or about-to-cancel subscriber sees a real,
functioning offer in the app; redemption shows up in both App Store
Connect's reporting and WeStretch's own subscriber records.

## Recommended next step

Confirm the open question first (does WeStretch's iOS app sell
subscriptions via StoreKit/IAP today, or only via the website's Stripe
checkout?) — that determines whether Part 1 is a same-day App Store
Connect config task or whether it's blocked on Part 2's StoreKit
integration existing at all. Whoever owns the iOS codebase is best placed
to answer this quickly.
