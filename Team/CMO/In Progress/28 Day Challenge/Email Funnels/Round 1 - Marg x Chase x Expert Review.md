# 28-Day Reset Challenge Email Funnel — Round 1: Marg × Chase × Expert Review

Reviewed: 2026-09-22. Source: `28-Day Reset Challenge Email Funnel (Original).md` (verbatim baseline, not edited) in this folder.

**Steps run:** Chase (strategy) OK, Expert (copy) OK, Marg (grading) OK.
**Skills applied:** westretch-core (personas, rubric, honesty guardrail), `voice.md`, `positioning.md`.
**Loops:** 2 of 12 (target reached for the funnel average, remaining ceilings are honest ones, named below).
**Style precedent followed:** `28-Day Reset Challenge Landing Page Review.md`, same grading loop and format, applied to 9 emails instead of a page.

---

## Open question: free users vs. lapsed-pro subscribers

The draft is sent to both segments and never differentiates. Task asked the three personas to weigh in rather than have this silently fixed.

**Marg's view.** If she's a free user who's never paid, this copy speaks to her fine, it's a normal top-of-funnel introduction to a challenge. But if she's a lapsed-pro subscriber, receiving nine emails that never acknowledge she already used WeStretch feels slightly off, almost like being treated as a stranger. She'd specifically expect something like "your history is still here" (this is a real, already-approved WeStretch lever, see `voice.md`'s "Progress is an asset, not a debt") and its total absence would lower her "Speak to me" score if she pictured herself in that seat.

**Chase's view.** This is a Focus/relevance gap under FATE, not a honesty problem. The two segments sit at different points on the Six-Axis model. A never-paid free user is still building openness and expectancy, so the current top-of-funnel "have you noticed this" messaging is correctly pitched for them. A lapsed-pro user already has expectancy *and* prior compliance (they paid once), so treating them identically wastes the single highest-converting lever available to that segment: saved progress. Right now that lever is used in zero of the nine emails.

**Expert's view.** Agrees it's a real gap, but this is a structural/resourcing decision (build two tracks, or add merge-tag-conditional lines), not a line-level copy defect inside a single draft. The lightest viable fix would be one conditional paragraph in Email 1 (open) and Email 8 or 9 (close), leaning on "your history and hold times are still here" for the lapsed-pro branch, while leaving the free-user track as written. That is a real scope change and shouldn't be made silently.

**Recommendation:** not applied in this round's redline. Named here for Karen's call. If she wants it, Round 2 can fork the sequence or add the conditional lines; none of the graded fixes below depend on this decision.

---

## Chase's strategy note (funnel-wide)

**Angle already in the draft (good instinct, didn't need inventing):** self-generated proof, "give it 15 minutes a day for 28 days and find out for yourself," is already the spine of the sequence. It's most explicit in Email 5 ("Or you can give it 28 days and finally see what happens when you do") and Email 9 ("You don't need another email from us. You need to decide before 5.") which respects the reader's autonomy instead of pressuring it.

- **FATE lever:** Focus (one ask across nine emails: join by Oct 19 / register by 5 PM PST), Emotion (relief from things quietly worked around, the whole "you adjust, you carry on" throughline in Email 3), Identity underneath, made explicit almost verbatim in Email 3: "you can decide that being mildly annoyed by your body every day is reason enough to do something about it."
- **Six-Axis read across the arc:** Emails 1 to 5 build openness and expectancy (naming the problem, reframing "I can live with it," reframing "I should stretch more"). Emails 6 to 7 raise focus and readiness (Monday check-ins). Emails 8 to 9 ask for compliance (register). That sequencing is correct, compliance is never asked before openness and expectancy are raised.
- **The one gap (same pattern the landing page review found):** trust and authority are never raised anywhere in the sequence. Zero mentions of physiotherapists, clinical backing, or how personalization actually works, across all nine emails, despite this being WeStretch's single ownable, honest differentiator. This is the same finding the landing page review made about the page before its fix, and it's worth flagging as a recurring pattern across CMO drafts, not just a one-off miss.
- **Ethical check:** passes overall. No manufactured urgency (Emails 8 and 9's deadline is a real registration cutoff, not invented), no fear-stacking, no fake authority, no invented social proof. One item needed a closer look, not because it manufactures urgency or fear, but because it drifts into language `voice.md` explicitly forbids: see "adapts... how you're feeling changes" below. That's a hard rule, not a style nitpick, so it's treated as a required fix, not an optional one.

---

## Cross-funnel findings (apply before individual grading)

**1. The recurring mechanism overclaim, the funnel's biggest single fix.**
Four of the nine emails (2, 3, 4, 5) use a near-identical phrase: *"personalized to you and adapts as you progress and how you're feeling changes"* (or a close variant). `voice.md`'s "Evolves with you" section is explicit that the accurate claim is: physiotherapists mapped the progression in advance, the app runs it using goals, time, and what's already been completed. It gives a direct list of banned phrasings, including "it adapts to what your body is telling it." "Adapts... how you're feeling changes" reads as exactly that banned claim, the app sensing and reacting to mood, which is not how the product actually works and is not supported anywhere in `positioning.md`'s mechanism description. This isn't a style preference, it's the honesty-guardrail-adjacent "never say it this way" list. Fixed in every instance below, and reworded differently each time per `voice.md`'s "repeat beliefs, rotate language" rule (the four instances were also near-verbatim copies of each other, a second, smaller problem on top of the accuracy one).

**2. Zero authority/credibility beat anywhere in the funnel.**
Same root cause as the landing page's pre-fix state. Fixed in two places only, not all nine: Email 1 (the first real introduction to the challenge, where trust needs to start building) and Email 8 (the last real decision point before the registration deadline, mirroring the landing page fix's placement "right before the price choice"). Not added everywhere on purpose, an authority clause bolted into every email would feel like padding, not proof; see honest ceilings below.

**3. Filler intensifiers (banned list: just, really, actually, simply, truly, genuinely).**
"Just" appears as pure filler in Emails 1, 2, 3, and the Email 7 subject line, cut in each case. Two exceptions kept deliberately: "actually" and "really" inside a reader's own quoted inner thought (Email 5's *"I really should stretch more,"* Email 9's *"I actually want to do this"*) are authentic represented speech, not narrator filler, so they stay. Email 5's non-quoted "how much better your body can actually feel" is narrator voice and was cut.

**4. Comma before an inserted name.**
`voice.md`: drop the optional comma unless dropping it creates a genuine misread (two tokens running together). Email 6's "What are you doing Monday, [First Name]?" keeps its comma, dropping it risks "Monday Karen" reading as one run-on phrase, the stated exception. Email 7's "...start doing something about it, [First Name]." drops its comma, no such collision risk there.

**5. "Everything in threes" overused across the sequence.**
Three separate emails (1, 4, 7) build a three-beat list of body complaints. `voice.md` flags this shape as one to watch when it repeats: "use two sometimes, use four." Email 1's triple is kept (it's the funnel's opener and, after the fix below, does real filmable work). Email 4's triple is left alone (it's this funnel's strongest, most filmable writing, no fix needed). Email 7's triple is trimmed to a pair, and its matching resolution triple later in the same email is trimmed to match, so problem and resolution now parallel cleanly at two beats each instead of drifting into automatic-sounding rhythm.

**6. Stacked "flip" plus "triple negation" back to back in Email 4.**
The subject ("This isn't really about stretching") is a flip, and the body immediately follows with a triple negation ("Not touching your toes. Not becoming someone who loves stretching. Having a body you don't have to think about quite so much."). Two of `voice.md`'s "sentence shapes that get overused" stacked in the same email. The subject's filler "really" is cut on its own merits (see 3), which softens the flip. The triple negation is trimmed from three fragments to two, connected with "It's" so the last line stops dangling as its own fragment.

**7. Redundant closing-line device.**
Emails 6 and 7 both end on a short, stand-alone "dramatic single line" (Email 6: "That's the deal." then "We start Monday."; Email 7: "That's what feeling better looks like."). Used twice back to back within Email 6 itself. `voice.md`: "if two pieces in a row are built on it, rebuild one." Email 6's "That's the deal." is cut, "We start Monday." stands alone. Email 7's closer is kept, it's the more earned instance, directly paying off the "so... and..." lines just above it.

---

## Loop 1 — Marg's grades on the draft as written

| Email | Attention | Speak to me | Believe | Act | Honest | Avg | Grade |
|---|---|---|---|---|---|---|---|
| 1. For the stiffness that keeps showing up | A- | A- | B | A- | A | 3.62 | A- |
| 2. If you only stretch when something bothers you... | A- | A- | B | B+ | B+ | 3.40 | B+ |
| 3. The problem is, you can live with it | A- | A | B | A- | A- | 3.62 | A- |
| 4. This isn't really about stretching | B+ | A | B | A- | A- | 3.54 | A- |
| 5. "I should stretch more" isn't a plan | A | A- | B | A- | A- | 3.62 | A- |
| 6. Got plans Monday? | A- | B+ | A- | A- | A | 3.68 | A- |
| 7. Tomorrow could just be another Monday | B+ | A- | B+ | A- | A- | 3.54 | A- |
| 8. Still thinking this might be what you need? | A- | A- | B | A | A- | 3.62 | A- |
| 9. In one hour, it's off the table | A | A- | A- | A- | A | 3.82 | A |

**Funnel average: 3.61 (A-)** — clears the A- target, but Believe is the weak dimension almost everywhere, and it's the same root cause each time: the missing authority beat and (in four emails) the mechanism overclaim.

**Marg, in her own words:**
- "Personalized" and "adapts as you progress" get said in almost every email. I never once find out *why* I should believe that, or that anyone qualified was involved. That's the same thing I said about the landing page.
- "Adapts... how you're feeling changes" makes it sound like the app is watching me somehow. I don't love that. I want to know it's actually a plan someone smart made, not something reading my mood.
- Email 2's CTA felt like the weakest "why should I act now" of the bunch, nothing new is being offered beyond "for four weeks," which I'd already heard in Email 1.
- Email 6 is a nice change of pace after five "reason why" emails, but it doesn't feel like it's about *me* specifically, it's the most generic one in the set. I don't mind that, a quick nudge email doesn't need to work hard.
- Email 9 is the best one as written. It respects that I can make my own decision and doesn't lean on me.

**Expert's diagnosis:** almost every low Believe score traces back to the same two things, missing authority and the mechanism-accuracy issue, exactly like the landing page review's finding. Fix those in the right places (not everywhere) and most of the low grades move together, same pattern as before.

---

## Loop 2 — after Expert's rewrite

| Email | Attention | Speak to me | Believe | Act | Honest | Avg | Grade |
|---|---|---|---|---|---|---|---|
| 1. For the stiffness that keeps showing up | A- | A | A- | A- | A | 3.82 | A |
| 2. If you only stretch when something bothers you... | A- | A- | A- | B+ | A | 3.68 | A- |
| 3. The problem is, you can live with it | A- | A | A- | A- | A | 3.82 | A |
| 4. This isn't about stretching | A- | A | A- | A- | A | 3.82 | A |
| 5. "I should stretch more" isn't a plan | A | A- | A- | A- | A- | 3.76 | A- |
| 6. Got plans Monday? | A- | B+ | A- | A | A | 3.74 | A- |
| 7. Tomorrow could be another Monday | A- | A- | B+ | A- | A | 3.68 | A- |
| 8. Still thinking this might be what you need? | A- | A- | A | A | A | 3.88 | A |
| 9. In one hour, it's off the table | A | A- | A- | A- | A | 3.82 | A |

**Funnel average: 3.78 (A-),** up from 3.61. Five emails now grade A (1, 3, 4, 8, 9); the rest hold a solid A- with named honest ceilings below, not forced past them.

---

## Honest ceilings (named, not forced past)

- **Believe, funnel-wide, can't reach A+ everywhere.** `positioning.md` confirms no quantitative outcome proof exists yet (no user counts, retention, or results data). Correctly never fabricated here, that's the right call, not a defect.
- **Email 6's Speak to me stays at B+ on purpose.** It's a short, low-key check-in email by design, matching `voice.md`'s tone ladder ("match the pace to the reader's state, not the format"). Forcing it to feel deeply personal would fight the point of a quick nudge.
- **Email 7's Believe stays at B+ on purpose.** It's a pure emotional beat, not a proof moment. Bolting an authority clause into it would break the moment the way an unearned aside would; the landing page review made the same call about the hero section for the same reason.
- **Act, most emails, capped just under A+.** The CTA copy itself, "[JOIN THE 28-DAY RESET]", already follows the strong formula (action + what you get). It wasn't broken, so it wasn't touched, same as the landing page review's conclusion on this exact button text.
- **The free vs. lapsed-pro gap is not graded here at all.** It's a structural decision for Karen, not a line-level defect inside this draft. See the section above.

## Nothing changed without sign-off

October 19 and 5 PM PST are treated as existing business facts, not something Expert or Marg can invent or alter. If either date changes, that's a fact-check for Karen, not a copy issue.

---

## Final copy, email by email

### Email 1

**Subject:** For the stiffness that keeps showing up *(unchanged)*
**Preview:** What if this time, you didn't stop as soon as it felt better? *(unchanged)*

Changes: cut a filler "just"; cut a filler "actually"; added the funnel's first authority beat where "personalized" was previously an unproven assertion; paired one generic line with a filmable specific from `positioning.md`'s "Problems we solve" list.

> If your neck is regularly bothering you...
>
> Or your back has opinions about the way you slept...
>
> Or sitting for too long means taking a second to straighten up when you stand...
>
> Then this is for you.
>
> On October 19, we're kicking off the **28-Day Reset Challenge.**
>
> For four weeks, you'll spend 15 minutes a day stretching what *your* body needs.
>
> Tell WeStretch what's bothering you. WeStretch draws from a stretch library developed with physiotherapists to personalize your stretches around those areas.
>
> So instead of working around the tight hip, sore neck or back that keeps acting up, you'll spend a little time every day working on it.
>
> And you're going to feel the difference.
>
> You'll get up easier. Get out of the car without thinking about your hip. Bend, reach and turn without thinking so much about how your body feels.
>
> **15 minutes a day for a body that feels better all day.**
>
> The Reset starts October 19.
>
> [JOIN THE 28-DAY RESET]

### Email 2

**Subject:** If you only stretch when something bothers you... *(unchanged)*
**Preview:** You're stopping at exactly the wrong time. *(unchanged)*

Changes: cut one filler "just" (kept the functional "not just," which is doing a real job); fixed and reworded the mechanism claim.

> Most people don't decide to stretch at 2:17 on a perfectly comfortable Tuesday.
>
> They stretch because something is bothering them.
>
> Their back feels stiff. Their hip is tight. Their neck is acting up again.
>
> And when nothing is complaining, stretching is pretty easy to forget.
>
> **That's what the 28-Day Reset Challenge changes.**
>
> For four weeks, you stretch for 15 minutes a day. Not just on the days your back is stiff or your neck is acting up.
>
> And you don't have to figure out what to do. Your stretching follows a routine physiotherapists mapped out, personalized to what you tell WeStretch and building as you go.
>
> So when you start feeling better, you don't stop and wait for the next reminder.
>
> You keep going.
>
> Give your body 15 minutes a day for four weeks and feel what changes when you give it some real consistency.
>
> [JOIN THE 28-DAY RESET]

### Email 3

**Subject:** The problem is, you can live with it *(unchanged)*
**Preview:** And that's exactly how stiffness quietly becomes your normal. *(unchanged)*

Changes: cut a filler "just"; fixed and reworded the mechanism claim.

> The annoying thing about stiffness is that it's usually pretty easy to live with.
>
> You find the position where your back doesn't bother you as much. You take a second to straighten up after sitting for a while. You turn a little differently when your neck is acting up.
>
> None of it is a big deal.
>
> And that's exactly why it's so easy to keep putting up with.
>
> You adjust. You carry on. Eventually, the little things you do because your body feels stiff become part of how you move through the day.
>
> **But "I can live with it" is a pretty low bar for how your body should feel.**
>
> You don't need to wait for your back to get worse. Or your hip to become a bigger problem. You can decide that being mildly annoyed by your body every day is reason enough to do something about it.
>
> That's what the **28-Day Reset Challenge** is for.
>
> Starting October 19, you'll spend 15 minutes a day with stretching built around what's bothering you and how you're progressing, using a routine physiotherapists mapped out.
>
> Give it four weeks.
>
> **Not because your body feels terrible. Because "fine" isn't the same as feeling good.**
>
> [JOIN THE 28-DAY RESET]

### Email 4

**Subject:** This isn't about stretching *(cut "really", a filler intensifier, in the highest-visibility line in the email)*
**Preview:** It's about everything you want your body to let you do. *(unchanged)*

Changes: subject filler cut; trimmed a stacked triple negation to two beats and connected it so the last line doesn't dangle as its own fragment; fixed and reworded the mechanism claim. Body otherwise unchanged, it has the strongest filmable imagery in the whole funnel and didn't need it.

> You probably don't care about becoming impressively flexible.
>
> You care about going for the long walk without wondering how your back will feel later.
>
> Sitting through dinner without having to keep finding a more comfortable position.
>
> Getting up the next morning without immediately noticing your neck, your back or that same tight hip.
>
> That's the real point of stretching.
>
> Not touching your toes, or becoming someone who loves stretching.
>
> It's having a body you don't have to think about quite so much.
>
> That's what the **28-Day Reset Challenge** is about.
>
> Starting October 19, you'll spend 15 minutes a day with a routine physiotherapists mapped out, personalized to you and building as you progress.
>
> Four weeks of giving your body the consistent stretching it hasn't been getting.
>
> Because the best thing about feeling better in your body is getting on with everything else.
>
> [JOIN THE 28-DAY RESET]

### Email 5

**Subject:** "I should stretch more" isn't a plan *(unchanged)*
**Preview:** So give it a start date: October 19. *(unchanged)*

Changes: fixed and reworded the mechanism claim; cut one narrator-voice "actually" (kept the two instances of "really"/"actually" that represent the reader's own quoted inner thought, those are authentic represented speech, not filler).

> You've probably thought it before:
>
> **I really should stretch more.**
>
> The problem with "more" is that it can start tomorrow.
>
> There's no start date. No finish line. No answer to how often, how long or what stretches you should actually be doing.
>
> So it stays something you *should* do.
>
> That's exactly what the **28-Day Reset Challenge** takes off your plate.
>
> Starting October 19, you stretch for 15 minutes a day. Your routine follows a progression physiotherapists mapped out, personalized to you as you go.
>
> For four weeks, there's no wondering whether you should stretch today or what you should do. You open WeStretch, your routine is there, and you do it.
>
> And that gives you something another month of *I really should stretch more* never will:
>
> The chance to find out how much better your body can feel.
>
> You can keep meaning to stretch more.
>
> Or you can give it 28 days and finally see what happens when you do.
>
> [JOIN THE 28-DAY RESET]

### Email 6

**Subject:** Got plans Monday? *(unchanged)*
**Preview:** The 28-Day Reset starts October 19. 15 minutes a day. Four weeks to feel the difference. *(unchanged)*

Changes: removed a redundant closing line stacked directly on top of another one. Name-comma kept deliberately, see cross-funnel finding 4.

> What are you doing Monday, [First Name]?
>
> Because the **28-Day Reset Challenge starts October 19.**
>
> For the next four weeks, give your body 15 minutes of personalized stretching a day.
>
> Your routine is built for you and adapts as you progress, so all you have to do is open WeStretch and stretch.
>
> 15 minutes a day to work on what's bothering you, so it can bother you less.
>
> We start Monday.
>
> [JOIN THE 28-DAY RESET]

### Email 7

**Subject:** Tomorrow could be another Monday *(cut "just")*
**Preview:** Or you could start feeling better. *(unchanged)*

Changes: subject filler cut, matched in the body's opening line; trimmed the problem triple and its matching resolution triple to two beats each so they parallel cleanly; dropped the comma before the inserted name (no misread risk here, unlike Email 6).

> Tomorrow could be another Monday.
>
> Your back feels how it feels. That tight spot is still that tight spot. You notice it, work around it and get on with your day.
>
> Or tomorrow could be the day you finally start doing something about it [First Name].
>
> The 28-Day Reset starts tomorrow.
>
> For the next four weeks, give your body 15 minutes of personalized stretching a day and work on the things that keep bothering you instead of continuing to work around them.
>
> So your back isn't the first thing you notice when you stand up. And that tight spot stops getting a say in how you move through your day.
>
> That's what feeling better looks like.
>
> [JOIN THE 28-DAY RESET]

### Email 8

**Subject:** Still thinking this might be what you need? *(unchanged)*
**Preview:** The Reset Challenge starts today. You can still join. *(unchanged)*

Changes: replaced a vague trust claim ("personalized to your body," exactly what Marg is built to punish) with the funnel's second and last authority beat, placed right before the final ask, mirroring where the landing page review placed its subscription-screen fix.

> Maybe you've been reading about the **28-Day Reset** and thinking, *this might actually be what I need.*
>
> Something simple enough to stick with. Personalized to what's bothering you, using a stretch library developed with physiotherapists. And long enough to finally do something about the things that keep bothering you.
>
> If that's you, you haven't missed it.
>
> The Reset starts today, and there's still time to join us. But not much time.
>
> Registration closes today at 5 PM PST.
>
> [JOIN THE 28-DAY RESET]

### Email 9

**Subject:** In one hour, it's off the table *(unchanged)*
**Preview:** There's no "maybe later" after 5. *(unchanged)*

No changes. This one was already clean, honest, and well-paced, a genuine example of the loop not manufacturing a problem where there wasn't one. The "actually" in "I actually want to do this" is kept for the same reason as Email 5's, it's the reader's own quoted inner voice, not narrator filler.

> For the past couple of weeks, joining the **28-Day Reset** has been something you could think about.
>
> In one hour, it won't be.
>
> Registration closes at **5 PM PST**, and after that, the Reset Challenge is underway and this round is closed.
>
> So if there's still a part of you thinking, *I actually want to do this,* listen to it.
>
> You don't need another email from us. You need to decide before 5.
>
> [JOIN THE 28-DAY RESET]
