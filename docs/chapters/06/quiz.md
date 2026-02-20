# Chapter 6 Quiz

Test your understanding of workflow design principles for reliable skill execution.

---

**Question 1** *(Bloom's: Remember)*
*Concept: Step 0 environment setup pattern (C048)*

What is the primary function of Step 0 in a skill workflow?

- [ ] A) To display the skill's version number and exit if the version is outdated
- [ ] B) To establish the filesystem context — project root, working paths, and environment verification — that all subsequent steps depend on
- [ ] C) To ask the user the first clarifying question before any work begins
- [ ] D) To run the quality scoring rubric before generating any output

??? success "Answer"
    **B) To establish the filesystem context — project root, working paths, and environment verification — that all subsequent steps depend on**

    Step 0 is always the first step in any well-designed skill workflow and always named "Setup" or "Environment Setup." Its three jobs are: announcing the skill name and version (confirming the correct skill loaded), detecting the project root (so all subsequent file paths are correct), and verifying prerequisites exist (so the skill fails loudly at the start rather than mid-execution on bad data). Without Step 0, every file path reference in subsequent steps is a potential failure point.

---

**Question 2** *(Bloom's: Understand)*
*Concept: User dialog trigger definition (C050)*

A user dialog trigger is best described as:

- [ ] A) A keyword the user types to activate a specific workflow branch
- [ ] B) An explicit instruction in the skill body telling Claude to pause execution and ask the user a specific question before proceeding
- [ ] C) A system event that fires when the context window is nearly full
- [ ] D) An automated response generated when the quality score falls below threshold

??? success "Answer"
    **B) An explicit instruction in the skill body telling Claude to pause execution and ask the user a specific question before proceeding**

    User dialog triggers are how skills remain collaborative rather than fully autonomous. They are written as explicit instructions like "Ask the user: '...'" followed by "Wait for user response before proceeding to Step N." Skills use dialog triggers strategically: before irreversible actions (file overwrites), when only the user can provide needed information (version numbers, scope decisions), and after presenting a plan that requires approval. The trigger must specify the exact question and must include the instruction to wait.

---

**Question 3** *(Bloom's: Apply)*
*Concept: Explicit pause instruction (C051)*

A skill's Step 3 asks the user for a version number. Which step definition correctly implements a user dialog trigger?

- [ ] A) "Step 3: The user should provide a version number at this point."
- [ ] B) "Step 3: Ask the user: 'What version number should I use? Press Enter for Unreleased.' Wait for the user response before proceeding to Step 4."
- [ ] C) "Step 3: If the user wants to specify a version, they can do so here."
- [ ] D) "Step 3: Infer the version from recent git tags automatically."

??? success "Answer"
    **B) "Step 3: Ask the user: 'What version number should I use? Press Enter for Unreleased.' Wait for the user response before proceeding to Step 4."**

    A correctly implemented dialog trigger has three components: the instruction for Claude to ask ("Ask the user:"), the exact question text in quotes, and an explicit pause instruction ("Wait for the user response before proceeding"). Option A tells the user what to do, not Claude. Option C is optional and imprecise. Option D avoids the dialog entirely by auto-detecting. Only Option B gives Claude an unambiguous instruction to pause, present a specific question, and wait before continuing.

---

**Question 4** *(Bloom's: Apply)*
*Concept: Conditional logic in steps (C053, C054)*

A changelog skill should run `git log` automatically if git is available, but ask the user to describe changes manually if git is not available. Which step structure correctly implements this?

- [ ] A) "Step 2: Run git log. If it fails, the skill is complete."
- [ ] B) "Step 2: Ask the user whether they want to use git or describe changes manually."
- [ ] C) "Step 2: Run `git log --oneline --since='30 days ago' --no-merges`. If git is not available, ask: 'Please describe the changes, one per line.' Wait for user response. If git IS available, proceed automatically to Step 3."
- [ ] D) "Step 2: Check if git is installed. If yes, stop and tell the user to run git log themselves."

??? success "Answer"
    **C) "Step 2: Run `git log --oneline --since='30 days ago' --no-merges`. If git is not available, ask: 'Please describe the changes, one per line.' Wait for user response. If git IS available, proceed automatically to Step 3."**

    Conditional logic in skill steps requires explicit branching: the step specifies what to do in each case (git available vs. not available), including when to pause for user input and when to proceed automatically. Option A fails silently. Option B asks the user to make a technical decision they may not need to make. Option D delegates the work back to the user entirely. The correct implementation handles both branches explicitly and specifies the automatic-proceed condition.

---

**Question 5** *(Bloom's: Analyze)*
*Concept: Sequential vs parallel steps (C058)*

When should a skill explicitly instruct Claude to run steps in parallel rather than sequentially?

- [ ] A) Always — parallel execution is always faster and preferable
- [ ] B) Never — sequential is the only reliable execution model for skills
- [ ] C) When two or more steps are genuinely independent (neither depends on the other's output) and parallelism would meaningfully reduce total execution time
- [ ] D) Only when the skill has more than 10 steps total

??? success "Answer"
    **C) When two or more steps are genuinely independent (neither depends on the other's output) and parallelism would meaningfully reduce total execution time**

    Sequential execution is the default because it is predictable and debuggable. Parallel execution is appropriate only when steps are genuinely independent — neither step needs the other's output to complete. For example, in a textbook pipeline, generating chapters and writing MicroSim specifications from the same outline can be parallelized because neither depends on the other. If a dependency exists between steps, parallelizing them risks starting a step on incomplete or absent inputs.

---
