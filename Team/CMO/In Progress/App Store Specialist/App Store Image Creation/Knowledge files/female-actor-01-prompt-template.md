# Female Actor 01: Pose-Only Prompt Template

Canonical identity reference: `female-actor-01-reference.png`

Use the reference image with every generation. This is an identity-preserving
image-to-image prompt, not a text-only character description. A prompt alone
cannot reliably reproduce the actor without the attached reference.

## Single input

Replace only `{{POSE}}`. Describe one physically visible pose, including limb
placement, hand placement, torso direction, head direction and any support or
contact with the floor. Do not add scene, wardrobe, lighting or styling
instructions to the pose input.

## Prompt template

```text
Use the attached female-actor-01-reference.png as the canonical identity
reference for FEMALE ACTOR 01.

This is an identity-preserving pose change, not a redesign and not a new
lookalike. Create a new photorealistic lifestyle photograph of the exact same
woman performing this pose:

{{POSE}}

IDENTITY LOCK: preserve from the reference:
- The same recognizable facial structure, facial proportions and natural
  mature features.
- The same apparent age: a healthy, relatable woman approximately 55–65.
- The same natural light complexion and realistic mature skin texture.
- The same short, chin-length salt-and-pepper grey hair, softly side-parted
  with natural volume and darker strands underneath.
- The same average, naturally fit body type and realistic proportions.
- No rejuvenation, glamour retouching, face reshaping or artificial skin.
- Do not invent a specific eye colour; follow the identity reference.

WARDROBE LOCK: reproduce the reference outfit without changes:
- Muted sage-green, short-sleeve crew-neck T-shirt with soft natural fabric.
- Loose charcoal-grey stretch pants.
- Bare feet.
- No visible brand marks, jewellery or added accessories.

SCENE LOCK:
- The same warm, calm, upscale but believable living-room environment.
- Beige walls, white crown moulding, warm hardwood floor and a large
  cream-textured rug.
- Bright multi-pane window on camera-left with sheer beige curtains and soft
  daylight.
- Neutral taupe sofa, restrained wooden side tables, leafy green houseplants
  and one subtle framed landscape.
- Keep the room clean, comfortable and lived-in; do not make it luxurious,
  clinical, gym-like or staged like a showroom.

PHOTOGRAPHY AND COMPOSITION:
- Premium photorealistic commercial lifestyle photography for WeStretch.
- Warm natural daylight from camera-left, realistic colour, gentle contrast
  and believable depth of field.
- Calm, approachable expression appropriate to the requested pose.
- Vertical 3:4 composition at high resolution.
- Adjust the camera distance only as needed to show the complete pose clearly.
- Keep the head and all hair fully visible. Keep both hands and both feet fully
  visible whenever the pose permits; never crop any other body part.
- Place the actor mainly in the middle and lower portion of the frame and
  preserve quiet, uncluttered negative space above her for later App Store
  branding.
- Use anatomically correct joints, hands, fingers, feet and weight-bearing.
  The requested stretch or movement must be biomechanically credible.

OUTPUT LOCK:
- One clean, text-free and logo-free lifestyle photograph.
- No captions, letters, logos, watermark, device frame or interface elements.
- No additional people, duplicated limbs, extra fingers, missing fingers,
  fused hands, distorted joints or impossible balance.
- Change only the body pose and the minimum framing required to contain it.
  Preserve the actor, wardrobe, environment, lighting and photographic style.
```

## Optional negative prompt

Use this only when the image model provides a separate negative-prompt field.

```text
different woman, lookalike, identity drift, younger face, altered facial
proportions, different hairstyle, long hair, fully white hair, changed skin
tone, beauty retouching, plastic skin, fashion makeup, changed body type,
changed clothing, shoes, jewellery, logos, text, watermark, extra person,
cropped head, cropped hair, cropped hands, cropped feet, extra fingers,
missing fingers, fused hands, duplicated limbs, malformed anatomy, impossible
joint angles, impossible balance, illustration, CGI, fitness-model aesthetic,
clinical room, gym, cluttered background, harsh studio light
```

## Pose input examples

```text
Standing upright on the rug in a gentle side bend to her left, feet hip-width
apart, left hand resting along the outside of her left thigh, right arm arcing
overhead toward the left, shoulders relaxed, chest facing the camera and gaze
forward.
```

```text
Seated upright on the rug with both legs extended forward, a soft bend in the
knees, torso hinging slightly from the hips, both hands resting lightly on the
shins, shoulders relaxed and gaze angled toward her toes.
```

```text
On hands and knees on the rug in a neutral tabletop position, hands directly
under shoulders, knees under hips, spine long, head aligned with the torso and
gaze down toward the rug.
```

## Consistency check

Reject and regenerate any image where:

- The face reads as a different woman.
- Apparent age, haircut, hair colour, body type or outfit changes.
- The pose is anatomically unclear or inaccurate.
- The head, hair or a body part is improperly cropped.
- Generated text, branding or a watermark appears.

For final App Store assets, add the approved WeStretch logo, fade and
typography only through the deterministic compositing workflow. Do not ask the
image model to generate those elements.
