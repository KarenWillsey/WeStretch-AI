# Email Funnels (28 Day Challenge); Memory

- The original draft doesn't actually differentiate free users from
  lapsed-pro subscribers, it reads as a generic top-of-funnel promo
  sequence despite Karen's framing it as being for those two segments.
  Surfaced to the reviewing personas/skills rather than silently
  resolved; log here once Karen decides whether the shipped version
  should split by segment or stay one sequence.
- Three redline rounds were requested against different baselines on
  purpose, not by oversight: round 1 and round 3 both redline the
  original independently (so they're comparable to each other), round 2
  redlines round 1's output (so "Corey's version" shows what changed on
  top of the Marg/Chase/Expert pass, not a second diff against the
  original).
- Round 1 (`westretch-core`: Marg x Chase x Expert) is complete. Funnel
  average went from 3.61 (A-) to 3.78 (A-) over 2 loops; 5 of 9 emails
  graded A after the fix. Biggest finding, reached independently of round
  3 and matching it: the "adapts as you progress and how you're feeling
  changes" line (Emails 2, 3, 4, 5, each slightly different wording)
  violates voice.md's ban on claiming the app senses/reacts to the user,
  rewritten to the physiotherapist-mapped-progression framing everywhere,
  worded differently each time. Also found and fixed: zero physio-informed
  authority beat anywhere in the 9 emails (same root issue as the landing
  page review found pre-fix); added it in exactly two places (Email 1's
  open, Email 8's close before the deadline ask), not everywhere, same
  restraint logic as the landing page fix. On free/lapsed-pro: independently
  reached the same recommendation as round 3, fork Email 1's opening (and
  also suggests Email 8/9's close) rather than build a parallel sequence,
  not actioned in the redline, Karen's call. Full grading loop and final
  copy: `Round 1 - Marg x Chase x Expert Review.md`.
- Round 3 (`westretch-direct-response-marketing` skill) found the
  personalization line ("adapts as you progress and how you're feeling
  changes") repeated across Emails 2, 3, 4, and 5 violates voice.md's
  non-negotiable against claiming the app observes/learns the user;
  rewritten to the physiotherapist-mapped-schedule framing everywhere it
  appeared. Also flagged as a critical gap: no email in the sequence
  states the 28-Day Reset's price, billing, or refund terms anywhere,
  even though Emails 6-9 build real urgency toward a deadline to buy it
  `[VERIFY: price, billing terms, refund policy]`. On the free/lapsed-pro
  question: recommend forking only Email 1's opening beat for lapsed-pro
  (lead with their saved progress/history) rather than building a
  parallel sequence, since Emails 3-9 work for both audiences once past
  the opening awareness gap. Karen's call, not actioned in the redline.
- Round 2 ("Corey's version": product-marketing + copywriting,
  copy-editing, emails, marketing-psychology, offers, cro, ab-testing,
  churn-prevention, launch, lead-magnets, marketing-council, all from the
  vendored marketingskills pack) redlines Round 1's output, not the
  original. Complete. Biggest single finding: Round 1's cross-funnel fix
  for the "adapts... how you're feeling changes" mechanism overclaim
  (voice.md non-negotiable) said it covered Emails 2-5 and was fixed in
  every instance, but Email 6 still had a version of the same violation
  ("adapts as you progress") and Round 1's own notes incorrectly called
  that line already-accurate. Fixed in Round 2. Also fixed: Email 2 was
  the only early-arc email that never stated the October 19 start date,
  which was the exact "weak why-act-now" gap Marg's Round 1 notes flagged
  and Round 1 never resolved; two small intra-email word-repetition fixes
  (Email 1, Email 8); and the CTA on Emails 8-9 only, changed from "[JOIN
  THE 28-DAY RESET]" to "[JOIN BEFORE 5 PM]" so the real same-day deadline
  is on the button itself, a scoped disagreement with Round 1's deliberate
  choice not to touch the CTA anywhere (cro and marketing-psychology
  converged on this one; recommended as an A/B test against the control,
  not assumed). The free/lapsed-pro segmentation question is now a
  three-way independent convergence: Round 1 (Marg/Chase), Round 3
  (direct-response checklist), and Round 2's marketing-council session
  (Eugene Schwartz's awareness-stage framework) all separately land on
  "fork Email 1's opening for lapsed-pro." Still not actioned, same
  restraint as Rounds 1 and 3: it's a scope decision for Karen. The
  missing price/billing/guarantee gap Round 3 found is now also
  independently confirmed by the `offers` skill's Anatomy-of-a-Complete-
  Offer check and by the marketing-council's Hormozi seat (value
  equation). Full reasoning and final copy:
  `Round 2 - Corey's Version.md`.
- Redline PDF format, corrected 2026-09-22 per Karen's feedback: the
  generator originally rendered a changed paragraph as two full lines (old
  entirely struck through, new entirely underlined directly below). Karen
  wants word-level inline diffs instead, only the actual changed words
  marked, sitting in the same sentence, not a duplicate line. `tools/
  redline_pdf.py` now does this by default (word-tokenized `difflib` diff
  per paragraph, with a readability space inserted when a red span butts
  directly against a green span with no natural whitespace between them).
  All three PDFs regenerated from the existing round1/2/3_redline.json
  files, no need to re-run the underlying reviews when only the rendering
  changes. Future redline work in this repo should keep using this
  inline-diff behavior, it's the standing convention now, not a one-off.
- Known cosmetic wart, not yet fixed: some review-agent copy still
  contains literal markdown `**bold**`/`*italic*` asterisks (carried over
  from the Original draft's own markdown formatting) that render as literal
  asterisk characters in the PDF rather than actual bold/italic. Low
  priority, flagged to Karen, not fixed unless she asks.
