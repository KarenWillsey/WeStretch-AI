# COO; Cross-Team Execution Plan: Path to 1,000 DAU

_Skill applied: `Team/COO/skills/cross-team-execution-plan`_

## Workstreams

1. **Analytics & DAU-definition lockdown** (CIO + CTO), gates every other workstream; see [cio.md](cio.md), [cto.md](cto.md).
2. **Onboarding/activation fix** (CXO + CTO + CPO); see [cxo.md](cxo.md), [cpo.md](cpo.md).
3. **Referral/invite loop** (CPO + CTO + CGO); build, then run as a live experiment; see [cgo.md](cgo.md), [cpo.md](cpo.md), [cto.md](cto.md).
4. **Organic content, ASO, and partnerships** (CMO), parallel, ongoing from week 1; see [cmo.md](cmo.md).
5. **Pricing/paywall decision** (CRO + CFO + CEO), a single upfront decision, not an ongoing workstream; see [cro.md](cro.md).
6. **Weekly growth review** (CGO owns, all roles attend), standing sync reading DAU, activation, and K-factor from week 1 through week 12.

## Owners and timeline

**Weeks 1–3; Foundation**
- Lock the DAU definition and ship event instrumentation (CIO/CTO).
- Confirm or rule out existing deep-link, push, and pricing infrastructure (CTO), resolves the provisional-estimate flags in [cto.md](cto.md).
- Ship onboarding quick wins (CXO/CTO).
- CEO makes the pricing/paywall call for the quarter (CRO/CFO input); see the disagreement preserved in [cro.md](cro.md).
- Ship ASO assets (CMO).
- Run the 5-user research pass (CPO).

**Weeks 4–8; Loop**
- Referral/invite loop live, K-factor experiment running (CGO/CTO).
- Re-engagement pushes live (CTO/CIO).
- Organic content cadence running (CMO).
- Weekly K-factor and retention read; week 6 is the explicit go/no-go checkpoint on the $0-budget approach (CFO, per [cfo.md](cfo.md)).

**Weeks 9–12; Push or pivot**
- If K-factor cleared threshold: double down on the referral loop, scale content around what's working.
- If not: escalate to CEO/board on budget injection vs. timeline extension per [cfo.md](cfo.md); don't quietly extend the same tactics past their tested limit.
- Cut anything not moving the DAU number by week 10, regardless of how much work has already gone into it.

## Coordination risks

The most likely failure mode on a small bootstrap team is one or two engineers becoming a sequential bottleneck across workstreams 1–3, since all three touch [cto.md](cto.md). Mitigate with a single shared tracker and one named DRI per workstream (even where the same person holds two DRI roles, the roles themselves should stay distinct in the tracker so a slip is visible immediately rather than absorbed silently. Second risk: workstream 5's pricing decision needs to land in week 1, not drift) a late pricing call would delay the DAU-vs-revenue framing every other workstream depends on.

## Definition of done

DAU, using the single definition locked in week 1 ([cio.md](cio.md)), sustained at **≥1,000 for 7 consecutive days** (not a single-day spike from a one-off content hit. If week 12 arrives short of that bar but the K-factor and retention trendlines are clearly still climbing, that is a "continue, don't restart" signal, not a failure) the plan's honest goal is a validated, compounding organic loop, of which hitting 1,000 by an exact date is the target but not the only measure of success.
