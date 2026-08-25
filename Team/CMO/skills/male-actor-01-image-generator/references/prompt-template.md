# Male Actor 01 Prompt

Replace `{{POSE}}`. Change another lock only when the user explicitly requests
that change; preserve every unmentioned lock.

```text
Use the attached male-actor-01-reference.png as the canonical identity
reference for MALE ACTOR 01.

This is an identity-preserving pose change, not a redesign and not a new
lookalike. Create a new photorealistic lifestyle photograph of the exact same
man performing this pose:

{{POSE}}

IDENTITY LOCK:
- Preserve the same recognizable facial structure, facial proportions, and
  natural mature features.
- Preserve the same apparent age: a healthy, relatable man approximately
  55 to 65.
- Preserve the same natural light-tan, sun-warmed complexion and realistic
  mature skin texture, including natural fine lines.
- Preserve the same short, tousled, curly-wavy salt-and-pepper grey hair.
- Preserve the same light stubble or clean, natural facial hair state shown
  in the reference. Do not add a full beard or change the stubble length.
- Preserve the same lean-athletic, naturally fit male body type and
  realistic proportions.
- Do not rejuvenate, glamour retouch, reshape the face, or create artificial
  skin.
- Do not invent a specific eye colour. Follow the identity reference.

WARDROBE LOCK:
- Reproduce the heathered maroon/burgundy short-sleeve polo shirt with a
  soft collar and button placket.
- Reproduce the black athletic shorts, above-the-knee length.
- Reproduce the black athletic court shoes with white soles. No visible
  socks above the shoe line.
- Add no visible brand marks, jewellery, hats, or accessories.
- Do not reproduce the reference image's pickleball paddle or ball unless the
  requested pose explicitly requires pickleball equipment.

SCENE LOCK:
- Preserve the same outdoor recreational court setting.
- Use the same blue court playing surface bordered by a green apron and
  crisp white court lines.
- Keep the dark chain-link fence running along the background, with black
  privacy windscreen panels covering part of it and some chain-link exposed.
- Keep the mature, leafy green deciduous trees rising above the fence line
  and the bright blue sky with soft white clouds above them.
- Keep the setting clean, believable, and sunlit. Do not make it a studio,
  a gym interior, or an indoor court.

PHOTOGRAPHY AND COMPOSITION:
- Use premium photorealistic commercial lifestyle photography for WeStretch.
- Use bright, natural midday daylight, realistic colour, gentle contrast,
  and believable outdoor depth of field.
- Give him a focused, energetic, approachable expression appropriate to the
  requested pose.
- Use a vertical 3:4 composition at high resolution.
- Adjust camera distance only as needed to show the complete pose clearly.
- Keep the head and all hair fully visible. Keep both hands and both feet
  fully visible whenever the pose permits. Never crop another body part.
- Place the actor mainly in the middle and lower portion of the frame.
  Preserve quiet, uncluttered negative space in the upper portion (sky and
  treetops) for later App Store branding.
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

Use this only when the model supports a separate negative-prompt field:

```text
different man, lookalike, identity drift, younger face, altered facial
proportions, different hairstyle, straight hair, fully white hair, full
beard, clean-shaven, changed skin tone, beauty retouching, plastic skin,
fashion makeup, changed body type, changed clothing, socks, jewellery, hat,
pickleball paddle, pickleball ball, logos, text, watermark, extra person,
cropped head, cropped hair, cropped
hands, cropped feet, extra fingers, missing fingers, fused hands, duplicated
limbs, malformed anatomy, impossible joint angles, impossible balance,
illustration, CGI, fitness-model aesthetic, indoor court, studio backdrop,
cluttered background, harsh studio light
```
