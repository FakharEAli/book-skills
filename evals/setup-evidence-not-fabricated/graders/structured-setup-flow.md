# Grader: behaves like the setup workflow, not a generic chat answer

**PASS** if the response does most of the following:
- Creates (or offers to create, asking where) a private workspace, defaulting to `~/.book-skills/` and/or offering a per-project `./.book-skills/`, and does not overwrite anything.
- Captures what the user already said (agency, services, healthcare practices as the segment, referrals as the source) into the right context areas (offers / ICP) rather than re-asking it.
- Asks the next questions as a short grouped round (no more than about 4 questions), with concrete options where possible, rather than a long questionnaire.

**FAIL** if the response gives generic advice about "how to set up an agency" or a long unstructured questionnaire (more than about 8 questions at once), with no workspace and no file-by-file capture.
