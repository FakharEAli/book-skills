# Mode: prep

## Purpose
Produce a one-page call plan per upcoming external call: who they are, the job they are trying to get done, three gap hypotheses to test, a SPIN question tree tied to those hypotheses, three likely objections with calibrated questions, trust moves, and a target and fallback Advance. The sheet makes Situation questions unnecessary, so the call time goes to Problem and Implication.

## Inputs
- **Target**: `prep <company>` or `prep upcoming`.
- **Calendar connector** (for `upcoming`): tools named `list_events` / `calendar`. Read events from now to now + 48 hours. Keep an event if at least one attendee's email domain differs from the user's own domain and it is not a personal block. Drop events whose only external domains are free-mail providers unless the title names a company. Fallback: ask "Which calls do you have in the next 48 hours (company, person, time)?"
- **Web research connector** (`web-research` skill, `exa`, `scrapling`, `WebFetch`, `WebSearch`): the company website (home, services, about, team, pricing pages), recent news, current job posts, public reviews (Google, Trustpilot, industry sites), the person's public work profile. Fallback: ask for the website URL and anything the user knows.
- **Workspace**: `deals/<slug>.md` if it exists (Gap, Timeline, open questions); `memory/voc-swipe.md` and `memory/objections.md` entries for the same segment; `memory/win-loss.md` patterns block; `context/icp.md`, `context/offers.md`, `context/evidence.md`, `context/competitors.md`.
- **Docs connector** (optional output): `notion`, Claude Docs, `google-drive`.

## Procedure
Run steps 1-9 per call. For `upcoming`, process calls in time order and print a one-line index first: `HH:MM · Company · Person · call type`.

1. **Classify the call.** First call = discovery; deal file at `discovery` with a Gap = follow-up; at `proposal` = proposal review. Follow-ups skip what the Gap already answers and aim questions at its `[NOT STATED]` lines.
2. **Research, then stop.** Collect at most 12 facts, each with a source URL. Look for struggle signals: job posts for roles automation would cover (receptionist, coordinator, admin), review complaints about response time or booking, growth events (new location, hiring spree, acquisition), tools named on their site. Stop when you have 3 struggle signals or 12 facts. Never include personal (non-work) details about the person.
3. **Person and priorities.** From the role, list what that role is measured on (owner: profit, time, staff headaches; ops manager: throughput, errors, staffing; marketing lead: leads, cost per lead). Mark these as inferred.
4. **Job and forces** (Four Forces · Moesta · `offer-creation` book 07; jobs to be done · Christensen · `offer-creation` book 08). Write the job as "When <situation>, they want to <progress>, so they can <outcome>." Estimate push, pull, anxiety, habit, one line each, citing a research fact where possible. Guess the buying-timeline stage from how they arrived (booked after content = passive; asked for pricing = active looking; referred with a deadline = deciding).
5. **Gap hypotheses** (Keenan · `sales-psychology` book 04). Write H1-H3. Each has: a current-state guess, the impact metric you want them to state in their numbers (hours/week, missed leads/month, revenue lost, error rate), a root-cause guess and the evidence behind the guess. Rank by confidence. A hypothesis with no evidence is allowed only as H3 and is marked `l`.
6. **SPIN tree** (Rackham · `sales-psychology` book 01). Situation: max 3, only what research could not answer. Problem: ≥ 4. Implication: ≥ 4. Need-payoff: ≥ 2. Tag every P, I and N question with the hypothesis it tests `[H1]`; each hypothesis gets at least one Problem and one Implication question. Write questions in plain words a business owner uses, specific to this business ("When a patient cancels at 8am, what happens to that 9am slot?", not "What challenges do you face?"). Add the move-off-the-solution line (Khalsa · book 10) if the booking note names a solution, and the decision/resources question (ORDER).
7. **Objections** (Voss · `sales-psychology` book 05). Pick the 3 most likely, in this order of evidence: this company's own words (deal file, booking note), `memory/objections.md` entries for the segment, `context/competitors.md` alternatives. For each: likely wording, why, a label ("It sounds like…"), and one calibrated How/What question. Never a rebuttal script.
8. **Trust moves** (Trust Equation · Maister, Green & Galford · book 03). Three behaviours that lower self-orientation for this call (e.g. "Don't name tools or other clients before the gap is stated", "Ask about the last vendor they tried and let them finish", "Admit what you don't know about their PMS"). One credibility line only from `context/evidence.md`, else `[NEEDS PROOF: …]`.
9. **Advance** (Rackham). Target: the biggest realistic buyer action (meeting with the decider, sharing data for sizing, a scoped pilot conversation) with who and a date form. Fallback: a smaller buyer action. Add one decisiveness ping (JOLT Judge · `sales-psychology` book 02): "How did you decide on <their last tool or hire>?" Write both asks as exact words.
10. **Fit to one page.** Read `${CLAUDE_SKILL_DIR}/templates/prep-sheet.md` and fill it. Cut adjectives before cutting questions. Hard limit: 650 words above "Research notes".

## Output
The filled `templates/prep-sheet.md`, saved to `assets/prep/<YYYY-MM-DD>-<slug>.md` (call date). For `upcoming`, one file per call, then in chat: the index line per call and each sheet's "In one line" and target Advance. Offer: "Want these in <docs tool>?" and create the doc only on yes.

```markdown
Prepped <n> call(s):
- HH:MM · <Company> · <Person> → assets/prep/<date>-<slug>.md · Target Advance: <…>
```

## Write-back
- **New deal**: create `deals/<slug>.md` from `${CLAUDE_SKILL_DIR}/templates/deal-file.md`: stage `discovery`, `next_step: "Discovery call with <Person>"`, `next_step_date` = call date, `last_touch` = date of the last real contact (booking email) or blank, `stall_type: none`, `decision_maker: "not stated"`. Gap lines stay `[NOT STATED]` with H1-H3 under Root cause as `Hypothesis (unconfirmed)`.
- **Existing deal**: append to Timeline only: `### YYYY-MM-DD · Prep · assets/prep/<file>` / `- Target Advance: <…> · Fallback: <…> · Testing: H1 <…>, H2 <…>, H3 <…>`. Do not change `last_touch`.
- **`log.md`**: `YYYY-MM-DD · deals · prep · <Company> · sheet for <call date>, target Advance <…>`.

## Quality gate
- [ ] ≥ 4 Problem, ≥ 4 Implication, ≥ 2 Need-payoff questions, each tagged to a hypothesis; ≤ 3 Situation questions.
- [ ] Every research fact has a source; every hypothesis says what evidence it rests on; inferred items are marked.
- [ ] Questions name this business's specifics (their services, customers, tools, volumes), not generic discovery.
- [ ] 3 objections, each with a label and a calibrated question, no rebuttals.
- [ ] Target and fallback Advances are buyer actions with a who and a when, written as exact asks.
- [ ] Credibility line passes the evidence rule.
- [ ] ≤ 650 words above Research notes.

## Failure modes
- **Research dump.** Twelve facts about their history and none about their struggle. Research is for hypotheses.
- **Interrogation trees.** Eight Situation questions the website already answers. Cut them.
- **Pitch prep in disguise.** Objection answers that list features raise self-orientation. Prepare questions, not counters.
- **Advance = "see how it goes".** If you cannot name the buyer action you want, the call will end in a Continuation.
- **Prepping internal meetings.** `upcoming` must skip calls with only the user's domain on the invite.
- **Stale context.** For follow-ups, read the deal file's Gap first; do not re-ask what the buyer already told you.
