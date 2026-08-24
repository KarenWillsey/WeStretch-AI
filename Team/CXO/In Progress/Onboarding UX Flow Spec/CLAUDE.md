# Onboarding UX Flow Spec — CLAUDE.md

Scope: turning Karen's wireframe mockups + dictated logic into a spec the
dev team and designer can build from — screen by screen, plus the
multi-session "drip-feed" education sequence that spans screens over time.
Read `Memory.md` alongside this file before adding or editing a screen.

## The model (Karen's "book" metaphor)

- **Book = Screen.** The screen name in the top-left corner of Karen's
  mockup image is the canonical ID used everywhere (filenames, JSON
  `screen` field, navigation targets).
- **Chapter = a state condition.** Which chapter renders is driven by user
  state (routines completed, account type: guest/free/pro, etc.) — this is
  the `if/else` branch in the JSON config that actually drives the app.
- **Headings inside a chapter = UI elements for that state**: Title,
  Subtitle, Button 1/2/3 (omit buttons that don't appear in that chapter).
- **`{Screen: X}` on a button = navigation target** — which book pressing
  that button opens next.

## Where things live

- `Images/` — Karen's uploaded wireframe mockups, one per screen, named to
  match the screen's label (e.g. `First Screen.png`, `Time.png`).
- `Screens/` — one Markdown file per screen ("book"): the dictated
  chapter/heading outline **plus** a JSON stub in the same file, per
  Karen's format decision (see Memory.md). Use `Screen-Template.md` as the
  starting structure for each new one.
- `Storyline.md` — the separate multi-session "drip-feed" education
  sequence (e.g. chapter 2 of the post-workout education only unlocks
  after routine 2 **and** every step in chapter 1 was completed). This
  stays out of individual screen books and instead references screens by
  name plus the gating condition, per Karen's format decision.
- `Onboarding-Flow.html` — the presentation-layer artifact: a clickable,
  self-contained walkthrough built from everything in `Screens/` and
  `Storyline.md`, published to claude.ai. Regenerate it (don't hand-edit)
  after any book changes — see Memory.md decision 5 for how it was built.
- `State-Variables.md` — the master list of variables any screen's chapter
  condition or the storyline's gates are allowed to reference (e.g.
  `routines_completed`, `account_type`). Check/extend this before inventing
  a new condition variable in a screen or in `Storyline.md`, so conditions
  stay consistent across the whole spec instead of drifting screen to
  screen.

## Workflow

1. Karen uploads wireframes to `Images/` (batch, per her stated workflow
   preference — see Memory.md).
2. For each screen, Karen dictates the chapters/headings; draft the
   Markdown book + JSON stub into `Screens/<Screen Name>.md` immediately
   and confirm before moving to the next screen.
3. Cross-screen navigation targets (`{Screen: X}`) must resolve to another
   file in `Screens/` — flag any target that doesn't have a corresponding
   book yet as an open item rather than silently guessing its content.
4. Once the full set of screens for a flow is drafted, build/update
   `Storyline.md` for any sequence that gates across sessions, and offer a
   Mermaid flowchart per user type (guest/free/pro) if useful for spotting
   dead ends — this was left optional, not automatic, per Karen's format
   choice.

## Memory

`Memory.md` in this folder holds durable decisions specific to this project
(format choices, naming conventions, calibrated state variables). See the
root `CLAUDE.md` "Memory" section for the full model.
