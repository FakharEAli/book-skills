# Mode: rehearse `<company | persona>`

## Purpose
Let the user practise a sales conversation against a realistic, in-character buyer built from real deal data, then get a scored debrief and drills. The persona resists the way real owners do: short answers, deflection of weak questions, hidden concerns that only surface when the seller earns them.

## Inputs
- Company argument: `deals/<slug>.md` (Gap, Timeline verbatims, stall_type, decision_maker, champion), the latest prep sheet in `assets/prep/` for that slug, `memory/objections.md` (this deal's objections and the segment's most frequent ones), `context/icp.md` (segment traits), `context/competitors.md` (who else they might be talking to).
- Persona argument (no deal, e.g. "skeptical clinic owner"): `context/icp.md` segment row, `memory/objections.md`, `memory/win-loss.md` losses for that segment.
- LinkedIn or web info about the real person: only what the user pastes or a URL the user provides, read with the **Web research** connector (fallback: ask the user to paste it). Never look up a private individual on your own initiative; keep any personal data in the workspace.
- Ask the user one question before building: "What call are you rehearsing (first discovery, proposal walkthrough, price conversation) and what Advance do you want out of it?"

## Procedure

1. **Build the persona brief.** Fill every field below. Tag each line `[sourced: <file or paste>]` or `[inferred]`. At least half of the objections and hidden concerns must be sourced when a deal file exists; if not, say the persona is mostly inferred.
   - **Role, company, situation:** title, size, what is happening now (from Gap current state and Timeline).
   - **Priorities:** top 3 this quarter, in their words where available.
   - **Personality:** one dominant style from evidence in the Timeline (e.g. "terse, numbers-first", "friendly but evasive", "skeptical, burned before") plus speaking habits (short sentences, interrupts, asks about price early).
   - **Past vendor experiences:** what went wrong before (from verbatims or `objections.md`).
   - **Objections to raise:** 3–5 real ones, each with the natural moment it surfaces (on hearing price, on hearing timeline, when asked for a next step).
   - **Hidden concerns (not stated upfront):** 1–3, e.g. fear of staff pushback, a partner who must agree, cash-flow timing, embarrassment about a failed past project. Each with the unlock condition: what the seller must do to earn it (a specific implication question, an accurate label, acknowledging the past failure).
   - **Budget reality:** what they could really spend, and how they will react to the user's actual price from `pricing.md`.
   - **What would make them say yes:** concrete conditions (a pilot, seeing a sample output, a reference, a date that fits their season).
   - **Call type and the user's target Advance.**

2. **Dispatch the agent.** Use the Agent tool with `subagent_type: "book-skills:prospect-roleplay"`. The prompt contains: the full persona brief, the call type, the user's target Advance, and "Stay in character. Wait for the seller's first line. On 'end roleplay', score per your rubric." Keep the returned agent ID.

3. **Tell the user how to run it**, in 4 lines:
   - "You talk as yourself; I'll pass your words to <Persona name>, who answers in character."
   - "Open the call the way you would for real."
   - "No coaching until the end. Say **end roleplay** to stop and get scored."
   - "Say **pause** if you need to step out without ending."

4. **Relay turns.** For each user message, send it verbatim to the agent with SendMessage (agent ID from step 2) and show the agent's reply verbatim, prefixed `**<Persona name>:**`. Add nothing: no hints, no commentary, no mid-call scoring. If the user types "pause", stop relaying until they say "resume". Forward "end roleplay" verbatim and show the scorecard.

5. **If dispatch or SendMessage is unavailable,** read `${CLAUDE_SKILL_DIR}/../../agents/prospect-roleplay.md` and play the persona inline under the same rules: stay in character, never coach, score only on "end roleplay", using the agent's rubric and output format. Say once at the start that you are running it inline.

6. **After scoring,** extract lessons: for each objection raised, did the seller's response work (persona softened, revealed more, or agreed to a step)? Use the best and worst seller lines quoted in the scorecard. Frameworks behind the rubric: SPIN implication questions and Advances (Rackham, `sales-psychology` book 01), labels and calibrated questions (Voss, book 05), gap depth (Keenan, book 04).

7. **Offer one rerun** targeting the lowest-scoring rubric line, with the same persona and one hidden concern made harder to unlock, or move to `negotiate` if price was the sticking point.

## Output
Before the roleplay, show the brief (so the user can correct it) and the run instructions:

```markdown
## Persona brief · <Persona name>, <role>, <company> · <call type>
Target Advance: <user's goal>
Source mix: <n> sourced · <n> inferred

| Field | Content | Source |
|---|---|---|
| Situation | … | [sourced: deals/<slug>.md] |
| Priorities | 1… 2… 3… | … |
| Personality | … | … |
| Past vendors | … | … |
| Objections (moment) | 1. "…" (on price) 2. … | … |
| Hidden concerns (unlock) | 1. … (unlocks if seller …) | … |
| Budget reality | … | … |
| Yes conditions | … | … |

**How to run it:** <4 lines from step 3>
```

After "end roleplay": the agent's scorecard verbatim, then:

```markdown
### Lessons saved
- <objection> → <what worked / failed> → appended to memory/objections.md
### Next rep
<one drill to do now, or "rerun with hidden concern #2 harder to unlock">
```

## Write-back
- `memory/objections.md`, one entry per objection the persona raised:
  ```markdown
  ### <YYYY-MM-DD> · "<objection as the persona said it>" · source: roleplay (<deal slug | persona>)
  - Real cause (per brief): <hidden concern or reason>
  - Worked: "<seller line>" (score <n>/100)
  - Failed: "<seller line>"
  - Drill: <one line>
  ```
  These are practice data. Never append roleplay lines to `memory/voc-swipe.md` and never quote them as buyer evidence.
- `deals/<slug>.md` (company mode only) Timeline: `### <date> · Rehearsal · pitch rehearse` with `- Score: <n>/100 · Weakest: <rubric line> · Drill: <…>`. Do not change `last_touch` (no buyer contact happened).
- `log.md`: `<date> · pitch · rehearse · <persona> <score>/100 · <slug or persona>`.

## Quality gate
- [ ] Every brief field filled; each line tagged sourced or inferred.
- [ ] Hidden concerns have explicit unlock conditions.
- [ ] The user's real price from `pricing.md` is in the brief so price reactions are realistic.
- [ ] No coaching shown between the first seller line and "end roleplay".
- [ ] Scorecard includes 0–100 score, verbatim best and worst seller lines, 3 drills.
- [ ] Lessons appended with `source: roleplay`; nothing written to voc-swipe.

## Failure modes
- **Pushover persona** that agrees after two questions: the brief must specify personality and objections with moments; reject a brief with no hidden concern.
- **Persona built from imagination** when deal data exists: re-read the Timeline verbatims and rebuild.
- **Breaking character to help:** the relay adds nothing; coaching waits for the scorecard.
- **Personal data leakage:** use only what the user supplied; do not search for the person.
- **Practice treated as evidence:** roleplay quotes never enter proposals or `voc-swipe.md`.
