---
name: pitch
description: "Builds and defends the commercial pitch from the user's real deal data: a One-Offer Sheet for a segment, a single-recommendation proposal with ROI math in the buyer's numbers, a live prospect roleplay with scoring, word-for-word negotiation responses, and a scored critique of an existing proposal or deck. Use when the user says \"build my offer for dental clinics\", \"write a proposal for Acme\", \"they said we're too expensive\", \"another agency quoted half\", \"let me practise the call with this prospect\", \"roleplay the owner\", \"review this proposal before I send it\", \"how should I price this\". Modes: offer, proposal, rehearse, negotiate, review."
argument-hint: "<offer|proposal|rehearse|negotiate|review> [segment | company | persona | pasted text]"
---

# Pitch

Turn what the workspace knows about buyers (gaps, verbatims, objections, pricing floors) into an offer, a proposal, a rehearsal or a negotiation answer. Every artifact is a DRAFT grounded in the user's own data, never in generic sales copy.

## 1. Setup

1. Read `${CLAUDE_SKILL_DIR}/../../shared/workspace.md` and resolve the workspace with its shell one-liner (`./.book-skills/` → `$BOOK_SKILLS_HOME` → `~/.book-skills/`).
2. Load, for every mode: `context/offers.md`, `context/pricing.md`, `context/evidence.md`, `context/voice.md`, `memory/objections.md`. Each mode file lists the extra files it needs (`context/icp.md`, `context/competitors.md`, `memory/voc-swipe.md`, `memory/win-loss.md`, `deals/<slug>.md`).
3. Resolve a company argument to `deals/<slug>.md` (slug = kebab-case of the company name; if no exact file, `ls deals/` and match by `company:` frontmatter; if two match, ask which).
4. Note which files are missing. A missing file is never a blocker when the request is answerable: work from what the user pasted, label each assumption `[ASSUMPTION: …]`, and say which file would remove it.

**Fallback if the shared file cannot be read:** the workspace is a private folder at one of the three paths above. Rule 2 (evidence): any outcome, number, client name, testimonial or "we've done X" in outbound text must trace to a line in `context/evidence.md`; otherwise write `[NEEDS PROOF: <what>]`, never invent or round up. Rule 3 (draft, never send): produce drafts only; sending, sharing, posting or booking needs the user's explicit yes in chat each time. Rule 4 (write back): after real work, append dated (`YYYY-MM-DD`), sourced entries to `memory/objections.md`, `memory/voc-swipe.md`, `deals/<slug>.md` and one line to `log.md`. If no workspace exists, finish with: *"Run `/book-skills:setup` once and every workflow will use your real ICP, offers and proof."*

## 2. Mode router

Parse the first word of `$ARGUMENTS` as the mode. If it is missing or not a mode name, infer from the request using the "when" column. If two modes still fit, ask one question ("Do you want me to write the proposal, or review the one you have?"). Then READ the mode file and follow it step by step.

| mode | when | file |
|---|---|---|
| `offer` | building or rebuilding the core package for one segment; "how should I price/name/guarantee this" | `${CLAUDE_SKILL_DIR}/modes/offer.md` |
| `proposal` | a specific deal needs a written proposal or deck | `${CLAUDE_SKILL_DIR}/modes/proposal.md` |
| `rehearse` | practising a call with a specific prospect or a persona | `${CLAUDE_SKILL_DIR}/modes/rehearse.md` |
| `negotiate` | the user pastes or describes pushback on price, scope, timing, authority, a competitor or risk | `${CLAUDE_SKILL_DIR}/modes/negotiate.md` |
| `review` | the user shares an existing proposal, deck, offer page or pitch and wants it critiqued | `${CLAUDE_SKILL_DIR}/modes/review.md` |

Routing tie-breaks: pasted buyer words that push back → `negotiate`, even if the user also says "proposal". A pasted draft the user wrote → `review`. "Practise", "roleplay", "mock call" → `rehearse`.

## 3. Shared rules for this skill

- **One recommendation** (JOLT, "Offer a recommendation"). Proposals and offers lead with a single option. If the user insists on choices, give at most two and mark one `Recommended` with a one-sentence reason. Never produce three tiers; explain why once, briefly (option overload creates a valuation stall).
- **The buyer's numbers, not yours.** Impact, ROI and pricing arguments use figures from the deal file or the user's message. If a figure is the user's estimate rather than the buyer's statement, label it `(your estimate)`. Show every calculation as a formula with the inputs, e.g. `ROI = £38,400 ÷ £6,000 = 6.4×`.
- **Verbatims are exact.** Quote buyer words only from deal files, debriefs, `voc-swipe.md` or the user's paste, with the source in brackets. Never paraphrase inside quotation marks.
- **Evidence rule on every outbound sentence.** Results, client names, timelines you have hit before, and "we've done this for X" need a line in `context/evidence.md`; otherwise `[NEEDS PROOF: …]`.
- **Draft, never send.** Docs and decks are created as private drafts. Never share, publish or email them. Say where the draft lives and that it has not been shared.
- **No discount without a trade.** Price moves only in exchange for a scope or terms change, and never below the floor in `context/pricing.md`.
- **Cite the method** inline in internal notes (not in buyer-facing text): framework name, author, `skill` book number.
- **Output conventions.** Filenames: `assets/<kind>/<YYYY-MM-DD>-<slug>.md`. Buyer-facing text follows `context/voice.md` (banned words removed, their preferred terms used). No em-dash chains, no hype adjectives ("revolutionary", "seamless", "game-changing").
- **Write back after every mode.** Each mode file gives the exact append format. Always add one line to `log.md`: `YYYY-MM-DD · pitch · <mode> · <one line> · <artifact path or deal slug>`. Roleplay output is practice, not buyer evidence: it may go to `objections.md` tagged `source: roleplay`, never to `voc-swipe.md`.
- **Agents.** Dispatch with the Agent tool, `subagent_type: "book-skills:<name>"`, passing every input inline (file contents or paths, pasted text). Agents do not see this conversation. If dispatch is unavailable, read the agent file at `${CLAUDE_SKILL_DIR}/../../agents/<name>.md` and do its steps inline, saying so.

## 4. Method library

Load a book file only when a step needs the detail or the user asks why. Do not re-teach the framework to the user; apply it.

| Framework | Used in | Book file |
|---|---|---|
| Positioning components, 10-step process, market frame styles (Dunford) | offer | `${CLAUDE_SKILL_DIR}/../offer-creation/books/03-obviously-awesome.md` |
| Positioning statement as stage artifact | offer | `${CLAUDE_SKILL_DIR}/../client-eagerness-playbook/books/01-obviously-awesome.md` |
| Value Proposition Canvas (Osterwalder et al.) | offer | `${CLAUDE_SKILL_DIR}/../offer-creation/books/02-value-proposition-design.md` |
| Grand Slam Offer, Value Equation, guarantees, MAGIC naming (Hormozi) | offer, review | `${CLAUDE_SKILL_DIR}/../offer-creation/books/01-100m-offers.md` |
| WTP conversations, leaders/fillers/killers, price integrity (Ramanujam, Tacke) | offer, negotiate | `${CLAUDE_SKILL_DIR}/../offer-creation/books/04-monetizing-innovation.md` |
| Irresistible offer, "one-sentence offer" (Joyner) | offer | `${CLAUDE_SKILL_DIR}/../offer-creation/books/05-the-irresistible-offer.md` |
| Value-based fees, no free pitching (Enns) | negotiate | `${CLAUDE_SKILL_DIR}/../offer-creation/books/06-win-without-pitching.md` |
| Current state → future state → gap, root cause (Keenan) | proposal, review, rehearse | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/04-gap-selling.md` |
| JOLT: recommend, limit exploration, take risk off the table (Dixon, McKenna) | all modes | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/02-the-jolt-effect.md` |
| Make the invisible tangible (Beckwith) | proposal, offer | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/07-selling-the-invisible.md` |
| SPIN, implication questions, Advance vs continuation (Rackham) | rehearse, review | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/01-spin-selling.md` |
| Labels, mirrors, calibrated questions, accusation audit, Ackerman (Voss) | negotiate, rehearse | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/05-never-split-the-difference.md` |
| Trust Equation, self-orientation (Maister, Green, Galford) | negotiate, review | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/03-the-trusted-advisor.md` |
| Collaborative scoping, "let's get real" money talk (Khalsa, Illig) | negotiate | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/10-lets-get-real-or-lets-not-play.md` |
| Evidence audit by proof type (Cialdini) | proposal, review | `${CLAUDE_SKILL_DIR}/../client-eagerness-playbook/books/06-influence.md` |
| Voice-of-customer wording (Wiebe) | offer, proposal | `${CLAUDE_SKILL_DIR}/../copywriting/books/08-where-stellar-messages-come-from.md` |
| Full stage sequence and proposal-review playbook | offer, review | `${CLAUDE_SKILL_DIR}/../client-eagerness-playbook/playbooks.md` |
