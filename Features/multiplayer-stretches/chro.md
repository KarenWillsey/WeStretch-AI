# CHRO — Hiring Plan: Multiplayer Stretching

_Skill applied: `CHRO/skills/hiring-plan`_

## Role justification

**No new hire is justified for the async MVP scope.** Per [cto.md](cto.md), Option 1 (async-only, built on existing infra) requires no new technical capability the current engineering team shouldn't already have — it's a data-model and notification feature, not a new discipline.

A hiring need would only emerge if the roadmap advances to **live synced sessions** (per [cpo.md](cpo.md)'s Option 3 / [cto.md](cto.md)'s Option 2), which requires real-time systems experience (WebSocket/pub-sub, connection state, latency handling) that the team may not currently have.

## Role definition (contingent, not immediate)

If live sync is greenlit after the 30-day retention checkpoint ([coo.md](coo.md)):
- **Role**: Backend engineer with real-time systems experience.
- **Scope**: owns the managed real-time backend integration (per CTO's recommended Option 2), session lifecycle, and reconnect/drift handling.
- **Fit in org**: reports into existing engineering team under CTO; not a new team, just a new skill on the existing team.

## Sequencing

Do not open this requisition now. Sequence: (1) ship async MVP with current team, (2) read the CGO retention experiment, (3) only if live sync is approved, open the role — timed so the hire isn't sitting idle waiting for a scope decision that hasn't been made yet.

## Sourcing/budget considerations

If/when triggered: a contractor engagement for the initial real-time integration may be more capital-efficient than a full-time hire, given this is a single well-scoped capability rather than an ongoing need — revisit full-time vs. contract once the live-sync scope is actually defined. No budget should be reserved for this until the contingency triggers, per [cfo.md](cfo.md).
