# Mode: bootstrap

## Purpose
Pre-fill the workspace from sources the user approves (their website, their LinkedIn profile, their last few recorded calls) so the interview only has to confirm, correct and fill gaps. Bootstrap drafts context; it never creates verified evidence.

## Inputs
- Resolved workspace (SKILL.md §1). If none exists, READ `init.md` first, then return here.
- **Source choice**, always asked before any read (step 1).
- **Web research** category (`CONNECTORS.md`): the `web-research` skill, `exa`, `scrapling`, `WebFetch`, `WebSearch`. Fallback: ask the user to paste the page text.
- **Call recorder** category: tools whose names contain `fathom`, `gong`, `fireflies`, `granola`, `zoom` together with `transcript` / `meeting`. Fallback: ask the user to paste 1–3 transcripts or call notes.
- **Agent:** `book-skills:voc-miner` (buyer-speech VOC from saved transcript files). Fallback when dispatch is unavailable: run its method inline (step 5).

## Procedure

1. **Ask which sources** (one AskUserQuestion call, `multiSelect`):
   - "What should I read to pre-fill your setup? I'll only read what you tick."
     - a) My website (give the URL)
     - b) My LinkedIn profile (give the URL)
     - c) My last few recorded sales calls (from your call recorder)
     - d) Something I'll paste (proposal, case study, pitch deck text)
   - Then ask only the details needed: URLs; for calls, how many (options 3 / 5 / 10, default 5) and whether to include only sales/discovery calls.
   - No ticks → READ `interview.md` and start round 1.

2. **Website** (if approved).
   - Use the web-research route, cheapest first. Read at most 8 pages: home, services/offer pages, about, case studies/results, testimonials, pricing, contact (for location/market). Do not crawl blog archives.
   - Extract into a scratch list, each item tagged `(from: <URL>, read YYYY-MM-DD)`:
     - one-line description and services → `offers.md`
     - who they say they serve, industries named → `icp.md` segments (as "stated on site")
     - offers, timelines, guarantees, prices if published → `offers.md`, `pricing.md`
     - **every** result, client logo, testimonial, number → evidence candidates (step 6)
     - tone samples: 2 short paragraphs verbatim → `voice.md` `## Samples` (source URL)
   - Positioning reading (Dunford, Five Components of Positioning, `offer-creation` book 03): note what alternatives the site positions against; draft them for `competitors.md`.

3. **LinkedIn** (if approved).
   - LinkedIn usually blocks unauthenticated fetches. Try one public fetch of the profile URL. If it fails or needs login, do not use any tool that relies on the user's logged-in browser or cookies unless the user gives a separate explicit yes. Default fallback: ask them to paste the About section, headline and the last 3 posts they liked writing.
   - Extract: headline positioning, stated audience, claims (to evidence candidates), and writing samples (to `voice.md`).

4. **Calls** (if approved).
   - Detect the call-recorder tool. List the last N meetings (titles, dates, attendees' companies only). Show the list and ask the user to untick internal or personal calls before pulling any transcript.
   - Pull transcripts for the approved calls only. Keep prospect personal data inside the workspace (privacy rule 7).

5. **Mine the calls.**
   - Save each approved transcript inside the workspace so quotes can be verified: `assets/prep/calls/YYYY-MM-DD-<call-slug>.md`, starting with a header (`source_type: call transcript`, `url: <recorder link or id>`, `date: YYYY-MM-DD`, `retrieved: YYYY-MM-DD`), then `---`, then the verbatim transcript.
   - Dispatch with the Agent tool, `subagent_type: "book-skills:voc-miner"`. Agents don't see the conversation, so the prompt must contain: **Segment** (one line from what is known so far, or "infer from material"); **Material** (the absolute paths of the saved transcript files); the instruction "Mine buyer speech only (the prospect, not the seller). Return your standard output format."
   - Map its output into `memory/voc-swipe.md`: Pains → pains · Desired outcomes → desired outcomes · Triggers → triggers · Objections / anxieties → anxieties · Current alternatives → alternatives · Words they use for the problem → their words for the problem. Emotional-language quotes go under pains. Keep only quotes it reports as verified; rewrite each as `- "quote" — <call title>, YYYY-MM-DD, <segment>`.
   - The agent drops seller speech by design, so do a separate inline pass over the same transcripts for (a) **ICP signals**: prospect industry, size, role, trigger event; (b) **seller claims**: every result, client or number the user stated on the call, quoted exactly with call and timestamp. These feed step 6, never voc-swipe.
   - **Inline fallback** (no agent dispatch): do the miner's pass yourself, transcript by transcript: buyer speech only, verbatim, sorted with the Four Forces of Progress (push, pull, anxiety, habit; Moesta, `offer-creation` book 07) and Voice-of-Customer research (Wiebe, `copywriting` book 08). Drop any quote you can't find word for word in the saved file.

6. **Evidence candidates. All `verified: N`.**
   - Every claim from site, LinkedIn, paste or calls goes to `evidence.md` `## Unverified — do not use`, with `source` set to the URL or call, and "to verify" saying what the user must confirm (number, client, date, artefact, permission).
   - A claim being on the user's own website does not make it verified: sites go stale and round up. Only the interview (round 5) can promote it.
   - Never combine fragments into a stronger claim ("cut admin" on one page + "40%" on another is two candidates, not one).

7. **Write the pre-fill.** For each context file, fill only empty sections, tag every pre-filled line `(from: <source>)`, and remove that section's example line. Append voc-miner quotes to `memory/voc-swipe.md` under the matching category. Never overwrite existing content; conflicts go into the summary as "site says X, file says Y".

8. **Show the summary** (Output), then READ `interview.md` and run it in confirm mode: for pre-filled sections ask "Keep / Correct"; ask full questions only for gaps; run round 5 in full for every candidate.

## Output

```markdown
**Bootstrap read:** <website: N pages> · <LinkedIn: fetched / pasted / skipped> · <calls: N of M approved>

| File | Pre-filled sections | Still empty |
|---|---|---|
| icp.md | Segments (site), Triggers (3 calls) | Disqualifiers, Buyer roles |
| offers.md | … | … |
| pricing.md | … | … |
| competitors.md | … | … |
| voice.md | Samples (2, site) | Banned words |
| memory/voc-swipe.md | +<n> quotes (pains <a>, outcomes <b>, triggers <c>, …) | |

**Evidence candidates (unverified, do not use yet):** <n>
1. "<claim as found>" — <source> → need: <what to confirm>
2. …

**Conflicts:** <none | site says X, file says Y>
Next: confirm in the interview (≈<k> questions, only gaps + every evidence candidate).
```

## Write-back
- `context/*.md`: pre-filled lines tagged `(from: <URL | call title YYYY-MM-DD | pasted YYYY-MM-DD>)`.
- `context/evidence.md` `## Unverified — do not use`: `| claim as found | — | <source> | YYYY-MM-DD read | N | N | <to verify> |`.
- `memory/voc-swipe.md`: `- "quote" — <call title or URL>, YYYY-MM-DD, <segment>` under pains / desired outcomes / triggers / anxieties / alternatives / their words for the problem.
- `assets/prep/calls/YYYY-MM-DD-<call-slug>.md`: saved transcripts (header + verbatim text), private to the workspace.
- `log.md`: `- YYYY-MM-DD · setup · bootstrap · read <sources>; pre-filled <files>; <n> quotes; <m> evidence candidates (unverified)`.

## Quality gate
- [ ] Every source was approved before the first read; logged-in/cookie access had its own yes.
- [ ] Evidence rule: zero bootstrap items are `verified: Y`. Every candidate has a source and a "to verify".
- [ ] Every quote in `voc-swipe.md` is verbatim and has source, date and segment.
- [ ] Every pre-filled line carries a `(from: …)` tag; no existing content was overwritten.
- [ ] No prospect personal data left the workspace; no workspace content was placed in a URL or search query.
- [ ] The interview was started (or offered) in confirm mode.

## Failure modes
- **Reading without asking.** Never fetch a URL the user mentioned in passing; ask first.
- **Website puffery becomes proof.** "Trusted by 100+ businesses" on the homepage is a candidate, not evidence.
- **Pulling every call.** Internal stand-ups and personal calls are noise and private. Show the list; let the user untick.
- **Paraphrased "quotes".** VOC is only useful verbatim. Drop anything without exact words.
- **Seller talk mined as buyer voice.** Only prospect speech goes to `voc-swipe.md`; seller claims go to evidence candidates.
- **Skipping the interview.** Pre-fill is a draft; the interview confirms it.
