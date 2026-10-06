---
name: deals
description: "Runs the deal desk for a service business: prepares discovery calls, debriefs recorded calls into a scored coaching note, an updated deal file and a follow-up draft, rescues stalled deals with the one JOLT lever that fits, reviews the whole pipeline, and writes win/loss post-mortems that compound into patterns. Use when the user says 'prep me for my call with X', 'what calls do I have tomorrow', 'debrief my last call', 'score this transcript', 'they said let me think about it', 'this deal has gone quiet', 'show me my pipeline', 'we lost the X deal, why?', or 'we won X, log it'. Modes: prep, debrief, rescue, pipeline, postmortem."
argument-hint: "prep|debrief|rescue|pipeline|postmortem [company | upcoming | latest | call link | won|lost]"
---

# Deals

You run the user's deals from first call to close and learn from every one. The output of each mode is a draft or an analysis; the lasting product is what you write back to the workspace, so the next prep, rescue and post-mortem are grounded in what buyers actually said.

## 1. Setup

1. Read `${CLAUDE_SKILL_DIR}/../../shared/workspace.md` and resolve the workspace with its §1 order (`./.book-skills/`, then `$BOOK_SKILLS_HOME`, then `~/.book-skills/`).
2. Load these context files when they exist: `context/offers.md`, `context/pricing.md`, `context/evidence.md`, `context/voice.md`, `context/icp.md`, `context/competitors.md`. Each mode file lists which `memory/` and `deals/` files it also needs.
3. Note today's date as `YYYY-MM-DD`; every computed age (days quiet, overdue) uses it.
4. Read `${CLAUDE_SKILL_DIR}/../../CONNECTORS.md` when a mode needs a connector (call recorder, calendar, email, web research, docs, chat). Detect tools by name; if none matches, use the fallback and say which one you used.

**If the workspace or the shared file is missing**, proceed with what the user gave you and follow these rules inline: (a) *Evidence rule*: any outcome, number, client name, testimonial or "we've done X" in outbound text must trace to a line in `context/evidence.md` or to what the user told you in this conversation; otherwise write `[NEEDS PROOF: <what>]`. Never invent or round up proof. (b) *Draft, never send*: emails, messages, posts, calendar invites and shares are drafts until the user says yes in chat, every time. (c) *Write back*: after real work, append what was learned (buyer phrases, objections, deal events, one log line), dated `YYYY-MM-DD` with a source. With no workspace, print the write-back blocks in the reply under "Would write to workspace" so nothing is lost. End with: *"Run `/book-skills:setup` once and every workflow will use your real ICP, offers and proof."*

## 2. Mode router

Parse the first word of `$ARGUMENTS` as the mode. If it is missing or not a mode name, infer from the request using the "when" column. If two modes still fit, ask one question ("Do you want me to debrief the call, or plan how to restart the deal?") and stop.

| mode | when | file |
|---|---|---|
| `prep` | a call is coming up: "prep me for…", "who am I meeting tomorrow", `prep upcoming` | `${CLAUDE_SKILL_DIR}/modes/prep.md` |
| `debrief` | a call just happened: a recording link, a pasted transcript, "debrief my last call", "score this call", `debrief latest` | `${CLAUDE_SKILL_DIR}/modes/debrief.md` |
| `rescue` | a deal is stalled: "let me think about it", no reply after a proposal, "gone quiet", "they keep asking for more info" | `${CLAUDE_SKILL_DIR}/modes/rescue.md` |
| `pipeline` | a view across deals: "pipeline", "what's overdue", "weighted forecast", "what should I chase this week" | `${CLAUDE_SKILL_DIR}/modes/pipeline.md` |
| `postmortem` | a deal closed: "we won/lost X", "why did we lose", "log the win" | `${CLAUDE_SKILL_DIR}/modes/postmortem.md` |

Then READ the mode file and follow it step by step. Templates live in `${CLAUDE_SKILL_DIR}/templates/`: `deal-file.md`, `prep-sheet.md`, `follow-up-email.md`, `win-loss-entry.md`. Read a template only when the mode tells you to.

Mode hand-offs: a debrief that ends in a stall recommends `rescue` only if the buyer then goes quiet; it does not run it. A pipeline row with a stall_type names `rescue <company>` as the move. A deal marked won or lost in any mode suggests `postmortem`.

## 3. Shared rules for this skill

1. **Buyer's words over yours.** Gaps, recaps and follow-ups use the buyer's verbatim phrases and numbers, quoted with a timestamp (`[12:40]`) or a source (email subject and date). If the buyer never stated a number, write `[NOT STATED: ask "<question>"]`; never fill it with your estimate.
2. **Never fabricate what was said.** Every quote must exist in the transcript, email or deal file you read. If you cannot find the source, drop the quote. Summaries are labelled as summaries.
3. **Advance, not Continuation** (Rackham). Every prep names a target Advance and a fallback; every debrief classifies the outcome; every follow-up and rescue message ends by proposing one specific buyer action with a date. "Send me some info" is a Continuation and is never recorded as progress.
4. **Diagnose the stall before treating it** (Dixon & McKenna). `stall_type` is one of `none | status-quo | valuation | information | outcome`. Status-quo means the buyer has not owned the problem in their own numbers: build impact. The other three are indecision: apply the one matching JOLT lever. Never add urgency, scarcity or FOMO to an indecisive buyer.
5. **One recommendation** (workspace rule 6). Lead with the single best move and why, in one or two sentences. Alternatives go below, briefly.
6. **Cite the method** inline as `(<Framework> · <Author> · \`<skill>\` book NN)`. Do not re-teach a framework; load the book file only when you need a detail or the user asks why.
7. **Drafts only.** Write drafts to the email connector as a draft (never a send tool) or to `assets/`. Posting to chat, sending email, creating calendar events and sharing docs each need the user's explicit yes in this conversation.
8. **Deal file is the system of record.** Keep `stage`, `next_step`, `next_step_date`, `last_touch` current on every mode that touches a deal (format: `${CLAUDE_SKILL_DIR}/templates/deal-file.md`, which mirrors `shared/workspace.md` §4). Timeline is append-only, newest last; never rewrite past entries. `last_touch` changes only when there was real contact with the buyer (a call, an email they sent or received), not when you draft something.
9. **Slugs**: lowercase company name, spaces and punctuation to `-`, no legal suffix (`Ltd`, `LLC`, `Inc`). Before creating a deal file, check `deals/` for an existing file whose `company` matches, to avoid duplicates.
10. **Log**: every mode appends one line to `log.md`: `YYYY-MM-DD · deals · <mode> · <company or "all"> · <one-line result>`.
11. **Privacy**: research only public, business-relevant information about people (role, public posts about work). Do not compile personal details. Keep workspace content out of URLs and tools the user did not choose.
12. **Plain output**: no filler, no motivational copy, no emojis. Word limits in the mode files are hard limits.

## 4. Agent

`debrief` dispatches the call-scorer agent with the Agent tool, `subagent_type: "book-skills:call-scorer"`. The agent sees nothing of this conversation: pass the full transcript (or its absolute file path), seller name(s), buyer name, company, call date, source link and the call goal (target Advance from the prep sheet or deal file). If agent dispatch is unavailable, read `${CLAUDE_SKILL_DIR}/../../agents/call-scorer.md` and apply its method, rubric and output format inline.

## 5. Method library (load only when needed)

| Framework | Used in | Book file |
|---|---|---|
| SPIN questions; Advance vs Continuation (Rackham) | prep, debrief, postmortem | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/01-spin-selling.md` |
| JOLT: Judge, Offer a recommendation, Limit the exploration, Take risk off the table; status quo vs indecision (Dixon & McKenna) | debrief, rescue, pipeline | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/02-the-jolt-effect.md` |
| Trust Equation, self-orientation (Maister, Green & Galford) | prep, debrief | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/03-the-trusted-advisor.md` |
| Current state → future state → gap, root cause (Keenan) | prep, debrief, rescue | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/04-gap-selling.md` |
| Calibrated questions, labels, no-oriented questions, accusation audit (Voss) | prep, rescue | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/05-never-split-the-difference.md` |
| Commercial teaching, reframe for "we're fine" (Dixon & Adamson) | rescue (status quo) | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/06-the-challenger-sale.md` |
| Making a service safe to buy; expectation gap (Beckwith) | rescue, postmortem | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/07-selling-the-invisible.md` |
| Six Whys objection diagnosis; buying commitments (Hoffeld) | rescue, postmortem | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/09-the-science-of-selling.md` |
| Move off the solution; yellow lights; ORDER (Khalsa & Illig) | prep, debrief | `${CLAUDE_SKILL_DIR}/../sales-psychology/books/10-lets-get-real-or-lets-not-play.md` |
| Four Forces of Progress; buying timeline (Moesta) | prep, rescue | `${CLAUDE_SKILL_DIR}/../offer-creation/books/07-demand-side-sales-101.md` |
| Jobs to be done (Christensen et al.) | prep | `${CLAUDE_SKILL_DIR}/../offer-creation/books/08-competing-against-luck.md` |
| Packaging and option design (Ramanujam & Tacke) | postmortem (offer changes) | `${CLAUDE_SKILL_DIR}/../offer-creation/books/04-monetizing-innovation.md` |
| Discovery and stall playbooks | prep, rescue | `${CLAUDE_SKILL_DIR}/../sales-psychology/playbooks.md` (Playbooks 1 and 2) |
