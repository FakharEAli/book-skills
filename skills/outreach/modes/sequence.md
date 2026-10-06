# Mode: sequence `<prospect | segment>`

## Purpose
Design a 5–7 touch, multichannel cadence over about 21 days where every touch carries something tangible the buyer can see, ends in a respectful break-up, and stops the moment the buyer signals anything. Services are invisible and buyers fear choosing wrong (Beckwith, `sales-psychology` book 07); each touch should lower that fear by showing, not telling.

## Inputs
- The prospect's draft file from `write` (`assets/sequences/<slug>-<date>.md`) if it exists; otherwise run `write` steps 1–4 first to get trigger, angle and proof line. For a segment, use the segment's top trigger from the latest `prospects/` file and write segment-level copy with `{{company}}`, `{{trigger}}` and `{{specific}}` merge fields.
- `memory/outreach-learnings.md` best-angles block (channel and asset winners, if any).
- `context/offers.md` and `context/evidence.md` (assets may only claim what the ledger supports), `context/voice.md`.
- Existing lead magnets in `assets/magnets/` (reuse before inventing).
- Channels the user actually uses: ask once if unknown ("Email + LinkedIn only, or also phone/voice notes?"). Default: email + LinkedIn.
- **Calendar** connector optional, to place real dates. Fallback: day numbers from the start date the user gives (default: next business day).

## Procedure
1. **Fix the start date** (Day 1, a Tuesday–Thursday if possible) and the channels.
2. **Lay out the touches** using the default skeleton, then adapt to the best-angles block:

| # | Day | Channel | Purpose | Asset |
|---|---|---|---|---|
| 1 | 1 | Email | Open on trigger; one reframe; question CTA | none (text only, from `write` variant A) |
| 2 | 3 | LinkedIn connect | Familiarity, no pitch | none (variant B) |
| 3 | 5 | Email (same thread) | Make it tangible | Mini-teardown of THEIR process: 3–5 bullets or an annotated screenshot of their enquiry/booking path, what happens to a lead at each step, where it stalls |
| 4 | 8 | LinkedIn DM (if accepted) or email | Show the mechanism | Loom script (≤ 90 seconds, see template) walking through how the fix would work on their flow |
| 5 | 12 | Email (new thread, new subject) | New angle from a different implication | 1-page process diagram (current vs proposed flow) or the most relevant magnet from `assets/magnets/` |
| 6 | 16 | Phone / voice note (optional) or LinkedIn comment on their post | Human touch | none; ≤ 30-second voicemail script referencing touch 3 |
| 7 | 21 | Email (thread of touch 1 or 5) | Break-up | none |

   Use at least two channels and at most three. Drop touch 6 if the user does not phone; keep at least 5 touches.
3. **Write each touch** with the same rules as `write` (trigger-led, one idea, proof from the ledger or `[NEEDS PROOF]`, question CTA, banned list). Follow-ups never start with "just following up", "bumping this", "circling back"; each adds a new piece of value or a new implication. Email follow-ups ≤ 75 words; DMs ≤ 70 words.
4. **Build the assets** (Beckwith "make the invisible tangible", book 07): name the asset, its format, its length, and draft its content outline. A teardown uses only what is publicly visible about their process; label every inference "likely". A diagram is a box-and-arrow outline the user can render. A Loom script uses the template below. Assets may describe how the work would function; they may not promise outcomes absent from `evidence.md`.
5. **Write the break-up** with a no-oriented question (Voss, `sales-psychology` book 05). People feel safe saying no, so give them an easy no that still invites a reply: "Have you given up on fixing the after-hours enquiries, or is it just not this quarter?" or "Would it be a bad idea to close this out on my side?" No guilt, no "I'll assume you're not interested" passive aggression, no fake deadline.
6. **Apply spacing rules** and **stop conditions** (below) and print them in the file so whoever runs the sequence follows them.
7. **Run the evidence auditor** on all touches and assets together, as in `write` step 9 (`subagent_type: "book-skills:evidence-auditor"`; inline if unavailable).
8. **Save** and, only if asked, create the first email as a draft via the Email connector. Never schedule or send.

### Spacing rules
- Minimum 2 calendar days between any two touches; never two touches on the same day.
- Business days only for email and phone, sent 07:30–10:00 or 16:00–18:00 in the prospect's time zone.
- Maximum 4 emails in the whole sequence; maximum 3 LinkedIn touches.
- Touch 5 opens a new thread with a new subject (a stale thread signals a sequence); the break-up returns to an existing thread.
- If the LinkedIn connection is not accepted by Day 8, replace touch 4 with an email carrying the same asset.

### Stop conditions (check before every touch)
- Any human reply, on any channel → stop all touches; switch to `reply`.
- Unsubscribe, "not interested", "remove me", or a complaint → stop all channels permanently; add `do-not-contact` to the prospect row, append the contact to `memory/suppression.md`, and note it in the deal file if one exists.
- Hard bounce → stop email; continue LinkedIn only if already connected.
- Out-of-office auto-reply → pause; resume 2 business days after the stated return date, shifting all later touches.
- They engage publicly (comment, profile view plus connect) → keep the cadence, but the next touch acknowledges it naturally.
- New disqualifier discovered (from `icp.md`) → stop.
- Touch 7 sent with no reply → end; move to nurture, re-eligible for a new trigger after 90 days.

## Output
File `assets/sequences/<slug>-sequence-<YYYY-MM-DD>.md`:

```markdown
---
target: <Company | segment>
date: YYYY-MM-DD
start_date: YYYY-MM-DD
status: draft
channels: [email, linkedin]
audit: PASS | FIX REQUIRED
tags:
  angle: <angle>
  trigger_type: <type>
  proof_id: <id | needs-proof | capability-only>
  assets: [teardown, loom, diagram, magnet]
---

# Sequence · <target> · 21 days

| # | Day | Date | Channel | Purpose | Asset | Words |
|---|---|---|---|---|---|---|

## Touch 1 · Day 1 · Email
Subject: <≤ 5 words lower-case>
<body>

## Touch 3 · Day 5 · Email · Asset: mini-teardown
<body>
### Asset: teardown of <Company>'s <process>
1. <step they take today> → <what happens to the lead> (source: <URL>)
...

## Touch 4 · Day 8 · LinkedIn DM · Asset: Loom script
<DM>
### Loom script (≤ 90 s)
- 0–10 s: "<Name>, this is their <page/flow> as a customer sees it."
- 10–40 s: where it stalls (2 points, on screen).
- 40–75 s: how the fixed flow would run (mechanism, no promised numbers unless in evidence.md).
- 75–90 s: question CTA.

## Touch 7 · Day 21 · Break-up
<body ending in a no-oriented question>

## Spacing rules
<as above>

## Stop conditions
<as above>
```

## Write-back
- `log.md`: `YYYY-MM-DD · outreach · sequence · <target>: <k> touches over 21 days, channels <list>, assets <list> (<file path>)`.
- If a new asset was created that could serve other prospects, note it in `memory/magnet-learnings.md`: `YYYY-MM-DD · asset <name> · built for <segment> · status untested`.
- No deal file until the prospect engages.

## Quality gate
- [ ] 5–7 touches, about 21 days, at least 2 channels, spacing rules satisfied.
- [ ] Every non-opening touch adds new value (an asset or a new implication); none is a bare bump.
- [ ] Each asset is named, scoped and outlined; teardown claims about their process are sourced or labeled "likely".
- [ ] Break-up uses a no-oriented question; no guilt, no fake deadline.
- [ ] Stop conditions and spacing rules printed in the file.
- [ ] Evidence rule applied to every touch and asset; auditor run.
- [ ] Status draft; nothing scheduled or sent.

## Failure modes
- **Bump-only follow-ups.** "Any thoughts?" five times. Every touch must carry a new thing to look at.
- **Teardown as insult.** Pointing out their flaws harshly reads as attack; frame it as "what a customer experiences" and keep it to the mechanism.
- **Over-cadence.** Seven emails in ten days gets the domain flagged. Respect the email cap.
- **Assets that overclaim.** A Loom that promises "40% more bookings" without a ledger line breaks the evidence rule as surely as an email does.
- **Ignoring signals.** Continuing the cadence after an OOO or a reply is the fastest way to look automated.
