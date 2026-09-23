# Email Funnels (28 Day Challenge); CLAUDE.md

Scope: copy review for the 9-email 28-Day Reset Challenge promo funnel
(free users and lapsed-pro subscribers). Sibling to the landing page work
one level up in `28 Day Challenge/`, same campaign, different surface.
Read `Memory.md` alongside this file before revising this copy further.

## Where things live

- `28-Day Reset Challenge Email Funnel (Original).md`: the source draft as
  handed to CMO by Karen, transcribed verbatim from `Challenge Promo
  emails.pdf`. Kept for comparison, don't overwrite it.
- `Round 1 - Marg x Chase x Expert Review.md`: the `westretch-core` skill
  pass (Marg the real-user, Chase the behavior-change strategist, Expert
  the conversion strategist), same trio used on the landing page review.
- `28-Day Reset Challenge Email Funnel - Redline 1 (Marg x Chase x Expert).pdf`:
  redline of the original against Round 1's edits.
- `Round 2 - Corey's Version.md`: the `product-marketing` skill (run
  first, per that skill's own instruction to load before other marketing
  work) plus every applicable skill from the vendored Corey Haines
  marketingskills package (`.agents/skills/`, junctioned into
  `.claude/skills/` at repo root) reviewing Round 1's output and proposing
  further improvements.
- `28-Day Reset Challenge Email Funnel - Redline 2 (Corey's Version).pdf`:
  redline of Round 1's output against Round 2's edits (chained, not
  against the original).
- `Round 3 - Direct-Response Marketing Review.md`: the
  `Team/CMO/skills/westretch-direct-response-marketing` skill applied
  directly to the original draft (independent of rounds 1 and 2).
- `28-Day Reset Challenge Email Funnel - Redline 3 (Direct-Response Marketing).pdf`:
  redline of the original against Round 3's edits.
- `tools/redline_pdf.py`: shared generator. Takes a JSON file (old/new
  paragraph pairs per email) and renders a PDF with removed text struck
  through in red and replacement text underlined in green, in the same
  flowing document. Reused across all three rounds; see the docstring for
  the JSON schema.

## Status

All three review passes complete (2026-09-22), each producing its own
redlined PDF against the appropriate baseline (see above). Not yet applied
to a live send; next step is Karen's sign-off on which round's copy (or
which specific lines across rounds) to ship, plus two open decisions now
surfaced independently by all three rounds: whether to split Email 1
(round 1 also flags Email 8/9's close) by free vs. lapsed-pro segment, and
where to add the 28-Day Reset's price/billing/refund terms, which no email
currently states (see `WORK-TRACKER.md` and this folder's `Memory.md`).
Round 2's biggest catch: Email 6 still had the "adapts as you progress"
mechanism-language miss Round 1 said it had fixed funnel-wide across
Emails 2-5, and Round 1's own notes incorrectly called that line clean.
Fixed in Round 2's redline.
