# 03 · Psychology (14th ed.)
**Author(s)**: David G. Myers, C. Nathan DeWall, June Gruber | **Year**: 2024 (14th ed.) | **Rank in category**: 03/10
**Why it's on the list**: comprehensive textbook foundation across the field

## Core Idea
Behaviour and mental life are best explained at three levels at once: biological, psychological, and social-cultural (the biopsychosocial approach). The book's working method is the scientific attitude: curiosity, skepticism, and humility, applied through critical thinking because intuition and common sense are reliably fooled by hindsight bias, overconfidence, and the tendency to see patterns in random events.

## Frameworks Introduced
**The Three Enemies of Intuition** — hindsight bias, overconfidence, perceiving order in random events. **How**: when a prospect says "I knew that tool would fail," that is hindsight bias; when they say "I know exactly where our bottlenecks are," test it against measured data before building; when they report "automation always breaks in Q4," ask for the count. **Why**: these are the three recurring reasons owners mis-diagnose their own operations. **Failure mode**: correcting the owner bluntly triggers defensiveness; show the data and let them revise.

**Memory as Reconstruction (encoding → storage → retrieval)** — memory is rebuilt at retrieval, shaped by cues, expectations, and later information (Loftus's misinformation effect). **How**: never rely on the prospect's recollection of how a process runs; shadow the process or pull system logs. **Spacing effect** and **testing effect**: distributed practice and retrieval beat massed re-reading. **Application**: onboarding and training for client staff should be spaced over weeks with short retrieval quizzes, not one long handover session.

**Operant Conditioning and Reinforcement Schedules (Skinner)** — behaviour followed by reinforcement increases; schedules shape persistence. **How**: continuous reinforcement teaches fastest; partial (especially variable) reinforcement produces behaviour that resists extinction. **Application**: when you want staff to adopt a new workflow, reinforce every use at first (visible wins, fast feedback), then taper. **Overjustification effect**: paying people for what they already enjoy can reduce intrinsic motivation; do not bribe adoption of a tool that already saves them pain.

**Attitudes ↔ Actions** — attitudes predict behaviour when external influences are minimal, the attitude is specific, and the person is aware of it; actions also shape attitudes (**foot-in-the-door**, role playing, cognitive dissonance). **How**: get small actions first (a 15-minute audit call, a one-process pilot). The action produces the attitude.

**Theories of Emotion (James-Lange, Cannon-Bard, Schachter-Singer two-factor)** — emotion involves physiological arousal plus cognitive labelling; the same arousal can be labelled excitement or anxiety depending on context (**spillover effect**). **How**: a prospect's nervous energy about change can be labelled as readiness if you supply the label and the plan.

**Adaptation-Level Phenomenon and Relative Deprivation** — people judge outcomes relative to a neutral level set by prior experience, and relative to others. Satisfaction fades as a new level becomes the norm. **How**: a client who saved 20 hours a week stops feeling it after a month; keep a visible dashboard of cumulative hours saved versus the pre-automation baseline, and compare against peers.

## Key Principles
- Correlation is not causation; owners constantly infer causation from co-occurrence ("sales dropped when we added the CRM"). Ask for the third variable.
- Confirmation bias and belief perseverance: once a belief forms ("AI tools are unreliable"), contrary evidence is discounted. Myers' remedy: ask the person to explain the opposite finding; considering the opposite reduces perseverance more than presenting data does.
- Framing changes choices with identical facts; "90% uptime" and "down 36 days a year" are the same fact.
- The availability heuristic drives risk perception: one vivid AI-failure story outweighs quiet successes. Supply your own vivid, specific success.
- Selective attention and perceptual set: people see what they expect. A sceptic will perceive a demo glitch as proof; a believer will not notice it. Set expectations before the demo.
- Intrinsic motivation (autonomy, competence, relatedness) sustains behaviour; design staff-facing automations to increase their sense of competence, not to monitor them.
- Group polarization: a team that already leans against change will lean harder after discussing it among themselves. Get into the room before they discuss it without you.
- Self-serving bias: people attribute success to themselves and failures to circumstances; expect the owner to credit their team for wins and blame the vendor for failures. Build measurement in from day one so attribution is on record.

## Anti-patterns
- Treating a confident eyewitness account of a process as accurate.
- One-shot training sessions (massed practice) for client staff.
- Relying on common sense explanations after the fact; "I knew it all along" is not evidence.
- Paying for adoption of something intrinsically useful.

## Worked Example (applied to Fakhar's business)
Onboarding a 30-person e-commerce team to an n8n order-exception workflow:
1. Pre-demo framing (perceptual set): "You'll see two edge cases we handle and one we deliberately route to a human. Watch for the human handoff."
2. Foot-in-the-door: ask the ops lead to run the first five exceptions herself before the team sees it.
3. Spaced training: three 15-minute sessions over two weeks, each starting with a 3-question retrieval quiz on the last session.
4. Reinforcement schedule: a Slack message for every successful auto-resolution in week one (continuous), then a daily tally (interval), then a weekly summary.
5. Adaptation-level counter: a dashboard tile that shows cumulative hours saved since go-live, with the pre-launch baseline fixed in view.
6. Attribution record: a shared log of what the automation handled and what humans handled, so that in month three the credit is not reassigned by self-serving bias.

## Caveats
- As a textbook, it reports consensus findings and notes replication problems in recent editions (ego depletion, some priming, Zimbardo); its treatment of each topic is broad rather than deep.
- Maslow's hierarchy is presented with the caveat that the order is not fixed and evidence is weak; do not use it as a sales framework.
- Book 06 (Barrett) rejects the "basic emotions" framing that textbooks still partly present; book 01 (Kahneman) goes far deeper on judgment.

## Connects To
- 01 (heuristics and biases in depth), 02 (social influence in depth), 05 (attention and memory illusions), 07 (adaptation and affective forecasting), 08 (correlation vs causation as reasoning tools).
- Sibling skills: human-behavior (habit and reinforcement), client-eagerness-playbook (onboarding).
