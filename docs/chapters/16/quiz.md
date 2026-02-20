# Chapter 16 Quiz

Test your understanding of testing strategies, debugging patterns, and the fix-the-skill principle.

---

**Question 1** *(Bloom's: Remember)*
*Concept: Separate session testing requirement (C186)*

Why must you start a fresh Claude Code session before testing an edited SKILL.md?

- [ ] A) Each session generates a new API key that gives access to different skill features
- [ ] B) Skills are loaded once at session start — an edited SKILL.md has no effect on a running session; only a new session will load the updated version
- [ ] C) Fresh sessions have higher token limits than continued sessions
- [ ] D) Claude Code clears its skill cache automatically when a new session starts, but only if the session is explicitly ended by the user

??? success "Answer"
    **B) Skills are loaded once at session start — an edited SKILL.md has no effect on a running session; only a new session will load the updated version**

    This is one of the most common sources of confusion in skill development. Skills are discovered and loaded into Claude's context at the moment the session starts. If you edit a SKILL.md while a session is running, the running session continues to use the old version of the skill. You fix the skill, try it again in the same session, and the problem persists — because you are still on the old version. The discipline is: edit the skill, start a new session, then test. Every iteration requires a fresh session.

---

**Question 2** *(Bloom's: Understand)*
*Concept: Manual testing workflow (C185)*

What are the five steps of the manual testing workflow for a skill, in the correct order?

- [ ] A) Write tests → deploy skill → run tests → review output → publish
- [ ] B) Install skill → start fresh session → invoke trigger → observe behavior → edit and repeat
- [ ] C) Read SKILL.md → write test cases → run test cases → fix failures → merge
- [ ] D) Invoke skill → score output → edit SKILL.md → reinstall → invoke again

??? success "Answer"
    **B) Install skill → start fresh session → invoke trigger → observe behavior → edit and repeat**

    The five-step manual testing loop is: (1) Install the skill (or verify symlink is correct), (2) start a fresh session, (3) invoke the exact trigger the skill defines, (4) observe the behavior against what the SKILL.md specifies, and (5) if the behavior diverges, edit the SKILL.md and return to step 2. The order matters: installing before starting the session ensures the new version is loaded. Observing before editing ensures you understand what actually went wrong before attempting a fix.

---

**Question 3** *(Bloom's: Apply)*
*Concept: Conditional branch testing (C187)*

A `changelog-generator` skill has two branches: one for git repositories (auto-proceeds) and one for non-git directories (asks the user for changes manually). What is the minimum set of test cases required to verify both branches?

- [ ] A) One test in a git repository is sufficient since that is the common case
- [ ] B) Two tests: one invocation from a git repository and one invocation from a directory with no git repository
- [ ] C) Ten tests with different git commit histories
- [ ] D) No tests are needed since conditional logic is verified by code review

??? success "Answer"
    **B) Two tests: one invocation from a git repository and one invocation from a directory with no git repository**

    Each distinct branch in a skill's conditional logic requires at least one test case to verify it executes correctly. The `changelog-generator` has exactly two branches based on git availability, so both must be tested. Relying only on the happy-path (git available) leaves the fallback branch untested — a branch that could have a bug causing the skill to fail or behave incorrectly when git is absent. Conditional branch testing is the minimum standard for a skill that has branching logic.

---

**Question 4** *(Bloom's: Evaluate)*
*Concept: Do not compensate with reprompting principle (C192)*

A skill produces output that categorizes a bug fix as "Added" instead of "Fixed." The developer adds "Actually this is a fix, not an addition" in the same session, and Claude corrects the output. What is wrong with this approach?

- [ ] A) Nothing — reprompting is a valid way to improve skill output
- [ ] B) The in-session correction fixes the symptom but not the cause — the next invocation will have the same miscategorization because the SKILL.md still lacks clear categorization criteria; the fix must be in the skill definition
- [ ] C) The developer should have approved the incorrect categorization and filed a bug report with Anthropic
- [ ] D) Reprompting is only valid if it is done within the first three turns of a session

??? success "Answer"
    **B) The in-session correction fixes the symptom but not the cause — the next invocation will have the same miscategorization because the SKILL.md still lacks clear categorization criteria; the fix must be in the skill definition**

    "Do not compensate with reprompting" is a core debugging principle. An in-session correction teaches Claude for the current session only. The next invocation starts fresh from the SKILL.md definition — which still has vague or missing categorization criteria. The correct action is to identify what the SKILL.md lacks (explicit categorization rules mapping commit patterns to sections) and add it there. Fix the skill, not the session. This principle prevents recurring errors from being masked by session-level workarounds.

---

**Question 5** *(Bloom's: Apply)*
*Concept: Quality score trigger testing (C189)*

How should a developer verify that a skill's quality scoring system is working — specifically that it actually blocks delivery when output falls below threshold?

- [ ] A) Read the SKILL.md carefully and trust that the rubric will be applied
- [ ] B) Intentionally introduce a flaw into the generated content (such as including conventional commit prefixes that should have been stripped) and verify that Claude flags this as a gap, reports a below-threshold score, and asks whether to revise before writing the file
- [ ] C) Check that the quality rubric table is formatted correctly in the markdown
- [ ] D) The quality scoring system is automatically verified at installation time by Claude Code

??? success "Answer"
    **B) Intentionally introduce a flaw into the generated content (such as including conventional commit prefixes that should have been stripped) and verify that Claude flags this as a gap, reports a below-threshold score, and asks whether to revise before writing the file**

    Testing the quality scoring system requires deliberately triggering the below-threshold case. A skill that always scores above threshold in testing has never been verified to actually enforce the gate. The technique is to create test conditions where the output will fail specific rubric criteria — an easy method is to ask for a changelog from a history where all commits use conventional commit prefixes, then verify the skill catches the prefix pollution and flags it as a quality gap. This confirms the gate is functional, not just present in the SKILL.md.

---
