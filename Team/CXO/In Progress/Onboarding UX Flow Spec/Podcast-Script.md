# Onboarding UX Flow — Listen-Through Script

One document, written to be read aloud, covering everything in the
folder. No tables, no code. Read top to bottom, nothing skipped.

---

## Chapter 1: What this project is

This project maps out WeStretch's onboarding flow — every screen a new
user sees, from downloading the app through their first few weeks, all
the way to hitting the Pro paywall. Karen dictated it screen by screen.
Claude turned it into a spec a programmer can build from.

There are four goals every screen gets checked against.

Goal one: right now, after a user looks at the leaderboard, they often
just... stop there. The app should actively bring them back to the Home
screen instead of leaving them stranded on the leaderboard.

Goal two: get more guest users to create an account.

Goal three: get more free users to become paying Pro users.

Goal four: the app has a slow drip of educational tips shown over many
sessions. That drip should actually get seen and finished, not just
technically exist.

Numeric targets — like "convert 5% more users" — haven't been set yet.
That's on purpose. The goals are locked in words; the numbers come later.

## Chapter 2: The voice rules

Five rules apply to every piece of copy in the app, everywhere:

One. The app should always feel intelligent and personal — every routine
is built from that user's own history.

Two. Ada, the animated instructor, should feel like she's advancing the
user — stretches get harder and longer as the user improves, and the app
should say so.

Three. The whole point is to get people stretching daily and coming back.

Four. Losing progress should feel like a real loss — that fear is
deliberately used to nudge people toward becoming Pro users.

Five. Talk to the user's ego. It's about their body, their progress,
their achievement — not a list of features.

## Chapter 3: First time opening the app

A brand new user opens the app. They see the WeStretch logo screen, then
a short splash video of someone stretching. Then they land on the very
first real screen.

Title: "Welcome. Let's get you stretching." No subtitle. There's a small
login link at the bottom for existing users. And two big buttons: "Full
Body" and "Customize."

Tapping Full Body sends them straight into picking how long they want to
stretch for. Tapping Customize sends them into a short set of questions
first — what they want to work on, which routines they want, which body
parts, and so on — before landing on the same "how long" screen.

## Chapter 4: Picking a time and rating how you feel

The time screen asks: "How long would you like your routine to be? I
build you a unique routine each time. You can choose from 3 to 60
minutes." Three buttons: 5 minutes, 10 minutes, or a custom length. If
they pick custom, they go set a number, then come back — and that third
button now shows their chosen number instead of saying "custom length."

All three choices lead to the same next screen: a check-in. "Well, your
routine is being custom built for you... Let's check in on how you are
feeling today." There's a slider from zero to ten for body stiffness.
Zero means as stiff as a board. Ten means feeling good. Five means
moveable. As soon as they move that slider, the actual stretching routine
starts.

## Chapter 5: Doing the routine

This screen isn't really "screens" in the usual sense — it's one
continuous live experience. Top left shows which pose they're on, like
"pose 3 of 8," wrapped in a circle that fills up as they progress. Top
right counts down the seconds left on the current pose. There's an exit
button, a pause button that turns into a play button, a "too fast" button
that slows Ada down by 25 percent, and a "next" button to skip ahead.

Here's the important rule: if the user gets through at least 75 percent
of the routine, it counts as finished — even if they didn't do every
single pose. Once it's finished, they're automatically taken to the
post-routine check-in. No extra tap needed.

## Chapter 6: Right after the routine

This is where Ada, the character, actually talks to them. "Congratulations!
Let's check in on how you feel." Subtitle: "I would like to work you up
to 15 minutes a day for amazing results." Same stiffness slider as
before, so we can compare before and after.

From there: if they earned a badge, they see it. Then their streak
progress. Then they collect coins for the day. Then — only if they hit
the goal they'd set — a celebration screen.

## Chapter 7: The very first drip message

Right after all that, on their very first completed routine only, two
special screens show up.

The first one recaps what they just did: "Your routine was however-many
minutes long, full body or whatever style you picked." Subtitle: "Keep up
your mobility." It explains that WeStretch builds every future routine
off your history — so if you want that saved across devices, log in now.
Two buttons: "Sure, I'll log in" or "Continue as guest." Either way, they
move on to the next screen.

That next screen explains the leaderboard: "Leaderboards are to help you
motivate and show up every day. It's based on how many minutes you
stretch in a day. Set a little personal goal to move up, or stay in the
top league." One button: "Take me to the leaderboard." That's the real,
already-existing leaderboard in the app — nobody's redesigning that part.

And this is exactly where goal one's problem shows up: right now, after
the leaderboard, there's no clear path back to Home. Two ideas have been
proposed to fix that — either auto-send them to Home after a bit, or put
a clear button on the leaderboard inviting them back. Neither is decided
yet.

## Chapter 8: Coming back on later days

When the user finishes a second routine and opens the app again, that
first screen changes based on two things: are they still a guest, or did
they make an account — and how many routines have they finished.

If they're a guest: the screen just says "Welcome back," and explains
that making an account would let WeStretch remember their settings. Same
two buttons as before.

If they made an account — a "free" user — it's warmer: "Welcome back,"
with their first name. And now there's a third button: "Last routine
settings," which skips the whole question-and-answer wizard and takes
them straight to the check-in screen using whatever they picked last
time.

By the third routine, the message becomes "Welcome back to your third
routine," and for guests it adds: "Take notice of the shifts occurring in
your body." For free users, it's warmer still, encouraging them to
explore the customization options.

## Chapter 9: The free trial, explained simply

Here's the trial system, and it's measured in routines finished, not
calendar days.

A guest starts with seven routines' worth of full access. If they make an
account before using all seven, they get seven more added on top of
whatever they had left. So the normal path is fourteen routines total of
full access.

Along the way, the app reminds them how many are left — "eleven routines
left," "ten routines left," and so on.

At routine eight, a soft paywall message shows up for the first time —
just a nudge, nothing's locked yet. At routine fourteen, it really locks:
"That was your last fully unlocked routine." From there, free users can
only do the plain full-body routine. Everything else is visible but
blurred out, and tapping a blurred option sends them to the paywall.

One important fix made during review: earlier drafts locked free users
the moment they hit their seventh routine, which was wrong — they should
keep full access all the way through routine thirteen. That's fixed now.

Guests who blow past their seven routines without ever making an account
get the same locked treatment — full body only, everything else blurred.

## Chapter 10: The drip education messages

Starting around the second or third routine, and continuing for many
sessions after, small one-topic teaching messages get sprinkled in — one
or two per session, never blocking anyone from just jumping in and
stretching.

Some are pinned to a specific moment because Karen said so directly: a
coins explainer around routine two or three, a streak explainer early on,
an explainer about body and position filters within the first two weeks,
a special discount offer exactly on routine five — sixty days of Pro for
two dollars, plus bonus coins and streak savers — a screen right before
routine seven explaining that everything's about to move to one combined
screen, a reminder about notifications sometime before routine ten, a
nudge to increase routine length around routine ten, and an explanation
of family sharing sometime before the hard paywall at routine fourteen.

The rest — things like sound settings, captions, meeting the instructor
characters, choosing a background, learning to speed up or slow down Ada,
sharing with a friend, feedback requests — don't have a set moment yet.
Claude proposed spacing them out starting around routine fifteen, but
that's a guess, not a decision. That guess is one of the things Karen
still needs to look at.

A few things repeat on their own schedule instead of a fixed routine
number: a reminder to sign up shows every three days for guests. A
streak-saving offer shows up specifically when someone had a five-day
streak, missed a day, and comes back. Progress stats — comparing how
stiff someone was before versus after — are meant to show roughly every
eight routines, but that lands on the exact same routine as the soft
paywall, which is probably too much at once and worth spacing apart.

## Chapter 11: What's fully written versus what's just a picture

Eleven screens have real, finished writing behind them: the welcome
screen, the time picker, the check-in ratings, the actual routine screen,
the post-routine screen, the combined customize screen used from routine
seven onward, the two special first-time drip messages, and three screens
that only exist in words so far — Home, the goal-setting screen, and the
streak-saver offer — because there's no picture for them yet.

Everything else — the question screens, the pose pickers, the badge
screen, the streak screen, the coin screen — those all have pictures
Karen drew, but no written logic behind them yet. That's fine, they're
just not built out.

## Chapter 12: What Karen needs to decide

Here's the actual list of things that need a yes, no, or a number from
Karen. Nothing else in this document needs a decision — just these.

One. Look at the proposed order for all those drip education messages
and say what's wrong with it.

Two. Decide how to actually fix the leaderboard dead-end — auto-send to
Home, or a button on the leaderboard.

Three. Someone needs to design Home, the goal-setting screen, and the
streak-saver screen — they only exist as words right now.

Four. A handful of small open questions are sitting in the project's
Global-Goals and State-Variables files — things like the exact twelve
body parts in the body filter, and whether tapping "too fast" twice
stacks the slowdown or caps at one adjustment.

That's everything. End of script.
