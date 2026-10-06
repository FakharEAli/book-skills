# Mode: interview

## Purpose
Fill `context/` with the user's real business facts in six short rounds, writing each file as its round ends, so every other skill can trust it: specific ICP, scoped offers, real prices, and an evidence ledger where nothing unproven passes as proof.

## Inputs
- Resolved workspace (SKILL.md §1); none → READ `init.md` first.
- All six `context/*.md` files. A section is **empty** if it holds only its instruction comment and example line.
- Bootstrap pre-fill (tagged `(from: <source>)`) and anything said in the opening message.
- **Connector category:** none. A URL offered mid-interview → ask, then follow `bootstrap.md` step 2.
- If `$ARGUMENTS` names a round (`business`, `icp`, `offers`, `pricing`, `evidence`, `voice`), run only that round.

## Procedure

**Round rules (apply to every round).**
- One AskUserQuestion call per round, at most 4 questions, each with 2–4 concrete options plus the implicit "Other". Use `multiSelect` where several answers can be true (segments, roles, triggers).
- Sections that already have content (bootstrap, earlier session): show in one line, ask "Keep / Correct". Ask only about gaps; skip a round with none.
- After the answers: write the file (remove each filled section's example line), append the log line, show Output §A, start the next round.
- Follow up only when an answer is unusable later: no segment, no price number, a claim with no specifics.

### Round 1 · Business, services, who you've sold to → `icp.md` (header) + `offers.md` (service list)
Positioning starts from the customers who already love you (Dunford, Five Components of Positioning, `offer-creation` book 03).
1. "What do you sell, in one line?" Options from what is known (e.g. "Done-for-you builds", "Monthly retainer", "Training").
2. "Which services do you deliver today?" (multiSelect).
3. "Who have you sold to so far?" Options: "0 clients yet", "1–3", "4–10", "10+". For 1+, follow up: industry and size of each (not names).
4. "How do most clients find you?" Options: referral, outbound, content, inbound/website.
Write `offers.md` `## Services delivered` and `icp.md` `## Who has bought before`.

### Round 2 · ICP → `icp.md`
Use the Customer Profile (jobs, pains, gains; Osterwalder, `offer-creation` book 02) and the push force of the Four Forces of Progress (Moesta, `offer-creation` book 07) for triggers.
1. "Which segments do you want more of, at what size?" (multiSelect; options from round 1 client types × "1–10 / 11–50 / 51–200 / 200+ staff").
2. "Who signs and who pushes for it?" (multiSelect) Owner/MD, operations or practice manager, finance, an internal champion.
3. "What happens right before someone needs you?" (multiSelect) e.g. "Lost a key admin person", "Growth broke a manual process", "Missed leads", "New system rollout".
4. "Who is NOT a fit?" (multiSelect) e.g. "Under <size>", "No budget owner", "Wants it free first".
Write `## Segments`, `## Firmographics`, `## Buyer roles`, `## Triggers`, `## Disqualifiers`; pains named in passing → `## Pains (their words)`.

### Round 3 · Offers and alternatives → `offers.md` + `competitors.md`
Value Equation (Hormozi, `offer-creation` book 01) for outcome, time delay and risk; hiring and firing (Christensen, `offer-creation` book 08) for alternatives.
1. "For your main offer: what result does the client get, measured how?" Options: hours saved per week, lead response time, error rate, revenue recovered, "not sure yet".
2. "Scope and timeline?" Options: "Fixed build, 2–4 weeks", "Fixed build, 4–8 weeks", "Monthly retainer", "Pilot then build".
3. "Do you offer a guarantee?" Options: "None", "Conditional (we keep working until X)", "Money back if X by date", "Pay on result".
4. "What do buyers compare you to, or do instead?" (multiSelect) "Do nothing", "Hire a VA / admin", "DIY tools (Zapier, Make)", "Their software vendor", "Another agency".
Write one `## Offer: <name>` block per offer (outcome, measure, scope, delivery, timeline, guarantee, exclusions) and each alternative into `competitors.md` (unknown fields stay gaps).

### Round 4 · Pricing → `pricing.md`
WTP conversation and Leaders, Fillers, Killers (Ramanujam, Tacke, `offer-creation` book 04).
1. "Price for the main offer?" Options as ranges in the user's currency, plus "Depends on scope". If "depends", ask the typical and the smallest real deal.
2. "Your floor, the price below which you walk?" Options: "Same as list", "10–20% under", "No floor yet".
3. "What do you anchor against?" Options: "Cost of a hire", "Hours saved × hourly rate", "Cost of lost leads", "Competitor quotes", "Nothing yet".
4. "When they push on price, what do you trade instead of discounting?" (multiSelect) "Smaller phase 1", "Upfront payment", "Case study rights", "Longer contract".
Write `## Price list`, `## Floor`, `## Anchors`, `## Trades instead of discounts`. Never fill a price the user did not give.

### Round 5 · Evidence → `evidence.md` (be strict)
Specific claims beat general ones (Hopkins, `copywriting` book 04); proof from hard messengers (named clients, numbers, third parties) outweighs self-description (Martin, Marks, `marketing-psychology` book 09); keep "what I know" separate from "what I hope" (Galef, `human-psychology` book 10).

1. Open: "List every result, client, testimonial or number you'd stand behind in front of that client. Rough is fine." Seed with claims from the opening message and bootstrap, labelled by origin.
2. For each candidate, ask (batch up to 4 questions per AskUserQuestion call):
   - "What exactly happened?" → number and unit, period, client (named or described: "a 3-site physio clinic"). Always offer "Not sure / I'd have to check".
   - "Where can you show it?" Options: "Client email / message", "Dashboard or report", "Signed testimonial", "Public case study URL", "Only my memory".
   - "Can the client be named publicly?" Options: "Yes, they agreed", "Describe, don't name", "No".
3. **Classify with this decision rule. No exceptions.**
   - `verified: Y` only if: specific (a number with a unit, or a concrete described outcome), dated (month or period), source is an artefact other than "my memory", and the user confirmed it this session.
   - Otherwise `verified: N` and the row goes in `## Unverified — do not use`, with the "to verify" column saying exactly what is missing (e.g. "number of hours; which clinic; before/after source").
   - Vague words ("loads", "a lot", "huge", "a few", "significantly") are never turned into numbers. If the user gives a number, record it as said ("about 6 hours a week" stays "about 6 hours a week", not "6+ hours").
   - `public-safe: Y` only on "Yes, they agreed" or a public URL. "Describe, don't name" → `N` for the name, with an anonymised wording in "exact wording allowed".
   - "Exact wording allowed" is the sentence outbound copy may use, no stronger than the source; agree it with the user.
4. Read the ledger back and ask "Anything here overstated?" Downgrade anything the user hesitates on.

### Round 6 · Voice → `voice.md`
1. "Paste 2–3 things you wrote and like (an email, a post, a proposal paragraph)." If none: "Like I talk on calls", "Plain and direct", "Warm", "Formal".
2. "Words or phrases you never want used?" Options: hype words, AI buzzwords (leverage, unlock, seamless), corporate filler.
3. "How do you sign off and address people?" Options: first name + short sign-off; formal.
From the samples write: average sentence length, formality (1–5), contractions, signature phrases (quoted), structure habits, banned words; samples verbatim in `## Samples`.

### Closing
Show Output §B and the single best next command. Zero verified evidence rows → the next step is collecting one artefact, not outreach.

## Output

**A. After each round:**
```markdown
**Round <n> · <name> → `context/<file>.md` written**
Filled: <sections>
Gaps: <sections left empty, or "none">
Unverified: <count> (round 5 only)
Next: Round <n+1> · <name>
```

**B. At the end:**
```markdown
**Setup complete: <workspace path>**
| File | Status |
|---|---|
| icp.md · offers.md · pricing.md · voice.md · competitors.md | <filled / partial: missing X>, one row each |
| evidence.md | <V> verified · <U> unverified (do not use) |
Best next step: <one command and why>
```

## Write-back
- `evidence.md` rows use the table columns exactly: `| claim | exact wording allowed | source | date | public-safe (Y/N) | verified (Y/N) |`; unverified rows add `| to verify |`.
- Client phrases the user quotes → `memory/voc-swipe.md`: `- "quote" — setup interview (user recall), YYYY-MM-DD, <segment>`.
- `log.md`, one line per round: `- YYYY-MM-DD · setup · interview · round <n> <name>: <files written>, <V> verified / <U> unverified`.

## Quality gate
- [ ] ≤4 questions per round, concrete options in the user's industry.
- [ ] Evidence rule: no row is `verified: Y` without specific claim + date + artefact source + confirmation. No vague claim was turned into a number; nothing was rounded up.
- [ ] Opening-message and bootstrap claims stay `N` unless confirmed with a source.
- [ ] No price, client name or result appears that the user did not state.
- [ ] Each file written before the next round; example lines removed; nothing overwritten without the user choosing.

## Failure modes
- **Inventing specificity.** "Saved loads of time" written as "saved 10+ hours/week". Fix: record it as said under Unverified and ask for the number and source.
- **Leading the witness.** Big-number-only options nudge overstatement; always include "Not sure".
- **Interrogation fatigue.** Use options, accept short answers, allow resume with `/book-skills:setup interview <round>`.
- **Generic ICP.** "SMBs" is not a segment. Push once for industry + size + role, then flag the gap.
- **Losing answers.** Write per round, never only at the end.
