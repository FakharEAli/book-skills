# Mode: reply `<pasted reply>`

## Purpose
Classify a prospect's reply, diagnose what is really behind it, and draft a response whose goal is an Advance: a specific action by the buyer, with a date, that moves the sale forward (Rackham, SPIN Selling, `sales-psychology` book 01). A pleasant reply with no agreed action is a Continuation and counts as a miss.

## Inputs
- The reply text (pasted, or fetched via the **Email** connector with `search_threads` / `get_thread` when the user names the thread). Also the message it answers: find it in `assets/sequences/<slug>-*.md` or ask for it.
- `deals/<slug>.md` if one exists; `memory/objections.md` (has this objection been answered before, and what worked?); `context/competitors.md` (what the named alternative does well and where it stops); `context/offers.md`, `context/pricing.md` (what you can trade instead of discounting), `context/evidence.md`, `context/voice.md`.
- **Calendar** connector, optional, to propose real free slots (`suggest_time`, `list_events`). Fallback: propose two specific slots in the next 3–5 business days and mark them `[CHECK CALENDAR]`.

## Procedure
1. **Classify** into exactly one class. Use the first rule that matches:

| Class | Signal | Goal of the response |
|---|---|---|
| `unsubscribe` | "remove me", "stop", "not interested" with no qualifier, legal threats | Confirm removal in one line. No pitch. Stop all channels. |
| `auto` | OOO, delivery failure, ticket-system acknowledgement | No reply. Pause sequence until return date + 2 business days. |
| `referral` | "talk to X", "not me, it's our ops manager" | Thank, ask permission to mention them, write a 2-line intro note the referrer can forward. Advance = intro sent by a date. |
| `not now` | "maybe next quarter", "busy until…", "after our launch" | Label the timing, ask one question that tests whether the problem is real, propose a dated check-in. Advance = agreed date to revisit. |
| `objection` | interest plus a reason not to proceed ("but we already use…", "too expensive", "we tried AI and it didn't work", "we do it in-house") | Diagnose the why (step 2), move off the solution (step 3), propose an Advance with a time. |
| `interested` | asks how it works, asks price, asks for a time, forwards to a colleague | Answer the one question asked in ≤ 2 sentences, propose an Advance with two times. |

   If a reply mixes signals, the more restrictive class wins (unsubscribe > auto > referral > not now > objection > interested). State the class and the one-line reason.
2. **Diagnose the objection with Hoffeld's Six Whys** (`sales-psychology` book 09): find which why the buyer has not yet answered and respond to that, not to the surface words.
   - "We already use <tool/vendor/VA>" → usually **Why change?** (status quo feels adequate) and sometimes **Why your industry solution?** (they think their category already covers it).
   - "Too expensive" / "no budget" → usually **Why change?** or **Why now?** dressed as **Why spend the money?**.
   - "We tried AI / automation before" → **Why you?** plus outcome fear (see step 4).
   - "We'll do it in-house" → **Why your industry solution?** (build vs buy).
   - "Not a priority" → **Why now?**
   Check `memory/objections.md` for the same objection; reuse what worked and say so.
3. **Move off the solution** (Khalsa, Let's Get Real or Let's Not Play, `sales-psychology` book 10). The buyer has anchored on a solution (their current tool, or your pitch as they imagined it). Acknowledge it without contesting it, then ask one question that gets underneath it to the business result: what the current setup is not doing, where it breaks, what it costs. For "we already use Zapier": "Good, then the plumbing's there. What's the part Zapier isn't handling today, the bits someone still does by hand?" Use a calibrated "what/how" question (Voss, book 05). Never criticise the tool, the vendor or their choice; never claim the alternative is bad. Draw on `competitors.md` only to know where the alternative stops, not to attack it.
4. **If the reply shows indecision** ("need to think", "send more info", "comparing a few options", "worried it won't work for us"), apply JOLT (`sales-psychology` book 02): **J**udge which source dominates (valuation, lack of information, outcome uncertainty); **O**ffer a recommendation ("Given what you've said, I'd start with just the after-hours piece"); **L**imit the exploration (send one thing, not a deck); **T**ake risk off the table with a smaller first step, a pilot or defined exit criteria from `offers.md`, and set expectations conservatively. Never invent a guarantee not in `offers.md`.
5. **Propose the Advance.** One concrete next step, owned by the buyer, with a date or two specific times: e.g. "Want me to sketch which of your current steps I'd automate and walk you through it Thursday at 10:00 or Friday at 14:00, 20 minutes?" or "Could you send me the two workflows your team still does by hand, and I'll come back by Wednesday with a one-page outline?" A vague "let me know" or "happy to chat sometime" fails.
6. **Hold value; do not discount.** No price cuts, free months, or "special pricing" in a reply to an objection. If price is raised, trade scope or terms from `pricing.md` (smaller first phase, payment schedule) and return to the size of the problem (Challenger: hold price by returning to the reframed problem, book 06).
7. **Draft the response.** ≤ 80 words for email, ≤ 60 for LinkedIn. Structure: acknowledge (label their position: "Sounds like the automation side is already covered") → one question that moves off the solution → the Advance with time. Proof only from the ledger or `[NEEDS PROOF]`. Banned list from SKILL.md applies. No accusation audit unless the reply was hostile.
8. **Self-check**: class stated; the why named; exactly one question before the Advance; the Advance has a day/time or date; no discount; no criticism of the alternative; word count printed.
9. **Run the evidence auditor** if the draft contains any claim, number or client reference (`subagent_type: "book-skills:evidence-auditor"`; inline if unavailable).
10. **Save and write back** (below). Create an email-client draft in the thread only if the user asks; never send.

## Output
In chat, and appended to `assets/sequences/<slug>-<YYYY-MM-DD>.md` under `## Replies`:

```markdown
### Reply · YYYY-MM-DD · <channel>
> <verbatim reply>

Class: <class> · Reason: <one line>
Why unanswered (Hoffeld): <why change | why now | why category | why you | why product | why spend | n/a>
Approach: <move off the solution (Khalsa) | JOLT: <lever> | referral intro | timing check>

**Draft response (<n> words)**
<text>

Advance sought: <buyer action> by <date/time>
Fallback if no answer in 3 business days: <one line>
```

## Write-back
- `memory/objections.md` (for `objection` and `not now`), append:
  ```markdown
  ### YYYY-MM-DD · <company-slug> · <channel> "<subject or first 6 words>"
  - Verbatim: "<exact objection text>"
  - Class: objection · Why: <why> (Hoffeld) · Alternative named: <tool/vendor/none>
  - Real cause (hypothesis): <one line>
  - Response: <approach + the question asked>
  - Advance proposed: <action> · <date>
  - Outcome: pending
  ```
  When a later reply resolves it, update `Outcome:` with the result and date rather than adding a duplicate.
- `memory/voc-swipe.md`: any vivid buyer phrase, verbatim, under its category, with date and source.
- `deals/<slug>.md`: for `interested`, `objection`, `referral` or `not now`, create the file if missing (`stage: lead`, `source: outreach`) per the workspace deal format; set `last_touch` to today, `next_step` to the Advance, `next_step_date` to its date; append a Timeline entry `### YYYY-MM-DD · Reply (<class>) · <channel>`.
- For `unsubscribe`: mark the prospect row `do-not-contact` in its `prospects/` file, append `- <email> · unsubscribed · YYYY-MM-DD · reply` to `memory/suppression.md`, and stop the sequence.
- `log.md`: `YYYY-MM-DD · outreach · reply · <Company>: <class>, why <why>, Advance <action> <date>`.
- Update the sequence file's `tags:` with `reply_class: <class>` so `review` can count it.

## Quality gate
- [ ] Exactly one class, with the rule that decided it.
- [ ] For objections: the unanswered why named; the response moves off the solution with a "what/how" question.
- [ ] The Advance is a specific buyer action with a date or two specific times; not a Continuation.
- [ ] No discount, no freebie, no criticism of the named alternative.
- [ ] Evidence rule: no outcome, number or client name outside `evidence.md`; `[NEEDS PROOF]` where needed.
- [ ] Within word limits; counts printed.
- [ ] Objection logged to `memory/objections.md`; deal file updated; nothing sent.

## Failure modes
- **Answering the surface.** Rebutting "we use Zapier" with feature comparisons; the issue is usually why change, not features.
- **Bashing the incumbent.** It insults the buyer's past decision and triggers consistency defence (Cialdini, commitment and consistency, `marketing-psychology` book 01).
- **Discounting to rescue interest.** Signals the price was never real and lowers perceived value.
- **Continuations.** "Happy to share more whenever suits!" ends the thread. Always a date.
- **Two questions plus an ask.** Overloads a cold buyer; one question, one Advance.
- **Treating "not now" as "no".** Ask whether the problem is real; if it is, a dated revisit is a legitimate Advance.
