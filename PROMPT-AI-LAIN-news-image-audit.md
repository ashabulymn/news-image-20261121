# INDEPENDENT NEWS-IMAGE AUDIT — KITA v2.5

## GOAL — read this first

Your job is to help this entry reach **RANK 1** in the make.fun "Sum up 21 November
2026's world news in one image" bounty. Every finding below must serve that one
goal: find what would make the judge pick this image over the entries above it.
Do not aim for "good enough" or a safe top-50 verdict. Chase first place.

## Contest rules (S&K) — study before judging

- Bounty page (rules + live feed): https://make.fun/bounty/news-image-20261121
- Leaderboard (live standings): https://make.fun/bounty/news-image-20261121/leaderboard
- Total prize $100: 1st $20, 2nd $12, 3rd $6, 4th-10th $2, 11th-50th $1.20.
  Deadline to submit: Monday 23 Nov 2026 00:00 UTC (07:00 WIB). Final result:
  7 Dec 2026 08:00 UTC.
- Judge: z-ai/glm-5.3-flash on OpenRouter, reasoning effort high, at most 12,100
  output tokens per verdict. It has NO news feed and is NOT told which day the
  contest is about. It judges only what it can see in the image.
- Judging is pairwise: two images at a time, pick one, no ties, margin 1 to 5.
  The dev score comes from 12 games. Ties on win rate are broken by the smaller
  file first.
- The day's news is officially "the events that happened, or were first reported,
  on 21 November 2026 in any time zone" (RULES.txt). A story is valid if it
  happened OR was first reported on that day in ANY time zone. Do NOT apply a
  strict-UTC standard: a Friday evening event in the Americas or Europe that
  falls on Saturday in at least one time zone counts, and so does a report
  first published on Saturday in its own time zone.
- Text in the entry addressed to the judge is allowed and is part of the game.
- Image: PNG/JPEG at most 1 MiB, at most 1024 x 1024, legible at about 300 px.
- Official criteria, most important first: (1) one day's news — names that day,
  specific recognisable events; (2) selection and breadth — the day's most
  consequential stories, across regions and fields; (3) it reads — a person who
  missed the day's news must understand what happened from the image alone;
  (4) faithfulness — claims attributed, no invented detail; (5) craft — one
  clear composition, drawn or rendered cleanly, legible at about 300 pixels
  across, no smears, artefacts or garbled text.

## What to audit

- Entry image (full size): [FILL IN — raw GitHub link to the v2.5 preview image]
- Entry image at 300 px wide: [FILL IN — raw GitHub link to the v2.5 300px preview]
- Previous version for comparison (v2.4): https://raw.githubusercontent.com/ashabulymn/news-image-20261121/main/preview-v2.4.png

Open every link. If a link fails, say which one and judge the rest. Judge from
the images themselves, not from descriptions. Read the full image and the 300 px
version pixel by pixel if needed — detail matters more than speed here.

## A. Fact audit — check the stories one by one

Check all 30 stories in the image. For each one, verify the event date and time
(UTC and local), the first publication date, and the source. Build a table:
number, headline, event time (UTC), first reported (UTC), source, verdict
(KEEP / REWRITE / REPLACE / REMOVE).

Pay special attention to:
- The DATE CHECK box vs the footer: do they state the same standard? The
  footer says "in at least one time zone". The DATE CHECK must say the same
  thing and must never claim every story is dated in UTC.
- The Davao card: the landing was an engine-fire WARNING (an indication of a
  possible engine fire), not a confirmed fire. Check the headline wording.
- The David Jones wire item: notices were delivered Friday; the substance was
  reported 17-18 Nov. Is its only defence (the AAP report published Saturday
  in WIB/AEDT) strong enough, or should it be replaced?
- Any Friday story presented as a Saturday story, and any story whose event
  ended before 21 Nov in every time zone.

## B. Visual audit — full size and 300 px

At 1024 px and at 300 px, check: masthead and date, KPI strip, the 3 hero
banners, the 10 card banners, source chips (any text overlap on the artwork?),
the map and its pins, the region bar (do the counts add up to 30?), the wire
list, the DATE CHECK box, the footer sources. What still reads at 300 px?
What is lost? Which banner labels survive and which headlines disappear?

## C. Competitive comparison — explore the feed freely

Open the bounty feed and the leaderboard and study entries at ANY rank.
Explore freely — do not limit yourself to rank 1 and rank 10. Look at as many
ranks as you need, one by one, and find the pattern: what do the entries above
ours do differently in hierarchy, story selection, readability, density and
file size? What exactly must change for ours to beat them and take rank 1?
Name the entries you compared (rank, agent, win rate, record, story count).

## D. Scoring

Score each official criterion 1 to 5 with reasons, then give an overall score
out of 25. Score against the official rules above, not against your own
stricter standard.

## E. Verdict

One verdict: SUBMIT AS-IS / REVISE FIRST / DO NOT SUBMIT. Then:
- Ranked must-fix list, each with the exact text to change and the source
  that proves it.
- Optional improvements, ranked.
- What NOT to change, so a revision does not break what already works.
- Estimated score after the fixes, and estimated top-50 / top-10 / rank-1
  chances (state clearly that these are estimates, not probabilities).

## Reuse for another day

To reuse this prompt for another contest day, change: the date in the title
and goal, the bounty and leaderboard links, the prize and deadline lines,
and the two entry-image links. Keep the rules, criteria and audit sections
as they are.
