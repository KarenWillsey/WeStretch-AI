# EU App Store business terms; do they change WeStretch's economics?

**Backlog item:** "Evaluate whether Apple's EU alternative business terms
(10% commission) change WeStretch's economics, if EU is a meaningful
subscriber market."
**Date:** 2026-09-05
**Run:** scheduled nightly-action (app-store-specialist-nightly-action)
**Shape:** research/evaluation. Nothing here is a live action against Apple.

---

## Short answer

**No, and the premise the item was written on is now out of date.**

The "EU alternative business terms at 10% commission" that this item was
seeded from (the Alternative Terms Addendum for Apps in the EU) **no
longer exists as a separate track.** Apple announced on 2026-08-18 that it
is collapsing every EU developer onto a **single unified set of EU
business terms, effective 2026-10-01**, and the Alternative Terms Addendum
and the StoreKit External Purchase Link Entitlement Addendum are
discontinued.

Under the unified terms, a WeStretch that is enrolled in the **Small
Business Program and selling through Apple In-App Purchase pays 15% in the
EU**, which is exactly what it pays everywhere else. So on the default
path there is **no EU-specific economic advantage or disadvantage left to
chase.** The question resolves without needing EU subscriber-mix data.

There *is* a 10% rate still on the table, but only if WeStretch stops
using Apple IAP in the EU (see "The one lever that still exists" below),
and the arithmetic on that comes out roughly break-even while adding real
compliance work. **Recommendation: stay on Apple In-App Purchase in the
EU.**

One thing genuinely needs doing before 2026-10-01, and it is not a
marketing task; see "Action required before 2026-10-01."

---

## What the unified EU terms actually are

Verified live on 2026-09-05 against
`https://developer.apple.com/support/apps-in-the-eu/` and
`https://developer.apple.com/support/dma-and-apps-in-the-eu/`, plus
Apple Newsroom's 2026-08 announcement. Rates quoted from Apple's own fee
tables.

**App Store commission (Apple In-App Purchase)**

| Rate | Applies to |
|---|---|
| 26% | Sales processed by Apple In-App Purchase. |
| 15% | Sales via Apple IAP from Small Business Program / Mini Apps Partner Program / Video Partner Program participants, **and** auto-renewable subscriptions after their first year. |

**App Store commission (alternative payment processing inside the app)**

| Rate | Applies to |
|---|---|
| 20% | Sales processed via alternative payment processing within the app. |
| 10% | Same, for Small Business Program / Mini Apps / Video Partner participants, and auto-renewable subscriptions after their first year. |

**Store services commission (out-of-app offers with actionable links)**

| Rate | Applies to |
|---|---|
| 15% | Out-of-app offers, excluding program participants and post-first-year auto-renewable subscriptions. |
| 10% | Out-of-app offers for program participants, and for auto-renewable subscriptions after a subscriber's first year. |

Only sales made **within 7 days of the link tap** are commissionable.

**Core Technology Commission**: 5% on sales in apps distributed **outside**
the App Store (alternative marketplaces or Web Distribution). It replaces
the old per-install Core Technology Fee. **It does not apply to apps
distributed on the App Store**, so it is irrelevant to WeStretch unless
WeStretch ever ships outside the App Store, which is not on any roadmap in
this repo. The old Initial Acquisition Fee and Store Services Fee tiers
are gone.

---

## Why this is a no-op for WeStretch's default path

WeStretch's known pricing (from `website-repo`'s live Stripe links, carried
forward from the 2026-08-30 subscription-offers checklist): **Monthly
$9.99/mo, Annual $59.99/yr, both with a 7-day free trial.**

| Path | Commission today (rest of world) | Commission in EU from 2026-10-01 |
|---|---|---|
| Apple IAP, Small Business Program member | 15% | **15%** |
| Apple IAP, not in Small Business Program | 30% | 26% (slightly better than ROW) |

If WeStretch is a Small Business Program participant, EU commission is
identical to everywhere else and no action changes that. If WeStretch is
*not* enrolled, the EU is marginally cheaper than the rest of the world
(26% vs 30%), but the fix for that is enrolling in the Small Business
Program, which is already its own open item (see
`Output/2026-08-21-small-business-program-checklist.md`, still unverified),
not anything EU-specific.

**Note the second half of the 15% row.** Auto-renewable subscriptions drop
to 15% after a subscriber's first year *regardless of Small Business
Program status*. For a Small Business Program member that is worth nothing
extra, because 15% is already the rate from day one. It only starts to
matter if WeStretch outgrows the program's $1M proceeds ceiling.

---

## The one lever that still exists, and why I do not recommend pulling it

The only way to reach 10% in the EU is to move off Apple IAP: either
**alternative payment processing inside the app** (10% for Small Business
Program members) or **linking out to WeStretch's own web checkout** (10%,
7-day attribution window). WeStretch already has a working Stripe checkout
on the website, so the link-out variant looks superficially cheap to do.

The arithmetic does not support it. Worked on a EUR 9.99 monthly sub, EU
VAT assumed at 21% (it varies by member state), assumptions stated below:

| | Apple IAP @ 15% | Own checkout @ 10% |
|---|---|---|
| Gross price | 9.99 | 9.99 |
| Less VAT at 21% | 8.26 net | 8.26 net |
| Apple commission | 1.24 | 0.83 |
| Payment processing (Stripe, approx. 1.5% + 0.25 EU cards) | 0.00 (Apple is merchant of record) | approx. 0.40 |
| **Developer keeps** | **approx. 7.02** | **approx. 7.03** |

Roughly a wash: about one cent per subscriber per month. And the
right-hand column additionally costs:

- **You become responsible for EU VAT.** Apple's own wording: "you're
  responsible for the collection and remittance of any applicable taxes
  for sales processed by an alternative payment provider." That means VAT
  OSS registration and filing, currently Apple's problem, not WeStretch's.
- **Monthly transaction reporting to Apple**, due within 15 days of each
  month end, per Apple's terms. A recurring operational obligation with a
  hard deadline.
- **A 12-month lock-in.** Apple: developers "select their payment
  options... and must maintain those options for 12 months." A wrong call
  here cannot be quietly reversed next quarter.
- **You own refunds, chargebacks, failed-payment recovery and billing
  support** in the EU, and you lose Apple's Billing Grace Period and
  App Store Server Notifications machinery for those subscribers, which is
  itself still an open work item
  (`Output/2026-08-21-billing-grace-period-and-server-notifications-checklist.md`).
- **Attribution risk on the link-out variant specifically:** only
  conversions within 7 days of the tap are commissionable to Apple, but
  conversions outside that window are also conversions WeStretch has to
  earn unaided, through a checkout handoff that leaks measurably compared
  to a native IAP sheet.

For a subscription business at WeStretch's scale, trading Apple's
merchant-of-record status and billing infrastructure for approximately
zero margin is a bad deal. Revisit only if WeStretch exits the Small
Business Program, where the comparison becomes 26% vs 10% and is a
genuinely different question.

**Assumptions in that table that a CFO should confirm before anyone acts
on it:** that Apple computes EU commission on the VAT-exclusive price;
WeStretch's actual Stripe EU card rate; and the blended VAT rate across
WeStretch's real EU subscriber mix. I could not verify any of the three.
The conclusion is not sensitive to reasonable variation in them; the two
columns stay within a few cents of each other unless Stripe's effective
rate is far below list.

---

## Action required before 2026-10-01 (not a marketing task)

This is the one thing in this item that needs a human with account access,
and it has a date on it. Apple's wording:

> "To move to the unified EU terms, they will need to agree to the updated
> Apple Developer Program License Agreement. After agreeing to the updated
> terms, their account will be subject to the unified EU terms starting
> October 1, 2026, or the date they agree, whichever is later."

Apple's page **does not state what happens to a developer who takes no
action by 2026-10-01.** That is a real open question, not a rhetorical
one, and the safe reading is that uninterrupted EU distribution should not
be assumed on an unsigned agreement.

**For whoever holds the Apple Developer Program Account Holder role:**

1. Sign in to App Store Connect, go to **Business** (or **Agreements, Tax,
   and Banking**), and check whether an **updated Apple Developer Program
   License Agreement** is pending acceptance.
2. If one is pending, read it and decide whether to accept before
   2026-10-01. **Pass looks like:** no pending agreement blocking EU
   distribution, and the account showing the unified EU terms.
3. While in there, confirm the **Small Business Program** enrollment status
   that the 2026-08-21 item is still waiting on. That single fact decides
   whether WeStretch's EU rate is 15% or 26%, and it is worth more than
   anything else in this document.
4. Do **not** accept any entitlement for alternative payment processing or
   external purchase links in the EU on the strength of this brief. Per the
   analysis above the recommendation is to stay on Apple IAP, and the
   choice locks for 12 months.

I have no App Store Connect or Apple Developer account access, so I cannot
check any of the above myself and am not claiming it is done.

---

## Recommended next step

Close this backlog item as answered: **no, the EU terms do not change
WeStretch's economics**, and the sub-question "is EU a meaningful
subscriber market" no longer needs answering to resolve it, because the
answer is the same either way. The only carry-forward is the Account
Holder check above, flagged separately in `WORK-TRACKER.md` because it is
time-boxed to 2026-10-01 and is not a CMO task.

## Knowledge Base correction

`Knowledge Base/apple-marketing-opportunities.md` (Small Business Program
section, the `[2026-08-21]` bullet) still described the now-discontinued EU
10% alternative-terms track as if it were current. I added a dated
correction line there pointing at this file, and flagged it for the next
monthly refresh so the fix survives the next live diff.

---

**Sources** (fetched live 2026-09-05):

- [Changes for apps in the European Union (Apple Developer Support)](https://developer.apple.com/support/apps-in-the-eu/)
- [DMA and apps in the EU (Apple Developer Support)](https://developer.apple.com/support/dma-and-apps-in-the-eu/)
- [Apple announces changes for apps in the European Union (Apple Newsroom, 2026-08)](https://www.apple.com/newsroom/2026/08/apple-announces-changes-for-apps-in-the-european-union/)
