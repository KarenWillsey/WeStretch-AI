# 28-Day Reset Challenge Email Funnel — Round 2: Corey's Version

Reviewed: 2026-09-22. Baseline: `Round 1 - Marg x Chase x Expert Review.md`'s
final revised copy (not the original draft). This round redlines Round 1's
output using the vendored Corey Haines `marketingskills` pack
(`.agents/skills/`), not the `westretch-core` personas Rounds 1 and 3 used.

**"Run first" step satisfied by reading (not by invoking the interactive
`product-marketing` workflow, which would try to rewrite `.agents/product-marketing.md`):**
`.agents/product-marketing.md` (router) → `Brand System/core/voice.md` (full)
→ `Brand System/core/positioning.md`.

**Skills applied, each against Round 1's actual text, not name-checked:**
`copywriting`, `copy-editing` (Seven Sweeps), `emails`, `marketing-psychology`,
`offers`, `cro`, `ab-testing`, `churn-prevention`, `launch`, `lead-magnets`,
`marketing-council`.

---

## Step 1 finding: a voice.md non-negotiable Round 1 said it fixed funnel-wide, but didn't

Round 1's cross-funnel finding #1 explicitly states the "adapts... how you're
feeling changes" mechanism overclaim (voice.md's banned "it adapts to what
your body is telling it" framing) was "fixed in every instance below" across
Emails 2, 3, 4, 5. **Email 6 was never on that list, and its copy still has
it:** *"Your routine is built for you and **adapts as you progress**, so all
you have to do is open WeStretch and stretch."* Round 1's own notes on Email 6
even call this line "already the accurate version... a useful template," which
is incorrect. It's the same ambiguous "adapts" language the rest of the funnel
was rewritten to avoid, just without the "how you're feeling changes" half
that made the other four instances obviously wrong.

This was caught on a straight second read against voice.md's own banned list,
not by any single named skill, so it's reported here first rather than folded
into a skill-by-skill section. **Fixed below in Email 6's final copy**, worded
differently from the other four instances per voice.md's "repeat beliefs,
rotate language" rule: *"Your routine follows a physiotherapist-mapped
progression, so all you have to do is open WeStretch and stretch."*

This is the single biggest change in this round: a compliance/accuracy miss
survived two independent review passes (Round 1's own grading loop and this
round's re-read), not a conversion nice-to-have.

---

## Skill-by-skill findings

### `copy-editing` (Seven Sweeps)

**Sweep 1, Clarity/Specificity — Email 2 never states the start date.**
Emails 1, 3, 4, 5 all anchor their close with "Starting October 19" or "On
October 19." Email 2 is the only one of the five awareness-building emails
that never states when the Challenge starts, it just says "for four weeks."
This is also the exact gap Marg flagged in Round 1's own Loop 1 notes ("Email
2's CTA felt like the weakest 'why should I act now' of the bunch") and Round
1 never resolved it. Adding the date gives the reader the same concrete
anchor every other email in the arc has, and directly answers Marg's
unresolved complaint. **Fixed**: *"Starting October 19, you stretch for 15
minutes a day for four weeks. Not just on the days your back is stiff or your
neck is acting up."*

**Sweep 2, Voice/repetition — two small intra-email repeats.**
Email 1: "Tell WeStretch what's bothering you. **WeStretch** draws from a
stretch library..." repeats "WeStretch" as the subject of two consecutive
sentences, which reads mechanically when read aloud (the checklist's own "Would
I say this out loud?" test). Fixed to "It draws from..." Email 8: "Personalized
to what's **bothering you**... finally do something about the things that keep
**bothering you**" repeats the same phrase twice in one short email (voice.md's
"repeat beliefs, rotate language" rule applies within a single email, not just
funnel-wide). Fixed the second instance to "finally make progress on the
things you've been working around," which also ties to the "work around"
motif Emails 1, 2 and 7 already use.

**Sweeps 3–7 (So What, Prove It, Specificity, Emotion, Zero Risk):** no further
changes. Round 1's authority-beat placement (Email 1 open, Email 8 close)
already answers "so what" and "prove it" without padding every email; forcing
proof into Emails 6 and 7 would break the honest ceilings Round 1 already
named for exactly that reason. Agreed with Round 1's restraint here.

### `emails`

Subject lines, preview text and email lengths all sit inside this skill's
normal ranges; no structural sequence problems. One real test idea, not a
forced edit (see `ab-testing` below): Email 6's subject, "Got plans Monday?",
is a strong pattern-interrupt after five "reason why" emails, exactly the
sequence-pacing this skill recommends, but it's untested against a more
Challenge-specific alternative.

### `marketing-psychology`

**Loss aversion at the actual decision point.** Emails 8 and 9 build real,
non-manufactured urgency in the body copy (5 PM PST deadline, already
verified as an honest fact by Round 1) but the CTA button text on both is
still the generic "[JOIN THE 28-DAY RESET]", identical to the CTA in Emails
1–7. Putting the deadline on the button itself, at the exact point the reader
is deciding, is a direct application of loss aversion and the framing effect
("$X off" works better right where the price is, not two lines above it). This
is a **direct disagreement with Round 1**, which explicitly left the CTA
untouched everywhere, reasoning that "[JOIN THE 28-DAY RESET]" already follows
the action + what-you-get formula. That's still true for Emails 1–7, where
there's no deadline to put on the button. It's not true for 8 and 9, where the
deadline is the entire point of the email. **Fixed, scoped to only those two
emails**: both change to "[JOIN BEFORE 5 PM]."

**Fresh-start effect, already well used.** "Got plans Monday?" and the
"Reset" framing itself both lean on the psychological pull of a clean
temporal landmark (new week, named reset). No change needed, flagged
because it's relevant to the Marketing Council's Sutherland/Hormozi
disagreement below.

### `offers`

Ran the Anatomy of a Complete Offer against the funnel. Core deliverable
(clear), scarcity (real, not fake), name (clear, ownable) all present.
**Bonus stack and guarantee are both absent across all 9 emails, and so is
price.** This converges exactly with Round 3's already-tracked finding
(`WORK-TRACKER.md`: "none of the 9 emails ever states the 28-Day Reset's
price, billing cadence, or refund/cancellation terms"). Per `positioning.md`,
no pricing or guarantee terms exist anywhere in this repo to draw from, and
inventing one is explicitly against the rules ("do not invent any... ask
Karen"). **Not fixed in copy, flagged as a third independent convergence**
(Round 1 didn't name it, Round 3 named it, this round's `offers` skill names
it again from a completely different framework). Also can't tell from
`positioning.md` whether joining the Challenge requires anything beyond the
existing Free/Pro tiers, which is exactly the ambiguity the missing terms
create.

### `cro`

Value proposition clarity, headline effectiveness and trust signals are all
already strong post-Round-1. The one CRO-relevant friction point is the same
one `marketing-psychology` found independently: CTA copy at the two hard-deadline
emails doesn't communicate the actual decision being asked (join *before a
specific time*, not just join). Same fix, converged finding, fixed once (see
above).

### `ab-testing`

Applied the hypothesis framework to two ideas surfaced above rather than
shipping them as unproven assumptions:

1. **CTA text test (Emails 8–9).** *Because Emails 8 and 9 build real
   time-bound urgency in the body but not in the CTA, we believe changing the
   button to "[JOIN BEFORE 5 PM]" will increase click-through from these two
   emails specifically, without affecting Emails 1–7. We'll know this is true
   when CTR on Emails 8–9 is measured against the current "[JOIN THE 28-DAY
   RESET]" control.* Shipped as the new default below per the converging
   `cro`/`marketing-psychology` case, but flagged for an actual A/B split
   rather than treated as self-evidently correct, consistent with this
   skill's "don't just assume" principle.
2. **Subject line test (Email 6).** *Because "Got plans Monday?" is generic
   relative to the rest of the funnel's specificity (Marg's own critique in
   Round 1), we believe a Challenge-specific variant such as "Your Reset
   starts Monday" may lift open rate without losing the pattern-interrupt
   pacing.* Not shipped as a replacement, since Round 1 deliberately kept this
   subject and its case for doing so (a quick nudge email doesn't need to work
   hard) is reasonable; recorded here as a test idea for Karen, not an edit.

### `churn-prevention`

Applied the win-back/re-engagement sequence pattern (check-in → value
reminder → incentive → last chance) since part of this audience is
lapsed-pro. **Finding: the funnel's existing five-beat arc already matches
this pattern structurally** (Emails 1–3 build openness/check-in, 4–5 are
value reminders, 6–7 raise the incentive/readiness, 8–9 are last-chance), so
no structural rework is needed. This validates Round 1/Chase's Six-Axis read
rather than contradicting it. The one thing this skill's lens can't resolve on
its own is the free/lapsed-pro segmentation question already flagged twice
(Round 1, Round 3); see Marketing Council below for a third independent
argument on that question.

### `launch`

Confirms email is being used correctly as the funnel's owned channel (ORB
framework). No changes recommended to the emails themselves; the checklist
items this skill would normally flag (social posts, in-app banner, "New"
sticker) are other channels' work, out of scope for a 9-email review and
already handled by the separately reviewed landing page.

### `lead-magnets`

The Challenge itself functions as this funnel's acquisition hook. Its "what's
inside" specificity (Email 1's three-beat symptom list plus the filmable
benefit list) already does the job this skill asks a lead magnet's landing
page to do. No gating/capture-flow issue exists in the email copy itself
(that lives on the landing page, already reviewed separately). No changes.

### `marketing-council`

*Simulated council, three seats plus one designated dissenter, each take
built from the advisor's documented, published frameworks, not their actual
opinion of this funnel.*

**Seated: Eugene Schwartz, Alex Hormozi, Rory Sutherland, with Byron Sharp as
dissenter.**

**Eugene Schwartz — awareness and sophistication stages.** Schwartz's core
method in *Breakthrough Advertising* is that copy can only channel existing
desire, never invent it, and the right opening depends entirely on where the
reader already sits on the awareness scale. A free user who's never paid is
problem-aware at best, so Emails 1–3's "have you noticed this" opening is
correctly pitched. A lapsed-pro subscriber is already solution-aware, in
Schwartz's terms, and possibly most-aware: they know WeStretch, they know it
worked, they stopped for some other reason. Treating both groups identically
for nine straight emails means the highest-leverage move for the lapsed-pro
half of the list, channeling the desire they already proved they had, never
happens. **Bottom line:** fork Email 1's opening for lapsed-pro now, not
because Marg's framing said so (Round 1) or because a direct-response
checklist said so (Round 3), but because the audience is provably at a
different awareness stage and the copy doesn't reflect it.

**Alex Hormozi — the value equation.** Hormozi would run Dream Outcome ×
Perceived Likelihood over Time Delay × Effort. Time Delay and Effort are both
already low (15 minutes a day, clear step-by-step). Perceived Likelihood
improved with Round 1's authority beats. But the equation has an undefined
term: price is nowhere in the denominator because it's nowhere in the copy at
all. Uncertainty about cost doesn't just fail to help the offer, in Hormozi's
framework it actively depresses perceived value, because the reader has to
supply their own (usually worse) assumption. **Bottom line:** resolve and
state the terms before send, converging with `offers` and Round 3's already-
tracked finding.

**Rory Sutherland — psycho-logic, dissenting from Hormozi.** Sutherland's
recurring argument in *Alchemy* is that the rational case for a purchase and
the actual reason people buy are often different things, and stacking more
logic onto an already-logical case can kill the magic that's actually doing
the work. This funnel's real lever isn't the physiotherapist-mapped-
progression explanation (useful, but a rational patch, not the hook); it's
the fresh-start effect already baked into "Reset" and "Got plans Monday?",
the psychological pull of a clean calendar landmark. **Bottom line:**
resolving the price gap is right (Hormozi), but do it plainly and once, not
by adding more justification paragraphs. Don't let a legitimate fix become an
excuse to over-explain the "why" at the expense of the "when."

**Byron Sharp — dissenting from the entire exercise, evidence-based brand
growth.** Sharp's position in *How Brands Grow* is that mental and physical
availability, being easy to think of and easy to buy, predicts growth far
better than persuasion depth. From that lens, the highest-leverage thing this
funnel does isn't any single line edit, it's that "28-Day Reset Challenge"
and the CTA are repeated verbatim and consistently across all nine emails,
building the kind of salience Sharp's research says actually compounds.
**Bottom line:** ship the accuracy fix (Email 6) because it's a factual
correction, be skeptical that further line-level tinkering on already-A-grade
copy moves anything, and put the next unit of effort into reach (does this
funnel actually get sent to every eligible free and lapsed-pro user, with
nothing in the way of the click) rather than a fourth redline pass.

**Where the council disagrees.** Hormozi says add the missing rational
information (price/terms); Sutherland says do it minimally so it doesn't
dilute the emotional fresh-start register; Schwartz says the segmentation gap
is the real lever; Sharp says stop optimizing copy and start verifying reach.
None of these are resolvable from inside this document, they all require
Karen's input (real price/terms) or a distribution decision (segment fork,
send list completeness) that sits above a copy redline.

**Chair's synthesis:** ship this round's copy edits (they're accuracy fixes
and convergent, low-risk conversion fixes, not new tinkering). Don't fork the
segment or invent price/guarantee terms in this redline, consistent with
Rounds 1 and 3's restraint, but note that the segmentation question now has
three independent frameworks pointing the same way (Marg/Chase, the
direct-response checklist, and now Schwartz's awareness stages), which is
worth flagging to Karen as a stronger signal than before. Resolve the
price/terms gap before send regardless of the segmentation decision, since
Hormozi, `offers`, and Round 3 all reach it independently. Sharp's reach
caution is a tripwire for whoever owns the send, not a copy fix.

---

## Convergences (same finding via independent lenses)

1. **Email 6's mechanism-language miss** — found by a direct re-read against
   voice.md, not a single named skill, but every skill that touched Email 6
   afterward (`copy-editing`, `marketing-psychology`) confirmed the fix.
2. **Missing price/billing/guarantee terms** — `offers` (Anatomy gap),
   `marketing-council`'s Hormozi seat (value equation), and Round 3
   (already in `WORK-TRACKER.md`) all reach this independently. Not fixed
   here, can't be without inventing numbers.
3. **Free vs. lapsed-pro segmentation** — Round 1 (Marg/Chase), Round 3
   (direct-response checklist), and now `marketing-council`'s Schwartz seat
   (awareness stages) all independently recommend forking Email 1's opening.
   Three-for-three convergence, still not actioned here, same restraint as
   Rounds 1 and 3: it's a scope decision for Karen, not a line-level fix
   inside a draft.
4. **CTA urgency at the decision point** — `cro` and `marketing-psychology`
   both flagged Emails 8–9's generic CTA independently. Fixed once.

## Disagreements

- **This round vs. Round 1, on touching the CTA.** Round 1 deliberately left
  "[JOIN THE 28-DAY RESET]" untouched everywhere, reasoning the formula
  already worked. This round agrees for Emails 1–7 (nothing changed) but
  disagrees for Emails 8–9 specifically, where a real deadline exists in the
  body and should exist on the button. Scoped disagreement, not a wholesale
  reversal.
- **Hormozi vs. Sutherland**, inside the council, on how to close the
  price/terms gap once Karen supplies it: state it plainly and once
  (Sutherland) vs. treat it as a full value-equation lever worth building out
  (Hormozi). Not resolved here, noted for whoever writes that line once the
  real terms exist.
- **Sharp vs. everyone else**, on whether a fourth redline pass is the right
  use of effort at all, versus a distribution/reach question. Included
  because a real council doesn't just agree with the premise of its own
  work.

---

## Nothing changed without sign-off

October 19 and 5 PM PST are still treated as existing business facts, per
Round 1's rule. No price, guarantee or billing term was invented anywhere in
this round; every place one would help, it's flagged instead (see
Convergence #2).

---

## Final copy, email by email

### Email 1

**Subject:** For the stiffness that keeps showing up *(unchanged from Round 1)*
**Preview:** What if this time, you didn't stop as soon as it felt better? *(unchanged)*

Change this round: fixed a repeated-subject sentence pair ("WeStretch...
WeStretch") that read mechanically read aloud.

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
> Tell WeStretch what's bothering you. It draws from a stretch library developed with physiotherapists to personalize your stretches around those areas.
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

Change this round: added the missing "Starting October 19" anchor, the one
awareness-arc email that never stated a date, directly answering Marg's
unresolved Round 1 critique that this email's CTA had the weakest "why act
now."

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
> Starting October 19, you stretch for 15 minutes a day for four weeks. Not just on the days your back is stiff or your neck is acting up.
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

No changes this round. Clean pass across every skill applied.

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

**Subject:** This isn't about stretching *(unchanged from Round 1)*
**Preview:** It's about everything you want your body to let you do. *(unchanged)*

No changes this round. Strongest filmable writing in the funnel, per Round 1;
agreed, left alone.

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

No changes this round.

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

**Subject:** Got plans Monday? *(unchanged; test idea recorded above, not shipped)*
**Preview:** The 28-Day Reset starts October 19. 15 minutes a day. Four weeks to feel the difference. *(unchanged)*

Change this round: fixed the mechanism-language miss described at the top of
this document, the biggest single fix in this round.

> What are you doing Monday, [First Name]?
>
> Because the **28-Day Reset Challenge starts October 19.**
>
> For the next four weeks, give your body 15 minutes of personalized stretching a day.
>
> Your routine follows a physiotherapist-mapped progression, so all you have to do is open WeStretch and stretch.
>
> 15 minutes a day to work on what's bothering you, so it can bother you less.
>
> We start Monday.
>
> [JOIN THE 28-DAY RESET]

### Email 7

**Subject:** Tomorrow could be another Monday *(unchanged from Round 1)*
**Preview:** Or you could start feeling better. *(unchanged)*

No changes this round.

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

Changes this round: fixed a repeated "bothering you" within the same short
email; changed the CTA to state the actual deadline, converging
`cro`/`marketing-psychology` finding, scoped only to this email and Email 9.

> Maybe you've been reading about the **28-Day Reset** and thinking, *this might actually be what I need.*
>
> Something simple enough to stick with. Personalized to what's bothering you, using a stretch library developed with physiotherapists. And long enough to finally make progress on the things you've been working around.
>
> If that's you, you haven't missed it.
>
> The Reset starts today, and there's still time to join us. But not much time.
>
> Registration closes today at 5 PM PST.
>
> [JOIN BEFORE 5 PM]

### Email 9

**Subject:** In one hour, it's off the table *(unchanged)*
**Preview:** There's no "maybe later" after 5. *(unchanged)*

Change this round: CTA changed to state the deadline, same reasoning as
Email 8.

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
> [JOIN BEFORE 5 PM]
