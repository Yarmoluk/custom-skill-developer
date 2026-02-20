# Chapter 3 Quiz

Test your understanding of building your first skill through iterative stages.

---

**Question 1** *(Bloom's: Remember)*
*Concept: Minimal viable skill (C026)*

What is the minimum content required for Claude Code to recognize a file as a valid skill?

- [ ] A) A complete workflow with at least 3 numbered steps
- [ ] B) A quality scoring rubric and an example session
- [ ] C) Only a valid YAML frontmatter block (no body content required)
- [ ] D) A YAML frontmatter block plus at least an Overview and When to Use section

??? success "Answer"
    **C) Only a valid YAML frontmatter block (no body content required)**

    The minimal viable skill is a `SKILL.md` file containing only valid YAML frontmatter — the `name` and `description` fields are sufficient for Claude Code to register the skill. This is Stage 1 of skill development. However, a minimal viable skill without workflow steps will cause Claude to improvise behavior inconsistently, which is precisely the problem that adding a structured workflow in Stage 2 resolves.

---

**Question 2** *(Bloom's: Understand)*
*Concept: Actionable step specification (C049)*

Which of the following workflow step descriptions is correctly written?

- [ ] A) "Step 1: Get the changes"
- [ ] B) "Step 1: Collect information about the project"
- [ ] C) "Step 1: Run `git log --oneline --since='30 days ago' --no-merges` and parse the output into a list of changes"
- [ ] D) "Step 1: Think about what changed recently"

??? success "Answer"
    **C) "Step 1: Run `git log --oneline --since='30 days ago' --no-merges` and parse the output into a list of changes"**

    A well-written workflow step is actionable — it specifies exactly what Claude should do, not just what the step is about. "Get the changes" and "collect information" are vague descriptions of goals, not executable instructions. "Think about what changed" is entirely non-specific. The correct answer provides the exact command to run and what to do with its output, leaving no ambiguity about what the step requires.

---

**Question 3** *(Bloom's: Apply)*
*Concept: Destructive action confirmation pattern (C052)*

A skill's Step 6 is about to write to an existing `CHANGELOG.md` file. What should the skill do before writing?

- [ ] A) Proceed automatically since the user already invoked the skill
- [ ] B) Display a confirmation prompt asking the user to approve the overwrite before writing
- [ ] C) Create a backup copy silently and then overwrite
- [ ] D) Skip the write step and display the content in the terminal instead

??? success "Answer"
    **B) Display a confirmation prompt asking the user to approve the overwrite before writing**

    The destructive action confirmation pattern is a critical requirement for any skill that writes, overwrites, or deletes files. The user must explicitly confirm before the file is modified. This pattern applies even when the user invoked the skill — invoking the skill is not blanket consent to overwrite existing files. The `changelog-generator` example in Chapter 3 implements this with: "I will prepend the new entry to your existing CHANGELOG.md. Confirm? (y/n)"

---

**Question 4** *(Bloom's: Apply)*
*Concept: Skill iteration loop (C070, C071)*

After invoking a `changelog-generator` skill in two separate sessions, you notice the output format differs between invocations. What should you do?

- [ ] A) Add clarifying instructions during the next session to guide Claude toward the correct format
- [ ] B) Accept the inconsistency as inherent to AI-generated output
- [ ] C) Identify which workflow step is underspecified and edit the SKILL.md to add explicit format instructions, then test in a new session
- [ ] D) Reinstall the skill from scratch

??? success "Answer"
    **C) Identify which workflow step is underspecified and edit the SKILL.md to add explicit format instructions, then test in a new session**

    The observe-compare-edit cycle (iteration loop) is the correct approach. Output format inconsistency is a signal that a workflow step is too vague. The fix belongs in the skill definition, not in a reprompt during the session. Adding in-session clarifications does not fix the root problem — the next invocation will have the same inconsistency. Edit the SKILL.md, start a new session, and verify the fix holds across multiple invocations.

---

**Question 5** *(Bloom's: Evaluate)*
*Concept: Production-readiness checklist (C074)*

A skill builder has completed Stage 4 of development. Which combination of criteria indicates the skill is production-ready?

- [ ] A) The skill has been invoked once successfully and has a quality rubric
- [ ] B) The skill has a complete frontmatter, structured workflow, quality scoring with a minimum threshold, an example session, and has been invoked in at least two separate sessions with consistent output
- [ ] C) The skill has more than 500 lines of content
- [ ] D) The skill has been reviewed by another developer and received positive feedback

??? success "Answer"
    **B) The skill has a complete frontmatter, structured workflow, quality scoring with a minimum threshold, an example session, and has been invoked in at least two separate sessions with consistent output**

    The production-readiness checklist covers three domains: frontmatter completeness (name matches directory, description is routing-ready), structure (overview, when-to-use, numbered steps, conditional logic, confirmation patterns), quality (rubric, minimum score, gap report), documentation (output files, example session, common pitfalls), and testing (two separate invocations, consistent output, branches tested). A single successful invocation does not confirm consistency. The two-session test is the minimum bar for behavioral consistency.

---
