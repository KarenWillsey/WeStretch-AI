# BOOK: Streak Saver Offer

No source mockup and minimal dictated content; Karen referenced this as
"an existing sheet I didn't give you." Drafted as a stub so the trigger
condition isn't lost; needs real copy from Karen or a designer before
it's usable. Applies [[Brand-Voice-Principles]].

## Chapter: default
State: `streak_count reached >= 5, then a day was missed, user has now returned`
(Karen's example: 5-day streak, misses day 6, returns day 7)

- Content: offers the user their "streak freeze" / streak saver to
  preserve the streak despite the missed day. **Exact copy not dictated, placeholder only.**
- Likely uses `coins_earned_today` or accumulated coins to "buy" the save,
  per the Coins explainer drip sheet ("coins can be used to buy a streak
  saver"); **confirm this is how the streak saver is actually spent.**

---

```json
{
  "screen": "Streak Saver Offer",
  "status": "stub, trigger condition only, no copy",
  "chapters": [
    {
      "condition": "streak_count >= 5 (prior) AND missed a day AND user returned",
      "title": "not dictated",
      "body": "offers to use a streak saver / streak freeze",
      "buttons": [
        {"label": "not dictated", "target": "not dictated"}
      ]
    }
  ]
}
```
