# Mode: debrief

## Purpose
Turn one sales call into a scored, evidence-backed coaching note; an updated deal file with the gap in the buyer's own numbers; verbatims and objections added to memory; and a follow-up draft that recaps in their words and proposes one dated Advance. Nothing may claim the buyer said something they did not say.

## Inputs
- **The transcript** (call-recorder connector, see `CONNECTORS.md`):
  - *Link*: use a recorder tool that resolves a URL or call ID (names containing `recording_by_url`, `call_id`, `transcript`), then fetch the full transcript with timestamps.
  - *`latest`*: list meetings from the last 14 days and take the most recent where at least one attendee's email domain differs from the user's own domain (get it from the recorder's identity tool, `context/voice.md`, or ask once). Skip internal-only calls and calls under 5 minutes. Print one line before continuing: `Debriefing: <title> · <YYYY-MM-DD> · <attendees>`.
  - *Pasted text*: use as-is. If it has no timestamps, number the lines and use `L<n>` references.
  - *Fallback* (no recorder tool, or fetch fails): ask the user to paste the transcript or their notes, and stop until they do.
  - Notes or a summary instead of a transcript: say so and label every quote "notes, not verbatim".
- **Deal context**: `deals/<slug>.md` if it exists; the latest `assets/prep/*-<slug>.md` (its target Advance is the call goal); `memory/objections.md`; `context/offers.md`, `context/pricing.md`, `context/evidence.md`, `context/voice.md`.
- **Email connector** for the draft (tools named `create_draft`); fallback `assets/follow-ups/`.

## Procedure
1. **Identify the call.** Company, buyer (name, role as stated), seller(s), date, link. Derive the slug (SKILL.md rule 9); check `deals/` for an existing file.
2. **Dispatch the scorer.** Use the Agent tool with `subagent_type: "book-skills:call-scorer"`. The prompt must contain: the complete transcript text (or its absolute path if saved), seller name(s), buyer name, company, call date, source link, and the call goal. Never trim the transcript. If dispatch is unavailable, read `${CLAUDE_SKILL_DIR}/../../agents/call-scorer.md` and produce the same scorecard inline.
3. **Verify the scorecard before using it.** For every quote, confirm it appears in the transcript (search for a distinctive 5-8 word fragment). Remove any quote you cannot find and lower that component if it depended on it. Re-add the component scores; they must equal the total. An "Advance" with no date is "Advance missing date" (12 points), not 20.
4. **Set `stall_type`** (JOLT · Dixon & McKenna · `sales-psychology` book 02):
   - Buyer never stated impact in their own words → `status-quo`.
   - Else the scorecard's dominant indecision type → `valuation`, `information` or `outcome`.
   - Else, or if the call ended in an Advance with a date and no indecision signals → `none`.
   If the deal file already had a stall_type and this call produced a dated buyer commitment, set `none` and note "resolved" in the Timeline.
5. **Set stage and next step.** Apply the stage table in `${CLAUDE_SKILL_DIR}/templates/deal-file.md`. If an Advance was agreed, `next_step` is that action (who, what) and `next_step_date` its date, as said. If not, `next_step` is `"PROPOSED: <the Advance in your follow-up>"` and `next_step_date` the first date you propose. `last_touch` = call date. `value` only if the buyer stated a budget or the user agreed a price on the call; otherwise leave it unchanged.
6. **Fill the Gap** (Keenan · `sales-psychology` book 04). For current state, future state, impact, root cause and emotion, write the buyer's verbatim with its reference. Keep earlier entries; add newer ones beneath. For each missing element write `[NOT STATED: ask "<question>"]` with a real Implication or Problem question for the next call. Any number you derive (weekly × 52) is labelled `Derived (not stated)`.
7. **Choose the ONE recommendation** for the follow-up (JOLT Offer a recommendation). Pick the option from `context/offers.md` (or the options discussed on the call) whose scope addresses the buyer's highest-impact stated problem with the least extra scope. Write the reason as one sentence that uses their number. Never recommend an option the buyer said they do not need. If the stall is `valuation`, this paragraph is mandatory and the other options are named once as "later, if <condition>". If no offer fits, write `[NEEDS INPUT: which offer fits <problem>]` instead of guessing. If the stall is `status-quo`, recommend no offer; recommend the sizing conversation.
8. **Propose the Advance** (Rackham · book 01). Buyer action + who + date. Use the scorecard's "Available Advance" when the call ended in a Continuation. Propose two dates 2-5 business days out, never weekends, never in the past. If a decider was named but absent, the Advance includes them.
9. **Draft the follow-up.** Read `${CLAUDE_SKILL_DIR}/templates/follow-up-email.md` and apply the variant row for this outcome and stall. Recap current → future → impact using their words. No claim beyond `context/evidence.md` and `context/offers.md`; otherwise `[NEEDS PROOF: <what>]`. Save with the email connector's draft tool (never a send tool) or to `assets/follow-ups/<YYYY-MM-DD>-<slug>.md`.
10. **Write the coaching summary**: exactly five lines (format below). "Do differently" is the single coaching note worth the most points; the yellow light is the first one scored N, else the first scored Partial.
11. **Write back** (next section), then show the Output.

## Output

```markdown
## Debrief · <Company> · <YYYY-MM-DD> · <source>
1. Score <NN>/100 (<band>) · Outcome: <Order | Advance | Continuation | No-sale>: <what, who, when or "no buyer action agreed">
2. Do differently next call: <one move> → say: "<exact line>"
3. Yellow light missed: <ref> "<buyer verbatim>" → name it: "<label or calibrated question>"  (or "None missed. Best handled: <ref> …")
4. Stall: <stall_type> → lever: <lever> (<Framework · Author · `sales-psychology` book NN>)
5. Next: <Advance agreed or proposed, date> · Draft: <email draft | path>

### Follow-up draft (not sent)
<the email>

### Deal file · deals/<slug>.md
stage <old → new> · stall_type <…> · next_step "<…>" · next_step_date <…> · last_touch <…> · value <… | unchanged>
Gap filled: <n>/5 · Still to ask: "<question>"

### Written to workspace
deals/<slug>.md (Timeline + Gap) · memory/voc-swipe.md (+<n>) · memory/objections.md (+<n>) · log.md

### Full scorecard
<scorecard from the agent, verified>
```

End with: "Send the draft, or change anything first?" Never send without a yes.

## Write-back
- **`deals/<slug>.md`**: create from `templates/deal-file.md` if missing (stage `discovery`, `source` from the user or "not stated"). Update frontmatter per steps 4-5, replace the Gap section with the merged version from step 6, add People named on the call, and append a Timeline entry:
  ```
  ### YYYY-MM-DD · <Discovery call | Follow-up call | Proposal review> · <link or "pasted transcript">
  - Score: NN/100 · Outcome: <…> · Advance: <what, who, date | "none: PROPOSED <…>">
  - Stall: <stall_type> · Lever: <lever>
  - Verbatims: "<quote>" [ref] · "<quote>" [ref]
  - Notes: <one line: biggest gap still open>
  ```
- **`memory/voc-swipe.md`**: append each scorecard verbatim under its category heading (`## Pains`, `## Desired outcomes`, `## Triggers`, `## Anxieties` (objections and worries), `## Alternatives`, `## Their words for the problem`; create a heading if missing). Line format (canonical, see `shared/workspace.md` §6): `- "<verbatim>" — <Company> call <link>[ref], YYYY-MM-DD, <icp segment | unknown>`. Skip exact duplicates.
- **`memory/objections.md`**: one block per objection or concern:
  ```
  ### YYYY-MM-DD · <Company> · "<objection verbatim>" [ref]
  - Real cause (hypothesis): <unanswered Six Whys item or JOLT type> · confidence <h|m|l>
  - Response on call: "<seller's words>" [ref] · Worked: <Y | N | unclear> (buyer next said: "<quote>")
  - Better next time: "<label or calibrated question>" (<Framework · Author · book NN>)
  - Source: <link>
  ```
- **`log.md`**: `YYYY-MM-DD · deals · debrief · <Company> · <score>/100, <outcome>, stall <type>, follow-up drafted`.
- No workspace: print these under "Would write to workspace".

## Quality gate
Before showing anything, confirm:
- [ ] Every quote in the summary, deal file, memory entries and email was found in the transcript. No quote was edited.
- [ ] Gap entries are the buyer's words; seller-only numbers are absent or labelled.
- [ ] Outcome classification follows Rackham: "send me something" or "I'll think about it" without a dated buyer action is a Continuation, and the summary does not call the call a success.
- [ ] stall_type follows step 4; the lever matches it; no urgency or scarcity appears anywhere if stall_type is an indecision type.
- [ ] The email has one recommendation, one call to action, a specific dated Advance, ≤ 170 words, and passes the evidence rule (`[NEEDS PROOF]` where needed).
- [ ] next_step is labelled PROPOSED unless the buyer agreed it.
- [ ] Scores sum to the total; the summary is five lines.

## Failure modes
- **Scoring the vibe.** A warm call with no Advance scores low. Say so plainly.
- **Recapping in your words.** "Streamline operations" is yours; "the front desk is drowning on Mondays" is theirs.
- **Menu follow-ups.** Re-sending three packages to a buyer who could not choose recreates the valuation problem.
- **Inventing the date.** A date the buyer did not agree to is PROPOSED everywhere.
- **Losing the learning.** Skipping the memory write-back makes the next prep generic.
- **Wrong call on `latest`.** Check attendee domains and print what you picked.
