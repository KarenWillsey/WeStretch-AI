# Monthly-with-12-Month-Commitment Plan + Streamlined Purchasing

**Backlog item:** Evaluate offering a monthly subscription with a 12-month
commitment as an additional plan tier alongside the existing Monthly/Annual
options, and confirm whether "streamlined purchasing" (completing a purchase
from outside the app) should stay on or be turned off.
**Date:** 2026-09-11
**Produced by:** app-store-specialist-nightly-action (scheduled run)

---

## The short version

**Question 1, the 12-month commitment plan: it cannot be sold in the United
States.** Apple excludes the US and Singapore from this billing option. Every
other storefront can have it. So this is not a "new tier for WeStretch," it is
an international-only tier. Whether it is worth doing comes down to one number
nobody in this repo has: what share of WeStretch's subscription revenue comes
from outside the US. Recommendation below, with the pricing already worked out
for the four storefronts I could read.

**Question 2, streamlined purchasing: leave it ON. It is currently doing
nothing anyway.** The setting only affects two Apple surfaces (Win-back Offers
and Contingent Pricing), and WeStretch has neither one configured. The real
task is not flipping a switch, it is making sure the app can handle a purchase
that happens outside it. That needs one StoreKit API (`PurchaseIntent`) and a
release. Ship that, then revisit.

---

# Part 1: Monthly subscription with a 12-month commitment

## What it actually is

The subscriber pays monthly, but commits to 12 monthly payments. It is an
annual plan wearing a monthly price tag.

Apple's own wording:

> "Unlike a standard monthly subscription, the subscriber is committing to 12
> monthly payments."

> "Once all 12 payments are completed, the subscription automatically renews
> into another 12 month commitment at the standard billing price of that
> payment option until they choose to cancel."

And the part that matters most:

> "If a customer cancels before the end of their commitment, they'll continue
> paying until their commitment is complete (except in certain regions), and
> their subscription will not renew."

## The four hard constraints

**1. Not available in the United States or Singapore.** Available in the other
173 App Store countries/regions. This is a flat Apple restriction, not
something WeStretch can work around.

**2. It is built on top of the annual plan, not next to it.** You do not create
a new product. You take the existing 1-year subscription (Premium Yearly), set
up "Upfront Billing" availability first, then add "Monthly with 12-Month
Commitment" availability on top. Apple: "Monthly billing will only be available
in countries or regions where you have set up upfront billing availability."

**3. The price is boxed in by Apple.** "The 12-month commitment total must be
greater than or equal to the upfront price, and less than or equal to 1.5 times
the upfront price." So the annual price sets both the floor and the ceiling.

**4. Device and build requirements.** It only shows on devices running OS 26.4
or later, and only in apps built with SDK 26.5 or later. iOS 26.6.2 was current
as of early September 2026 and iOS 27 ships 2026-09-14, so 26.4+ already covers
a large majority of active devices. But WeStretch's minimum iOS is 15.2, which
suggests a deliberately older-device-friendly audience. Those users simply will
not see this option. That is graceful degradation, not a blocker.

## What it would cost, per storefront

I read the live in-app purchase prices off four non-US storefronts tonight.
Apple's 1.0x-to-1.5x rule then gives the legal price band exactly:

| Storefront | Premium Yearly (upfront) | Standalone Monthly | Legal commitment total | Per month that is | Suggested price |
|---|---|---|---|---|---|
| United Kingdom | £34.99 | £4.99 | £34.99 to £52.49 | £2.92 to £4.37 | **£4.29/mo** (£51.48) |
| Germany | €34.99 | €4.99 | €34.99 to €52.49 | €2.92 to €4.37 | **€4.29/mo** (€51.48) |
| Canada | C$59.99 | C$9.99 | C$59.99 to C$89.99 | C$5.00 to C$7.50 | **C$7.49/mo** (C$89.88) |
| Australia | A$69.99 | A$9.99 | A$69.99 to A$104.99 | A$5.83 to A$8.75 | **A$8.49/mo** (A$101.88) |

Prices must land on one of Apple's price points, so the exact figures above may
snap to the nearest rung. Treat them as targets, not final values.

**The useful thing about that table:** in every storefront, Apple's maximum
allowed commitment price is *below* the standalone monthly price. The plan
cannot help but look like a discount. £4.29 reads cheaper than £4.99, and the
customer still pays £51.48 over the year against £34.99 for the annual plan.
That is roughly **47% more revenue per subscriber-year than the annual plan**,
from a price that presents as cheaper than monthly.

Against the standalone monthly plan the gain is larger still, because monthly
subscribers churn. If the average WeStretch monthly subscriber stays four
months, that is £19.96 in the UK. A 12-month commitment is £51.48 guaranteed.

## The honest counterweight

The mechanic that makes it profitable is the same mechanic that generates angry
customers. Someone who wants out in month three keeps paying for nine more
months. Apple exempts "certain regions," but most are not exempt.

Two things make that riskier for WeStretch than for an average app:

- **The audience skews older.** The positioning, the iOS 15.2 minimum, and the
  accessibility angle all point the same way. A locked-in annual commitment
  billed monthly is the kind of thing that reads as a trap to that audience,
  and it is the kind of complaint that goes to a credit card company rather
  than to support.
- **The rating base is thin.** 53 ratings at 4.45 stars as of tonight. It does
  not take many "I could not cancel" one-star reviews to move that number, and
  product page quality is one of Apple's featuring criteria.

There is also a cash-flow trade. The annual plan collects £34.99 today. The
commitment plan collects £4.29 today and the rest over a year. More money
total, slower.

And it renews into *another* 12-month commitment automatically. That is a
heavier lock than the annual plan, which a customer can cancel any time before
renewal.

## Recommendation

**Do not roll this out globally. Decide it with one number, then pilot.**

The number: what percentage of WeStretch's subscription revenue comes from
outside the US and Singapore? That is in App Store Connect under Sales and
Trends, broken out by territory. Nothing in this repo has it.

- **If under roughly 15%:** park this item. The upside is capped by a small
  base, and the brand risk is not worth it for a rounding error.
- **If meaningful:** pilot in **the UK and Canada only**, for one quarter. Both
  are English-language, both already have real local pricing, and both are
  small enough to pull the plug on. Hold Germany and Australia back until the
  pilot reports.

Three things should land before the pilot, not after:

1. **The Premium vs Pro naming split gets settled** (open since 2026-09-07). A
   confusing plan lineup plus a lock-in commitment is the worst combination.
2. **The in-app purchase showcase gets configured** (drafted 2026-09-07), so
   the product page explains the plans in plain words instead of showing raw
   SKU names.
3. **The paywall states the commitment honestly.** The Knowledge Base already
   carries Apple's rule that "the full billed amount must be the most prominent
   price shown." For this plan that means the paywall has to show the total and
   the 12-payment obligation clearly, not bury them under "£4.29/mo."

If it goes live and generates complaints, Apple lets you back out: App Store
Connect, Availability, Monthly with 12 Month Commitment, Remove Monthly
Billing. Existing customers finish their commitment and then do not renew.

---

# Part 2: Streamlined purchasing

## What it actually covers, which is less than the item implies

Streamlined purchasing lets someone buy a WeStretch subscription from inside
the App Store app, without opening WeStretch. It is **on by default**.

But Apple's help page is specific about the scope:

> "Turning off streamlined purchasing will apply to subscriptions merchandised
> on the App Store like Contingent Pricing and Win-back Offers."

It explicitly does **not** apply to subscription offer codes or in-app purchase
promo codes redeemed from the App Store.

So the setting only does anything if WeStretch has Win-back Offers or
Contingent Pricing running.

- **Win-back Offers:** drafted and recommended on 2026-08-30, never confirmed
  as configured. No evidence in this repo that any exist.
- **Contingent Pricing:** a discount for people who subscribe to a different
  app's subscription. Apple ran it as an invite-only pilot. WeStretch is almost
  certainly not in it.

**Conclusion: streamlined purchasing is switched on and attached to nothing.**
There is no live surface for anyone to buy from outside the app today. Turning
it off would change nothing, and turning it off is not even possible right now
(see below).

## The question that will actually matter

It becomes real the moment Win-back Offers go live. At that point a lapsed
subscriber can tap a win-back offer in the App Store and pay, never having
opened WeStretch.

Apple's stated reason to turn the setting off:

> "If your subscription requires steps at the time of purchase, such as signing
> into the app, you can choose to turn off streamlined purchasing."

**That describes WeStretch.** The CXO onboarding spec treats login as optional
and supports a guest path, while streaks, coins and cross-device history are
account-bound. If Premium entitlement is tied to a WeStretch account
server-side, an App-Store-side purchase arrives with no account to attach it
to. The customer has paid and has nothing until they open the app and sign in.

**But turning it off is the wrong fix.** It adds friction to exactly the flow
the win-back offer exists for: the lapsed user now has to go find the app and
open it. You would be blunting your own re-acquisition tool.

## Recommendation

**Leave streamlined purchasing ON. Fix the app instead.**

The right fix is `PurchaseIntent`, the StoreKit API Apple points at. The app
watches for a purchase that started outside it, then on next launch attaches
the entitlement to the right account, prompting for sign-in if it has to, and
lands the user straight in the paid experience rather than back at a paywall.

Three reasons this is the better path:

1. It keeps the low-friction purchase that makes win-back offers work.
2. It solves the account-attachment problem instead of avoiding it.
3. **It is the prerequisite for ever turning the setting off.** Apple: "Before
   you can turn off streamlined purchasing, your latest approved binary must
   include the necessary StoreKit APIs." So today WeStretch could not turn it
   off even if it wanted to. Shipping `PurchaseIntent` buys the option.

**Sequencing:** ship `PurchaseIntent` handling in a normal release, then
configure Win-back Offers, then watch the first ones land. Only flip the switch
off if account reconciliation genuinely cannot be made to work.

## If it does need turning off later

Role needed: Account Holder, Admin, App Manager, or Marketing.

1. App Store Connect, Apps, select WeStretch.
2. Sidebar, **Subscriptions**.
3. Scroll to **Streamlined Purchasing**, click **Edit**.
4. Toggle off.

It sits just under Billing Grace Period, which is the same screen the
2026-08-21 billing-grace-period checklist sends someone to. Worth doing both in
one visit.

---

## What I could not verify

No App Store Connect access, and this repo holds no application source code.

- Whether Win-back Offers or Contingent Pricing are configured. Not publicly
  readable.
- What share of subscription revenue is non-US. Sales and Trends, by territory.
- Whether Premium entitlement is account-bound or device-bound. Needs the iOS
  app and its backend.
- Whether the shipping build uses SDK 26.5 or later.
- Whether the app already implements `PurchaseIntent`. Almost certainly not,
  but it needs the codebase to confirm.

---

## Incidental findings (not part of the backlog item)

Reading four storefronts to build the pricing table turned up three things
nobody has recorded:

**1. International pricing is roughly half the US price in the UK and Germany.**

| | US | UK | Germany | Canada | Australia |
|---|---|---|---|---|---|
| Premium Monthly | $9.99 | £4.99 | €4.99 | C$9.99 | A$9.99 |
| Premium Yearly | $59.99 | £34.99 | €34.99 | C$59.99 | A$69.99 |
| Premium Quarterly | $20.99 | £11.99 | (not listed) | C$20.99 | A$22.99 |

£4.99 is about US$6.30 and €4.99 is about US$5.40, against $9.99 in the US.
That is roughly a 40% discount to UK and German customers. It may be deliberate
purchasing-power pricing, or a stale price tier nobody has revisited. Worth a
look by whoever owns pricing.

**2. Two SKUs exist that have never appeared in the US list.** "Missed Day
Token" at C$2.99 / A$2.99, and "Pro Monthly" at €34.99 in Germany. Apple caps
the public list at ten items and orders it itself, so this may be display
ordering rather than a real availability difference. But "Pro Monthly" at
€34.99 a month, sitting next to Premium Monthly at €4.99, is a seven-fold gap
that nothing in this repo explains. It is the same unresolved Premium-vs-Pro
question flagged on 2026-09-07, now with a second data point.

**3. The US in-app purchase list is unchanged since 2026-09-07.** Same ten
SKUs, same prices. Live version is 8.1.33, shipped 2026-09-10. Rating is 4.45
stars on 53 ratings, also unchanged.

---

## Decisions needed from Karen

1. **Is the non-US share of subscription revenue big enough to bother?** This
   decides the whole 12-month-commitment question. Needs one look at App Store
   Connect, Sales and Trends, by territory.
2. **If yes, is a lock-in commitment plan acceptable for WeStretch's brand?**
   Someone who cancels in month three keeps paying for nine more. That is a
   product decision as much as a pricing one, and it sits awkwardly next to the
   older-adult positioning.
3. **UK and Canada pilot, or skip it entirely?** Recommendation is pilot those
   two for a quarter, or skip. Not a global launch either way.
4. **Should `PurchaseIntent` go on the iOS backlog now?** It is the unlock for
   win-back offers working properly, and the prerequisite for ever turning
   streamlined purchasing off.
5. **Are the UK and German prices intentional?** About 40% below the US.

---

## Sources

- Apple, Auto-renewable Subscriptions: https://developer.apple.com/app-store/subscriptions/
- Apple, Set availability for an auto-renewable subscription (12-month commitment rules, pricing band, regional exclusions, OS/SDK requirements): https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-availability-for-an-auto-renewable-subscription/
- Apple, Manage Streamlined Purchasing (default on, scope, role, steps, PurchaseIntent prerequisite): https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-streamlined-purchasing/
- Apple, PurchaseIntent (StoreKit): https://developer.apple.com/documentation/storekit/purchaseintent
- Apple, Announcing contingent pricing for subscriptions: https://developer.apple.com/news/?id=6e9odqgu
- Live pricing and app metadata read 2026-09-11 from `itunes.apple.com/lookup?id=1458915362` and the US/CA/GB/AU/DE storefront HTML, using the method recorded in this project's `Memory.md`.
