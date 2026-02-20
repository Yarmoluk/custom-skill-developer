# Chapter 7 Quiz

Test your understanding of quality scoring systems and self-evaluating skills.

---

**Question 1** *(Bloom's: Remember)*
*Concept: 1-100 point scale convention (C062)*

What scoring scale is used as the standard across the McCreary skill ecosystem for quality rubrics?

- [ ] A) 1-5 star rating
- [ ] B) Letter grades (A through F)
- [ ] C) 1-100 point scale
- [ ] D) 0.0-10.0 decimal scale

??? success "Answer"
    **C) 1-100 point scale**

    The 100-point scale is the standard across the McCreary skill ecosystem. It was chosen for three reasons: humans interpret 100-point scores intuitively (73 communicates "passing but not great" without explanation), sub-categories can be weighted in increments of 5 or 10 for natural integer totals, and common thresholds (70, 80, 85) fall on round numbers that align with standard quality tiers. Skills using this scale produce scores that are immediately interpretable by users and comparable across different skills.

---

**Question 2** *(Bloom's: Understand)*
*Concept: Minimum passing score threshold (C063)*

A skill developer is building a skill for drafting medical education content. The default threshold is 75. What adjustment should they consider, and why?

- [ ] A) Lower the threshold to 60 because medical content requires more iteration and users will refine it anyway
- [ ] B) Raise the threshold to 80 or higher because high-stakes content warrants stricter quality gates before delivery
- [ ] C) Keep the threshold at 75 since it is the standard and should not be changed
- [ ] D) Remove the threshold entirely and let the user decide whether the output is acceptable

??? success "Answer"
    **B) Raise the threshold to 80 or higher because high-stakes content warrants stricter quality gates before delivery**

    Thresholds should reflect the stakes of the domain. For high-stakes content (medical education, legal documentation, production code), raising the minimum acceptable threshold is appropriate — errors in these domains have real consequences. The default of 75 is suitable for general-purpose content. Draft content intended for human revision might use a lower threshold of 60. The key requirement is that thresholds must be defined explicitly in the SKILL.md. "Acceptable" left undefined produces inconsistent behavior.

---

**Question 3** *(Bloom's: Understand)*
*Concept: Self-assessment by Claude (C066)*

What is the fundamental problem that quality scoring solves in skill design?

- [ ] A) Claude generates text too slowly without a scoring system to guide it
- [ ] B) Claude has no built-in mechanism for determining whether its output meets your specific domain standards — quality scoring externalizes those criteria explicitly
- [ ] C) Quality scoring prevents Claude from producing offensive content
- [ ] D) Quality scoring enables Claude to compare outputs from different sessions

??? success "Answer"
    **B) Claude has no built-in mechanism for determining whether its output meets your specific domain standards — quality scoring externalizes those criteria explicitly**

    Claude generates fluent, plausible output, but without explicit criteria it defaults to implicit judgment about what "good" looks like. That implicit judgment may not match your domain requirements. Quality scoring externalizes those requirements into a rubric that Claude applies consistently, every run. The three practical benefits are consistency (same criteria applied every run), transparency (users see specific scores, not vague judgments), and automation of revision (low-scoring output triggers revision before delivery).

---

**Question 4** *(Bloom's: Apply)*
*Concept: Gap report behavior (C064)*

A skill runs and scores 61/100 against its rubric. The minimum passing score is 70. What should the skill do?

- [ ] A) Deliver the output with a note that it scored below threshold
- [ ] B) Present a gap report identifying which criteria failed, ask the user if they want revisions, and wait for input before writing any files
- [ ] C) Automatically revise and re-score without informing the user
- [ ] D) Halt execution entirely and ask the user to start over from scratch

??? success "Answer"
    **B) Present a gap report identifying which criteria failed, ask the user if they want revisions, and wait for input before writing any files**

    Between the adequate range (55-69) and insufficient range (below 40), a score of 61 falls in "Adequate: Ask user whether to deliver or revise." The gap report must identify specific failing criteria — not just report the score — so the user can make an informed decision. Silent delivery of below-threshold output defeats the purpose of having a quality gate. Complete halt is reserved for scores below 40 (Insufficient). The correct behavior is transparency about what failed plus a decision point for the user.

---

**Question 5** *(Bloom's: Evaluate)*
*Concept: Criterion specificity requirement (C068)*

A skill developer writes this quality criterion: "Content is well-written and appropriate for the audience." Why is this criterion poorly designed?

- [ ] A) It is too long and takes up too many tokens in the SKILL.md
- [ ] B) "Well-written" and "appropriate" are subjective and unmeasurable — Claude cannot apply this consistently, making the score meaningless
- [ ] C) It does not reference any specific output file by name
- [ ] D) Quality criteria must always be written as yes/no questions, not descriptive statements

??? success "Answer"
    **B) "Well-written" and "appropriate" are subjective and unmeasurable — Claude cannot apply this consistently, making the score meaningless**

    Criteria must be explicit and measurable before they produce consistent scores. "Well-written" and "appropriate" leave interpretation to Claude's implicit judgment — exactly what quality scoring is designed to replace. Effective criteria are concrete: "No sentence exceeds 25 words," "Every definition is 2-4 sentences," "All quantitative claims cite a source." These can be checked deterministically. Vague criteria produce scores that vary between sessions and provide no actionable guidance when an output fails them.

---
