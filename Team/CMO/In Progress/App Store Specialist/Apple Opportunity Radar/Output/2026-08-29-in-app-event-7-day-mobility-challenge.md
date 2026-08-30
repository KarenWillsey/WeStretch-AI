# In-App Event Draft: "7-Day Mobility Challenge"

Addresses backlog item: "Launch an App Store In-App Event fitness challenge
(e.g. "7-Day Mobility Challenge")."
Date: 2026-08-29 (scheduled nightly run)

Status: **draft for review — not submitted to Apple.** This skill has no
App Store Connect access and never takes live action against Apple.

---

## 1. Event basics

| Field | Value |
|---|---|
| Event type (badge) | **Challenge** — correct type per Knowledge Base for a fitness-challenge event (not Competition, since there's no leaderboard/ranking; not Live Event/Premiere/New Season/Special Event/Major Update). |
| Duration | 7 days (well within Apple's 31-day max). |
| Promotion window | Can go live in App Store Connect up to 14 days before the event start date — recommend submitting ~10 days ahead to leave buffer for Apple review + any rejection/resubmit cycle. |
| Suggested start day | A Monday, so the 7 days line up with a calendar week (helps the "Day 1 of 7" framing feel natural). Exact date is Karen/Manager's call — not picked here. |

## 2. Metadata draft (character-limit checked)

**Event name** (max 30 chars): **"7-Day Mobility Challenge"** — 24 characters.
Not a call-to-action, no punctuation/caps issues, no pricing or superlative claims.

**Short description** (max 50 chars): **"Stretch daily for 7 days. Feel the difference."** — 46 characters.

**Long description** (max 120 chars) — two options, pick one:

- Option A (88 chars): "A physio-informed 7-day stretch plan. One guided session a day, led step-by-step by Ada."
- Option B (88 chars): "Seven days, one guided stretch a day. Physio-informed, step-by-step, paced to your body."

Recommend **Option B** — leads with the two Strategic Thesis "words we own"
(physio-informed, step-by-step) and names Ada implicitly through "guided,"
without the name-drop feeling forced in a tight 88 characters.

### Compliance check against Apple's event-metadata restrictions

- [x] No specific prices mentioned.
- [x] No unverifiable claims ("best," "#1," etc.) — matches the Strategic
      Thesis honesty guardrail: we prove the process (physio-informed,
      guided, daily), not an outcome we haven't earned the right to claim.
- [x] Event name is not a call-to-action.
- [x] No all-caps or excessive punctuation.
- [ ] No text/logos in event media, no borders/gradients — **applies to the
      artwork, not this metadata; flagged in section 3 below for whoever
      builds the image.**

## 3. Event experience concept (what a user actually gets)

Each of the 7 days unlocks one guided WeStretch session themed around daily
mobility, not a generic timer-based stretch list:

- **Day 1–2:** Gentle full-body mobility, physio-informed baseline movement.
- **Day 3–4:** Targeted stiffness relief (the areas WeStretch users most
  commonly flag: neck/shoulders, low back, hips).
- **Day 5–6:** Building range of motion, still paced to the user's own
  history, not a fixed template.
- **Day 7:** A wrap-up session + a simple in-app prompt reflecting on how
  the week felt (no outcome claims made *for* the user — the reflection is
  their own, which keeps this honest per the Strategic Thesis).

Every day is guided by Ada (continuous animated demonstration, not a static
pose with a countdown) and adapts to the user's own body/history, consistent
with "Uniquely Yours" — this is explicitly **not** a fixed 7-day template
handed to everyone identically; the *day themes* are fixed, but each day's
actual stretch selection still runs through WeStretch's normal
personalization.

This is a content/product-side decision (how "Day N unlocks" is actually
built and tracked in-app) — this draft assumes it's buildable with existing
routine-personalization logic, but confirming that is a product/engineering
question, not something this skill can verify.

## 4. Asset requirements — route to existing pipelines, not built here

Per this skill's own rules, asset-shaped work routes to the existing CMO
sub-projects rather than being generated inline:

- **Event card artwork** (Apple auto-applies borders/gradients, so submit
  clean art with no text/logo baked in, no pre-added border/gradient) →
  `Team/CMO/In Progress/App Store Specialist/App Store Image Creation/`.
  Suggested visual: Ada mid-stretch, matching the existing screenshot
  brand look, day-count implied rather than stated in-image (Apple applies
  its own "Day X" event-progress UI on top, so don't duplicate it in the art).
- **Any supporting headline/subtitle variants for promotion** (social,
  email teasers linking to the event) → `App Store Image Text Copywriting/`
  for App Store-side assets, or the CMO email-funnel work for outbound.
- Apple's exact required image dimensions/formats for event cards aren't
  in the Knowledge Base yet — confirm current specs in App Store Connect
  when building the artwork brief (Apple's own event-creation flow states
  the required sizes at submission time).

## 5. Open items for Karen/Manager review

1. Confirm exact start date (recommend a Monday; see section 1).
2. Confirm the "Day N unlocks a themed session" mechanic is actually
   buildable with current app logic before submitting the event — this
   draft assumes yes but can't verify.
3. Pick long-description Option A vs B (or request another pass).
4. Hand off artwork brief (section 4) to App Store Image Creation once the
   above is confirmed.
5. Submit in App Store Connect once approved — 14-day promotion window
   means submission should happen ~10+ days before the chosen start date.
