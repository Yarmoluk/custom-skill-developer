# Chapter 14 Quiz

Test your understanding of analysis and validation skills, DAG validation, and quality gate patterns.

---

**Question 1** *(Bloom's: Remember)*
*Concept: Analysis skill definition (C160)*

What is the defining purpose of an analysis skill, distinguishing it from data format and code generation skills?

- [ ] A) Analysis skills transform data from one format to another
- [ ] B) Analysis skills produce executable programs from natural language descriptions
- [ ] C) Analysis skills evaluate existing artifacts against defined criteria and return structured assessments with scores, flags, and recommendations
- [ ] D) Analysis skills manage session state and log files for downstream skills

??? success "Answer"
    **C) Analysis skills evaluate existing artifacts against defined criteria and return structured assessments with scores, flags, and recommendations**

    Analysis skills are the quality layer of the skill ecosystem. Where data format skills transform and code generation skills produce, analysis skills evaluate. They take an existing artifact — a Markdown file, a learning graph, a MicroSim — and return a structured assessment. The critical design requirement is that criteria must be explicit and measurable before the skill is written. "Good quality" is not a criterion; "has 8 to 12 concepts per learning unit" is.

---

**Question 2** *(Bloom's: Understand)*
*Concept: DAG validation skill (C162)*

A learning graph is described as a DAG (directed acyclic graph). Which of the following is NOT a property that a DAG validation skill should verify?

- [ ] A) No cycles exist in the graph (no circular prerequisite chains)
- [ ] B) No orphan nodes exist (every concept is reachable from an entry point)
- [ ] C) All concepts have the same difficulty level
- [ ] D) No dangling references exist (every edge points to a concept node that exists)

??? success "Answer"
    **C) All concepts have the same difficulty level**

    A DAG validation skill verifies structural integrity of the learning graph: absence of cycles (acyclicity), no orphan nodes (connectivity), no dangling references (referential integrity), appropriate depth distribution (not all concepts at the same level), and appropriate connectivity (no concepts with zero edges). Uniform difficulty level is not a structural property — a well-designed learning graph intentionally spans multiple difficulty levels from beginner to advanced. Requiring uniform difficulty would actually be a design flaw.

---

**Question 3** *(Bloom's: Apply)*
*Concept: Composite quality score (C165)*

A book metrics generator evaluates a textbook and produces these sub-scores: chapter completeness 18/20, MicroSim coverage 12/15, glossary completeness 14/15, reading level appropriateness 9/10, internal link integrity 10/10, cross-references 7/10, visual balance 8/10, learning objectives coverage 7/10. What is the composite score, and what does it indicate?

- [ ] A) 85/100 — excellent, deliver immediately with no caveats
- [ ] B) 72/100 — adequate, potentially flagging cross-references and learning objectives as improvement areas
- [ ] C) 55/100 — needs work, automatic revision required before delivery
- [ ] D) 100/100 — all criteria met, no further action needed

??? success "Answer"
    **A) 85/100 — excellent, deliver immediately with no caveats**

    Adding the sub-scores: 18 + 12 + 14 + 9 + 10 + 7 + 8 + 7 = 85. Using the standard quality threshold table, 85-100 is "Excellent: deliver immediately, no caveats." The composite quality score aggregates weighted sub-category scores into a single actionable signal. Individual sub-scores (cross-references: 7/10, learning objectives: 7/10) identify specific improvement opportunities even when the overall score is in the excellent range, giving the user targeted guidance for future enhancement.

---

**Question 4** *(Bloom's: Understand)*
*Concept: Read-heavy skill pattern (C167)*

Analysis skills are often described as "read-heavy." What does this mean and why does it create a token efficiency concern?

- [ ] A) Analysis skills produce reports with many lines of text
- [ ] B) Analysis skills must read all the artifacts they evaluate into context before scoring — for a 12-chapter textbook this could mean loading 80,000+ tokens of content just to apply the rubric
- [ ] C) Analysis skills require more computing resources than other skill types
- [ ] D) Analysis skills reference more external documentation than other skill types

??? success "Answer"
    **B) Analysis skills must read all the artifacts they evaluate into context before scoring — for a 12-chapter textbook this could mean loading 80,000+ tokens of content just to apply the rubric**

    The read-heavy nature of analysis skills creates unique token efficiency challenges. To evaluate a textbook's quality, the skill must read the textbook — potentially tens of thousands of tokens of chapter content, MicroSim files, and glossary. This is unavoidable for thorough analysis but must be designed carefully. Strategies include reading chapter summaries rather than full text when possible, processing chapters sequentially rather than all at once, and focusing scoring on specific criteria that can be assessed from targeted reads rather than complete content loading.

---

**Question 5** *(Bloom's: Analyze)*
*Concept: Content gap identification (C166)*

A book metrics generator reports that 3 of the 17 chapters have no associated MicroSim, 2 chapters are below the minimum word count threshold, and the glossary has 12 undefined terms. How should this analysis skill report these findings?

- [ ] A) Report only the overall composite score without itemizing the gaps
- [ ] B) Provide a structured gap report listing each finding with the specific chapter or term affected, the severity, and a recommended action — then present this to the user before any writing or modification occurs
- [ ] C) Automatically fix all gaps before presenting the report to the user
- [ ] D) Report the findings and immediately begin revising the affected chapters without user confirmation

??? success "Answer"
    **B) Provide a structured gap report listing each finding with the specific chapter or term affected, the severity, and a recommended action — then present this to the user before any writing or modification occurs**

    An analysis skill's output is a structured assessment — not a repair action. The gap report must be specific: which 3 chapters lack MicroSims (not just "3 chapters"), which 2 chapters are below word count (by how much), which 12 glossary terms are undefined (the exact terms). Actionable specificity is what makes the report useful. The report is presented to the user before any modifications — the analysis skill evaluates; it does not automatically fix. Repair actions belong in separate workflow steps or separate skills, triggered by user decision.

---
