---
name: westretch-radio-ads
description: >
  Generate a fresh batch of 5 announcer-ready WeStretch 30-second radio ad scripts on
  unique topics. Automatically scans the Output folder to avoid repeating the same angle
  (new stories on existing topics are fine), then applies Chase strategy, Expert copy,
  and Marg grading before saving a clean studio-ready markdown file. Use whenever the user
  asks for radio ads, radio scripts, 30-second spots, radio copy, new radio ideas, or wants
  to rotate WeStretch radio creative. Always depends on westretch-core; invoke it first.
  Even if the user just says "write more radio ads" or "give me some radio scripts," use this skill.
  For revising or polishing a single existing script instead of generating a fresh batch,
  use the sibling radio-ad-revise skill instead.
---

# WeStretch Radio Ad Writer

Produces a batch of 5 announcer-ready 30-second radio ad scripts, each on a distinct angle,
each graded to an A average before delivery. Saves a clean studio-ready markdown file to the
Output folder.

## Step 0; Load westretch-core first

Invoke the westretch-core skill before writing a single word of copy. It holds the personas,
the Strategic Thesis, the ICP, and the honesty guardrail that every piece of WeStretch
marketing must respect. Do not proceed until it is loaded.

Key things to carry forward from westretch-core into this task:
- **ICP**: Busy, active adults 50+ with reduced mobility and some stiffness/pain. Adjacent:
  injury/rehab users, desk workers, busy parents.
- **Words we own**: Physio-informed. Step-by-step. Evolves with you.
- **Honesty guardrail**: Lead with and prove the process. Never manufacture outcome proof.
- **What WeStretch is NOT**: Not yoga, not a stretch library, not a timer list.
- **Real authority anchor**: Licensed physiotherapists designed the stretch library. Use it.

## Step 1; Scan the Output folder for existing radio ad angles

Read the contents of this project's own Output folder:
`C:\Users\karen\Documents\WeStretch AI\WeStretch-AI\Team\CMO\In Progress\Radio Specialist\5 x 30 second radio copy\Output\`

Find any markdown files that contain radio ad scripts (look for files named
`WeStretch-Radio-Ads-*.md` or similar). For each file found, extract the topic and specific
angle of each ad (e.g., "travel; post-flight stiffness on planes and buses",
"morning (waking up with a stiff back at 7 AM", "desk) afternoon neck and shoulder pain").

Build a "covered angles" list. The rule is:
- Do not repeat the exact same story angle.
- A fresh angle on an existing topic is allowed and encouraged. Example: "travel" has been
  covered via planes and road trips, but "hiking/adventure travel soreness" or "cruise ship
  stiffness" would be fresh.

If no prior radio ad files exist, the covered-angles list is empty.

## Step 2; Chase selects 5 fresh topics and designs the strategy

For each of the 5 ads, Chase identifies:
- The **scene or moment** (specific, visual, relatable for the ICP, not vague)
- **FATE mapping**: Focus (the moment), Authority (physio-informed), Tribe (who they are),
  Emotion (what they feel right then)
- The **identity the ad builds** ("I'm someone who keeps moving no matter what")
- **Six-Axis read**: Is the prospect open? Never ask for compliance before openness is raised.
- Whether to use **self-generated proof** (Chase's preferred technique when outcomes can't
  be honestly promised: invite them to try it and notice for themselves)

**Topic pool** (not exhaustive; Chase may add others that fit the ICP):
- Morning stiffness: waking up tight, hips that won't cooperate, back that needs coaxing
- Travel: adventure hiking soreness, cruise ship stiffness, long-haul flight aftermath,
  road trip with grandkids, international travel jet lag
- Desk/work: afternoon slump, work-from-home back pain, too many video calls
- Garden and yard: post-gardening lower back, weekend lawn work, planting season knees
- Golf: pre-round warm-up, post-round hip tightness, protecting your swing
- Pickleball or recreational sports: weekend play, staying in the game
- Post-workout: cool-down after the gym, morning run aftermath
- Grandchildren: keeping up with them, getting down on the floor and back up again
- Post-injury maintenance: after physio discharge, keeping progress going at home
- Nighttime wind-down: end-of-day routine, sleep prep, calming tight muscles
- Weekend warrior: Saturday project soreness, Sunday hike aftermath
- Couch/TV stiffness: getting up after a long movie, the evening sit

Choose the 5 that:
1. Are NOT on the covered-angles list (or bring a genuinely new story to a covered topic)
2. Collectively span different times of day, activities, and life moments, so the rotation
   feels varied, not repetitive
3. Are most likely to resonate with the ICP (50+ active adults) or strong adjacent audiences

## Step 3; Expert writes the copy

For each of the 5 scripts, Expert writes one clean radio ad following these rules.

**Length: 74–82 words.** At a comfortable announcer pace (approximately 150 words per minute),
this lands in 30 seconds. Count words. Cut ruthlessly. Every word earns its place.

**Structure:**
1. **Hook (2–3 short punchy sentences):** A specific, visual, relatable moment. Paint the
   scene in sound. No generic openers like "Are you tired of..." or "Do you struggle with..."
   Start in the middle of the moment.
2. **Solution (3–4 sentences):** Introduce WeStretch. Lead with the physio credential.
   Highlight ease: step-by-step, avatar-guided, works around your body, schedule, and goals.
   The phrase "designed with physiotherapists" or "built with licensed physiotherapists"
   must appear in every ad. It is the single most honest differentiator WeStretch has.
3. **Proof or access line (1 sentence):** Either a self-generated proof invitation
   ("try it today and notice the difference for yourself") or a concrete access
   statement ("if you have your phone, you have your program"). Never a promised
   outcome, and never a prescribed time commitment (no "ten minutes a day" style
   claims; sessions are user-controlled, not fixed-length; see this project's
   `Memory.md`).
4. **CTA:** "Download WeStretch today at WeStretch dot CA."

**House style (non-negotiable):**
- No em dashes, anywhere, company-wide rule (see the repo root `Memory.md`). Use commas,
  periods, colons, or parentheses instead.
- No outcome promises without proof. Do not write "reduce your pain," "improve your balance,"
  "feel better," or "change your life" as guaranteed results. Prove the process; let the
  listener generate their own outcome experience.
- No fear, guilt, manufactured urgency, or anxiety about aging. No "before it's too late,"
  "before your body gives out," or "don't let stiffness win."
- No jargon as headlines: "physio-informed" is fine in context; "adaptive algorithm" or
  "AI-powered" are not.
- "Avatar" is fine; it's 2026 and the audience knows what an app avatar is.

**Variety across the 5 scripts:**
- Do not open all 5 with the same sentence structure ("You wake up." five times = failure).
- Do not use "step by step" as the second phrase in every ad.
- Do not close all 5 with the same proof line.
- Each ad must feel like it was written for that specific person in that specific moment,
  not like a template with a swapped hook. Read all 5 back-to-back before finalizing;
  if they sound like variations of one script, rewrite the weakest ones.

## Step 4; Marg grades each script

Score each of the 5 scripts individually on Marg's 5 dimensions (A+ to F):
1. **Attention**: does the hook earn attention in the first two seconds, on audio alone?
2. **Speak to me**: does it sound like it's for me, not a mass audience?
3. **Believe**: do I buy it, or does it overclaim or tell me how I feel?
4. **Act**: does it make me want to download without feeling pushed?
5. **Honest**: does it feel real, or like a polished pitch?

**Target:** A average (≥ 3.50) on every script before it goes in the file.

Run the Expert × Marg loop (max 3 passes per script) until each hits target. If a
dimension reaches an honest ceiling below A+, name it and stop. Do not force the score
by overclaiming; the honest ceiling is a feature, not a failure.

## Step 5; Save and present the output file

**Filename:** `WeStretch-Radio-Ads-30sec-[YYYY-MM-DD].md`

Save to this project's own Output folder:
`C:\Users\karen\Documents\WeStretch AI\WeStretch-AI\Team\CMO\In Progress\Radio Specialist\5 x 30 second radio copy\Output\`

If a file with today's date already exists, append `-v2`, `-v3`, etc.

**File format, exactly this structure:**

```
# WeStretch Radio Ad Scripts; 30-Second Rotation
[date] | Batch of 5

---

## AD 1: [THEME IN CAPS]
*Topic: [one-line description of the specific angle]*

[clean script text; exactly what the announcer reads, nothing else]

---

## AD 2: [THEME IN CAPS]
*Topic: [one-line description of the specific angle]*

[clean script text]

---

[continue for AD 3, AD 4, AD 5]

---

*Steps run: Chase (strategy) OK, Expert (copy) OK, Marg (grading) OK.*
*Honest ceilings: [list any dimensions that hit an honest ceiling and why, or "none"]*
```

The scripts inside the `##` blocks are clean announcer copy only. No grades, no grading
notes, no persona labels, no production direction inside the script text itself. The
announcer picks up the file and reads straight from it.

After saving, present the file to the user with `mcp__cowork__present_files`.
