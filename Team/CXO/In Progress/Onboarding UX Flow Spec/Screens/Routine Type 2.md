# BOOK: Routine Type 2

Source mockup: `Images/Screenshot 2026-08-19 151851.png` (screen 1, "Routine Type 2")
Applies [[Brand-Voice-Principles]].

Two distinct roles for this screen, both landing here:
1. **Manual path**: reached any time a user taps through the full wizard
   (First Screen → Second → pain/sport → standing/floor → Base Positions →
   Body Filter → Time) and arrives at a final review/edit sheet.
2. **Routine 7+ path (free users)**: from routine 7 onward, `First
   Screen` routes here directly instead of showing the step-by-step
   wizard at all (see [[First Screen]] chapter `routines_completed >= 6`).

## Chapter: account_type != free (guest or pro, full access)
State: `account_type != "free"`

- Header: "Customize Your Routine"
- Fields (all editable): Routine Length (`routine_length_minutes`),
  Routine Type (full type list, all tappable), Body Filter
  (`body_filter`, shows N/12 selected), Base Positions
  (`standing_poses_selected`/`floor_poses_selected`, shows N/8 each)
- Button: "Let's Go" (manual path) / "Let's stretch" (routine 7+ entry
  path; **confirm with Karen whether the label actually differs by path
  or is always the same**) → {Screen: Rating}

## Chapter: account_type == free AND trial_routines_remaining > 0
State: `account_type == "free" AND trial_routines_remaining > 0`

Free users still inside their trial budget (typically routines 7–13) get
**full access**, same as the non-free chapter; nothing is locked yet.
This chapter was missing in the first draft and contradicted the
`First Screen` countdown chapters ("10 routines left" etc.), which assume
full customize access continues until the budget actually runs out.
Fixed 2026-08-21.

- Same fields/access as the `account_type != free` chapter above, all
  routine types tappable.
- Optional reminder banner: "{trial_routines_remaining} routines left" (no lock, no paywall tap).
- Button: "Let's Go" / "Let's stretch" → {Screen: Rating}

## Chapter: account_type == free AND trial_routines_remaining <= 0
State: `account_type == "free" AND trial_routines_remaining <= 0`

This is the real hard-paywall state (routine 14+ in the typical budget),
the locked view described in the original draft belongs here, not to
every free user unconditionally.

- Only the **Full Body** routine type card is tappable.
- All other routine type cards are shown **blurred/greyed out**; tapping
  any of them → {Screen: paywall place holder}
- Info banner at top: "Fully unlock every customization", tapping it
  also → {Screen: paywall place holder}
- The banner's offer includes a share-to-friend option: sharer receives
  coins, friend receives 60 days of Pro for $2. **Confirmed 2026-08-20:
  this is the same offer as Storyline.md's day-5/routine-5 one-time
  offer**; shown plain first; the share-with-a-friend variant is
  introduced later in the drip sequence, not bundled with its first
  appearance.
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
      "condition": "account_type == 'free' && trial_routines_remaining > 0",
      "header": "Customize Your Routine",
      "fields": ["routine_length_minutes", "body_filter", "standing_poses_selected", "floor_poses_selected", "routine_type (all options tappable)"],
      "banner": {"text": "{trial_routines_remaining} routines left", "target": null},
      "button": {"label": "Let's Go / Let's stretch", "target": "Rating"}
    },
    {
      "condition": "account_type == 'free' && trial_routines_remaining <= 0",
      "header": "Customize Your Routine",
      "fields": ["routine_length_minutes", "body_filter", "standing_poses_selected", "floor_poses_selected", "routine_type (only Full Body tappable, others blurred)"],
      "banner": {"text": "Fully unlock every customization", "target": "paywall place holder"},
      "locked_type_tap_target": "paywall place holder",
      "button": {"label": "Let's Go / Let's stretch", "target": "Rating"}
    }
  ]
}
```
