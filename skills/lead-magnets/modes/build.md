# Mode: build `<problem> [format]`

## Purpose
Produce one complete, ready-to-use lead magnet for one problem in one segment: the format chosen by awareness stage, every word written, every number sourced or flagged, and a draft built in the best available tool. Never published.

## Inputs
- **Problem and segment.** From the request; match it to a problem in `assets/magnets/<segment-slug>-market-brief.md` if one exists.
- **Awareness and sophistication.** From the brief's frontmatter. If no brief: estimate from what the user said with the step 1 rubric, label it "estimated from your description", and offer `research` in one line at the end.
- **Verbatims.** Brief + `memory/voc-swipe.md` for this segment and problem.
- **Offer.** `context/offers.md`: the paid fix the magnet points to. If absent, write `[NEEDS OFFER: <what the next step sells>]` in the CTA.
- **Proof, voice, history.** `context/evidence.md`, `context/voice.md`, `memory/magnet-learnings.md` (don't rebuild a format killed for this segment without saying what differs).
- **Tools.** Forms, Decks, Docs connectors (step 8 has fallbacks).

## Procedure

1. **Fix the awareness stage** (Schwartz · 5 Stages of Market Awareness, `copywriting` book 01). Use the brief. Without one, classify the user's description: symptom not linked to a fixable cause → Unaware; problem named, no fix → Problem-aware; fix category named → Solution-aware; vendors compared → Product-aware; asking your price → Most-aware. State the stage and the phrase that decided it.

2. **Choose the format with the decision table.** One format; the table decides, not taste.

   | Awareness stage | What the prospect lacks | Format | Why this and not the next one down |
   |---|---|---|---|
   | Unaware | Doesn't see the problem | **Diagnostic scorecard / self-assessment** (10–15 questions, score, bands) | Lets them discover the problem themselves; a cost calculator assumes they already accept there is a cost to calculate |
   | Problem-aware | Doesn't know what it costs or that it is fixable | **Cost calculator** or **"hidden cost" report** | Turns a felt annoyance into their own number; a teardown assumes they are already shopping for fixes |
   | Solution-aware | Doesn't know which approach works or what good looks like | **Teardown, benchmark, or playbook** | Shows the mechanism and the standard; an ROI model assumes they are comparing you to a named alternative |
   | Product-aware / comparing | Doesn't know whether it pays back or how to choose | **ROI model, buyer's checklist, or case-study breakdown** | Supports the comparison they are already making |
   | Most-aware | Needs only the terms | **Audit / offer** (free audit, fixed-scope pilot, priced quote) | They need a reason to act now, not more education |

   **Sophistication modifier** (`copywriting` book 01): at stage 3–4, the magnet must name a mechanism (the scorecard's dimensions or the calculator's formula is the mechanism; give it a name). At stage 5, lead with identification: frame the scorecard as "which kind of <role> are you" rather than a claim.
   **User-named format that mismatches:** say in two lines why it misfits ("An ROI calculator asks owners to value fixing something they don't believe is broken"), build the table's format, and offer theirs for when the segment moves up a stage.

3. **Scope it: diagnosis free, fix paid** (Value Equation and Grand Slam problems → solutions, `offer-creation` book 01). Write three lines: *Reveals* (the problem and its cost, in their numbers). *Leaves for the paid offer* (the implementation). *Quick win* (one thing they can do in under 30 minutes after using it). Constraints: consumable in ≤10 minutes (time delay); no setup, login or reading beyond the result (effort and sacrifice); solves exactly one problem from the brief. Name it with MAGIC (`offer-creation` book 01), 3–7 words, e.g. "The 12-Question Missed-Call Scorecard for Clinic Owners".

4. **Write the full content** from `${CLAUDE_SKILL_DIR}/templates/magnet-formats.md`, section for the chosen format. Minimums: scorecard 10–15 questions, 4 behaviourally specific answer options each scored 0–3, 3–4 dimensions, 3 bands each with diagnosis + 3 recommendations + one CTA; calculator: every input with unit and who in the business knows it, formula written out, output sentence, sensitivity line, worked example labelled "Example inputs, not a benchmark"; report: 1,200–2,500 words, 5–7 sections, each ending in a self-check; teardown: 5–8 numbered findings each with evidence, impact and fix category. Use verbatims as question wording and section titles wherever one fits (Curse of Knowledge, `marketing-psychology` book 05).

5. **Stickiness pass.** Check and fix any fail before moving on.
   - *SUCCESs* (`marketing-psychology` book 05). Simple: one core sentence at the top. Unexpected: one question or result that breaks their assumption. Concrete: no "efficiency" or "optimise"; only things you could film. Credible: a testable credential (their own score or number). Emotional: one owner, one emotion verbatim. Story: one 3–5 sentence struggling-moment scenario, labelled "Illustrative scenario" unless `evidence.md` has a real one.
   - *STEPPS* (`marketing-psychology` book 06). Practical Value: every band or section has a step usable today without buying. Social Currency: a label or score they would repeat ("Level 2: Leaky").
   - *Make the invisible tangible* (Beckwith, `sales-psychology` book 07): a named result screen, numbered steps, a before/after table. The prospect can point at something.

6. **Evidence pass.** List every number, benchmark, client reference and outcome claim, and classify it: (a) prospect input or derived from it → fine; (b) a line in `context/evidence.md` → keep, cite it in `sources.md`; (c) industry benchmark → only if you fetched a public page this session that contains the figure, recorded in `sources.md` with URL, publisher, date and the exact sentence; (d) anything else → `[NEEDS PROOF: <what number, for whom>]` or a calculator input ("your average job value"). Widely repeated statistics with no traceable primary source are (d). Never round; never stretch a benchmark to another segment, country or year.

7. **Write the bridge.** The final screen or page: one sentence naming the gap the result revealed, one sentence on what the paid offer does about it (from `offers.md`), one CTA as a soft Advance (a 15-minute result review, "reply with your score"). One CTA only.

8. **Build the draft in a tool.**
   - Scorecard → Forms connector (`typeform`, `forms`): questions, score-based logic or calculated fields, band endings; unpublished, no publish call. Fallback: markdown spec plus a scoring table any form tool can copy.
   - Calculator → Forms (calculated fields) or Docs; fallback: a spreadsheet spec (cells, formulas).
   - Report, playbook, teardown → Docs (`notion`, Claude Docs, `google-drive`) or Decks (`gamma`, `canva`, `pptx` skill) for a PDF; private, not shared. Fallback: markdown.
   Report the tool, the draft link, and that it is unpublished.

9. **Write files.** `assets/magnets/<magnet-slug>/magnet.md` (full content) and `assets/magnets/<magnet-slug>/sources.md` (every class b and c item).

## Output
Show the user, in this order:

```markdown
**Recommendation:** <Format> — because the segment is <stage> (<deciding phrase or share>). <One line on why not the obvious alternative.>
Method: Schwartz · 5 Stages of Awareness — `copywriting` book 01; format table in lead-magnets/build.

# <MAGIC name>
Core sentence: <what the magnet proves>
Reveals: … · Leaves for the paid offer: … · Quick win: …

<FULL magnet content from the format template>

## Bridge / CTA
## Evidence
- Prospect inputs: <list>
- From evidence.md: <claim → line>
- Public benchmarks: <figure — publisher, URL, date> (or "none used")
- Open: [NEEDS PROOF: …] × <n>
## Draft built
<tool> · <link or file path> · status: unpublished draft
```

## Write-back
- `memory/magnet-learnings.md`, append a registry entry that `review` updates later:
  ```
  ## YYYY-MM-DD · <magnet-slug> · built
  - segment: <segment> · problem: <problem> · awareness: <stage> · sophistication: <n>
  - format: <format> · tool: <tool/link or file>
  - hypothesis: <segment> owners at <stage> will opt in because <reason>; success = opt-in ≥ <x>% and calls/opt-in ≥ <y>% (thresholds from review mode)
  - open proof: <n> [NEEDS PROOF] items
  ```
- `log.md`: `YYYY-MM-DD · lead-magnets · build · <format> for <segment>/<problem> · assets/magnets/<magnet-slug>/magnet.md`

## Quality gate
- [ ] Format matches the decision table; the stage and its evidence are stated.
- [ ] Full content, not an outline (step 4 minimums met; count them).
- [ ] Scope lines written; the magnet does not deliver the implementation.
- [ ] SUCCESs, Practical Value, Social Currency and tangibility checks pass.
- [ ] Evidence rule: every number is a prospect input, an `evidence.md` line, or a fetched public benchmark with URL in `sources.md`; everything else is `[NEEDS PROOF: …]`. No invented clients, results or "studies show".
- [ ] Exactly one CTA.
- [ ] Unpublished draft; nothing shared.

## Failure modes
- **Picking the impressive format.** Nobody calculates the cost of a problem they don't believe they have; an ROI calculator for an unaware segment gets few opt-ins.
- **Giving away the whole fix.** It removes the reason to call.
- **Generic questions.** "Do you use automation?" diagnoses nothing; ask about observable behaviour in their words.
- **Borrowed statistics.** A familiar number with no primary source fails the evidence rule. Turn it into an input.
- **Identical bands.** Each band needs its own diagnosis and free step.
