# Proposal template

Fill every `<field>`. Delete guidance lines in *italics* before saving. Buyer-facing text is second person ("you"), follows `context/voice.md`, and contains no unsupported claim (`[NEEDS PROOF: …]` instead). Target length: 600–1,100 words; one page per section in a deck.

```markdown
---
company: <Company>
deal: deals/<slug>.md
prepared_for: "<Name, role>"
prepared_by: "<User name, business>"
date: <YYYY-MM-DD>
status: DRAFT, not sent
valid_until: <YYYY-MM-DD, 14–30 days out>
---

# <Outcome in the buyer's words>, for <Company>
*Title = the future state, not your service name. ≤ 12 words.*

## 1. Where you are today
<2–4 sentences describing their current state in plain facts: volumes, tools, who does what.>

> "<verbatim about the problem>" — <Name, role> [<source, date>]
> "<second verbatim about cost, frustration or risk>" — <Name, role> [<source, date>]

## 2. Where you want to be
<2–3 sentences: the future state they described. Use their outcome words.>

## 3. What the gap costs you
| Input (your figures) | Value | Source |
|---|---|---|
| <e.g. missed enquiries per week> | <n> | <call date / their spreadsheet> |
| <conversion rate> | <%> | <…> |
| <average value> | <amount> | <…> |

**Annual impact:** <formula with inputs> = **<currency amount>/year**
*Label any input that is not theirs "(our estimate)". No benchmarks from other clients unless in evidence.md.*

## 4. Why it keeps happening
<Root cause in 1–3 sentences: the mechanism, not the symptom. End with why the current workaround cannot fix it.>

## 5. What we recommend
**We recommend <one scope, named>.** <Two sentences: why this closes the largest part of the gap with the least disruption to your team.>

*If, and only if, the buyer asked for options: add one alternative below, framed as a smaller start or a later phase. Never three.*
<Optional: **Smaller start:** <scope>. Choose this if <condition>. We still recommend the option above because <reason>.>

What is included:
- <deliverable tied to pain 1>
- <deliverable tied to pain 2>
- <deliverable tied to pain 3>

Not included (so there are no surprises): <items>. Phase 2, if you want it later: <one line>.

## 6. How it will work
| Phase | Weeks | What happens | Your owner | Our owner | What you will see |
|---|---|---|---|---|---|
| <Map> | 1 | <…> | <their name> | <role> | <e.g. a one-page map of your enquiry flow> |
| <Build> | 2–3 | <…> | <…> | <…> | <e.g. first live auto-replies in a test inbox> |
| <Prove> | 4 | <…> | <…> | <…> | <e.g. weekly report: response time, bookings> |
| <Hand over> | 5 | <…> | <…> | <…> | <e.g. documentation, recorded walkthrough, admin access> |

Your team's time: <n> hours in week 1, <n> hours/week after.

**Sample of what you will get:**
<A short mock of the real artefact, built from their data: the message their customer receives, a dashboard row, a summary email.>

## 7. Your risk, taken off the table
<One primary risk reversal matched to the risk they named, with exact terms:
- Pilot: "<scope>, <weeks>, success means <measurable criteria>. On <date> you decide to continue or stop; stopping costs nothing further."
- Milestone billing: "<n> payments, each due when <visible deliverable> is live."
- Exit clause: "30 days' notice, any time. You keep every workflow, account and document.">

What we can realistically expect: <conservative figure, supported by evidence.md or framed as the target with how it will be measured>.

## 8. Investment
| Item | Amount |
|---|---|
| <recommended scope> | <price> |
| <ongoing, if any> | <price / month> |
| **First-year total** | **<total>** |

**Return:** <annual impact> ÷ <first-year total> = **<r>×** in year one.
**Payback:** <first-year total> ÷ (<annual impact> ÷ 12) = **<n> months**.
Payment terms: <from pricing.md or the chosen milestone schedule>.

## 9. Next step
<Action> with <name(s)> on **<weekday, date>** at <time>. If that works, <the step after, with date, e.g. pilot kickoff on <date>>.
*One Advance, one owner, one date within 7 days of sending.*

## About us
<2–3 lines. Every claim from evidence.md; otherwise [NEEDS PROOF: …]. No logos or client names without an evidence line.>
```

## Deck mapping (when a Decks connector is used)
Slide 1 title (section title) · 2 today + verbatims · 3 the gap cost (table + formula) · 4 root cause · 5 recommendation · 6 plan table · 7 sample output · 8 risk reversal · 9 investment + ROI · 10 next step. No slide may add a claim that is not in the markdown.
