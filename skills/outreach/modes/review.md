# Mode: review `[period]`

## Purpose
Close the learning loop. Count what was sent and what came back, compare reply rates by angle, trigger type, proof line, CTA and channel, call winners and losers only when the sample supports it, and rewrite the "current best angles" block that `write` reads first. Opinions about copy are worth little next to a counted result (Hopkins, Scientific Advertising, `copywriting` book 04).

Default period: the last 30 days. Accept "last 2 weeks", "September", "since 2026-09-01", or "all".

## Inputs
- **Sends and their tags**: every `assets/sequences/*.md` in the period with `status` sent or a send date. Ask the user to confirm which drafts were actually sent if the files only say `draft` (offer a checklist of file names). Tags come from the frontmatter `tags:` block (`angle`, `trigger_type`, `proof_id`, `cta_type`, `channel`, `personalization`, `accusation_audit`, `reply_class`).
- **Replies**: via the **Email** connector (`search_threads` on sent mail in the period, then `get_thread`) and match threads to sequence files by recipient domain and subject. LinkedIn has no connector: ask the user for accepts and replies, or a pasted export. Fallback for everything: pasted stats in any shape (CSV, a sequencing tool's report, a typed summary).
- `memory/outreach-learnings.md` (previous findings and the current block), `memory/objections.md` (objection mix in the period), `log.md`.

## Procedure
1. **Build the send table.** One row per touch sent: date, prospect slug, touch #, channel, all tags, outcome (`no reply`, `auto`, `unsubscribe`, `bounce`, or the reply class). Untagged sends are kept but grouped as `untagged`; tell the user how many.
2. **Check deliverability before judging copy.** If hard bounces > 3% of emails, or overall reply rate (all replies including negative) < 1% across ≥ 100 emails, report a probable deliverability problem (list hygiene, domain warm-up, sending volume) and mark all email copy findings `UNRELIABLE` for this period.
3. **Compute rates per dimension value** (angle, trigger type, proof id, CTA type, channel, personalization, accusation audit):
   - Sends `n` (count first touches separately from follow-ups; first-touch rates are the main comparison).
   - Reply rate = human replies / sends (exclude `auto` and bounces from both).
   - Positive reply rate = (`interested` + `referral` + `objection` that reached an Advance) / sends.
   - Advance rate = replies that produced a dated next step / sends.
   - Baseline = the same rate across all tagged sends in the period.
4. **Apply the minimum-sample rules.** Small agencies have small samples; set criteria as counts (Testing Business Ideas, `offer-creation` book 09).
   - **Winner**: n ≥ 30 sends AND ≥ 3 positive replies AND positive reply rate ≥ 1.5x baseline.
   - **Loser**: n ≥ 30 sends AND (0 positive replies OR positive reply rate ≤ 0.5x baseline).
   - **Directional**: 15 ≤ n < 30 with a ≥ 2x difference from baseline. Report as a hunch, never put in the best-angles block as a winner.
   - **Inconclusive**: everything else. Say "keep testing" and how many more sends are needed to reach 30.
   - Compare only like with like: one dimension at a time, same segment, same touch number. If one angle was only ever paired with one trigger type, say the effects are confounded.
5. **Read the replies, not only the counts.** Pull 3–5 verbatim phrases that explain why a winner worked or a loser failed (they go to `voc-swipe.md`). Summarise the objection mix from `objections.md` for the period: which why (Hoffeld) dominated.
6. **Check proof effects.** Compare sends with a ledger proof line vs `capability-only` vs `needs-proof`. If capability-only sends perform close to proof sends, say so; if proof sends win clearly, list the proof gaps (from `## Proof gaps`) worth closing first.
7. **Decide the next tests.** At most 2 changes for the next period, each with a hypothesis, the variable, the control, and the target n ("Test the no-oriented CTA against worth-a-look on dental first touches, 30 each").
8. **Rewrite the best-angles block** at the top of `memory/outreach-learnings.md` (template below). Only winners enter it. Losers enter the "avoid" list. Keep per-segment entries; never delete a previous winner without a new period's data showing it dropped below baseline at n ≥ 30.
9. **Append the dated findings** below the block. Never edit earlier dated sections.

## Output
In chat: a short scorecard (sends, reply rate, positive rate, Advance rate vs last period), winners, losers, directional hunches, the two next tests, and one recommendation.

The block at the top of `memory/outreach-learnings.md` (replace in place):

```markdown
<!-- best-angles:start -->
## Current best angles (updated YYYY-MM-DD from review of <period>)
| Segment | Dimension | Use | Evidence (n, positive rate vs baseline) | Since |
|---|---|---|---|---|
| <segment> | angle | <angle name>: <one-line description> | n=42, 9.5% vs 4.1% | YYYY-MM-DD |
| <segment> | trigger | <type> | | |
| <segment> | proof | <evidence id> | | |
| <segment> | CTA | <cta type + example wording> | | |
| <segment> | channel | <channel / order> | | |

**Avoid:** <dimension: value (n, rate)> · …
**Testing now:** <test 1> · <test 2>
<!-- best-angles:end -->
```

Dated findings, appended below:

```markdown
## Review YYYY-MM-DD · <period>
Source: <email connector | pasted stats | user-confirmed list> · Sends: <n first touches> + <n follow-ups> · Untagged: <n>
Deliverability: OK | UNRELIABLE (<reason>)
Overall: reply <x%> · positive <y%> · Advance <z%> (prev period: …)

| Dimension | Value | n | Reply % | Positive % | vs baseline | Verdict |
|---|---|---|---|---|---|---|

Verbatims: "<phrase>" (<slug>, <date>) · …
Objection mix: why change <k> · why now <k> · why you <k> · …
Proof effect: <one line>
Next tests: 1. <hypothesis, variable, control, target n> 2. …
```

## Write-back
- `memory/outreach-learnings.md`: block replaced, dated section appended (above).
- `memory/voc-swipe.md`: the verbatims, each `YYYY-MM-DD · "<phrase>" · <slug> · <channel>`, under the right category.
- `memory/objections.md`: update `Outcome:` fields for any objections resolved in the period.
- `log.md`: `YYYY-MM-DD · outreach · review · <period>: <n> sends, positive <y%>, winners <k>, losers <k>`.

## Quality gate
- [ ] Every rate shows its n; no percentage without a count.
- [ ] Winner and loser calls meet the minimum-sample rules; under-30 results are labeled directional or inconclusive.
- [ ] Deliverability checked before any copy verdict.
- [ ] Confounded comparisons flagged.
- [ ] Best-angles block contains only winners, with evidence and date; avoid list and current tests present.
- [ ] Findings appended with date and source; earlier sections untouched.
- [ ] Evidence rule: any recommended new proof line comes from `evidence.md`; gaps are listed as gaps, not filled.

## Failure modes
- **Crowning a winner on 8 sends.** Two replies out of eight is noise. The rules exist to stop this.
- **Counting auto-replies as replies.** Inflates rates and hides deliverability problems.
- **Blaming copy for deliverability.** A 0.4% reply rate across 300 emails is a sending problem first.
- **Changing everything at once.** Two variables per period at most, or nothing can be attributed.
- **Untagged sends.** If `write` drafts were edited before sending, ask the user what changed and re-tag; otherwise they cannot teach anything.
- **Overwriting history.** The dated sections are the audit trail; only the block at the top is replaced.
