<h1 align="center">📚 Book Skills</h1>

<p align="center">
  <strong>A client-acquisition system for Claude Code, built on 70 books.</strong><br>
  It researches your market, writes your magnets and outreach, debriefs your calls, rescues stalled deals and builds your proposals,<br>
  grounded in <em>your</em> ICP, offers and proof, and it learns from every call and reply.
</p>

<p align="center">
  <img alt="Workflows" src="https://img.shields.io/badge/workflow%20skills-5-ff6f61?style=for-the-badge">
  <img alt="Modes" src="https://img.shields.io/badge/modes-23-orange?style=for-the-badge">
  <img alt="Agents" src="https://img.shields.io/badge/agents-4-blueviolet?style=for-the-badge">
  <img alt="Books" src="https://img.shields.io/badge/books%20distilled-70-blue?style=for-the-badge">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-lightgrey?style=for-the-badge">
</p>

<p align="center">
  <a href="#-install">Install</a> ·
  <a href="#-what-it-does">What it does</a> ·
  <a href="#-the-loop">The loop</a> ·
  <a href="#-commands">Commands</a> ·
  <a href="#-why-its-different">Why it's different</a> ·
  <a href="#-evals">Evals</a> ·
  <a href="#-the-70-books">The 70 books</a> ·
  <a href="#%EF%B8%8F-honest-caveats">Caveats</a>
</p>

---

```text
/book-skills:deals debrief latest
→ Score 58/100 · ended in a Continuation ("send me some info"), not an Advance
→ Missed yellow light at 14:32: "we tried something like this before"
→ Stall: valuation uncertainty → JOLT · Offer a recommendation
→ Deal file updated · 6 buyer verbatims saved · follow-up drafted with a dated next step
```

Most "AI sales" prompts give generic advice. Book Skills **does the work**: it reads your call recordings, inbox and prospect data through whatever tools you've connected, applies named frameworks from the best books on selling, and writes back what it learned to a private workspace, so month six is sharper than month one.

---

## 🚀 Install

```bash
claude plugin marketplace add FakharEAli/book-skills
claude plugin install book-skills@book-skills
```

Then, once:

```text
/book-skills:setup
```

Setup creates your private workspace (`~/.book-skills/`, never in this repo) and interviews you for your ICP, offers, pricing, proof and voice. Optional `bootstrap` mode pre-fills it from your website, LinkedIn and recent call transcripts, and asks before reading any of them.

<details>
<summary>Cowork · claude.ai · local clone</summary>

- **Cowork:** download the repo as a zip, rename it `book-skills.plugin`, and drop it into a Cowork chat (or Settings → Plugins).
- **claude.ai:** zip any single folder under `skills/` and upload it at Settings → Capabilities → Skills. Knowledge skills work fully; workflow skills work without a workspace and say what they assumed.
- **Local clone:** `git clone https://github.com/FakharEAli/book-skills && claude plugin marketplace add ./book-skills && claude plugin install book-skills@book-skills`
</details>

---

## 🧭 What it does

| Layer | Skill | What you get |
|---|---|---|
| **1 · Lead magnets** | `/book-skills:lead-magnets` | A market brief in your buyers' own words (scraped reviews, forums, job posts), then the right magnet **for their awareness stage**: scorecard, cost calculator, teardown or ROI model, written in full, with landing page, 5-email nurture and launch post |
| **2 · Outreach** | `/book-skills:outreach` | Prospect lists scored 0–100 with a cited "why now" trigger per row; cold emails and LinkedIn messages that pass an evidence audit; 21-day sequences; reply handling that moves to a dated next step; a review that learns which angles actually get replies |
| **3 · Deals** | `/book-skills:deals` | One-page call prep with a SPIN question tree; **debriefs that score your call**, update the deal, save buyer verbatims and draft the follow-up; JOLT-based rescue for stalled deals; weighted pipeline; win/loss post-mortems that surface patterns |
| **4 · Pitch** | `/book-skills:pitch` | A One-Offer Sheet priced from your real deal gaps; single-recommendation proposals with ROI in the buyer's numbers; live negotiation help; **roleplay against a simulated prospect** who hides concerns until you earn them |
| **0 · Setup** | `/book-skills:setup` | Workspace creation, interview, optional bootstrap from your site/LinkedIn/calls, and a health audit |

Underneath sit **7 knowledge skills** (psychology, behaviour, marketing psychology, sales psychology, copywriting, offer creation, and the client-eagerness playbook), the method library every workflow cites. You can call them directly too.

---

## 🔁 The loop

```text
           ┌──────────── context/ ─────────────┐
           │  ICP · offers · pricing · EVIDENCE │
           │  voice · competitors               │
           └───────────────┬───────────────────┘
                           ▼
 lead-magnets ──▶ outreach ──▶ deals ──▶ pitch ──▶ won / lost
      ▲              ▲           │          │          │
      │              │           ▼          ▼          ▼
      └──────────────┴──── memory/ ◀───────────────────┘
          voc-swipe · objections · outreach-learnings
          magnet-learnings · win-loss · suppression
```

Every mode **writes back**: buyer phrases from calls feed your copy, objections feed your proposals, reply rates rewrite your "current best angles", win/loss patterns reshape your offer. That data is yours alone. It's what no generic prompt, course or competitor can copy.

---

## ⌨️ Commands

| Skill | Modes |
|---|---|
| `setup` | `init` · `interview` · `bootstrap` · `audit` |
| `lead-magnets` | `research <segment>` · `build <problem> [format]` · `funnel <magnet>` · `review` |
| `outreach` | `list <segment> [n]` · `write <prospect>` · `sequence <prospect>` · `reply <pasted reply>` · `review [period]` |
| `deals` | `prep <company\|upcoming>` · `debrief <link\|latest>` · `rescue <company>` · `pipeline` · `postmortem <company> won\|lost` |
| `pitch` | `offer <segment>` · `proposal <company>` · `rehearse <company>` · `negotiate <pushback>` · `review <draft>` |

Or just describe the situation ("the dentist went quiet after the proposal") and Claude routes it.

**Agents** (dispatched by the workflows): `call-scorer` (100-point call rubric with verbatims and timestamps) · `voc-miner` (verbatim buyer language, source-checked) · `evidence-auditor` (every claim vs. your proof ledger) · `prospect-roleplay` (in-character buyer for practice).

**Hooks:** a session-start line flags overdue next steps and stale reviews (silent when there's nothing to say, zero cost without a workspace), and an outbound guard asks before any tool sends, posts, publishes or books. Drafts are never blocked.

---

## 💎 Why it's different

- **The evidence rule.** Every result, number, client name or testimonial in outbound copy must trace to a row in your `evidence.md`. Anything else becomes `[NEEDS PROOF: …]`. It will not invent proof, and the auditor checks before you see a draft.
- **Draft, never send.** Nothing leaves your machine without your yes. A hook enforces it.
- **Decisions, not advice.** Explicit rubrics and thresholds: trigger decay by age, minimum 30 sends before calling a winner, Continuation-capped call scores, magnet keep/kill bands, a computed inverted Ackerman ladder from your price floor.
- **Named methods, cited.** SPIN, JOLT, Gap Selling, Trust Equation, Value Equation, Schwartz awareness stages, Commercial Teaching, tactical empathy: each recommendation names the framework and the book file it came from.
- **Tool-agnostic.** Fathom, Gong, Gmail, Clay, Apollo, Notion, Gamma, Typeform, Supabase, Slack, or none: it detects what you've connected and falls back gracefully. See [CONNECTORS.md](CONNECTORS.md).
- **Private by design.** Your workspace lives outside the plugin. The public repo contains methods, never your data.

---

## 🧪 Evals

`evals/` holds 10 cases, each a realistic synthetic scenario with 3–4 pass/fail graders that test the behaviour a generic assistant gets wrong:

| Case | What it tests | With plugin | Baseline |
|---|---|---|---|
| `deals-debrief-continuation-not-advance` | "send me some info" is a Continuation, not a win | **4/4** | 1/4 |
| `deals-debrief-valuation-stall` | classifies valuation indecision; one recommendation; dated Advance | **4/4** | 1/4 |
| `deals-rescue-outcome-uncertainty` | takes risk off the table; no FOMO | **4/4** | 2/4 |
| `lead-magnets-build-format-by-awareness` | picks magnet format by awareness stage | **4/4** | 2/4 |
| `lead-magnets-no-invented-stats` | refuses to invent statistics | **3/3** | 1/3 |
| `outreach-reply-objection-advance` | "we use Zapier" → move off the solution → dated next step | **4/4** | 3/4 |
| `outreach-write-needs-proof` | no invented client results; ≤90 words; question CTA | **3/3** | 2/3 |
| `pitch-negotiate-competitor-half-price` | no reflex discount; calibrated question; trade | **4/4** | 4/4 |
| `pitch-proposal-one-recommendation` | one recommendation; ROI in buyer's numbers; risk reversal | **4/4** | 3/4 |
| `setup-evidence-not-fabricated` | vague claims filed as unverified, not as proof | **3/3** | 1/3 |
| **Total** | | **37/37 (100%)** | 20/37 (54%) |

Method: one run per arm, graded blind by a separate model against the rubric files; full verdicts in [evals/RESULTS.md](evals/RESULTS.md). Caveats: n = 1 per arm; the rubrics were written alongside the skills, so they test the behaviours the plugin is designed for; blinding is imperfect because plugin outputs mention its own commands.

Run them with `claude plugin eval .` (early access), or read the cases as a spec.

---

## 🏗 Architecture

```
book-skills/
├── skills/
│   ├── setup/ lead-magnets/ outreach/ deals/ pitch/    # workflow skills: SKILL.md → modes/*.md → templates/
│   └── human-psychology/ … client-eagerness-playbook/  # knowledge skills: SKILL.md → books/NN-*.md → playbooks
├── agents/        call-scorer · voc-miner · evidence-auditor · prospect-roleplay
├── hooks/         session_status.py · outbound_guard.py
├── shared/        workspace.md: the contract every workflow follows
├── evals/         10 cases × graders
└── CONNECTORS.md  tool categories, detection, fallbacks
```

**Token economics:** only skill descriptions are always loaded. A workflow loads its `SKILL.md` (~1.5k tokens) and then only the one mode file it needs (~2k). Book files load only when a recommendation needs the full method.

---

## 📖 The 70 books

<details>
<summary><strong>Human psychology</strong> · Kahneman, Aronson, Myers, Tavris &amp; Aronson, Chabris &amp; Simons, Barrett, Gilbert, Nisbett, Pinker, Galef</summary>

Thinking, Fast and Slow · The Social Animal · Psychology (14th ed.) · Mistakes Were Made (but Not by Me) · The Invisible Gorilla · How Emotions Are Made · Stumbling on Happiness · Mindware · How the Mind Works · The Scout Mindset
</details>

<details>
<summary><strong>Human behaviour</strong> · Sapolsky, Ross &amp; Nisbett, Wood, Thaler &amp; Sunstein, Haidt, Lieberman, Fogg, Mullainathan &amp; Shafir, Henrich, Simler &amp; Hanson</summary>

Behave · The Person and the Situation · Good Habits, Bad Habits · Nudge: The Final Edition · The Righteous Mind · Social · Tiny Habits · Scarcity · The Secret of Our Success · The Elephant in the Brain
</details>

<details>
<summary><strong>Marketing psychology</strong> · Cialdini, Shotton, Barden, Heath &amp; Heath, Berger, Sutherland, Martin &amp; Marks, Sharp</summary>

Influence (New and Expanded) · The Choice Factory · Decoded · Pre-Suasion · Made to Stick · Contagious · The Catalyst · Alchemy · Messengers · How Brands Grow
</details>

<details>
<summary><strong>Sales psychology</strong> · Rackham, Dixon &amp; McKenna, Maister/Green/Galford, Keenan, Voss, Dixon &amp; Adamson, Beckwith, Pink, Hoffeld, Khalsa &amp; Illig</summary>

SPIN Selling · The JOLT Effect · The Trusted Advisor · Gap Selling · Never Split the Difference · The Challenger Sale · Selling the Invisible · To Sell Is Human · The Science of Selling · Let's Get Real or Let's Not Play
</details>

<details>
<summary><strong>Copywriting</strong> · Schwartz, Bly, Sugarman, Hopkins, Ogilvy, Masterson &amp; Forde, Caples, Wiebe, Halbert, Whitman</summary>

Breakthrough Advertising · The Copywriter's Handbook · The Adweek Copywriting Handbook · Scientific Advertising · Ogilvy on Advertising · Great Leads · Tested Advertising Methods · Where Stellar Messages Come From · The Boron Letters · Cashvertising
</details>

<details>
<summary><strong>Offer creation</strong> · Hormozi, Osterwalder et al., Dunford, Ramanujam &amp; Tacke, Joyner, Enns, Moesta &amp; Engle, Christensen et al., Bland &amp; Osterwalder, Kim &amp; Mauborgne</summary>

$100M Offers · Value Proposition Design · Obviously Awesome · Monetizing Innovation · The Irresistible Offer · The Win Without Pitching Manifesto · Demand-Side Sales 101 · Competing Against Luck · Testing Business Ideas · Blue Ocean Strategy
</details>

<details>
<summary><strong>Client-eagerness playbook</strong> · the 10-book reading order as a 10-stage process</summary>

Obviously Awesome → Value Proposition Design → $100M Offers → SPIN Selling → The Trusted Advisor → Influence → Selling the Invisible → Where Stellar Messages Come From → The JOLT Effect → Breakthrough Advertising
</details>

---

## ⚠️ Honest caveats

- **Distilled from the authors' published frameworks, not from book text.** No passages are reproduced. Uncertain claims were omitted, not invented; each book file has a Caveats section. Lowest confidence: Wiebe's *Where Stellar Messages Come From* (written from her publicly taught method).
- **Proprietary sales research** (SPIN, JOLT, Challenger) is practitioner evidence, not peer-reviewed science, and is labelled that way.
- **Thresholds are rules of thumb** (reply-rate winners, magnet keep/kill bands, pricing ratios). They are labelled as the plugin's defaults, and you can override them in your workspace.
- **It drafts; you decide.** The system is built to stop overclaiming and pressure tactics, not to automate judgment away.

---

## 🤝 Contributing

PRs welcome: a sharper rubric, a missing caveat, a new connector fallback, a new eval case. Keep to the structure in `shared/workspace.md`, keep eval fixtures synthetic, and never paste book text.

## 📄 License

MIT © Fakhar E Ali. The books belong to their authors; buy them.
