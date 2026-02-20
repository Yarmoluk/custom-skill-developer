# Chapter 2 Quiz

Test your understanding of the Claude Code skill ecosystem, discovery, and the 30-skill limit.

---

**Question 1** *(Bloom's: Remember)*
*Concept: 30-skill limit (C019)*

What is the maximum number of active skills Claude Code supports at any time?

- [ ] A) 10
- [ ] B) 20
- [ ] C) 30
- [ ] D) Unlimited

??? success "Answer"
    **C) 30**

    Claude Code enforces a hard limit of 30 active skills. This is not an arbitrary policy — it reflects a real constraint in how skills integrate with Claude's context. When Claude Code starts a session, it injects a compact registry of all installed skills into the system prompt. The system prompt has a finite token budget, and beyond 30 skills the overhead becomes significant enough that the limit is enforced.

---

**Question 2** *(Bloom's: Understand)*
*Concept: System prompt budget (C020)*

Why does the 30-skill limit exist, specifically in terms of how skills integrate with Claude's context?

- [ ] A) Claude cannot read more than 30 markdown files simultaneously
- [ ] B) Each skill's name and description is injected into the system prompt at session start, consuming token budget regardless of whether the skill is used
- [ ] C) The Claude Code application only has memory for 30 skill directory paths
- [ ] D) The agentskills.io specification limits all compliant runtimes to 30 skills

??? success "Answer"
    **B) Each skill's name and description is injected into the system prompt at session start, consuming token budget regardless of whether the skill is used**

    The system prompt budget is finite. Every skill registration — the `name` and `description` from the YAML frontmatter — consumes tokens unconditionally. Unlike traditional software where you only pay for what you execute, every registered skill costs context tokens on every session invocation. At 30 moderately detailed descriptions, the registry begins to consume a meaningful fraction of the available system prompt budget. The limit enforces disciplined ecosystem design.

---

**Question 3** *(Bloom's: Understand)*
*Concept: Skill discovery at session start (C021)*

When does Claude Code discover and register available skills?

- [ ] A) Every time the user types a slash command
- [ ] B) Once at session start, by scanning the skill directories
- [ ] C) Continuously in the background during a session
- [ ] D) Only when the user explicitly runs `/skills refresh`

??? success "Answer"
    **B) Once at session start, by scanning the skill directories**

    Claude Code discovers skills by scanning `~/.claude/skills/` and `.claude/skills/` at the very beginning of each session. The resulting registry is built once and used for the duration of the session. A practical consequence: if you install a new skill while a session is running, you must start a new session for it to appear. Editing a SKILL.md mid-session has no effect until the next session.

---

**Question 4** *(Bloom's: Understand)*
*Concept: Description field as routing signal (C034)*

The `description` field in a skill's YAML frontmatter is best described as:

- [ ] A) Documentation for human readers browsing a skill collection
- [ ] B) A routing signal that Claude uses to decide when to invoke the skill
- [ ] C) A free-form notes field with no functional effect
- [ ] D) A summary that is displayed in the terminal after the skill completes

??? success "Answer"
    **B) A routing signal that Claude uses to decide when to invoke the skill**

    The description field is not documentation — it is routing logic. Claude reads the registry of all skill descriptions when it starts a session. When a user describes what they want, Claude matches intent against those descriptions. A description that is vague, too long, or poorly targeted causes Claude to miss invocation opportunities or invoke the skill incorrectly. Short, precise descriptions written from Claude's routing perspective outperform long, comprehensive ones.

---

**Question 5** *(Bloom's: Analyze)*
*Concept: Skill taxonomy (C024)*

A developer has built 6 closely related report-generation skills (executive, technical, sales, operations, compliance, and board). What is the best strategy given the 30-skill limit?

- [ ] A) Keep all 6 as separate skills since they are genuinely different workflows
- [ ] B) Delete 3 of the 6 skills to keep the count manageable
- [ ] C) Consolidate all 6 into a single meta-skill with a routing table, reducing 6 slots to 1
- [ ] D) Convert the skills to system prompts, which have no count limit

??? success "Answer"
    **C) Consolidate all 6 into a single meta-skill with a routing table, reducing 6 slots to 1**

    When multiple related skills share a common user intent but diverge in workflow details, the meta-skill pattern is the correct solution. A single meta-skill with a routing table replaces 6 separate skill registrations with 1, freeing 5 slots for other skills while preserving all 6 workflows. The reference guides for each variant are stored in a `references/` subdirectory and loaded on demand, so their token cost is only incurred when that specific variant is actually needed.

---
