# Routine screen: critique and recommended revision

2026-09-13. CXO. Supersedes the Round 02 recommendation.

[View the revised screen](Output/Round%2003/01-calm-routine.png) | [178-character caption](Output/Round%2003/02-long-caption.png) | [Gallery](review.html)

## Decision

Use neutral Pause / Resume, one small progress ring containing X/Y, a large unframed countdown with a seconds unit, full-width captions, and three short control labels. Ada remains the main visual.

Karen's feedback is direct evidence: earlier screens were too busy; she requested minimal text; the red Pause felt like quitting. These are three comments from one reviewer, not a representative usability study.

## Skills and scope

Reviewed every available skill category for relevance. Applied the following lenses. Unrelated advertising, SEO, sales, pricing, spreadsheets, video and publishing workflows would add no useful evidence to this screen.

| Skill or source | Application |
|---|---|
| CXO ux-design-review | Hierarchy, clarity, consistency, access and tone |
| CXO customer-journey-audit | Start watching, stretch away from phone, glance, slow, pause, resume, exit |
| WeStretch core: Chase | Autonomy and attention strategy |
| WeStretch core: Expert | Remove visual competition and ambiguous microcopy |
| WeStretch core: Marg | Simulated customer critique and regrading |
| CPO user-research-synthesis | Separate Karen's evidence from untested hypotheses |
| Copy editing and its checklist | Seven sweeps applied to essential interface words |
| Brand core and app kit | Correct the mandatory red-button rule for playback |
| Imagegen | Generate and inspect the two revised visual states |
| CTO tech-architecture-review | Screened: no new architecture is needed; implementation risks documented below |

Marg, Chase and Expert are skill-based simulations. No actual customer panel or famous designer reviewed these files. Scores below are editorial judgments, not research results.

## Design principles applied

- **Dieter Rams:** make the tool understandable and unobtrusive. Here, remove the second ring and oversized red control so the demonstration leads. This is our application of his published principles. [Vitsoe](https://www.vitsoe.com/us/about/good-design)
- **Jakob Nielsen:** show state, preserve user control and prefer recognition over memory. Keep progress, pause state and Exit discoverable. [Usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
- **Aurora Harley:** an unfamiliar icon can require interpretation. Replace the turtle with Slower and label the thumbnail Next. Three useful words are preferable to three guesses. [Icon usability](https://www.nngroup.com/articles/icon-usability/)
- **Accessibility review:** specify at least 4.5:1 text contrast for ordinary text, 3:1 for qualifying large text and essential graphical controls. A changing gym requires a reliable backing surface behind text. This is a target, not a claim that generated artwork passes. [WCAG 2.2](https://www.w3.org/TR/WCAG22/)

## What fails in Round 02

| Priority | Problem | Consequence | Correction |
|---|---|---|---|
| Critical | Saturated red Pause dominates | Karen reads an invitation to stop the routine | Charcoal control, white pause bars and Pause label |
| High | Both counters use large circles | Two unrelated meanings look equivalent | One progress ring; plain 18s countdown |
| High | Captions squeezed between counters | 178 characters cannot reliably fit at readable size | Full-width caption row beneath fixed counters |
| High | Turtle alone | Requires learning an icon during exercise | Slower word control |
| High | Unlabelled next Ada on the floor | Can look like a second live demonstrator | Contained thumbnail labelled Next |
| High | No visible speed feedback | User cannot know whether slowdown worked | Show current rate and Slower / Faster after first change |
| Medium | Blank ceiling in short-caption view | Space appears unused | Reserve it for long captions and full-motion clearance, not more widgets |
| Medium | X is visually small | Visible mark does not guarantee easy touch | Minimum 48 logical-pixel hit area, away from playback |
| Medium | Colour treated as mandatory branding | Brand competes with current activity | At most one red CTA, no obligation to use one during playback |

## Chase strategy before the interface copy

FATE emphasis: Focus on Ada and the countdown; Emotion through calm presentation. Authority comes from the existing demonstration, not added badges. Tribe messaging is unnecessary during a stretch.

Identity: a person choosing their own pace. Six-Axis lens: support autonomy and clear understanding; do not infer psychological traits from appearance or exploit insecurity. The strategy fits a guided demonstration that needs little decision-making.

Five candidate approaches considered:

| Approach | Execution and hook | FATE / identity / Six-Axis emphasis | Ethical check and fit |
|---|---|---|---|
| Quiet guide, recommended | Calm playback and essential words | Focus, calm; capable self-direction; autonomy | No pressure; supports following Ada |
| Pure symbols | Remove all labels | Focus; experienced user; familiarity assumed | Too much guessing for a new user |
| Timer first | Enlarge countdown further | Focus; time-aware; clarity | Useful at distance but risks displacing Ada |
| Caption first | Large instruction panel | Authority through guidance; supported; understanding | Good for long cues, but preserve body clearance |
| Progress first | Large ring and completion emphasis | Emotion; continuing participant; accomplishment | Can turn exercise into a scoreboard; not appropriate here |

## Marg and Expert review loop

Steps run: Chase (strategy) OK, Expert (copy) OK, Marg (grading) OK.

Attention means keeping attention on Ada. Act means confidently controlling the routine, not conversion. Scale uses the skill's grade values. Three evaluations, two revision passes.

| Evaluation | Attention | Speak to me | Believe | Act | Honest | Average / nearest grade |
|---|---|---|---|---|---|---|
| Round 02 baseline | B, 3.0 | B, 3.0 | A, 4.0 | B, 3.0 | A, 4.0 | 3.40 / B+ |
| Quiet controls draft | A-, 3.7 | A-, 3.7 | A, 4.0 | B+, 3.3 | A, 4.0 | 3.74 / A- |
| Final visual and behavior specification | A-, 3.7 | A-, 3.7 | A, 4.0 | A-, 3.7 | A, 4.0 | 3.82 / A- |

- **Baseline Marg simulation:** the red button pulls attention away from stretching; the turtle and second figure require interpretation. Expert removes red playback, uses seconds and three labels.
- **Draft Marg simulation:** quieter, but the long caption becomes small and speed state is unspecified. Expert gives captions a full row, enlarges the long-caption sample and specifies speed feedback.
- **Final Marg simulation:** controls are easier to explain and the two counters have distinct shapes. A static image cannot establish legibility at distance, motion clearance or comprehension. Stop at this honest ceiling.

No A+ claim. Raising an editorial score cannot replace testing. The visual alone does not demonstrate the specified interactions.

## Final interface and behavior

| Element | Specification |
|---|---|
| Progress | 64 logical-pixel ring starting at 12 o'clock. X/Y centered. Fill = completed / total. At 12/66 the current unfinished pose is the 13th, not the 12th. No second percentage. |
| Countdown | Plain white tabular numerals, proposed 64px at 390px viewport, with smaller s. Counts hold seconds; never overlays the body. |
| Caption | Full width below counters. Proposed 22px, minimum 20px for this routine view, approximately 26px line height. Preserve all supplied words. Use an opaque-enough charcoal backing under text and fade only beyond it. |
| Pause | Neutral charcoal, white bars, Pause label; 56px control with minimum 48px hit area. Same location becomes play icon and Resume. |
| Slower | Initially a 48px-high word control. After first change, show Slower, current rate and Faster in a quiet expanded speed row above the bottom controls. Reserve space so it never covers Ada. |
| Next | Small contained pose thumbnail with Next. Not a second live person in the gym. Announce next pose name to assistive technology. |
| Exit | White X, at least 48px target in safe area, separate from Pause. Accessible name Exit routine. Available in every state. |
| Colours | Existing Fire Red remains #FC4850. Website CTA gradient remains #FC4850 / #FF5960 / #E22931. Pause and Resume do not use it. |

Speed examples: 1x, 0.75x, 0.5x are proposals pending Unity confirmation. Faster restores toward normal speed; do not imply faster-than-normal is supported. At limits disable the unavailable action while keeping its place stable. Slowdown should affect model movement without silently changing prescribed hold duration; confirm engine behavior before implementation.

Pause must freeze the relevant model, hold clock and synchronized audio/caption playback together. Resume continues the same state. Preserve progress during a pause. Exit behavior and credit persistence must use verified existing rules, not promises invented in the mockup.

Accessible labels: 12 of 66 poses completed; 18 seconds remaining; Pause routine; Resume routine; Slow model down; Speed model up; Exit routine; Next pose, followed by its name. Do not announce every countdown tick. Announce meaningful changes without interrupting instructions.

## Long-caption constraint

The supplied maximum is 178 characters. The delivered test text is exactly 178 characters including spaces and punctuation:

> Follow Ada through this movement at your speed. Watch the position of her arms and feet as she moves, then hold the position until the countdown reaches the end of this movement.

This is a typography test fixture, not approved coaching copy.

A 390px screen with 24px margins provides 342px for text. Flanking it with two 64px counters and two 12px gaps leaves only 190px. This is why the recommendation moves captions beneath the counters.

Fit complete cues by measured rendered width and height, not character-count thresholds. Start at the preferred size, then reduce only to the defined minimum. Never truncate, scroll away unseen words or continually resize during a cue. Support system text scaling. Longer translations may exceed the English test fixture.

Reserve a caption-safe region before starting the routine, based on the actual cue set and text scale. Where that region leaves inadequate demonstration space, use a dedicated caption band and reframe the existing gym viewport. Do not shrink Ada beyond tested visibility or allow text over her. This is a layout change, not a change to the gym asset.

The long image shows six lines close to Ada's hair. Production needs a larger guaranteed clearance envelope for raised arms and changing camera views. Exact 178-character fit on every device remains unverified.

## Journey and implementation

The user starts the routine, sets the phone down, follows Ada, glances at remaining hold time, checks Next, approaches the phone to change speed, pauses, resumes or exits. Quick wins: neutral playback, distinct counter shapes, labels. Structural work: caption layout measurement, synchronized state, safe framing through all poses.

Reuse the current Unity screen and assets with revised overlay components. A native overlay rewrite would add synchronization and maintenance work without evidence it is needed. A new rendering system is disproportionate. Cost and schedule cannot be estimated credibly without inspecting the current Unity implementation.

No additional tracking is required for this design. Keep touch controls available without time-based hiding. Render the ring from numeric completion events, not timer interpolation.

## Copy-editing pass

Clarity: Slower, Pause, Next and s. Voice: calm and direct. So what: each word identifies a control or status. Proof: no outcome claims. Specificity: completed count and seconds are distinct. Emotion: remove visual pressure. Zero risk: clear Pause / Resume and Exit, with no sales reassurance or retention friction.

## Verification and remaining evidence

- Inspected both delivered images: neutral Pause, one progress ring, seconds unit, three labels, full body visible in the pictured pose.
- Rejected the first long-caption draft: it had 177 characters and undersized type. Corrected fixture is 178 characters and the delivered image shows its complete text in six lines.
- Generated assets preserve the gym direction, but are not pixel-identical Unity frames. Existing gym assets remain mandatory.
- Image typography, target dimensions and gradient contrast are illustrative. Native layout and dynamic font fitting are specified, not implemented.
- Test on actual supported phones at normal and enlarged text sizes, from the user's chosen standing and floor distances.
- After two stretches, ask people to explain both counters, identify Next, slow and restore speed, pause/resume and exit. Record confusion and mistaken exits. Do not claim success until observed.
- Check maximum caption, translations, notch safe areas, raised arms, wide poses and floor poses in motion. Validate 48px targets and contrast against every background state.
- Existing project open items cover direction review, phone comprehension and Unity timing. No claim of user-tested optimization.
