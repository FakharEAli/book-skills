# Mode: review `<draft proposal | deck | offer page | pitch>`

## Purpose
Critique an existing proposal, deck, sales page or pitch script against the seven tests that decide whether a buyer signs, score it, and rewrite the weakest section so the user leaves with something better, not just a list of flaws.

## Inputs
- The draft: pasted text, a local file path, or a link via the **Docs** or **Decks** connector (read only; never edit the source document). Fallback: ask the user to paste it or export to markdown/PDF.
- If a company is named: `deals/<slug>.md` (Gap, verbatims, impact numbers, named risks) so the review can check the draft against what the buyer actually said.
- `context/evidence.md` (for the audit), `context/pricing.md` (floor, trades), `context/voice.md`.
- If the draft is not a proposal (e.g. a landing page), keep the same seven tests and note which do not apply (score N/A, excluded from the total).

## Procedure

1. **Identify** the artifact type, the audience, and the stage it is used at (pre-call, post-discovery, final). Locate the buyer's gap, the recommendation, the plan, the risk terms, the price, and the ask; note where each is or that it is missing.

2. **Run the evidence audit first.** Dispatch `book-skills:evidence-auditor` with the Agent tool. Pass the full draft text, the full text of `context/evidence.md` (or "NO EVIDENCE FILE: treat every claim as unsupported"), and: "List every claim about results, clients, timelines, capability or experience; for each, quote the matching evidence line or return NEEDS PROOF with a replacement." If dispatch is unavailable, do it inline: list each claim, match it to an evidence line, else mark `[NEEDS PROOF]`, and name the proof type that would back it (social proof, authority, demonstration; Cialdini, `client-eagerness-playbook` book 06).

3. **Score the seven tests**, 0 / 1 / 2 each:

   | # | Test | 0 | 1 | 2 | Method |
   |---|---|---|---|---|---|
   | 1 | Gap in the buyer's words | no buyer problem, or only yours | problem stated, no verbatims or impact | current → future → impact → root cause with ≥ 2 sourced verbatims | Gap Selling, `sales-psychology` book 04 |
   | 2 | One recommendation | 3+ options or a menu | 2 options, none recommended | one recommendation (or 2 with one clearly recommended) and why | JOLT, book 02 |
   | 3 | Risk reversal | none | vague ("we stand behind our work") | specific pilot / milestone billing / exit clause matched to a named risk | JOLT, book 02; Hormozi, `offer-creation` book 01 |
   | 4 | Tangible plan | "we'll build it" | phases but no owners or visible results | named phases, owners both sides, buyer hours, week 1/2/4 visible results, sample output | Beckwith, `sales-psychology` book 07 |
   | 5 | Evidence audit pass | unsupported claims presented as fact | some unsupported claims | every claim traced or marked `[NEEDS PROOF]` | Cialdini, `client-eagerness-playbook` book 06 |
   | 6 | Price justified by impact | price with no impact | impact stated but no math | ROI and payback math in the buyer's numbers, price after value | Keenan book 04; Ramanujam, `offer-creation` book 04 |
   | 7 | Clear, dated Advance | "let us know" | action without date or owner | one action, owner, date ≤ 7 days | SPIN, `sales-psychology` book 01 |

   Total /14 (exclude N/A from the denominator). Verdict: ≥ 12 **ready to send** (after fixes listed) · 8–11 **revise** · ≤ 7 **rebuild with `pitch proposal`**.
   Automatic cap: any unsupported result or client claim caps the verdict at "revise" regardless of score.

4. **Quote the problem lines.** For each test scoring 0 or 1, quote the exact line(s) from the draft (≤ 25 words each) and say in one sentence what is wrong.

5. **Also flag** (no score): self-orientation signals (Trust Equation, Maister et al., `sales-psychology` book 03): first page about "we" rather than "you"; jargon the buyer never used; words banned in `context/voice.md`; length over 1,500 words for a first proposal; discount offered in the document; price below the floor in `pricing.md`.

6. **Pick the weakest section**: lowest score; on ties, the earlier test in the table (a missing gap undermines everything after it). Rewrite that section in full using the draft's own facts plus deal-file facts. Where a needed fact is missing, insert `[ASK BUYER: …]` or `[NEEDS PROOF: …]` rather than inventing. Keep the rewrite within ±20% of the original section length unless the original is a single line or missing.

7. **Top 3 fixes** for the rest, each one line, ordered by impact on the verdict.

## Output

```markdown
## Review · <artifact> · <company or audience> · <YYYY-MM-DD>
**Score:** <n>/<14 or less> · **Verdict:** <ready | revise | rebuild> <cap note if any>

| # | Test | Score | Evidence from draft | Fix |
|---|---|---|---|---|
| 1 | Gap in buyer's words | <0-2> | "<quote>" | … |
| 2 | One recommendation | … | … | … |
| 3 | Risk reversal | … | … | … |
| 4 | Tangible plan | … | … | … |
| 5 | Evidence audit | … | <n> claims, <n> unsupported | … |
| 6 | Price vs impact | … | … | … |
| 7 | Dated Advance | … | … | … |

**Evidence audit:** <claim → evidence line | NEEDS PROOF> (method: agent | inline)
**Other flags:** <self-orientation, voice, length, discount, floor>

### Rewrite: <weakest section name>
<full rewritten section>

### Next 3 fixes
1. … 2. … 3. …
```

Save to `assets/reviews/<YYYY-MM-DD>-<slug>.md` when a deal file exists or the user asks.

## Write-back
- `deals/<slug>.md` Timeline (if a deal exists):
  ```markdown
  ### <YYYY-MM-DD> · Proposal reviewed · pitch review
  - Score: <n>/14 · Verdict: <…> · Weakest: <test> · Unsupported claims: <n>
  ```
- `context/evidence.md`: never edited by this mode. If the draft contained real results the user confirms are true, list them as "Candidates for evidence.md" and ask the user for the source before adding.
- `log.md`: `<date> · pitch · review · <artifact> <n>/14 <verdict> · <slug or file>`.

## Quality gate
- [ ] All seven tests scored with a quoted line or "missing".
- [ ] Evidence audit run (agent or inline) and its result shown.
- [ ] Verdict follows the thresholds and the unsupported-claim cap.
- [ ] Rewrite is a full section, uses only real facts, marks gaps.
- [ ] No claim added in the rewrite that is not in the draft, the deal file, or `evidence.md`.
- [ ] Source document untouched.

## Failure modes
- **Polishing prose while the structure is wrong:** a missing gap or three-tier menu outranks wording.
- **Generous scoring:** a 2 requires every element in the column; otherwise 1.
- **Rewrite invents proof or numbers:** use placeholders.
- **Reviewing against generic best practice** when the deal file shows what the buyer said: check the draft against their words.
