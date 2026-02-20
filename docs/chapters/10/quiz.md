# Chapter 10 Quiz

Test your understanding of session logging, state tracking, and cross-session continuity.

---

**Question 1** *(Bloom's: Remember)*
*Concept: Log directory convention (C116)*

What is the conventional directory and filename format for session logs in the skill ecosystem?

- [ ] A) `~/.claude/logs/[skill-name].log`
- [ ] B) `./logs/[skill-name]-v[VERSION]-[YYYY-MM-DD].md`
- [ ] C) `./output/session-log.txt`
- [ ] D) `./[skill-name]/history.json`

??? success "Answer"
    **B) `./logs/[skill-name]-v[VERSION]-[YYYY-MM-DD].md`**

    The log directory convention places logs in a `logs/` directory relative to the working directory, not in a global location. The filename includes the skill name, version, and date: for example, `./logs/report-generator-v1.2.0-2024-11-15.md`. This convention enables version-specific log filtering, date-based retrieval, and identification of which skill version produced a given log. Logs use `.md` format (not `.json`) for both human and Claude readability without a parser.

---

**Question 2** *(Bloom's: Understand)*
*Concept: Session logging definition (C113)*

Why are session logs described as "external memory that survives context resets"?

- [ ] A) Logs are stored in a cloud database that persists independently of Claude's context
- [ ] B) When a session ends or is compacted, the context is cleared — but log files written to disk remain, allowing the next session to read them and understand prior state without re-doing completed work
- [ ] C) Claude's memory automatically transfers to log files when the context window fills
- [ ] D) Log files are encrypted and can only be read by the same Claude session that created them

??? success "Answer"
    **B) When a session ends or is compacted, the context is cleared — but log files written to disk remain, allowing the next session to read them and understand prior state without re-doing completed work**

    Session logs solve the continuity problem created by context resets. When context fills and Claude Code compacts the session, or when the user starts a fresh session, all in-context memory of what was accomplished is gone. A session log written to disk survives this reset. The next session's first action is a cheap read of the log (~600 tokens for a state file) that immediately communicates what was completed, what is in progress, and what remains — enabling precise resumption rather than starting from scratch.

---

**Question 3** *(Bloom's: Understand)*
*Concept: Cross-session continuity (C115)*

A skill is processing a batch of 20 files. After completing 14, the session ends unexpectedly. What makes cross-session continuity possible for the next session?

- [ ] A) Claude automatically remembers the last session's progress
- [ ] B) The user must manually tell the next session which files were completed
- [ ] C) A state tracking file (such as a JSON status file) written during execution records each file's completion status, enabling the new session to read it and resume from file 15
- [ ] D) The next session re-processes all 20 files and deduplicates the output

??? success "Answer"
    **C) A state tracking file (such as a JSON status file) written during execution records each file's completion status, enabling the new session to read it and resume from file 15**

    State tracking with a structured file (JSON or markdown) is the infrastructure that makes cross-session continuity possible. The skill writes completion status as it processes each item — not only at the end of the entire batch. A `chapter-status.json` or `pipeline-status.json` that records "chapters 1-14: complete, chapter 15: pending" gives the next session everything it needs to resume precisely. Without this file, recovery from mid-batch interruption requires either re-processing everything or manual user intervention.

---

**Question 4** *(Bloom's: Apply)*
*Concept: Resume session pattern (C119)*

What should be the first action when starting a session to resume interrupted work on a multi-chapter skill?

- [ ] A) Ask the user how far they got in the previous session
- [ ] B) Start from the beginning to ensure consistency with prior output
- [ ] C) Read the session log or state file first to determine current state, then proceed from the earliest incomplete step
- [ ] D) Delete the partial output and regenerate everything cleanly

??? success "Answer"
    **C) Read the session log or state file first to determine current state, then proceed from the earliest incomplete step**

    The resume session pattern's first action is always reading the existing state — the log file or status JSON. This single cheap read (typically 200-600 tokens) provides a complete picture of prior work without loading all the generated content. After reading state, the skill identifies the first incomplete step and resumes from there. Asking the user is error-prone (users may not remember exact progress). Starting from scratch wastes the work already done. Re-reading all output files to infer state is expensive and fragile.

---

**Question 5** *(Bloom's: Apply)*
*Concept: State tracking with JSON files (C117)*

A session log entry shows: `"step-05-chapter-writer": { "status": "in_progress", "sub_status": { "complete": 7, "pending": 5 } }`. What does this tell the next session?

- [ ] A) Step 5 failed and needs to be restarted from chapter 1
- [ ] B) Step 5 is partially complete — 7 chapters are done and 5 remain; resume by writing chapter 8 (the first pending chapter)
- [ ] C) Step 5 requires user approval before it can continue
- [ ] D) Step 5 has a quality score of 7 out of 12 possible points

??? success "Answer"
    **B) Step 5 is partially complete — 7 chapters are done and 5 remain; resume by writing chapter 8 (the first pending chapter)**

    The JSON state entry communicates three pieces of information: the step name (step-05-chapter-writer), the overall status (in_progress, meaning it started but did not complete), and the sub-status breakdown (7 complete, 5 pending). The next session can read this in a few hundred tokens and immediately know where to resume — no need to scan all output files or ask the user. This is the core value of structured state files: precise, cheap state reconstruction at the start of any new session.

---
