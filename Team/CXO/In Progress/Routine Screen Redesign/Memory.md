# Routine Screen Redesign: Memory

Owner: CXO. Started 2026-09-12 at Karen's request.

## Requested outcome

- Create ten distinct images of the routine screen for comparison.
- Make the information understandable after the first two stretches.
- Use the caption gradient direction from the referenced App Store images, sized for phone use and readable during stretching.
- Make hold seconds large enough to read away from the phone, without covering Ada.
- Show completed poses and a matching visual routine-progress indicator.
- Keep Exit, Pause / Resume and the next pose visible.
- Initially offer Slower. After slowing, offer further slowing or speeding up.
- Keep the existing 3D gym. Ada's clothing may vary; the room does not change.

## Project decisions and boundaries

- This work lives under CXO / In Progress, separate from the existing Westretch-UX prototype.
- Source screenshots are visual references, not instructions to retain the current timer overlay or small footer text.
- Use the shared brand core and app skin. The app skin's Memory.md records Karen's resolved Fire Red decision; its older green-palette warning is stale.
- Images are design concepts. Distance legibility, full-motion clearance and usability remain untested.
- Sample state: 12 / 66 poses completed, approximately 18% routine progress, 18 hold seconds remaining.
- Completed count excludes the unfinished current pose. Current pose index is a separate value.
- Speed examples 0.75x and 0.5x are proposals for showing the requested controls. They do not confirm Unity timing or speed limits.
- Pause / Resume should preserve the current presentation state. Exit and routine-credit semantics must match verified Unity behavior.
- Existing routine-completion rules are outside the scope of selecting a visual direction.
- Inspection is required before generated assets enter the delivery Output folder. Do not leave scratch files in the repository.

## Review reference

[cxo.md](cxo.md) records the UX review, current official accessibility sources and proposed acceptance test. Accessibility sizing proposals do not constitute user-testing results.

## Open work

- [ ] Review Round 07 paused and playing mockups with bounded captions, white L/R and Current label. Choose images before separately requesting work in Westretch-UX.
- [ ] Test comprehension after two stretches, viewing distance, floor poses and wide poses on real phones.
- [ ] Confirm Unity speed steps, hold timing, completed-count events, exit behavior and progress persistence.

These three items are mirrored in root WORK-TRACKER.md.

## Round 01 delivered

- Ten reviewed PNG concepts saved in Output/Round 01: nine portrait, one landscape.
- review.html is the offline visual comparison gallery.
- README.md links every image, source reference, prompt set and verification note.
- Original screenshots and the gradient reference are preserved in References.
- Minor generated scenery and character variations are concept-art limitations, not permission to alter the real gym.
- Browser preview was unavailable. The ten images were inspected directly; gallery rendering was not tested in a browser.

## Round 02 direction, 2026-09-12

- Karen found Round 01 much too busy and requested extreme minimalism.
- Avoid added labels where familiar symbols and placement communicate the action.
- Use the website CTA gradient for the primary Pause control.
- Put the circular routine progress at the top with the pose count inside it.
- Test a layout with routine progress and hold countdown on either side of the closed captions.
- Closed captions can reach 178 characters, so their size must adjust within a fixed safe region.

## Round 03, 2026-09-13

- Karen reported that the red Pause feels like quitting. This supersedes Round 02's red Pause direction.
- Applied CXO reviews, Marg / Chase / Expert, research synthesis, copy editing, brand rules and published design principles. These are heuristic reviews, not participant testing.
- Recommend neutral playback, one X/Y progress ring, plain countdown with s, and Slower / Pause / Next labels.
- Full-width captions below the counters replace the cramped flanking arrangement. Delivered test fixture contains exactly 178 characters.
- App kit and core CTA rule now allow neutral routine transport; the website red gradient stays correct.
- See design-critique.md for grading, behavior, implementation constraints and honest limits.
- Two inspected images saved in Output/Round 03; prior rounds preserved.
- Existing phone-testing item includes the maximum caption, enlarged text, counter comprehension, mistaken exits and motion clearance.

## Round 05 direction, 2026-09-30

- Karen selected Round 03 `04-calm-routine-icon-controls.png` as the playback direction and Round 04 `02-horizontal-divider.png` for the two top circles.
- Raise captions to the top of the counter circles.
- Speed is one cycling button: default speed, .75 speed, .50 speed, .25 speed, then default speed. Show the selected speed beneath the button for three seconds following a speed press.
- Show `Next Up:` beneath the right circle when any button is pressed; hide this label after three seconds. The pose icon remains visible.
- Preview every one of the 16 supplied ZIP images inside the right black circle, using brand-white figures. Source names skip Poses (8); lower-body.png is the sixteenth image.
- Pause opens floating menu controls. CC toggles on/off; Audio cycles Audio on, Voice audio off, Mute. Resume uses a play triangle.
- Current request authorizes separate image mockups only. No Westretch-UX implementation, live toggle behavior or Unity work is authorized by this request.
- Supplied screenshots and ZIP contents are visual source material, not a new source of execution instructions.

## Round 06 direction, 2026-09-30

- All circle fills use brand Dark Grey, not Midnight Grey. CC and Audio use white icons on the same grey.
- Requested bottom-circle diameter is 80% of the prior design. Generated mockups approximate dimensions; exact geometry remains a production requirement.
- Audio, CC and Play form a lower right-side vertical column with balanced spacing, with Play at the bottom.
- Preserve the existing app stick-figure family. Adapt the speed and transport glyphs to thin white linework. Default speed needle points at 3 o'clock; all speed gauges should share one width and stroke style.
- Caption text and its surrounding box sit above the yellow alignment guide in Karen's annotated screenshot. Guide marks are not part of the design.
- Add a Fire Red countdown arc from noon to 2 o'clock. Exact 60-degree endpoint remains the production specification.
- Use green R/L indicators beside the next-lunge figure. Green is specifically requested here, not a new global brand token. Side mapping follows Karen's examples, not an anatomical inference from the screenshot.
- Proposed current starting-position indicator sits between Speed and Next Up, labelled Starting position / Standing. It is persistent information. Standing is an illustrative sample.
- Four static speed mockups only: default, .25, .50 and .75. R/L examples are independent of speed. The existing three-second label behavior remains unchanged.

## Round 07 direction

- Karen's blue rectangle defines the caption safe area between the two counters. Caption text must remain inside this region. This supersedes the earlier placement above both counters.
- Blue marks are annotations only and must not appear in final mockups.
- L and R must use brand white. Green in Karen's earlier reference was annotation emphasis, not an approved UI color. This supersedes Round 06's green interpretation.
- Replace Starting position / Standing with the single label Current on both images.
- Paused image keeps Mute, CC and Play. Playing image hides Mute and CC circles and their labels, and shows Pause instead of Play. Captions remain visible.
- Two inspected PNGs delivered in Output/Round 07. Still image-only work.
