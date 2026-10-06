# Mode: review

## Purpose
Turn magnet results into a decision per magnet and segment (keep, iterate, kill) with stated thresholds, and record what was learned so the next `build` starts from evidence instead of taste.

## Inputs
- **Results per magnet, per segment, per channel, per period:** landing visits (or post impressions/comments if there is no page), opt-ins, replies, calls booked, and optionally deals opened/won.
- **Where from, in order:** (1) numbers the user pastes; (2) Forms connector (`typeform`, `forms`: responses and completion counts per form); (3) Database connector (`supabase`, `airtable`, `execute_sql`) if the user keeps a leads table; (4) the workspace: `deals/*.md` with `source: magnet` for calls and deals. Ask for whatever is missing in one message listing the exact fields; never estimate a missing count.
- **Registry and history.** `memory/magnet-learnings.md`: each magnet's build entry (segment, awareness stage, format, hypothesis, success thresholds) and earlier reviews.
- **Thresholds override.** If `memory/magnet-learnings.md` or `context/icp.md` contains a `thresholds:` line, use it instead of the defaults below and say so.

## Procedure

1. **Normalise the data** into one row per magnet × segment × channel × period:
   `magnet | segment | channel (warm: own audience/list · cold: ads/outreach/new audience) | period | visits | opt-ins | replies | calls | deals`.
   Never mix warm and cold traffic in one rate; they behave differently. If the channel is unknown, ask once; if still unknown, label the row "channel unknown" and do not compare it with labelled rows.

2. **Compute rates.** Show the arithmetic.
   - Opt-in rate = opt-ins ÷ visits (skip if visits unknown).
   - Reply rate = replies ÷ opt-ins (diagnostic for the nurture).
   - Call rate = calls ÷ opt-ins (the back-end decision metric).
   - Visit-to-call = calls ÷ visits.
   - Deals ÷ calls, if deals are known.
   Round rates to one decimal place; never round counts.

3. **Check the sample before deciding** (evidence strength, `offer-creation` book 09). A row is decidable when it has ≥ 100 visits and ≥ 14 days live, or ≥ 30 opt-ins. Below that, the decision is "insufficient data: keep running until <date or count>". Exception: 0 opt-ins after ≥ 100 visits is decidable as a front-end failure.

4. **Apply the thresholds.** The defaults are this plugin's starting rules of thumb, not industry benchmarks; say so when you show them. Once the workspace has three or more reviewed magnets, propose replacing each keep line with the median of the user's own kept magnets.

   | Metric | Traffic | Keep | Iterate | Kill |
   |---|---|---|---|---|
   | Opt-in rate | warm | ≥ 30% | 15–29.9% | < 15% |
   | Opt-in rate | cold | ≥ 15% | 5–14.9% | < 5% |
   | Call rate (calls ÷ opt-ins), needs ≥ 30 opt-ins | any | ≥ 5% | 2–4.9% | < 2% |

5. **Decide with the matrix.** One decision per decidable row.

   | Front end (opt-in) | Back end (call rate) | Decision | What to change |
   |---|---|---|---|
   | Keep | Keep | **KEEP** | Add distribution: a new channel, a repost with a comment-bait variant, use it in outreach. Leave the magnet alone. |
   | Keep | Iterate/Kill | **ITERATE back end** | Bridge, thank-you page, email 5 Advance. Check whether the magnet gives away the fix (diagnosis free, fix paid, `offer-creation` book 01) or attracts the wrong segment (check the qualifying field). |
   | Iterate | Keep | **ITERATE front end** | Headline (rescore on the Four Functions, `copywriting` book 02), lead type vs awareness (`copywriting` book 06), channel. |
   | Iterate | Iterate | **ITERATE one variable** | Front end first; one variable per test. |
   | Kill | any, or < 30 opt-ins | **ITERATE once, then KILL** | First failure: re-check the awareness stage and format against the `build` decision table; a mismatch is the likeliest cause. If the new version also fails: KILL. |
   | Kill | Kill | **KILL** | Record the likely cause. |

   Compare each row with the hypothesis in the build entry: met, partly met, or missed.

6. **Compare across segments and formats.** If one magnet runs in two segments, report each separately; it can be a keep in one and a kill in the other. If two formats ran for one segment, note which awareness-stage call the results support. Flag results that contradict the brief (e.g. a scorecard for "unaware" owners where every reply names a vendor → the segment may be solution-aware; suggest re-running `research`).

7. **Write a Learning Card per magnet** (Test Card / Learning Card, `offer-creation` book 09): observation (the numbers), insight (one sentence, labelled hypothesis), decision, next test with its success number set now.

8. **Lead with one recommendation**: the single most valuable change across all magnets (usually scaling the best keep, or fixing the biggest leak), then the table.

## Output

```markdown
# Magnet review · YYYY-MM-DD · period <start>–<end>
**Recommendation:** <one move> — because <numbers>.
Thresholds: plugin defaults (rules of thumb, not benchmarks) | user thresholds from <file>

| Magnet | Segment | Channel | Visits | Opt-ins | Opt-in % | Replies | Reply % | Calls | Call % | Deals | Decidable? | Decision |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

## <magnet-slug> · <segment> · <channel>
- Arithmetic: opt-in <opt-ins> ÷ <visits> = <x>% · call <calls> ÷ <opt-ins> = <y>%
- vs hypothesis: met | partly | missed
- Learning Card: observed … · insight (hypothesis) … · decision KEEP | ITERATE | KILL · next test: <change> · success = <metric ≥ number> by <date>

## Contradictions with the market brief
## Data gaps
```

## Write-back
- `memory/magnet-learnings.md`, one entry per magnet × segment reviewed:
  ```
  ## YYYY-MM-DD · <magnet-slug> · review
  - segment: <segment> · channel: <warm|cold> · period: <start>–<end> · source: <pasted | form tool | db | deals/>
  - numbers: visits <n> · opt-ins <n> (<x>%) · replies <n> (<x>%) · calls <n> (<x>%) · deals <n>
  - decision: KEEP | ITERATE front | ITERATE back | KILL | INSUFFICIENT DATA
  - learning: <one sentence, labelled hypothesis> · format <format> at awareness <stage>: supported | contradicted
  - next test: <change> · success = <metric ≥ number> by <YYYY-MM-DD>
  ```
- If a deal came from a magnet and its deal file lacks `source: magnet`, list it for the user to fix; do not edit deal files from this mode.
- `log.md`: `YYYY-MM-DD · lead-magnets · review · <n> magnets: <k> keep, <i> iterate, <x> kill · memory/magnet-learnings.md`

## Quality gate
- [ ] Every rate shows its arithmetic; counts are as given, never estimated.
- [ ] Warm and cold traffic never combined in one rate.
- [ ] Sample rule applied; undecidable rows say which count or date makes them decidable.
- [ ] Thresholds stated and labelled as plugin defaults or user thresholds.
- [ ] One decision per decidable row, from the matrix; one variable per next test.
- [ ] Insights labelled as hypotheses; no causal claim the data can't support.
- [ ] Evidence rule: no external conversion benchmark unless fetched with a URL; otherwise compare only with the user's own history.
- [ ] Learnings appended to `memory/magnet-learnings.md`.

## Failure modes
- **Killing on a tiny sample.** 4 opt-ins from 30 visits is noise. Apply the sample rule.
- **Comparing with "industry average" conversion rates.** Unsourced averages fail the evidence rule and rarely match the channel. Compare with the user's own magnets.
- **Changing three things at once.** The next review can't say what worked.
- **Blaming the magnet for a back-end leak.** High opt-in with no calls is usually the bridge or the CTA.
- **Forgetting the segment.** Results for one segment don't transfer to another.
