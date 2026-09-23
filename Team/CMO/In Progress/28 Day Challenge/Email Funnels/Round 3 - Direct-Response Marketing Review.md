# Round 3 — Direct-Response Marketing Review

Skill applied: `westretch-direct-response-marketing` (WS_SABRI_SKILL_USED), run directly
against `28-Day Reset Challenge Email Funnel (Original).md`. Independent of Round 1
(Marg x Chase x Expert) and Round 2 (Corey's Version) — this redlines the original only,
per `Memory.md`'s note that rounds 1 and 3 are deliberately comparable siblings.

Also read in full per the mandatory brand files: `Team/CMO/In Progress/Brand System/core/voice.md`
and `core/positioning.md`.

---

## Headline finding: the personalization language breaks voice.md's #1 non-negotiable, five times

Emails 2, 3, 4, and 5 all describe the stretching as personalized "**and adapts as you
progress and how you're feeling changes**" (or a close variant). That phrase — the app
reacting to "how you're feeling" — is the exact framing voice.md bans: *"never say the
app learns your body, watches how you move, adapts to what your body is telling it."*
The real claim is stronger and more honest: physiotherapists already mapped the
progression, WeStretch runs it on a schedule. That's what "evolves with you" means to
say, and it's what's rewritten throughout below. This is the single biggest and most
repeated fix in this pass — it's a factual-honesty issue, not a style preference, and it
was wrong in nearly half the sequence.

(Email 6's "adapts as you progress" has no feelings clause attached — that one's fine
as written and is the model for how to phrase this elsewhere.)

## Critical gap: no email ever states the price

Running the sequence against the skill's 17-step sequence (step 13, "reveal the price,"
and step 14, "genuine urgency"), Emails 6 through 9 build real deadline pressure toward
a 5 PM PST cutoff, but at no point in nine emails does the copy say what registration
costs, what it includes, or what billing/trial terms apply. positioning.md confirms the
Reset is "a separate paid challenge," so this isn't a free feature — someone clicking
[JOIN THE 28-DAY RESET] from Email 6 onward is walking into a price they haven't been
told. Building urgency around an unstated cost is a conversion risk (surprise-priced
paywalls depress click-through and drive complaints/refunds) and it's a direct violation
of the sequence's own escalation logic: you can't ethically rush a decision you haven't
described. **Recommend inserting exact price, billing cadence, and trial/refund terms
starting at Email 5 or 6** — the first email that's explicitly offer-forward rather than
purely problem/insight-driven. I have not invented a number; this needs Karen/ops input
`[VERIFY: 28-Day Reset price, billing terms, refund policy]` before send.

## The free vs. lapsed-pro question — my view

Karen framed this drop as "free users, or pro users whose subscription has lapsed," but
the draft is a single undifferentiated top-of-funnel sequence. Running it through the
skill's awareness-matching step (Section 4, "match the message to awareness"):

- **A cold free user** is realistically **problem-aware to solution-aware** at best —
  they have the app but may never have experienced a structured routine. Emails 1-3
  spending real estate re-establishing "stiffness sneaks up on you, reactive stretching
  doesn't work" is the correct move for this reader.
- **A lapsed-pro subscriber** is already **most-aware**. They paid for WeStretch once,
  used it, and stopped. Opening on "if your neck is regularly bothering you..." treats
  someone who already has a physio-informed history with the product like a cold
  stranger. It skips the strongest lever available for that segment: **progress is an
  asset, not a debt** (voice.md). A returning subscriber responds better to "you know
  what showing up did before, your history's still there" than to being re-introduced
  to the concept of stretching.

**My recommendation:** don't build two parallel 9-email sequences — that's a lot of
production for one campaign and Emails 3 through 9 work for both audiences as written
(once past awareness). Instead, **fork only the opening beat of Email 1 (and optionally
Email 2)**: a lapsed-pro variant that leads with their saved history/streak instead of
introducing the problem cold, then rejoins the same spine from Email 3 onward. That's a
one-email (maybe two-email) production cost, not a nine-email one, and it fixes the
actual awareness mismatch instead of leaving it unaddressed. This is Karen's call to
make, not mine to force through the redline — flagging it here and in `Memory.md`
rather than silently forking the whole sequence.

## Awareness stage and escalation read, email by email

| # | Subject | Awareness stage | 17-step role |
|---|---|---|---|
| 1 | For the stiffness that keeps showing up | Problem-aware | Call out audience, make problem vivid |
| 2 | If you only stretch when something bothers you... | Problem-aware → solution-aware | Insight + reveal distinct mechanism |
| 3 | The problem is, you can live with it | Problem-aware | Handle the "it's fine" objection |
| 4 | This isn't really about stretching | Solution-aware | Translate feature into life outcome |
| 5 | "I should stretch more" isn't a plan | Product-aware | Handle the "I'll start eventually" objection, soft offer |
| 6 | Got plans Monday? | Product-aware → most-aware | Present the offer, one CTA |
| 7 | Tomorrow could just be another Monday | Most-aware | Day-before urgency |
| 8 | Still thinking this might be what you need? | Most-aware | Day-of urgency, remove risk of missing out |
| 9 | In one hour, it's off the table | Most-aware | Final-hour urgency, close |

**Is the escalation sound?** Yes, structurally. Problem recognition → outcome →
objection-handling → offer → three-stage urgency is the right shape, and Emails 6-9 are
genuinely well-built real-deadline urgency (no fake scarcity, no invented numbers).
Email 9 in particular needs zero copy changes — it's the strongest email in the funnel
and a model for the others: specific deadline, honest tone, one clean CTA, no oversell.

**The one structural weakness**, beyond the price gap above: Emails 1-4 (four of nine)
stay in pure problem/insight mode before the product's mechanism gets a real answer.
For a list that's at minimum product-aware, that's slower than it needs to be. I haven't
rewritten the structure — the copy at each stage is good — but if Karen wants a tighter
funnel, collapsing Emails 3 and 4's insight into one email and using the reclaimed slot
for the price/offer reveal would tighten this further. Noted, not actioned, since it
changes the email count Karen already approved.

## Line-level edits

Full reasoning per email below. Every change is reflected in the redline PDF and the
JSON source at `tools/round3_redline.json`.

### Email 1 — no structural issues
Subject and preview are strong, specific, filmable hooks — keep. Only edit: cut the
filler "just" from "just 15 minutes a day" (voice.md lists "just" as a filler
intensifier that does no work). This is also the email where, per the segmentation
note above, Karen could insert a lapsed-pro-specific opening variant if she decides to
fork it; I haven't built that variant here since it's her call whether to fork at all.

### Email 2 — personalization violation fixed
"Your stretching is personalized to you and adapts as you progress and how you're
feeling changes" rewritten to the authorized "evolves with you" framing: physiotherapists
mapped the plan, WeStretch runs it. Also cut two instances of filler "just."

### Email 3 — personalization violation fixed
Same fix applied to "stretching personalized to you, how you're feeling and how you're
progressing." Minor filler cut ("just become part of").

### Email 4 — personalization violation fixed, plus a soft guilt fix
Same "adapts... how you're feeling changes" fix. Also softened "the consistent
stretching it hasn't been getting" — as written it mildly implies the reader has been
neglecting their body, which brushes against voice.md's "nobody should feel like
they've failed." Rewritten to tie back to Email 2's actual insight (reactive vs.
consistent stretching) instead of implying a personal shortfall.

### Email 5 — personalization violation fixed, plus a callback tightened
Same mechanism fix. Also: the opening "I really should stretch more" doesn't quite
match the subject line's "I should stretch more" — since the whole email's hook depends
on that internal-monologue phrase feeling exact, I cut "really" so body and subject
say the same thing (consistency strengthens the recognition moment). Cut "really" again
in the closing callback, and rewrote it so it doesn't literally repeat the opening line —
voice.md flags "repeating the opening line at the end to close the loop" as a device that
reads as manufactured rather than earned. Also cut a stray "actually."

### Email 6 — no copy changes, but this is where the price gap should close
As written, this is a clean, well-built offer/CTA email — "adapts as you progress" here
has no feelings clause and is the correct, compliant phrasing. Flagging again: this is
the natural slot for price/billing/trial terms per the 17-step sequence, and it's
currently silent on all three.

### Email 7 — filler cut, one triad varied
Cut "just" from subject and opening line to match. The symptom list ("Your back feels
how it feels. Your neck does what it does. That tight spot is still that tight spot.")
is the fourth near-identical three-item list in the sequence by this point (Emails 1, 2,
3 all use the same device) — voice.md notes threes are "overused... exactly why it
starts sounding automatic" and to vary sometimes. Trimmed to two items here for rhythm;
left the email's closing triad alone since one strong triad per email is fine, it's only
back-to-back repetition across the sequence that gets formulaic.

### Email 8 — subject and preview sharpened
"Still thinking this might be what you need?" passes voice.md's own editing-checklist
test the wrong way — "could this sentence appear in any wellness app? If yes, rewrite
it" — yes, it could. For a same-day deadline email, the real deadline is a stronger
Attention hook than a soft question. Rewrote subject to lead with the actual cutoff
time and tightened the preview to match. Body copy is otherwise solid and unchanged.

### Email 9 — no changes
Strongest email in the funnel: honest, specific, one CTA, no oversell, genuine deadline.
Model for what the earlier urgency emails should sound like.

---

## Full revised copy (all 9 emails)

### Email 1
**Subject:** For the stiffness that keeps showing up
**Preview:** What if this time, you didn't stop as soon as it felt better?

If your neck is regularly bothering you...

Or your back has opinions about the way you slept...

Or sitting for too long means taking a second to straighten up when you stand...

Then this is for you.

On October 19, we're kicking off the **28-Day Reset Challenge.**

For four weeks, you'll spend 15 minutes a day stretching what *your* body needs.

Tell WeStretch what's bothering you, and your stretches are personalized around those areas.

So instead of working around the tight hip, sore neck or back that keeps acting up, you'll spend a little time every day actually working on it.

And you're going to feel the difference.

You'll get up easier. Move more comfortably. Bend, reach and turn without thinking so much about how your body feels.

**15 minutes a day for a body that feels better all day.**

The Reset starts October 19.

[JOIN THE 28-DAY RESET]

### Email 2
**Subject:** If you only stretch when something bothers you...
**Preview:** You're stopping at exactly the wrong time.

Most people don't decide to stretch at 2:17 on a perfectly comfortable Tuesday.

They stretch because something is bothering them.

Their back feels stiff. Their hip is tight. Their neck is acting up again.

And when nothing is complaining, stretching is pretty easy to forget.

**That's what the 28-Day Reset Challenge changes.**

For four weeks, you stretch for 15 minutes a day. Not only on the days your back is stiff or your neck is acting up.

And you don't have to figure out what to do. Physiotherapists already mapped what your stretching should look like next, and WeStretch runs that plan for you, four weeks in a row.

So when you start feeling better, you don't stop and wait for the next reminder.

You keep going.

Give your body 15 minutes a day for four weeks and feel what changes when you give it some real consistency.

[JOIN THE 28-DAY RESET]

### Email 3
**Subject:** The problem is, you can live with it
**Preview:** And that's exactly how stiffness quietly becomes your normal.

The annoying thing about stiffness is that it's usually pretty easy to live with.

You find the position where your back doesn't bother you as much. You take a second to straighten up after sitting for a while. You turn a little differently when your neck is acting up.

None of it is a big deal.

And that's exactly why it's so easy to keep putting up with.

You adjust. You carry on. Eventually, the little things you do because your body feels stiff become part of how you move through the day.

**But "I can live with it" is a pretty low bar for how your body should feel.**

You don't need to wait for your back to get worse. Or your hip to become a bigger problem. You can decide that being mildly annoyed by your body every day is reason enough to do something about it.

That's what the **28-Day Reset Challenge** is for.

Starting October 19, you'll spend 15 minutes a day on a routine built from a physiotherapist-mapped progression, matched to what you're working on and where you are in it.

Give it four weeks.

**Not because your body feels terrible. Because "fine" isn't the same as feeling good.**

[JOIN THE 28-DAY RESET]

### Email 4
**Subject:** This isn't really about stretching
**Preview:** It's about everything you want your body to let you do.

You probably don't care about becoming impressively flexible.

You care about going for the long walk without wondering how your back will feel later.

Sitting through dinner without having to keep finding a more comfortable position.

Getting up the next morning without immediately noticing your neck, your back or that same tight hip.

That's the real point of stretching.

Not touching your toes. Not becoming someone who loves stretching.

Having a body you don't have to think about quite so much.

That's what the **28-Day Reset Challenge** is about.

Starting October 19, you'll spend 15 minutes a day on stretching physiotherapists already mapped out for you, with hold times and difficulty stepping up on a schedule as you go.

Four weeks of consistent stretching, on a schedule instead of only when something's bothering you.

Because the best thing about feeling better in your body is getting on with everything else.

[JOIN THE 28-DAY RESET]

### Email 5
**Subject:** "I should stretch more" isn't a plan
**Preview:** So give it a start date: October 19.

You've probably thought it before:

**I should stretch more.**

The problem with "more" is that it can start tomorrow.

There's no start date. No finish line. No answer to how often, how long or what stretches you should actually be doing.

So it stays something you *should* do.

That's exactly what the **28-Day Reset Challenge** takes off your plate.

Starting October 19, you stretch for 15 minutes a day. Your routine follows a physiotherapist-mapped progression already built for four weeks, so you're never guessing what's next.

For four weeks, there's no wondering whether you should stretch today or what you should do. You open WeStretch, your routine is there, and you do it.

And that gives you something another month of good intentions never will:

The chance to find out how much better your body can feel.

You can keep meaning to stretch more.

Or you can give it 28 days and finally see what happens when you do.

[JOIN THE 28-DAY RESET]

### Email 6
**Subject:** Got plans Monday?
**Preview:** The 28-Day Reset starts October 19. 15 minutes a day. Four weeks to feel the difference.

What are you doing Monday, [First Name]?

Because the **28-Day Reset Challenge starts October 19.**

For the next four weeks, give your body 15 minutes of personalized stretching a day.

Your routine is built for you and adapts as you progress, so all you have to do is open WeStretch and stretch.

15 minutes a day to work on what's bothering you, so it can bother you less.

That's the deal.

We start Monday.

[JOIN THE 28-DAY RESET]

### Email 7
**Subject:** Tomorrow could be another Monday
**Preview:** Or you could start feeling better.

Tomorrow could be another Monday.

Your back feels how it feels. That tight spot is still there. You notice it, work around it, and get on with your day.

Or tomorrow could be the day you finally start doing something about it, [First Name].

The 28-Day Reset starts tomorrow.

For the next four weeks, give your body 15 minutes of personalized stretching a day and work on the things that keep bothering you instead of continuing to work around them.

So your back isn't the first thing you notice when you stand up. Your neck isn't something you keep checking on. And that tight spot stops getting a say in how you move through your day.

That's what feeling better looks like.

[JOIN THE 28-DAY RESET]

### Email 8
**Subject:** Registration closes at 5 PM today
**Preview:** Doors are open until 5 PM PST today.

Maybe you've been reading about the **28-Day Reset** and thinking, *this might actually be what I need.*

Something simple enough to stick with. Personalized to your body. And long enough to finally do something about the things that keep bothering you.

If that's you, you haven't missed it.

The Reset starts today, and there's still time to join us. But not much time.

Registration closes today at 5 PM PST.

[JOIN THE 28-DAY RESET]

### Email 9
**Subject:** In one hour, it's off the table
**Preview:** There's no "maybe later" after 5.

For the past couple of weeks, joining the **28-Day Reset** has been something you could think about.

In one hour, it won't be.

Registration closes at **5 PM PST**, and after that, the Reset Challenge is underway and this round is closed.

So if there's still a part of you thinking, *I actually want to do this,* listen to it.

You don't need another email from us. You need to decide before 5.

[JOIN THE 28-DAY RESET]
