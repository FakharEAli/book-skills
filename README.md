<h1 align="center">📚 Book Skills</h1>

<p align="center">
  <strong>70 books. 7 Claude Code skills. One job: make clients eager to work with you.</strong>
</p>

<p align="center">
  <img alt="Skills" src="https://img.shields.io/badge/skills-7-blueviolet?style=for-the-badge">
  <img alt="Books" src="https://img.shields.io/badge/books%20distilled-70-blue?style=for-the-badge">
  <img alt="Always-on cost" src="https://img.shields.io/badge/always--on%20cost-~1k%20tokens-green?style=for-the-badge">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-lightgrey?style=for-the-badge">
</p>

<p align="center">
  <a href="#-install">Install</a> ·
  <a href="#-which-skill-when">Which skill when</a> ·
  <a href="#-the-70-books">The 70 books</a> ·
  <a href="#-how-a-skill-is-built">How a skill is built</a> ·
  <a href="#-design-decisions">Design decisions</a> ·
  <a href="#%EF%B8%8F-honest-caveats">Caveats</a>
</p>

---

**Book Skills** is a Claude Code plugin that turns the best books on psychology, behaviour, marketing, sales, copywriting and offer design into **decision rules, playbooks and fill-in templates** your agent applies while you work. Not summaries. Toolkits.

It was built for one concrete situation: running an AI-automation agency and selling to business owners. Every worked example, script and template is written for that case, but the frameworks are the authors' and travel anywhere a service is sold.

```
/book-skills:sales-psychology  prospect said "let me think about it"
/book-skills:offer-creation    package our onboarding automation for dental clinics
/book-skills:copywriting       rewrite this landing page hero for a problem-aware audience
```

---

## 🚀 Install

```bash
claude plugin marketplace add FakharEAli/book-skills
claude plugin install book-skills@book-skills
```

That's it. Seven skills appear as `/book-skills:<name>`. Restart any open session to pick them up.

<details>
<summary>Install from a local clone instead</summary>

```bash
git clone https://github.com/FakharEAli/book-skills.git
claude plugin marketplace add ./book-skills
claude plugin install book-skills@book-skills
```
</details>

<details>
<summary>Use in claude.ai (no Claude Code)</summary>

Zip any folder under `skills/` and upload it at **Settings → Capabilities → Skills**. Each skill is self-contained.
</details>

---

## 🧭 Which skill when

| You are… | Invoke | Books |
|---|---|---|
| Starting a **new offer or new industry** and want the whole sequence | `/book-skills:client-eagerness-playbook` ⭐ *start here* | 10-book reading order as a 10-stage process with templates |
| **Packaging, pricing, positioning**, guarantees, testing willingness to pay | `/book-skills:offer-creation` | Hormozi, Osterwalder, Dunford, Ramanujam, Joyner, Enns, Moesta, Christensen, Bland, Kim & Mauborgne |
| Running **discovery calls**, hearing "let me think about it", negotiating scope | `/book-skills:sales-psychology` | Rackham, Dixon & McKenna, Maister, Keenan, Voss, Adamson, Beckwith, Pink, Hoffeld, Khalsa |
| Writing **landing pages, cold email, LinkedIn, proposals** | `/book-skills:copywriting` | Schwartz, Bly, Sugarman, Hopkins, Ogilvy, Masterson, Caples, Wiebe, Halbert, Whitman |
| Making the **message land**: proof, credibility, removing resistance | `/book-skills:marketing-psychology` | Cialdini, Shotton, Barden, Heath, Berger, Sutherland, Martin & Marks, Sharp |
| Understanding how prospects **judge risk and justify past failures** | `/book-skills:human-psychology` | Kahneman, Aronson, Myers, Tavris, Chabris & Simons, Barrett, Gilbert, Nisbett, Pinker, Galef |
| Why "yes" doesn't become **implementation**; onboarding and adoption | `/book-skills:human-behavior` | Sapolsky, Ross & Nisbett, Wood, Thaler & Sunstein, Haidt, Lieberman, Fogg, Mullainathan, Henrich, Simler & Hanson |

Each skill's `SKILL.md` carries a **Situation Index** so Claude knows which book file to open for the problem you describe.

---

## 📖 The 70 books

<details open>
<summary><strong>1 · Human psychology</strong> — how people think, feel, perceive and justify decisions</summary>

| # | Book | Author |
|---|---|---|
| 01 | Thinking, Fast and Slow | Daniel Kahneman |
| 02 | The Social Animal | Elliot Aronson, Joshua Aronson |
| 03 | Psychology (14th ed.) | David G. Myers, C. Nathan DeWall, June Gruber |
| 04 | Mistakes Were Made (but Not by Me) | Carol Tavris, Elliot Aronson |
| 05 | The Invisible Gorilla | Christopher Chabris, Daniel Simons |
| 06 | How Emotions Are Made | Lisa Feldman Barrett |
| 07 | Stumbling on Happiness | Daniel Gilbert |
| 08 | Mindware | Richard E. Nisbett |
| 09 | How the Mind Works | Steven Pinker |
| 10 | The Scout Mindset | Julia Galef |
</details>

<details>
<summary><strong>2 · Human behaviour</strong> — why people act, form habits, cooperate and resist change</summary>

| # | Book | Author |
|---|---|---|
| 01 | Behave | Robert M. Sapolsky |
| 02 | The Person and the Situation | Lee Ross, Richard E. Nisbett |
| 03 | Good Habits, Bad Habits | Wendy Wood |
| 04 | Nudge: The Final Edition | Richard H. Thaler, Cass R. Sunstein |
| 05 | The Righteous Mind | Jonathan Haidt |
| 06 | Social | Matthew D. Lieberman |
| 07 | Tiny Habits | BJ Fogg |
| 08 | Scarcity | Sendhil Mullainathan, Eldar Shafir |
| 09 | The Secret of Our Success | Joseph Henrich |
| 10 | The Elephant in the Brain | Kevin Simler, Robin Hanson |
</details>

<details>
<summary><strong>3 · Marketing psychology</strong> — attention, perception, trust, desire and choice</summary>

| # | Book | Author |
|---|---|---|
| 01 | Influence (New and Expanded) | Robert B. Cialdini |
| 02 | The Choice Factory | Richard Shotton |
| 03 | Decoded | Phil Barden |
| 04 | Pre-Suasion | Robert Cialdini |
| 05 | Made to Stick | Chip Heath, Dan Heath |
| 06 | Contagious | Jonah Berger |
| 07 | The Catalyst | Jonah Berger |
| 08 | Alchemy | Rory Sutherland |
| 09 | Messengers | Stephen Martin, Joseph Marks |
| 10 | How Brands Grow | Byron Sharp |
</details>

<details>
<summary><strong>4 · Sales psychology</strong> — discovery, trust, indecision, negotiation</summary>

| # | Book | Author |
|---|---|---|
| 01 | SPIN Selling | Neil Rackham |
| 02 | The JOLT Effect | Matthew Dixon, Ted McKenna |
| 03 | The Trusted Advisor | David H. Maister, Charles H. Green, Robert M. Galford |
| 04 | Gap Selling | Keenan |
| 05 | Never Split the Difference | Chris Voss, Tahl Raz |
| 06 | The Challenger Sale | Matthew Dixon, Brent Adamson |
| 07 | Selling the Invisible | Harry Beckwith |
| 08 | To Sell Is Human | Daniel H. Pink |
| 09 | The Science of Selling | David Hoffeld |
| 10 | Let's Get Real or Let's Not Play | Mahan Khalsa, Randy Illig |
</details>

<details>
<summary><strong>5 · Copywriting</strong> — researching the message and writing words that sell</summary>

| # | Book | Author |
|---|---|---|
| 01 | Breakthrough Advertising | Eugene M. Schwartz |
| 02 | The Copywriter's Handbook (4th ed.) | Robert W. Bly |
| 03 | The Adweek Copywriting Handbook | Joseph Sugarman |
| 04 | Scientific Advertising | Claude C. Hopkins |
| 05 | Ogilvy on Advertising | David Ogilvy |
| 06 | Great Leads | Michael Masterson, John Forde |
| 07 | Tested Advertising Methods | John Caples |
| 08 | Where Stellar Messages Come From | Joanna Wiebe |
| 09 | The Boron Letters | Gary C. Halbert, Bond Halbert |
| 10 | Cashvertising | Drew Eric Whitman |
</details>

<details>
<summary><strong>6 · Offer creation</strong> — outcome, scope, price, terms, positioning, validation</summary>

| # | Book | Author |
|---|---|---|
| 01 | $100M Offers | Alex Hormozi |
| 02 | Value Proposition Design | Osterwalder, Pigneur, Bernarda, Smith |
| 03 | Obviously Awesome | April Dunford |
| 04 | Monetizing Innovation | Madhavan Ramanujam, Georg Tacke |
| 05 | The Irresistible Offer | Mark Joyner |
| 06 | The Win Without Pitching Manifesto | Blair Enns |
| 07 | Demand-Side Sales 101 | Bob Moesta, Greg Engle |
| 08 | Competing Against Luck | Christensen, Hall, Dillon, Duncan |
| 09 | Testing Business Ideas | David J. Bland, Alexander Osterwalder |
| 10 | Blue Ocean Strategy | W. Chan Kim, Renée Mauborgne |
</details>

<details>
<summary><strong>7 · Client-eagerness playbook</strong> — the cross-category reading order, as a process</summary>

| Stage | Book | Artifact you produce |
|---|---|---|
| 1 | Obviously Awesome | Positioning statement |
| 2 | Value Proposition Design | Value Proposition Canvas for one segment |
| 3 | $100M Offers | One focused package: outcome, scope, price, terms |
| 4 | SPIN Selling | Discovery-call outline |
| 5 | The Trusted Advisor | Trust-building plan |
| 6 | Influence | Evidence audit of website and proposal |
| 7 | Selling the Invisible | Ways prospects can evaluate the service |
| 8 | Where Stellar Messages Come From | Customer-language swipe file |
| 9 | The JOLT Effect | Plan for indecision and "let me think about it" |
| 10 | Breakthrough Advertising | One message per awareness stage |
</details>

---

## 🏗 How a skill is built

Every skill follows the same shape, adapted from [book-to-skill](https://github.com/virgiliojr94/book-to-skill)'s output format:

```
skills/sales-psychology/
├── SKILL.md          ~2.5k tokens · core frameworks + Situation Index → loaded on invoke
├── playbooks.md      step-by-step workflows for real tasks, each step cites its book
├── cheatsheet.md     "when X, do Y, because Z" · decision trees · thresholds · tells
├── patterns.md       every technique across the 10 books, deduplicated
├── glossary.md       terms → definition → (book ##)
└── books/
    ├── 01-spin-selling.md        ~1.2k tokens each · loaded only when relevant
    ├── 02-the-jolt-effect.md
    └── …
```

Each book file: **Core Idea → Frameworks (with explicit steps and failure modes) → Key Principles → Anti-patterns → Worked Example applied to selling AI automation → Caveats → Connects To.**

**Token economics** (from `claude plugin details book-skills`):

| | Cost |
|---|---|
| Always-on, all 7 skills | ~1,035 tokens / session |
| Per invocation | ~2.6–3k tokens (`SKILL.md` only) |
| Book file | ~1–1.6k tokens, on demand |

---

## 🎯 Design decisions

- **Seven skills, not one.** Claude routes on the `description` line. Seven specific descriptions route better than one "70 books about selling" blob, and only the invoked skill's `SKILL.md` ever loads.
- **Playbooks over summaries.** The most-used file in each skill is `playbooks.md`: numbered steps, output templates, common failures. Reading about SPIN is not the same as having a discovery-call outline.
- **Exact framework names.** "SPIN", "Value Equation", "REDUCE", "Trust Equation", "B = MAP". Authors name things for a reason; paraphrases lose the precision.
- **Where books disagree, say so.** Hormozi's urgency devices vs Dixon & McKenna's finding that pressure deepens indecision; Barrett vs Pinker on emotion; Kahneman vs Nisbett vs Galef on whether you can debias yourself. Each `patterns.md` has a "where the books disagree" section.
- **Cross-linked.** The playbook skill points to the fuller treatment in sibling skills with relative links that resolve wherever the plugin is installed.

---

## ⚠️ Honest caveats

- **Distilled from the authors' published frameworks, not from book text.** No passages are reproduced. Where a builder was unsure of a specific claim it was omitted, not invented, and each book file has a Caveats section. The lowest-confidence file is Joanna Wiebe's *Where Stellar Messages Come From* (recent practitioner book; written from her publicly taught Copyhackers method and flagged as such).
- **Proprietary sales research** (SPIN's 35,000 calls, JOLT's 2.5M conversations, Challenger) is marked as practitioner evidence, not peer-reviewed science.
- **Replication issues** are called out where known: social priming in *Thinking, Fast and Slow*, ego depletion, contested nudge effect sizes.
- **Hormozi's results don't guarantee yours.** The framework is applied as something to validate, not a promise.

If you own a book as EPUB/PDF, [book-to-skill](https://github.com/virgiliojr94/book-to-skill)'s fold-in mode can enrich the matching skill with the real text.

---

## 🤝 Contributing

Corrections to a framework, a missing caveat, or a sharper decision rule: open a PR against the relevant `skills/<skill>/books/NN-*.md`. Keep the file's section structure and token budget. Please don't paste book text.

## 📄 License

MIT © Fakhar E Ali. The books belong to their authors; buy them.
