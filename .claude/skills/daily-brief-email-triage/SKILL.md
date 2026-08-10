---
name: daily-brief-email-triage
description: Use when running Karen's daily email triage over Outlook (via the Microsoft 365 MCP connector) as part of the daily brief — classifies the inbox and the unsubscribe folder, drafts replies in Karen's voice, moves spam to Deleted, and produces the Outlook activity delta rollup for Kari (kari@kasa.ca).
---

# Daily Brief — Email Triage (Outlook)

Reference: `CEO/In Progress/Set up Daily housing/Implementation Spec.md` for the full problem/spec this serves.

Ground rule for everything below: **when in doubt, don't act.** If you can't tell whether something is spam or has value, treat it as having value (list under "Needs My Attention" or "Threads Waiting On You"), never delete it. If you can't tell what a reply should say, don't invent one — flag it for Karen instead of guessing.

## No dedup tracking — this is intentional

There is no processed/reviewed marker of any kind (no Outlook category, no state file) for inbox or Unsubscribe items. Karen wants both folders **fully re-scanned and re-reported every run**, even if the same item showed up yesterday — the goal is mailbox zero, and repetition is the reminder that something is still sitting there undealt with. An item stops appearing only when it's actually gone from the folder (deleted, or moved/replied to by Karen), or in Unsubscribe's case, when Karen clears it herself.

The one exception: don't create a *second* Outlook reply draft for a thread that already has one pending from a previous run — see §3. That check is done by reading Outlook's own current state (the Drafts folder), not a separate tracking file.

## Confirmed authorizations (do not re-ask for these)

- Moving inbox spam/low-value messages to Deleted — **confirmed by Karen**.
- Moving Unsubscribe-folder junk to Deleted — confirmed.
- Creating reply drafts in Karen's voice — confirmed, but **never send them**.
- Sending the Outlook activity rollup to kari@kasa.ca automatically — confirmed.

All moves-to-Deleted use `outlook_batch_delete_messages` (soft delete, recoverable from Deleted Items, up to 50 message ids per call, no full-message read required) — not a permanent delete. `outlook_modify_labels` cannot be used for this; it explicitly refuses Trash-family destinations. Avoid `outlook_trash_thread` for this purpose: it requires a conversationId that can only be obtained by reading each message's full body first, which is needlessly expensive for routine spam cleanup.

## 0. Setup

1. Call the Microsoft 365 MCP `get_me` to confirm the mailbox this run is operating on. Record the address for the report header.
2. If the M365 MCP tools are not reachable at all, stop here and emit only:
   `COULDN'T CHECK: Email — Microsoft 365 connector unavailable ([error]).`
   Do not fabricate any email content or fall back to a previous run's data.

## 1. Unsubscribe folder — full scan, every run

The "Unsubscribe" folder is populated by Karen's existing mail rule (subject/body containing "unsubscrib"). This skill does not manage that rule — it reads the folder's contents. It's a subfolder of Inbox in this mailbox; look it up via `read_resource` on `mail:///folders/` (folder search by name only finds top-level folders) and read its contents via `mail:///folders/{id}`.

1. Pull every message currently in the folder.
2. For each, write a few-word summary. Formatting Karen wants (applies to both this folder and inbox spam in §2): one item per line, **company/sender name bolded** first, then a summary under one sentence. E.g. `**Halara** — clothing sale promo.` This is specifically so it's fast to scan.
3. Classify as **value** or **junk**:
   - Value = anything that isn't pure marketing — a real reply that got mis-filed, a receipt/confirmation/delivery update, anything tied to an active project or commitment, anything ambiguous.
   - Junk = clearly bulk marketing / newsletter / social-network notification digest — no action ever needed.
4. Value → leave the message in the folder untouched. List under **Needs My Attention**. (It will show up again tomorrow until Karen deals with it herself — that's by design.)
5. Junk → collect ids and move to Deleted via `outlook_batch_delete_messages` (batches of up to 50). List under **Deleted**.

## 2. Main inbox — full scan, every run

1. Pull every message currently in the Inbox.
2. For each, classify:
   - **Needs reply** — see §3.
   - **Spam / low value** — collect id for `outlook_batch_delete_messages` to Deleted, list under **Deleted** using the same `**Sender** — summary.` format as §1.
   - **Follow-up** — Karen is only waiting on someone else; determine this from the thread's own state (is the most recent message in the thread from Karen, with no reply yet?), not from any external tracking.
   - Everything else (FYI, no action needed, already effectively resolved) — see the fuller-detail treatment below. List under **Other Inbox Mail**.
3. Build **Threads Waiting On You** as the Needs Reply + Follow-up items combined — this is the direct answer to "what in my inbox needs me to read and deal with."

### Other Inbox Mail — full detail, not a one-liner (Karen's explicit ask, 2026-08-09)

Only "Other Inbox Mail" gets this treatment — **Needs My Attention** (§1, Unsubscribe folder value items) and **Threads Waiting On You** keep their existing one-line-per-item format.

For each item (or thread) in this category:
- Bold the subject/thread name as a header line, same as elsewhere.
- Under it, a bullet per distinct fact — dates, numbers, names, asks, decisions, deadlines. Nothing gets dropped or compressed away; if in doubt, add another bullet rather than omit. Each bullet stays a single short line (this is what keeps it scannable despite being more detail than other sections).
- **If the item is part of a multi-message thread, summarize the whole thread as one consolidated section** — one bold header, then bullets pulling from every message in the thread — not one entry per message. Read the full thread (not just the latest message) before summarizing it.

Example:
```
**Q3 Vendor Renewal — Acme Corp**
- Renewal due Sept 15, current rate $400/mo
- 10% discount offered if signed by Aug 30
- Contact: Jane Doe, jane@acme.com
- No response needed unless we want the discount
```

## 3. Voice-matched reply drafting

1. Pull the ~15–20 most recent messages from the Sent folder via `outlook_email_search` to infer Karen's real patterns: greeting/sign-off, sentence length, formality, how she says yes/no.
2. Before drafting for a given thread, check the Drafts folder for an existing draft already tied to that conversation. If one exists, don't create another — report it as already-pending in **Threads Waiting On You** and reference the existing draft.
3. If no draft exists yet:
   - Routine reply (scheduling, acknowledgment, simple yes/no, no new facts required) → draft it in Karen's voice via `outlook_create_reply_draft`. **Save as a draft only — never call a send tool for this.** The draft attaches to the thread; the original message stays in the inbox.
   - Reply requires a decision, commitment, or fact only Karen has → do **not** draft full text. List the item with a one-line note on what's needed from her ("needs your call on X") instead of guessing.
4. List every Needs Reply item with subject, sender, thread reference, and whether a full draft exists.

## 4. Outlook activity rollup for Kari

**Scope (Karen's ask, 2026-08-09):** Kari runs the family enterprise office alongside Karen — personal and corporate both — and needs her own knowledge of what happened in the mailbox to stay equal to Karen's, not just what Karen sent. This rollup now covers **sent mail** and **inbox items Karen filed into a subfolder or deleted herself**. It deliberately excludes anything this automation's own spam cleanup (§1/§2) already moved to Deleted — Kari doesn't need to hear about junk mail cleanup, only about Karen's own actions/decisions.

State file: `CEO/In Progress/Set up Daily housing/state/kari-activity-summary.json` — the one and only state file this skill uses. It exists because "what have we already told Kari" isn't answerable from Outlook's own state the way inbox/Unsubscribe dedup is. Shape:
```
{
  "last_report_sent_at": "<ISO timestamp>",
  "last_message_ids": [...],
  "last_inbox_snapshot": [{"id": "...", "subject": "...", "sender": "..."}, ...]
}
```

1. **Sent-mail delta** (unchanged from before): read `last_report_sent_at`, search Sent for messages after it, build headline-only lines (subject + recipient, no body).
2. **Inbox activity delta** (new): compare `last_inbox_snapshot` against the current Inbox contents already pulled in §2 of this run.
   - Any snapshot id no longer present in the current Inbox has left the inbox since the last check — either Karen filed it somewhere, Karen deleted it herself, or this run's own spam cleanup moved it to Deleted.
   - Drop any id that appears in **this run's own** `deleted` list (§1/§2) — that's automation cleanup, not a Karen action, and stays out of Kari's rollup.
   - For every remaining id, call `read_resource` on `mail:///messages/{id}` and read `parentFolderId`, matched against the folder list already fetched in setup:
     - Resolves to a real subfolder (not Inbox, not Deleted Items) → report as "filed into **[Folder]**."
     - Resolves to Deleted Items → report as "deleted by Karen" (distinct from this run's automated spam sweep, which is silent).
     - Read fails entirely (message no longer resolvable) → report as "left the inbox, folder untraceable" rather than guessing where it went.
   - This only tracks the Inbox folder, not every folder in the mailbox — Karen's ask was specifically about things landing in the inbox and then getting filed away, not a full-mailbox audit trail.
3. Build one combined activity list: sent items, filed items, Karen-deleted items — headline-only lines throughout (subject/recipient/destination, no body content).
4. If there's nothing new in either category, still send a one-line "No new activity since [timestamp]" note — silence would be indistinguishable from the automation being broken.
5. Send via `outlook_send_mail` to `kari@kasa.ca` — sent automatically, not drafted (see Confirmed authorizations).
6. Only after a confirmed successful send: update `kari-activity-summary.json` with the new `last_report_sent_at`, `last_message_ids`, and a fresh `last_inbox_snapshot` (current Inbox ids/subjects/senders from this run). If the send fails, leave the state file untouched entirely.

## 5. Verification pass (required before handing off to compose)

- Every message pulled from Inbox and Unsubscribe this run must land in exactly one of: Needs Reply, Follow-up, Other Inbox Mail, Deleted, Needs My Attention. None dropped, none double-counted.
- Every subject/sender/count in the output must come from this run's actual tool results — never remembered or assumed from a prior run.

## 6. Failure handling

- Any individual MCP call failure: don't guess or skip silently. Include a `COULDN'T CHECK: [what]` line in this section's output with the real error text.
- If a permission error (`FORBIDDEN` or similar) appears on a tool call this skill relies on, stop and report it plainly — don't retry blindly or attempt a workaround that wasn't agreed with Karen.

## Output contract (consumed by `daily-brief-compose`)

```
mailbox: <address>
threads_waiting_on_you: [{subject, sender, thread_ref, kind: needs_reply|follow_up, draft_exists: bool, note?}]
other_inbox: [{subject, sender, thread_ref, is_thread: bool, detail_bullets: [string, ...]}]
needs_my_attention: [{subject, sender, why}]           # from Unsubscribe folder
deleted: [{subject, sender, summary, source: inbox|unsubscribe}]
kari_rollup: {sent: bool, sent_count: N, filed_count: N, deleted_by_karen_count: N}
couldnt_check: [string, ...]
```