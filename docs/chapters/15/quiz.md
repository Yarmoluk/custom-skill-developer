# Chapter 15 Quiz

Test your understanding of skill installation, registry, and the 30-skill limit management.

---

**Question 1** *(Bloom's: Remember)*
*Concept: Global installation path (C168)*

What is the global installation path for Claude Code skills that makes them available across all projects?

- [ ] A) `/usr/local/share/claude/skills/`
- [ ] B) `~/.claude/skills/`
- [ ] C) `./skills/` in the current working directory
- [ ] D) `~/.config/claude/global-skills/`

??? success "Answer"
    **B) `~/.claude/skills/`**

    The global installation path is `~/.claude/skills/`. Skills installed here are available in every Claude Code session, regardless of which project directory the session starts from. This is appropriate for general-purpose utilities, skills used across multiple projects, and skills that belong to your personal workflow rather than a specific project. The tilde (`~`) expands to the user's home directory, making the path consistent across operating systems.

---

**Question 2** *(Bloom's: Remember)*
*Concept: /skills command listing (C176)*

What command lists all currently installed and available skills in a Claude Code session?

- [ ] A) `/list`
- [ ] B) `/skills`
- [ ] C) `/help skills`
- [ ] D) `/catalog`

??? success "Answer"
    **B) `/skills`**

    The `/skills` command triggers Claude Code to display all skills currently registered in its skill catalog — the skills discovered at session start from both the global and project-local paths. Running `/skills` after installing a new skill (in a new session) is the standard verification step to confirm the skill loaded correctly and with the expected name. If a skill does not appear in the `/skills` output, it was either not discovered (path issue) or has malformed frontmatter.

---

**Question 3** *(Bloom's: Understand)*
*Concept: Discovery order (C170)*

A project has both a global `~/.claude/skills/book-metrics/SKILL.md` and a project-local `.claude/skills/book-metrics/SKILL.md`. Which version does Claude Code use?

- [ ] A) The global version, because global always takes precedence
- [ ] B) The project-local version, because project-local overrides global when names match
- [ ] C) Both versions are loaded and Claude picks the better one
- [ ] D) Claude Code throws an error when two skills have the same name

??? success "Answer"
    **B) The project-local version, because project-local overrides global when names match**

    Project-local skills take precedence over global skills with the same name. This override behavior is intentional and useful: it allows a project to use a customized version of a general-purpose skill without modifying the global installation. For example, a textbook project might need a project-specific `book-metrics` skill configured for its particular chapter structure, while other projects continue using the standard global version.

---

**Question 4** *(Bloom's: Understand)*
*Concept: Symlink installation pattern (C171)*

Why is the symlink pattern preferred over copying SKILL.md files to the installation directory?

- [ ] A) Symlinks are smaller files and consume less disk space
- [ ] B) With a symlink, editing the source file in the development repository immediately updates the installed version — there is no separate copy to keep in sync
- [ ] C) Claude Code only reads symlinks, not regular files, for security reasons
- [ ] D) Symlinks enable multiple users to share the same skill installation simultaneously

??? success "Answer"
    **B) With a symlink, editing the source file in the development repository immediately updates the installed version — there is no separate copy to keep in sync**

    The symlink pattern creates a symbolic link from the installation directory (`~/.claude/skills/my-skill/`) to the actual skill directory in your development repository. When you edit `SKILL.md` in the development repo, the symlink means the installation directory immediately reflects the change. Without symlinks, a copy-based approach requires manually updating the installation after every edit — a step that is routinely forgotten. The `install.sh` script automates symlink creation; `uninstall.sh` removes it.

---

**Question 5** *(Bloom's: Apply)*
*Concept: Profile-based installation (C181)*

A developer has 45 skills but the limit is 30. They switch between two contexts: textbook production (needs 20 textbook skills) and client consulting (needs 18 consulting skills, with 8 overlapping the textbook set). What is the most effective management strategy?

- [ ] A) Delete 15 skills permanently to get under the limit
- [ ] B) Create two installation profiles with separate install scripts — one for textbook work and one for consulting work — each activating the relevant subset of skills
- [ ] C) Convert all 45 skills into a single giant meta-skill
- [ ] D) Keep all 45 skills installed and accept the limit violation

??? success "Answer"
    **B) Create two installation profiles with separate install scripts — one for textbook work and one for consulting work — each activating the relevant subset of skills**

    Profile-based installation is the strategic response to ecosystem growth beyond the 30-skill limit. An `install-textbook.sh` script creates symlinks for the 20 textbook skills; an `install-consulting.sh` creates symlinks for the 18 consulting skills. Switching profiles takes seconds. Skills that are not currently active consume no system prompt tokens. Archiving inactive skills (removing symlinks without deleting source files) is the complementary pattern for less frequently needed skills. Neither approach destroys skills — they simply control which ones are active.

---
