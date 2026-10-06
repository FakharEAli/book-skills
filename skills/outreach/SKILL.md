---
name: outreach
description: "Builds scored prospect lists with a cited why-now trigger per row, writes evidence-checked cold emails and LinkedIn messages, designs 21-day multichannel sequences, drafts replies that turn objections into a dated next step, and reviews which angles, triggers and proof lines actually get replies. Use when the user says \"build me a prospect list\", \"find leads in <segment>\", \"write a cold email to\", \"draft LinkedIn outreach for\", \"make a follow-up sequence\", \"how do I reply to this\", \"they said they already use X\", \"what's working in my outreach\". Modes: list, write, sequence, reply, review."
argument-hint: "<list|write|sequence|reply|review> [segment n | prospect | pasted reply | period]"
---

# Outreach

Outbound that earns a reply because it is specific, provable and easy to answer. Every message is a draft, every claim traces to the proof ledger, and every run teaches the next one through `memory/outreach-learnings.md`.

## 1. Setup

1. Read `${CLAUDE_SKILL_DIR}/../../shared/workspace.md` and resolve the workspace with the order it gives (`./.book-skills/`, then `$BOOK_SKILLS_HOME`, then `~/.book-skills/`).
2. Load, if present: `context/icp.md`, `context/offers.md`, `context/evidence.md`, `context/voice.md`, `context/competitors.md`. Then load the memory file the mode names (`memory/outreach-learnings.md` for `write`, `sequence`, `review`; `memory/objections.md` for `reply`).
3. Read `${CLAUDE_SKILL_DIR}/../../CONNECTORS.md` and detect tools for the categories the mode needs (Prospecting / enrichment, Web research, Email, Calendar). Say in one line which tool or fallback you used.

**Fallback if the shared file cannot be read or no workspace exists.** Proceed with what the user gave you and label every assumption `[ASSUMED]`. Apply these rules regardless: (a) the evidence rule: any outcome, number, client name, logo, testimonial or "we've done X" must trace to a line in `context/evidence.md`; if it does not, write `[NEEDS PROOF: <what>]` in its place, never invent or round up; with no evidence file, use capability-only framing ("we build X") and no client results; (b) draft, never send: sending, posting, connecting or booking needs the user's explicit yes in chat, every time; (c) write back: append dated (`YYYY-MM-DD`), sourced entries to `memory/` and one line to `log.md` after real work. End with: *"Run `/book-skills:setup` once and every workflow will use your real ICP, offers and proof."*

## 2. Mode router

Parse the first word of `$ARGUMENTS` as the mode. If it is missing or not a mode, infer from the request using the "when" column. If two modes still fit, ask one question ("Do you want the message itself, or the full follow-up cadence?") and stop.

| mode | when | file |
|---|---|---|
| `list` | "find/build prospects", "leads in <segment>", "who should I contact" | `${CLAUDE_SKILL_DIR}/modes/list.md` |
| `write` | "write a cold email / LinkedIn note / DM to <prospect>", "draft outreach for this list" | `${CLAUDE_SKILL_DIR}/modes/write.md` |
| `sequence` | "follow-up sequence", "cadence", "what do I send after", "multichannel plan" | `${CLAUDE_SKILL_DIR}/modes/sequence.md` |
| `reply` | user pastes a prospect's reply; "how do I answer this", "they said…" | `${CLAUDE_SKILL_DIR}/modes/reply.md` |
| `review` | "what's working", "reply rates", "review last month's outreach" | `${CLAUDE_SKILL_DIR}/modes/review.md` |

READ the mode file and follow it step by step. Do not work from this summary alone.

Chaining: `list` ends by offering `write` for A-tier rows; `write` ends by offering `sequence`; any pasted reply switches to `reply`; `review` updates the block that `write` reads first.

## 3. Shared rules

**Quality bar for every outbound draft**
- Opens on the prospect's own specific trigger, with a source URL kept in the file (not in the message). No trigger found → say so; do not fabricate personalization.
- One idea per message: trigger → one reframe or implication → one proof line → one question.
- Proof line matched by sector and size from `context/evidence.md`, or `[NEEDS PROOF: <sector/size result>]`, or a capability-only line. Never a client result that is not in the ledger.
- Ends with a low-friction question CTA ("Worth a look?", "Is this on your radar?"). Not a meeting request in a first touch.
- Banned: "I hope this finds you well", "quick question", "just checking in", "just following up", "touching base", "AI-powered", "cutting-edge", "revolutionize", "game-changer", "leverage" as a verb, "synergy", flattery of their content or company, any "I noticed" line not backed by a real source, fake urgency or fake scarcity.
- Voice: apply `context/voice.md` (words used / never used) after drafting.
- Limits: email body ≤ 90 words, subject ≤ 5 words lower-case; LinkedIn connection note ≤ 280 characters; LinkedIn DM after accept ≤ 70 words. Count them; print the counts.

**Evidence audit before showing.** Dispatch the `evidence-auditor` agent on every set of drafts (see `write` step 9). If agent dispatch is unavailable, run its method inline: list every claim, mark SUPPORTED / UNSUPPORTED / VAGUE / RISKY against `evidence.md`, fix, and show the table.

**Output conventions**
- Prospect lists → `prospects/<YYYY-MM-DD>-<segment-slug>.md`.
- Drafts and sequences → `assets/sequences/<company-slug>-<YYYY-MM-DD>.md` (or `<segment-slug>-...` for segment sequences).
- Email-connector drafts only when the user asks; never send. LinkedIn content is always text for the user to paste.
- Every draft file carries a `tags:` block (angle, trigger type, proof id, CTA type, channel). `review` depends on it.

**Write-back (every mode)**
- One line to `log.md`: `YYYY-MM-DD · outreach · <mode> · <one line>`.
- New buyer phrases from replies or reviews → `memory/voc-swipe.md`.
- Objections → `memory/objections.md` (format in `reply`).
- Prospects that engage → create or update `deals/<company-slug>.md` per the workspace deal format (`stage: lead`, `source: outreach`, `last_touch`, `next_step`, `next_step_date`).
- Learnings → `memory/outreach-learnings.md` (format in `review`).

**Privacy.** Collect only what outreach needs: company, domain, contact name, role, business email or LinkedIn URL, trigger and its URL. Never personal phone numbers, home addresses, family details, personal social accounts, or protected characteristics. Prospect data stays in the workspace; never put it in URLs or tools the user did not choose.

**One recommendation.** End each mode with the single next move (e.g. "Send variant A to the 6 A-tier rows; I've drafted them") and the alternatives in one short line.

## 4. Method library

Load a book file only when a step needs the detail or the user asks why. Cite the framework and book in output when it drives a choice.

| Framework | Used in | Book file |
|---|---|---|
| Commercial Teaching (Warmer, Reframe), Teach-Tailor-Take Control | write, sequence | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/06-the-challenger-sale.md` |
| SPIN Implication questions; Advance vs Continuation | write, reply | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/01-spin-selling.md` |
| Current state / future state, impact | write, reply | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/04-gap-selling.md` |
| Question pitch, subject-line pitch | write | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/08-to-sell-is-human.md` |
| Accusation audit, no-oriented questions, labeling, calibrated questions | write, sequence, reply | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/05-never-split-the-difference.md` |
| Fear of buying the invisible; make it tangible | sequence | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/07-selling-the-invisible.md` |
| The Six Whys | reply | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/09-the-science-of-selling.md` |
| Move off the solution; yellow lights; ORDER | reply | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/10-lets-get-real-or-lets-not-play.md` |
| JOLT (indecision) | reply | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/02-the-jolt-effect.md` |
| Trust Equation (self-orientation) | write, reply | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/03-the-trusted-advisor.md` |
| Cialdini: social proof by similarity, liking, truthful scarcity | write, audit | `${CLAUDE_SKILL_DIR}/../marketing-psychology/books/01-influence.md` |
| Specific claims; salesmanship in print; testing | write, review | `${CLAUDE_SKILL_DIR}/../copywriting/books/04-scientific-advertising.md` |
| Evidence strength; small-sample criteria | review | `${CLAUDE_SKILL_DIR}/../offer-creation/books/09-testing-business-ideas.md` |
