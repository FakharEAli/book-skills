# Mode: rescue

## Purpose
Restart a deal that has gone quiet or stalled on "let me think about it" by diagnosing why it stalled and applying the single lever that fits. The output is one message draft, an alternative-channel version, and a no-oriented variant, each ending in a small dated Advance. Pressure is not a lever: urgency added to an indecisive buyer deepens the indecision (Dixon & McKenna · `sales-psychology` book 02).

## Inputs
- **Deal history**: `deals/<slug>.md` (Gap, Timeline, stall_type, People). If missing, ask the user for: what was proposed, the buyer's last words, and dates of the last contacts. Also accept pasted notes or emails.
- **Email connector** (`search_threads`, `get_thread`): the last 5 threads with the buyer's domain, to get their exact last words and count unanswered touches since the stall. Fallback: the deal file Timeline, or ask.
- **Call recorder** (optional): the last call's transcript if the Timeline links one and the buyer's stall words are not quoted in the deal file.
- **Context**: `context/offers.md`, `context/pricing.md` (which risk terms exist: pilots, phases, support, guarantees, exit terms), `context/evidence.md`, `context/voice.md`; `memory/objections.md` for what worked before.

## Procedure
1. **Read the history.** Extract, with sources: the buyer's last words; the last buyer-stated impact; every concern they raised; what was proposed (offer, price, options); the dates of the last buyer message and of every seller touch since. Compute `days_quiet` = today − date of the last buyer message.
2. **Check timing.** If the buyer named a date they would come back and it has not passed, recommend waiting until that date and draft the message for that day. If there have been ≥ 3 unanswered seller touches over ≥ 30 days, go to step 8 (close the file).
3. **Classify with the JOLT decision tree** (Dixon & McKenna · book 02; Playbook 2 in `${CLAUDE_SKILL_DIR}/../sales-psychology/playbooks.md`):
   ```
   Has the buyer stated the problem's impact in their own words (Gap > Impact is a buyer verbatim)?
   ├─ No  → STATUS QUO: no owned problem. Lever: build impact.
   └─ Yes → INDECISION. Which signal is in their own words (most recent wins)?
        ├─ choosing between options, "which is best", "what would you do" → VALUATION → Offer a recommendation
        ├─ "need more info", asks for more case studies/demos, re-asks answered questions → LACK OF INFORMATION → Limit the exploration
        ├─ "what if it doesn't work / breaks", "my team won't use it", burned before → OUTCOME UNCERTAINTY → Take risk off the table
        └─ no signal in their words → UNKNOWN → the message is a Judge ping (step 5, ping variant)
   ```
   Record the classification with the quote that decided it. A decider who has not been involved is noted as a second issue; mention it in the message only if it is the buyer's stated reason.
4. **Choose ONE lever and its content.**
   - **Build impact** (Keenan · book 04; Dixon & Adamson · book 06): one Implication question in their words, or one reframe insight about their situation with a specific question. Offer a 15-minute sizing call. No offer, no price.
   - **Offer a recommendation**: name the one option that fixes their stated top problem, why in one sentence using their number, and what can wait.
   - **Limit the exploration**: the 2-3 criteria that decide this for them, where you stand on each in one line, and "more research won't change the picture". Propose a decision date.
   - **Take risk off the table** (also Beckwith · book 07): pick the terms that answer their stated fear, from this menu, only as they exist in `context/offers.md` / `pricing.md`:
     - *Pilot*: one workflow, fixed length, fixed fee, a written success threshold.
     - *Phased rollout*: shadow mode first (it drafts, a person approves), then one person, then the team; nothing changes for staff on day one.
     - *Support terms*: named owner, response time, monitoring that alerts before the team notices, a documented manual fallback ("if it stops, your team does exactly what they do today").
     - *Exit clause*: stop after phase 1 with nothing further owed, keep the documentation and workflows.
     - *Realistic expectations*: promise the threshold you always beat, lower than the headline.
     A term not in the workspace is written as `[NEEDS APPROVAL: <term>]` for the user to decide; never offer it as settled.
5. **Draft the primary message** (≤ 120 words, the channel the buyer last replied on):
   1. Label their concern using their words (Voss · book 05): "When we last spoke you said '<verbatim>'. That's a reasonable thing to worry about."
   2. The lever content from step 4.
   3. A small, dated Advance phrased as a no-oriented question: "Would it be a bad idea to take 20 minutes on <Day DD Mon> to <specific buyer action>?"
   *Ping variant* (UNKNOWN): "Before I send anything else: is the hesitation about whether to do this at all, which option, or whether it'll actually work for <their team/business>?"
6. **Draft the alternative channel** (≤ 50 words): a phone or voicemail script if the primary is email; an email if the primary was chat; or a note via the champion (People) if one exists. Same lever, same Advance.
7. **Draft the no-oriented variant** (≤ 40 words): "Have you given up on <fixing their problem, in their words>?" plus one line making it easy to answer either way ("Either answer is fine; it tells me whether to close the file or book the <step>."). Use it as the second touch if the primary gets no reply in 5 business days.
8. **Close the file** (only from step 2): one no-oriented message ("Have you given up on <X>? If so I'll close the file and won't chase.") and recommend stage `nurture`.
9. **Scan every draft for banned phrases** and remove them: "just checking in", "circling back", "touching base", "following up on my last", "any update", "bumping this", "limited spots", "price goes up", "offer ends", "before it's too late", "last chance", "don't miss out", and any deadline or discount not written in `context/pricing.md`. If stall_type is valuation, information or outcome, no deadline of any kind.

## Output
```markdown
## Rescue · <Company> · quiet <n> days · <stage>
Diagnosis: <STATUS QUO | VALUATION | LACK OF INFORMATION | OUTCOME UNCERTAINTY | UNKNOWN> · deciding quote: "<verbatim>" (<source, date>)
Lever: <one lever> (<Framework · Author · `sales-psychology` book NN>) · Why this, not more pressure: <one line>

### Message (DRAFT · <channel> · not sent)
<≤120 words>

### Alternative channel (DRAFT · <channel>)
<≤50 words>

### No-oriented variant (second touch, if no reply by <Day DD Mon>)
<≤40 words>

### Risk terms used
<term> · source: <offers.md line | [NEEDS APPROVAL]>

Not doing: <the tempting wrong move, e.g. "sending the case-study pack: feeds the information loop">
```
Then ask: "Send, edit, or switch channel?" Send only on an explicit yes.

## Write-back
- **`deals/<slug>.md`**: `stall_type` = the classification (UNKNOWN keeps the old value); `next_step: "PROPOSED: <Advance>"`; `next_step_date` = the proposed date; stage `nurture` only after the user approves a close-the-file message. Do not change `last_touch` (a draft is not contact). Append:
  ```
  ### YYYY-MM-DD · Rescue drafted · quiet <n>d
  - Stall: <type> (deciding quote: "<verbatim>", <source>) · Lever: <lever>
  - Advance proposed: <what, who, date> · Channel: <primary> / alt <alt>
  ```
  When the user confirms it was sent, set `last_touch` to the send date and add `- Sent YYYY-MM-DD`.
- **`memory/objections.md`**: if the stall exposed a concern not yet logged for this deal, add a block in the debrief format with `Response on call: n/a (rescue)`.
- **`log.md`**: `YYYY-MM-DD · deals · rescue · <Company> · <type> → <lever>, Advance proposed <date>`.

## Quality gate
- [ ] Classification cites a buyer quote with a source; status quo was ruled out by a buyer-stated impact before any indecision type was chosen.
- [ ] Exactly one lever; the message content matches it.
- [ ] No banned phrase, no fake urgency, no unapproved deadline or discount, no FOMO.
- [ ] Every risk term exists in the workspace or is marked `[NEEDS APPROVAL]`; every result claim passes the evidence rule.
- [ ] Every draft ends in a dated, small buyer action; the no-oriented variant is present.
- [ ] Word limits held: 120 / 50 / 40.

## Failure modes
- **More information to an information-stalled buyer.** Another deck extends the loop. Curate and close it.
- **De-risking a problem they don't own.** A pilot offer to a status-quo buyer reads as discounting. Build impact first.
- **Urgency theatre.** "Spots are filling up" to a buyer afraid of messing up raises the fear. Lower the stakes instead.
- **Stacking levers.** Recommendation + pilot + criteria + case study in one email is a menu. One lever.
- **Open-ended pilots.** A pilot with no end date or success threshold is exploration without end (book 02 anti-pattern). Fix length, fee and threshold.
- **Chasing forever.** Three unanswered touches over a month means close the file politely.
