/*
 * Redline PDF generator for WeStretch email-funnel copy reviews.
 *
 * Renders a "track changes in one document" style PDF: unchanged text in
 * black, inline within the same sentence. Input is a JSON file (see schema
 * below); output is a PDF.
 *
 * Usage:
 *     node redline_pdf.js input.json output.pdf "Document Title" "Subtitle line"
 *
 * JSON schema:
 * {
 *   "emails": [
 *     {
 *       "label": "Email 1",                      // short id, e.g. "Email 1"
 *       "subject_old": "...", "subject_new": "..." or null if unchanged,
 *       "preview_old": "...", "preview_new": "..." or null if unchanged,
 *       "paragraphs": [
 *         {"old": "text or null", "new": "text or null"},
 *         ...
 *       ],
 *       "notes": "optional reviewer rationale for this email, or null"
 *     },
 *     ...
 *   ]
 * }
 *
 * Rules encoded by the renderer:
 * - old == new (both present, identical) -> render once, plain black.
 * - old present, new present, different  -> word-level diff rendered as ONE
 *   paragraph: unchanged words stay plain black, only the words that were
 *   actually removed are struck through in red, only the words that were
 *   actually added/changed are underlined in green, inline in reading order
 *   (no duplicate full sentence below).
 * - old present, new null                -> whole line struck through in red, tagged [REMOVED].
 * - old null, new present                -> whole line underlined in green, tagged [ADDED].
 */

const fs = require("fs");
const PDFDocument = require("pdfkit");

const RED = "#c0392b";
const GREEN = "#1a7f37";
const GREY = "#6b6b6b";
const INK = "#1a1a1a";
const NOTES_COLOR = "#3a3a6a";
const RULE_LIGHT = "#e0e0e0";
const RULE_MED = "#cccccc";

const STYLES = {
  DocTitle: { font: "Helvetica-Bold", size: 18, lineGap: 4, color: INK, spaceAfter: 4 },
  DocSubtitle: { font: "Helvetica", size: 10.5, lineGap: 3, color: GREY, spaceAfter: 18 },
  EmailHeading: { font: "Helvetica-Bold", size: 13, lineGap: 3, color: INK, spaceBefore: 22, spaceAfter: 6 },
  MetaLabel: { font: "Helvetica-Bold", size: 9.5, lineGap: 3, color: INK, spaceBefore: 2, spaceAfter: 1 },
  Body: { font: "Helvetica", size: 10.5, lineGap: 4.5, color: INK, spaceAfter: 6 },
  Tag: { font: "Helvetica-Oblique", size: 8, lineGap: 3, color: GREY, spaceAfter: 2 },
  Notes: { font: "Helvetica-Oblique", size: 9.5, lineGap: 4.5, color: NOTES_COLOR, spaceBefore: 6, spaceAfter: 4, leftIndent: 10 },
};

const TOKEN_RE = /\S+|\s+/g;

function tokenize(text) {
  return text.match(TOKEN_RE) || [];
}

/**
 * Port of Python difflib.SequenceMatcher (autojunk=False, no isjunk) —
 * find_longest_match / get_matching_blocks / get_opcodes — so the JS diff
 * finds the same longest-contiguous-block matches difflib does. A plain
 * LCS backtrack is NOT equivalent here: it can be fooled into treating an
 * incidental single-token match (e.g. a shared whitespace token between
 * two words) as its own "equal" run, fragmenting what should be one
 * replace opcode into an alternating word-by-word del/ins mess.
 */
function findLongestMatch(a, b, b2j, alo, ahi, blo, bhi) {
  let besti = alo, bestj = blo, bestsize = 0;
  let j2len = new Map();
  for (let i = alo; i < ahi; i++) {
    const newj2len = new Map();
    const indices = b2j.get(a[i]) || [];
    for (const j of indices) {
      if (j < blo) continue;
      if (j >= bhi) break;
      const k = (j2len.get(j - 1) || 0) + 1;
      newj2len.set(j, k);
      if (k > bestsize) { besti = i - k + 1; bestj = j - k + 1; bestsize = k; }
    }
    j2len = newj2len;
  }
  while (besti > alo && bestj > blo && a[besti - 1] === b[bestj - 1]) {
    besti--; bestj--; bestsize++;
  }
  while (besti + bestsize < ahi && bestj + bestsize < bhi && a[besti + bestsize] === b[bestj + bestsize]) {
    bestsize++;
  }
  return { i: besti, j: bestj, size: bestsize };
}

function getMatchingBlocks(a, b) {
  const la = a.length, lb = b.length;
  const b2j = new Map();
  for (let i = 0; i < lb; i++) {
    if (!b2j.has(b[i])) b2j.set(b[i], []);
    b2j.get(b[i]).push(i);
  }
  const queue = [[0, la, 0, lb]];
  const matchingBlocks = [];
  while (queue.length) {
    const [alo, ahi, blo, bhi] = queue.pop();
    const { i, j, size } = findLongestMatch(a, b, b2j, alo, ahi, blo, bhi);
    if (size) {
      matchingBlocks.push([i, j, size]);
      if (alo < i && blo < j) queue.push([alo, i, blo, j]);
      if (i + size < ahi && j + size < bhi) queue.push([i + size, ahi, j + size, bhi]);
    }
  }
  matchingBlocks.sort((x, y) => x[0] - y[0] || x[1] - y[1] || x[2] - y[2]);
  let i1 = 0, j1 = 0, k1 = 0;
  const nonAdjacent = [];
  for (const [i2, j2, k2] of matchingBlocks) {
    if (i1 + k1 === i2 && j1 + k1 === j2) {
      k1 += k2;
    } else {
      if (k1) nonAdjacent.push([i1, j1, k1]);
      i1 = i2; j1 = j2; k1 = k2;
    }
  }
  if (k1) nonAdjacent.push([i1, j1, k1]);
  nonAdjacent.push([la, lb, 0]);
  return nonAdjacent;
}

function getOpcodes(a, b) {
  const blocks = getMatchingBlocks(a, b);
  let i = 0, j = 0;
  const answer = [];
  for (const [ai, bj, size] of blocks) {
    let tag = "";
    if (i < ai && j < bj) tag = "replace";
    else if (i < ai) tag = "delete";
    else if (j < bj) tag = "insert";
    if (tag) answer.push({ tag, i1: i, i2: ai, j1: j, j2: bj });
    i = ai + size; j = bj + size;
    if (size) answer.push({ tag: "equal", i1: ai, i2: i, j1: bj, j2: j });
  }
  return answer;
}

/**
 * Turn opcodes into (kind, text) segments: an "equal" opcode becomes one
 * "eq" segment; a "delete"/"insert"/"replace" opcode becomes a "del"
 * segment (the whole removed chunk) and/or an "ins" segment (the whole
 * added chunk), in that order, so a removal reads before its replacement.
 * A whitespace-only chunk is downgraded to "eq" (pure whitespace changes
 * shouldn't render as a strike/underline).
 */
function buildSegments(oldTokens, newTokens, opcodes) {
  const segments = [];
  for (const { tag, i1, i2, j1, j2 } of opcodes) {
    const oldChunk = oldTokens.slice(i1, i2).join("");
    const newChunk = newTokens.slice(j1, j2).join("");
    if (tag === "equal") {
      segments.push(["eq", oldChunk]);
      continue;
    }
    if ((tag === "delete" || tag === "replace") && oldChunk.trim()) segments.push(["del", oldChunk]);
    else if (oldChunk) segments.push(["eq", oldChunk]);
    if ((tag === "insert" || tag === "replace") && newChunk.trim()) segments.push(["ins", newChunk]);
    else if (newChunk) segments.push(["eq", newChunk]);
  }
  return segments;
}

/**
 * Word-level diff of old->new, returned as an ordered list of
 * {kind: "eq"|"del"|"ins", text} runs ready to hand to pdfkit as
 * continued text segments.
 *
 * A readability gap is inserted between a strike-through span and an
 * underline span that land back to back with no whitespace between them
 * (e.g. "you..." -> "you,").
 */
function inlineDiffParts(oldStr, newStr) {
  const oldTokens = tokenize(oldStr);
  const newTokens = tokenize(newStr);
  const segments = buildSegments(oldTokens, newTokens, getOpcodes(oldTokens, newTokens));

  const parts = [];
  let prevKind = null, prevText = "";
  for (const [kind, text] of segments) {
    const abut = (prevKind === "del" || prevKind === "ins")
      && (kind === "del" || kind === "ins")
      && prevKind !== kind
      && prevText.slice(-1) && !/\s/.test(prevText.slice(-1))
      && text.slice(0, 1) && !/\s/.test(text.slice(0, 1));
    if (abut) parts.push({ kind: "eq", text: " " });
    parts.push({ kind, text });
    prevKind = kind;
    prevText = text;
  }
  return parts;
}

function ensureSpace(doc, neededPts) {
  const bottom = doc.page.height - doc.page.margins.bottom;
  if (doc.y + neededPts > bottom) doc.addPage();
}

function applyStyle(doc, styleName) {
  const style = STYLES[styleName];
  doc.font(style.font).fontSize(style.size).fillColor(style.color);
  return style;
}

/** Draw a plain paragraph in the given style, honoring spaceBefore/After. */
function drawText(doc, text, styleName, opts = {}) {
  const style = applyStyle(doc, styleName);
  if (style.spaceBefore) doc.y += style.spaceBefore;
  const indent = style.leftIndent || 0;
  const x = doc.page.margins.left + indent;
  const width = doc.page.width - doc.page.margins.left - doc.page.margins.right - indent;
  ensureSpace(doc, style.size * 2);
  doc.text(text, x, doc.y, { width, lineGap: style.lineGap, ...opts });
  if (style.spaceAfter) doc.y += style.spaceAfter;
}

/** Draw a paragraph built from inline {kind, text} runs (plain/del/ins) in the given style. */
function drawParts(doc, parts, styleName, labelPrefix = "") {
  const style = applyStyle(doc, styleName);
  if (style.spaceBefore) doc.y += style.spaceBefore;
  const indent = style.leftIndent || 0;
  const x = doc.page.margins.left + indent;
  const width = doc.page.width - doc.page.margins.left - doc.page.margins.right - indent;
  ensureSpace(doc, style.size * 2);

  const runs = [];
  if (labelPrefix) runs.push({ kind: "eq", text: labelPrefix });
  runs.push(...parts);

  runs.forEach((run, idx) => {
    const first = idx === 0;
    const last = idx === runs.length - 1;
    doc.font(style.font).fontSize(style.size);
    if (run.kind === "del") {
      doc.fillColor(RED);
    } else if (run.kind === "ins") {
      doc.fillColor(GREEN);
    } else {
      doc.fillColor(style.color);
    }
    const runOpts = {
      continued: !last,
      underline: run.kind === "ins",
      strike: run.kind === "del",
      lineGap: style.lineGap,
    };
    if (first) {
      doc.text(run.text, x, doc.y, { ...runOpts, width });
    } else {
      doc.text(run.text, runOpts);
    }
  });

  if (style.spaceAfter) doc.y += style.spaceAfter;
}

function drawHR(doc, thickness, color) {
  ensureSpace(doc, thickness + 4);
  const x1 = doc.page.margins.left;
  const x2 = doc.page.width - doc.page.margins.right;
  doc.save();
  doc.lineWidth(thickness).strokeColor(color)
    .moveTo(x1, doc.y).lineTo(x2, doc.y).stroke();
  doc.restore();
  doc.y += thickness + 4;
}

function renderPair(doc, old, newVal, styleName = "Body", labelPrefix = "") {
  if (old != null && newVal != null && old.trim() === newVal.trim()) {
    drawParts(doc, [{ kind: "eq", text: old }], styleName, labelPrefix);
    return;
  }
  if (old != null && newVal != null) {
    drawParts(doc, inlineDiffParts(old, newVal), styleName, labelPrefix);
    return;
  }
  if (old != null && newVal == null) {
    drawText(doc, "[REMOVED]", "Tag");
    drawParts(doc, [{ kind: "del", text: old }], styleName, labelPrefix);
    return;
  }
  if (old == null && newVal != null) {
    drawText(doc, "[ADDED]", "Tag");
    drawParts(doc, [{ kind: "ins", text: newVal }], styleName, labelPrefix);
    return;
  }
}

function buildPdf(data, outPath, title, subtitle) {
  return new Promise((resolve, reject) => {
    const doc = new PDFDocument({
      size: "LETTER",
      margins: {
        top: 0.85 * 72,
        bottom: 0.85 * 72,
        left: 0.9 * 72,
        right: 0.9 * 72,
      },
      info: { Title: title },
      bufferPages: true,
    });
    const stream = fs.createWriteStream(outPath);
    doc.pipe(stream);
    stream.on("finish", resolve);
    stream.on("error", reject);

    drawText(doc, title, "DocTitle");
    drawText(doc, subtitle, "DocSubtitle");

    drawParts(doc, [
      { kind: "del", text: "Struck-through red text" },
      { kind: "eq", text: " = words removed from the prior draft.  " },
      { kind: "ins", text: "Underlined green text" },
      { kind: "eq", text: " = new/changed words, shown inline in the same sentence.  Unmarked black text is unchanged." },
    ], "Notes");

    doc.y += 6;
    drawHR(doc, 0.75, RULE_MED);

    for (const email of data.emails || []) {
      drawText(doc, email.label || "", "EmailHeading");

      drawText(doc, "Subject:", "MetaLabel");
      renderPair(doc, email.subject_old ?? null, email.subject_new ?? null, "Body");

      if ((email.preview_old ?? null) !== null || (email.preview_new ?? null) !== null) {
        drawText(doc, "Preview:", "MetaLabel");
        renderPair(doc, email.preview_old ?? null, email.preview_new ?? null, "Body");
      }

      doc.y += 4;
      for (const para of email.paragraphs || []) {
        renderPair(doc, para.old ?? null, para.new ?? null, "Body");
      }

      if (email.notes) {
        drawText(doc, `Reviewer notes: ${email.notes}`, "Notes");
      }

      doc.y += 4;
      drawHR(doc, 0.5, RULE_LIGHT);
    }

    doc.end();
  });
}

async function main() {
  const [, , inPath, outPath, title, subtitle] = process.argv;
  if (!inPath || !outPath || !title || !subtitle) {
    console.log('Usage: node redline_pdf.js input.json output.pdf "Title" "Subtitle"');
    process.exit(1);
  }
  const data = JSON.parse(fs.readFileSync(inPath, "utf-8"));
  await buildPdf(data, outPath, title, subtitle);
  console.log(`Wrote ${outPath}`);
}

if (require.main === module) {
  main().catch((err) => {
    console.error(err);
    process.exit(1);
  });
}

module.exports = { buildPdf, inlineDiffParts, tokenize, getOpcodes };
