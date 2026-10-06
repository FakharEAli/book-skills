# Mode: pipeline

## Purpose
Give one honest view of every open deal: what stage it is really at, what is overdue, what each deal needs next in one line, and what the pipeline is worth weighted by stage. The "next move" column is the value: each row applies the same rules the other modes use, so the user knows exactly which mode to run on which deal this week.

## Inputs
- **All deal files**: `deals/*.md`. Parse YAML frontmatter; also read each file's `## Gap` (is Impact a buyer verbatim?) and its last Timeline entry (last outcome: Advance or Continuation).
- **Stage probabilities**: defaults below, overridden by a `## Pipeline` section in `context/pricing.md` with lines `stage: <percent>` (e.g. `proposal: 40`). Use any stage the override names; keep defaults for the rest. Say which source you used.
- **Chat connector** (`slack`, `teams`): only when the user asks to post. Fallback and default: print in the conversation.
- **Database connector**: not needed; the markdown files are the system of record.
- No `deals/` folder or no files: say "No deal files yet. Run `deals prep <company>` or `deals debrief` to create the first one." and stop.

Default stage probabilities:

| stage | probability |
|---|---|
| lead | 5% |
| discovery | 15% |
| proposal | 35% |
| negotiation | 60% |
| won | 100% (closed, shown separately) |
| lost | 0% (closed, shown separately) |
| nurture | 2% |

## Procedure
1. **Parse.** For each file record: company, stage, value, currency, source, stall_type, next_step, next_step_date, last_touch. A file with broken or missing frontmatter goes in a "Needs repair" list with the field missing; do not guess values.
2. **Compute.** `days_since_touch` = today − last_touch. `overdue_days` = today − next_step_date when positive. `proposed` = next_step starts with "PROPOSED:".
3. **Flag** (several may apply; show the most severe first):
   - `OVERDUE <n>d`: next_step_date in the past.
   - `NO NEXT STEP`: next_step empty or next_step_date missing.
   - `UNCONFIRMED`: next step is PROPOSED and next_step_date is within 2 days or past.
   - `STALE`: days_since_touch > 14 in discovery, proposal or negotiation; > 45 in lead.
   - `GAP OPEN`: stage proposal or negotiation, but Gap Impact is not a buyer verbatim (a proposal priced on an unowned problem).
   - `NO VALUE`: value blank (excluded from totals, counted separately).
4. **Pick the next move** per open deal: apply the first rule that matches and write it as one line ≤ 15 words, naming the mode to run.

   | Condition | Recommended next move |
   |---|---|
   | stall_type valuation | `rescue`: recommend one option, drop the others (JOLT Offer a recommendation) |
   | stall_type information | `rescue`: name the 3 deciding criteria, set a decision date (JOLT Limit the exploration) |
   | stall_type outcome | `rescue`: pilot or phased start with exit terms (JOLT Take risk off the table) |
   | stall_type status-quo | `rescue`: one Implication question to size the problem; no offer (build impact) |
   | OVERDUE and days_since_touch > 7 | `rescue`: buyer missed the step; diagnose before chasing |
   | OVERDUE, recent touch | Do the step today, or agree a new date with the buyer |
   | Last Timeline outcome Continuation, or NO NEXT STEP | Ask for a dated Advance: <buyer action implied by stage> |
   | GAP OPEN | Book a 20-min sizing call before negotiating price (Keenan) |
   | proposal stage, no decision date | Agree a decision date (JOLT Limit the exploration) |
   | Call in the next 48h | `prep <company>` |
   | Call happened, no debrief entry | `debrief latest` |
   | otherwise | On track: <next_step> by <next_step_date> |

   Closed deals: `won` or `lost` with no matching entry in `memory/win-loss.md` → "Run `postmortem <company> <won|lost>`".
5. **Total.** Per stage: count, sum of value, weighted value = value × probability. Group totals by currency; never convert. Report open pipeline (lead to negotiation plus nurture), weighted open pipeline, and closed won / lost this calendar month and quarter (by the date of the Won/Lost Timeline entry).
6. **Pick this week's top 3.** Rank open deals by weighted value × urgency, where urgency = 3 if OVERDUE, 2 if stall_type ≠ none or UNCONFIRMED, 1 otherwise. List the three with their next move.
7. **Post only if asked.** If the user asked to post to chat, show the exact message (top 3 + totals, no buyer quotes, no personal data) and post only after an explicit yes.

## Output
```markdown
## Pipeline · YYYY-MM-DD · <n> open deals · probabilities: <defaults | context/pricing.md>

### This week (top 3)
1. <Company> · <stage> · <value> · <flag> → <next move>
2. …
3. …

### Open deals
| Company | Stage | Value | Days since touch | Next step date | Stall | Flags | Next move |
|---|---|---|---|---|---|---|---|
| <…> | proposal | 6,800 GBP | 21 | 2026-09-29 (OVERDUE 7d) | outcome | OVERDUE, STALE | rescue: pilot or phased start with exit terms |

### Totals by stage (<currency>)
| Stage | Deals | Value | Probability | Weighted |
|---|---|---|---|---|
| … | | | | |
| **Open total** | | | | **<weighted>** |
Unvalued deals: <n> (<companies>) · excluded from totals

### Closed
Won this month: <n> · <value> · Lost this month: <n> · Post-mortems missing: <companies or "none">

### Needs repair
<file · missing field> or "none"
```
Sort the open table by: flagged first (OVERDUE, then stall, then STALE), then weighted value descending.

## Write-back
- **`log.md`**: `YYYY-MM-DD · deals · pipeline · all · <n> open, <total> <currency> (weighted <w>), <k> overdue, top: <Company>`. This line is the trend record; do not create other files.
- **Deal files**: read-only in this mode. Do not change any frontmatter. If a file needs repair, list it; fix it only if the user says so.
- If posted to chat on approval: append `· posted to <channel>` to the log line.

## Quality gate
- [ ] Every open deal file appears exactly once, in the table or in Needs repair.
- [ ] Overdue flags are computed against today's date; days are integers.
- [ ] Every next move is one line, follows the rule table, and names a mode when one applies.
- [ ] Weighted totals = value × the stated probability; currencies are not mixed; unvalued deals are counted, not treated as zero.
- [ ] Probability source is stated.
- [ ] Nothing was posted without a yes; no buyer quotes or personal data in a chat post.

## Failure modes
- **Optimistic stages.** A deal at `proposal` with a Continuation as the last outcome is flagged, not celebrated. Trust the Timeline over the stage label.
- **Silent zeros.** Treating a blank value as 0 hides deals. Count them separately.
- **Generic advice.** "Follow up" is not a next move. Name the lever or the Advance.
- **Mutating files.** Pipeline is a read; changing stages here hides history. Changes happen in debrief, rescue or postmortem.
- **Converting currency.** Exchange rates are not in the workspace; report per currency.
