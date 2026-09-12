---
name: daily-brief-compose
description: Use when merging daily-brief-email-triage, daily-brief-asana, and daily-brief-jira output into Karen's final morning brief email; renders the audio version, writes the work queue and the full-detail file, runs the fail-loud verification pass, and sends the scannable one-line-per-item email.
---

# Daily Brief: Compose (V2, one line per item)

Reference: `Team/CEO/In Progress/Set Up Daily Housekeeping/Implementation Spec.md`.

This skill pulls no data. It merges the structured output already produced by
`daily-brief-email-triage`, `daily-brief-asana` and `daily-brief-jira`, plus the
`data_gathering_tokens` figure the orchestrator captured (§7a), and produces four
things:

1. **Audio** (`make-brief-audio.ps1` to OneDrive, plays on her phone)
2. **Email** (one line per item, nothing longer)
3. **Work queue** (`state/today-queue.json`, drives `daily-brief-walkthrough`)
4. **Full detail file** (`state/YYYY-MM-DD-full.md`, everything, never in the email)

## Why V2 exists (2026-09-12)

V1 was complete and unreadable. Karen stopped reviewing it: "the output is
completely useless for me and has made me slower." The cause was not length for
its own sake, it was shape. V1 rendered most sections as multi-bullet blocks,
and the one section written for her, Today's Priorities, sat at the bottom.

She identified what does work: the **Deleted** section. `**Halara**, clothing
sale promo.` A bold name, then a handful of words, one item per line. She reads
that fast and always has. **V2 applies the Deleted shape to every section.**

**Coverage did not shrink. Words per item did.** Karen cannot neglect anything:
she is working toward Inbox zero and Unsubscribe zero, and every item needs its
appropriate attention. So nothing is dropped from the brief. The detail that
used to bloat the email now lives in the full-detail file and in the
walkthrough, where she meets it one item at a time instead of all at once.

This supersedes the 2026-08-09 "zero detail loss in Other Inbox Mail" rule,
which required rendering every `detail_bullets` entry inline. That rule made the
email unusable. The bullets are preserved verbatim in the full-detail file and
in `today-queue.json`, so no fact is lost, it just is not mailed to her.

## 0. The approved example: copy it

`Team/CEO/In Progress/Set Up Daily Housekeeping/reference-brief-email.html` is
the exact HTML of the 2026-09-12 brief, pulled from Sent Items. Karen approved
it unprompted: "That email copy was great." **Read it before composing and
match it.** It is the gold standard for section order, line shape, density and
the footer, and it outranks any reading of the rules below that would drift
from it.

Do not replace that file with a later brief unless Karen approves a new one.
Its value is that she signed off on this specific one.

## 1. The line format (this is the whole skill)

Every item in every section is exactly one line:

```
**Name** - under ten words, ending in a period.
```

- **Bold the name first.** Sender, company, person, task or ticket key. Her eye
  lands on the bold and decides whether to keep reading. Never open a line with
  a date, a status word, or "Re:".
- **Then a dash, then the shortest true summary.** Target under ten words. Hard
  ceiling: the line must not wrap on a phone, so keep the whole line under
  about 70 characters.
- **Never two sentences. Never a sub-bullet. Never a nested list.**
- Lead with the verb she needs, not the background: `yes/no by Mon.` not
  `they have asked whether you would be able to confirm.`
- Money, dates and counts stay literal and verbatim: `$567.61 due Mon.`
- If an item genuinely cannot be said in one line, that is a signal it belongs
  in the walkthrough, not that the line gets longer. Put the short version in
  the email and the full version in the queue entry.

**Section headers carry a count**: `DECIDE (3)`. She needs to know the size of a
section before she enters it. A count is the one piece of context worth the
characters.

## 2. Email structure

Sections in this order. Omit any section whose count is zero, except
**Couldn't Check**, which appears whenever it is non-empty and always first.

```
Subject: [N] to decide, [M] to reply - [date]

COULDN'T CHECK (n)      <- fail-loud, first, never buried
DECIDE (n)              <- needs a yes/no or a choice only Karen can make
REPLY (n)               <- needs a response from her; draft already written
DATED (n)               <- money or deadlines with a date, incl. carried-forward
UNFILED, SHOULD BE INBOX (n)   <- Unsubscribe-folder items with real value
DELETED (n)             <- unchanged from V1; this format was already right
TASKS (n)               <- Asana + Jira, one line each, most urgent first
FYI (n)                 <- no action needed
Checked, nothing: ...   <- one line, see section 3
Footer                  <- audio path + how to start the walkthrough
```

Rules per section:

- **DECIDE** is the top of the email because it is the only thing that stops if
  she does not act. Cap it at 5 visible lines. If there are more than 5, show
  the 5 most urgent and add a final line `**+n more** - in the walkthrough.`
  Never drop the extras; they stay in the queue.
- **REPLY**: every line here must have a draft already created by
  `daily-brief-email-triage`. If a draft failed, the item moves to DECIDE.
- **DATED**: carried-forward items keep the V1 honesty rule. Append
  ` (carried, unconfirmed)` to the line when the item came from a previous run's
  log rather than today's scan. Never present a carried item as today's data.
- **UNFILED, SHOULD BE INBOX** is the renamed V1 "Needs My Attention". Karen has
  said explicitly that mail lands in Unsubscribe that belongs in the Inbox and
  she must see those for sure. Recurs daily until she clears it.
- **DELETED** keeps the V1 format verbatim: `**Halara**, clothing sale promo.`
  Do not restructure this section. It is the model the rest of the brief copies.
- **TASKS**: compress Asana and Jira into single lines, e.g.
  `**Asana** - 190 open, 2 overdue 60 days.` Named individual tasks get their
  own line only when overdue or due today.

## 3. The "Checked, nothing" line (fail loud, one line)

V1 printed a full header plus a sentence for every empty section, which cost
Karen several lines a day to tell her nothing happened. V2 keeps the fail-loud
guarantee at one line total, at the bottom:

```
Checked, nothing: Jira mentions, Asana urgent flags, Unsubscribe.
```

An omitted source still reads as "not checked," so **every source that ran clean
and empty must be named here.** This line is not optional and must never be
dropped to save space. A source that errored goes in COULDN'T CHECK, never here.

## 4. Audio

Karen asked for audio first: it removes reading entirely for the morning pass,
and she can play it on her phone before she is at a desk.

1. Write the spoken script to `state/YYYY-MM-DD-audio-script.txt`.
2. Run:
   `powershell -ExecutionPolicy Bypass -File "Team/CEO/In Progress/Set Up Daily Housekeeping/make-brief-audio.ps1" -ScriptFile "<that file>"`
3. The script prints the output path as its last line. Capture it for the email
   footer. A non-zero exit is a **fail-loud gap**: the email still sends, with a
   line in COULDN'T CHECK saying the audio did not render and why.

**Writing the spoken script** is a different job from writing the email. Spoken
text has no bold and no bullets, so structure has to be carried by the sentences:

- Open with the shape of the day: `Good morning. Three decisions, two replies,
  and one payment due Monday.`
- Then the DECIDE items, then DATED, then REPLY. **Stop there.** Deleted, FYI
  and Tasks are not read aloud; they are scanning material, not listening
  material.
- One short sentence per item. Say the name first, as the email bolds it first.
- Spell out what a synthesiser mangles: `five hundred sixty seven dollars and
  sixty one cents`, `Monday September fourteenth`. No symbols, no abbreviations,
  no email addresses, no URLs, no ticket keys read out as letters.
- Close with the count of everything not read aloud: `Twelve more items are in
  the email, nothing urgent.`
- **Target 60 to 90 seconds of finished audio**, which at Karen's 1.8x playback
  is roughly 280 to 420 words of script. If it runs longer, cut items from the
  spoken version, not detail from the email.
- **Speed is baked into the render, not left to the player.** The script
  defaults to `-Speed 1.8` because that is the pace Karen listens at, and
  because a plain WAV gives her no speed control on a phone. Do not pass a
  `-Speed` or `-Rate` override unless she asks for a different pace.
- Quote the finished duration in the footer (`1:10`) from the actual file, not
  an estimate: seconds = (file bytes - 44) / 32000 at the 16 kHz mono format.

## 5. The work queue (`state/today-queue.json`)

`daily-brief-walkthrough` reads this. Write it **before** sending the email, so
the email's "say brief in Claude" footer is never a promise the queue cannot
keep.

```json
{
  "date": "2026-09-12",
  "generated_at": "2026-09-12T05:12:00-06:00",
  "items": [
    {
      "id": "q1",
      "section": "DECIDE",
      "line": "**Boys' Choir** - yes/no by Mon. Driver 4pm, 2 setup.",
      "name": "Boys' Choir",
      "detail_bullets": ["...verbatim from the source skill..."],
      "source": "email",
      "ref": "<Outlook messageId>",
      "draft_id": null,
      "suggested_actions": ["yes", "no", "draft"],
      "status": "open"
    }
  ]
}
```

- **Every item in the email gets a queue entry**, including the ones hidden
  behind `+n more`, including FYI and Deleted. The email is the summary; the
  queue is the complete record.
- `detail_bullets` carries the source skill's output **verbatim**. This is where
  the V1 no-detail-loss guarantee now lives.
- `ref` must be the live Outlook `messageId`, Asana permalink, or Jira key, so
  the walkthrough can act without re-searching.
- `status` starts `"open"` on every item. The walkthrough owns it after that.

## 6. Full-detail file (`state/YYYY-MM-DD-full.md`)

Everything V1 used to mail her, in V1's format, written to disk instead. This is
the safety net that makes the compact email safe: no fact is lost, it is just
not in front of her. Name its path in the footer once, in one line.

## 7. Verification pass (before composing anything)

- Confirm every source skill that ran actually returned output. If
  `daily-brief-email-triage`, `daily-brief-asana` or `daily-brief-jira` did not
  run or errored entirely, that goes at the top in COULDN'T CHECK, not skipped.
- Carry forward every `couldnt_check` entry from each source verbatim.
- Do not paraphrase facts (subjects, counts, task names, amounts) beyond what
  the source produced. Compose reformats; it never reinterprets. Compressing a
  paragraph to a line is reformatting. Changing a number is not.
- Check the previous run's log for dated commitments whose date has not passed
  and carry them into DATED, marked `(carried, unconfirmed)`.

## 7a. Token cost (footer, not the subject)

The orchestrator passes either `data_gathering_tokens` (a number) or
`data_gathering_tokens_partial: true`. It covers steps 1-3 only, never compose's
own cost, which cannot be known before compose finishes.

- number present -> footer line: `~{N} tokens (excl. compose)`
- `data_gathering_tokens_partial: true` -> `tokens: partial (some steps unreported)`
- neither passed -> omit the line rather than inventing one.

Moved out of the subject line in V2: the subject is the one line Karen always
sees on her phone, and a token count is noise there.

## 8. Send

**Exactly one email reaches Karen per run.** She asked for this on 2026-09-12
after a day that produced two: the brief, and a separate audio message. The
audio is an attachment on the brief, never its own email. If the brief has
already been sent in a given run, do not send a follow-up, correction or
supplement to her; fold it into the next morning's brief instead. The only
exception is the one the HTML read-back allows: a single corrected copy when
the first arrived showing literal tags.

The Kari rollup goes to kari@kasa.ca and does not count against this.

- Recipient: Karen's own mailbox (the address confirmed via `get_me` in
  `daily-brief-email-triage`).
- Subject: `[N] to decide, [M] to reply - [date]`, e.g.
  `3 to decide, 2 to reply - Fri Sep 12`. If she reads only the phone
  notification, she still knows the shape of her day.
- **Send the body as raw, unescaped HTML** (real `<p>`/`<b>`/`<ul>` characters,
  not `&lt;p&gt;`). This applies on both send paths below; the escaped-tags bug
  does not care which one you used.

### Primary path: Outlook COM, so the audio is a real attachment

Karen listens on her phone, and a OneDrive path in the footer is not something
she can tap in Mail. The MCP connector cannot attach files at all, so the brief
is sent through the local Outlook desktop client instead.

1. Write the HTML body to `state/YYYY-MM-DD-body.html`. **Pass it as a file,
   never as a command-line string**; a long body on the command line hits the
   same quoting traps that broke `run-daily-brief.ps1` on 2026-09-12.
2. Run:
   `powershell -ExecutionPolicy Bypass -File "Team/CEO/In Progress/Set Up Daily Housekeeping/send-brief-email.ps1" -Subject "<subject>" -BodyHtmlFile "<that file>" -AttachmentPath "<the WAV from section 4>"`
3. The script confirms the message reached Sent Items **and** that it carries an
   attachment before exiting 0. It needs no separate read-back.

Exit codes: `0` sent and confirmed, `2` Outlook COM unavailable, `3` sent but
unconfirmed, `1` other.

### Fallback: MCP send, no attachment

On any non-zero exit, fall back to the Microsoft 365 MCP mail-send tool with the
HTML body type set, and **say so in the brief**: add a COULDN'T CHECK line
reading `Audio not attached, Outlook send failed. File is at <path>.` Never let
the fallback happen silently; she will be waiting for an attachment that is not
there.

After an MCP fallback send, **read the message back from Sent Items** and
confirm it rendered as real HTML rather than visible literal tags. If not, send
one corrected copy and say so in the run summary. See
`daily-brief-email-triage`'s HTML section and the project `Memory.md`.

**Known risk on the 5am scheduled run:** Outlook COM needs an interactive
desktop session. If the task ever fires while Karen is logged off, exit 2 is the
expected result and the fallback carries the morning. That is a degraded brief,
not a failed one; keep it that way.
- The Kari activity rollup is **not** sent from here.
  `daily-brief-email-triage` already sends that separately to kari@kasa.ca.

## 9. Footer

Four lines, no more:

```
Listen: attached, 1:10. Also in OneDrive > Daily Brief.
Work it: say "brief" in Claude to go one item at a time.
Full detail: state/2026-09-12-full.md
~48,000 tokens (excl. compose)
```

If the send fell back to MCP and the audio could not be attached, the first
line becomes the OneDrive path alone, and the COULDN'T CHECK line from section 8
explains why.

## 10. Failure handling

If composing or sending fails, do not silently drop the report. Surface the
failure in the conversation so whoever is running this knows the brief did not
go out. If the email fails but the audio rendered, say that explicitly: she can
still listen.
