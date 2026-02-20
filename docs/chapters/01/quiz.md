# Chapter 1 Quiz

Test your understanding of what Claude Code skills are and how they work.

---

**Question 1** *(Bloom's: Remember)*
*Concept: Claude Code skill definition (C001)*

A Claude Code skill is defined as which of the following?

- [ ] A) A fine-tuned model variant trained on domain-specific data
- [ ] B) A markdown file named `SKILL.md` that defines an autonomous workflow for Claude to execute
- [ ] C) A saved chat prompt stored in Claude's memory
- [ ] D) A plugin written in JavaScript that extends Claude's capabilities

??? success "Answer"
    **B) A markdown file named `SKILL.md` that defines an autonomous workflow for Claude to execute**

    A Claude Code skill has a precise technical definition: it is a `SKILL.md` file that defines an autonomous workflow. This distinguishes it from saved prompts (stateless), fine-tuned models (alter weights), plugins (require code), and system prompts (global, not composable). The skill lives in the filesystem, persists across sessions, and directs Claude to execute a structured sequence of steps.

---

**Question 2** *(Bloom's: Remember)*
*Concept: Path resolution (C008, C009)*

When Claude Code resolves a skill at invocation time, where does it look for skills? Select the most complete answer.

- [ ] A) Only in `~/.claude/skills/` (global path)
- [ ] B) Only in `.claude/skills/` in the current project
- [ ] C) In `~/.claude/skills/` (global) and `.claude/skills/` (project-local), with project-local taking precedence
- [ ] D) In any directory listed in the `PATH` environment variable

??? success "Answer"
    **C) In `~/.claude/skills/` (global) and `.claude/skills/` (project-local), with project-local taking precedence**

    Claude Code scans two filesystem locations: the global `~/.claude/skills/` (available across all projects) and the project-local `.claude/skills/` relative to the project root. When the same skill name exists in both locations, the project-local version overrides the global one. This two-tier system allows you to have a project-specific version of a skill without affecting your global installation.

---

**Question 3** *(Bloom's: Understand)*
*Concept: Skill persistence (C003)*

Which property of skills most directly distinguishes them from ad-hoc prompting?

- [ ] A) Skills run faster than typed prompts
- [ ] B) Skills persist in the filesystem so they can be invoked repeatedly without rewriting the instructions
- [ ] C) Skills allow Claude to access the internet
- [ ] D) Skills bypass Claude's content policies for trusted users

??? success "Answer"
    **B) Skills persist in the filesystem so they can be invoked repeatedly without rewriting the instructions**

    Persistence is one of the three defining properties of a skill (alongside structure and quality gates). A skill lives at a known path in the filesystem — you write it once and invoke it repeatedly. Ad-hoc prompts disappear when the conversation ends and must be recreated each time. Persistence enables versioning, sharing, and iterative improvement over time.

---

**Question 4** *(Bloom's: Understand)*
*Concept: Standard Operating Procedure analogy (C006)*

The "Standard Operating Procedure (SOP)" analogy helps explain skills because:

- [ ] A) Both SOPs and skills are written in YAML and validated by a computer
- [ ] B) Both define exactly what to do, in what order, with explicit checkpoints — constraining the workflow while the executor applies judgment within it
- [ ] C) Both are used exclusively in medical and legal contexts where precision is mandatory
- [ ] D) Both are stored in a centralized database accessible to all practitioners

??? success "Answer"
    **B) Both define exactly what to do, in what order, with explicit checkpoints — constraining the workflow while the executor applies judgment within it**

    The SOP analogy captures the essence of skill design: a hospital SOP does not say "do surgery well" — it specifies exact steps in exact order with defined checkpoints. Claude Code skills work identically. The skill definition is the SOP; Claude is the executor. The critical nuance is that Claude brings reasoning capability to each step — the skill constrains the workflow, Claude applies judgment within it.

---

**Question 5** *(Bloom's: Apply)*
*Concept: Quality gates property (C005)*

A skill's quality scoring system triggers at the end of execution. A skill produces changelog output that scores 68/100 against its rubric, and the minimum passing score is 75. What should Claude do?

- [ ] A) Deliver the output with a note that the score was below threshold
- [ ] B) Silently discard the output and ask the user to start over
- [ ] C) Present a gap report identifying what fell below threshold and offer to revise before delivering
- [ ] D) Raise the minimum passing score automatically to match the current output

??? success "Answer"
    **C) Present a gap report identifying what fell below threshold and offer to revise before delivering**

    Quality gates are one of the three defining properties of skills. When output scores below the defined threshold, the skill must flag the specific gaps — not silently deliver substandard output, not discard the work entirely, and not adjust the threshold. The gap report gives the user actionable information about what failed and the option to revise before the output is delivered. This self-evaluation mechanism is what separates skills from simple generators.

---
