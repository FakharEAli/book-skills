# Playbooks

Step-by-step workflows chaining several books for your real tasks. Book numbers in brackets refer to `books/NN-*.md`.

---

## 1. Discovery call with an owner who is confident their process is fine

**Goal**: surface the real scope and cost without contradicting the owner.
**Inputs**: 45-minute call; owner plus, ideally, the person who does the work.

**Steps**
1. Set the perceptual frame [03]: "I'll ask you to walk the process end to end; the useful part is where it gets fuzzy."
2. Explanatory depth probe [05]: "From trigger to done, step by step, including who touches it." Note every "then it just goes to..." as a gap.
3. Ask the doer [05]: turn to the ops person: "What goes wrong that never reaches [owner]?"
4. Count, don't narrate [01, 08]: for each pain, "roughly how many times a week?" and "what else changed when it got worse?"
5. Status quo bias test [10]: "If you were starting the company today, would you run it this way?"
6. Their probability [10]: "Gut number that this process holds for two more years?"
7. Anchor the cost [01, 08]: hours × loaded rate, plus owner-hours × the owner's revenue-generating rate. Say the number aloud.
8. Premortem invitation [01]: "If we did this and it failed in six months, why?" Record verbatim.
9. Within two hours [05, 03]: send a one-page process map and the cost number; ask both attendees to correct it.

**Output artifact**: Process map (steps, owner, exception count/week, gap flags) + Cost-of-problem line + Premortem risks list + Corrections received.
**Common failure**: accepting the owner's fluent description as the process and quoting from it; the gaps appear at build time as "scope creep."

---

## 2. Handling "we tried automation before and it failed"

**Goal**: move the prospect one step back up the pyramid of choice without asking them to admit a mistake.
**Inputs**: the objection, said on a call or in reply to outreach.

**Steps**
1. Do not argue [04]. Validate the frequency: "That's the most common outcome I see."
2. Situational attribution [02, 04, 08]: "It's almost never the owner's judgment; it's usually that the agency built it and left and nobody inside owned it."
3. Artefacts over memory [04, 05]: "Do you still have the scope doc or the invoices? I'd like to see what was in it."
4. Specifics engage System 2 [01]: "Which part broke: trigger, data mapping, or the handoff to a person?"
5. Sunk cost as paid learning [01, 08]: "That spend is gone either way. What it bought is knowing which process matters and what breaks it."
6. Emotion → goal [09]: if there is anger at the old vendor, the goal is "deter cheaters"; answer with accountability (milestones, pay-on-running, admin access handed over day one).
7. Small, reversible, private step [04, 07]: one workflow, fixed fee, 30 days, documented handover.
8. Let them state the new belief [02, 04]: "What would it take for you to trust this again?"
9. Inoculate [02]: name the objection their team will raise ("it'll break when the API changes") and answer it before they hear it.

**Output artifact**: Objection response script (steps 1–8 as a one-page template) + Accountability terms block for the proposal (milestones, pay-on-running, access/documentation handover).
**Common failure**: pitching "we're different from them," which implicitly criticises the prospect's past judgment and adds dissonance.

---

## 3. Proposal and pricing page that survives risk perception

**Goal**: a written offer that reads as low-risk to a loss-averse owner and holds up after signing.
**Inputs**: process map and cost number from Playbook 1; your delivery base rates.

**Steps**
1. Reference point first [01]: open with their annual cost of the problem (from Playbook 1), before any price.
2. Outside view [01]: your historical frequencies: "Of our last N workflows, X still run untouched; Y needed a rebuild when the client changed systems."
3. Two-sided message [02]: three named risks, each with its handling.
4. Argue against your interest [02]: one thing you recommend not automating yet, and why.
5. Shrink the imagined failure [07]: define failure narrowly (threshold, window, remedy): "if mis-routing exceeds 1 in 20 in 30 days, we rebuild or refund the pilot."
6. Do not inflate the relief [07]: measured outcome plus how it is tracked; no "transform."
7. Reversibility then commitment [07, 02]: 30-day pilot, then a fixed term; state why the term exists.
8. Symmetric terms [09]: what you deliver by when; what they owe only after. Put the guarantee where it costs you.
9. One default [08]: the recommended plan pre-selected; alternatives on request. Frequencies, not percentages [01, 09].
10. Cognitive ease [01]: one page, short sentences, one repeated phrase for the outcome.

**Output artifact**: Proposal skeleton — Cost of problem → Base rates → Three risks and handling → What we won't do → Pilot terms (threshold, window, remedy) → Measured outcome and tracking → Term and why → Payment symmetry → Recommended plan.
**Common failure**: leading with features and price; the prospect compares on dimensions they will never experience at consumption [07].

---

## 4. LinkedIn post or cold outreach for a sceptical owner audience

**Goal**: peripheral-route content that does not trigger identity defence.
**Inputs**: one peer story with numbers; the audience's identity language.

**Steps**
1. Reverse-engineer the resistance [09]: what does "no AI" protect? Status, independence, trade identity. Name the goal, not the emotion.
2. Lead with a similar peer, not with AI [02, 09]: same trade, same size, specific town.
3. Frequencies [01, 09]: "9 of the last 10 kept it running past 90 days; 1 dropped it when they changed phone systems."
4. Identity-safe metaphor [10, 09]: "a receptionist who never goes home," not "modernise."
5. Vivid, specific success to offset the vivid failure story they already carry [03].
6. Granular emotion word [06]: name the specific state removed ("Sunday-night callback dread"), not "stress."
7. One doable instruction with any fear [02]: "listen to one week of your missed calls."
8. Symmetry and costly commitment in the CTA [09]: "you pay nothing until you've heard the first week of captured calls."
9. Scout check before posting [10]: selective skeptic test: would you believe this claim from a competitor? Cut what fails.

**Output artifact**: Post/email template — Peer + place + boring change → Frequency line → Identity-safe metaphor → Specific state removed → One instruction → Symmetric CTA.
**Common failure**: "forward-thinking owners are adopting AI," which makes the sceptic's identity the thing under attack and produces soldier mindset.

---

## 5. Onboarding and the first 90 days so the client keeps feeling the gain

**Goal**: adoption by staff, durable satisfaction, accurate attribution.
**Inputs**: signed engagement; staff list; pre-launch baseline metrics.

**Steps**
1. Fix the baseline before go-live [01, 08]: hours, error counts, cycle times; otherwise regression to the mean gets credited or blamed.
2. Post-signing confirmation [02]: short note confirming the decision and the first milestone date.
3. Predict the bumps [06]: "week one feels like more work; week three goes quiet."
4. Situational design for adoption [08]: default to the new path; remove the old shortcut; name an internal owner.
5. Foot-in-the-door [03]: the ops lead runs the first five cases personally before the team sees it.
6. Spaced training with retrieval [03]: three 15-minute sessions over two weeks, each opening with a 3-question quiz.
7. Reinforcement taper [03]: every success announced in week one; daily tally in week two; weekly after.
8. Adaptation counter [03, 07, 09]: dashboard tile "hours returned since go-live" against the fixed baseline; peer comparison where you have it.
9. Attribution log [03, 08]: what the automation handled vs what humans handled, from day one.
10. Peak-end design [01, 07]: the 90-day review is the peak: a measured before/after on their own data, presented to the owner and the ops lead together.
11. Ask for the label at the review [06]: "what's the feeling about it now, if you had to name it?" Record it; it is your testimonial and your surrogate for the next prospect [07].

**Output artifact**: 90-day plan — Baseline sheet → Confirmation note → Bump forecast → Adoption defaults and owner → Training schedule with quizzes → Reinforcement schedule → Dashboard tile spec → Attribution log → Review agenda.
**Common failure**: a single long handover session and no baseline; by month three the client has adapted, cannot feel the gain, and attributes the improvement to their team.

---

## 6. Your own win/loss review and forecast calibration

**Goal**: learn what actually predicts closes and shipping, instead of what you remember.
**Inputs**: last 20+ proposals with dates, stakeholders, terms, and outcomes.

**Steps**
1. Ignore stated reasons [08]: "budget" and "timing" are confabulated; code behaviours (ops lead joined, pilot offered, days to reply, asked about ownership).
2. Small-sample humility [08, 01]: 20 is a hypothesis generator, not a finding.
3. Self-selection check [08]: who got offered a pilot and why, before concluding pilots close.
4. Randomise one variable for the next 20 [08]: pilot offered or not within qualified leads.
5. Equivalent bet [10]: write P(close) and P(ships on time) per live proposal; score quarterly; compare to your historical hit rate.
6. Five tests on your biggest open deal [10]: double standard, outsider, conformity, selective skeptic, status quo bias.
7. Premortem on your pipeline [01]: "it's Q+2 and revenue missed; why?"
8. Update one belief by one notch [10]: a specific sentence, a specific direction, written down.
9. Check your affect [06]: deals you feel "cold" about on a tired day get re-rated after sleep.

**Output artifact**: Win/loss sheet (behaviour codes, outcome, your pre-call probability, result) + Quarterly calibration score + Belief-update log.
**Common failure**: overhauling the pitch after one loss (over-updating) or explaining every loss by the prospect's disposition (fundamental attribution error, [08]).
