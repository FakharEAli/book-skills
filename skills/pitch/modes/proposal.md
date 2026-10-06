# Mode: proposal `<company>`

## Purpose
Write one proposal for one deal that restates the buyer's gap in their own words and numbers, makes ONE recommendation, makes delivery tangible, takes risk off the table, prices against quantified impact, and ends in a dated Advance. Draft only; never shared.

## Inputs
- `deals/<slug>.md`: frontmatter (stage, value, currency, decision_maker, champion, stall_type), `## Gap`, every Timeline entry (debrief scores, Advances, verbatims).
- Debrief or prep files referenced in the Timeline (`assets/prep/…`), and the transcript via the **Call recorder** connector if a call link is present (fallback: ask the user to paste the transcript or notes).
- `context/offers.md` (the offer that fits), `context/pricing.md` (price, floor, trades), `context/evidence.md`, `context/voice.md`, `memory/objections.md` (this buyer's and the segment's named risks), `memory/voc-swipe.md`.
- If no deal file exists, use what the user pasted. Minimum to proceed: a current-state problem, one impact number, and who decides. Missing any of the three: ask for it in one message listing all three; do not invent.

## Procedure

1. **Readiness check (Gap Selling, `sales-psychology` book 04).** Confirm the deal file holds: current state, future state, impact in the buyer's numbers, root cause. Score each 0/1. If impact or root cause is 0, stop and say: "The gap isn't quantified yet; a proposal now becomes a price fight." Offer 3 discovery questions to close it (how much / how often / what happens when) and produce the draft with `[GAP NOT CONFIRMED: …]` only if the user insists.

2. **Gap section.** Build current state → future state → impact → root cause using buyer verbatims with source (`[Discovery call 2026-09-30]`). Impact math in their figures, annualised, formula shown, e.g. `14 missed enquiries/week × 22% close rate × £1,800 avg job × 48 weeks = £266,112/yr`. Label any input that is the user's estimate `(your estimate)`. Root cause names the mechanism, not the symptom ("no owner for after-hours enquiries", not "slow replies").

3. **One recommendation (JOLT "Offer a recommendation", `sales-psychology` book 02).** Pick the single scope that closes the largest share of the gap within the buyer's capacity. Write it as "We recommend…" with a 2-sentence reason tied to the gap. If the user asks for tiers (good/better/best, three options):
   - Reply once, briefly: three options turn a yes/no into a comparison and push buyers into a valuation stall; one recommendation with an optional phase 2 closes faster.
   - If they still insist: at most 2 options, one marked `Recommended`, the other framed as "smaller start" or "later phase", never a decoy. Never produce three.
   - Record the decision in the internal notes.

4. **Make the invisible tangible (Beckwith, `sales-psychology` book 07).** Implementation plan with named phases (e.g. "Map", "Build", "Prove", "Hand over"), an owner per task on both sides (their named people from the deal file; yours by role), buyer hours required per week, and what they will SEE at week 1, week 2 and week 4 (a screen, a report, a message their customer receives). Include one sample output: a mock of the artefact (the auto-reply text, the dashboard row, the weekly summary) built from their own data where available.

5. **Risk reversal (JOLT "Take risk off the table"; Hormozi guarantees, `offer-creation` book 01).** Choose by the risk this buyer named (search their Timeline and `objections.md`):
   - doubts it will work → paid pilot on one workflow with written success criteria and a stop/continue decision date;
   - cash or budget → milestone billing, each payment tied to a deliverable they can see;
   - lock-in or "what if you go away" → exit clause: 30-day notice, they keep all workflows, accounts and documentation.
   Pick one primary; at most one secondary. Promise only what `evidence.md` supports; state the conservative expected result.

6. **Investment framed against impact.** Price from `pricing.md` for the recommended scope. Show:
   - `ROI (year 1) = annual impact ÷ price`
   - `Payback = price ÷ (annual impact ÷ 12)` in months (weeks if under 2 months)
   - If ROI < 3×, flag it in the internal notes: either the gap is undersized or the scope is too big; never inflate the impact.
   Present price after the gap and plan, never first. No discounts in the document; trades from `pricing.md` stay in reserve for `negotiate`.

7. **Next step with a date (Advance, Rackham, `sales-psychology` book 01).** One concrete action, owner, date within 7 days of sending, e.g. "30-minute review with <decision maker> on Thu 15 Oct to confirm pilot start 19 Oct". Never "let me know your thoughts".

8. **Evidence audit.** Dispatch `book-skills:evidence-auditor` with the Agent tool. The prompt must include: the full proposal markdown, the full text of `context/evidence.md` (or "NO EVIDENCE FILE: treat every claim as unsupported"), and the instruction "List every claim about results, clients, timelines, capability or experience; for each, quote the matching evidence line or return NEEDS PROOF with a replacement." Apply every finding: replace unsupported claims with `[NEEDS PROOF: …]`. If dispatch is unavailable, do it inline with the same steps and say so.

9. **Render.** Fill `${CLAUDE_SKILL_DIR}/templates/proposal.md` exactly. Save markdown to `assets/proposals/<YYYY-MM-DD>-<slug>.md`. Then, if a **Decks** connector exists (Gamma, Canva, or the `pptx` skill), create a draft deck from the same content, one slide per template section, no extra claims; else if a **Docs** connector exists (Notion, Claude Docs, Google Drive), create a private draft doc. Never share, publish, or set link access; say "Draft created, not shared". If neither exists, the markdown is the deliverable; say which fallback was used.

## Output
The filled template (see `templates/proposal.md`), followed in chat by an internal note block, not part of the document:

```markdown
### Internal notes (not in the proposal)
- Gap readiness: current <0/1> · future <0/1> · impact <0/1> · root cause <0/1>
- Recommendation: <scope> · why: <1 line> · options shown: <1 | 2 (recommended marked)>
- Risk reversal: <type> · because buyer said "<verbatim>" [source]
- ROI: <impact> ÷ <price> = <r>× · payback <n> months
- Evidence audit: <n> claims, <n> supported, <n> NEEDS PROOF (<method: agent | inline>)
- Draft locations: <md path> · <deck/doc link or "none"> · not shared
- Trades held in reserve: <from pricing.md>
```

## Write-back
- `deals/<slug>.md` Timeline:
  ```markdown
  ### <YYYY-MM-DD> · Proposal drafted · assets/proposals/<file>
  - Recommendation: <scope> · Price: <p> · ROI: <r>× · Risk reversal: <type>
  - Proposed Advance: <action> on <date>
  - Status: draft, not sent
  ```
- Ask whether it was sent. Only when the user confirms sending: set frontmatter `stage: proposal`, `next_step`, `next_step_date`, `last_touch: <today>`, and append `### <date> · Proposal sent · <channel>`.
- `log.md`: `<date> · pitch · proposal · <company> draft, <r>× ROI · assets/proposals/<file>`.

## Quality gate
- [ ] Gap stated with at least 2 buyer verbatims, each with source.
- [ ] Impact in their numbers, formula visible; estimates labelled.
- [ ] Exactly one recommendation (or two with one marked Recommended).
- [ ] Plan names phases, owners, buyer hours, week 1/2/4 visible results, one sample output.
- [ ] One risk reversal tied to a named risk.
- [ ] ROI and payback math shown; price ≥ floor; no discount.
- [ ] Dated Advance with owner.
- [ ] Evidence audit run; zero unsupported claims remain unmarked.
- [ ] Draft only; nothing shared.

## Failure modes
- **Feature list instead of gap:** if the first page talks about you, rewrite from current state.
- **Menu of tiers:** creates a valuation stall; collapse to one.
- **Impact inflation:** using your benchmark instead of their number; label or remove it.
- **Vague plan** ("we'll build and test"): add what they see each week.
- **Guarantee you can't keep:** downgrade to pilot or milestone billing.
- **Continuation ending** ("happy to answer questions"): replace with a dated Advance.
