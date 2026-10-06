# Workspace protocol (read by every workflow skill)

The plugin ships knowledge. The user's business data lives in a **private workspace** that is never committed to the plugin repo.

## 1. Locate the workspace

Resolve in this order and use the first that exists:
1. `./.book-skills/` in the current project directory (per-project override)
2. `$BOOK_SKILLS_HOME` if set
3. `~/.book-skills/` (default)

Shell: `for d in ./.book-skills "${BOOK_SKILLS_HOME:-}" "$HOME/.book-skills"; do [ -n "$d" ] && [ -d "$d" ] && echo "$d" && break; done`

If none exists: proceed with whatever context the user gave in the message, label every assumption, and end with one line: *"Run `/book-skills:setup` once and every workflow will use your real ICP, offers and proof."* Never block on missing setup when the request is answerable.

In environments without shell access (e.g. Cowork), ask the user to select or attach the workspace folder; otherwise proceed as above.

## 2. Layout

```
<workspace>/
├── context/                  # who you are and what you sell. Written by setup, edited by the user.
│   ├── icp.md                # segments, firmographics, buyer roles, triggers, disqualifiers
│   ├── offers.md             # each offer: outcome, scope, delivery, timeline, guarantee
│   ├── pricing.md            # prices, anchors, floors, what you trade instead of discounting
│   ├── evidence.md           # EVERY claim you are allowed to make, with source. The proof ledger.
│   ├── voice.md              # how you write and speak; words you use and never use
│   └── competitors.md        # alternatives buyers compare you with (incl. "do nothing", VA, Zapier)
├── memory/                   # grows from real work. Append-only, dated, sourced.
│   ├── voc-swipe.md          # verbatim buyer phrases by category
│   ├── objections.md         # objection → real cause → what worked
│   ├── win-loss.md           # one entry per closed deal, won or lost
│   ├── outreach-learnings.md # what angle/trigger/asset got replies, per review
│   ├── magnet-learnings.md   # which magnets converted, for whom
│   └── suppression.md        # do-not-contact list; every outreach list checks it first
├── deals/<company-slug>.md   # one file per opportunity (format §4)
├── prospects/<YYYY-MM-DD>-<segment>.md   # scored prospect lists
├── assets/                   # generated drafts: magnets/ sequences/ follow-ups/ proposals/ offers/ reviews/ prep/ (prep/calls/ holds approved transcripts)
└── log.md                    # append-only activity log: date · skill · mode · one line
```

## 3. Rules every workflow follows

1. **Read before writing.** Load `context/icp.md`, `context/offers.md`, `context/evidence.md` and `context/voice.md` before producing anything outbound. Load the relevant `memory/` file before recommending an angle (`objections.md` before any copy that handles risk or doubt).
2. **The evidence rule.** Any outcome, number, client name, logo, testimonial or "we've done X" in outbound copy must trace to a line in `context/evidence.md`. If it does not, write `[NEEDS PROOF: <what>]` in its place. Never invent proof. Never round up.
3. **Draft, never send.** Produce drafts (email drafts, Notion pages, local files). Sending, posting, publishing or booking requires the user's explicit yes in chat, every time.
4. **Write back.** After real work, append what was learned: buyer phrases → `voc-swipe.md`; objections → `objections.md`; deal events → `deals/<slug>.md`; one line → `log.md`. Dated (`YYYY-MM-DD`), with source (call link, email subject, URL). This is what makes the system improve.
5. **Cite the method.** When a recommendation comes from a framework, name it and the book skill it lives in (e.g. "JOLT · Limit the exploration — `sales-psychology` book 02"). Load that book file when the user asks why.
6. **One recommendation.** Lead with the single best move and why. Alternatives go below, briefly.
7. **Privacy.** Never place workspace content in URLs, public repos, or third-party tools the user didn't choose. Prospect personal data stays in the workspace.

## 4. Deal file format (`deals/<company-slug>.md`)

```markdown
---
company: Acme Dental Group
slug: acme-dental-group
stage: discovery       # one of: lead | discovery | proposal | negotiation | won | lost | nurture
value: 4500            # expected first-year value, number only
currency: GBP
source: outreach | magnet | referral | inbound | content
decision_maker: "Name, role"
champion: "Name, role"
stall_type: none      # one of: none | status-quo | valuation | information | outcome | decision-process
quoted_price: 5200     # number in the proposal, once sent
next_step: "Office manager reviews intake-workflow demo"
next_step_date: 2026-10-12
last_touch: 2026-10-06 # last REAL contact with the buyer, not a draft
closed:                # YYYY-MM-DD once won or lost
---

## Gap
Current state · Future state · Impact (in their numbers) · Root cause
- Impact (annual): 93600   # machine-readable line; pitch reads it

## Timeline (append-only, newest last)
### 2026-10-06 · Discovery call · <link>
- Score: …  · Advance: …  · Verbatims: "…"
```

`stage`, `next_step`, `next_step_date`, `last_touch` must always be current; the session-start hook reads them to flag overdue deals.

## 5. Connectors

Detect tools by name at runtime; never assume one is present. See `CONNECTORS.md` at the plugin root. If a category has no tool, use the fallback listed there and say which one you used.

## 6. File conventions (shared by every skill)

- **Examples.** Template lines ending `<!-- example: delete -->` are synthetic. Ignore them when reading; remove them when writing the first real entry in that section.
- **Evidence ids.** Rows in `context/evidence.md` carry stable ids: `ev-NN` verified, `uv-NN` unverified. Outbound drafts and audits cite the id (`proof: ev-03`). Never reuse a retired id.
- **VOC lines.** `memory/voc-swipe.md` has six headings: Pains · Desired outcomes · Triggers · Anxieties · Alternatives · Their words for the problem. Append under the matching heading: `- "verbatim" — source (link or title), YYYY-MM-DD, segment`. Grep first; skip duplicates.
- **Objections.** `memory/objections.md` blocks are headed `### YYYY-MM-DD · <Company> · "<objection>"`. Practice data from roleplay is tagged `source: roleplay` and is never treated as buyer evidence.
- **Best angles.** `memory/outreach-learnings.md` keeps a rewrite-in-place block between `<!-- best-angles:start -->` and `<!-- best-angles:end -->`; dated review sections (`## YYYY-MM-DD · review`) are appended below it.
- **Pricing fields.** `context/pricing.md` headings that workflows parse: `## Price list`, `## Floor`, `## Anchors`, `## Trades instead of discounts`, `## Payment terms`, optional `## Pipeline` (`stage: percent`).
- **Asset status.** Generated drafts in `assets/` start with frontmatter `status: draft` and, once the user confirms they went out, `status: sent` + `sent_date: YYYY-MM-DD`. Outreach review counts only `sent`.
- **Log.** `log.md` lines: `YYYY-MM-DD · <skill> · <mode> · <one line> · <artifact path>`.
