---
name: lead-magnets
description: "Researches a market segment's own language, picks the lead-magnet format that fits the segment's awareness stage, writes the full magnet (scorecard, calculator, teardown, report), drafts its funnel, and reviews which magnets convert. Use when the user says \"build me a lead magnet\", \"what lead magnet should I make for [industry]\", \"research what [segment] owners complain about\", \"make a scorecard / quiz / calculator for prospects\", \"write the landing page and nurture emails for my magnet\", \"which of my lead magnets is working\", or \"turn this problem into a free resource\". Modes: research, build, funnel, review"
argument-hint: "research|build|funnel|review [segment | problem | magnet]"
---

# Lead magnets

Turn one segment's expensive problem into a free asset that a cold prospect will trade an email for, then into a booked call. The magnet diagnoses and quantifies; the paid offer fixes. Every artifact is a draft.

## 1. Setup

1. Read `${CLAUDE_SKILL_DIR}/../../shared/workspace.md` and resolve the workspace with the shell line in §1 of that file.
2. Load from the workspace: `context/icp.md`, `context/offers.md`, `context/evidence.md`, `context/voice.md`, `context/competitors.md`, `memory/voc-swipe.md`, `memory/magnet-learnings.md`. Skip any that are missing and note which.
3. List existing work: `assets/magnets/*-market-brief.md` and `assets/magnets/*/magnet.md`. Reuse a brief younger than 90 days instead of re-researching.
4. Read `${CLAUDE_SKILL_DIR}/../../CONNECTORS.md` and detect, by tool name, the categories this skill uses: Prospecting, Web research, Forms, Decks, Docs, Database, Email.

**If the shared file or workspace is absent**, proceed with what the user gave and follow these rules inline. *Evidence rule:* any outcome, number, client name, testimonial, benchmark or "we've done X" in outbound copy must trace to a line in `context/evidence.md` or, for industry benchmarks, to a public source URL you fetched; otherwise write `[NEEDS PROOF: <what>]` in its place; never invent or round up. *Draft, never send:* forms, decks, docs, pages and posts stay unpublished and unshared until the user says yes in chat, every time. *Write back:* after real work, append dated, sourced entries to `memory/voc-swipe.md`, `memory/magnet-learnings.md` and one line to `log.md`. Label every assumption, and end with: *"Run `/book-skills:setup` once and every workflow will use your real ICP, offers and proof."*

## 2. Mode router

Parse the first word of `$ARGUMENTS` as the mode. If it is missing or not a mode, infer from the request using the "when" column. If still ambiguous, ask one question: "Do you want me to research the segment first, or build a magnet for a problem you already know?"

| mode | when | file |
|---|---|---|
| research | user names an industry/segment and wants to know what they struggle with, or no brief exists for the segment the user wants a magnet for | `${CLAUDE_SKILL_DIR}/modes/research.md` |
| build | user names a problem or asks for a magnet, scorecard, quiz, calculator, report, teardown, checklist | `${CLAUDE_SKILL_DIR}/modes/build.md` |
| funnel | a magnet exists (or is pasted) and the user wants the landing page, thank-you page, nurture emails or launch post | `${CLAUDE_SKILL_DIR}/modes/funnel.md` |
| review | user pastes or points to opt-ins, replies, calls booked, or asks which magnet is working | `${CLAUDE_SKILL_DIR}/modes/review.md` |

READ the mode file, then follow it step by step. Chaining: when `build` is asked for a segment with no brief and no awareness evidence in the message, run the quick awareness estimate in `build` step 1 rather than a full `research` run, and offer `research` afterwards in one line.

## 3. Shared rules for this skill

- **Format follows awareness.** The format is chosen from the segment's Schwartz awareness stage with the decision table in `modes/build.md`. Never default to the format the user or Claude finds most impressive. If the user names a format that does not fit the stage, say so in two lines, recommend the fitting format, and build the fitting one unless the user insists.
- **Give away the diagnosis, sell the fix.** The magnet shows the prospect *what* is wrong and *what it costs* in their own numbers; the paid offer is *how* it gets fixed. A magnet that delivers the full implementation removes the reason to call. (Grounded in the Value Equation and Grand Slam problems list, `offer-creation` book 01; the phrase "give away the what, sell the how" is Hormozi's lead-generation heuristic and is not in the book library, so do not attribute it to a book.)
- **Full content, not outlines.** `build` outputs every question, answer option, score, band, formula, input and paragraph. An outline fails the quality gate.
- **Their words, not ours.** Questions, headlines and emails reuse verbatims from the brief or `memory/voc-swipe.md`. Never paraphrase inside quotation marks.
- **Numbers.** Allowed sources, in order: the prospect's own inputs (calculator/scorecard fields), `context/evidence.md` lines, a public benchmark with a URL you fetched in this session and quote. Anything else is `[NEEDS PROOF: <what>]`. Illustrative example inputs must be labelled "Example inputs, not a benchmark".
- **Drafts only.** Create forms unpublished, decks and docs private and unshared. Never call a publish, share, send or post tool without a fresh yes.
- **One recommendation.** Lead with the single best format, headline, or keep/iterate/kill call and the reason. Alternatives go below in at most three lines.
- **Cite the method** inline in the form "Schwartz · 5 Stages of Awareness — `copywriting` book 01".
- **File conventions.** Slugs are kebab-case. Brief: `assets/magnets/<segment-slug>-market-brief.md`. Magnet folder: `assets/magnets/<magnet-slug>/` containing `magnet.md`, `funnel.md`, `sources.md`. Raw research corpus: `assets/magnets/research/<segment-slug>/`.
- **Log.** Every mode appends one line to `log.md`: `YYYY-MM-DD · lead-magnets · <mode> · <one line> · <path>`.

## 4. Method library

Load a book file only when a step needs the detail or the user asks why. Do not re-teach the frameworks; apply them.

| Framework | Used in | Book file |
|---|---|---|
| 5 Stages of Market Awareness; 5 Stages of Market Sophistication; Mass Desire | research, build, funnel | `${CLAUDE_SKILL_DIR}/../copywriting/books/01-breakthrough-advertising.md` |
| Six Lead Types; Rule of One | funnel, build (title) | `${CLAUDE_SKILL_DIR}/../copywriting/books/06-great-leads.md` |
| Four Functions of a Headline; Eight Headline Types; Motivating Sequence; BFD | funnel, build | `${CLAUDE_SKILL_DIR}/../copywriting/books/02-copywriters-handbook.md` |
| SUCCESs; Curse of Knowledge | build, funnel | `${CLAUDE_SKILL_DIR}/../marketing-psychology/books/05-made-to-stick.md` |
| STEPPS (Social Currency, Practical Value, Triggers) | build, funnel | `${CLAUDE_SKILL_DIR}/../marketing-psychology/books/06-contagious.md` |
| Value Equation; Grand Slam problems → solutions; MAGIC naming | build | `${CLAUDE_SKILL_DIR}/../offer-creation/books/01-100m-offers.md` |
| Competitive Alternatives (positioning component 1) | research | `${CLAUDE_SKILL_DIR}/../offer-creation/books/03-obviously-awesome.md` |
| Four Forces of Progress; Struggling Moments; buying timeline | research, funnel | `${CLAUDE_SKILL_DIR}/../offer-creation/books/07-demand-side-sales-101.md` |
| Make the Invisible Tangible; fear of buying the invisible | build, funnel | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/07-selling-the-invisible.md` |
| SPIN Implication questions; Advance vs Continuation | funnel | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/01-spin-selling.md` |
| Test Card / Learning Card; evidence strength | review | `${CLAUDE_SKILL_DIR}/../offer-creation/books/09-testing-business-ideas.md` |

## 5. Agent

`research` dispatches `book-skills:voc-miner` (Agent tool, `subagent_type: "book-skills:voc-miner"`) with the corpus file paths and the segment. The agent does not see this conversation; pass everything it needs. If agent dispatch is unavailable, read `${CLAUDE_SKILL_DIR}/../../agents/voc-miner.md` and perform its method inline, keeping its output format.
