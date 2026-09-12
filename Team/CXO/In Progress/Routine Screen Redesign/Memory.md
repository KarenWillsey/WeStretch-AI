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

- [ ] Select the direction to develop from the ten images.
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
