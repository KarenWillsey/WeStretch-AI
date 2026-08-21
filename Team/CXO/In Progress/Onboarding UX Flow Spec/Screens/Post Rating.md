# BOOK: Post Rating

Source mockup: `Images/Screenshot 2026-08-19 151851.png` (screen 4, "Post Rating")
Applies [[Brand-Voice-Principles]]. This is the "post-routine talk" —
Karen confirmed the animated character's check-in happens on this screen,
not a separate undrawn one.

## Chapter: default
State: (none — always shown immediately after `Do routine` finishes)

- Title: "Congratulations! Let's check in on how you feel"
- Subtitle: "I would like to work you up to 15 minutes a day for amazing results."
- Slider: "Body Stiffness" (same slider as `Rating`) → sets `stiffness_after`
- On interact:
  - if `badges_earned` is non-empty → {Screen: Badges}
  - else → {Screen: Streak Progress} (skip Badges entirely when none were earned — **confirm with Karen**)

Downstream (not part of this book, see [[Storyline]] for the full sequence
and [[State-Variables]] for `stiffness_before`/`stiffness_after`): Badges
(if any) → Streak Progress → Collect coins → drip sheet(s) → Leaderboard
Explainer → Leaderboard → Home.

---

```json
{
  "screen": "Post Rating",
  "chapters": [
    {
      "condition": "always",
      "title": "Congratulations! Let's check in on how you feel",
      "subtitle": "I would like to work you up to 15 minutes a day for amazing results.",
      "slider": {
        "label": "Body Stiffness",
        "variable": "stiffness_after",
        "min": 0,
        "max": 10
      },
      "on_interact_target_if": [
        {"condition": "badges_earned not empty", "target": "Badges"},
        {"condition": "else", "target": "Streak Progress"}
      ]
    }
  ]
}
```
