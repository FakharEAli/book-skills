# Grader: classifies the stall as indecision, valuation type

Priya owned the problem in her own numbers ("Roughly sixty empty slots a week", "about fifty-five quid", "fourteen percent") and then could not choose between packages ("which one would you go for", "I keep flip-flopping", "What do most clinics pick?"). Under JOLT (Dixon & McKenna) that is indecision of the valuation type, not a status-quo problem.

**PASS** if the response does all of:
- Classifies the stall as indecision with valuation as the type (wording such as "valuation", "too many options / can't choose between options" counts), e.g. `stall_type: valuation` in the deal-file update.
- Supports it with at least one of Priya's option-choosing quotes.
- Names the matching lever as Offer a recommendation (or an unambiguous equivalent: "give her one clear recommendation").
- Classifies the call outcome as a Continuation (or otherwise clearly says no dated buyer action was agreed), not a success.

**FAIL** if any of:
- The primary classification is status quo, lack of information, or outcome uncertainty.
- No stall classification is given.
- The lever recommended is more information (e.g. send the comparison of all three), urgency, or a discount.
- The call is described as having secured an Advance or next step because Sam promised to email a comparison.
