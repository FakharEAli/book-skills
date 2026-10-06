# Eval results · v2.0.0 · 2026-10-06

Each case was run once with the plugin and once as plain Claude (no plugin), then graded blind (A/B order randomised) by a separate grader against the case's rubric files. Per-criterion verdicts and reasons below.

## deals-debrief-continuation-not-advance

| Criterion | With plugin | Baseline |
|---|---|---|
| classifies-continuation | PASS: "Score 20/100 (needs work) · Outcome: Continuation" with "Advance secured / 20 / 0", and the next step is recorded as "PROPOSED: Gareth Okafor and Leanne Price join a 20-minute walkthrough". | PASS: States "'Send me some info and I'll have a look' is a continuation, not an advance" and "it hasn't moved forward". It gives no numeric score, and the next step is written as "proposing a 20–30 min call", not as agreed. |
| coaching-names-the-advance | PASS: Gives an exact line with a buyer action and a when: "could we go through it together with Leanne for 20 minutes, Thursday or Monday?" | FAIL: The only exact line, "Could we get 20 minutes with her so she can shape it?", has no day or time. The close advice, "propose something specific, like a call with Leanne on a date", is not a line Jo could say. |
| flags-missed-yellow-light | PASS: Flags "[03:40], 'Tenants hated it.', which needed: 'What did they hate about it?'" and reports "Seller ~61%" talk time, plus the "[00:10] ~120-word pitch... before any question". | FAIL: It names the chatbot and Leanne yellow lights and the pitch-first opening, but gives no timestamp for any of them. The rubric requires each yellow light "with its timestamp". |
| follow-up-proposes-advance | PASS: Marked "DRAFT · not sent". It recaps "coming in from four directions" and "a black hole", the only ask is "20 minutes, Thu 08 Oct or Mon 12 Oct?", and proof is replaced by "[NEEDS PROOF: an anonymised example...]". | FAIL: The recap and the dated ask ("Tuesday 13th or Thursday 15th October" with Leanne) are good. But the email sits under the heading "Follow-up email" and is never marked as a draft or as not sent. |

## deals-debrief-valuation-stall

| Criterion | With plugin | Baseline |
|---|---|---|
| buyer-words-no-invented-proof | PASS: Quotes match the transcript ("sitting around fourteen percent", "nobody has time to ring round"). The derived figure is labelled "around £3,300 a week by my maths", the email claims no results, and it names the "[03:31] 'The phones are fine for us'" yellow light. | FAIL: The coaching cites no timestamps for any yellow light. It also says "All of these figures come from Priya" above derived figures ("about £3,300 a week, or roughly £170k a year"), which attributes them to her. |
| classifies-valuation-indecision | PASS: "Stall: valuation → lever: Offer a recommendation", supported by "[04:28] 'Because I keep flip-flopping.'", and "Outcome: Continuation: no buyer action agreed". | FAIL: It never classifies the stall as valuation-type indecision. The nearest it gets is "She's indecisive" under risks, with no stall type named. |
| dated-advance-in-follow-up | PASS: The single CTA is "20 minutes with you and Martin to decide whether Fill goes ahead. Does Thu 08 Oct or Fri 09 Oct work better?", and the deal file records it as "PROPOSED". | FAIL: The email has two asks, "I'm also happy to join a 15-minute call with you both" and "Could we grab 20 minutes on Thursday or Friday", so it lacks a single call to action. |
| recommends-one-option | PASS: "My recommendation: Fill", with "I'd leave Front Desk aside; you told me the phones and intake forms work fine. Remind alone leaves cancelled slots empty." | PASS: Says "I'd go for Fill", tied to her cancellations and forgetting, with "Why not Front Desk" and "Why not Remind". The side-by-side table is secondary to the recommendation. |

## deals-rescue-outcome-uncertainty

| Criterion | With plugin | Baseline |
|---|---|---|
| classifies-outcome-uncertainty | PASS: "Diagnosis: OUTCOME UNCERTAINTY", supported by the whiteboard and "I'm not technical" quotes, and it rules out status quo with "We probably lose eight, ten grand a month". | PASS: "She's afraid of the outcome" and `stall_type: outcome uncertainty`, supported by the Monday-morning quote, and it rules out status quo with "The quotes thing is killing us though, I know that." |
| no-oriented-and-dated-advance | PASS: Includes "Would it be a bad idea to take 20 minutes with you and Kerry on Wednesday 14 Oct", the variant "have you given up on getting every quote followed up", and a phone/voicemail alternative. | FAIL: No no-oriented question appears anywhere. The ask is "Would a 15-minute call this Thursday or Friday help". |
| no-pressure-no-fomo | PASS: The drafts contain no banned phrases and no urgency. It explicitly rejects "Tying it to boiler season". | FAIL: The draft adds seasonal urgency: "If we start in the next week or so, the follow-ups would be running before the worst of the boiler season". |
| takes-risk-off-the-table | PASS: Centres on "Phase 1 only, quote follow-up, £3,200, two weeks... You can stop after Phase 1" and "named contact... daily health check... within 4 business hours". It answers Kerry with "Kerry never fixes anything" and flags the fallback as [NEEDS APPROVAL]. | PASS: Leads with "it's mine to fix, not Kerry's. I'm your named contact... daily... within 4 working hours" and "starting with just the quote follow-up: £3,200, live in 2 weeks... you stop there". |

## lead-magnets-build-format-by-awareness

| Criterion | With plugin | Baseline |
|---|---|---|
| full-scorecard-content | PASS: Writes out 12 behaviour questions scored 0–3, "Maximum score = 3 × 12 = 36", and three bands with distinct diagnoses and actions. It ends with "CTA (the only one)" and "Status: unpublished draft". | FAIL: It builds a four-step self-audit with a tally sheet ("0–1 missed new callers a week"). There are no 10–15 questions with point-valued answer options and no maximum score. |
| justifies-by-awareness-stage | PASS: Names "the Unaware stage" ("Schwartz · 5 Stages of Awareness"), cites "I put it down to the season" and "Our phones are fine, honestly", and explains that a calculator asks owners to value something "they don't think is broken". | FAIL: It never names an awareness stage (Unaware) or Schwartz. It only says "Your six owners don't believe that yet". |
| no-invented-proof | PASS: Says "Public benchmarks: none used. The scorecard deliberately contains no statistics." The scenario is labelled "not a real clinic". | PASS: Every figure is a time estimate or the prospect's own input ("Use your own figures here, not industry averages"), and no stats or clients are invented. |
| picks-diagnostic-format | PASS: "A diagnostic scorecard, not an ROI calculator", with the calculator kept "for later". | PASS: It builds an audit-style "Lunchtime & After-Six Phone Check" and defers the ROI idea: "Build the ROI calculator later". |

## lead-magnets-no-invented-stats

| Criterion | With plugin | Baseline |
|---|---|---|
| delivers-full-report-draft | PASS: A full seven-section report with the "Profit lost per month = A × B × (C − D) × E × F" formula and "example inputs, not a benchmark". It uses "off the tools", has one CTA, and is marked "Status: unpublished draft". | FAIL: The report is complete, but it is presented as "the full report, ready for layout" and is never labelled as a draft. |
| no-invented-statistics | PASS: Says "Public benchmarks: none used", and sourced figures are replaced with "[NEEDS PROOF: share of UK homeowners who contact more than one contractor...]". | FAIL: It states "nearly 7 times more likely" and "more than 60 times" citing "Harvard Business Review, March 2011" with no URL, while admitting "I can't browse the web from here". It also uses the vague "Research across thousands of businesses keeps finding". |
| proof-handling-is-explicit | PASS: "I've left out every statistic I couldn't trace to a source", it lists the 2 NEEDS PROOF items, and it points to the 15-minute enquiry audit and to trade-platform surveys as ways to get real numbers. | PASS: Explains "I've only used figures I can tie to a named, published source", lists the sources plus a checklist to verify them, and offers an enquiry log and a 7-day test as ways to get real numbers. |

## outreach-reply-objection-advance

| Criterion | With plugin | Baseline |
|---|---|---|
| advance-with-time | PASS: Proposes '15 minutes, Thursday 8 Oct at 10:00 or Friday 9 Oct at 14:00? [CHECK CALENDAR]'. | FAIL: Next step is 'Happy to look at your current setup and tell you honestly whether it's worth changing' with no day, date or time. |
| classifies-objection | PASS: 'Class: objection' and 'Why change? Sam thinks the status quo is good enough' (Hoffeld Six Whys). | PASS: Calls it 'a soft objection, not a no' and diagnoses the Zapier line as 'a way of saying "we've got automation covered"' (anchored on existing tool). |
| moves-off-solution | PASS: Accepts 'the plumbing's there' then one open question: 'What's the part Zapier isn't handling today, the bits someone still does by hand...?' | PASS: Calls Zapier 'a solid base' then asks one open question: 'when a quote request comes in at 8pm, what does your Zap do with it right now?' |
| no-discount-no-bashing | PASS: No discount, neutral 'alongside Zapier', and 'No outcomes, numbers, client names or guarantees are in the draft.' | PASS: No concession, Zapier framed positively ('a solid base'), and no client results or numbers claimed. |

## outreach-write-needs-proof

| Criterion | With plugin | Baseline |
|---|---|---|
| limits-and-question-cta | PASS: Subject 'front desk role and callbacks' (5 lower-case words), body 80 words, opens on 'Fernbrook's front desk coordinator ad', ends 'Worth a look?'. | FAIL: Subject 'Your front desk coordinator ad' has a capital letter, body is well over 90 words, and the CTA asks 'Would a 15-minute call next week be useful?' |
| needs-proof-or-capability | PASS: Capability-only line 'We build missed-call text-back and automatic appointment reminders...' plus an 'Open proof gap' with a [NEEDS PROOF: physio or allied-health clinic result...] marker explained outside the email. | PASS: Proof slot is capability-only bullets ('the caller gets a text within a minute...') and notes say 'No proof in the email yet... add it as a single line'. |
| no-invented-results | PASS: Only capability and prospect facts; 'There are no client names, numbers or "we've helped clinics like yours" lines'. | PASS: Email describes only what 'my team automates' and restates the ad and reviews; no past clients or outcome figures. |

## pitch-negotiate-competitor-half-price

| Criterion | With plugin | Baseline |
|---|---|---|
| calibrated-question-on-other-quote | PASS: Asks 'What's actually in their quote? How are they handling the rebooking by text, and the dashboard across all three clinics?' before value. | PASS: Includes the open question 'What happens after go-live? Who fixes it when something breaks or Cliniko changes, and what does that cost?' about the other quote. |
| no-immediate-discount | PASS: Opens with label and question, says 'matching it is off the table', phase-1 price 'must stay at or above £5,500', Ackerman ends at £5,580. | PASS: Starts with 'Can we look at what's in their quote', never goes below £5,500, and ties lower figures to scope (phased £5,900) or terms ('If you can do X, I can do Y'). |
| returns-to-impact | PASS: '30 no-shows/wk × £65 × 48 wks = £93,600/yr' against '£10,800', 'ROI ... 8.7×', break-even about 3.5 no-shows a week, all correct. | PASS: '£93,600 a year (30 a week × £65 × 48 weeks)' vs '£10,800', with correct recovery scenarios '5 of those 30 slots a week ... £15,600'. |
| trades-scope-or-terms | PASS: 'If it doesn't, I can phase it: reminders and rebooking now, the dashboard later' plus milestone billing, and 'Compare scope, not character.' | PASS: Offers a phased start and full scope at £6,500 for upfront payment, 12-month commitment or case-study rights: 'If you can do X, I can do Y'; no disparagement ('If they can do all that for half, take it'). |

## pitch-proposal-one-recommendation

| Criterion | With plugin | Baseline |
|---|---|---|
| dated-next-step-and-no-invented-proof | PASS: 'A 30-minute review with Dana and Lee on Monday 12 October at 9:30am'; proof slots are marked '[NEEDS PROOF: past client results...]'. | PASS: Ends with 'A 30-minute review with you (and Lee...)... Tuesday 13 October at 9:30 or Thursday 15 October at 9:30' and has no client names or case results. |
| one-recommendation-explained | PASS: 'I've written one recommendation, not three tiers. Three options turn Dana's yes/no into a comparison exercise'. | FAIL: Presents three priced tiers 'Good £4,500 / Better £6,500 / Best £9,500'. |
| risk-reversal-matches-named-risk | PASS: 'Last year a service booked jobs into slots you didn't have. So the first month runs as a pilot with written success criteria', with a decision 'On Friday 13 November'. | PASS: 'Because of what happened last time' adds a shadow-mode week where 'Lee confirms each one' and 'you can cancel the monthly fee with no penalty' if the 10-minute target is missed by month two. |
| roi-math-from-given-numbers | PASS: '25 calls × 40% × 50% × £420 × 50 weeks = £105,000', '6 hours × £18 × 50 weeks = £5,400', '£110,400 ÷ £10,700 = 10.3×'. | PASS: Table shows 25 → 40% → 50% × £420 × 50 weeks = '£105,000' plus '6 hrs at £18' = '£5,400', compared with the £10,700 first-year cost. |

## setup-evidence-not-fabricated

| Criterion | With plugin | Baseline |
|---|---|---|
| asks-for-specifics-and-source | PASS: 'to verify: which clinics..., how many hours before and after, over what period, and an artefact such as a client email, report or testimonial'. | PASS: Asks 'For each clinic you've helped: what did you build, and what changed? (Hours saved per week...)', covering both the measure and the specific clinics. |
| no-fabricated-verified-evidence | PASS: Filed under 'Unverified — do not use' with 'verified: N', and 'I won't turn them into a number of clinics or hours saved'. | FAIL: It marks the claim 'Unverified' but then offers it as usable marketing copy: 'the honest version is: "I've helped a few small clinics cut down on admin time."' |
| structured-setup-flow | PASS: Offers '~/.book-skills/ (recommended)' or './.book-skills/', says 'Nothing that already exists gets overwritten', and maps each statement to offers.md, icp.md or evidence.md. | FAIL: Says 'I can't create files or folders for you', offers no ~/.book-skills/ workspace, and asks six numbered questions instead of a short round. |

**Caveats:** n = 1 per arm; rubrics were authored with the skills; blinding imperfect (plugin outputs reference its commands). Treat as a regression suite and a spec, not a benchmark.
