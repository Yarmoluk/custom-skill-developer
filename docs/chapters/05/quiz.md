# Chapter 5 Quiz

Test your understanding of YAML frontmatter fields and their requirements.

---

**Question 1** *(Bloom's: Remember)*
*Concept: Name field requirement (C028)*

Which of the following is a valid `name` field value for a SKILL.md file?

- [ ] A) `Glossary Generator`
- [ ] B) `glossary_generator`
- [ ] C) `GlossaryGenerator`
- [ ] D) `glossary-generator`

??? success "Answer"
    **D) `glossary-generator`**

    The `name` field must be in kebab-case: all lowercase, words separated by hyphens, no spaces, no underscores, and no special characters. `Glossary Generator` fails because of the space and capital letter. `glossary_generator` fails because underscores are not allowed. `GlossaryGenerator` fails because camelCase is not permitted. Only `glossary-generator` satisfies all kebab-case requirements. A version suffix like `glossary-generator-v2` is also acceptable.

---

**Question 2** *(Bloom's: Remember)*
*Concept: Name-to-directory matching requirement (C035)*

What is the relationship between the `name` field in YAML frontmatter and the directory containing the SKILL.md file?

- [ ] A) They can differ freely — the `name` field takes precedence in all cases
- [ ] B) The directory name must exactly match the `name` field value
- [ ] C) The directory name must be the `name` field value converted to PascalCase
- [ ] D) There is no required relationship; Claude Code uses the filename only

??? success "Answer"
    **B) The directory name must exactly match the `name` field value**

    A mismatch between directory name and the `name` field creates ambiguity in skill resolution and should be treated as a configuration error. If the directory is `~/.claude/skills/readme-generator/`, the `name` field must be `readme-generator`. This convention enables Claude Code to locate skills reliably: it maps the invoked name directly to a directory path. The convention is strict by design — when names diverge, debugging becomes unnecessarily difficult.

---

**Question 3** *(Bloom's: Understand)*
*Concept: Description field importance (C029)*

Why do short, precise descriptions outperform long, comprehensive ones in the frontmatter?

- [ ] A) Claude can only read the first 50 words of any description field
- [ ] B) Short descriptions load faster from disk
- [ ] C) Descriptions appear in the system prompt on every session, making verbose descriptions a recurring token cost that competes with useful context
- [ ] D) Long descriptions confuse Claude's natural language processing

??? success "Answer"
    **C) Descriptions appear in the system prompt on every session, making verbose descriptions a recurring token cost that competes with useful context**

    Every skill description is injected into the system prompt at session start, whether or not the skill is used in that session. A 500-word description wastes far more tokens than a 50-word description — multiplied across every session you run. The token budget is shared among all context components: system prompt, conversation history, file reads, and Claude's output. Bloated descriptions eat into that budget on every invocation, reducing how much useful work the session can accomplish before context fills.

---

**Question 4** *(Bloom's: Remember)*
*Concept: allowed-tools field (C031)*

What does the `allowed-tools` field in YAML frontmatter control?

- [ ] A) The list of Claude Code slash commands the skill can register
- [ ] B) Which filesystem tools Claude is permitted to use during skill execution
- [ ] C) The external APIs the skill can call
- [ ] D) The programming languages the skill can generate code in

??? success "Answer"
    **B) Which filesystem tools Claude is permitted to use during skill execution**

    The `allowed-tools` field enforces tool permissions during skill execution. For example, `allowed-tools: Bash(~/.claude/skills/glossary-generator:*)` restricts Bash execution to the skill's own directory. This is a security boundary: it prevents a skill from running arbitrary shell commands beyond its intended scope. Skills that should not run any shell commands can omit this field or specify a restrictive scope. The field is optional but strongly recommended for skills that execute code.

---

**Question 5** *(Bloom's: Apply)*
*Concept: YAML frontmatter block (C027)*

A developer receives an error that a skill is not recognized by Claude Code. The SKILL.md begins with a blank line before the opening `---`. What is the most likely cause and fix?

- [ ] A) The blank line is fine; the issue must be in the description field
- [ ] B) The opening `---` must be the very first line of the file — removing the blank line will fix the issue
- [ ] C) YAML frontmatter requires exactly one blank line before the opening `---`
- [ ] D) The skill needs to be reinstalled after any file change

??? success "Answer"
    **B) The opening `---` must be the very first line of the file — removing the blank line will fix the issue**

    YAML frontmatter has a strict requirement: the opening `---` must be the very first line of the file — no blank lines, no comments, no byte-order marks before it. Claude Code reads the frontmatter block by detecting this delimiter. A blank line before it causes Claude Code to fail to parse the file as a skill, meaning the skill will not appear in skill listings and cannot be invoked by name. This is one of the most common reasons a new skill fails to load.

---
