# Round 02 Generation Prompt

Built-in image generation was used with three references: the current routine screenshot, Round 01 concept 06 and the App Store caption-gradient sample.

```text
Use case: ui-mockup.
Create one finished high-fidelity portrait mobile app screen, edge to edge, no phone bezel, no presentation board, no title outside the app.

Reference roles:
1. Current routine screenshot: authoritative Ada character, pose, clothing and existing 3D gym. Preserve the full gym view and Ada without covering her.
2. Round 01 concept 06: reference only for its circular routine-progress idea.
3. App Store image: reference only for the soft charcoal-to-transparent caption fade.

Direction: EXTREME MINIMALISM. Remove every unnecessary panel, card, label, heading, percentage, current-pose name, next-pose name, model-speed text and decorative border. Use symbols wherever possible. The only visible text or numbers should be:
- closed caption exact sample: "Tilt left. Rotate left."
- progress exact: "12 / 66"
- countdown exact: "18"

Top information strip only:
- A circular routine-progress ring on the LEFT, filled exactly 18.2 percent, with "12 / 66" centered inside. No percent sign and no word poses.
- The closed caption centered between the two circles. White Inter semibold over a smooth Midnight Grey charcoal-to-transparent gradient. The caption area is a fixed safe region that can support up to 178 characters. For this short sample, do not make it oversized. Show visually that the caption can wrap to four lines without moving either circle. Typography should scale dynamically within the fixed region: about 24px for short captions, reducing only as needed to a readable minimum for 178 characters.
- A simple large countdown on the RIGHT, visually balanced with the progress circle. Show "18" only inside a clean dark circle or open timer field. Do not add Hold, seconds, or seconds left.
- The progress circle, caption area and countdown must never overlap Ada's movement area.

Main screen:
- Existing 3D gym fills the screen.
- Ada remains the clear full-body focus with head, hands and feet visible.
- No other overlay on Ada.
- No current pose text and no next pose text.

Controls:
- A plain X icon at top-left safe corner for exit, outside the caption reading area.
- At bottom center, one simple circular Pause button using two vertical pause bars. No word Pause. Use the exact website CTA vertical gradient: #FC4850 at 0%, #FF5960 at 50%, #E22931 at 100%, with a slight shadow. Black pause icon for contrast.
- A small turtle icon button at bottom-left for slower. No text.
- A small next-pose thumbnail at bottom-right showing Ada in a T-pose, with no label and no button-like border.
- Keep all three bottom controls far below Ada's feet and visually quiet.

Color and style: Midnight Grey #1F1F1F, white, restrained grey, and the exact CTA gradient above. No bright red anywhere except progress fill and Pause. No gradients on secondary controls. No percent display. No repeated information. No added words. No large bottom dock. No side rails. No multiple cards. No new gym elements. No watermark.

The result must feel calm and almost empty, with maximum room for Ada.
```
