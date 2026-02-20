# Chapter 8 Quiz

Test your understanding of meta-skill routers, routing tables, and disambiguation protocols.

---

**Question 1** *(Bloom's: Remember)*
*Concept: References directory pattern (C091)*

In a meta-skill directory structure, where do reference guides for each variant live?

- [ ] A) In a separate `~/.claude/references/` global directory
- [ ] B) In a `references/` subdirectory inside the meta-skill's own skill folder
- [ ] C) Embedded directly inside the meta-skill's SKILL.md file
- [ ] D) In the project root alongside `mkdocs.yml`

??? success "Answer"
    **B) In a `references/` subdirectory inside the meta-skill's own skill folder**

    The `references/` directory lives inside the skill folder, for example `~/.claude/skills/report-generator/references/`. Reference guides in this directory are never loaded speculatively — the meta-skill loads exactly one guide corresponding to the routing decision. Files in `references/` do not appear in the skill registry and do not count toward the 30-skill limit. This directory structure is what enables the token efficiency benefit: variant detail is isolated until it is actually needed.

---

**Question 2** *(Bloom's: Understand)*
*Concept: Routing as primary meta-skill job (C077)*

When a meta-skill is invoked, what is its first and primary job?

- [ ] A) To immediately begin producing output using the most common variant
- [ ] B) To ask the user which variant they want before doing anything else
- [ ] C) To analyze the user's request, identify the appropriate sub-skill variant via the routing table, load the corresponding reference guide, and then execute
- [ ] D) To load all reference guides simultaneously so any variant is ready immediately

??? success "Answer"
    **C) To analyze the user's request, identify the appropriate sub-skill variant via the routing table, load the corresponding reference guide, and then execute**

    A meta-skill's primary job is routing, not output generation. It reads the routing table, applies keyword matching and semantic understanding to the user's request, selects the most appropriate variant, and loads only that variant's reference guide. From the user's perspective, they invoked one skill. Under the hood, the meta-skill transparently selected and is now running the right workflow. Loading all reference guides simultaneously is the anti-pattern to avoid — it eliminates the token efficiency benefit entirely.

---

**Question 3** *(Bloom's: Apply)*
*Concept: Synonym coverage in routing table (C084)*

A `report-generator` meta-skill has a routing table where "sales, pipeline, revenue" map to the sales variant. A user asks for a "Q3 ARR breakdown." What should happen, and why?

- [ ] A) The skill should fail to route since "ARR" is not in the keyword list
- [ ] B) The skill should ask the user to rephrase using one of the listed keywords
- [ ] C) The skill should route to the sales variant because "ARR" (Annual Recurring Revenue) is semantically equivalent to revenue context, even though it is not literally in the keyword list
- [ ] D) The skill should default to the executive summary variant as the safest choice

??? success "Answer"
    **C) The skill should route to the sales variant because "ARR" (Annual Recurring Revenue) is semantically equivalent to revenue context, even though it is not literally in the keyword list**

    The routing table functions as a signal vocabulary, not a rigid parser. Claude uses natural language understanding, so routing applies when the concept is clearly present even if the exact word differs. "ARR breakdown" implies a sales/revenue context even without the word "revenue" appearing literally. This is why building comprehensive synonym coverage matters: "ARR," "MRR," "quota," and "pipeline" should all be added to the keyword list to reduce vocabulary mismatch failures.

---

**Question 4** *(Bloom's: Apply)*
*Concept: Escape hatch clarifying question (C089, C090)*

A meta-skill's disambiguation protocol fails to resolve an ambiguous request after working through all decision tree nodes. What should the skill do?

- [ ] A) Default silently to the most common variant without telling the user
- [ ] B) Ask the user up to three clarifying questions to narrow down the correct variant
- [ ] C) Ask the user exactly ONE targeted clarifying question that distinguishes between the remaining candidate variants
- [ ] D) Halt and ask the user to restart with a more specific request

??? success "Answer"
    **C) Ask the user exactly ONE targeted clarifying question that distinguishes between the remaining candidate variants**

    The escape hatch is the final step in the disambiguation protocol when keyword matching and decision tree logic both fail to resolve routing. It is constrained to exactly one clarifying question — not an interview, not multiple rounds. Users who invoke a skill want output, not interrogation. The one-question constraint is a design requirement, not a suggestion. The question should be targeted: "Is this report for leadership review, technical documentation, sales tracking, or operational monitoring?" — directly identifying the distinguishing dimension.

---

**Question 5** *(Bloom's: Evaluate)*
*Concept: Two-variant as conditional not meta-skill (C100)*

A developer is building a `commit-generator` skill that needs two slightly different outputs: one for feature commits and one for fix commits. Should they build a meta-skill?

- [ ] A) Yes — any time there are multiple variants, a meta-skill is the correct pattern
- [ ] B) No — two variants with minor differences should be handled with an if/else conditional block in a single SKILL.md, not a meta-skill
- [ ] C) Yes — because two reference guides are needed to hold the variant specifications
- [ ] D) No — two variants should always be two separate skills for maximum clarity

??? success "Answer"
    **B) No — two variants with minor differences should be handled with an if/else conditional block in a single SKILL.md, not a meta-skill**

    The meta-skill pattern is warranted when you have 3 or more sub-variants that share a common user intent but diverge substantially in workflow steps, and each variant's specification is substantial enough (500+ tokens) to justify lazy loading. Two variants with minor differences are a conditional, not a router. A single SKILL.md with "If the commit is a feature, do X. If it is a fix, do Y" is cleaner and requires less infrastructure than building a full meta-skill with a references directory for just two slight variations.

---
