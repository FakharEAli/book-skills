# Mode: audit

## Purpose
Check the workspace's health in one pass and return a score out of 100 plus the three fixes worth the most. Audit is read-only apart from one log line; it tells the user what to fix and which command fixes it.

## Inputs
- Resolved workspace (SKILL.md §1). None found → say so in one line and offer `/book-skills:setup init`. Stop.
- All of `context/*.md`, `memory/*.md`, `deals/*.md` (frontmatter only), `log.md`.
- Today's date (`date +%F`).
- **Connector category:** none. Shell for counting; fallback: Read each file and count by hand.

## Procedure

1. **Define "empty".** A file or section is empty if, after removing HTML comments (`<!-- … -->`), lines containing `example: delete`, headings, table header/separator rows and blank lines, fewer than 2 lines remain. Template examples never count as content.

2. **Context completeness (40 points).** Score each file: full points if every section is non-empty, half if at least one section is non-empty, 0 if empty or missing.
   | File | Points | Why it matters |
   |---|---|---|
   | evidence.md | 10 | Without it every outbound claim becomes `[NEEDS PROOF]` |
   | icp.md | 8 | Prospecting and scoring read it |
   | offers.md | 8 | Proposals, magnets and outreach read it |
   | pricing.md | 5 | Negotiation and proposals |
   | voice.md | 5 | Every draft |
   | competitors.md | 4 | Objections and positioning |
   Positioning gaps matter most where the Five Components of Positioning (Dunford, `offer-creation` book 03) break: no alternatives, no best-fit customer, no value proof.

3. **Evidence hygiene (20 points).** Parse the table rows of `evidence.md` (exclude example rows).
   - Valid row = has a non-empty source and a date.
   - Score = 20 × valid rows / all rows (no rows → 0).
   - **Critical flags** (each one is automatically a top-3 fix): a row with `verified: Y` but no source or no date; a row with `public-safe: Y` where the source is "memory" or blank; a verified claim with vague wording ("loads", "a lot", "huge"). Specific claims beat general ones (Hopkins, `copywriting` book 04).
   - Count `verified: Y` rows. Zero verified rows → flag "no usable proof".

4. **Pipeline hygiene (20 points).** For each `deals/*.md`, read the frontmatter between the first two `---` lines. Open = stage not `won` or `lost`.
   ```bash
   for f in "$W"/deals/*.md; do [ -e "$f" ] || continue
     awk 'NR==1&&/^---/{p=1;next} p&&/^---/{exit} p' "$f" | grep -E '^(company|stage|value|next_step|next_step_date|last_touch):' | sed "s|^|$(basename "$f" .md) |"
   done
   ```
   - Healthy open deal = `next_step` non-empty and `next_step_date` ≥ today.
   - Overdue = `next_step_date` < today; record days overdue.
   - Stale touch = `last_touch` more than 21 days ago.
   - Score = 20 × healthy open / all open. No open deals → 20 and note "no pipeline yet".

5. **Memory growth (15 points).** 3 points for each of the 5 memory files that has at least one real dated entry (a line or heading containing `YYYY-MM-DD` that is not an example). List the files never written to.

6. **Review cadence (5 points).** Find the latest `## YYYY-MM-DD` heading in `memory/outreach-learnings.md` (ignore example lines). ≤14 days → 5; 15–30 → 3; >30 or none → 0. Also note whether `## Current best angles` is empty.

7. **Log activity (no points, context only).** Date of the last line in `log.md`; number of lines in the last 30 days.

8. **Rank the fixes.** Build a candidate list, then pick the top 3 by this order (higher beats lower; ties broken by points recoverable):
   1. Critical evidence flags (risk of a false claim going out).
   2. Zero verified evidence rows.
   3. Overdue deals (most overdue first; group into one fix if several).
   4. icp.md or offers.md empty/partial.
   5. Open deals with no next step.
   6. Review cadence 0 while outreach is happening (`log.md` shows outreach in the last 30 days).
   7. Memory files never written to.
   8. pricing, voice, competitors gaps.
   Each fix names the exact command: e.g. `/book-skills:setup interview evidence`, `/book-skills:deals rescue <slug>`, `/book-skills:setup interview icp`. Prefer the setup command when the fix is a context gap; point to the owning workflow skill for deals and outreach.

9. **Score band.** 85–100 healthy · 60–84 usable with gaps · 30–59 thin, outputs will be generic · <30 not set up.

## Output

```markdown
**Workspace health: <score>/100 · <band>**  (`<workspace path>`, checked YYYY-MM-DD)

| Area | Score | Finding |
|---|---|---|
| Context | <x>/40 | <empty or partial files> |
| Evidence | <x>/20 | <V> verified · <U> unverified · <k> rows missing source |
| Pipeline | <x>/20 | <open> open · <o> overdue · <n> no next step |
| Memory | <x>/15 | never written: <files> |
| Review cadence | <x>/5 | last outreach review: <date or never> (<d> days) |

**Top 3 fixes**
1. <fix> — <why, one line> → `<command>`
2. <fix> — <why> → `<command>`
3. <fix> — <why> → `<command>`

<Critical: <evidence flag details>, only if any>
Last activity in log.md: <date> (<n> entries in 30 days)
```

## Write-back
- `log.md`: `- YYYY-MM-DD · setup · audit · score <s>/100; top fix: <fix 1>`.
- No other file is changed. If the user asks to apply a fix, switch to the named mode or skill; do not edit files from within audit.

## Quality gate
- [ ] Template example lines and rows were excluded from every count.
- [ ] Every number in the table was computed from the files, not estimated.
- [ ] Every critical evidence flag appears in the top 3 (evidence rule: a `verified: Y` row without a source is a false-proof risk).
- [ ] Each of the 3 fixes names one concrete command.
- [ ] No file other than `log.md` was modified.

## Failure modes
- **Counting templates as content.** Makes a brand-new workspace look healthy. Apply step 1 strictly.
- **Fuzzy frontmatter.** Quoted values, trailing `# comments` and missing fields are common. Strip quotes and comments; treat a missing `next_step_date` as "no next step".
- **Date confusion.** Compare dates as `YYYY-MM-DD` strings only after validating the format; skip and flag malformed dates.
- **Ten fixes instead of three.** The user acts on one. List three, ranked.
- **Editing during audit.** Audit reports; the user chooses what to fix.
