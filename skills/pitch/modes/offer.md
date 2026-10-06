# Mode: offer `<segment>`

## Purpose
Produce ONE package for ONE segment by running stages 01–03 of the client-eagerness sequence (positioning → Value Proposition Canvas → Grand Slam Offer) filled from the workspace, not from imagination. Output a One-Offer Sheet and a proposed diff to `context/offers.md`.

## Inputs
- `context/icp.md` (the segment row: firmographics, buyer roles, triggers, disqualifiers), `context/competitors.md`, `context/offers.md`, `context/pricing.md`, `context/evidence.md`, `context/voice.md`.
- `memory/voc-swipe.md` (pains, gains, outcome words), `memory/objections.md` (named risks), `memory/win-loss.md` (who loved it, who walked).
- Every `deals/*.md` whose frontmatter or Gap section matches the segment: read the `## Gap` impact lines and any `WTP:` timeline lines.
- Fallback: if fewer than 3 deals or fewer than 10 verbatims exist for the segment, ask the user to paste call notes or answer 5 questions (what do they use today, what breaks, what does it cost them, what did they say when they hesitated, what would they pay). Tag the output `Confidence: low (n deals, n verbatims)`.

## Procedure

1. **Scope the segment.** One industry plus one expensive operational problem. If the user names a broad segment ("SMBs"), pick the narrowest sub-segment with the most deal files and say so. Rule: one offer per run (client-eagerness-playbook, stage rule).

2. **Positioning, Dunford's 10 steps** (`offer-creation` book 03). Fill each step from data, citing the file:
   1. Customers who love it: list won deals from `win-loss.md` in this segment; what they compared you to.
   2. Positioning team: name who should review (user plus anyone in `context/` who sells or delivers); mark `[USER TO CONFIRM]`.
   3. Baggage: the category the user currently calls themselves in `offers.md`; note if it invites the wrong comparison.
   4. Competitive alternatives: from `competitors.md` plus deal files. Always include "do nothing", "hire/VA", and "DIY tool". For each, its real strength.
   5. Unique attributes: only those the alternatives lack AND that `evidence.md` supports. Unsupported → `[NEEDS PROOF]`.
   6. Value themes: cluster attributes into 2–4 themes, each tied to a verbatim gain.
   7. Who cares a lot: traits shared by the deals with the largest quantified gaps.
   8. Market frame: choose Head-to-Head, Big Fish Small Pond, or Create a New Game. Default to Big Fish Small Pond for a niche service firm unless evidence shows you beat the leader on its own criteria.
   9. Trend: add one only if a buyer mentioned it in a verbatim.
   10. Capture: the positioning block of the sheet.

3. **Value Proposition Canvas** (`offer-creation` book 02). Customer Profile from `voc-swipe.md` only: jobs, pains, gains. Rank the top 3 pains by severity = (number of deals mentioning it) × (median quantified impact where known). Each pain shows one verbatim with source. Value Map: one pain reliever per ranked pain, one gain creator per top gain. A pain without a reliever is either out of scope (say so) or the offer is wrong.

4. **Grand Slam Offer, Value Equation** (`offer-creation` book 01). Score each lever 1–5 using this rubric, then write how to raise it:

   | Lever | 1 | 3 | 5 |
   |---|---|---|---|
   | Dream outcome | vague activity ("automation") | named result | named result in the buyer's verbatim, with a number |
   | Perceived likelihood | no proof | process shown, proof thin | matching proof in `evidence.md` + guarantee |
   | Time delay (5 = fastest) | first value > 90 days | first value 30 days | visible result in week 1 |
   | Effort & sacrifice (5 = least) | buyer does setup, data cleanup, training | shared | done-for-you, ≤ 2 hours of buyer time |

   Rule: do not price until every lever is ≥ 3. Fix the lowest lever first. Then list the problem → solution → delivery-vehicle stack and cut anything that does not raise a lever (Hormozi trimming). Mark items as leader / filler / killer (`offer-creation` book 04); remove killers or make them add-ons.

5. **Price, anchored to quantified gaps.** Collect every annual impact figure from the segment's deal Gap sections. Compute median and minimum. House rule (edit in `pricing.md` if the user prefers another): first-year price ≤ 20% of the median annual impact (buyer ROI ≥ 5×) and ≤ 33% of the minimum (ROI ≥ 3× even for the weakest fit). Show the math. Never price below the floor in `pricing.md`; if the rule lands below floor, the segment is wrong or scope must shrink, say which.
   - **WTP check** (Ramanujam, `offer-creation` book 04): if no deal file has a `WTP:` line, a stated budget, or a price reaction, mark price `Provisional` and generate 4 WTP questions for the next 5 calls, in the segment's language, adapted from the Van Westendorp meter: at what price would this be so cheap you'd doubt it works; a bargain; getting expensive but still worth it; too expensive to consider. Add: log answers as `WTP:` lines in each deal file.

6. **Guarantee chosen by the risk buyers actually named.** Count risk-type objections in `objections.md` for this segment. Pick the most frequent and map:

   | Named risk | Guarantee / risk reversal (Hormozi book 01; JOLT "take risk off the table", `sales-psychology` book 02; Beckwith book 07) |
   |---|---|
   | "Will it actually work for us?" (outcome) | conditional guarantee on a measurable leading indicator, or paid pilot with exit criteria |
   | "We tried this before, it broke" | pilot on one workflow, written exit criteria, no long contract |
   | "Too much of our time" (effort) | done-for-you setup with a stated buyer-hour cap |
   | "What if you disappear / lock-in" | they own all workflows and accounts; exit clause with handover |
   | Budget / cash risk | milestone billing tied to visible deliverables |

   Never guarantee an outcome `evidence.md` cannot support. Underpromise: state the conservative figure (JOLT).

7. **Name with MAGIC** (`offer-creation` book 01): Magnetic reason, Announce the avatar, Give a goal, Indicate a time interval, Complete with a container word. Draft 3, then recommend one (≤ 9 words). Use the segment's words from `voc-swipe.md`.

8. **One-sentence offer** (Joyner, `offer-creation` book 05): "For <avatar> who <pain verbatim>, <name> delivers <outcome> in <time>, or <risk reversal>."

## Output
Write to `assets/offers/<YYYY-MM-DD>-<segment-slug>.md`:

```markdown
# One-Offer Sheet · <Offer name> · <segment> · DRAFT
Confidence: <high|medium|low> (<n> deals, <n> verbatims, <n> WTP data points)

## One sentence
<For … who …, … delivers … in …, or …>

## Positioning (Dunford)
- Alternatives we replace: <alt — its real strength> ×3+
- Unique attributes (proof): <attribute — evidence.md line | [NEEDS PROOF]>
- Value themes: <theme — verbatim gain [source]>
- Best-fit buyer: <traits>
- Market frame: <style> · "<category phrase>"

## Customer profile → value map (top 3 pains)
| # | Pain (verbatim [source]) | Severity | Pain reliever |

## Value Equation
| Lever | Score 1–5 | Why | How to raise |
Total: <n>/20

## Package
- Outcome: <buyer's words + number>
- In scope (leaders): … · Fillers: … · Removed (killers): …
- Delivery: <phases, buyer hours cap, first visible result by week N>

## Price
- Median annual impact <x> · minimum <y> (from <n> deals)
- Price: <p> (<Provisional|Validated>) · ROI at median = <x>/<p> = <r>× · at minimum = <y>/<p> = <r>×
- Floor (pricing.md): <f> · Trades instead of discount: <from pricing.md>
- WTP questions for next 5 calls: 1… 2… 3… 4…

## Guarantee
<terms> · chosen because <n> of <m> logged objections named <risk>

## Name options
1. <recommended> · 2. … · 3. …
```

Then show a unified diff for `context/offers.md` (new or replaced offer block) and ask: "Write this to offers.md?" Write only on yes.

## Write-back
- `context/offers.md`: only after explicit yes.
- Each deal file used: nothing, unless WTP questions were generated; then append under Timeline `### <date> · WTP questions queued · pitch offer` with the 4 questions.
- `log.md`: `<date> · pitch · offer · <segment> one-offer sheet (<confidence>) · assets/offers/<file>`.

## Quality gate
- [ ] One segment, one outcome, one price, one guarantee.
- [ ] Every pain and gain carries a verbatim with source; none invented.
- [ ] Every unique attribute and every proof line traces to `evidence.md` or shows `[NEEDS PROOF]`.
- [ ] All four levers ≥ 3, or the sheet says which lever blocks pricing.
- [ ] ROI math shown with inputs; price ≥ floor.
- [ ] Guarantee maps to a counted, named risk.
- [ ] Diff shown; `offers.md` untouched without a yes.

## Failure modes
- **Inventing pains** to fill the canvas: leave the cell empty and add a discovery question instead.
- **Pricing from cost or competitors** rather than impact: rerun step 5.
- **Kitchen-sink scope** to look valuable: every item must raise a lever (Hormozi), else cut.
- **Outcome guarantee with no proof**: switch to pilot or milestone billing.
- **Clever names** the buyer would not say: names use swipe-file words.
