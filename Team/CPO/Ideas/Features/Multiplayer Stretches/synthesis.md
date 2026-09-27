# Synthesis: Multiplayer Stretching

Cross-functional summary of [cpo.md](cpo.md), [cto.md](cto.md), [cxo.md](cxo.md), [cmo.md](cmo.md), [cgo.md](cgo.md), [cro.md](cro.md), [coo.md](coo.md), [cfo.md](cfo.md), [cio.md](cio.md), [chro.md](chro.md).

## The plan, in one paragraph

Ship a **free-tier, async-only "stretch party"** MVP (invite friends to complete a routine within a time window, see each other's completion status) using existing infrastructure, no new hires, and near-zero marketing spend. Treat it explicitly as a retention hypothesis test, not a committed feature launch: instrument a proper experiment, hold a 30-day checkpoint, and only then decide whether to invest further in live synced sessions, group monetization, or paid acquisition.

## Where every role agrees

- **Start small, prove the hypothesis before spending**: CPO (async before live sync), CTO (existing infra before new real-time backend), CFO (labor cost only, no infra/marketing spend yet), CHRO (no hire until scope is proven), CMO/CRO (no paid spend or paywall until validated) all converge on the same sequencing logic independently.
- **Tone risk is the biggest UX/brand risk, not technical risk**: CXO and CMO both flag that a social accountability feature can easily read as pressure/shame rather than encouragement; this is called out as the top design constraint, not a footnote.
- **Privacy is a launch blocker, not a follow-up**: CIO's consent-at-invite-accept and CTO's access-control concerns are both marked as must-fix-before-launch, and COO's execution plan places the privacy review on the critical path rather than in parallel-but-optional.

## Open questions to resolve before kickoff

1. **Does WeStretch currently have a friend/contact graph?** Flagged independently by CPO and CTO as a hidden dependency that changes the effort estimate; this needs an answer before the engineering timeline in [coo.md](coo.md) can be trusted.
2. **What confirms "success" at the 30-day checkpoint?** CGO recommends pre-registering the retention-lift threshold with CFO/CPO before launch; this hasn't been set yet and should be decided in the kickoff, not after seeing results.
3. **Actual current pricing tiers**: [cro.md](cro.md)'s recommendation (free-tier feature) assumes a free+paid split exists; confirm against real plan structure.

## Recommended next step

Kick off with a short session to answer the three open questions above, then greenlight the async MVP per [coo.md](coo.md)'s workstream plan. Do not scope live sync, paid marketing, or a new hire until the 30-day retention read is in.
