"""WeStretch App Store image compositor.

Deterministically composites a text-free lifestyle photograph with the approved
WeStretch logo, title and subtitle, matching the authorized reference design
(Output/Default A/Screen 2.png, measured at 853x1844).

All layout constants below are CALIBRATED from pixel measurements of the
authorized reference image — do not change them without re-measuring.
See Knowledge files/03, 04, 08 for the specs these implement.

Modes:
  --source-image PATH   Single photo -> 3 crop/zoom variants x 2 sizes = 6 PNGs
  --source-dir PATH     Folder with 3 photos -> 1 crop each x 2 sizes = 6 PNGs

Every export is measured back (logo/title/subtitle visible bands) and checked
against the authorized targets. Any FAIL blocks delivery (non-zero exit).
"""
import argparse
import sys
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_LOGO = SCRIPT_DIR / "Knowledge files" / "02_WeStretch_Logo_Do_Not_Modify.png"
DEFAULT_TITLE_FONT = SCRIPT_DIR / "Fonts" / "Inter-ExtraBold.ttf"
DEFAULT_SUBTITLE_FONT = SCRIPT_DIR / "Fonts" / "Inter-SemiBold.ttf"

OUTPUT_SIZES = [
    (1320, 2868),  # iPhone 6.9"
    (2064, 2752),  # iPad 13"
]

# ---- Calibrated layout constants (fractions of canvas height H / width W) ----
LOGO_TOP_PCT = 0.0493          # visible artwork top edge, %H
LOGO_CENTER_X_PCT = 0.4953     # visible artwork horizontal centre, %W
LOGO_HEIGHT_PCT = 0.02332      # visible artwork height, %H (alpha bbox)
LOGO_MAX_WIDTH_PCT = 0.6108    # visible artwork max width, %W

TITLE_FONT_PCT = 0.03850       # font size, %H  (calibrated; NOT 4.6%)
TITLE_MIN_FONT_PCT = 0.03558
TITLE_ADVANCE_PCT = 0.04934    # baseline-to-baseline, %H (1.282 x font size)
TITLE_TOP_PCT = 0.11876        # visible lettering top of first line, %H
TITLE_BOX_W_PCT = 0.90         # max text width: min(90%W, 41%H)
TITLE_BOX_H_PCT = 0.41
TITLE_MAX_LINES = 3            # only 2 allowed when a subtitle is present

SUBTITLE_FONT_PCT = 0.02223    # font size, %H  (calibrated; NOT 2.75%)
SUBTITLE_MIN_FONT_PCT = 0.02021
SUBTITLE_ADVANCE_PCT = 0.02874 # baseline-to-baseline, %H (1.293 x font size)
SUBTITLE_TOP_PCT = 0.23156     # visible lettering top of first line, %H
SUBTITLE_BOX_W_PCT = 0.90      # max text width: min(90%W, 30%H)
SUBTITLE_BOX_H_PCT = 0.30
SUBTITLE_MAX_LINES = 3

# Fade: charcoal gradient field (NOT pure black), photo emerges 28%->42%.
# Bottom tone is brand Midnight Grey #1F1F1F (Brand Guildeline.pdf).
FADE_TOP_RGB = (12, 13, 14)
FADE_BOTTOM_RGB = (31, 31, 31)
FADE_FIELD_END_PCT = 0.28      # solid charcoal down to here
FADE_CLEAR_PCT = 0.42          # fully transparent from here down

TEXT_RGB = (255, 255, 255)

# Verification tolerances (fraction of canvas dimension)
TOL_POS = 0.004
TOL_LOGO_H = 0.0018


def die(msg: str):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def load_font_strict(path: Path, size: int) -> ImageFont.FreeTypeFont:
    """Load the exact font file or abort. Never silently substitute a font."""
    if not path.exists():
        die(f"Required font file not found: {path}\n"
            "Fallback fonts are FORBIDDEN — install the Inter static TTFs in the Fonts folder.")
    return ImageFont.truetype(str(path), size)


def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines, current = [], ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if draw.textlength(candidate, font=font) <= max_width or not current:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def fit_text(draw, text, font_path, H, W, target_pct, min_pct, box_w_pct, box_h_pct, max_lines, label):
    max_width = min(int(W * box_w_pct), int(H * box_h_pct))
    size = int(round(H * target_pct))
    min_size = int(round(H * min_pct))
    while size >= min_size:
        font = load_font_strict(font_path, size)
        lines = wrap_text(draw, text, font, max_width)
        if len(lines) <= max_lines:
            return font, lines, size, max_width
        size -= 1
    die(f"{label} does not fit in {max_lines} lines even at minimum size "
        f"({min_size}px). Do not shrink further — ask the user to shorten the text.")


def draw_text_block(draw, lines, font, W, H, top_pct, advance_pct):
    """Draw centred lines so the VISIBLE ink top of line 1 sits at top_pct*H."""
    cx = W / 2
    ink_offset = draw.textbbox((cx, 0), lines[0], font=font, anchor="ma")[1]
    y_anchor = round(H * top_pct) - ink_offset
    advance = H * advance_pct
    for i, line in enumerate(lines):
        draw.text((cx, round(y_anchor + i * advance)), line, font=font,
                  fill=TEXT_RGB, anchor="ma")


def build_fade_overlay(W, H):
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    field_end = int(H * FADE_FIELD_END_PCT)
    clear = int(H * FADE_CLEAR_PCT)
    for y in range(clear):
        if y < field_end:
            t = y / max(1, field_end)
            r = round(FADE_TOP_RGB[0] + (FADE_BOTTOM_RGB[0] - FADE_TOP_RGB[0]) * t)
            g = round(FADE_TOP_RGB[1] + (FADE_BOTTOM_RGB[1] - FADE_TOP_RGB[1]) * t)
            b = round(FADE_TOP_RGB[2] + (FADE_BOTTOM_RGB[2] - FADE_TOP_RGB[2]) * t)
            a = 255
        else:
            t = (y - field_end) / max(1, clear - field_end)
            s = t * t * (3 - 2 * t)  # smoothstep — no hard edge
            r, g, b = FADE_BOTTOM_RGB
            a = round(255 * (1 - s))
        overlay.paste((r, g, b, a), (0, y, W, y + 1))
    return overlay


def crop_photo(photo, W, H, zoom=1.0, focus_x=0.5, focus_y=0.5):
    """Cover-crop with optional extra zoom and a focus point (source fractions)."""
    sw, sh = photo.size
    scale = max(W / sw, H / sh) * zoom
    rw, rh = round(sw * scale), round(sh * scale)
    resized = photo.resize((rw, rh), Image.LANCZOS)
    left = min(max(round(focus_x * rw - W / 2), 0), rw - W)
    top = min(max(round(focus_y * rh - H / 2), 0), rh - H)
    return resized.crop((left, top, left + W, top + H))


def prepare_logo(logo_path: Path, W, H):
    logo = Image.open(logo_path).convert("RGBA")
    bbox = logo.getbbox()
    if bbox is None:
        die(f"Logo file appears empty/fully transparent: {logo_path}")
    vis = logo.crop(bbox)
    vw, vh = vis.size
    scale = (H * LOGO_HEIGHT_PCT) / vh
    if vw * scale > W * LOGO_MAX_WIDTH_PCT:
        scale = (W * LOGO_MAX_WIDTH_PCT) / vw
    sw, sh = max(1, round(vw * scale)), max(1, round(vh * scale))
    scaled = vis.resize((sw, sh), Image.LANCZOS)
    left = round(W * LOGO_CENTER_X_PCT - sw / 2)
    top = round(H * LOGO_TOP_PCT)
    return scaled, (left, top)


# ---------------------------- verification ----------------------------------

def detect_bands(img, limit_pct=0.30, thresh=175):
    """Visible bright bands (white text / logo incl. red marks) in the top of the canvas."""
    rgb = img.convert("RGB")
    px = rgb.load()
    W, H = rgb.size
    limit = int(H * limit_pct)
    rows = []
    for y in range(limit):
        cols = [x for x in range(W)
                if (lambda p: 0.299 * p[0] + 0.587 * p[1] + 0.114 * p[2] > thresh
                    or (p[0] > 150 and p[1] < 110 and p[2] < 110))(px[x, y])]
        rows.append((len(cols), cols))
    bands, current, gap = [], None, 0
    for y in range(limit):
        count, cols = rows[y]
        if count >= 3:
            gap = 0
            if current is None:
                current = {"top": y, "bottom": y, "left": min(cols), "right": max(cols)}
            else:
                current["bottom"] = y
                current["left"] = min(current["left"], min(cols))
                current["right"] = max(current["right"], max(cols))
        elif current is not None:
            gap += 1
            if gap > 8:
                bands.append(current)
                current, gap = None, 0
    if current is not None:
        bands.append(current)
    return bands


def verify_output(path, W, H, n_title_lines, n_subtitle_lines):
    """Measure the exported PNG and compare against authorized-design targets."""
    img = Image.open(path)
    bands = detect_bands(img)
    expected = 1 + n_title_lines + n_subtitle_lines
    lines = [f"--- {path.name} ({W}x{H}) ---"]
    ok = True

    def check(name, actual, target, tol):
        nonlocal ok
        good = abs(actual - target) <= tol
        ok &= good
        lines.append(f"  {'PASS' if good else 'FAIL'} {name}: {actual*100:.2f}% (target {target*100:.2f}% ±{tol*100:.2f})")

    if len(bands) != expected:
        ok = False
        lines.append(f"  FAIL band count: found {len(bands)}, expected {expected} "
                     f"(1 logo + {n_title_lines} title + {n_subtitle_lines} subtitle)")
    else:
        logo = bands[0]
        check("logo top", logo["top"] / H, LOGO_TOP_PCT, TOL_POS)
        check("logo height", (logo["bottom"] - logo["top"] + 1) / H, 0.0228, TOL_LOGO_H)
        check("logo centre", (logo["left"] + logo["right"] + 1) / 2 / W, LOGO_CENTER_X_PCT, 0.006)
        t0 = bands[1]
        check("title top", t0["top"] / H, TITLE_TOP_PCT, TOL_POS)
        for i in range(1, n_title_lines):
            adv = (bands[1 + i]["top"] - bands[i]["top"]) / H
            check(f"title line {i+1} advance", adv, TITLE_ADVANCE_PCT, 0.004)
        s0 = bands[1 + n_title_lines]
        check("subtitle top", s0["top"] / H, SUBTITLE_TOP_PCT, TOL_POS)
        for b, label in [(t0, "title"), (s0, "subtitle")]:
            check(f"{label} centre", (b["left"] + b["right"] + 1) / 2 / W, 0.50, 0.008)
    return ok, "\n".join(lines)


# ------------------------------ compositing ---------------------------------

def compose(photo_path, W, H, title, subtitle, logo_path, title_font_path, subtitle_font_path,
            zoom=1.0, focus_x=0.5, focus_y=0.5):
    photo = Image.open(photo_path).convert("RGB")
    canvas = crop_photo(photo, W, H, zoom, focus_x, focus_y).convert("RGBA")
    canvas.alpha_composite(build_fade_overlay(W, H))

    logo_img, logo_pos = prepare_logo(logo_path, W, H)
    canvas.alpha_composite(logo_img, logo_pos)

    draw = ImageDraw.Draw(canvas)
    # A 3-line title would collide with the fixed subtitle position, so the
    # title may only use 3 lines when there is no subtitle.
    title_max_lines = 2 if subtitle else TITLE_MAX_LINES
    t_font, t_lines, _, _ = fit_text(draw, title, title_font_path, H, W,
                                     TITLE_FONT_PCT, TITLE_MIN_FONT_PCT,
                                     TITLE_BOX_W_PCT, TITLE_BOX_H_PCT, title_max_lines, "Title")
    draw_text_block(draw, t_lines, t_font, W, H, TITLE_TOP_PCT, TITLE_ADVANCE_PCT)

    n_sub_lines = 0
    if subtitle:
        s_font, s_lines, _, _ = fit_text(draw, subtitle, subtitle_font_path, H, W,
                                         SUBTITLE_FONT_PCT, SUBTITLE_MIN_FONT_PCT,
                                         SUBTITLE_BOX_W_PCT, SUBTITLE_BOX_H_PCT,
                                         SUBTITLE_MAX_LINES, "Subtitle")
        draw_text_block(draw, s_lines, s_font, W, H, SUBTITLE_TOP_PCT, SUBTITLE_ADVANCE_PCT)
        n_sub_lines = len(s_lines)

    return canvas.convert("RGB"), len(t_lines), n_sub_lines


# Crop/zoom variants for single-source mode: (zoom, focus_x, focus_y).
# focus_x/focus_y are fractions of the source image.
#
# CROP RULES (from the job owner, 2026-08-07): at most half a foot may be
# cropped off — no other body part; the head AND hair must be fully visible.
# Exceptions require the user's explicit permission recorded per job. If a
# source photo cannot satisfy this for a required output size, STOP and ask.
# These values are tuned per source photo — verify visually for a new photo.
#
# Current tuning: "source image one" (lying pose, toes 13.5%..hair 90% of
# width). iPhone cannot fit that span; the user granted one-time permission
# to crop the raised leg on the TALL variants, keeping head/hair perfect.
VARIANTS_TALL = [
    (1.00, 0.635, 0.50),  # V1: full-height crop, hair fully in, raised leg runs off left
    (1.10, 0.655, 0.55),  # V2: mild zoom, framed lower on the body
    (1.22, 0.685, 0.60),  # V3: tighter zoom on torso/face
]
VARIANTS_WIDE = [
    (1.00, 0.50, 0.50),   # V1: full cover crop, whole body in frame
    (1.12, 0.60, 0.55),   # V2: mild zoom, whole body still in frame
    (1.25, 0.55, 0.60),   # V3: tighter zoom, crops only ~half the raised foot
]


def variant_params(idx, W, H):
    """Pick crop parameters for variant idx (0-based) by canvas orientation."""
    variants = VARIANTS_TALL if W / H < 0.6 else VARIANTS_WIDE
    return variants[idx]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--source-image", help="Single photo: produce 3 crop/zoom variants per size.")
    src.add_argument("--source-dir", help="Folder with 3 photos: one crop each per size.")
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--subtitle", default="")
    ap.add_argument("--logo-path", default=str(DEFAULT_LOGO))
    ap.add_argument("--title-font", default=str(DEFAULT_TITLE_FONT))
    ap.add_argument("--subtitle-font", default=str(DEFAULT_SUBTITLE_FONT))
    ap.add_argument("--zip", action="store_true", help="Also package the six PNGs into a ZIP.")
    args = ap.parse_args()

    logo_path = Path(args.logo_path)
    title_font_path = Path(args.title_font)
    subtitle_font_path = Path(args.subtitle_font)
    if not logo_path.exists():
        die(f"Logo file not found: {logo_path}")
    load_font_strict(title_font_path, 20)
    load_font_strict(subtitle_font_path, 20)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.source_image:
        photo = Path(args.source_image)
        if not photo.exists():
            die(f"Source image not found: {photo}")
        jobs = [(idx + 1, photo, None, None, None) for idx in range(3)]
    else:
        src_dir = Path(args.source_dir)
        photos = sorted(p for p in src_dir.iterdir()
                        if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"})
        if len(photos) < 3:
            die(f"Source dir must contain at least 3 photos, found {len(photos)}.")
        jobs = [(i + 1, p, 1.0, 0.5, 0.5) for i, p in enumerate(photos[:3])]

    created, all_ok, report_parts = [], True, []
    for idx, photo, zoom, fx, fy in jobs:
        for W, H in OUTPUT_SIZES:
            if zoom is None:  # single-source mode: per-orientation crop params
                z, x, y = variant_params(idx - 1, W, H)
            else:
                z, x, y = zoom, fx, fy
            name = f"V{idx}_{W}x{H}.png"
            dest = out_dir / name
            img, n_title, n_sub = compose(photo, W, H, args.title, args.subtitle,
                                          logo_path, title_font_path, subtitle_font_path,
                                          z, x, y)
            img.save(dest, "PNG")
            ok, report = verify_output(dest, W, H, n_title, n_sub)
            all_ok &= ok
            report_parts.append(report)
            created.append(dest)
            print(f"{'OK  ' if ok else 'FAIL'} {dest}")

    report_path = out_dir / "verification_report.txt"
    report_path.write_text(
        "WeStretch App Store image verification (targets from authorized Screen 2.png)\n"
        f"Fonts: {title_font_path.name} / {subtitle_font_path.name}\n"
        f"Logo: {logo_path.name}\n\n" + "\n\n".join(report_parts) + "\n",
        encoding="utf-8")
    print(f"Verification report: {report_path}")

    if not all_ok:
        die("One or more outputs failed verification — DO NOT deliver these files.")

    if args.zip:
        zip_path = out_dir / f"WeStretch_App_Store_Images_{out_dir.name}.zip"
        with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
            for f in created:
                z.write(f, arcname=f.name)
        print(f"Created {zip_path}")


if __name__ == "__main__":
    main()
