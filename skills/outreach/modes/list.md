# Mode: list `<segment> [n]`

## Purpose
Build a scored, disqualified, sourced prospect list for one ICP segment, so that `write` starts from rows that have a real reason to hear from the user this month. Default `n` = 25 qualified rows (cap 100 per run).

## Inputs
- `context/icp.md`: the named segment's firmographics (industry, size band, geography, business model), buyer roles, trigger list, disqualifiers. If the segment is not in `icp.md`, list the segments that are and ask which one; if `icp.md` is absent, ask the user for industry, size band, geography and buyer role in one message, then mark the list `[ASSUMED ICP]`.
- `context/evidence.md`: needed for the evidence-match score.
- `context/competitors.md`: names of tools or providers whose churn signals count as triggers.
- Existing `prospects/*.md` and `deals/*.md`: to de-duplicate (never re-list a domain that already has a deal file or appeared in a list in the last 90 days, unless the user asks).
- **Prospecting / enrichment** connector (Clay, Apollo, Common Room or any tool matching `search-companies`, `search-contacts`, `prospect`). Fallback: the `web-research` skill or web search, plus any CSV the user provides. Say which you used.
- **Web research** connector for trigger verification (job boards, review sites, news, company site).

## Procedure
1. **Translate the segment into a search.** From `icp.md`, write the filter set: industry codes or keywords, employee or location count band, geography, buyer titles (primary and fallback). Show it in one line before searching.
2. **Pull 2–3x `n` candidates** through the prospecting connector (or web search: directory pages, "hiring <manual role> <city>", review-platform category pages). Record only: company, domain, contact name, role, business email or LinkedIn URL. Nothing else about the person.
3. **Disqualify first.** Apply every disqualifier in `icp.md` (e.g. below size floor, franchise with central IT, regulated data the user cannot handle, existing client, competitor). Plus universal disqualifiers: no website, out of business, any email/domain/LinkedIn URL in `memory/suppression.md` (check it first, every run), domain already in an open deal. Mark `DQ: <reason>` and move the row to the "Disqualified" section; do not score it.
4. **Find the why-now trigger.** For each surviving row, look for the trigger types below in this order, stop at the first strong one, and keep the source URL. This is Challenger "why now": a change in their world that makes the status quo more expensive this month (`sales-psychology` book 06; also Hoffeld's "Why now?", book 09).
   - Job post for a role the user's offer automates (receptionist, scheduler, admin, data entry, SDR, customer service).
   - New hire in the role that would own the automation (ops manager, practice manager, head of CS) in the last 90 days.
   - Funding, acquisition, new location, new service line, expansion announcement.
   - Public reviews mentioning slowness, no reply, missed calls, booking friction (≥ 2 such reviews in the last 6 months).
   - Tech change: new CRM, booking, phone or helpdesk system visible on the site or in a post.
   - Competitor churn: public complaint about, or migration away from, a tool or provider in `competitors.md`.
5. **Score each row 0–100** with the rubric below. Show the four sub-scores, not only the total.
6. **Write the why-now line**: one sentence, factual, ≤ 20 words, naming the trigger and its date, e.g. "Posted a second front-desk job ad on 2026-09-28; reviews since August mention unanswered calls." No inference stated as fact; inferences start with "Likely".
7. **Tier and sort.** A ≥ 75, B 55–74, C 40–54, drop < 40 (keep dropped rows in a collapsed section so the user can see why). Sort by score, then trigger recency.
8. **Stop at `n` A+B rows** or when candidates run out; report the shortfall honestly rather than padding with C rows.

### Scoring rubric

| Dimension | Points | Rule |
|---|---|---|
| **ICP fit** | 0–30 | Industry matches segment: 10 (adjacent: 5). Size inside band: 10 (within 25% of edge: 5). Contact is a listed buyer role: 10 (fallback role: 5; no named person: 0). |
| **Trigger strength** | 0–35 | Job post for an automatable manual role, live: 35. New hire in owning role < 90 days: 30. Funding / expansion / new location < 90 days: 28. ≥ 2 reviews citing slowness or no reply in 6 months: 25. Tech change or competitor churn < 90 days: 20. Any of these 91–180 days old: 10. Older, unsourced or guessed: 0. Second independent trigger: +5 (cap 35). |
| **Reachability** | 0–15 | Verified business email of the named buyer: 15. Named buyer with LinkedIn active in last 30 days: 10. Only a generic inbox or contact form: 5. None: 0. |
| **Evidence match** | 0–20 | `evidence.md` has a result in the same sector and a client 0.5x–2x their size: 20. Same sector, other size, or adjacent sector, same size: 12. Capability only (offer exists, no client proof): 5. Nothing relevant: 0. Name the evidence line id. |

A trigger with no source URL scores 0. A row with evidence match ≤ 5 is still listable, but `write` will use `[NEEDS PROOF]` or capability-only framing for it; flag it.

## Output
File `prospects/<YYYY-MM-DD>-<segment-slug>.md`:

```markdown
---
segment: <segment name from icp.md>
date: YYYY-MM-DD
source: <connector or "web search + user CSV">
requested: <n>
qualified: <A+B count>
icp_version: <date or "ASSUMED">
---

# <Segment> prospects · YYYY-MM-DD

Filters: <industry> · <size band> · <geo> · roles: <primary> / <fallback>

| # | Company | Domain | Contact | Role | Channel | Fit /30 | Trigger /35 | Reach /15 | Proof /20 | Score | Tier | Why now | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | email / LinkedIn | | | | (ev-id) | | A | <≤ 20 words, dated> | <URL> |

## Disqualified
| Company | Reason (icp.md disqualifier or universal) |

## Dropped (< 40)
| Company | Score | Main gap |

## Notes
- Shortfall: <n requested vs qualified, and why>
- Proof gaps: <sectors/sizes with no evidence line → candidates for [NEEDS PROOF]>
```

In chat, show the top 10 rows, the counts, and one recommendation ("Write to the 7 A-tier rows first; 3 of them share the front-desk-job-ad trigger, so one angle covers them").

## Write-back
- `log.md`: `YYYY-MM-DD · outreach · list · <segment>: <qualified>/<requested> qualified, top trigger <type> (<file path>)`.
- `memory/outreach-learnings.md`, under a `## Trigger supply` heading (append): `YYYY-MM-DD · <segment> · triggers found: job-post <k>, new-hire <k>, funding <k>, reviews <k>, tech <k>, churn <k> · source <connector>`. `review` uses this to judge which triggers are both common and effective.
- Do not create deal files at this stage; deals start when a prospect engages.

## Quality gate
- [ ] Every scored row has a why-now line and a working source URL; no URL → trigger score 0.
- [ ] Every `icp.md` disqualifier was checked; DQ rows are listed with the reason.
- [ ] Sub-scores shown and they sum to the total.
- [ ] No duplicate domains against existing deals or lists from the last 90 days.
- [ ] Personal data limited to company, domain, name, role, business email or LinkedIn URL.
- [ ] Evidence rule: the "Proof" column cites an `evidence.md` line id or says capability-only / none; no implied client results.
- [ ] Shortfall reported, not padded.

## Failure modes
- **Firmographic-only lists.** A perfect-fit company with no trigger is a C at best; resist promoting it because it "looks right".
- **Stale triggers.** A job post from eight months ago is not why-now. Date every trigger and apply the decay.
- **Inferred triggers stated as fact.** "They're struggling with leads" without a review or post is fabrication. Use "Likely" or score 0.
- **Over-collection.** Enrichment tools return phone numbers and personal profiles; drop them before writing the file.
- **One connector, one bias.** Database tools miss owner-operated businesses; when the segment is small local firms, supplement with review-site and job-board searches.
- **Evidence blindness.** Listing 25 dental clinics when `evidence.md` has no healthcare proof sets up 25 weak emails; surface the proof gap in Notes so the user can fix it or choose another segment.
