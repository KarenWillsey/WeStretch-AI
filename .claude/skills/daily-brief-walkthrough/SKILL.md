---
name: daily-brief-walkthrough
description: Use when Karen says "brief", "work the brief", "walk me through the brief", or wants to clear her inbox from the chat rather than Outlook. Walks today-queue.json one item at a time, drafts replies in her voice, and sends, deletes or files them directly from the conversation so she never opens Outlook.
---

# Daily Brief: Walkthrough

Reference: `Team/CEO/In Progress/Set Up Daily Housekeeping/Implementation Spec.md`.
Voice for drafted replies: `daily-brief-email-triage` section 3. Do not invent a
second set of voice rules here; that skill owns them.

Reads `Team/CEO/In Progress/Set Up Daily Housekeeping/state/today-queue.json`,
written by `daily-brief-compose`. Presents the day one item at a time and
executes Karen's decision immediately via the Microsoft 365 MCP tools.

## Why this exists

Reading a list is the expensive part for Karen, not deciding. A list of twelve
items costs her twelve items of reading before she can act on the first one. One
item on screen costs one. The goal of a session is Inbox zero and Unsubscribe
zero, reached one decision at a time, without her leaving the chat.

## Start of a session

1. Read `state/today-queue.json`. If it is missing or its `date` is not today,
   say so in one line and offer to run `/daily-brief` instead. Do not silently
   walk a stale queue.
2. Count `status: "open"` items and open with one line:
   `12 open. 3 decisions first. Ready?` Nothing else. No summary of the day, no
   preview of the list; the email already did that.
3. Then go straight into item 1.

## Order of work

1. **DECIDE** - only Karen can call these, and they block.
2. **REPLY** - drafts already exist; she is approving, not writing.
3. **UNFILED, SHOULD BE INBOX** - the ones that must not be missed.
4. **DATED** - confirm each is handled or scheduled.
5. **DELETED** and **FYI** - **batch these, do not walk them.** Karen reads the
   bold-name-plus-few-words list format quickly and has said so explicitly. Show
   the whole list at once and ask a single question: `all fine?` Walking these
   one at a time would waste her session on the part that already works.

## Presenting one item

```
3 of 12 - Boys' Choir

Yes or no by Monday. They need a 4pm driver
and two volunteers for 3:30 setup.

  yes / no / draft / open / skip
```

- **Position first, every single time** (`3 of 12`). She cannot hold it between
  turns and should never have to.
- **Name on the first line**, same bold name the email used, so the item is
  recognisable from the brief she already scanned.
- **Two or three short lines of context maximum**, from the queue entry's
  `detail_bullets`. This is where V1's detail finally gets to be useful: it is
  in front of her only for the one item she is working.
- **Actions on one line at the bottom.** Offer at most 5. Always include `skip`.
- If she asks for more, give her the full `detail_bullets` verbatim, then re-ask.

## Actions

| She says | You do |
|---|---|
| `yes` / `no` | Draft the reply carrying that answer, show it, wait for `send`. |
| `draft` | Write the reply, show it, wait for `send`. |
| `send` | Send it. Confirm in one line, mark the item `done`, move on. |
| `edit ...` | Apply her change, show the revised draft, wait for `send`. |
| `delete` | Move the message to Deleted Items. Mark `done`. |
| `unsub` | Move to Deleted and note the sender for an unsubscribe pass. |
| `file` | Ask which folder only if it is not obvious, then move it. |
| `open` | Give her the Outlook/Asana/Jira link for that item. |
| `skip` | Leave `status: "open"`, move on, and re-offer it at the end. |
| `stop` | Save progress, report what is left in one line, end cleanly. |

**Never send anything without her explicit `send`.** Showing a draft is not
permission to send it. This matches her standing rule that nothing goes out
unreviewed, and the tools here act on her real mailbox.

Use `outlook_create_reply_draft` so the reply threads correctly, then
`outlook_send_draft`. Do not compose a fresh message with
`outlook_send_mail` when replying to something; it breaks the thread.

## HTML bodies

Same rule as everywhere else in this project: pass **raw unescaped tags** and
set the HTML body type. Both, or the mail arrives showing literal `&lt;p&gt;`.
See `daily-brief-email-triage`'s HTML section.

## After each action

Write the updated `status` straight back to `today-queue.json`. Do not batch
the writes to the end of the session. Karen can be interrupted at any point and
the file is what lets her resume; an unsaved session is a session she has to
redo, which is exactly the failure this project exists to prevent.

Status values: `open`, `done`, `skipped`.

## End of a session

One line, no recap:

```
Done: 9. Skipped: 3. Inbox is at 3.
```

If anything was skipped, name the shortest next action and stop:
`Next: Boys' Choir still needs a yes or no before Monday.`

Do not summarise the session, do not list what was sent, do not ask if she
needs anything else. She was present for all of it.

## Karen's reading profile

She has a reading disability and ADHD. Every response in a walkthrough session
follows the `i-have-adhd` shape whether or not that skill was invoked: lead with
the action, restate position each turn, one thing on screen at a time, no
preamble, no closers, specific times not vague ones. Compact lines beat complete
sentences. If a rule here and a habit of yours disagree, this section wins.
