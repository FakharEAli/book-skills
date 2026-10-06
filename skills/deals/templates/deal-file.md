# Deal file template

Mirrors `shared/workspace.md` §4. Create at `deals/<company-slug>.md`. Fill only from sources (call, email, user's words, public web); anything unknown stays as written below.

```markdown
---
company: <Company name as they write it>
slug: <company-slug>
stage: lead | discovery | proposal | negotiation | won | lost | nurture
value:                 # expected first-year value, number only; blank until stated or agreed
currency: <from context/pricing.md, else blank>
source: outreach | magnet | referral | inbound | content
decision_maker: "<Name, role>"     # "not stated" until someone says who decides
champion: "<Name, role>"           # the person pushing for this internally, if any
stall_type: none | status-quo | valuation | information | outcome | decision-process
quoted_price:          # the number in the proposal, if one was sent
next_step: "<buyer action, who, what>"   # prefix "PROPOSED: " until the buyer agrees
next_step_date: YYYY-MM-DD
last_touch: YYYY-MM-DD             # last real contact with the buyer (not a draft you wrote)
closed:                            # YYYY-MM-DD when stage becomes won or lost
---

## Gap
- **Current state**: "<buyer verbatim>" [ref] · or [NOT STATED: ask "<question>"]
- **Future state**: "<buyer verbatim>" [ref]
- **Impact (their numbers)**: "<buyer verbatim with number>" [ref] · Derived (not stated): <calc, labelled>
- Impact (annual): <number, same currency, blank if unknown>   # machine-readable; pitch pricing reads this line
- **Root cause**: "<buyer verbatim>" [ref] · Hypothesis (unconfirmed): <…>
- **Emotion / personal stake**: "<buyer verbatim>" [ref]

## People
- <Name> · <role as stated> · <stance: champion | decider | influencer | blocker | unknown> · source: <ref>

## Open questions
- <what we still need to learn, and the exact question to ask>

## Timeline (append-only, newest last)
### YYYY-MM-DD · <Event: Prep | Discovery call | Follow-up drafted | Proposal | Rescue drafted | Reply | Won | Lost> · <link or "pasted transcript" or email subject>
- Score: <NN/100 or n/a> · Outcome: <Advance | Continuation | Order | No-sale | n/a> · Advance: <what, who, date or "none">
- Stall: <stall_type> · Lever: <JOLT lever or "none">
- Verbatims: "<quote>" [ref] · "<quote>" [ref]
- Notes: <one line>
```

Stage rules (apply the first that matches):

| Evidence | Stage |
|---|---|
| Buyer said yes to buy, signed or paid | `won` |
| Buyer or user ended it ("we've gone another way", disqualified) | `lost` |
| Price, terms or contract being discussed after a proposal | `negotiation` |
| Proposal sent or a proposal-review meeting agreed | `proposal` |
| A discovery call booked or held | `discovery` |
| Contact exists, no call yet | `lead` |
| Buyer asked to revisit later (≥ 60 days), or 3 unanswered rescue touches over ≥ 30 days | `nurture` |

Never move a stage backwards except to `nurture`. Never set `won` from a Continuation.
