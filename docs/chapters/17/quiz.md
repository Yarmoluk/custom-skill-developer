# Chapter 17 Quiz

Test your understanding of publishing, distribution, versioning, and skill collection structure.

---

**Question 1** *(Bloom's: Remember)*
*Concept: GitHub-based skill distribution (C196)*

What is the primary distribution mechanism for published Claude Code skills?

- [ ] A) A centralized marketplace at skills.claude.ai
- [ ] B) GitHub repositories containing the skill with an install script that creates symlinks
- [ ] C) The agentskills.io package registry, analogous to npm for Node.js
- [ ] D) Direct email distribution of SKILL.md files to interested users

??? success "Answer"
    **B) GitHub repositories containing the skill with an install script that creates symlinks**

    There is no central registry or marketplace for Claude Code skills. The primary distribution mechanism is GitHub: a repository containing the skill files, an `install.sh` script that creates the symlinks to `~/.claude/skills/`, and an `uninstall.sh` that removes them. Discovery happens through personal recommendation, GitHub search, community lists, and references in textbooks and tutorials. This decentralized model means the README and repository description are the primary means of communicating what a skill does and why to install it.

---

**Question 2** *(Bloom's: Understand)*
*Concept: Semantic versioning for skills (C198)*

Why should published skills use semantic versioning (e.g., `1.2.3`), and what do the three numbers represent?

- [ ] A) Semantic versioning is required by GitHub for all repositories; the numbers represent year, month, and day
- [ ] B) Semantic versioning communicates compatibility: MAJOR (breaking changes), MINOR (new features, backward compatible), PATCH (bug fixes, backward compatible) — helping users understand whether an update requires reviewing their workflows
- [ ] C) The three numbers represent quality score tiers: below 70, 70-85, and above 85
- [ ] D) Semantic versioning is optional for skills since there is no registry enforcing standards

??? success "Answer"
    **B) Semantic versioning communicates compatibility: MAJOR (breaking changes), MINOR (new features, backward compatible), PATCH (bug fixes, backward compatible) — helping users understand whether an update requires reviewing their workflows**

    Semantic versioning communicates the impact of an update without requiring users to read the full changelog. MAJOR version bumps signal that the skill's behavior has changed in ways that may break existing workflows — users should review before updating. MINOR bumps add new capabilities without breaking existing ones. PATCH bumps fix bugs. For skills in a pipeline, this matters: a MAJOR update to a stage skill might require updating the file contracts with other stages. Versioning makes these implications explicit.

---

**Question 3** *(Bloom's: Remember)*
*Concept: Skill documentation requirements (C199)*

Which file is described as non-optional for a publishable skill and serves as its primary marketing and onboarding document?

- [ ] A) `CHANGELOG.md`
- [ ] B) `CONTRIBUTING.md`
- [ ] C) `README.md`
- [ ] D) `INSTALL.md`

??? success "Answer"
    **C) `README.md`**

    The README is the primary marketing and onboarding document for a published skill. Because there is no central marketplace, discovery and evaluation happen through GitHub. If the README does not clearly communicate what the skill does, who it is for, how to install it, and what it produces, the skill will not be used. A published skill without a complete README is effectively invisible to potential users who find it through search. The README is required — all other documentation files are optional supplements.

---

**Question 4** *(Bloom's: Understand)*
*Concept: Skill collection repository structure (C200)*

What distinguishes a skill collection repository from a single-skill repository?

- [ ] A) Skill collections have more complex YAML frontmatter fields
- [ ] B) A skill collection repository contains multiple related skills organized in a `skills/` subdirectory, with a shared collection-level `install.sh` that creates symlinks for all skills at once
- [ ] C) Skill collections are hosted on a different platform than single-skill repositories
- [ ] D) Skill collections require a database backend to manage skill metadata

??? success "Answer"
    **B) A skill collection repository contains multiple related skills organized in a `skills/` subdirectory, with a shared collection-level `install.sh` that creates symlinks for all skills at once**

    A skill collection repository groups multiple related skills (such as the full `claude-textbook-skills` collection) under a single repository with a shared structure: a `skills/` directory containing one subdirectory per skill, a collection-level `install.sh` that creates symlinks for all skills simultaneously, an `uninstall.sh` that removes them all, and a top-level README describing the collection. Individual skills within a collection may also have per-skill READMEs. The shared install script makes adopting an entire toolkit a single-command operation.

---

**Question 5** *(Bloom's: Apply)*
*Concept: Skill packaging for sharing (C195)*

A developer has built a `book-metrics-generator` skill for personal use. It works well but hardcodes the path `/Users/danielyarmoluk/Documents/textbooks/` in several steps. What must they fix before publishing it?

- [ ] A) Nothing — the hardcoded path is fine as long as other users create the same directory
- [ ] B) Replace all hardcoded absolute paths with relative paths from the working directory, or accept the output directory as a parameter — ensuring the skill works correctly regardless of where the user runs it from
- [ ] C) Add a note in the README asking users to edit the path before installing
- [ ] D) Convert the hardcoded path to a symlink before distributing

??? success "Answer"
    **B) Replace all hardcoded absolute paths with relative paths from the working directory, or accept the output directory as a parameter — ensuring the skill works correctly regardless of where the user runs it from**

    Hardcoded absolute paths are a personal-use anti-pattern that breaks distribution. A skill with `/Users/danielyarmoluk/Documents/textbooks/` embedded in its steps will fail for every user who does not have that exact directory structure. Published skills must use relative paths from the working directory (so the user controls where the skill operates by choosing where to invoke it) or accept path parameters. This is one of the most important transformations between "it works for me" and "it works for anyone."

---
