# Review: staff Voice Document vs what the repo already says

Written 2026-09-09, before any merge. Karen asked for advice first.
Nothing in this file has been incorporated anywhere yet.

## Verdict

The document is good. Better than most brand voice work, and noticeably better
than the fragments currently scattered across this repo. It should become the
basis of WeStretch's voice.

It cannot be dropped in as is. It contradicts two rules Karen herself set, and
it is missing three things the brand book treats as core.

---

## What it does better than anything we have

| Section | Why it is worth keeping verbatim |
|---|---|
| "If you can film the sentence, it's specific enough" | The single most useful test in the document. Nothing in the repo has an equivalent. |
| "When writing starts sounding written" | An anti-formula section: the flip, triples, stacked fragments, "Here's the thing". This is the section that stops copy reading as machine generated. No competitor voice doc has this. |
| Priority order (clear, useful, specific, sound like us) | Resolves conflicts instead of listing ideals. Rare and valuable. |
| Words we avoid | Concrete and testable, not vibes. |
| "Never write as though age itself is the problem" | Correct, and it matches the CMO image brief. |
| "Zero em dashes" | Already company policy. Good sign the author knows the house rules. |

---

## Conflict 1: guilt. This is the big one.

**Karen dictated, 2026-08-20** (`Team/CXO/In Progress/Onboarding UX Flow Spec/Brand-Voice-Principles.md`, principle 4):

> **Conversion lever: FOMO on invested progress.** The fear of losing the
> time/history/progress a user has already invested is a deliberate, ongoing
> conversion mechanism toward Pro, not just a one-time pitch.

**The staff document says the opposite, three times:**

> We're not trying to make people feel guilty.

> Nobody is behind. Nobody needs to earn their way back. Nobody should feel like they've failed.

> Editing checklist: "Could any sentence make someone feel guilty?"

It also bans the exact vocabulary that lever runs on: *fall behind, get back on
track, catch up, make up for*.

These cannot both be true. Loss aversion on invested progress is a guilt
mechanism. Either the FOMO lever survives and the staff doc's warmth is scoped
to everywhere except the Pro upgrade path, or the FOMO lever is retired.

**Recommendation: scope it, do not retire it.** Loss aversion is legitimate and
it converts. Write the rule as "we never imply the reader has failed, and we do
remind them what their streak and history are worth." The difference is
"you've lost 12 days" versus "your 40 routines stay with you on Pro". Same
lever, no blame. But this is Karen's call, not a writer's.

## Conflict 2: "Evolves with you" is close to a banned claim

**Root `Memory.md`, rule 6** forbids describing personalization as the app
learning, watching, or getting to know the user's body. The real mechanism is
physiotherapist recommended selection plus a scheduled step up in hold time
and difficulty.

**The staff document's "Words we own" says:**

> The app builds each one from your goals, your body, the time you have and
> everything you've already done, and it keeps adapting as you go.

"Keeps adapting as you go" and "builds from your body" read as observational
learning. That is the framing Karen corrected on 2026-08-29.

The same paragraph then gets it exactly right: *"Hold times progress."* That
part is true and on the record.

**Recommendation:** keep "Evolves with you" as the positioning phrase, rewrite
what sits under it. The honest version is stronger anyway: it is not that the
app guesses about your body, it is that physiotherapists already decided what
comes next and the app runs that progression on schedule. Prescriptive beats
adaptive as a trust claim.

## Conflict 3: Ada and Bruce are not in the document at all

The brand book gives four pages (p30 to p38) to Ada as the central character,
with a defined personality (motivator plus explainer, smart, adaptive, calm),
her own quoted lines, outfits and mix-and-match rules, plus Bruce as her higher
energy counterpart.

A voice document that never mentions the character who speaks most of the
in-app copy is incomplete. Ada's voice and WeStretch's voice are not the same
thing and the relationship needs stating.

**Recommendation:** add a section. WeStretch is the brand voice. Ada is a
character who speaks in it. Bruce is the same voice at higher energy. The
tone ladder in the document already supports this, it just needs naming.

## Conflict 4: smaller wording clashes

| Staff doc | Repo says | Fix |
|---|---|---|
| "Physio-informed" | Root `Memory.md` rule 6 uses "physio backed" | Pick one and use it everywhere. "Physio backed" is plainer and already in use. |
| "generally over fifty" | Brand image brief and CMO docs say "adults 50 to 65" | Align. 50 to 65 is the actual target. |
| Karen's principle 2: copy should credit the app with "tracking and advancing the user" | Staff doc avoids surveillance framing | "Tracking" has the same problem as "learning". Retire the word, keep "advancing". |
| Karen's principle 5: "speak to the user's ego" | Staff doc: "steady confidence", no hype | Compatible if "ego" means their achievement rather than flattery. Worth confirming. |

## Gap: it is a marketing voice doc, not a product one

It covers homepage, social, lifecycle email. WeStretch's words mostly live
somewhere else:

- In-app microcopy and sheet titles (hundreds of strings in the UX prototype)
- Push notifications
- App Store title, subtitle, description and screenshot copy
- Paywall and cancellation copy
- Error and empty states

The tone ladder ("the more the reader is feeling, the less personality we
bring") extends to all of these cleanly. It just has not been written down yet.

It also does not carry Karen's token rule: **drop optional commas around an
inserted name.** "Nice work {first_name}" not "Nice work, {first_name}".
That rule only matters in product copy, which is why a marketing-shaped doc
missed it.

---

## Does the Corey Haines skill pack have a voice skill?

**No dedicated voice skill.** The closest are `copywriting`, `copy-editing` and
`product-marketing`.

**But the plumbing matters more than the skill.** Nearly every skill in the pack
opens with the same instruction:

> If `.agents/product-marketing.md` exists, read it before writing. Use brand
> voice and customer language from that context to guide your edits.

That file does not exist yet. Which means all 57 installed marketing skills are
currently running with no knowledge of WeStretch at all: no voice, no audience,
no banned words, no em dash rule.

`product-marketing/SKILL.md` exists to generate that file. Its template has 12
sections, two of which are **Brand Voice** and **Customer Language**.

**This is the highest leverage thing on the list.** Creating
`.agents/product-marketing.md` turns every marketing skill in the pack from
generic to WeStretch specific in one file.

---

## Recommended sequence

1. **Karen decides the three conflicts above.** Nothing else can start.
2. **Merge into one voice document** at `core/voice.md` in this folder,
   replacing the current short stub. Keep the staff doc's structure, correct
   the claims, add Ada and Bruce, add the product copy section.
3. **Retire the old fragments** by pointing them at the merged file:
   `Team/CXO/In Progress/Onboarding UX Flow Spec/Brand-Voice-Principles.md`
   becomes a pointer, not a second source of truth. Two voice docs is how
   drift starts, which is the same failure the colour palette just had.
4. **Generate `.agents/product-marketing.md`** from the merged doc using the
   `product-marketing` skill, so the whole skill pack inherits it.
5. **Credit the author.** The document is genuinely strong work and most of it
   survives the merge intact.
