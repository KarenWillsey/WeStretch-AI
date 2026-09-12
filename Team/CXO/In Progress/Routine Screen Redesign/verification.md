# Round 01 Verification

Date: 2026-09-12. Scope: visual concept delivery, not product approval.

## Completed

- All ten final PNGs were visually inspected before being copied into Output/Round 01.
- Every final file decodes successfully. Ten unique SHA-256 hashes confirm no duplicated file deliveries.
- Nine portrait images and one landscape image are present.
- Each has readable hold/seconds wording, a completed-pose count, a routine-progress graphic, Exit, next-pose information and a primary Pause or Resume control.
- Large countdowns do not cover the active Ada in these stills. The sampled active model's head and feet remain visible.
- Progress graphics visually approximate 12/66. Exact fill geometry must be calculated by the app in implementation.
- Speed controls illustrate normal, 0.75x and 0.5x states. Concept 04's erroneous generated 1.5x label was corrected before delivery.
- Concept 03's hard caption boundary was replaced by a soft fade.
- Concept 06's countdown was enlarged and its progress header reduced.
- Concept 07's next-pose model was reduced so its arms and hands fit and it stays secondary to the active demonstration.
- Concept 08's countdown was enlarged, model speed labelled, and the next-pose box removed to avoid making it look like a button.
- Concept 10's caption gradient was strengthened.

## File dimensions

| Concept | Width | Height |
|---|---:|---:|
| 01 | 860 | 1828 |
| 02 | 860 | 1828 |
| 03 | 853 | 1844 |
| 04 | 861 | 1827 |
| 05 | 861 | 1827 |
| 06 | 853 | 1844 |
| 07 | 860 | 1828 |
| 08 | 850 | 1850 |
| 09 | 860 | 1828 |
| 10 | 1825 | 862 |

## Limits and next validation

- These images are generated approximations of the supplied gym, Ada and brand typography. They are not pixel-preserved Unity captures, and minor background/character/lettering variations must not become asset-change instructions.
- The contrast and text-size values in cxo.md are proposed implementation targets. No pixel-perfect font verification, dynamic contrast audit or native touch-target validation is claimed.
- Standing stills cannot prove clearance for wide-arm, seated, floor or rotating-camera views. Those checks are part of the tracked phone test.
- Static images do not implement pause, resume, exit, speed changes or completion events. The interaction behavior is specified in cxo.md and awaits Unity confirmation.
- No browser was connected in this session. Browser discovery returned an empty list. The offline gallery's source and local references were checked, but its browser rendering and clicks were not executed.
- Image generation stayed on the built-in tool. Exact original and refinement prompts are preserved in project JSON files.
