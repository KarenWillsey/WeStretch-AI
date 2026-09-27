# BOOK: Leaderboard Explainer

No source mockup: not among the uploaded wireframes. Content fully
dictated by Karen; formalized as its own book here (was previously only
captured inline in `Storyline.md` step S2). Applies [[Brand-Voice-Principles]].

Second sheet of the drip funnel: one-page explanation shown right before
the user's first visit to the real leaderboard.

## Chapter: default
State: (none, shown before first leaderboard visit; **confirm with Karen**
whether it repeats every session or only the first time, same open
question as `Routine Recap`)

- Title: "Leaderboards are to help you motivate and show up every day."
- Body: "It's based on how many minutes you stretch in a day. Set a little
  personal goal to move up, or stay in the top league."
- Button "Take me to the leaderboard" → {Screen: Leaderboard (real)}
  (existing live leaderboard, out of scope for this spec, see
  Screen-Inventory.md row #28)

---

```json
{
  "screen": "Leaderboard Explainer",
  "chapters": [
    {
      "condition": "before first leaderboard visit",
      "title": "Leaderboards are to help you motivate and show up every day.",
      "body": "It's based on how many minutes you stretch in a day. Set a little personal goal to move up, or stay in the top league.",
      "buttons": [
        {"label": "Take me to the leaderboard", "target": "Leaderboard (real)"}
      ]
    }
  ]
}
```
