# CTO — Engineering Roadmap & Architecture: Path to 1,000 DAU

_Skills applied: `Team/CTO/skills/tech-architecture-review`, `Team/CTO/skills/engineering-roadmap`_

## Tech architecture review

### Current state

**Unknown to this planning pass.** No repo describes WeStretch's actual mobile/backend/infra stack, whether push notifications are wired up, or whether deep-linking/attribution exists. Every estimate below is provisional pending a real codebase/infra review — this repeats, deliberately, the exact caution [`CHATTY_REVIEW.md`](../Multiplayer Stretches/CHATTY_REVIEW.md) raised about the prior Multiplayer Stretches pass, which handed down firm effort estimates without ever confirming the underlying architecture.

### Options

Rather than 2-3 architecture paths for a single system, the real decision here is **build-vs-defer** across three candidate capabilities:

1. **Analytics/event instrumentation** — needed regardless of stack; likely the fastest path is a drop-in SDK (e.g., an existing analytics vendor) rather than building anything custom.
2. **Deep-link + attribution for referrals** — if the app already has any deep-linking, this is small; if not, this is the single largest unknown-cost item in the whole plan.
3. **Push infrastructure** — same shape of risk: small if it exists, a real project if it doesn't.

### Recommendation

Spend the first few days of week 1 answering "does X exist already" for all three, before committing the 12-week roadmap below to specific effort sizes. A lean team should not build new real-time or social backend infrastructure this quarter regardless of the answer — see cut list below.

### Risks

Building on unconfirmed assumptions about existing infra is exactly how the prior feature's timeline became untrustworthy. Flag any effort estimate below as **provisional** until discovery closes this gap.

## Engineering roadmap

Given a small/bootstrap engineering team (assume 1–2 engineers unless [chro.md](chro.md)'s constraints say otherwise):

1. **Analytics/activation/retention event instrumentation** (S–M, but only if a vendor SDK is used; L if built from scratch) — must ship first, everything else is unmeasurable without it. See [cio.md](cio.md).
2. **Referral/invite link + attribution** (S–M if deep-linking exists, else M–L) — primary growth lever per [cgo.md](cgo.md)/[cpo.md](cpo.md).
3. **Onboarding reorder** (S) — defer signup past first-workout preview, per [cxo.md](cxo.md).
4. **Push re-engagement triggers** (S if push infra exists, else M–L).
5. **ASO assets** — no engineering effort; owned by [cmo.md](cmo.md).

### Debt vs. features balance

Reserve roughly 20% of capacity for reliability — a growth push that causes crashes or slowdowns under new load defeats its own purpose. 80% to the roadmap above.

### Risks to the timeline

With only 1–2 engineers and 4 build items above, item 4 (push re-engagement) is the most likely to slip if item 2's actual effort turns out larger than assumed. Flag this now rather than discover it in week 8.

### What's explicitly deprioritized

- Any live/synchronous multiplayer or new real-time backend — same conclusion the prior planning pass reached in [`Features/Multiplayer Stretches/cto.md`](../Multiplayer Stretches/cto.md), still valid, and matches [cpo.md](cpo.md)'s cut list here.
- Any new backend migration or platform change — not proportionate to a 3-month growth sprint on a small team.
