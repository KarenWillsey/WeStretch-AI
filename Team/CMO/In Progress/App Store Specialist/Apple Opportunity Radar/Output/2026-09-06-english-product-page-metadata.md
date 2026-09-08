# English App Store product page metadata

Addresses backlog item: "Draft English App Store product page metadata
(name <=30 chars, subtitle <=30 chars, keyword field <=100 chars,
promotional text <=170 chars, long-form description), prerequisite for
localizing product page metadata into French and Spanish."

Date: 2026-09-06 (scheduled nightly run)

## Read this first: the item's premise was partly wrong

The item was seeded on 2026-08-26 with the finding that "no English app
name, subtitle, keyword-field content, or long-form description exists
anywhere in the repo." That was true of the repo, and it is still true.
It is not true of the App Store.

**WeStretch has a live, fully written English product page right now**
(app ID 1458915362, "WeStretch: Custom Stretches", version 8.1.32,
released 2026-09-03, 4.5 stars from 53 ratings). So this run is not a
blank-page draft. It does two things instead:

1. Captures the live English metadata into the repo, so it exists as a
   source of record and the French/Spanish localization item has
   something real to work from.
2. Proposes a revised version, field by field, with the reasons, so
   Karen can approve, reject, or part-approve each field on its own.

Nothing was changed on Apple's side. This is a draft only.

**How the baseline was read (no App Store Connect access needed):**
public iTunes Lookup API (`itunes.apple.com/lookup?id=1458915362`) for
the name and description, and the public storefront HTML for the
subtitle. Both fetched live today. Two fields are **not** publicly
readable and are still unknown: the **keyword field** and
**promotional text**. See "Needs App Store Connect access" below.

---

## 1. Live baseline, as of 2026-09-06 (verified)

| Field | Live value | Chars | Limit |
|---|---|---|---|
| App name | `WeStretch: Custom Stretches` | 27 | 30 |
| Subtitle | `Pain Relief,Stiffness,Mobility` | 30 | 30 |
| Keyword field | not publicly readable | ? | 100 |
| Promotional text | appears unset (the storefront shows the description with no promo block above it) | ? | 170 |
| Description | full text preserved in section 6 below | 2531 | 4000 |
| Primary category | Health & Fitness | | |
| Secondary category | Sports | | |
| Seller | We Bananas Software Inc. | | |
| Price | Free, with in-app purchases $0.99 to $69.99 | | |
| Minimum iOS | 15.2 | | |

**Side note that answers an open item elsewhere:** minimum iOS is
**15.2**, not 18. That is directly relevant to the 2026-09-03 backlog
output on deep-linked Custom Product Pages, which needed iOS 18+ and
could not confirm the deployment target. This is the shipping app's
declared minimum per Apple's own API, so deep-linked CPPs will not reach
the part of the install base below iOS 18. Recorded here; that checklist
should be updated with it.

---

## 2. App name (limit 30)

**Recommendation: keep `WeStretch: Custom Stretches` (27/30). Do not change it.**

It carries the brand plus two indexed terms ("custom", "stretches"), it
reads clearly, and it has ranking history. Renaming resets that history
for no clear gain. The old storefront URL slug still says
`westretch-the-stretching-app`, so the name has already been changed at
least twice; a third change is churn, not optimization.

If a change is ever wanted anyway, these fit the limit and were checked:

| Option | Chars |
|---|---|
| `WeStretch: Stretching Coach` | 27 |
| `WeStretch: Daily Stretching` | 27 |
| `WeStretch Stretch & Mobility` | 28 |

## 3. Subtitle (limit 30)

The live subtitle, `Pain Relief,Stiffness,Mobility`, is a keyword list
with the spaces stripped to fit. At exactly 30/30 it does index those
three terms, but it does no conversion work at all. A cold browser
scanning search results reads the name and the subtitle together, and
that pair currently says what the app is *about* without saying what
makes it different.

**Recommended: `Stretching for Pain & Mobility` (30/30)**

Reads as a phrase, keeps two of the three keywords, and moves "stiffness"
into the keyword field where it costs less. Alternatives, all within
limit:

| Option | Chars | Note |
|---|---|---|
| `Stretching for Pain & Mobility` | 30 | recommended, clearest to a cold browser |
| `Physio-Backed Pain & Mobility` | 29 | leads with the differentiator; "physio" is substantiated |
| `Daily Stretches for Stiffness` | 29 | narrower, habit framing |
| `Your Physio-Informed Routine` | 28 | most on-brand, weakest on search terms |

**This is a good A/B test rather than a guess.** The 2026-08-22 Product
Page Optimization plan already exists for the first three screenshots;
the subtitle is testable the same way. Recommend testing the recommended
subtitle against the live one rather than swapping it outright.

## 4. Keyword field (limit 100)

Not readable from outside, so this is a proposal, not a diff. Rules
applied, from the Knowledge Base "App Store Listing" section: commas with
no spaces, no repeats of terms already in the name or subtitle (Apple
indexes those separately), no plural of a word already present, no
competitor names, nothing irrelevant.

**If the recommended subtitle is adopted** (name and subtitle then cover:
westretch, custom, stretches, stretching, pain, mobility):

```
stiffness,flexibility,physiotherapy,posture,back,neck,hip,shoulder,knee,senior,warmup,limber,sore
```
97/100

**If the current subtitle is kept** (name and subtitle then cover:
westretch, custom, stretches, pain, relief, stiffness, mobility):

```
flexibility,physiotherapy,posture,back,neck,hip,shoulder,knee,senior,warmup,limber,sore,routine,age
```
99/100

**Deliberately excluded, and why:**

- **yoga**: high volume, but the Strategic Thesis is explicit that
  WeStretch is not a yoga app. Apple's rule against irrelevant keywords
  applies, and the traffic it would buy is the wrong intent.
- **splits**: in the app's old name, and a real search term, but far off
  the 50+ ICP. Optional, low priority.
- **arthritis, sciatica, rehab, physical therapy**: real search demand,
  but they pull the listing toward implied medical treatment. The
  Knowledge Base "Health and Fitness Claims" section warns against
  unsupported diagnosis and treatment framing, and the description
  already carries health-adjacent claims (section 6). Karen's call,
  flagged rather than silently used. "physiotherapy" is included because
  the physiotherapist partnership is a real, substantiable fact about how
  the content was built, not a treatment claim.

## 5. Promotional text (limit 170)

Appears unset today, which is a free lever going unused: promotional text
sits above the description, and **it can be changed without shipping an
app update**. Three drafts, ready to paste.

**A. Default / evergreen (156/170)**

```
Tell WeStretch how long you have, what you want to work on, and what to skip. It builds the routine, then Ada guides every move. New poses added this month.
```

Drop the last sentence in any month where no poses were added. Do not
leave a stale claim sitting there.

**B. In-App Event tie-in (147/170)**

```
New: the 7-Day Mobility Challenge. Seven short routines, built around your body and the time you have, guided step by step. Start any day you like.
```

Pairs with the 2026-08-29 In-App Event draft. Use only once that event is
actually live, and pull it down the day it ends.

**C. Problem-first (145/170)**

```
Stiff in the morning? Tell WeStretch what hurts and how many minutes you have. It builds a routine around it, and Ada shows you every move, live.
```

Recommended cadence: A as the resting state, B during an event, C as the
seasonal swap for January, when fitness-resolution search peaks.

## 6. Description (limit 4000)

The live description is good. It has a real hook, a clear mechanism, and
a genuine differentiator. It is not being replaced wholesale, and the
revision below reuses most of it sentence for sentence.

Six things in it are worth fixing, and four of those are compliance
issues, not style preferences.

### Flagged issues in the live text

1. **Implied medical outcome claim (compliance).** The user quote about
   near misses, not falling, and better balance is followed by "That is
   what happens when a program actually works." The quote itself is a
   real user's own words, which is fine. The sentence after it turns one
   person's experience into a general claim that the app improves balance
   and reduces falls. That is an unsupported injury-prevention and health
   outcome claim (Knowledge Base "Health and Fitness Claims"), and the
   Strategic Thesis rule is explicit: never manufacture outcome proof,
   prove the process instead. Fix: keep the quote, cut the
   generalization, say plainly that it is one person's experience.
2. **"the things that are about to change your life" (compliance).** An
   outcome promise made to a stranger who has not opened the app. Cut.
3. **"She is too young to need two new knees and two new hips."**
   Ambiguous on the page (it reads as though the app prevented joint
   replacement) and it carries the same implied medical claim as #1. Cut.
4. **"Hold times start short and progress safely as your body is ready."**
   Two problems. "Safely" as an absolute is the kind of safety claim the
   Apple copy rules already forbid on screenshots, and "as your body is
   ready" implies the app senses readiness. It does not. The real
   mechanism is that hold time and difficulty step up on a schedule.
   Rewritten below.
5. **"6,700+ physio-informed poses" (verify before it ships again).**
   The Strategic Thesis flags that the library count has been stated
   inconsistently across surfaces and says to confirm the one true number
   before publishing it. It is already published. The number is left
   untouched in the revision because guessing at it would be worse, but
   somebody needs to confirm 6,700+ is current and correct.
6. **"Give us 7 days risk free."** Must match the offer actually
   available *in the app*. The 2026-08-30 subscription-offers output
   could not confirm whether the iOS app sells subscriptions through
   StoreKit at all, or only through the website's Stripe checkout
   (Monthly $9.99, Annual $59.99, 7-day trial). If there is no 7-day
   trial inside the app, this line is misleading in Apple's sense and is
   a rejection risk.

Two smaller notes: the description switches from "we" to "my mother"
mid-paragraph, which the revision resolves to "our founder's mother"
(revert if the first-person founder voice is intentional), and there is
no safety line, which a stretching app aimed at 50+ users should have.

### Proposed revision (3,088 chars, within the 4,000 limit)

```
Something has changed. Maybe you noticed it on the stairs. Maybe it was getting up off the floor. Maybe you just quietly stopped doing things you used to do without a second thought.

You are not looking for a yoga class. You are not looking for a video where someone tells you to breathe into the stretch for 30 seconds while cheerful music plays. You have tried that. It does not stick, because it was never built for you.

WeStretch is different, and we want you to understand why before you scroll past.

We are a sophisticated algorithm wearing a very friendly face. You tell us three things: how much time you have right now, what your goal is today (a warmup feels nothing like a stiffness routine), and whether there are positions you would rather skip (lunges: off. We understand). Thirty seconds later you are following a step-by-step animated instructor through a routine built for you.

Not pulled from a small library. Not a template someone recorded for everyone. Built from your stretch history, your goals, and 6,700+ physio-informed poses, organized so that over time every joint moves in every direction it should. Hold times start short and step up on a schedule as you keep going, which a pre-recorded video can never do.

No two sessions are the same. Your routine evolves with you.

WHAT YOU GET
- A routine built around your body, your goals, and the minutes you actually have
- Poses mapped by licensed physiotherapists for safe joint movement
- Ada, an animated guide who moves through every stretch with you, live. No static sketch, no countdown timer, no guessing at the pose from a picture
- Problem areas you can tell us to work around
- Sessions as short as a few minutes, at home, in whatever you are wearing, with nobody watching

WeStretch lives in the space between expensive physiotherapy and generic YouTube routines. Physio-informed expertise. A routine that is yours alone. An experience so simple that an 87 year old can set up and start stretching in under 30 seconds. We know, because she is our founder's mother and our office timed her.

Here is one user, in her own words, after stretching daily for years:

"I was thinking today I might try something new and stretch different times throughout the day. I have had some near misses but have not fallen. When I think back, I used to fall all the time. My balance is definitely better. It's kind of amazing. The only thing I have done since Covid is stretching every day and the part that is interesting is that my stamina is actually pretty good. I can do a flight of stairs easily without feeling out of breath."

That is her experience, not a promise about yours. What we can promise is the process: expert-mapped movement, built around you, guided step by step.

Everything unfamiliar feels strange at first. Give it honest minutes a day for two weeks and judge it yourself.

WeStretch is a stretching and mobility app. It is not a medical device and does not diagnose or treat any condition. Stop any movement that hurts, and talk to your doctor if you have an injury or a medical condition.
```

**What changed, one line each:** kept the hook and the mechanism
paragraphs close to verbatim; dropped the shouting capitals on NOT (the
sentences carry it without them); added a scannable "WHAT YOU GET" block,
since most readers never tap "more" and the mid-description detail was
effectively invisible to them; rewrote the hold-time sentence to the true
schedule-based mechanism; folded in the two confirmed real assets that
were missing (the moving avatar versus a static sketch and timer, and
at-home privacy); reframed the testimonial as one person's experience and
cut the generalization after it; cut the two outcome promises; replaced
the trial sentence with the dare that the already-graded screenshot and
video copy closes on, so the page, the screenshots, and the video now end
on the same note; added a safety and non-medical-device line.

**Consent note on the testimonial.** This quote is a direct message from
a user, not an App Store review, so Apple's reviewer-consent rule from
the 2026-09-02 output does not technically apply. Written permission to
quote her should still be on file, and it is worth confirming that it is,
given the health-adjacent content of what she says.

---

## 7. Needs App Store Connect access (this automation has none)

1. Read and record the **current keyword field**, so section 4 becomes a
   real diff instead of a proposal.
2. Confirm **promotional text is actually empty**, then set draft A.
3. Confirm the **7-day free trial exists as an in-app offer**, not only
   on the website. This decides whether a trial line can appear in the
   description at all.
4. Confirm the **6,700+ pose count** is current and correct.
5. Confirm **written permission** is on file for the quoted user.
6. Check whether the app supports **Dark Mode**. That is already its own
   backlog item, and the same App Store Connect visit can answer it.

## 8. Handoffs

- **Unblocks the French and Spanish localization item.** The 2026-08-26
  output localized the screenshot and video copy and stopped because
  metadata had no English source. It has one now, whichever version Karen
  approves. Note that the subtitle localizes into a 30-character box in
  each language; French will not fit a literal translation of any of the
  four options, so it needs writing to the limit, not translating to it.
- **Product Page Optimization.** The subtitle is the cleanest next A/B
  test after the screenshot test from 2026-08-22.
- **Custom Product Pages.** The 2026-08-23 plan drafted per-page keyword
  fields and promotional text for five audiences. Those should be
  re-checked against whatever default keyword field is finally set, so
  the CPPs do not simply duplicate it.
