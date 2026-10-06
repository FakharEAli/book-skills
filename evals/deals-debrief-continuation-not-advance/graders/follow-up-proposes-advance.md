# Grader: the follow-up turns "send me info" into a dated Advance, without invented proof

A generic answer drafts "As promised, here's some info about us, let me know your thoughts". The plugin's follow-up must recap in Gareth's words and propose one specific, dated buyer action. Jo has one unnamed client and no permission to share numbers.

**PASS** if the email draft does all of:
- Recaps at least one of Gareth's own phrases or numbers accurately (maintenance "from four directions", "three hundred" a month as his guess, "half her day is WhatsApp", the landlord who called them "a black hole" after leaving with twelve properties).
- Proposes one specific next step involving Gareth and/or Leanne with a concrete day or date after 2026-10-06 (or two specific options), as the single call to action.
- Contains no named client, no client numbers, and no outcome claims stated as fact. Phrases like "an agency went from chaos to everything logged in two weeks" appear only with `[NEEDS PROOF: …]` or not at all.
- Is marked as a draft, not sent.

**FAIL** if any of:
- The email's main content is the info pack or examples, ending in "let me know", "any questions", or "speak soon" without a dated buyer action.
- It invents or names a client, or states results as achieved ("pays for itself in X months", "cuts admin by 50%") without a `[NEEDS PROOF]` marker.
- It misquotes Gareth or attributes words to him he did not say.
