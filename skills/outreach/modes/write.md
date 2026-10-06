# Mode: write `<prospect | list file>`

## Purpose
For each prospect, produce three evidence-checked drafts: a cold email, a LinkedIn connection note and a LinkedIn DM for after the connection is accepted. Each is built on the prospect's own trigger, one reframe, one matched proof line and one easy question. Drafts only; nothing is sent.

## Inputs
- **The prospect**: a row from a `prospects/*.md` file, a company name and domain, or a description in the message. For a list file, process A-tier rows first (max 10 per run; ask before doing more).
- `memory/outreach-learnings.md`: READ the block between `<!-- best-angles:start -->` and `<!-- best-angles:end -->` FIRST. Prefer the current winning angle, trigger framing, proof line style and CTA for this segment; avoid listed losers. If the block is absent, say "no tested angles yet" and proceed.
- `context/evidence.md` (proof ledger), `context/offers.md` (what can be offered), `context/voice.md`, `context/icp.md` (segment pains), `context/competitors.md`.
- **Web research** connector (or `web-research` skill) for the prospect's site, recent posts, reviews, job ads. Fallback: ask the user for 2–3 URLs or pasted text.
- **Email** connector only if the user asked for email drafts in their mail client.

## Procedure
1. **Load the best-angles block** (above). Note which angle you will use and why in one line.
2. **Research 2–3 specifics** about this prospect, each with a URL and date: (a) the trigger from the list row, re-verified; (b) one detail from their site or service pages (how bookings, enquiries or quotes are handled today); (c) one of: a recent post by the contact, a review theme, a job ad's duties list. Use only public business information. If you find fewer than 2 verifiable specifics, say so, write a segment-level version, and tag it `personalization: segment` so `review` can compare.
3. **Choose the angle.** Turn the trigger into an implication the buyer has not priced. Use Challenger Commercial Teaching: a Warmer (show you understand peers like them) compressed into the trigger line, then one Reframe ("the cost isn't the hire, it's the enquiries that wait while the role is empty") (`sales-psychology` book 06). Or phrase it as a SPIN Implication question ("When the front desk is short, what happens to calls after 5pm?") (book 01). One reframe per message; never two.
4. **Pick the proof line** by Cialdini similarity: social proof works most when the others are similar in sector and size (`marketing-psychology` book 01). Search `evidence.md` in this order: same sector + similar size (0.5x–2x) → same sector → same problem in an adjacent sector → none. Quote the ledger line exactly; keep its numbers as written (never round up, never combine two clients). If none qualifies, use either `[NEEDS PROOF: <sector> result for <problem>]` or a capability-only line that states what you build and how it works, with no outcome claimed ("We build the after-hours text-back and booking hand-off; it runs on the phone system you already have."). Never imply prior clients you cannot name in the ledger.
5. **Decide on an accusation audit** (Voss, `sales-psychology` book 05). Use one short clause in cold contexts where the likely objection is "another agency pitching AI": "You probably get a lot of these, and most promise more than they ship." Use it in at most one of the three variants; skip it if the voice file rules it out or the message is already at the word limit.
6. **Write the CTA as a question pitch** (Pink, `sales-psychology` book 08): a question that makes them generate the reason, low-friction, answerable in one word. Good: "Worth a look?", "Is this on your list for Q4, or not a priority?", "Would a 2-minute walkthrough of how it'd work for <Company> be useless?" (no-oriented, Voss). Bad: "Do you have 15 minutes this week?", "When can we hop on a call?".
7. **Draft the three variants.**
   - **Cold email.** Subject ≤ 5 words, all lower-case, specific to them (Pink's subject-line pitch: utility or curiosity plus specificity), e.g. "front desk role and calls". Body ≤ 90 words: line 1 trigger (their fact, no "I noticed" unless sourced) → line 2 reframe or implication → line 3 proof line → line 4 question CTA. Sign-off with the user's name only. No links in the first email unless the user insists (deliverability); no attachments.
   - **LinkedIn connection note.** ≤ 280 characters including spaces. Trigger + one-line reason to connect + no pitch, no link. A question is optional here; the ask is the connection.
   - **LinkedIn DM after accept.** ≤ 70 words. Thank-free opening, trigger or reframe, proof line, question CTA. Different wording from the email; never paste the email.
8. **Self-check** each variant: count words / characters and print them; scan for the banned list in SKILL.md §3 and for flattery ("love what you're doing", "impressive growth"); check Hopkins's salesmanship-in-print test: would you say this sentence across a desk to this person (`copywriting` book 04)? Check self-orientation: count "we/I/our" vs "you/your"; if "we" sentences outnumber "you" sentences, rewrite (Trust Equation, `sales-psychology` book 03).
9. **Dispatch the evidence auditor** before showing anything. Use the Agent tool with `subagent_type: "book-skills:evidence-auditor"` and pass in the prompt: the full text of all drafts, the absolute path to `context/evidence.md` (or its full content if no workspace), the prospect's sector and size, and the claims context ("cold outreach; no guarantees offered unless in offers.md"). Apply every fix it returns. If verdict is FIX REQUIRED after fixes, show the remaining `[NEEDS PROOF]` markers to the user rather than removing the claim silently. If agent dispatch is unavailable, run the auditor's method inline (claim table → SUPPORTED / UNSUPPORTED / VAGUE / RISKY → corrected draft → verdict) and show the table.
10. **Save** to `assets/sequences/<company-slug>-<YYYY-MM-DD>.md` (template below). Create email drafts through the Email connector only if the user asked; never send. Then offer `sequence` for this prospect.

## Output
```markdown
---
prospect: <Company>
slug: <company-slug>
contact: "<Name>, <role>"
date: YYYY-MM-DD
status: draft
audit: PASS | FIX REQUIRED (<n> NEEDS PROOF)
tags:
  angle: <short name, e.g. empty-role-cost>
  trigger_type: job-post | new-hire | funding | reviews | tech-change | competitor-churn | none
  proof_id: <evidence.md line id | needs-proof | capability-only>
  cta_type: worth-a-look | priority-check | no-oriented | other
  personalization: specific | segment
  accusation_audit: yes | no
---

# Outreach drafts · <Company> · YYYY-MM-DD

## Research (sources)
1. <specific> · <URL> · <date>
2. <specific> · <URL> · <date>
3. <specific> · <URL> · <date>

Angle: <one line, framework + book> · Best-angles block used: <yes: which / no tested angles yet>

## A. Cold email (<n> words)
Subject: <≤ 5 words, lower-case>

<body>

<name>

## B. LinkedIn connection note (<n> chars)
<text>

## C. LinkedIn DM after accept (<n> words)
<text>

## Evidence audit
<auditor table and verdict, condensed>
```

In chat: show the three drafts with counts, the audit verdict, any open `[NEEDS PROOF]`, and one recommendation.

## Write-back
- `log.md`: `YYYY-MM-DD · outreach · write · <Company>: 3 drafts, angle <angle>, audit <verdict> (<file path>)`.
- If a proof gap blocked the best angle, append to `memory/outreach-learnings.md` under `## Proof gaps`: `YYYY-MM-DD · <segment> · needed: <claim> · used instead: <capability-only | NEEDS PROOF>`.
- Do not create a deal file yet; `reply` does that when the prospect engages.

## Quality gate
- [ ] Best-angles block read first (or its absence stated).
- [ ] 2–3 researched specifics with URLs, or tagged `personalization: segment`.
- [ ] Structure holds: trigger → one reframe/implication → one proof line → question CTA.
- [ ] Email body ≤ 90 words; subject ≤ 5 words, lower-case; connection note ≤ 280 chars; DM ≤ 70 words; counts printed.
- [ ] Each email and DM ends with a question mark.
- [ ] Evidence rule: every outcome, number, client name or "we've done X" is a verbatim ledger line, or `[NEEDS PROOF: …]`, or removed for a capability-only line. No implied guarantees.
- [ ] No banned phrase, no flattery, no fake personalization, no fake scarcity.
- [ ] Evidence auditor dispatched (or run inline) and its fixes applied.
- [ ] `tags:` block complete.
- [ ] Status is draft; nothing sent.

## Failure modes
- **Inventing a result to fill the proof slot.** The commonest and most damaging error. No ledger line, no number.
- **Fake personalization.** "Loved your recent post" with no post read. Every specific needs a URL in the Research section.
- **Pitching before teaching.** Leading with "we build AI agents" instead of their trigger; the solution belongs at the end of Commercial Teaching, not the start.
- **Meeting-ask CTAs.** "15 minutes?" asks for a commitment before value; use the question pitch.
- **Copy-paste across channels.** The DM must read as a different message; repeat content trains them to ignore you.
- **Over-length.** Count, do not estimate. Cut adjectives and the second idea first.
- **Ignoring the learnings block.** Re-testing a proven loser wastes sends; if you deviate from the block, state the reason (e.g. new segment).
