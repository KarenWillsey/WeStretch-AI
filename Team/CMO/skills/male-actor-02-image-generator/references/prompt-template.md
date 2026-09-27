# Male Actor 02 Prompt

Replace `{{POSE}}`. Change another lock only when the user explicitly requests
that change; preserve every unmentioned lock.

```text
Use the attached male-actor-02-reference.png as the canonical identity
reference for MALE ACTOR 02.

This is an identity-preserving pose change, not a redesign and not a new
lookalike. Create a new photorealistic lifestyle photograph of the exact same
man performing this pose:

{{POSE}}

IDENTITY LOCK:
- Preserve the same recognizable facial structure, facial proportions, and
  natural mature features.
- Preserve the same apparent age: a healthy, relatable man approximately
  55 to 65.
- Preserve the same natural light complexion with a warm, lightly sun-touched
  tone and realistic mature skin texture, including natural fine lines around
  the eyes and mouth.
- Preserve the same short silver-grey hair, side-parted, neatly cut and full
  on top, slightly shorter at the temples.
- Keep him clean-shaven. Do not add stubble, a moustache, or a beard.
- Preserve the same solid, naturally fit, average-athletic male body type and
  realistic proportions. He is fit and active, not a bodybuilder.
- Do not rejuvenate, glamour retouch, reshape the face, or create artificial
  skin.
- Do not invent a specific eye colour. Follow the identity reference.

WARDROBE LOCK:
- Reproduce the navy-blue long-sleeve quarter-zip pullover in soft, lightly
  textured performance knit, with the zip partly open at the collar and a
  lighter blue crew-neck tee just visible underneath.
- Reproduce the light grey athletic shorts, just above the knee.
- Reproduce the blue-and-grey low-profile running shoes with white soles and
  low no-show socks.
- Reproduce the black hinged knee brace on his RIGHT knee: a fitted black
  neoprene sleeve with an open patella window, side hinge stays, and two
  adjustable straps above and below the knee. It is a supportive sports brace,
  never a bandage, wrap, or medical cast.
- Add no visible brand marks, jewellery, hats, or accessories.
- Do not reproduce the reference image's phone unless the requested pose
  explicitly requires him to be holding one.

SCENE LOCK:
- Preserve the same bright, calm, upscale but believable classic living room.
- Keep the warm medium-brown hardwood floor and the large round cream textured
  area rug.
- Keep the cream-white walls and white trim, the white painted fireplace with
  its mantel on camera-right, and the white built-in shelving beside it with
  restrained books, ceramics, small potted plants, and framed photos.
- Keep the large white-framed multi-pane window on camera-left with soft green
  foliage visible outside.
- Keep the cream upholstered armchair with tapered wood legs, the round dark
  wood two-tier side table on camera-left with a small potted plant and a
  shallow ceramic bowl, the tall leafy indoor tree in a woven basket, and the
  framed landscape print above the mantel.
- Keep the room clean, comfortable, and lived-in. Do not make it luxurious,
  clinical, gym-like, or staged like a showroom.

PHOTOGRAPHY AND COMPOSITION:
- Use premium photorealistic commercial lifestyle photography for WeStretch.
- Use bright, warm natural daylight from camera-left, realistic colour, gentle
  contrast, and believable depth of field.
- Give him a warm, relaxed, approachable expression: soft eyes, a smooth
  unfurrowed brow, a relaxed jaw, and either an easy natural smile or a warm
  neutral mouth. He looks quietly capable and at ease in his own home.
- Do not make him look strained, frowning, scowling, stern, pained, grimacing,
  tense, disapproving, upset, or angry. Effort in the body must never show as
  strain in the face.
- Do not overcorrect into a broad grin, a toothy laugh, or exaggerated
  delight. That reads as staged stock photography, not real.
- Use a vertical 3:4 composition at high resolution.
- Use a roughly chest-level to waist-level camera height as in the reference,
  and adjust camera distance only as needed to show the complete pose clearly.
- Keep the head and all hair fully visible. Keep both hands and both feet fully
  visible whenever the pose permits. Never crop another body part.
- Keep the right-knee brace clearly visible and unobstructed whenever the pose
  permits.
- Place the actor mainly in the middle and lower portion of the frame. Preserve
  quiet, uncluttered negative space above him for later App Store branding.
- Use anatomically correct joints, hands, fingers, feet, and weight-bearing.
  Make the requested stretch or movement biomechanically credible.

OUTPUT LOCK:
- Produce one clean, text-free, and logo-free lifestyle photograph.
- Add no captions, letters, logos, watermark, device frame, or interface.
- Add no people, duplicated limbs, extra fingers, missing fingers, fused
  hands, distorted joints, or impossible balance.
- By default, change only the body pose and the minimum framing required to
  contain it. Preserve the actor and every unmentioned wardrobe, environment,
  lighting, and photographic-style constraint.
```

## Outdoor variant

When the user explicitly asks for an outdoor or walking scene, attach
`assets/male-actor-02-reference-outdoor-walk.png` alongside the identity
anchor and replace only the SCENE LOCK block above with the following. Every
other lock stays as written, including the right-knee brace.

```text
SCENE LOCK:
- Preserve the same bright outdoor park setting: a wide paved path running
  away from the camera, flanked by mature leafy green deciduous trees.
- Keep the soft ornamental grasses and low green planting along both verges.
- Keep the dappled sunlight falling across the path and the bright, hazy
  daylight filtering through the canopy.
- Keep the setting clean, believable, and sunlit. Do not add traffic,
  buildings, signage, crowds, or park furniture.
- Show him alone unless the user explicitly asks for other people. Never carry
  the woman or the child from the supporting reference into the image on your
  own.
```

Use this only when the model supports a separate negative-prompt field:

```text
frowning, furrowed brow, knitted eyebrows, scowl, grimace, clenched jaw,
stern expression, angry, annoyed, disapproving, pained, strained face,
squinting in effort, forced smile, toothy grin, laughing, exaggerated
expression, blank staring, vacant expression,
different man, lookalike, identity drift, younger face, altered facial
proportions, different hairstyle, long hair, bald, dark brown hair, fully
white hair, stubble, moustache, beard, changed skin tone, beauty retouching,
plastic skin, changed body type, bodybuilder, changed clothing, short sleeves,
t-shirt only, long trousers, barefoot, jewellery, hat, sunglasses,
missing knee brace, brace on the left knee, brace on both knees, bandage,
elastic wrap, medical cast, logos, text, watermark, extra person, woman,
child, cropped head, cropped hair, cropped hands, cropped feet, extra fingers,
missing fingers, fused hands, duplicated limbs, malformed anatomy, impossible
joint angles, impossible balance, illustration, CGI, fitness-model aesthetic,
clinical room, gym, studio backdrop, cluttered background, harsh studio light,
night, dim lighting
```
