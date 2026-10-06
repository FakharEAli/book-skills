# Templates: magnet formats

Use the section for the format chosen in `build` step 2. Every section produces finished content: fill every placeholder with real wording. Numbers come only from prospect inputs, `context/evidence.md`, or a fetched public source recorded in `sources.md`; otherwise `[NEEDS PROOF: …]`.

## A. Diagnostic scorecard / self-assessment (unaware)

```markdown
# <MAGIC name>
<One-line promise: "12 questions, 4 minutes: see where <outcome> leaks out of your <business>.">
Core sentence: <what the score proves>

## Dimensions (3–4; together they are the named mechanism)
1. <Dimension name> — <what it measures, one line>
2. …

## Questions (10–15; 3–5 per dimension)
Q1 [<dimension>] <Behavioural question in their words: "When a call comes in after 5 pm, what happens to it?">
- 0 · <worst observable behaviour: "It rings out; we see it in the morning, maybe">
- 1 · <…>
- 2 · <…>
- 3 · <best observable behaviour: "It is answered or called back within 15 minutes, every time">
Why we ask (shown on the result page): <one line linking the behaviour to a consequence; no statistic unless sourced>
(repeat through Q10–Q15)

## Scoring
- Max score = 3 × <number of questions>. Show the total and each dimension as a % of its max.
- Lowest dimension = "your biggest leak"; it drives the first recommendation.

## Bands (3)
| Band | Score range (% of max) | Label (social currency) |
|---|---|---|
| 1 | 0–40% | <e.g. "Leaky"> |
| 2 | 41–70% | <e.g. "Patched"> |
| 3 | 71–100% | <e.g. "Tight"> |

### Band 1 · <label>
Diagnosis (≤ 60 words): <what this pattern means, concrete, in their words>
Do this week (free, ≤ 30 minutes each):
1. <specific action>
2. <specific action>
3. <specific action>
What fixing it properly involves: <one line naming the gap the paid offer closes; not the build steps>
CTA: <one soft Advance, e.g. "Reply with your score; I'll send the first fix I'd make.">
(repeat for bands 2 and 3; band 3 gets a "keep it tight" action set and a lighter CTA)

## Result screen (tangible)
Score · band label · dimension bars · "Your biggest leak: <dimension>" · top 3 actions · one CTA
```

## B. Cost calculator (problem-aware)

```markdown
# <MAGIC name>
Core sentence: <"Your missed after-hours enquiries cost you <currency> X a month, in your own numbers.">

## Inputs (the prospect enters them; no pre-filled benchmarks)
| # | Input | Unit | Who in the business knows it | Allowed range |
|---|---|---|---|---|
| I1 | <Enquiries per week after hours> | count | <front desk / call log> | 0–500 |
| I2 | <Share you don't reach within a day> | % | <owner estimate> | 0–100 |
| I3 | <Share of reached enquiries that become jobs> | % | <owner / CRM> | 0–100 |
| I4 | <Average first-job value> | currency | <invoices> | > 0 |

## Formula
Monthly cost = I1 × 4.33 × (I2 ÷ 100) × (I3 ÷ 100) × I4
<State each step in words; name the formula as the mechanism.>

## Output sentence
"Based on your numbers, about <result> a month goes to whoever answers first." (to the nearest whole unit; never rounded up)

## Sensitivity line
"If you reached half of those, you'd keep <result ÷ 2>."

## Worked example (Example inputs, not a benchmark)
I1 = <n>, I2 = <n>%, I3 = <n>%, I4 = <n> → <arithmetic shown> = <result>

## Honest limits
<what it leaves out: repeat business, referrals, staff time>; "Your real figure will differ; this counts only what you entered."

## Bridge + CTA
```

## C. "Hidden cost" report (problem-aware)

```markdown
# <MAGIC name> · 1,200–2,500 words · 5–7 sections
Core sentence: …
## 1. The moment it happens (struggling-moment scenario, labelled illustrative unless from evidence.md)
## 2. Cost #1: <direct cost> — mechanism in plain words · "Work out yours:" <formula using their inputs>
## 3. Cost #2: <time / staff cost> — … · self-check
## 4. Cost #3: <knock-on cost: reviews, referrals, staff turnover> — … · self-check
## 5. Why it stays hidden (why nobody measures it; the habit of the present)
## 6. The 15-minute audit you can do today (numbered steps, free)
## 7. What fixing it involves (the gap, not the build) + one CTA
Every section ends with a self-check the reader answers with their own numbers.
Statistics: none unless sourced in sources.md; otherwise [NEEDS PROOF: <figure, segment, year>] or convert to a self-check input.
```

## D. Teardown, benchmark, or playbook (solution-aware)

```markdown
# <MAGIC name>
Subject: <anonymised example business, a public competitor page, or the prospect's own funnel with permission>
## Findings (5–8, numbered)
### Finding 1: <what we saw, concrete>
- Evidence: <screenshot description / quote / test result, with date>
- Impact: <consequence in their terms; numbers only if sourced or measured in the test>
- Fix category: <the kind of fix; not the build steps>
## Summary table: finding → pass / fail
## What good looks like: the standard, numbered
## Bridge + CTA
Playbook variant: 5–9 numbered plays, each with "when to use", "the play", "how you'll know it worked".
Benchmark variant: only with a sourced dataset (URL in sources.md) or the user's own measured data; otherwise build a teardown.
```

## E. ROI model, buyer's checklist, or case-study breakdown (product-aware)

```markdown
ROI model: inputs (current cost, solution cost, time to go live, expected change) entered BY THE PROSPECT or taken from evidence.md; payback months = one-off cost ÷ monthly gain; 12-month net; show the formula and a "conservative" column at half the expected change.
Buyer's checklist: 10–15 criteria, each with "Ask the vendor: …", "A good answer sounds like: …", "Red flag: …"; criteria may favour your unique attributes, honestly.
Case-study breakdown: only from evidence.md: situation, trigger, alternatives considered, what was built, result (exact figures), what the client said (verbatim). If no case exists: [NEEDS PROOF: case study] and switch to the checklist.
```

## F. Audit / offer (most-aware)

```markdown
Name · what the audit checks (5–7 items) · what they receive (a written one-page result) · time required from them · price or "free", with the honest capacity limit · one CTA with a specific booking action.
```
