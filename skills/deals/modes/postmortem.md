# Mode: postmortem

## Purpose
Close a deal with a structured win/loss entry that separates what the buyer said from what probably happened, audits which frameworks held or failed, and turns the lesson into one concrete change each for the offer, outreach and discovery. Every fifth entry, regenerate the patterns block so the user sees the most common loss reason, average cycle and the source that closes best.

## Inputs
- **Target**: `postmortem <company> won|lost`. If won/lost is missing, infer from the user's words or the last Timeline entry; if still unclear, ask.
- **Deal file**: `deals/<slug>.md` (frontmatter, Gap, People, full Timeline). If missing, ask for: first contact date, source, value, what was proposed, the buyer's stated reason. Proceed with what you get and mark gaps.
- **Buyer's stated reason**: the closing email or call. Email connector (`search_threads`, `get_thread`) for the last thread with the buyer's domain; call recorder for the last call if the Timeline links one. Fallback: ask the user to paste the buyer's message. If the buyer gave no reason, write "not stated"; never write one for them.
- **Memory**: `memory/win-loss.md` (existing entries, for the count), `memory/objections.md` (entries for this company).
- **Context**: `context/offers.md`, `context/pricing.md`, `context/icp.md` (was this deal in the ICP?).

## Procedure
1. **Reconstruct the timeline.** From the Timeline list: first touch date, each call with score and outcome, each Advance and Continuation, each stall_type change, proposal date and value, close date. `cycle` = close − first touch, in days. Count calls, Advances, Continuations.
2. **Stated reasons.** Quote the buyer's own words for why they bought or did not, with source and date. Up to 3 quotes. No paraphrase in this field.
3. **Inferred real reason.** One sentence, with a confidence level and at least two pieces of evidence (refs to Timeline entries, scores, quotes). Test it against:
   - *Six Whys* (Hoffeld · `sales-psychology` book 09): which of why change, why now, why this category, why you, why this service, why spend was never answered in the buyer's words? Losses on "price" are usually an unanswered why change or why now.
   - *Status quo vs indecision* (Dixon & McKenna · book 02): did they own the problem (Gap Impact is a buyer verbatim) and still not decide (indecision, which type), or never own it (status quo)?
   - *ICP fit* (`context/icp.md`): was the deal outside the ICP or did it hit a disqualifier?
   For wins: what was the deciding moment (quote) and which move created it.
4. **Assign one category** from the list in `${CLAUDE_SKILL_DIR}/templates/win-loss-entry.md`. Wins use `won-<short reason>` (e.g. `won-pilot-derisked`, `won-referral-trust`).
5. **Framework audit.** For each, mark Held or Failed with one piece of evidence; skip any with no evidence and say "no evidence".
   - Discovery depth (SPIN · Rackham · book 01): Implication and Need-payoff present in scored calls?
   - Gap quantified (Keenan · book 04): buyer-stated impact before the proposal?
   - Trust (Maister · book 03): self-orientation moments in scorecards; did the buyer share awkward truths?
   - Moving off the solution and yellow lights (Khalsa · book 10): named or skipped?
   - Stall handling (JOLT · book 02): was the stall classified, and was the matching lever used, or was pressure or more information added?
   - Advance discipline (Rackham): Continuations vs Advances; any Continuation recorded as progress?
   - Risk reduction (Beckwith · book 07): was the service made tangible and safe (pilot, phase, exit), and did expectations match?
6. **Changes.** Exactly one each, concrete enough to act on this week, naming the file it belongs in:
   - Offer (`context/offers.md` or `pricing.md`; packaging per Ramanujam & Tacke · `offer-creation` book 04 if the loss involved option confusion or price).
   - Outreach (angle, trigger, segment; pointer for `memory/outreach-learnings.md`).
   - Discovery (a specific question to add to prep, tied to where this deal broke).
   Propose context-file edits as text; apply them only if the user says yes, since context files are the user's.
7. **Write the entry** with `${CLAUDE_SKILL_DIR}/templates/win-loss-entry.md`.
8. **Patterns.** Count entries in `## Entries` after appending. If the count is a multiple of 5 (5, 10, 15…), or the user asked, regenerate `## Patterns so far` at the top of the file using the template's patterns block, computed only from the entries. Under 10 entries, mark it "directional only". Replace the old block; never edit entries.

## Output
```markdown
## Post-mortem · <Company> · <WON | LOST> · cycle <n>d · <value> <currency> · source <source>
**Lesson in one line:** <the inferred real reason and the change it implies>

Stated (buyer): "<verbatim>" (<source, date>)
Real reason (inferred, <h|m|l>): <one sentence> · Evidence: <ref>, <ref>
Category: <category> · Unanswered why: <…>

| Framework | Held / Failed | Evidence |
|---|---|---|
| SPIN discovery | | |
| Gap quantified | | |
| Trust / self-orientation | | |
| Yellow lights / move off solution | | |
| Stall diagnosis (JOLT) | | |
| Advance discipline | | |
| Risk reduction | | |

Change → Offer: <…> (file) · Outreach: <…> (file) · Discovery: <…> (prep question)

Written: memory/win-loss.md (entry <n>) · deals/<slug>.md · log.md <· patterns regenerated>
```
If patterns were regenerated, print the block after the entry.

## Write-back
- **`memory/win-loss.md`**: append the entry (create the file per the template if missing); regenerate patterns per step 8.
- **`deals/<slug>.md`**: `stage: won | lost`; `stall_type`: for a no-decision loss, the final type; otherwise `none`. `next_step`: won → `"Kick-off: <first delivery step>"` with its date if known; lost → `"Revisit: <trigger to watch for>"` with `next_step_date` = close + 90 days. `last_touch` = date of the buyer's closing message. Append Timeline: `### YYYY-MM-DD · <Won | Lost> · <source of the decision>` / `- Stated: "<verbatim>" · Real (inferred): <…> · Category: <…> · Post-mortem: memory/win-loss.md`.
- **`memory/objections.md`**: if the loss reason is an objection not already logged for this company, add a block (debrief format) with `Worked: N`.
- **`log.md`**: `YYYY-MM-DD · deals · postmortem · <Company> · <WON|LOST> <category>, cycle <n>d<, patterns updated>`.

## Quality gate
- [ ] Stated reason is verbatim with a source, or "not stated". It is not paraphrased into the inferred reason.
- [ ] Inferred reason has a confidence level and ≥ 2 evidence refs; it never states the buyer's motives as fact.
- [ ] Exactly one category; exactly one change each for offer, outreach, discovery, each naming its file.
- [ ] Cycle computed from Timeline dates; value and currency from frontmatter.
- [ ] Patterns regenerated if and only if the count is a multiple of 5 (or asked); computed only from entries; small samples flagged.
- [ ] No context file edited without a yes.

## Failure modes
- **Taking "price" at face value.** Price is usually the polite reason. Check the Six Whys before logging `lost-price`.
- **Blaming the buyer.** "They weren't ready" is not a lesson. Find the move that would have revealed it earlier.
- **Hindsight certainty.** Inferences are labelled with confidence; evidence beats story.
- **Wins without lessons.** A win's deciding moment is the most reusable thing in the file. Record the question or term that unlocked it.
- **Patterns from five deals treated as law.** Mark them directional until n ≥ 10.
