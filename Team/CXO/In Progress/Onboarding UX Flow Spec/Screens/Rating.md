# BOOK: Rating

Source mockup: `Images/Screenshot 2026-08-19 151851.png` (screen 2, "Rating")
Applies [[Brand-Voice-Principles]].

No conditional chapters dictated yet: single chapter, reached from every
`Time` button and from `First Screen`'s "Last routine settings" button.

## Chapter: default
State: (none; always shown before a routine starts)

- Title: "Well, your routine is being custom built for you…"
- Subtitle: "Let's check in on how you are feeling today."
- Slider: "Body Stiffness", range 0–10 → sets `stiffness_before`
  - 0 label: "Can't get any stiffer" / "Stiff as a board"
  - 5 label: "Moveable"
  - 10 label: "Feeling good"
  - **Confirm labels**: Karen's dictation had "the tin on the slider says feeling good," read here as "10" (voice-transcription artifact); double-check against the actual mockup/Figma before finalizing.
- Interacting with the slider → {Screen: Do routine}

---

```json
{
  "screen": "Rating",
  "chapters": [
    {
      "condition": "always",
      "title": "Well, your routine is being custom built for you…",
      "subtitle": "Let's check in on how you are feeling today.",
      "slider": {
        "label": "Body Stiffness",
        "variable": "stiffness_before",
        "min": 0,
        "max": 10,
        "min_label": "Can't get any stiffer / Stiff as a board",
        "mid_label": "Moveable",
        "max_label": "Feeling good"
      },
      "on_interact_target": "Do routine"
    }
  ]
}
```
