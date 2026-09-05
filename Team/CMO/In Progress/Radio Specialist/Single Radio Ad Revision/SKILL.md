---
name: radio-ad-revise
description: >
  Revise, tighten, or polish a single existing WeStretch radio ad script for natural
  read-aloud delivery within a target spot length (default 30 seconds). Use when the user
  supplies an existing radio/VO ad script and wants it improved, shortened, reworded, or
  checked for fit, not for generating a fresh batch of new scripts (see westretch-radio-ads
  for that). Always depends on westretch-core; invoke it first.
---

# WeStretch Single Radio Ad Revision

Takes one existing WeStretch radio ad script (from the user, a teammate, or a prior round)
and revises it for natural spoken delivery, applying the read-aloud house style learned from
real revision rounds (see `Memory.md`).

## Step 0; Load westretch-core first

Invoke the westretch-core skill before making any edit. It holds the personas, Strategic
Thesis, ICP, and honesty guardrail every piece of WeStretch marketing must respect.

## Step 1; Apply the user's requested edit literally first

If the user asked for a specific change (a line swap, a word choice, a tone note), make that
exact change before doing anything else. Don't second-guess an explicit instruction,
implement it, then move to the read-aloud pass below.

## Step 2; Read-aloud house style checklist

Run every draft, whether user-supplied or self-revised, through this checklist (see
`Memory.md` for the specific incidents behind each rule):

1. **Word count for the target spot length.** Default 30-second spot = 74–82 words at a
   natural announcer pace (~150–160 wpm). Count words; if over, trim the most redundant
   clause first; don't cut lines the user has already explicitly approved unless there's
   no other way to hit the target.
2. **No em dashes, anywhere**: company-wide rule (see the repo root `Memory.md`). Use a
   period or comma instead. This applies even to text supplied by someone else (a
   teammate's draft); strip any em dash before it ships.
3. **Short, plain declarative sentences over dash-linked or heavily subordinate-clause
   sentences.** If a sentence needs a colon, semicolon, or "which" clause to hold together,
   it's a candidate to split into two plain sentences instead.
4. **Avoid corporate/written words** ("solution," "designed to help you") where a plainer
   spoken word works ("app," "keeps you").
5. **Never prescribe a fixed session length** (e.g. "just ten minutes"). Sessions are
   user-controlled; if duration comes up, frame it as the user's choice, or omit it
   entirely.
6. **No punchy rhetorical-question or staccato-fragment openers** (e.g. "Golf on Saturday.
   Yard work Sunday... You've got plans; but does your body?"). This brand's openers read
   better as one warm, flowing sentence that moves from the audience's activities to the
   problem, not a fragmented hook.

## Step 3; Fit to spot length, then explain the diff

If trimming was needed to hit the word-count target, note in the output file exactly what
was cut and why (one line per change); this project's `Output/` history is meant to be
legible to a non-technical reviewer (Karen, Kari, or the office) without them having to diff
the raw text.

## Step 4; Save the output

Save to this project's own `Output/` folder as a markdown file. Include: the current/latest
script at the top, a short "what changed and why" section, and prior rounds preserved below
for reference (don't delete history, mark superseded rounds clearly instead).
