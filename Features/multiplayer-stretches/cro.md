# CRO — Pricing Strategy: Multiplayer Stretching

_Skill applied: `CRO/skills/pricing-strategy`_

## Current state

WeStretch's existing tier structure is assumed to be free + paid subscription (confirm actual tiers before finalizing). No current pricing decision has been made about where multiplayer sits relative to that split.

## Proposal

Launch multiplayer stretching as **available to all users, including free tier**, at least for the async MVP. Rationale: this is fundamentally a retention and viral-loop mechanic (per [cgo.md](cgo.md) and [cmo.md](cmo.md)) — gating it behind a paywall suppresses exactly the invite behavior that makes it valuable, since free-tier users invited into a party may be the strongest paid-conversion leads once they're hooked on the app.

Reserve monetization for a later layer once the mechanic is proven: e.g., a paid tier unlocks larger group sizes, custom/curated group routines, or (if built) live synced sessions — not the core social mechanic itself.

## Impact estimate

- **Conversion**: indirect positive — multiplayer as a free-tier hook should improve free-to-paid conversion by increasing engagement depth and habit formation, more than it would as a direct paywalled feature. *(Estimate, not measured — validate via the CGO experiment before committing to a paid-tier gate later.)*
- **Existing-user sentiment**: low risk, since nothing is being taken away or repriced — this is additive to the free tier.

## Rollout plan

- No grandfathering needed since this isn't a price change — it's a new free-tier capability.
- Communicate as an app update/feature announcement (see [cmo.md](cmo.md)), not a "new plan" — framing it as a paywalled premium feature at launch would undercut the growth-loop rationale above.
- Revisit monetization only after the CGO retention experiment confirms the mechanic works, and only add paywalled *extensions* (bigger groups, live sync), never retroactively gate the core async feature.
