# Mode: init

## Purpose
Create the private workspace from the shipped templates, without ever touching an existing one, then hand straight into the interview (or bootstrap) so the user leaves with real context, not empty files.

## Inputs
- **Location choice.** Default `~/.book-skills/`. Alternatives: per-project `./.book-skills/` (one workspace per client project or per business), or `$BOOK_SKILLS_HOME` if the user has set it.
- **Existing workspace check.** The resolver in SKILL.md §1, plus a direct check of the chosen target path.
- **Templates.** `${CLAUDE_SKILL_DIR}/templates/context/*.md`, `${CLAUDE_SKILL_DIR}/templates/memory/*.md`, `${CLAUDE_SKILL_DIR}/templates/log.md`.
- **Connector category:** none. Shell is needed to copy files. Fallback (no shell, e.g. Cowork): ask the user to select or attach a folder, then Read each template and Write it into that folder one by one.
- **Anything the user already said** in the opening message (business, clients, claims). Keep it for the interview; do not write it anywhere yet.

## Procedure

1. **Resolve.** Run the resolver from SKILL.md §1. If it prints a path, a workspace exists: go to step 2. If it prints nothing, go to step 3.

2. **Existing workspace: never overwrite.**
   - Tell the user where it is and list what it contains (`ls -R <workspace> | head -60`).
   - Do not copy, re-create or reset anything. Offer exactly two choices with AskUserQuestion: "Check its health (audit)" or "Fill gaps (interview)".
   - If some template files are missing (e.g. an older workspace without `memory/magnet-learnings.md`), offer to add only the missing ones, using the no-clobber copy in step 5. Show the list of files that would be added before doing it.
   - Then READ `audit.md` or `interview.md` and follow it. Stop this mode.

3. **Ask the location** (one AskUserQuestion call, one question):
   - "Where should your workspace live?"
     - a) `~/.book-skills/` (recommended: one workspace for your business, used from any project)
     - b) `./.book-skills/` in this project (separate workspace per project or brand)
     - c) A custom folder (uses `$BOOK_SKILLS_HOME`; you add `export BOOK_SKILLS_HOME=<path>` to your shell profile yourself)
   - For c), do not edit the user's shell profile. Print the export line for them to add.

4. **Per-project safety.** If b) and the current directory is a git repository (`git rev-parse --is-inside-work-tree` succeeds):
   - Run `git check-ignore -q .book-skills/`. If not ignored, tell the user the workspace holds private client data and ask to append `.book-skills/` to `.gitignore`. Append only on yes. If they decline, warn once that it will be committed on `git add .`, then continue.

5. **Create the tree** (no-clobber; `W` is the chosen path, `T` the templates dir):
   ```bash
   W="$HOME/.book-skills"   # or ./.book-skills or the custom path
   T="${CLAUDE_SKILL_DIR}/templates"
   mkdir -p "$W/context" "$W/memory" "$W/deals" "$W/prospects" \
            "$W/assets/magnets" "$W/assets/sequences" "$W/assets/proposals" "$W/assets/prep" \
            "$W/assets/offers" "$W/assets/reviews" "$W/assets/follow-ups"
   for f in "$T"/context/*.md; do [ -e "$W/context/$(basename "$f")" ] || cp "$f" "$W/context/"; done
   for f in "$T"/memory/*.md;  do [ -e "$W/memory/$(basename "$f")" ]  || cp "$f" "$W/memory/";  done
   [ -e "$W/log.md" ] || cp "$T/log.md" "$W/log.md"
   ls -R "$W"
   ```
   Expected result: 6 files in `context/` (icp, offers, pricing, evidence, voice, competitors), 6 in `memory/` (voc-swipe, objections, win-loss, outreach-learnings, magnet-learnings, suppression), `log.md`, and empty `deals/`, `prospects/`, `assets/{magnets,sequences,proposals,prep,offers,reviews,follow-ups}/`. If the count differs, report which file is missing and copy it individually; never continue with a partial tree silently.

6. **Log the creation.** Append to `log.md`:
   `- YYYY-MM-DD · setup · init · workspace created at <path> (6 context, 5 memory templates)`

7. **Choose how to fill it** (one AskUserQuestion call, one question):
   - "How do you want to fill it in? About 15 minutes either way."
     - a) Interview me now (6 short rounds)
     - b) Pre-fill from my website / LinkedIn / recent calls first, then confirm with a shorter interview
     - c) Later (stop here)
   - a) → READ `interview.md` and start at round 1, carrying forward anything from the opening message as pre-filled answers to confirm.
   - b) → READ `bootstrap.md`.
   - c) → show the Output block and end with `/book-skills:setup interview`.

## Output

Show this after step 5 (and again at the end if the user stops):

```markdown
**Workspace created:** `<path>`

context/   icp · offers · pricing · evidence · voice · competitors   (templates, not filled)
memory/    voc-swipe · objections · win-loss · outreach-learnings · magnet-learnings · suppression
deals/ · prospects/ · assets/{magnets,sequences,proposals,prep}/ · log.md

Every file has a synthetic example marked `<!-- example: delete -->`. Those
examples are never used as proof; workflows ignore them.

**Next:** <interview round 1 | bootstrap | `/book-skills:setup interview`>
```

## Write-back
- `log.md`: one line on creation (step 6). The interview and bootstrap modes add their own lines.
- `.gitignore` of the current repo: `.book-skills/` appended only with the user's yes (step 4).
- No other files are edited in this mode.

## Quality gate
Before showing the Output:
- [ ] No existing file was overwritten (every copy used the `[ -e ] ||` guard, or the Write fallback targeted only non-existent paths).
- [ ] The tree has all 6 context files, all 5 memory files, `log.md` and the 7 empty folders.
- [ ] A per-project workspace inside a git repo is git-ignored, or the user explicitly declined.
- [ ] Nothing from the opening message has been written as evidence yet; claims wait for round 5 of the interview (evidence rule).
- [ ] The user's shell profile was not edited.

## Failure modes
- **Re-initialising over real data.** Caused by skipping the resolver or using `cp -f`. Always resolve first; always use the no-clobber guard. If the user wants a fresh start, tell them to rename the old folder themselves (`mv ~/.book-skills ~/.book-skills.bak`); never delete it.
- **Wrong location picked silently.** A `./.book-skills/` in the current project shadows `~/.book-skills/` for that project. If both exist, say which one is active and why (resolver order).
- **Committing client data.** Per-project workspaces inside a repo leak on `git add .`. Step 4 exists for this.
- **Treating template examples as real.** Examples are synthetic and marked. Never quote them in outputs and never count them in audit.
- **Stopping after the copy.** Empty templates help nobody. Always offer the interview or bootstrap in the same turn.
- **No shell available.** Do not fail. Ask for a folder and write files individually; confirm the final list.
