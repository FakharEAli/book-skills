---
name: setup
description: "Creates and maintains the private Book Skills workspace: builds the folder from templates, interviews the user to fill ICP, offers, pricing, evidence and voice, optionally pre-fills from their website, LinkedIn and recent calls, and audits workspace health. Use when the user says \"set me up\", \"set up book skills\", \"run setup\", \"create my workspace\", \"fill in my ICP and offers\", \"add proof to my evidence file\", \"pre-fill from my website / my calls\", \"check my workspace\" or \"what's missing in my setup\". Modes: init, interview, bootstrap, audit"
argument-hint: "<init|interview|bootstrap|audit> [round or source]"
---

# Setup: workspace creation, interview, bootstrap, audit

Every other Book Skills workflow reads the workspace this skill builds. Its job is to get true, sourced, specific context into `context/` so that later outbound work never has to guess or invent proof.

## 1. Setup step

Read `${CLAUDE_SKILL_DIR}/../../shared/workspace.md`. Resolve the workspace exactly as its §1 says (first that exists: `./.book-skills/`, `$BOOK_SKILLS_HOME`, `~/.book-skills/`):

```bash
for d in ./.book-skills "${BOOK_SKILLS_HOME:-}" "$HOME/.book-skills"; do [ -n "$d" ] && [ -d "$d" ] && echo "$d" && break; done
```

- No workspace found: that is expected for this skill. Route to `init` unless the user asked only for `audit` (then report "no workspace yet" and offer `init`).
- Workspace found: load whichever `context/*.md` files the chosen mode lists under Inputs. Never overwrite a file that already has content.

If the shared file cannot be read, apply these rules inline: (2) **Evidence rule**: any outcome, number, client name, testimonial or "we've done X" may only be used if it traces to a line in `context/evidence.md`; otherwise write `[NEEDS PROOF: <what>]`; never invent proof, never round up. (3) **Draft, never send**: nothing is sent, posted or published without the user's explicit yes in chat. (4) **Write back**: after real work, append dated (`YYYY-MM-DD`), sourced entries to the right workspace file and one line to `log.md`.

## 2. Mode router

Parse the first word of `$ARGUMENTS` as the mode. If missing or not a mode, infer from the request. If still ambiguous, ask one question: "Create a new workspace, fill in your details, pre-fill from your website/calls, or check what's there?"

| mode | when | file |
|---|---|---|
| `init` (default) | No workspace exists, or the user says "set me up" / "create my workspace" | `${CLAUDE_SKILL_DIR}/modes/init.md` |
| `interview` | Workspace exists and context files are empty or partial; "fill in my ICP", "update my offers", "add proof" | `${CLAUDE_SKILL_DIR}/modes/interview.md` |
| `bootstrap` | User wants pre-fill from website, LinkedIn or recorded calls before (or instead of starting) the interview | `${CLAUDE_SKILL_DIR}/modes/bootstrap.md` |
| `audit` | "check my workspace", "what's missing", "is my setup healthy", or `init` found an existing workspace | `${CLAUDE_SKILL_DIR}/modes/audit.md` |

Inference rules:
- "Set me up" with a workspace already present → `audit`, then offer `interview` for the gaps. Never re-run `init` over it.
- The user mentions a URL, LinkedIn or "my calls" during setup → `bootstrap` (after `init` if needed).
- A second word naming a round (`interview evidence`, `interview pricing`) → run only that round.
- The opening message already contains claims ("I've helped a few clinics save loads of time") → keep them; they seed the interview, and round 5 rules decide where they are filed.

Then READ the mode file and follow it step by step.

## 3. Shared rules for this skill

**Asking questions.** Use the AskUserQuestion tool when available: at most 4 questions per call, each with 2–4 concrete options (the user can always pick "Other" and type). Group questions by the file they fill. Without the tool, ask in chat as a numbered list of at most 4, with lettered options, and wait for the answer. One round per turn; never dump all rounds at once.

**Ask before reading anything external.** Website, LinkedIn, call recordings, inbox, CRM: name the source and get a yes before the first read. Anything that needs the user's logged-in accounts or cookies gets its own explicit yes.

**Evidence is strict.** This is the most important rule in the skill.
- A claim is `verified: Y` only when it has all four: a specific claim (a number, a named or described client, a concrete result), a date or period, a source artefact the user can produce (invoice, dashboard, signed testimonial, case study URL, email from the client), and the user's confirmation in this session.
- Vague claims ("saved loads of time", "helped a few clinics", "great results") are never converted into numbers. File them under `## Unverified — do not use` with what is needed to verify them.
- Anything Claude extracted (website, LinkedIn, transcripts) is `verified: N` until the user confirms it and names the source.
- `public-safe: Y` only when the user says the client agreed to be named or the result is already public. Default `N`.
- Never round up, never extrapolate ("3 clinics" does not become "dozens"), never merge two results into one.

**Write after every round.** Write or update the file the round fills before asking the next round, then show a 3–6 line summary: what was written, what is still a gap, what is unverified. The user can stop at any time and keep everything already written.

**Never overwrite.** Create missing files from templates; edit existing files only by filling empty sections or by appending. If a section already has content that conflicts with a new answer, show both and ask which to keep.

**Templates.** Live in `${CLAUDE_SKILL_DIR}/templates/`. Each section has a one-line `<!-- instruction -->` comment and a synthetic example marked `<!-- example: delete -->`. When writing real content into a section, remove that section's example line; keep the instruction comment.

**Write-back for every mode.** Append one line to `<workspace>/log.md`:
`- YYYY-MM-DD · setup · <mode> · <one line: what changed, which files>`

**Output conventions.** Paths shown relative to the workspace (`context/icp.md`). No motivational copy. End each mode with the single best next command, e.g. `/book-skills:setup interview evidence`.

**Privacy.** Workspace content never goes into URLs, search queries that include client names, or tools the user didn't choose. If the workspace is per-project (`./.book-skills/`) inside a git repo, make sure it is git-ignored before writing (see `init`).

## 4. Method library

Load only when needed (to phrase a sharper question, or when the user asks why a question matters). Do not re-teach the frameworks in the interview; use them to choose what to ask.

| Framework | Used for | File |
|---|---|---|
| Five (plus one) Components of Positioning (Dunford) | Rounds 1 and 3: competitive alternatives, unique attributes, value, best-fit customers | `${CLAUDE_SKILL_DIR}/../offer-creation/books/03-obviously-awesome.md` |
| Customer Profile: jobs, pains, gains (Osterwalder, Pigneur) | Round 2 ICP and segment pains | `${CLAUDE_SKILL_DIR}/../offer-creation/books/02-value-proposition-design.md` |
| Four Forces of Progress; timeline interview (Moesta) | Round 2 triggers; bootstrap call mining | `${CLAUDE_SKILL_DIR}/../offer-creation/books/07-demand-side-sales-101.md` |
| Hiring and firing; Job Spec (Christensen) | Round 3 alternatives ("what do they fire to hire you") | `${CLAUDE_SKILL_DIR}/../offer-creation/books/08-competing-against-luck.md` |
| Value Equation; guarantees (Hormozi) | Round 3 outcome, timeline, guarantee | `${CLAUDE_SKILL_DIR}/../offer-creation/books/01-100m-offers.md` |
| WTP conversation; Leaders, Fillers, Killers (Ramanujam, Tacke) | Round 4 pricing, floor, what to trade | `${CLAUDE_SKILL_DIR}/../offer-creation/books/04-monetizing-innovation.md` |
| Specific claims beat general ones (Hopkins) | Round 5: why "saved loads of time" is useless as proof | `${CLAUDE_SKILL_DIR}/../copywriting/books/04-scientific-advertising.md` |
| Hard vs soft messengers (Martin, Marks) | Round 5: which proof types carry weight with owners | `${CLAUDE_SKILL_DIR}/../marketing-psychology/books/09-messengers.md` |
| Scout mindset (Galef) | Round 5: separating what is known from what is hoped | `${CLAUDE_SKILL_DIR}/../human-psychology/books/10-the-scout-mindset.md` |
| Voice-of-Customer research; message mining (Wiebe) | Bootstrap VOC extraction; voc-swipe categories | `${CLAUDE_SKILL_DIR}/../copywriting/books/08-where-stellar-messages-come-from.md` |
