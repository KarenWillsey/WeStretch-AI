# CPO — Roadmap Prioritization: Multiplayer Stretching

_Skill applied: `CPO/skills/roadmap-prioritization`_

## Scoring

| Candidate scope | Impact | Effort | Confidence | Goal it serves |
|---|---|---|---|---|
| Async "stretch party" (invite friends, shared completion view) | High | M | Medium | Retention, D7/D30 |
| Live synced session (real-time room, in-step routine) | High | L | Low | Retention, differentiation |
| Leaderboards/streak-sharing only (no live interaction) | Medium | S | High | Engagement, low-risk test |

Async is the highest-leverage first cut: most of the retention benefit (social accountability, visible streaks) with a fraction of the engineering cost of real-time sync. Live sessions are a stronger differentiator but effort and risk are meaningfully higher, and we don't yet have evidence users want *synchronous* stretching vs. just knowing a friend did it too.

## Ranked roadmap

1. **Async stretch party (MVP)** — invite up to 4 friends to a shared routine within a 24h window, shared completion/streak view. Justification: cheapest path to test the core hypothesis (does social visibility improve retention) before investing in real-time infra.
2. **Group streaks & nudges** — if (1) lands, add group streak mechanics and "your friend hasn't stretched today" nudges. Justification: compounds retention effect once the base mechanic is validated.
3. **Live synced session** — only pursue if (1) shows a clear retention lift and qualitative feedback specifically asks for "doing it together in real time." Justification: highest cost, should be earned by data, not assumed.

## Cut list (for now)

- **Video/camera presence in live sessions** — cut. Adds privacy complexity and infra cost disproportionate to unproven demand; revisit only after live sync itself is validated.
- **Public/stranger matchmaking** (stretch with a random user) — cut. Trust/safety and moderation overhead is high for a feature whose core value (accountability) works better with people you already know.

## Dependencies

- Async MVP needs: friend/contact graph (does WeStretch have one today? if not, this is a blocking dependency — see [cto.md](cto.md)), push notification infra for invites, and a lightweight "session" data model.
- Live sync (if pursued later) needs real-time infra decision — see [cto.md](cto.md).
- Data sharing between users (streaks, completion) needs a privacy/consent pass — see [cio.md](cio.md).
