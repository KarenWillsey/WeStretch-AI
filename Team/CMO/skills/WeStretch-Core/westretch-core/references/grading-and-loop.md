# The grading loop, rubric, and honesty guardrail

## The rubric (Marg scores each piece A+ → F on 5 dimensions)
Adapt each dimension to the asset:
1. **Attention**, earns attention in the first moment (subject/preview for email; hook/thumbnail for a video card; headline for a page).
2. **Speak to me**, sounds like it's about *me*, not everyone.
3. **Believe**, believable, not overclaimed; doesn't tell me how I feel.
4. **Act**, makes me want the next step without feeling pushed.
5. **Honest**, feels honest, not like bait.

Scale for the A+ push: A+ = 4.3, A = 4.0, A− = 3.7, B+ = 3.3, B = 3.0.

## The loop
Marg grades → Expert rewrites the lowest-scoring dimensions → Marg re-grades → repeat. Continue until every piece hits the target, **or 12 loops, whichever comes first**.

## The target
1. First reach an **A-average per piece** (≥ 3.50).
2. Then push toward **A+ on every dimension where it's honestly possible**.
3. Where a dimension hits a legitimate ceiling below A+ (e.g., a deliberately soft CTA on a win-back email, or a warm-not-clickbait subject), **stop and name the dimension and why**. Do not force the score by sacrificing honesty. The honest ceiling is a feature, not a failure.

## The honesty guardrail (non-negotiable)
- No fake urgency, invented stats/results, fabricated testimonials, borrowed/false authority, or a pitch disguised as something else.
- Expert may not juice a grade by breaking this. If the only way to hit target is overclaiming, stop and flag it.
- Personalization only with data that is actually known, always with a safe fallback.
- If a proof point is required but doesn't exist, leave a clearly marked blank for the user, never invent it.

## Per-card / per-piece grading (for A/B testing)
When the asset is a sequence (e.g., video title cards) or a set (e.g., a screen series), grade each card/piece individually on the 5 dimensions with an average and letter grade, plus a one-line role tag (opener / trust / personalization / stakes / close) and note. This produces a "card bank" so the user can A/B test by swapping individual pieces, not just whole sequences. For mid-sequence cards, read "Attention" as "keeps me watching" and "Act" as "moves me forward."

## Known failure patterns from real review feedback
These are confirmed failure modes, found by an actual human reviewer, not hypothesized. Marg checks every new piece against this list in addition to the 5-dimension rubric. When length-editing (or any editing) triggers one of these, that is a real defect, not a style nitpick.

- **Don't trim into a sentence fragment.** Cutting words to hit a length limit can leave a grammatically incomplete line. A card or title must remain a complete, standalone sentence or phrase after every edit, read it alone and confirm it parses.
- **Don't leave a comparison unstated.** Words like "no keeping up," "easier than," "unlike," imply a comparison. If the thing being compared against gets cut for length, the line can read as meaningless or as the literal opposite of what's true. Either state the comparison in the same line or don't use a comparative at all.
- **Re-check attribution after every trim, not just before.** Cutting words can silently shift who or what a claim credits. Example: "physiotherapists mapped what's safe for you" credits personal assessment to the physiotherapists; the true claim is that physiotherapists mapped the general safe-movement framework and the algorithm personalizes it per user. A trim that drops the qualifier can turn an honest claim into an overclaim, this is an honesty-guardrail failure, not a wording preference.
- **Don't leave a pronoun without a same-line antecedent.** "Tell it what to work around. It works around it." is vague in isolation, "it" and "what to work around" have no concrete referent inside the line itself. Name the concrete thing (what hurts, what to avoid) even under a tight limit.
- **Read every card as if it's the only one the viewer ever sees.** See the standalone constraint in the app-store-copy skill: cards in a looping video are not guaranteed to be seen in sequence.

### Review log (the feedback-intake method)
Whenever a real human reviewer (not Marg) flags a piece, log it here before fixing the copy: what they said, why (the root cause, not just the symptom), and what rule it produced. This is how outside feedback becomes a durable part of the skill instead of a one-time fix.

| Date | Reviewer | Item | Comment | Root cause | Rule added |
|------|----------|------|---------|------------|------------|
| 2026-08-10 | Kari (office) | App-store-copy Part 1, card 3, "Licensed physiotherapists mapped what's safe for you" | "Nope" | Overclaimed physiotherapist involvement; the algorithm personalizes, physios mapped the general framework | Re-check attribution after every trim (this list) |
| 2026-08-10 | Kari (office) | App-store-copy Part 1, card 4, "Tell it what to work around. It works around it." | "Not clear" | Pronoun ("it") with no concrete antecedent in the line | Don't leave a pronoun without a same-line antecedent (this list) |
| 2026-08-10 | Kari (office) | App-store-copy Part 1, card 5, "Ada guides you step by step. No guessing, no keeping up." | Confused: you do have to keep up with Ada, unlike a live class where you might not | "No keeping up" is a comparison (vs. a class) left unstated after trimming, reads as contradicting the product | Don't leave a comparison unstated (this list) |
| 2026-08-10 | Kari (office) | App-store-copy Part 1, card 7, "Give it a few honest minutes a day for two weeks. Let your own body tell you." (trimmed) | "This doesn't make sense" | Trimming dropped the verb ("Give it"), leaving a sentence fragment | Don't trim into a sentence fragment (this list) |

## The deliverable (every run)
- **A one-line confirmation that all three personas ran, in order, with nothing skipped.** Format: `Steps run: Chase (strategy) OK, Expert (copy) OK, Marg (grading) OK.` For a copy-only task, show `Chase (n/a, copy-only)`.
- **A short, labeled Chase strategy note before the copy:** the FATE lever(s), the identity it builds, the Six-Axis read, and why this angle fits. Never fold Chase into a single line. His direction must be visible.
- How many loops it took.
- A per-loop log: a grade table (piece × 5 dimensions + average + letter), Marg's key critiques, Expert's changes.
- The final pieces, ready to use.
- An appendix: where the guardrail blocked a juiced grade, any optional personalization notes, and which dimensions hit an honest ceiling and why.
