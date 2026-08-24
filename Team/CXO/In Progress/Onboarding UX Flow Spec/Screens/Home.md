# BOOK: Home

No source mockup — not among the uploaded wireframes. Partial content
only: Karen described specific elements but never the full screen.
**This book is incomplete — needs a real mockup/design pass**, drafted
here only so the elements she did specify aren't lost, and because Goal 1
(closing the leaderboard dead-end) depends on this screen existing.
Applies [[Brand-Voice-Principles]].

## Known elements (dictated, not a full chapter/JSON spec)

- **Summary cards**: described as "the full picture" of the user's
  progress — this is the whole reason Goal 1 wants users routed here.
  **No content specified** — needs a design pass.
- **Guest banner** (top of screen, guest users only): "You are a guest
  user. Sign up anytime to save your history." Tapping it → {Screen: Sign Up}
- **Top widget** (tap target): opens a calendar view of stretch history
  (which days the user stretched).
- **Persistent "Turn Pro" banner** (free users): tapping it → {Screen: paywall place holder}
- **Bottom nav**: confirmed to include at minimum Leaderboard, Notifications, Settings.
  **Full nav list not specified** — likely also includes Home itself and
  possibly a Progress/History tab; confirm with Karen before finalizing.

## Proposed fix for Goal 1 (leaderboard dead-end) — NOT decided, flag for review

Karen's dictated funnel currently ends at: `Leaderboard Explainer` →
`Leaderboard (real)`, with Home reachable only via manual bottom-nav
navigation from there — which is the dead-end Goal 1 exists to fix. Two
candidate directions, neither chosen yet:

1. **Change the funnel's endpoint** — after the user has viewed/explored
   `Leaderboard (real)`, auto-advance to `Home` (e.g. after a dwell time,
   or on a clear "Continue" action) instead of leaving them stranded on
   the leaderboard. Leaderboard stays reachable any time via bottom nav,
   same as today — only the *first-session funnel's* landing spot changes.
2. **Add an explicit CTA on the real leaderboard** inviting the user back
   to Home (e.g. "See your full summary" button) — lower-risk since it
   doesn't require an auto-navigation timer, but relies on the user
   tapping it.

Since the real leaderboard is out of scope for this spec (see
Screen-Inventory.md #28), whichever direction is chosen will need
sign-off/implementation outside this project's `Screens/` books — flagging
the decision here so it doesn't get lost.

---

```json
{
  "screen": "Home",
  "status": "incomplete — elements only, no full chapter spec",
  "elements": {
    "summary_cards": {"content": "not specified"},
    "guest_banner": {"condition": "account_type == 'guest'", "text": "You are a guest user. Sign up anytime to save your history.", "target": "Sign Up"},
    "history_widget": {"action": "open_calendar_view"},
    "turn_pro_banner": {"condition": "account_type == 'free'", "target": "paywall place holder"},
    "bottom_nav": ["Leaderboard", "Notifications", "Settings", "confirm full list"]
  }
}
```
