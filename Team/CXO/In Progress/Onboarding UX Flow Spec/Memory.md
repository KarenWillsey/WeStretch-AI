# Onboarding UX Flow Spec — Memory

Durable decisions for this project only. See `Team/CXO/Memory.md` for
role-level memory and the root `Memory.md` for cross-role facts.

## Spec format (project)

Established 2026-08-19, when Karen was struggling to communicate a wireframe
based user-flow to engineering/design:

1. **Each screen ("book") is documented as Markdown outline + JSON stub in
   the same file**, not outline-only and not a full separate flowchart by
   default.
   - **Why:** Karen wanted the dictated "if this, then do that" logic to be
     human-readable for her/the designer AND directly usable by engineers
     without a translation step — she chose this over outline-only (too
     informal for eng) and over outline+JSON+Mermaid-always (extra
     diagramming work not needed for every screen).
   - **How to apply:** Every file in `Screens/` follows
     `Screen-Template.md`. A Mermaid flowchart can still be added per user
     type when it's useful for spotting dead ends, but it's optional, not
     a default part of every screen's file.

2. **The multi-session "drip-feed" education sequence lives in its own
   `Storyline.md`, not folded into each screen's chapter conditions.**
   - **Why:** Karen's example (chapter 2 of post-workout education unlocks
     only after routine 2 *and* every step of chapter 1 was completed)
     spans multiple screens and multiple sessions — gating logic like that
     would otherwise get duplicated across every screen it touches.
   - **How to apply:** A screen's own `Screens/<name>.md` file should stay
     scoped to that screen's own state-driven chapters. Any condition that
     references "has the user already seen/completed a different screen or
     sequence step" belongs in `Storyline.md`, which references screens by
     name.

3. **Project home is `Team/CXO/In Progress/`, not CPO or a cross-role
   `Features/` folder.**
   - **Why:** Karen confirmed this is fundamentally a UX design review /
     customer journey artifact (CXO's mandate), not primarily a roadmap
     doc.
   - **How to apply:** If other roles end up needing to attach their own
     docs to this same flow (e.g. CMO reviewing copy, CRO reviewing
     paywall logic on pro-user branches), follow the root `CLAUDE.md`
     cross-functional pattern rather than moving this whole project.

4. **Workflow: Karen uploads all wireframe images first, then dictates
   chapters screen by screen**, rather than one screen fully at a time.
   - **Why:** Karen's own stated preference, so screen names/order can be
     established up front from the images before dictation starts.
   - **How to apply:** Once images land in `Images/`, list out the screen
     names/order found in them and confirm with Karen before starting to
     draft `Screens/` files from dictation.

5. **Presentation layer: build an interactive clickable flow map (Artifact),
   separate from the git-tracked `Screens/*.md` source of truth.**
   - **Why:** Karen needs to walk the team through this live, and 23
     separate markdown files isn't presentable as-is; she confirmed she
     wants a real clickable-prototype feel (branches per user type),
     not a Gamma slide deck or diagrams-only.
   - **How to apply:** Don't build this artifact until the `Screens/`
     books have real content — build it once a meaningful chunk of the
     flow is drafted, not screen-by-screen. Load the `artifact-design`
     skill before building it, per the Artifact tool's own requirement.

6. **Global Goals locked 2026-08-19 (qualitative only, numeric targets
   TBD)** — see `Global-Goals.md`: (1) close the leaderboard dead-end by
   routing explored-leaderboard users to Home, (2) guest→account
   conversion, (3) free→pro paywall conversion, (4) drip-feed education
   actually gets engaged with, not just technically gated.
   - **Why:** Karen asked to be interviewed on this specifically so the
     finished spec could be checked against it, rather than goals being
     inferred after the fact.
   - **How to apply:** When each screen book or `Storyline.md` step is
     drafted, note which of these 4 goals it serves (or flag if none do).

7. **Mockup strategy: reuse real screenshots for the 23 already-designed
   screens; plain structural placeholders only for screens that don't
   exist yet (e.g. Home).**
   - **Why:** Karen wants team-facing mockups to "stick strictly to what
     is live in our app already" — the app is Unity with a 3D animated
     character, which no available tool here can faithfully regenerate.
     Fabricating AI-generated "Unity-style" art for undesigned screens and
     presenting it as accurate would misrepresent it as real.
   - **How to apply:** When building the clickable flow-map Artifact,
     embed the actual uploaded screenshots for existing screens. For new
     screens, use plain boxes/labels/button-position layouts in the
     existing color language, clearly marked as layout-only/not final art
     — never generate character/gym concept art and let it pass as
     production-accurate.
   - Karen wants a Figma MCP connector added for real component access;
     no tool in this session can add a connector (requires her account
     auth) — she was pointed at Settings → Connectors (matching how
     Asana/Gamma/Mailchimp/Microsoft 365 got connected) or Figma's own
     Dev Mode MCP Server as a custom connector. Once connected, prefer it
     over screenshots for any new-screen mockup work.

8. **Brand voice/positioning rules live in their own `Brand-Voice-Principles.md`,
   referenced by every book instead of restated per screen.**
   - **Why:** Karen dictated 5 standing rules (intelligent/personalized,
     Ada advancing the user, daily-stretching motivation, invested-progress
     FOMO toward Pro, ego-forward copy) as applying "everywhere," not to
     one screen.
   - **How to apply:** Every new `Screens/*.md` book and every
     `Storyline.md` sheet should note `Applies Brand-Voice-Principles` and
     draft copy consistent with it, rather than re-deriving tone per screen.

9. **Structural insight: free-user flow collapses to one screen
   (`Routine Type 2`) starting at routine 7.** Routines 1–6 use the full
   step-by-step wizard (First Screen → Second → pain/sport →
   standing/floor → Base Positions → Body Filter → Time); routine 7
   onward, `First Screen` routes straight into `Routine Type 2` instead.
   - **Why:** Karen's own dictated structure — this is a big enough shift
     in the flow's shape that it's worth remembering explicitly rather
     than re-deriving it from scattered chapter conditions later.
   - **How to apply:** Any change to the wizard screens (Second, pain,
     sport, standing, floor, Base Positions, Body Filter, Time) should
     consider whether `Routine Type 2` needs the equivalent field, since
     it's the wizard's replacement for returning free users.

## Open items (project)

- Master list of state variables is still growing — see
  `State-Variables.md` open items (body_filter's full 12-part list,
  whether pain/stiffness/pace are 3 variables or 1, exact `routine_id`
  mechanism).
- Full screen inventory (23 screens across 4 uploaded images) is captured
  in `Screen-Inventory.md`, none drafted into `Screens/` yet. Two screens
  (positions 9 and 10, the pose-summary and body-filter sheets in the
  second image) have no visible top-left label in the mockup — provisionally
  named "Base Positions" and "Body Filter" from their in-app headers;
  confirm with Karen before treating those as final.
- Karen's dictated live-app flow mentions a "post-routine talk" from the
  animated character and a drip-feed screen with an undefined cadence
  ("radus" — likely a transcription artifact for the actual word) — both
  need clarification before `Storyline.md` can be drafted for real. See
  `Global-Goals.md` "Open items."
- Home screen (with summary cards) referenced as the fix-target for Goal 1
  is not among the uploaded wireframes yet — will need its own mockup/book.
