# Mode: negotiate `<pasted pushback>`

## Purpose
Live help when a buyer pushes back. Classify the pushback, then give the exact words to say: a label and a calibrated question first, a scope or terms trade instead of a discount, a clear hold-or-cut decision, and what not to say. Fast: the user may be mid-thread or between calls.

## Inputs
- The pushback, verbatim (pasted email, message or the user's note of what was said). If the user paraphrases, ask once for the exact words if they have them; proceed either way.
- `deals/<slug>.md` if a company is named or inferable: the Gap (impact figures), quoted price, stage, decision maker, Timeline.
- `context/pricing.md`: list price, floor, and the "trades" list (what you give or take instead of discounting). If no trades list exists, use the default trades below and mark `[DEFAULT TRADES: add yours to pricing.md]`.
- `context/competitors.md` (for competitor pushback), `memory/objections.md` (what worked before for this objection).
- No workspace: work from the paste; ask for quoted price and the buyer's impact figure only if the answer depends on them.

## Procedure

1. **Classify** (one primary, one secondary at most). Cues → real cause to test:

   | Type | Cues | Usual real cause |
   |---|---|---|
   | Price | "too expensive", "budget is X", "can you do better" | value not felt; impact not agreed; testing for a discount |
   | Scope | "do we need all of this", "just the first part" | effort/disruption fear; one part matters most |
   | Timing | "next quarter", "after busy season", "not now" | cash timing; capacity; low urgency (status quo) |
   | Authority | "need to run it by…", "my partner decides" | not the decision maker; fear of looking wrong internally |
   | Competitor | "another agency quoted…", "we could use Zapier/VA" | unlike-for-like scope; looking for a reason; anchor shopping |
   | Risk | "what if it doesn't work", "we tried before" | outcome uncertainty / FOMU (JOLT, `sales-psychology` book 02) |

   Check `objections.md` for the same objection and reuse what worked, citing the entry date.

2. **Label + calibrated question** (Voss, `sales-psychology` book 05). Write one label ("It sounds like…", "It seems like…") naming the buyer's likely concern without agreeing to it, and one calibrated "What/How" question that makes them reveal the real cause. Optional: one no-oriented question ("Would it be a bad idea to…?"). Never "Why…?" (sounds accusatory). If the relationship feels tense, add a one-line accusation audit ("You might feel I'm about to defend every line of this…").

3. **Return to the impact** (Gap Selling, `sales-psychology` book 04). Pull the annual impact from the deal file and restate the trade-off in their numbers: `£X/yr gap vs £Y price = Z× return`. If the impact was never agreed, the next move is a question that re-confirms it, not a price move.

4. **Decide: hold price, trade terms, or cut scope.**

   | Situation | Decision |
   |---|---|
   | Impact agreed, ROI ≥ 5×, objection is price only | **Hold price.** Label, re-anchor on impact, trade terms if needed. |
   | Real budget cap stated, ROI ≥ 3× | **Cut scope to fit**, keep your rate: smaller start / phase 1 only. |
   | ROI < 3× or impact never quantified | **Do not negotiate.** Return to discovery; the gap is undersized. |
   | Competitor quote | **Compare scope like-for-like first.** Hold price if scopes differ; trade terms if they match. |
   | Timing or cash | **Trade terms**: milestone billing, later start, split payment. Hold price. |
   | Authority | **Not a price issue.** Ask to include the decision maker; offer a 15-minute joint review. |
   | Risk | **Take risk off the table**: pilot, exit clause, milestone billing (JOLT). Hold price. |
   | Final round, decision maker present, user chooses to defend a number | **Inverted Ackerman** (step 6). |

5. **Pick the trade** from `pricing.md` "trades" (Khalsa, `sales-psychology` book 10; Ramanujam price integrity, `offer-creation` book 04). Every concession is conditional: "If you can…, I can…". Default trades if none are listed: remove a filler item; phase the scope (phase 1 now, phase 2 later); slower timeline; buyer does a defined task (data export, content); payment upfront in exchange for a reduction of at most 5%; 12-month commitment for a lower monthly rate; case-study and referral rights; milestone billing. Never trade away the leader item that closes the gap.

6. **Inverted Ackerman, final price defence only** (Voss book 05, inverted for the seller). Use only if the buyer has agreed the gap and scope, trades are exhausted, and the user chooses to defend a number. Compute from `pricing.md`: P = quoted price, F = floor, G = P − F.
   - Move 1: P − 0.45G · Move 2: P − 0.75G · Move 3: P − 0.92G · Final: a precise, non-round number between Move 3 and F, never below F, plus one small non-monetary item (e.g. an extra training session) to signal the limit.
   - Between every move: a label or calibrated question, never an immediate counter. Tie each move to something received where possible.
   - Example: P 9,000, F 6,500, G 2,500 → 7,875 → 7,125 → 6,700 → final 6,590 + one extra handover session.
   - If the buyer needs below F: walk away politely, or cut scope (step 4). Say so plainly.

7. **Write the exact words.** A 3–6 line script in the user's voice (`context/voice.md`), in the channel they are using (spoken vs email). Order: label → calibrated question → impact restated → trade offered as "If…, then…" → Advance with a date. Email version ≤ 120 words.

8. **What NOT to say.** 3–5 lines specific to this pushback, e.g.: no percentage discount offered first; no "that's our standard rate"; no feature list to justify price; no criticism of the competitor; no "just checking in" follow-up; no new options added (option overload, JOLT).

## Output

```markdown
## Pushback: "<verbatim>"
**Type:** <primary> (+ <secondary>) · **Likely real cause:** <one line> · **Seen before:** <objections.md entry date + what worked | none>

**Decision:** <Hold price | Trade terms | Cut scope | Back to discovery | Ackerman> because <rule from table, with ROI = <impact> ÷ <price> = <r>×>

**Say this** (<call | email>):
> <label>
> <calibrated question>
> <impact restated in their numbers>
> <If you can …, I can …>
> <Advance with date>

**Trade on the table:** <trade> (from pricing.md | default)
**Hold line:** never below <floor>; <Ackerman steps if used: m1 · m2 · m3 · final + item>

**Don't say:**
- …
- …

*Method: <framework · author · skill book>*
```

## Write-back
- `deals/<slug>.md` Timeline:
  ```markdown
  ### <YYYY-MM-DD> · Pushback · <type> · pitch negotiate
  - Said: "<verbatim>" [<source>]
  - Response drafted: <label + question, one line> · Trade: <trade> · Price held at: <amount | moved to amount>
  ```
  Update `stall_type` if the pushback is clearly an indecision type (valuation / information / outcome). Set `stage: negotiation` only if the deal was at proposal or later.
- `memory/objections.md`: if the objection is new or the response differs from past ones, append `### <date> · "<objection>" · source: <deal slug, channel>` with `- Real cause: <hypothesis, unconfirmed>` and `- Tried: <response>`. After the buyer replies, ask the user what happened and add `- Result: …`.
- `memory/voc-swipe.md`: append the buyer's verbatim under `Objections` with date and source.
- `log.md`: `<date> · pitch · negotiate · <type>, <decision> · <slug>`.

## Quality gate
- [ ] Classification stated with the real cause to test.
- [ ] Label and calibrated question come before any trade or number.
- [ ] No discount without a trade; nothing below floor.
- [ ] Impact restated in the buyer's numbers (or flagged as missing).
- [ ] Exact words provided, in channel, with a dated Advance.
- [ ] Don't-say list specific to this pushback.
- [ ] Any claim about results or other clients passes the evidence rule.

## Failure modes
- **Reflex discount:** the first move is a question, never a number.
- **Arguing value with a feature list:** go back to their gap.
- **Treating authority or timing as price:** route to the right fix.
- **Ackerman too early:** it is a last-round tool; using it first trains the buyer to haggle.
- **Badmouthing the competitor:** compare scope, not character.
