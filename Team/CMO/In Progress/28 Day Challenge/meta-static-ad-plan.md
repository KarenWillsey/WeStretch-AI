# Reset Challenge: Static Ad Build And Test Plan

**Plan dated 5 October 2026. Subsequently approved for production by Karen.**

**Production update:** Karen required CMO female-actor or male-actor skills for image production. The nine-image first batch is complete: [open the deliverables](Static%20Ads/README.md). The proposal below is retained as the production brief; its planning-stage pause and source gaps have been resolved. Campaign launch dependencies remain open.

## Recommended decision

Build **three concepts in three sizes: nine final images**. Launch three ads, each with its own placement-specific images. The three sizes are adaptations, not separate creative hypotheses.

Use the expert's three everyday frustrations, with the proposed copy below. Keep one consistent design system. After results, test **two challengers against the strongest original**. That means five creative versions over two rounds, not five versions of each concept.

Approve the words, source photos and layout rules together before production. Store them in an editable template so later improvements replace a field rather than rebuild an ad. One production system is achievable; knowing the winning message before testing is not.

## What informed this plan

- Karen's supplied expert brief is the creative starting point.
- `westretch-core` and the authoritative brand voice govern all proposed copy. **WS_CORE_SKILL_USED.**
- `marketing-plan` was read first as requested. It routes single-channel work to `ads`; its full 12-month marketing-plan workflow is outside this request.
- `ads`, `ad-creative` and `westretch-direct-response-marketing` inform the test structure, copy hierarchy and landing-page connection. Generic skill suggestions about fear, age labels, fabricated testimonials, high-volume production or guaranteed gains do not override WeStretch rules.
- The existing Reset landing-page copy specifies 28 days, 15 minutes daily, October 19 to November 15, and a monthly or annual subscription. These are recorded campaign facts, subject to confirmation before launch. This is not an assumed free challenge or the separate 30-day trial campaign.
- The older 25-concept Meta batch is a separate project. It is not evidence of performance. No account performance export was examined for this plan.

## Proposed copy for approval

These are proposed changes, not silent replacements of the expert's wording. All three retain the exact requested on-image CTA: **JOIN THE RESET CHALLENGE**.

Put **28-DAY RESET CHALLENGE** in a small, readable campaign label on every image. It must remain secondary to the headline.

| ID | Concept | Proposed on-image headline | Supporting copy | Hypothesis |
|---|---|---|---|---|
| R01 | Slept Wrong | Another morning of “slept wrong.” | Start the day with guided stretching. | A familiar morning expression earns recognition quickly. |
| R02 | Stiff, Sore + Tight | Less working around stiffness. More getting on with the day. | 28 days of guided stretching, one day at a time. | An everyday-life benefit is more inviting than a list of symptoms. |
| R03 | There's Always Something | Getting out of the car shouldn't be the hard part. | Make time for movement with the 28-Day Reset. | A specific daily moment outperforms a broad symptom list. |

**Why change the originals:**

- R01: remove “Sick of” and the direct assertion about the viewer's body. Keep the recognizable “slept wrong” language without framing it as a customer quotation.
- R02: reduce generic “this is for you” language and avoid presenting improved health in 28 days as a promised result. “Less working around” expresses the desired direction, not a guaranteed outcome.
- R03: replace three stacked discomfort claims with one filmable moment. This is the largest creative change and specifically needs Karen's agreement. A car-exit photo must support it.
- The original “Your back is stiff. Your hips are tight” also raises personal-attribute review concerns. Removing “your” alone is not a guarantee of platform approval. Judge the whole ad, image and destination together.

### Common text outside the image

Keep this identical across the first three ads so the creative package is the main variable.

**Primary text:**

> Join the 28-Day Reset Challenge with WeStretch. Follow guided, physio-informed stretching for 15 minutes a day and see what feels different. A WeStretch subscription is required.

**Meta headline:** Join the 28-Day Reset Challenge

**Optional description:** 15 minutes a day for 28 days

**Native Meta button:** Learn More, if available for the chosen setup. The printed image CTA remains JOIN THE RESET CHALLENGE. The click leads to the challenge landing page, where people can understand the offer before choosing a plan.

Preview truncation in each placement. Essential information must not depend on the optional description displaying. Dates and prizes stay off the images in this first batch. This reduces clutter and avoids locking artwork to unconfirmed campaign details.

## Visual direction and source selection

One natural photo, a large headline, short support, the original logo and a clear red CTA. A warm, ordinary setting should make the situation recognizable. Avoid pain grimaces, symptom diagrams, before-and-after comparisons, medical props added for persuasion, decorative stickers and staged exuberance.

| Concept | Photo direction | Existing source status |
|---|---|---|
| R01 | Morning at home, comfortable clothing, relaxed expression | `Image Catalogue/female-actor-02-standing-side-bend-scandinavian-bedroom.png` was visually inspected. It is an approved-catalogue candidate showing a bedroom stretch. The raised hand needs generous clearance; use a separate text panel rather than covering the pose. |
| R02 | An accessible stretch in an ordinary room | `Image Catalogue/female-actor-03-seated-forward-fold-living-room.png` is a catalogue candidate. The image viewer failed to load it in this session, so visual suitability remains unverified. |
| R03 | Getting out of a parked car, calm expression, complete and believable action | No exact car-exit image selected. Search the approved catalogue first. If none fits, propose one reference-locked shot using an existing WeStretch actor. Do not substitute an unrelated stretching photo under a car headline. |

Paths above are relative to `Team/CMO/`. The catalogue is the approved source archive. The newer Reset landing-page photos in `Review ToDo/` remain pending sign-off according to project memory; do not silently treat them as approved.

Before generation, inspect the shortlisted sources at full size and record exact paths, dimensions and approval status in a source manifest. Avoid low-resolution blog thumbnails. Keep the existing actor identity, clothing and expression rules. New photos use the selected actor's own skill and canonical reference, not a text-only approximation of that person.

### Layout rules

- Work Sans Bold for headlines; Inter for support and CTA. Use the brand tokens and original logo assets, with logo clearance equal to the logo's `w` width.
- Use Midnight Grey and white for the main text contrast, with Fire Red for the primary CTA. Typography and logo remain editable, separate from the photograph.
- Start with a simple solid text area beside or above the photograph. Use an overlay only where readability stays strong without darkening the person's face.
- Target headline size around 72 to 96 px and support around 42 to 48 px on a 1080-wide canvas. These are starting estimates, not existing brand requirements. Check at 360 px display width and revise the layout before shrinking the words.
- Keep the full action understandable, intentional line breaks and breathing room around hands, faces and text. Consistent hierarchy matters more than identical coordinates across formats.

| Export | Composition | Essential-content boundary |
|---|---|---|
| 1080 x 1350 | Lead design. Headline first, photo and CTA balanced below or alongside | Use a generous inset; inspect at phone feed size. |
| 1080 x 1080 | Reflow the headline and rebalance the photo area | Brand system requires an 8% inset, approximately 87 px. |
| 1080 x 1920 | Recompose vertically with the message, logo and CTA in the central area | Proposed conservative working box: x = 90 to 990, y = 280 to 1200. Background may extend beyond it. |

The repo's existing vertical minimum is 250 px clear at top and 350 px at bottom. The tighter central box above is a proposed production precaution for placement interfaces, not a claim that one universal Meta safe zone has been verified. Check current Stories and eligible Reels previews in Ads Manager before export approval. If a placement needs more clearance, reflow it. Confirm static eligibility for the actual campaign setup.

## Tools and production sequence

| Step | Repo skill or tool | Concrete output after approval |
|---|---|---|
| 1. Lock brief | This plan, `westretch-core`, `ad-creative` | Approved copy manifest, three photo selections, objective and destination |
| 2. Fill photo gaps only | Relevant existing actor skill; available image-generation/editing tool | Reference-locked source photo, only if the approved catalogue cannot supply it |
| 3. Recover crop room if needed | `create-4k-crop-master` | Reviewed text-free master preserving identity and action |
| 4. Compose | Local editable HTML/CSS or SVG using brand tokens and real font files | Three responsive-to-format layout templates, not AI-painted lettering |
| 5. Inspect | Browser render, image inspection and phone-size previews | Contact sheet plus full-resolution checks across all nine outputs |
| 6. Package | Deterministic export and manifest | Nine exact-size PNGs, editable sources, copy sheet and handoff notes |
| 7. Launch and learn | Meta expert using Ads Manager | Placement previews, verified conversion events and dated results sheet |

These are proposed future steps. No renderer or ad assets were built in this planning session. Work Sans Bold was not located in the repository font search; obtain the correct font and verify rendering before composition. Inter assets exist. Do not substitute Inter for the display face. Higgsfield skills are available as an optional photo-production route, but no paid generation or connection is needed to reuse approved photography.

Work in a staging area. Only visually checked files go into the final `Output/` folder. Save editable text, source-image links, crop coordinates, approved copy and version IDs so a later wording change is repeatable.

Suggested filenames: `reset-r01-v01-1080x1350.png`, with matching `1080x1080` and `1080x1920` files. Use R02 and R03 for the other concepts.

## Test plan

**Primary decision:** which creative package brings suitable people into the paid Reset offer at an acceptable acquisition cost?

### Round 1: three creative packages

- Three concepts, one version each, three sizes each. Nine exports and three ads.
- Keep destination, primary text, offer, native CTA, eligible audience and attribution settings consistent. Adaptation by placement is allowed.
- The headline and scene differ together. This is a concept test, so results cannot isolate whether words or photography caused the difference.
- Use the Meta expert's existing account structure. With a small budget, keep the test consolidated rather than creating nine competing ad sets.
- Normal delivery can allocate spend unevenly. Low delivery means insufficient evidence, not that a concept failed. If causal comparison matters and budget permits, use Meta's controlled A/B testing tools with a single variable.
- Review automatic creative enhancements before launch. Preserve approved copy, crops and identities; do not let unreviewed rewrites or expansion confound this test.

### Round 2: strongest original plus two challengers

- Keep the strongest original as control.
- Challenger A changes only its headline toward the strongest customer-language insight from results or comments.
- Challenger B changes only its photograph or text placement, keeping the control copy.
- Produce each challenger in all three sizes: six additional exports only after learning. Total across both rounds: five versions, fifteen images.
- If spend supports only one comparison, test one challenger against the control and save the other.

### Budget and evidence

Budget, historical paid-conversion CPA and acceptable acquisition cost are unknown. Three initial concepts is a lean production recommendation, not a statistical sample-size claim.

Before launch, the Meta expert sets the spend cap, target CPA, conversion event, attribution window and review date. For planning only, three concepts with a directional allowance of five target-CPA multiples each would require `15 x target CPA` total. If target CPA were $30 in the account currency, that is $450. This is an illustrative spend envelope, not a sufficient-sample guarantee or approved budget. Actual comparisons require enough conversions for the intended decision.

Allow approximately one full week for the first read if the confirmed launch date permits, without frequent edits. Account for conversion reporting delay. If the October 19 start is unchanged, approve and produce promptly; do not force two rounds into the calendar or call a low-volume result conclusive.

### Measurement and decisions

| Signal | Use |
|---|---|
| Completed paid joins or validated subscription purchase event, CPA | Primary acquisition decision if this is the verified checkout flow |
| Trial start and later paid conversion | Use separately if checkout actually starts a trial; never label a trial as a paid join |
| Outbound CTR, outbound CPC, landing-page views | Diagnose attention and click-to-page problems |
| Checkout starts and page-to-purchase rate | Identify offer or destination friction |
| First routine, cancellations and refunds where available | Check whether acquired users are a useful fit |

Use a neutral UTM identifier such as `utm_content=r01_v01`; do not place inferred health information in URLs or conversion payloads. Verify browser/server deduplication if both event sources are used, and check the full checkout path before spending.

**Keep** an economically promising ad with acceptable conversion quality. **Iterate** an attention winner with weak conversion only after checking message match and checkout. **Stop** after the agreed spend limit and reporting delay if results are uneconomic. **Hold judgment** when delivery or conversion volume is too low. Never scale on clicks alone or claim an A+ copy score proves sales performance.

## Quality gate before delivery

- Every word matches the approved copy manifest, including punctuation and CTA.
- Each concept passes the WeStretch core review independently. No age labels, shame, learned-body claims, guaranteed outcomes, invented testimonials or em dashes.
- Actual Work Sans Bold and Inter render; no fallback fonts, overlap or clipped text.
- Photos preserve actor identity, plausible anatomy and a natural expression. Logo is an original asset.
- All nine files have the exact requested dimensions and are checked individually at full resolution and phone size.
- Essential content survives the actual placement overlays. Square and vertical layouts are recomposed, not automatic crops of the portrait ad.
- Landing page continues the Reset offer, works on mobile and has correct dates, subscription terms, checkout and confirmation.
- Deliver a contact sheet, editable sources, nine PNGs, copy sheet and a concise launch manifest. No draft or rejected asset enters `Output/`.

## Decisions to settle before production

1. **Karen:** approve the three proposed headlines and supporting lines, especially R03's car-exit interpretation, or retain a different everyday moment.
2. **Karen:** confirm the suggested existing models and photo direction. A matching approved R03 source is still needed or must be generated.
3. **Meta expert:** supply the test budget, target CPA, recent relevant results if available, audience/geography and intended conversion event. These govern launch breadth, not whether this plan can be approved.
4. **Campaign owner:** confirm October 19 to November 15, year, subscription/trial terms and final landing-page URL. Existing tracker already records landing-page approval, checkout-link and confirmation-page work. Resolve these before paid traffic.

**Pause here.** Karen explicitly requested a plan and a pause before building. Approval of this plan authorizes the agreed production scope, not ad spend or publishing.

## WeStretch core review record

Steps run: Chase (strategy) OK, Expert (copy) OK, Marg (grading) OK.

These are simulated editorial personas, not independent customer research. One revision cycle, two grading passes. Scores assess copy only; visual grading waits for finished layouts.

### Chase strategy

**FATE:** Focus on a recognizable moment; Authority through the factual physio-informed process in primary text; Tribe through familiar people and ordinary homes; Emotion through relief and capability, without escalating discomfort.

**Identity:** someone who makes room for everyday movement. No identity based on age, illness or failure.

**Six-Axis read:** assume low initial focus and cautious openness. Suggestibility is unknown and not exploited. Build connection with a recognizable scene; build expectancy around a clear routine, not guaranteed relief. Ask for a page visit before purchase compliance. These are planning assumptions, not measured audience traits.

The three routes test morning recognition, life beyond stiffness, and a specific daily action. Use the user's three-route scope rather than adding five unrelated strategies.

### Pass 1: supplied image-copy packages

| Piece | Attention | Speak to me | Believe | Act | Honest | Average | Grade |
|---|---|---|---|---|---|---|---|
| R01 original | A 4.0 | A 4.0 | B 3.0 | B+ 3.3 | A- 3.7 | 3.60 | A- |
| R02 original | B+ 3.3 | B+ 3.3 | B 3.0 | B+ 3.3 | A- 3.7 | 3.32 | B+ |
| R03 original | A 4.0 | A- 3.7 | B 3.0 | B 3.0 | B+ 3.3 | 3.40 | B+ |

Marg's main reactions: R01 recognizes a moment but tells me how I feel; R02 could be almost any wellness offer and implies an outcome; R03 piles on problems and “Let's work on that” does not explain the next step. Expert's changes are recorded with each proposed concept above.

### Pass 2: proposed image packages and common Meta text

| Piece | Attention | Speak to me | Believe | Act | Honest | Average | Grade |
|---|---|---|---|---|---|---|---|
| R01 proposed | A 4.0 | A 4.0 | A 4.0 | A- 3.7 | A+ 4.3 | 4.00 | A |
| R02 proposed | A- 3.7 | A- 3.7 | A 4.0 | A- 3.7 | A+ 4.3 | 3.88 | A- |
| R03 proposed | A 4.0 | A 4.0 | A 4.0 | A- 3.7 | A+ 4.3 | 4.00 | A |
| Common Meta text | A- 3.7 | A- 3.7 | A+ 4.3 | A- 3.7 | A+ 4.3 | 3.94 | A- |

Honest ceilings: R02 remains broader than a single scene. The common text is deliberately explanatory. Action scores stop short of A+ because neither verified outcome proof nor account results were supplied; adding urgency or guaranteed relief to raise the grade would break the guardrail. R03 depends on a matching photo. Do not certify the unbuilt ads as A+.

### Sources and verification limits

- Local authority: [voice](../Brand%20System/core/voice.md), [positioning](../Brand%20System/core/positioning.md), [tokens](../Brand%20System/core/tokens.css), [formats](../Brand%20System/marketing/formats.md), [core skill](../../skills/westretch-core/SKILL.md), and [Reset landing-page copy](28-Day%20Reset%20Challenge%20Landing%20Page%20%28Final%20Copy%29.md).
- Meta provides education on using A/B tests and metrics for creative decisions: [Meta Blueprint: Measure the impact of your ad creative](https://www.facebookblueprint.com/student/path/253050-ad-creative-testing-course).
- Meta emphasizes safe-zone composition for Reels: [Meta Reels ads](https://www.facebook.com/business/ads/facebook-instagram-reels-ads). Its video performance figures are not evidence that these static ads will perform similarly.
- Current detailed policy/specification pages could not be read without rate-limit or login blocks on October 5: [personal attributes](https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/), [safe zones](https://www.facebook.com/business/help/980593475366490), [Stories image guide](https://www.facebook.com/business/ads-guide/update/image/instagram-story). Treat the copy and safe-box choices as conservative recommendations; the Meta expert must verify the current placement and policy details in the account before launch.
