# BOOK: Routine Type 2

Source mockup: `Images/Screenshot 2026-08-19 151851.png` (screen 1, "Routine Type 2")
Applies [[Brand-Voice-Principles]].

Two distinct roles for this screen, both landing here:
1. **Manual path** — reached any time a user taps through the full wizard
   (First Screen → Second → pain/sport → standing/floor → Base Positions →
   Body Filter → Time) and arrives at a final review/edit sheet.
2. **Routine 7+ path (free users)** — from routine 7 onward, `First
   Screen` routes here directly instead of showing the step-by-step
   wizard at all (see [[First Screen]] chapter `routines_completed >= 6`).

## Chapter: account_type != free (guest or pro — full access)
State: `account_type != "free"`

- Header: "Customize Your Routine"
- Fields (all editable): Routine Length (`routine_length_minutes`),
  Routine Type (full type list, all tappable), Body Filter
  (`body_filter`, shows N/12 selected), Base Positions
  (`standing_poses_selected`/`floor_poses_selected`, shows N/8 each)
- Button: "Let's Go" (manual path) / "Let's stretch" (routine 7+ entry
  path — **confirm with Karen whether the label actually differs by path
  or is always the same**) → {Screen: Rating}

## Chapter: account_type == free
State: `account_type == "free"`

- Same fields as above, but:
  - Only the **Full Body** routine type card is tappable.
  - All other routine type cards are shown **blurred/greyed out**; tapping
    any of them → {Screen: paywall place holder}
  - Info banner at top: "Fully unlock every customization" — tapping it
    also → {Screen: paywall place holder}
  - The banner's offer includes a share-to-friend option: sharer receives
    coins, friend receives 60 days of Pro for $2. **Confirm this is the
    same promotion as the day-5 one-time offer in Storyline.md, or a
    second distinct mechanic** (see State-Variables.md open items).
- Button: "Let's Go" / "Let's stretch" → {Screen: Rating}

---

```json
{
  "screen": "Routine Type 2",
  "chapters": [
    {
      "condition": "account_type != 'free'",
      "header": "Customize Your Routine",
      "fields": ["routine_length_minutes", "body_filter", "standing_poses_selected", "floor_poses_selected", "routine_type (all options tappable)"],
      "button": {"label": "Let's Go / Let's stretch", "target": "Rating"}
    },
    {
      "condition": "account_type == 'free'",
      "header": "Customize Your Routine",
      "fields": ["routine_length_minutes", "body_filter", "standing_poses_selected", "floor_poses_selected", "routine_type (only Full Body tappable, others blurred)"],
      "banner": {"text": "Fully unlock every customization", "target": "paywall place holder"},
      "locked_type_tap_target": "paywall place holder",
      "button": {"label": "Let's Go / Let's stretch", "target": "Rating"}
    }
  ]
}
```
