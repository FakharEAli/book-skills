# Win/loss entry and patterns block

File: `memory/win-loss.md`. Structure, top to bottom:

```markdown
# Win / loss

## Patterns so far (regenerated every 5 entries · last: YYYY-MM-DD · n=<entries>)
<patterns block, see below>

## Entries (append-only, newest last)
### YYYY-MM-DD · <Company> · WON | LOST
...
```

If the file does not exist, create it with the heading, an empty `## Patterns so far` line reading `_Appears after 5 entries._`, and `## Entries`.

## Entry format

```markdown
### YYYY-MM-DD · <Company> · <WON | LOST> · source: <source> · value: <n or "not stated"> <currency> · cycle: <n>d
- Deal file: deals/<slug>.md · First touch: YYYY-MM-DD · Closed: YYYY-MM-DD · Calls: <n> · Advances: <n> · Continuations: <n>
- Category: <won-<reason> | lost-price | lost-no-decision-status-quo | lost-no-decision-valuation | lost-no-decision-information | lost-no-decision-outcome | lost-competitor | lost-diy | lost-timing | lost-fit>
- Stated reason (buyer, verbatim): "<quote>" · <source: call [ts] link | email subject YYYY-MM-DD> · or "not stated"
- Real reason (inferred, confidence <h|m|l>): <one sentence> · Evidence: <ref>, <ref>
- Unanswered "why" (Hoffeld Six Whys): <why change | why now | why this category | why you | why this service | why spend | none>
- Held: <Framework: what worked, ref> · <…>
- Failed: <Framework: what broke, ref> · <…>
- Change → offer: <one concrete change> · outreach: <one> · discovery: <one>
- Reusable: <verbatim worth reusing, or the question that unlocked the deal>
```

`cycle` = closed date − first Timeline date in the deal file, in days. Category is exactly one value.

## Patterns block (written when the entry count is a multiple of 5, or on request)

```markdown
- Record: <W> won / <L> lost · win rate <n>% · (n < 10: directional only)
- Most common loss reason: <category> (<n> of <L>) · Example: <Company YYYY-MM-DD>
- Average cycle: won <n>d · lost <n>d · median all <n>d
- Source that closes best: <source> <won>/<total> (<n>%) · worst: <source> <won>/<total> · sources with < 3 deals: listed, not ranked
- Most frequent unanswered why: <why> (<n>)
- Framework that most often failed: <framework> (<n>) · most often held: <framework> (<n>)
- Average value: won <n> <currency> · lost <n> <currency> (per currency, never converted)
- One change to make now: <the single change that addresses the top loss reason, and the context file it belongs in>
```

Compute only from entries in the file. Replace the old patterns block; never edit entries.
