#!/usr/bin/env python3
"""Check PNG integrity and basic real-transparency requirements."""

import argparse
import json
from pathlib import Path
from PIL import Image


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path)
    parser.add_argument("--transparent", action="store_true", help="Require a transparent cutout")
    args = parser.parse_args()

    with Image.open(args.image) as image:
        image.verify()
    with Image.open(args.image) as image:
        image.load()
        fmt, size, mode = image.format, image.size, image.mode
        alpha = image.getchannel("A") if "A" in image.getbands() else None
        bbox = alpha.getbbox() if alpha else None
        extrema = alpha.getextrema() if alpha else None
        if alpha:
            w, h = size
            corners = [alpha.getpixel(p) for p in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]]
            border_max = max(
                alpha.crop((0, 0, w, 1)).getextrema()[1],
                alpha.crop((0, h - 1, w, h)).getextrema()[1],
                alpha.crop((0, 0, 1, h)).getextrema()[1],
                alpha.crop((w - 1, 0, w, h)).getextrema()[1],
            )
        else:
            corners, border_max = None, None

    problems = []
    if fmt != "PNG":
        problems.append("File is not PNG")
    if args.transparent:
        if alpha is None or extrema is None or extrema[0] != 0 or extrema[1] == 0:
            problems.append("No usable transparent/opaque alpha range")
        if corners != [0, 0, 0, 0]:
            problems.append("One or more corner pixels are not fully transparent")
        if border_max != 0:
            problems.append("Visible pixels reach an outer border; check crop or edge leakage")
    print(json.dumps({
        "file": str(args.image), "size": size, "mode": mode,
        "alpha_range": extrema, "alpha_bbox": bbox,
        "corner_alpha": corners, "border_max_alpha": border_max,
        "passed": not problems, "problems": problems,
    }, indent=2))
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
