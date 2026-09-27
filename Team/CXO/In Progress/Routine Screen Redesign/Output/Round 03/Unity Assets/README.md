# Routine Screen Unity Assets

Transparent PNG assets recreated from `07-calm-routine-no-upper-gradient.png`.

## Files

- `countdown-ring.png`: outer ring around the hold countdown.
- `counter-background.png`: optional dark centre behind countdown or pose text.
- `progress-track-ring.png`: smaller grey routine-progress track.
- `pause-icon.png`: white pause glyph only.
- `play-icon.png`: matching white play glyph.
- `progress-fill-ring.png`: full Fire Red ring for Unity radial filling.
- `progress-round-cap.png`: round endpoint used with the red radial fill.

The ring assets are 512 x 512 px. The pause and play icons are 256 x 256 px. The endpoint is 64 x 64 px. All use transparent RGBA backgrounds.

## Unity import settings

For every PNG:

- Texture Type: Sprite (2D and UI)
- Sprite Mode: Single
- Alpha Source: Input Texture Alpha
- Alpha Is Transparency: enabled
- Mesh Type: Full Rect
- Wrap Mode: Clamp
- Filter Mode: Bilinear
- Compression: None
- Generate Mip Maps: disabled

Keep each ring RectTransform perfectly square and enable Preserve Aspect.

## Red progress outline

Use two stacked UI Images of the same size:

1. Bottom Image: `progress-track-ring.png`, Type Simple.
2. Top Image: `progress-fill-ring.png`, Type Filled, Fill Method Radial 360, Fill Origin Top, Clockwise enabled.

Set the red image amount from completed poses:

```csharp
progressImage.fillAmount = totalPoses > 0
    ? Mathf.Clamp01((float)completedPoses / totalPoses)
    : 0f;
```

For the sample design, `12 / 66 = 0.1818`.

Unity's radial fill produces flat cut edges. To match the design's rounded ends:

- Place one `progress-round-cap.png` at the 12 o'clock start point.
- Place a second cap at the live endpoint.
- Make each cap's displayed diameter equal to the red ring thickness.
- Rotate the endpoint around the ring centre by `fillAmount * 360` degrees clockwise.
- Hide both caps when progress is zero. At full progress, hide the endpoint cap because it overlaps the start cap.

The red is the brand Fire Red `#FC4850`.
