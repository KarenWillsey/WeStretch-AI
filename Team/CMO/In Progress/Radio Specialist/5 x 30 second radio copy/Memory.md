# Radio Specialist (5 x 30 Second Radio Copy) Memory

## Fix: skill was saving output outside the repo (2026-08-20)

`SKILL.md` Step 1 and Step 5 previously pointed at an OneDrive folder
(`C:\Users\karen\OneDrive\Documents\Claude\Projects\WeStretch\Output\`)
instead of this project's own `Output/` folder. As a result, the
2026-07-31 batch was never copied into the repo. It has now been recovered
into `Output/WeStretch-Radio-Ads-30sec-2026-07-31.md`, and both steps in
`SKILL.md` now point at this project's own `Output/` folder.

**Why:** Karen's standing rule, all Radio Specialist output, from any
skill run or ad-hoc request, must land in the relevant project's own
`Output/` folder, not OneDrive or anywhere else.

**How to apply:** if a future skill run can't find expected prior angles,
or new output doesn't appear here, check that `SKILL.md`'s Step 1/Step 5
paths haven't drifted back to an external location.

## Fix: proof-line example prescribed a fixed time commitment (2026-08-20)

`SKILL.md` Step 3's example proof line was "give it ten minutes and notice
the difference yourself", a fixed-duration claim. Replaced with "try it
today and notice the difference for yourself," and an explicit rule was
added against prescribing session length in any generated script.

**Why:** matches the user-control-over-duration preference established in
`Single Radio Ad Revision/Memory.md`: WeStretch sessions are user-
controlled, not fixed-length, across all radio ad copy, not just single-ad
revisions.
