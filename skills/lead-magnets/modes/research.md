# Mode: research `<industry or segment>`

## Purpose
Build a market-language brief for ONE segment: the five most expensive problems in the segment's own words, what triggers them to act, how aware and how sophisticated the market is, and what they use instead today. The brief is the input to `build` and `funnel`; its verbatims seed `memory/voc-swipe.md`.

## Inputs
- **Segment definition.** From `context/icp.md` if the segment is there (firmographics, buyer role, disqualifiers). Otherwise derive one line from the request ("owner-operated HVAC firms, 5–30 staff, UK") and label it an assumption. If the request names a whole industry ("healthcare"), narrow to one segment before starting and say which; a brief covering several segments averages away the language.
- **Company sample (20–50).** Prospecting connector first (tools named `clay`, `apollo`, `common-room`, `search-companies`, `prospect`): search by industry, headcount and geography from the ICP. Fallback: web research (directories, association member lists, map listings via search, "best <segment> in <city>" lists), or a CSV the user provides. Record name, URL, size signal, location in `assets/magnets/research/<segment-slug>/companies.md`. Company names stay in the workspace; never put them in outbound copy.
- **Competitor list.** `context/competitors.md` plus the vendors/tools the segment's reviews mention. Include non-software alternatives (agency, VA, answering service, hire, spreadsheet, do nothing).
- **Web research tools.** `web-research` skill, `exa`, `scrapling`, `WebFetch`, `WebSearch`. If none work, ask the user to paste review pages, threads or call notes, and say the brief is built from pasted material only.

## Procedure

1. **Plan the corpus.** Target source types and minimums:

   | Source type | Where | Minimum |
   |---|---|---|
   | Own sites | homepage, services, about, FAQ of the 20–50 companies | 20 sites |
   | Reviews OF the companies | Google reviews, Trustpilot, Yelp, industry directories | 40 reviews |
   | Reviews OF competitors/tools they use | G2, Capterra, Trustpilot, app stores | 40 reviews; prioritise 1–3 star and "cons" fields |
   | Job posts | Indeed, LinkedIn Jobs, careers pages for admin, ops, front-desk, coordinator, dispatcher roles | 10 posts |
   | Owner talk | Reddit (`site:reddit.com <segment> owner <pain word>`), industry forums, public Facebook group posts, trade-press comments | 15 threads |

   Reviews of the companies show what *their* customers punish them for (the downstream cost). Competitor-tool reviews show what owners hate about current alternatives. Job posts show what owners pay a salary to fix. Owner threads show struggling moments in first person (Struggling Moments, `offer-creation` book 07).

2. **Collect and save raw text.** One file per item or per batch in `assets/magnets/research/<segment-slug>/<type>-NN.md`, each starting with:
   ```
   source_type: review-of-company | review-of-competitor | job-post | forum | site
   url: <exact URL>
   date: <date on the item, YYYY-MM-DD, or "undated">
   retrieved: <today, YYYY-MM-DD>
   ---
   <verbatim text, no edits>
   ```
   Keep only text that mentions a problem, outcome, workaround, trigger, objection or alternative. Strip reviewer surnames and handles; keep role words ("practice manager", "owner"). Stop collecting a type once three consecutive items add no new problem.

3. **Check the threshold.** If fewer than 3 source types or fewer than 100 items total, continue but set `confidence: thin` and name what is missing. Never fill gaps with what "owners in this industry usually say".

4. **Dispatch the VOC miner.** Agent tool, `subagent_type: "book-skills:voc-miner"`, prompt containing: the segment line; the absolute path of every corpus file (Glob them first); the instruction "Return your full output format, including frequency counts by distinct source and the 10 strongest phrases." If agent dispatch is unavailable, read `${CLAUDE_SKILL_DIR}/../../agents/voc-miner.md` and run its method inline on the same files.

5. **Rank the problems: Frequency × Cost signal.** Group the miner's pain verbatims into problems (one problem = one root cause, named in the segment's words). Score each:
   - **Frequency (F, 1–5)** by count of *distinct sources*, not mentions: 1 = 1–2, 2 = 3–5, 3 = 6–10, 4 = 11–20, 5 = 21+.
   - **Cost signal (C, 0–5)**, the highest level any verbatim reaches: 0 no cost stated; 1 annoyance only; 2 time lost stated ("I spend my evenings on it"); 3 money, customer or staff lost stated without a number ("we lost the job"); 4 the speaker quantifies it ("three jobs a week"); 5 quantified and recurring, or a job post exists to fix it.
   - **Priority = F × C** (max 25). Ties break on trigger presence, then on fit with `context/offers.md`. Keep the top 5. A problem with C ≤ 1 never makes the top 5, however frequent: annoyances do not buy.

6. **Extract triggers ("why now").** From job posts (a new hire is a trigger), reviews and threads: events that precede action, such as a staff member leaving, opening a location, a bad review, a season, a regulation, a price rise in a current tool. Map each to a Four Forces push (`offer-creation` book 07) and to the recurring cue that keeps it top of mind (STEPPS · Triggers, `marketing-psychology` book 06). Each trigger needs at least one verbatim.

7. **Estimate the awareness stage** (Schwartz · 5 Stages of Market Awareness, `copywriting` book 01). Classify every owner-voiced pain verbatim:
   - *Unaware signal:* describes a symptom or bad outcome without naming the problem or a fixable cause ("slow month", "customers are flaky these days").
   - *Problem-aware:* names the problem, no solution ("we miss too many calls", "nothing works for this").
   - *Solution-aware:* names a solution category, not vendors ("thinking about an answering service").
   - *Product-aware:* names or compares vendors (competitor reviews are mostly this).
   - *Most-aware:* asks for your price or terms; appears only in your own inbound, not in market research.

   Compute the share per bucket over owner-voiced verbatims only (exclude end-customer reviews; they describe consequences, not the owner's awareness). The segment stage is the modal bucket. If the top two buckets are within 10 percentage points, choose the LESS aware one: cold traffic forgives an indirect lead more than a direct claim it does not believe (Great Leads, `copywriting` book 06). Report the shares.

8. **Estimate sophistication** (Schwartz · 5 Stages of Market Sophistication, `copywriting` book 01) from competitor sites, ads and reviews: 1 = few or no competitors making the claim; 2 = several make the same direct claim; 3 = claims enlarged to exhaustion ("24/7", "never miss a lead" everywhere); 4 = competitors sell named mechanisms ("AI receptionist", "smart routing"); 5 = reviews voice disbelief ("they all promise this"). Quote the evidence for the chosen stage.

9. **List competitive alternatives** (Dunford · Competitive Alternatives, `offer-creation` book 03): what the segment does today instead, including do nothing, hire, VA, spreadsheet, generic tool, other agency. For each: verbatim evidence, count of distinct sources, the main complaint about it. "Do nothing" counts when owners describe tolerating the problem.

10. **Write the brief** from the template, then write back.

## Output
Write `assets/magnets/<segment-slug>-market-brief.md` from the full template in `${CLAUDE_SKILL_DIR}/templates/market-brief.md`. Then show the user:

```markdown
**Recommendation:** build a magnet for "<problem #1>" first — <F×C and trigger reason, one sentence>.
Segment: … · confidence: solid | thin (<gap>)
| # | Problem (their words) | F | C | F×C | Strongest verbatim — source |
Awareness: <stage> (<bucket shares>) → format: <from build table>
Sophistication: <1–5> (<evidence quote>)
Brief: assets/magnets/<segment-slug>-market-brief.md · VOC added: <n> new lines
```

## Write-back
- `memory/voc-swipe.md`: for each verbatim the miner returned, Grep the file for the quote first; append only new ones under the matching category heading (canonical format, `shared/workspace.md` §6):
  ```
  ## Pains            → - "<verbatim>" — <source URL>, <item date>, <segment> · problem: <problem-slug>
  ## Triggers         → - "<verbatim>" — <source URL>, <item date>, <segment>
  ```
  Category map: pain/emotion → Pains · outcome → Desired outcomes · trigger → Triggers · objection → Anxieties · alternative → Alternatives · their-words → Their words for the problem.
- `log.md`: `YYYY-MM-DD · lead-magnets · research · <segment>: top problem "<problem>", awareness <stage> · assets/magnets/<segment-slug>-market-brief.md`

## Quality gate
- [ ] 20–50 companies listed, or `confidence: thin` set with the reason.
- [ ] ≥3 source types; every verbatim has a URL and a date (or "undated").
- [ ] Every quote is character-for-character from a corpus file (spot-check 5 with Grep).
- [ ] F counts distinct sources; C uses the 0–5 rubric; no C ≤ 1 problem in the top 5.
- [ ] Awareness call shows bucket shares and applies the 10-point tie rule.
- [ ] Sophistication call quotes its evidence.
- [ ] Alternatives include "do nothing" when evidenced.
- [ ] Evidence rule: no market statistic without a fetched public URL; anything else is `[NEEDS PROOF: <what>]`.
- [ ] No personal names of reviewers or forum users.

## Failure modes
- **Researching an industry, not a segment.** Language from dentists and vets averages into mush. Narrow first.
- **Counting mentions, not sources.** One angry thread with 40 replies inflates F. Count distinct sources.
- **Reading end-customer reviews as owner awareness.** They show consequences (useful for C), not owner beliefs.
- **Paraphrasing.** "Owners feel overwhelmed by admin" is a summary; keep summaries outside quotes.
- **Defaulting to problem-aware.** Use the bucket shares.
- **Scraping behind logins.** Public pages or pasted text only; ask before using the user's logged-in accounts.
