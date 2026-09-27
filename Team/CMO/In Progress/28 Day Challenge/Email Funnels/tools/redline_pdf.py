"""
Redline PDF generator for WeStretch email-funnel copy reviews.

Renders a "track changes in one document" style PDF: unchanged text in black,
inline within the same sentence. Input is a JSON file (see schema below);
output is a PDF.

Usage:
    python redline_pdf.py input.json output.pdf "Document Title" "Subtitle line"

JSON schema:
{
  "emails": [
    {
      "label": "Email 1",                      // short id, e.g. "Email 1"
      "subject_old": "...", "subject_new": "..." or null if unchanged,
      "preview_old": "...", "preview_new": "..." or null if unchanged,
      "paragraphs": [
        {"old": "text or null", "new": "text or null"},
        ...
      ],
      "notes": "optional reviewer rationale for this email, or null"
    },
    ...
  ]
}

Rules encoded by the renderer:
- old == new (both present, identical) -> render once, plain black.
- old present, new present, different  -> word-level diff rendered as ONE
  paragraph: unchanged words stay plain black, only the words that were
  actually removed are struck through in red, only the words that were
  actually added/changed are underlined in green, inline in reading order
  (no duplicate full sentence below).
- old present, new null                -> whole line struck through in red, tagged [REMOVED].
- old null, new present                -> whole line underlined in green, tagged [ADDED].
"""

import json
import re
import sys
import html
import difflib

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, HRFlowable
)

RED = "#c0392b"
GREEN = "#1a7f37"
GREY = "#6b6b6b"


def esc(text):
    return html.escape(text, quote=False)


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="DocTitle", fontName="Helvetica-Bold", fontSize=18,
        leading=22, spaceAfter=4, textColor=colors.HexColor("#1a1a1a"),
    ))
    styles.add(ParagraphStyle(
        name="DocSubtitle", fontName="Helvetica", fontSize=10.5,
        leading=14, spaceAfter=18, textColor=colors.HexColor(GREY),
    ))
    styles.add(ParagraphStyle(
        name="EmailHeading", fontName="Helvetica-Bold", fontSize=13,
        leading=16, spaceBefore=22, spaceAfter=6,
        textColor=colors.HexColor("#1a1a1a"),
        borderWidth=0,
    ))
    styles.add(ParagraphStyle(
        name="MetaLabel", fontName="Helvetica-Bold", fontSize=9.5,
        leading=13, spaceBefore=2, spaceAfter=1,
        textColor=colors.HexColor("#1a1a1a"),
    ))
    styles.add(ParagraphStyle(
        name="Body", fontName="Helvetica", fontSize=10.5, leading=15,
        spaceAfter=6, textColor=colors.HexColor("#1a1a1a"),
    ))
    styles.add(ParagraphStyle(
        name="Tag", fontName="Helvetica-Oblique", fontSize=8, leading=11,
        spaceAfter=2, textColor=colors.HexColor(GREY),
    ))
    styles.add(ParagraphStyle(
        name="Notes", fontName="Helvetica-Oblique", fontSize=9.5, leading=14,
        spaceBefore=6, spaceAfter=4, textColor=colors.HexColor("#3a3a6a"),
        leftIndent=10,
    ))
    return styles


def old_markup(text):
    return f'<font color="{RED}"><strike>{esc(text)}</strike></font>'


def new_markup(text):
    return f'<font color="{GREEN}"><u>{esc(text)}</u></font>'


_TOKEN_RE = re.compile(r"\S+|\s+")


def _tokenize(text):
    return _TOKEN_RE.findall(text)


def inline_diff_markup(old, new):
    """Word-level diff of old->new, returned as one reportlab markup string.

    Unchanged tokens render plain. Removed tokens render struck-through red.
    Added tokens render underlined green, placed immediately after the
    removed span they replace (or in place, for pure insertions) so the
    whole thing reads as one sentence, not two.
    """
    old_tokens = _tokenize(old)
    new_tokens = _tokenize(new)
    matcher = difflib.SequenceMatcher(None, old_tokens, new_tokens, autojunk=False)

    # Build a flat list of (kind, raw_text) segments first, kind in
    # {"eq", "del", "ins"}, so we can add a readability gap between a
    # strike-through span and an underline span that land back to back
    # with no whitespace between them (e.g. "you..." -> "you,").
    segments = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        old_chunk = "".join(old_tokens[i1:i2])
        new_chunk = "".join(new_tokens[j1:j2])
        if tag == "equal":
            segments.append(("eq", old_chunk))
            continue
        if tag in ("delete", "replace") and old_chunk.strip():
            segments.append(("del", old_chunk))
        elif old_chunk:
            segments.append(("eq", old_chunk))
        if tag in ("insert", "replace") and new_chunk.strip():
            segments.append(("ins", new_chunk))
        elif new_chunk:
            segments.append(("eq", new_chunk))

    parts = []
    prev_kind, prev_text = None, ""
    for kind, text in segments:
        if (
            prev_kind in ("del", "ins") and kind in ("del", "ins") and prev_kind != kind
            and prev_text[-1:] and not prev_text[-1:].isspace()
            and text[:1] and not text[:1].isspace()
        ):
            parts.append(" ")
        if kind == "del":
            parts.append(old_markup(text))
        elif kind == "ins":
            parts.append(new_markup(text))
        else:
            parts.append(esc(text))
        prev_kind, prev_text = kind, text
    return "".join(parts)


def render_pair(story, styles, old, new, style_name="Body", label_prefix=""):
    if old is not None and new is not None and old.strip() == new.strip():
        story.append(Paragraph(f"{label_prefix}{esc(old)}", styles[style_name]))
        return
    if old is not None and new is not None:
        story.append(Paragraph(f"{label_prefix}{inline_diff_markup(old, new)}", styles[style_name]))
        return
    if old is not None and new is None:
        story.append(Paragraph("[REMOVED]", styles["Tag"]))
        story.append(Paragraph(f"{label_prefix}{old_markup(old)}", styles[style_name]))
        return
    if old is None and new is not None:
        story.append(Paragraph("[ADDED]", styles["Tag"]))
        story.append(Paragraph(f"{label_prefix}{new_markup(new)}", styles[style_name]))
        return


def build_pdf(data, out_path, title, subtitle):
    styles = build_styles()
    doc = SimpleDocTemplate(
        out_path, pagesize=LETTER,
        topMargin=0.85 * inch, bottomMargin=0.85 * inch,
        leftMargin=0.9 * inch, rightMargin=0.9 * inch,
        title=title,
    )
    story = []
    story.append(Paragraph(esc(title), styles["DocTitle"]))
    story.append(Paragraph(esc(subtitle), styles["DocSubtitle"]))
    story.append(Paragraph(
        f'<font color="{RED}"><strike>Struck-through red text</strike></font> = words removed from the prior draft.'
        f'  <font color="{GREEN}"><u>Underlined green text</u></font> = new/changed words, shown inline in the same sentence.'
        f'  Unmarked black text is unchanged.',
        styles["Notes"],
    ))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=0.75, color=colors.HexColor("#cccccc")))

    for email in data["emails"]:
        story.append(Paragraph(esc(email.get("label", "")), styles["EmailHeading"]))

        story.append(Paragraph("Subject:", styles["MetaLabel"]))
        render_pair(story, styles, email.get("subject_old"), email.get("subject_new"), "Body")

        if email.get("preview_old") is not None or email.get("preview_new") is not None:
            story.append(Paragraph("Preview:", styles["MetaLabel"]))
            render_pair(story, styles, email.get("preview_old"), email.get("preview_new"), "Body")

        story.append(Spacer(1, 4))
        for para in email.get("paragraphs", []):
            render_pair(story, styles, para.get("old"), para.get("new"), "Body")

        if email.get("notes"):
            story.append(Paragraph(f"Reviewer notes: {esc(email['notes'])}", styles["Notes"]))

        story.append(Spacer(1, 4))
        story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#e0e0e0")))

    doc.build(story)


def main():
    if len(sys.argv) < 5:
        print('Usage: python redline_pdf.py input.json output.pdf "Title" "Subtitle"')
        sys.exit(1)
    in_path, out_path, title, subtitle = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    with open(in_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    build_pdf(data, out_path, title, subtitle)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
