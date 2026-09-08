# In-App Purchase / Subscription Showcase; Configuration Plan

**Backlog item:** Configure the in-app purchase/subscription showcase on the
product page (up to 20 items across IAPs + subscriptions, custom order,
35-char name / 55-char description each), new Apple feature, not yet used.
**Date:** 2026-09-07
**Produced by:** app-store-specialist-nightly-action (scheduled run)
**Status:** draft for review. Nothing was configured or submitted to Apple.

---

## Headline finding: WeStretch already sells through Apple IAP

The 2026-08-30 run (`Output/2026-08-30-subscription-offers-config-checklist.md`)
was blocked on an open question: *does the iOS app transact subscriptions
through StoreKit at all, or only through the website's Stripe links?*

**Answer: it transacts through Apple IAP.** The live US product page lists
in-app purchases, read tonight from the public storefront HTML (same
technique as the 2026-09-06 run, see project `Memory.md`; no App Store
Connect needed). That unblocks the introductory / promotional / win-back
offer work from 2026-08-30, which had been parked on this exact question.

## Live baseline (US storefront, read 2026-09-07)

Apple currently auto-generates a "Top In-App Purchases" list on the page,
capped at 10 items and ordered by Apple, not by WeStretch. What a visitor
sees today, verbatim, in this order:

| # | Name shown publicly | Price |
|---|---|---|
| 1 | Premium Monthly | $9.99 |
| 2 | Premium Yearly | $59.99 |
| 3 | Premium Quarterly | $20.99 |
| 4 | 999 Coins | $6.99 |
| 5 | 200 Coins | $1.99 |
| 6 | 50 Coins | $0.99 |
| 7 | `Streak Saver (1) ` | $1.99 |
| 8 | `Streak Saver (7) ` | $11.99 |
| 9 | `Streak Saver (3) ` | $4.99 |
| 10 | Pro Quarterly | $69.99 |

No showcase is configured. The page has no showcase section, no custom
order, and no per-item descriptions, so this backlog item's premise is
correct: this is a real, unused lever.

### Three problems visible on the live page right now

1. **These are internal SKU names, not marketing names.** "999 Coins",
   "Streak Saver (3)", "Pro Quarterly" read like a spreadsheet. A stranger
   deciding whether to download has no idea what any of them are.
2. **Three names have a trailing space** (`Streak Saver (1) `,
   `Streak Saver (3) `, `Streak Saver (7) `). Cosmetic, but it is public.
3. **The public names say "Premium." The app says "Pro."** WeStretch's own
   onboarding/paywall spec (`Team/CXO/In Progress/Onboarding UX Flow Spec/`)
   calls the paid tier **Pro** throughout ("Turn Pro banner",
   "coins-for-Pro-for-a-day", "Free to Pro conversion"). The store sells
   **Premium** Monthly/Yearly/Quarterly *and, separately,* a **Pro
   Quarterly** at $69.99, which is 3.3x the Premium Quarterly at $20.99.
   Either there are two genuinely different tiers nobody in this repo has
   written down, or the naming has drifted. **This needs Karen's answer
   before the showcase copy can be finalized** (see open questions).

Also worth noting: the Premium Monthly ($9.99) and Premium Yearly ($59.99)
prices match the website's Stripe links exactly, so the two channels are at
price parity. Good.

## What Apple allows

From `Knowledge Base/apple-marketing-opportunities.md` (2026-09-01 entry):

- Up to **20 items total**, across in-app purchases and subscriptions combined.
- **Customizable display order**; WeStretch chooses it, not Apple.
- Per item: **display name max 35 characters**, **description max 55 characters**.
- Showcased items are **discoverable in App Store search** and **can be
  featured on the Today / Apps tabs**, routing back to the product page.

Source: https://developer.apple.com/app-store/product-page/

## Recommendation: showcase 3 items, not 10

The instinct is to fill all 20 slots. Don't. WeStretch has at most 10
publicly visible SKUs and 7 of them are consumables (coins and streak
savers). Putting a coin store on the product page makes a health and
mobility app look like a game with paid boosts, to someone who has not
installed it yet and has no idea what a streak is. Coins and streak savers
are **retention** mechanics that make sense *after* download; they are not
**acquisition** arguments.

The showcase's real value here is the opposite: it is the first chance to
put a *sentence* next to the subscription instead of just a price.

**Recommended showcase, in this display order:**

| Order | SKU | Display name | Chars | Description | Chars |
|---|---|---|---|---|---|
| 1 | Premium Yearly | `Premium Annual` | 14/35 | `Every routine, every goal, all year. Best value.` | 48/55 |
| 2 | Premium Monthly | `Premium Monthly` | 15/35 | `Every routine, every goal. Month to month.` | 42/55 |
| 3 | Premium Quarterly | `Premium 3 Months` | 16/35 | `Every routine, every goal, for three months.` | 44/55 |

Annual goes first deliberately: it is the plan WeStretch wants, and the
showcase order is one of the few places Apple lets you say so. Apple renders
the price itself, so no prices appear in the copy (per the Knowledge Base
rule that prices vary by region and must not be hard-coded into metadata).

**Pro Quarterly is deliberately left out of the draft** because I don't know
what it is. If Pro is a real, better tier, it probably belongs at position 1.
Placeholder if it stays:

| Order | SKU | Display name | Chars | Description | Chars |
|---|---|---|---|---|---|
| ? | Pro Quarterly | `Pro 3 Months` | 12/35 | *needs the answer to "what does Pro add?"* | - |

### Fallback copy, if Karen wants the consumables showcased anyway

Not recommended, but drafted so the decision isn't blocked on writing. All
within limits:

| SKU | Display name | Chars | Description | Chars |
|---|---|---|---|---|
| 999 Coins | `999 Coins` | 9/35 | `Earn coins by stretching, or top up your balance.` | 49/55 |
| 200 Coins | `200 Coins` | 9/35 | `A mid-size coin top-up for streak savers.` | 41/55 |
| 50 Coins | `50 Coins` | 8/35 | `A small coin top-up for streak savers.` | 38/55 |
| Streak Saver (1) | `1 Streak Saver` | 14/35 | `Miss a day without losing your streak. One save.` | 48/55 |
| Streak Saver (3) | `3 Streak Savers` | 15/35 | `Protect your streak on three missed days.` | 41/55 |
| Streak Saver (7) | `7 Streak Savers` | 15/35 | `Protect your streak on seven missed days.` | 41/55 |

The coin descriptions assume coins are *earned by finishing routines* and
*spent on streak savers*, which is what
`Team/CXO/In Progress/Onboarding UX Flow Spec/Storyline.md` says ("finishing
a routine earns coins; coins can buy a streak saver"). That same spec's
`Screens/Streak Saver Offer.md` flags the mechanic as **unconfirmed**, so
confirm it before publishing this copy.

## Whoever has App Store Connect access: what to do

1. **App Store Connect, WeStretch, the in-app purchase / subscription
   showcase section of the product page.** Confirm the feature is available
   on this account (it is new; availability may lag).
2. **Before configuring: check whether turning the showcase on replaces the
   auto-generated "Top In-App Purchases" list, or sits alongside it.** I
   could not determine this from the public page or the Knowledge Base. If
   it only *adds* a section and the raw-SKU-name list stays, then the
   trailing-space and Premium-vs-Pro naming problems above still need fixing
   at the SKU level regardless.
3. **Check whether each showcased item requires promotional artwork.**
   Apple's older "promote your in-app purchases" feature required a
   1024x1024 image per item. If the showcase does too, that is an asset
   request to
   `Team/CMO/In Progress/App Store Specialist/App Store Image Creation/`,
   and this item is blocked on it. **Verify, don't assume**; the Knowledge
   Base entry doesn't mention artwork either way.
4. **Enter the three rows** from the recommended table, in that order.
5. **Fix the three trailing spaces** in the Streak Saver reference names
   while you're in there.
6. **Report back the full SKU list.** The public page caps at 10 items;
   there are probably more (a Pro Monthly and Pro Yearly would be the
   obvious guesses). The showcase allows 20, so the real list matters.
7. **Localization:** showcase names and descriptions are metadata and will
   need French and Spanish versions, same as everything else. Feed them into
   the localization item
   (`Output/2026-08-26-localize-app-store-assets-fr-es.md`) rather than
   treating them separately.

## Open questions for Karen

1. **What is "Pro Quarterly" ($69.99) and how does it differ from "Premium
   Quarterly" ($20.99)?** Everything else in this plan is drafted; this is
   the one thing genuinely blocking a final version.
2. **Should the store say "Pro" or "Premium"?** The app says Pro. The store
   says Premium. Pick one; the mismatch costs conversion at the paywall,
   because the name the user just saw on the product page isn't the name
   inside the app.
3. **Showcase the consumables (coins, streak savers) or not?** My
   recommendation is no, subscriptions only. Fallback copy is drafted above
   if you disagree.
4. **Is "Best value" acceptable on the annual plan?** It is true relative to
   WeStretch's own monthly price, which is what makes it safe. Flagging it
   only because the 2026-09-06 run found four claim-compliance problems in
   the live description, so this is worth a deliberate yes.

## Carry-forward for other backlog items

- **The 2026-08-30 subscription offers item is unblocked.** Its blocking
  question ("does WeStretch sell via StoreKit?") is now answered: yes.
  Introductory / promotional / win-back offers are all actually available.
- **Premium/Pro naming** is bigger than this item and touches the paywall,
  the description, and the CXO onboarding spec. Flagged to the Manager.

## How the live data was read (repeatable, no App Store Connect)

```
curl -sL -A "<browser user agent>" \
  "https://apps.apple.com/us/app/westretch-the-stretching-app/id1458915362"
```

The IAP list is in the page's embedded JSON, under an `Annotation` block with
`"title":"In-App Purchases"`, as `textPairs` of `[name, price]`. The
`itunes.apple.com/lookup` API does **not** return in-app purchases; only the
storefront HTML does.
