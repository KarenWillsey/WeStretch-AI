# Round 05: Routine controls
Date: 2026-09-30. Owner: CXO. Status: image review.

[Open visual gallery](review.html)

## Review set
- 4 speed states and 1 view after labels disappear.
- 16 individual full-screen pose-icon mockups.
- 4 pause-menu screens covering both CC states and all 3 audio states.
- Earlier rounds preserved.

## Requested behavior
- Speed cycles default speed > .75 speed > .50 speed > .25 speed > default speed.
- Show the selected speed underneath its button for 3 seconds following a speed press.
- Any button press shows `Next Up:` beneath the right circle for 3 seconds.
- After the labels disappear, all three controls remain visible.
- Pause reveals floating CC and audio buttons; the center control becomes Resume.
- CC cycles on/off. Audio cycles Audio on > Voice audio off > Mute > Audio on.
- Static images cannot demonstrate timing. These notes preserve the requested behavior for a later, separately authorized build.

## Visual decisions
- Playback reference: Round 03 / 04-calm-routine-icon-controls.png.
- Counter reference: Round 04 / 02-horizontal-divider.png.
- Captions raised into the upper edge region of the counter circles.
- Brand-white figures inside dark right-hand circles.
- Pose silhouettes follow the supplied images. Head fill and stroke weight vary slightly in generated previews.
- Existing gym and Ada remain the scene references. Small generative differences are not a request to change the real scene.

## Source mapping
[Original supplied ZIP](../../References/round-05-pose-icons.zip)

- [Pose 01 / Poses (1).png](pose-01.png)
- [Pose 02 / Poses (2).png](pose-02.png)
- [Pose 03 / Poses (3).png](pose-03.png)
- [Pose 04 / Poses (4).png](pose-04.png)
- [Pose 05 / Poses (5).png](pose-05.png)
- [Pose 06 / Poses (6).png](pose-06.png)
- [Pose 07 / Poses (7).png](pose-07.png)
- [Pose 08 / Poses (9).png](pose-08.png)
- [Pose 09 / Poses (10).png](pose-09.png)
- [Pose 10 / Poses (11).png](pose-10.png)
- [Pose 11 / Poses (12).png](pose-11.png)
- [Pose 12 / Poses (13).png](pose-12.png)
- [Pose 13 / Poses (14).png](pose-13.png)
- [Pose 14 / Poses (15).png](pose-14.png)
- [Pose 15 / Poses (16).png](pose-15.png)
- [Pose 16 / lower-body.png](pose-16.png)

The ZIP has no Poses (8). It contains Poses (1) through (7), Poses (9) through (16), and lower-body.png. All 16 are represented.

## Verification and limits
- Built-in imagegen edits. Exact prompts are in prompts.json.
- Inspected the speed and pause screens directly, and the pose screens in a contact sheet with enlarged icon details.
- Rejected white-fade pose renders and corrected the dark header/footer.
- Restored Exit X in pause screens after inspection.
- These are exploratory images, not final production assets. Exact caption alignment, consistent gauge geometry, menu positioning and original icon stroke fidelity need deterministic reproduction after a design is chosen.
- No UX app, Unity code, live controls or three-second timers were built.
- Approval is the next project decision, tracked in project Memory.md and root WORK-TRACKER.md.

