# BOOK: Time

Source mockup: `Images/Screenshot 2026-08-19 151837.png` (screen 5, "time")
Applies [[Brand-Voice-Principles]].

New state variable this book introduces: `custom_length_minutes` (integer
or null) — set by the `Minutes` screen, read back here to relabel button 3.

---

## Chapter: custom_length_minutes == null (default)
State: `custom_length_minutes == null`

- Title: "How long would you like your routine to be?"
- Subtitle: "I build you a unique routine each time. You can choose from 3 to 60 minutes."
- Button 1 "5 Minutes" → {Screen: Rating} (sets `routine_length_minutes = 5`)
- Button 2 "10 Minutes" → {Screen: Rating} (sets `routine_length_minutes = 10`)
- Button 3 "Custom Length" → {Screen: Minutes}

## Chapter: custom_length_minutes != null (returning from Minutes screen)
State: `custom_length_minutes != null`

- Title: "How long would you like your routine to be?"
- Subtitle: "I build you a unique routine each time. You can choose from 3 to 60 minutes."
- Button 1 "5 Minutes" → {Screen: Rating} (sets `routine_length_minutes = 5`)
- Button 2 "10 Minutes" → {Screen: Rating} (sets `routine_length_minutes = 10`)
- Button 3 "{custom_length_minutes} Minutes" → {Screen: Rating} (sets `routine_length_minutes = custom_length_minutes`) — label replaces "Custom Length" with the number chosen on the `Minutes` screen

All three buttons on both chapters route to the same destination
(`Rating`); only the label and the value written to `routine_length_minutes`
differ.

---

```json
{
  "screen": "Time",
  "chapters": [
    {
      "condition": "custom_length_minutes == null",
      "title": "How long would you like your routine to be?",
      "subtitle": "I build you a unique routine each time. You can choose from 3 to 60 minutes.",
      "buttons": [
        {"label": "5 Minutes", "target": "Rating", "sets": {"routine_length_minutes": 5}},
        {"label": "10 Minutes", "target": "Rating", "sets": {"routine_length_minutes": 10}},
        {"label": "Custom Length", "target": "Minutes"}
      ]
    },
    {
      "condition": "custom_length_minutes != null",
      "title": "How long would you like your routine to be?",
      "subtitle": "I build you a unique routine each time. You can choose from 3 to 60 minutes.",
      "buttons": [
        {"label": "5 Minutes", "target": "Rating", "sets": {"routine_length_minutes": 5}},
        {"label": "10 Minutes", "target": "Rating", "sets": {"routine_length_minutes": 10}},
        {"label": "{custom_length_minutes} Minutes", "target": "Rating", "sets": {"routine_length_minutes": "custom_length_minutes"}}
      ]
    }
  ]
}
```
