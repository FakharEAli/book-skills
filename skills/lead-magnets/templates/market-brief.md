# Template: market brief

Fill every field. Quotes are verbatim from corpus files, never paraphrased. Summaries sit outside quotation marks. Write `none found` rather than leaving a section empty.

```markdown
---
segment: <one line: role, business type, size, geography>
segment_slug: <kebab-case>
created: YYYY-MM-DD
confidence: solid | thin (<what is missing>)
companies: <n>          # 20–50
items: <n>              # reviews + posts + job ads + site pages used
source_types: [review-of-company, review-of-competitor, job-post, forum, site]
awareness: unaware | problem-aware | solution-aware | product-aware | most-aware
awareness_shares: "unaware <x>% · problem <y>% · solution <z>% · product <w>%"
sophistication: 1 | 2 | 3 | 4 | 5
corpus: assets/magnets/research/<segment-slug>/
---

# <Segment> market brief

## Top 5 expensive problems
Ranked by Frequency (distinct sources, 1–5) × Cost signal (0–5). Problems with C ≤ 1 excluded.

| # | Problem (their words) | F (sources) | C (level reached) | F×C | Strongest verbatim — source, date |
|---|---|---|---|---|---|
| 1 | | <1–5> (<n>) | <0–5> (<level name>) | | "…" — <URL>, YYYY-MM-DD |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

## Verbatims per problem
### 1. <problem>
- Cost evidence: <the highest-C verbatim and why it reaches that level>
- "…" — <source type>, <URL>, <date>
- "…" — …
(5–10 per problem; mix source types)

## Triggers (why now)
| Trigger event | Force it amplifies (Four Forces) | Recurring cue (STEPPS Triggers) | Verbatim — source |
|---|---|---|---|
| <e.g. front-desk staff member quits> | Push | <e.g. Monday rota gaps> | "…" — <URL>, <date> |

## Awareness stage
- Call: <stage> (Schwartz · 5 Stages of Awareness — `copywriting` book 01)
- Shares over <n> owner-voiced verbatims: unaware x% · problem y% · solution z% · product w%
- Tie rule applied: yes/no (<reason>)
- Deciding verbatims: "…" — <source>; "…" — <source>
- Implication for format: <format from the build decision table>

## Sophistication stage
- Call: <1–5> (Schwartz · 5 Stages of Sophistication — `copywriting` book 01)
- Evidence: competitor claims seen: "…" (<competitor type>, <URL>); review disbelief: "…" — <URL>
- Implication: <state claim simply | enlarge | introduce named mechanism | elaborate mechanism | lead with identification>

## Competitive alternatives (Dunford · Competitive Alternatives — `offer-creation` book 03)
| Alternative | Distinct sources | What they like | What they hate (verbatim — source) |
|---|---|---|---|
| Do nothing / tolerate it | | | |
| Hire (receptionist, coordinator) | | | |
| Generic tool | | | |
| Answering service / VA | | | |

## Words they use for the problem
<their terms ranked by distinct sources; also list terms they never use (e.g. "workflow", "automation") so copy avoids them>

## Recommended first magnet
Problem #<n> · format: <format> · why: <two sentences tied to F×C and awareness>

## Gaps and next research
- <missing source type or thin problem, and where to get it>
- Statistics the magnet will want that need a public source: [NEEDS PROOF: …]
```
