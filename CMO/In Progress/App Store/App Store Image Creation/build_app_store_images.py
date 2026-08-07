import argparse
import os
import sys
import zipfile
from math import ceil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


TITLE = "Physio-Informed, Adaptive Intelligence"
SUBTITLE = "Always get teh right pose at the right time."

OUTPUT_SIZES = [
    (1320, 2868),  # iPhone
    (2064, 2752),  # iPad
]

LOGO_TOP_PCT = 0.0493
LOGO_CENTER_PCT = 0.4953
LOGO_HEIGHT_PCT = 0.0239
LOGO_MAX_WIDTH_PCT = 0.6108

TITLE_FONT_SIZE_PCT = 0.0460
TITLE_LINE_HEIGHT_PCT = 0.0494
TITLE_MAX_WIDTH_PCT = 0.36
TITLE_MAX_WIDTH_PCT_FALLBACK = 0.90
TITLE_TOP_PCT = 0.1193

SUBTITLE_FONT_SIZE_PCT = 0.0275
SUBTITLE_LINE_HEIGHT_PCT = 0.0293
SUBTITLE_MAX_WIDTH_PCT = 0.30
SUBTITLE_MAX_WIDTH_PCT_FALLBACK = 0.90
SUBTITLE_TOP_PCT = 0.2316

FADE_SOLID_END_PCT = 0.24
FADE_TRANSPARENT_END_PCT = 0.36


def load_font(font_path: Path, size: int, fallback_family: str = "arial.ttf"):
    try:
        return ImageFont.truetype(str(font_path), size)
    except Exception:
        try:
            return ImageFont.truetype(fallback_family, size)
        except Exception:
            print(f"WARNING: Could not load '{font_path}' or '{fallback_family}'. Using default bitmap font.")
            return ImageFont.load_default()


def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.ImageDraw):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        candidate = f"{current_line} {word}".strip()
        candidate_width = draw.textbbox((0, 0), candidate, font=font)[2]
        if candidate_width <= max_width or not current_line:
            current_line = candidate
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines


def resize_and_crop(image: Image.Image, target_width: int, target_height: int) -> Image.Image:
    src_width, src_height = image.size
    scale = max(target_width / src_width, target_height / src_height)
    resize_width = ceil(src_width * scale)
    resize_height = ceil(src_height * scale)
    resized = image.resize((resize_width, resize_height), Image.LANCZOS)

    left = (resize_width - target_width) // 2
    top = (resize_height - target_height) // 2
    return resized.crop((left, top, left + target_width, top + target_height))


def add_fade(image: Image.Image) -> Image.Image:
    width, height = image.size
    fade = Image.new("L", (width, height), 0)
    solid_end = int(height * FADE_SOLID_END_PCT)
    transparent_end = int(height * FADE_TRANSPARENT_END_PCT)

    for y in range(solid_end, transparent_end):
        alpha = int(255 * (1.0 - (y - solid_end) / max(1, transparent_end - solid_end)))
        fade.paste(alpha, (0, y, width, y + 1))

    fade.paste(255, (0, 0, width, solid_end))

    black = Image.new("RGBA", (width, height), (0, 0, 0, 255))
    image.alpha_composite(Image.new("RGBA", (width, height), (0, 0, 0, 0)).convert("RGBA"))
    image.paste(black, (0, 0), fade)
    return image


def prepare_logo(logo_path: Path, target_size: tuple[int, int]) -> tuple[Image.Image, tuple[int, int]]:
    logo = Image.open(logo_path).convert("RGBA")
    bbox = logo.getbbox()
    if bbox is None:
        raise ValueError(f"Logo image '{logo_path}' appears empty or fully transparent.")

    visible_logo = logo.crop(bbox)
    target_width, target_height = target_size
    visible_width, visible_height = visible_logo.size

    scale = (target_height * LOGO_HEIGHT_PCT) / visible_height
    if visible_width * scale > target_width * LOGO_MAX_WIDTH_PCT:
        scale = (target_width * LOGO_MAX_WIDTH_PCT) / visible_width

    scaled_width = max(1, int(visible_width * scale))
    scaled_height = max(1, int(visible_height * scale))
    scaled_logo = visible_logo.resize((scaled_width, scaled_height), Image.LANCZOS)

    top = int(target_height * LOGO_TOP_PCT)
    center_x = int(target_width * LOGO_CENTER_PCT)
    left = int(center_x - scaled_width / 2)
    return scaled_logo, (left, top)


def draw_centered_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: int, x_center: int, y_top: int, line_height: int, fill=(255, 255, 255)):
    lines = wrap_text(text, font, max_width, draw)
    y = y_top
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        line_width = bbox[2] - bbox[0]
        x = x_center - line_width // 2
        draw.text((x, y), line, font=font, fill=fill)
        y += line_height
    return lines


def measure_text_lines(text: str, font: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.ImageDraw):
    lines = wrap_text(text, font, max_width, draw)
    return lines


def verify_logo_placement(logo_info: dict[str, float]) -> str:
    lines = []
    lines.append("Logo placement verification:")
    lines.append(f"  Output size: {logo_info['output_width']}x{logo_info['output_height']}")
    lines.append(f"  Logo top: {logo_info['top_pct']:.5f} of canvas height")
    lines.append(f"  Logo center: {logo_info['center_pct']:.5f} of canvas width")
    lines.append(f"  Logo visible width: {logo_info['width_pct']:.5f} of canvas width")
    lines.append(f"  Logo visible height: {logo_info['height_pct']:.5f} of canvas height")
    lines.append(f"  Logo max width allowed: {LOGO_MAX_WIDTH_PCT:.5f} of canvas width")
    lines.append(f"  Expected logo top: {LOGO_TOP_PCT:.5f} of canvas height")
    lines.append(f"  Expected logo center: {LOGO_CENTER_PCT:.5f} of canvas width")
    return "\n".join(lines) + "\n"


def fit_font_for_text(text: str, font_path: Path, output_width: int, output_height: int, max_width_pct: float, target_size_pct: float, min_size_pct: float, draw: ImageDraw.ImageDraw):
    max_width = min(int(output_width * max_width_pct), int(output_width * TITLE_MAX_WIDTH_PCT_FALLBACK))
    font_size = max(1, int(round(output_height * target_size_pct)))
    min_size = max(1, int(round(output_height * min_size_pct)))

    while font_size >= min_size:
        font = load_font(font_path, font_size)
        lines = measure_text_lines(text, font, max_width, draw)
        if len(lines) <= 3:
            return font, lines, font_size
        font_size -= 1

    font = load_font(font_path, min_size)
    lines = measure_text_lines(text, font, max_width, draw)
    return font, lines, min_size


def compose_image(source_path: Path, logo_path: Path, output_dimensions: tuple[int, int], save_path: Path, title_font_path: Path, subtitle_font_path: Path):
    output_width, output_height = output_dimensions
    image = Image.open(source_path).convert("RGBA")
    image = resize_and_crop(image, output_width, output_height)
    image = add_fade(image)

    logo_img, logo_pos = prepare_logo(logo_path, (output_width, output_height))
    image.paste(logo_img, logo_pos, logo_img)

    draw = ImageDraw.Draw(image)
    x_center = output_width // 2

    title_font, title_lines, _ = fit_font_for_text(
        TITLE,
        title_font_path,
        output_width,
        output_height,
        TITLE_MAX_WIDTH_PCT,
        TITLE_FONT_SIZE_PCT,
        0.0425,
        draw,
    )
    title_line_height = max(1, int(round(output_height * TITLE_LINE_HEIGHT_PCT)))
    title_max_width = min(int(output_width * TITLE_MAX_WIDTH_PCT), int(output_width * TITLE_MAX_WIDTH_PCT_FALLBACK))
    title_y_top = int(round(output_height * TITLE_TOP_PCT))
    draw_centered_text(draw, TITLE, title_font, title_max_width, x_center, title_y_top, title_line_height)

    subtitle_font, subtitle_lines, _ = fit_font_for_text(
        SUBTITLE,
        subtitle_font_path,
        output_width,
        output_height,
        SUBTITLE_MAX_WIDTH_PCT,
        SUBTITLE_FONT_SIZE_PCT,
        0.0250,
        draw,
    )
    subtitle_line_height = max(1, int(round(output_height * SUBTITLE_LINE_HEIGHT_PCT)))
    subtitle_max_width = min(int(output_width * SUBTITLE_MAX_WIDTH_PCT), int(output_width * SUBTITLE_MAX_WIDTH_PCT_FALLBACK))
    subtitle_y_top = int(round(output_height * SUBTITLE_TOP_PCT))
    draw_centered_text(draw, SUBTITLE, subtitle_font, subtitle_max_width, x_center, subtitle_y_top, subtitle_line_height)

    image.save(save_path, "PNG")
    logo_info = {
        "output_width": output_width,
        "output_height": output_height,
        "top_pct": logo_pos[1] / output_height,
        "center_pct": (logo_pos[0] + logo_img.width / 2) / output_width,
        "width_pct": logo_img.width / output_width,
        "height_pct": logo_img.height / output_height,
    }
    return save_path, logo_info


def build_outputs(source_dir: Path, output_dir: Path, logo_path: Path, title_font_path: Path, subtitle_font_path: Path):
    source_images = sorted([p for p in source_dir.iterdir() if p.is_file() and p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}])
    if len(source_images) < 3:
        raise ValueError("Source directory must contain at least 3 source images for the three concepts.")

    output_dir.mkdir(parents=True, exist_ok=True)
    created_files = []

    verification_path = output_dir / "logo_verification.txt"
    with verification_path.open("w", encoding="utf-8") as verification_file:
        verification_file.write("Logo Placement Verification Report\n")
        verification_file.write("=================================\n\n")

        for idx, source_image in enumerate(source_images[:3], start=1):
            for width, height in OUTPUT_SIZES:
                filename = f"V{idx}_{width}x{height}.png"
                save_path = output_dir / filename
                save_path, logo_info = compose_image(
                    source_image,
                    logo_path,
                    (width, height),
                    save_path,
                    title_font_path,
                    subtitle_font_path,
                )
                created_files.append(save_path)
                print(f"Created {save_path}")

                verification_file.write(f"{filename}\n")
                verification_file.write(verify_logo_placement(logo_info))
                verification_file.write("\n")

    zip_path = output_dir / f"WeStretch_App_Store_Images_{output_dir.name}.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for file_path in created_files:
            archive.write(file_path, arcname=file_path.name)

    print(f"Created ZIP archive: {zip_path}")
    return created_files, zip_path


def parse_args():
    parser = argparse.ArgumentParser(description="Compose WeStretch App Store images from base lifestyle photographs.")
    parser.add_argument("--source-dir", required=True, help="Folder containing 3 source lifestyle images.")
    parser.add_argument("--output-dir", required=True, help="Folder where V1/V2/V3 PNGs and ZIP will be written.")
    parser.add_argument("--logo-path", required=True, help="Path to 02_WeStretch_Logo_Do_Not_Modify.png.")
    parser.add_argument("--title-font", required=False, default=None, help="Path to Inter ExtraBold or fallback font file.")
    parser.add_argument("--subtitle-font", required=False, default=None, help="Path to Inter SemiBold or fallback font file.")
    return parser.parse_args()


def main():
    args = parse_args()
    source_dir = Path(args.source_dir)
    output_dir = Path(args.output_dir)
    logo_path = Path(args.logo_path)

    # If the exact Inter font files are absent, use the same fallback family for both text layers.
    fallback_font = Path(args.title_font) if args.title_font else None
    fallback_semibold = Path(args.subtitle_font) if args.subtitle_font else fallback_font

    title_font_path = fallback_font if fallback_font and fallback_font.exists() else Path("Inter-ExtraBold.ttf")
    subtitle_font_path = fallback_semibold if fallback_semibold and fallback_semibold.exists() else Path("Inter-SemiBold.ttf")

    if not source_dir.exists() or not source_dir.is_dir():
        raise FileNotFoundError(f"Source directory not found: {source_dir}")
    if not logo_path.exists():
        raise FileNotFoundError(f"Logo file not found: {logo_path}")

    build_outputs(source_dir, output_dir, logo_path, title_font_path, subtitle_font_path)


if __name__ == "__main__":
    main()
