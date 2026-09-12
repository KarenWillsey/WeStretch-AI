# Routine Screen Redesign: CXO Review

Owner: CXO. Started 2026-09-12. Skill applied: [UX Design Review](../../skills/ux-design-review/SKILL.md).

## Design objective

After two stretches, the user should understand the timer, progress, next pose and controls without an explanation. Ada's complete movement must remain visible from a practical stretching distance.

The ten images are alternative screen layouts for review. They are not validated interfaces or evidence that viewing-distance targets have been met.

## Source boundaries

- Karen's current request sets this project's scope and required controls.
- The supplied screenshots establish the current Ada character and unchanged 3D gym. Existing overlays are reference material, not requirements to preserve.
- The requested App Store reference supplies the caption gradient direction. App Store poster typography and dimensions do not set phone UI sizes.
- Use the [app skin](../App%20Design%20System/tokens/app-tokens.css) and shared [brand core](../../../CMO/In%20Progress/Brand%20System/core/tokens.css). Keep Inter, the gym environment and one Fire Red primary action.
- The [older routine spec](../Onboarding%20UX%20Flow%20Spec/Screens/Do%20Routine.md) contains unresolved assumptions. Do not copy its current-pose index into a field labelled completed, or treat its speed and completion rules as newly approved decisions.

## Shared information and proposed behavior

| Element | Requirement for every direction |
|---|---|
| Caption | Short current instruction on the requested gradient, with generous padding. Keep the text over a consistently dark area. Avoid animated caption placement. |
| Hold timer | Large stable numeral with an explicit hold/seconds label. Sample: 18 seconds. Keep its entire area outside Ada's movement bounds. |
| Pose count | Sample: 12 / 66 poses completed. This excludes an unfinished current pose. If every previous pose was completed, the current pose is number 13. |
| Routine progress | Match the completed count: 12 divided by 66 is approximately 18%. Use a bar, ring or track with the same meaning in every state. |
| Exit | Visible while running and paused. Never depend on a hidden menu or disappearing controls. |
| Pause / Resume | One persistent primary control in the same place. Pause freezes the model, countdown, captions and automatic pose transition. Resume continues that state. |
| Next pose | Clearly labelled preview with the upcoming pose's name. It does not imply a skip action. |
| Model speed | Initially offer Slower. Once reduced, show Slower, current speed and Faster together. Speed changes must visibly update the current speed. |

Proposed speed examples are 1x, 0.75x and 0.5x, bounded at normal speed and the slowest supported step. These illustrate the requested controls; the numeric steps are not confirmed product behavior.

The hold countdown should begin when the hold begins. During movement into a pose, use an explicit transition label rather than an unexplained zero. The label must reflect actual routine state.

Do not assume that slowing the model changes a prescribed hold duration. Confirm synchronization of motion, speech, captions and real elapsed seconds in Unity. No countdown or pose completion event should advance while paused.

Exit must stop the running presentation immediately. Its destination, partial-progress persistence and routine-credit rules need confirmation against Unity. Do not redefine the existing routine-completion threshold in this visual project.

## Accessibility and viewing distance

- Local minimums are 48 logical design pixels for touch targets and 16.5 for body text. For native implementation, use platform units: Apple recommends at least 44 points and Android at least 48dp. Exported PNG pixels are not native touch dimensions. [Apple](https://developer.apple.com/design/tips/), [Android](https://developer.android.com/guide/topics/ui/accessibility/views/apps-views)
- Start testing with captions at 22 to 26 logical pixels, timer numerals at 88 to 112, and control labels at 18 to 22. These are design hypotheses for a 390-wide reference screen, not proven distance requirements.
- Target at least 4.5:1 for normal text, 3:1 for qualifying large text, and 3:1 for essential control and progress indicators. Check actual text positions across the gradient and changing gym frames. [WCAG text contrast](https://www.w3.org/TR/WCAG22/#contrast-minimum), [non-text contrast](https://www.w3.org/TR/WCAG22/#non-text-contrast)
- White small labels on a red gradient need measurement. The brand recipe alone does not establish sufficient contrast.
- Keep body text and controls usable with text enlargement. Apple recommends supporting enlargement to at least 200 percent. [Apple accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
- Give controls text labels as well as icons. Progress must remain understandable without identifying red. Accessible labels should distinguish hold seconds, completed poses and model speed.
- Avoid announcing every countdown second through a screen reader. Preserve spoken movement guidance, and test useful announcements for pause, resume and speed changes.
- Review standing, side, wide-arm and floor poses through every camera angle. A timer clear of Ada in one still can cover her during a transition.

## Review the ten directions

Compare actual architecture: timer position and shape, progress placement, caption area, control grouping, Ada's available stage and portrait versus landscape. Color changes or mirrored controls alone do not make a new direction.

Prefer layouts with a dedicated model area and reserved timer space. Layouts with side rails or large dashboards need careful comparison because enlarging the timer can make Ada too small. Full-gym overlays need a movement-bounds test before selection.

Do not choose a winner from the static images alone. Select a direction to test, then preserve its information positions while checking the complete routine states.

## Acceptance test for the selected direction

1. Use a real phone at normal display scale. Record the phone size, brightness, lighting, stand height and distance. Start at 1 metre, then test 1.5 and 2 metres as exploratory distances.
2. Let a first-time participant follow two stretches without teaching the controls. Ask them to identify hold seconds, completed poses, routine progress and the upcoming pose.
3. Ask them to pause, resume, slow the model, slow it again and return toward normal speed. Ask them to find Exit. Each action should be found without hints; pause and exit must never be mistaken for one another.
4. Repeat with wide-arm and floor poses and during camera changes. Confirm that Ada's head, hands and feet stay visible and that the large timer can be read from the participant's stretching position.
5. Verify paused, resumed, first-pose, final-pose and slowest-speed states. Match count and progress to real completion events. Check caption wrapping and large-text settings.

Suggested lean first round: five participants. Treat any repeated misunderstanding, model obstruction or inability to read the timer as a revision trigger. This is a proposed test plan; no participant testing has happened yet.

## Open work

- [ ] Select the direction to develop from the ten images.
- [ ] Test comprehension after two stretches, viewing distance, floor poses and wide poses on real phones.
- [ ] Confirm Unity speed steps, hold timing, completed-count events, exit behavior and progress persistence.
