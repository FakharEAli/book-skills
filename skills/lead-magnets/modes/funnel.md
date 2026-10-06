# Mode: funnel `<magnet>`

## Purpose
Draft everything that carries a prospect from first sight of the magnet to a booked conversation: landing page, thank-you page, a 5-email nurture, and a LinkedIn launch post with 3 comment-bait variants. All drafts; nothing goes live.

## Inputs
- **The magnet.** `assets/magnets/<magnet-slug>/magnet.md` (or pasted). Need: name, format, core sentence, segment, awareness stage, sophistication, band names or output sentence, bridge CTA. If the stage is missing, run `build` step 1 to estimate it and label it.
- **Verbatims.** `memory/voc-swipe.md` filtered to the segment and problem, plus the brief. Need at least 5 distinct phrases (one per email). Fewer → use what exists, mark gaps `[NEEDS VOC: phrase for <idea>]`, and suggest `research`.
- **Offer, proof, voice, objections.** `context/offers.md`, `context/evidence.md`, `context/voice.md`, `memory/objections.md`.
- **Tools.** Email connector may hold drafts (`create_draft`), but nurture copy goes to file by default; Docs connector optional for the landing page. No send, schedule, publish or post call without a fresh yes.

## Procedure

1. **Rule of One** (Great Leads, `copywriting` book 06). Before writing, fill five lines: Idea / Emotion / Story / Benefit / Response. The Response is the single CTA ("Take the 12-question scorecard"). If a line has two entries, cut one.

2. **Choose the lead type by awareness** (Six Lead Types, `copywriting` book 06):

   | Stage | Lead type for the hero | Example shape |
   |---|---|---|
   | Unaware | Story or Proclamation | "At 6:10 pm the phone rang twice and stopped." / "Your best month is hiding in your call log." |
   | Problem-aware | Big Secret or Problem-Solution | "The after-hours gap most clinics never measure" |
   | Solution-aware | Promise or Problem-Solution | "See exactly where your intake leaks, in 4 minutes" |
   | Product-aware | Promise | "Check any vendor against the 9 tests that matter" |
   | Most-aware | Offer | "Free 20-minute intake audit, 5 slots this month" (scarcity only if true) |

   At sophistication 3–4, name the magnet's mechanism in the subhead; at 5, open with identification ("For owners who've stopped trusting automation pitches").

3. **Headlines** (Eight Headline Types and Four Functions of a Headline, `copywriting` book 02). Draft one per type: Direct, Indirect, News, How-To, Question, Command, Reason-Why, Testimonial (Testimonial only from `evidence.md`, else skip). Score each 0–4 on attention, audience selection, complete message, pull into body. Discard any under 3. Ship the top scorer that fits the step 2 lead type, plus one alternate for an A/B test. Show the scoring table.

4. **Landing page.** Motivating Sequence skeleton (`copywriting` book 02), ≤ 450 words, one CTA repeated (same verb, same button text) at most three times, no navigation links, no second offer.
   - Hero: headline + subhead (≤ 20 words) + CTA button + one tangible preview line ("12 questions · 4 minutes · instant score").
   - Need: 2–3 short paragraphs or bullets built from verbatims (use at least two, unattributed on the page, sourced in the notes).
   - What you get: 3–5 bullets, each a concrete outcome of the magnet, not a feature (So What? test, `copywriting` book 02).
   - Result preview (Make the Invisible Tangible, `sales-psychology` book 07): describe or mock the result screen (score, band name, top 3 fixes).
   - Proof: from `evidence.md` only, else `[NEEDS PROOF: testimonial from a <segment> owner]` or omit the block.
   - Risk reducers: no call required, time to complete, what you will email.
   - Form: minimum fields (first name, work email; one qualifying field only if `review` needs it for segmentation).

5. **Thank-you page** (≤ 120 words): confirm; deliver (link, or "your result is on screen and in your inbox"); set expectations (5 emails over 10 days, one line on what they cover); one next step as a soft Advance (SPIN · Advance vs Continuation, `sales-psychology` book 01): "Reply with your score and the question you scored 0 on; I'll send back the fix I'd start with." A booking link appears only for the highest-need band.

6. **5-email nurture.** Each email: body ≤ 150 words; one idea; exactly one VOC phrase quoted verbatim (record its source in the draft's notes line, not in the email); voice from `voice.md`; ends in either a SPIN Implication question (a consequence of the problem, answerable by reply) or a soft Advance (a specific buyer action).

   | # | Day | Idea | Ends with |
   |---|---|---|---|
   | 1 | 0 | Deliver; what their result means; the core sentence | Implication question about their lowest-scoring area |
   | 2 | 2 | The struggling moment (`offer-creation` book 07) as a short scenario, labelled illustrative unless from `evidence.md` | Implication question |
   | 3 | 4 | The mechanism: why the problem happens, named (Schwartz mechanization when sophistication ≥ 3) | Implication question |
   | 4 | 7 | The anxiety (Four Forces · Anxiety, `offer-creation` book 07): the top objection from the brief or `memory/objections.md`, and what reduces it | Soft Advance (reply a keyword for a free item) |
   | 5 | 10 | The bridge: what fixing it involves; what you do vs what they do | Soft Advance with a concrete ask: a 15-minute result review, two time options or a link |

   Subject lines ≤ 6 words; no curiosity the email doesn't pay off. No discount, no fake deadline.

7. **LinkedIn launch post** (STEPPS · Social Currency and Practical Value, `marketing-psychology` book 06). ≤ 220 words. First two lines ≤ 200 characters and work alone (they are all that shows before "see more"); use the step 2 lead type. Body: the problem in their words, what the magnet reveals, one sample question or band. CTA: comment a keyword to receive it (the user sends links themselves; this skill never DMs). At most 3 hashtags. No unsourced numbers.

8. **3 comment-bait variants** (alternate posts or first comments, each ≤ 80 words): (A) keyword CTA ("Comment SCORE"); (B) a one-word-answer question lifted from a scorecard item ("After 5 pm your calls go to: voicemail / mobile / service / nobody?"); (C) social currency: share the band labels, ask "Which band are you?" Each must be honest about what the commenter receives.

9. **Evidence and file pass.** Run the evidence rule over every asset; turn unsourced numbers into `[NEEDS PROOF: …]`. Write everything to `assets/magnets/<magnet-slug>/funnel.md`. If the user asks for email-tool drafts, create drafts only.

## Output
`assets/magnets/<magnet-slug>/funnel.md`:

```markdown
# Funnel: <magnet name> · DRAFT · YYYY-MM-DD
Segment: … · Awareness: … · Sophistication: … · Lead type: …
Rule of One: Idea … / Emotion … / Story … / Benefit … / Response …

## Headline scoring
| Type | Headline | Attn | Select | Message | Pull | Total |

## Landing page
### Hero
### Need
### What you get
### Result preview
### Proof
### Risk reducers
### Form

## Thank-you page

## Nurture
### Email 1 · Day 0 · Subject: …
<body>
Notes: idea … · VOC: "…" — <source> · ends with: implication question | soft Advance
(repeat for emails 2–5)

## LinkedIn launch post
## Comment-bait variants
### A · keyword
### B · one-word answer
### C · social currency

## Evidence
Sourced: … · [NEEDS PROOF]: …
```

## Write-back
- `memory/magnet-learnings.md`, under the magnet's registry entry: `- YYYY-MM-DD · funnel drafted · lead type: <type> · headline A: "<…>" · headline B: "<…>" · CTA: "<…>"`
- `memory/voc-swipe.md`: nothing, unless the user supplies new phrases (append them in the research format).
- `log.md`: `YYYY-MM-DD · lead-magnets · funnel · <magnet-slug> drafts · assets/magnets/<magnet-slug>/funnel.md`

## Quality gate
- [ ] Hero lead type matches the awareness table.
- [ ] Headline table present; shipped headline scores ≥ 3.
- [ ] Landing page ≤ 450 words, one CTA, no navigation, no second offer.
- [ ] Thank-you page ends with one soft Advance.
- [ ] 5 emails, each ≤ 150 words, one idea, exactly one verbatim VOC phrase with its source in notes, ending in an Implication question or soft Advance.
- [ ] LinkedIn post ≤ 220 words, hook ≤ 200 characters; 3 variants present.
- [ ] Evidence rule: no number, testimonial or client reference without an `evidence.md` line or fetched public URL; else `[NEEDS PROOF: …]`.
- [ ] Everything marked DRAFT; nothing sent, scheduled, published or posted.

## Failure modes
- **Direct lead to unaware traffic.** "Get our missed-call calculator" to owners who don't think they miss calls is noise.
- **Two CTAs.** "Take the quiz or book a call" weakens both.
- **Emails that teach the fix.** Email 3 explains why it happens, not the build steps.
- **Paraphrased VOC.** If it isn't in the swipe file verbatim, it isn't a quote.
- **Continuation endings.** "Let me know if you have questions" is a Continuation; end with a consequence question or a specific action.
