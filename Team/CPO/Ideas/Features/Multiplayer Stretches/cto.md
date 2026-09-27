# CTO; Tech Architecture Review: Multiplayer Stretching

_Skill applied: `Team/CTO/skills/tech-architecture-review`_

## Current state

WeStretch's architecture today is assumed single-player: routines, completions, and streaks are scoped to one user with no cross-user data model, no friend graph, and no real-time messaging layer (per the CPO doc's open dependency question). This review assumes that baseline; confirm against actual backend before committing to the recommendation below.

## Options

1. **Async-only, built on existing infra**: model a "session" as a shared record referenced by multiple user IDs, invites sent via existing push notification system, completion status polled/pushed on normal request cadence. No new real-time infrastructure required.
   - Cost: Low. Complexity: Low. Time-to-ship: Weeks, not months.
2. **Live sync via managed real-time backend** (e.g., a hosted WebSocket/pub-sub service), a session room broadcasts routine timer state and participant status to all joined clients in real time.
   - Cost: Medium (new vendor + ongoing usage-based cost). Complexity: Medium-High (new failure modes: reconnect handling, drift between client timers, room lifecycle). Time-to-ship: 1-2 months.
3. **Live sync built in-house** (self-hosted WebSocket server), same capability as (2) without a managed vendor.
   - Cost: High (infra to build and operate). Complexity: High. Time-to-ship: 2-3+ months. Not recommended at current team size.

## Recommendation

Ship **Option 1 (async-only)** first, matching the CPO's MVP scope. It requires no new infrastructure category, keeps operational surface area flat, and directly tests the core retention hypothesis. If the data supports moving to live sessions, revisit with **Option 2**; a managed real-time backend is the right call for a small team; building and operating our own WebSocket infra (Option 3) is not proportionate to our stage.

## Risks

- **Friend graph as a hidden dependency**: if WeStretch has no existing concept of "friends/contacts," that's a prerequisite feature, not a detail; it changes the effort estimate for even the async MVP. Confirm before scoping.
- **Data exposure between users**: any shared session record now holds cross-user references; access control needs explicit review (see [cio.md](cio.md)) so User A can never pull User B's data outside the shared session context.
- **Vendor lock-in (Option 2, if/when pursued)**: choose a real-time provider with a reasonable migration path; avoid one that requires deep client-side coupling.
