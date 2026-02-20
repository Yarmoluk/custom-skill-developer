# Chapter 4 Quiz

Test your understanding of the complete SKILL.md structure and its sections.

---

**Question 1** *(Bloom's: Remember)*
*Concept: 10-section skill layout convention (C046)*

Which section comes immediately after the Workflow section in a well-structured SKILL.md?

- [ ] A) Common Pitfalls
- [ ] B) Quality Scoring
- [ ] C) Output Files
- [ ] D) Example Session

??? success "Answer"
    **C) Output Files**

    The conventional 10-section SKILL.md layout follows this order: Overview, When to Use This Skill, Workflow, Output Files, Quality Scoring, Example Session, Common Pitfalls (and optionally additional sections). The Output Files section comes directly after the Workflow because it documents what the workflow produces. This ordering is logical: first describe what to do (workflow), then describe what gets created (output files), then describe how to evaluate it (quality scoring).

---

**Question 2** *(Bloom's: Remember)*
*Concept: When to Use section (C037)*

The "When to Use This Skill" section should contain which three types of information?

- [ ] A) Installation instructions, version history, and license information
- [ ] B) Positive trigger conditions, negative trigger conditions (Do NOT use if), and prerequisites
- [ ] C) Workflow steps, quality criteria, and example output
- [ ] D) Author name, contact information, and changelog

??? success "Answer"
    **B) Positive trigger conditions, negative trigger conditions (Do NOT use if), and prerequisites**

    The "When to Use" section serves a routing and gatekeeping function. Positive trigger conditions tell Claude (and the user) when the skill is appropriate. Negative trigger conditions ("Do NOT use if") prevent the skill from being invoked in situations where it would produce incorrect or unhelpful output. Prerequisites specify what must be true before the skill can run successfully. Together, these three components prevent misuse and failed invocations.

---

**Question 3** *(Bloom's: Understand)*
*Concept: Overview section (C036)*

What is the primary purpose of the Overview section in a SKILL.md?

- [ ] A) To provide installation instructions for new users
- [ ] B) To list all YAML frontmatter fields and their values
- [ ] C) To explain the skill's purpose and primary output in 1-2 sentences that help Claude orient to the task
- [ ] D) To document every edge case and exception the skill handles

??? success "Answer"
    **C) To explain the skill's purpose and primary output in 1-2 sentences that help Claude orient to the task**

    The Overview section is the first content Claude reads after the frontmatter. Its job is orientation: what does this skill do, and what does it produce? It should be concise — 1-2 sentences is the target — because Claude needs to understand the skill's scope immediately, not read a paragraph before beginning. The overview is not documentation for humans browsing a catalog; it is the first instruction Claude receives about the purpose of what it is about to execute.

---

**Question 4** *(Bloom's: Apply)*
*Concept: Common Pitfalls section (C045)*

When writing the Common Pitfalls section for a `git-commit-generator` skill, which of the following is the most useful pitfall entry?

- [ ] A) "The skill may not work perfectly every time"
- [ ] B) "Make sure Claude Code is installed correctly before using this skill"
- [ ] C) "Running from a subdirectory: `git status` will show incorrect relative paths. Prevention: The skill's Step 0 runs `git rev-parse --show-toplevel` to verify you are in the repository root."
- [ ] D) "This skill requires the `git` command to be available"

??? success "Answer"
    **C) "Running from a subdirectory: `git status` will show incorrect relative paths. Prevention: The skill's Step 0 runs `git rev-parse --show-toplevel` to verify you are in the repository root."**

    An effective pitfall entry has three components: the specific failure mode (what goes wrong), the condition that triggers it (running from a subdirectory), and the prevention (how the skill already handles it, or how the user should avoid it). Vague warnings like "may not work perfectly" are useless. Generic prerequisites ("requires git") belong in the When to Use section, not pitfalls. A well-written pitfall encodes knowledge that would otherwise require debugging to discover.

---

**Question 5** *(Bloom's: Analyze)*
*Concept: Example Session section (C044)*

A skill builder debates whether to include an Example Session section. What is the strongest argument for including it?

- [ ] A) It increases the skill file's line count, making it look more comprehensive
- [ ] B) It provides an exact behavioral specification: if Claude's actual output matches the example, the skill is working; if there is divergence, the skill definition needs adjustment
- [ ] C) It reduces the need to write detailed workflow steps since the example shows what to do
- [ ] D) It is required by the agentskills.io specification and cannot be omitted

??? success "Answer"
    **B) It provides an exact behavioral specification: if Claude's actual output matches the example, the skill is working; if there is divergence, the skill definition needs adjustment**

    The Example Session section functions as a behavioral contract. It shows exactly what a correct interaction looks like from invocation to completion — what Claude says, what it does, what it outputs, what it asks. During testing, you compare actual behavior against the example session. Divergence signals a gap in the skill definition that needs repair. It is the most concrete tool for verifying skill correctness available to a skill builder.

---
