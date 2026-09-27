# BOOK: Set Your Goal

No source mockup: not among the uploaded wireframes. Applies
[[Brand-Voice-Principles]]. Reached after the free-user Pro-trial
explainer around routine 6–7 (see `Storyline.md`); exact entry trigger
still TBD.

## Chapter: first visit
State: (first time reaching this screen)

- Explainer copy: "Set your default routine length here. But remember to
  come back every few weeks and add a minute or two, or 10, if you're
  cheeky." **(Karen's wording, lightly cleaned up)**
- Field: default routine length → sets `default_routine_length`
- Toggle: "Everyday Stretcher" vs. "Weekday Stretcher" → sets `daily_goal_type`
  - `everyday_stretcher` is the option tied to streaks.
- **Not specified**: what happens on save (target screen), whether this
  toggle can be changed later from Settings, and what "Weekday Stretcher"
  changes functionally beyond opting out of streak tracking.

---

```json
{
  "screen": "Set Your Goal",
  "status": "incomplete, first-visit copy only, no navigation target specified",
  "chapters": [
    {
      "condition": "first visit",
      "body": "Set your default routine length here. But remember to come back every few weeks and add a minute or two, or 10, if you're cheeky.",
      "fields": [
        {"name": "default_routine_length", "type": "integer_minutes"},
        {"name": "daily_goal_type", "type": "enum", "options": ["everyday_stretcher", "weekday_stretcher"], "note": "everyday_stretcher ties to streaks"}
      ]
    }
  ]
}
```
