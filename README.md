# Book Skills

Seven Claude Code skills distilling 70 books (10 per category) into decision rules, playbooks and templates for selling AI-automation services to business owners.

## Install

```bash
claude plugin marketplace add <owner>/book-skills   # GitHub
claude plugin install book-skills@book-skills
```

Local: `claude plugin marketplace add /path/to/book-skills` then the same install line.

## Which skill when

| Situation | Skill |
|---|---|
| New offer or new industry, end to end | `/book-skills:client-eagerness-playbook` (start here) |
| Packaging, pricing, positioning, guarantees, WTP tests | `/book-skills:offer-creation` |
| Discovery calls, "let me think about it", negotiation | `/book-skills:sales-psychology` |
| Landing pages, cold email, LinkedIn, proposals | `/book-skills:copywriting` |
| Message, proof, credibility, removing resistance | `/book-skills:marketing-psychology` |
| How prospects judge risk and justify past failures | `/book-skills:human-psychology` |
| Yes-but-no-implementation, onboarding, adoption | `/book-skills:human-behavior` |

Each skill: `SKILL.md` (core frameworks + situation index) → `playbooks.md` (step-by-step workflows) → `books/NN-*.md` (one per book, loaded on demand) → `cheatsheet.md`, `patterns.md`, `glossary.md`.

Distilled from the authors' published frameworks; no book text is reproduced. If you own a book as EPUB/PDF, [book-to-skill](https://github.com/virgiliojr94/book-to-skill) can fold the real text into the matching skill.
