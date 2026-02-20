# Chapter 12 Quiz

Test your understanding of data format skills, the data.json pattern, and Python helper integration.

---

**Question 1** *(Bloom's: Remember)*
*Concept: Scripts directory pattern (C150)*

Where should Python helper scripts used by a data format skill be stored?

- [ ] A) In `~/.claude/scripts/` alongside the global skill directory
- [ ] B) In the skill's own directory alongside the SKILL.md file, typically in a `scripts/` subdirectory
- [ ] C) In `/usr/local/bin/` so they are globally executable
- [ ] D) Inline within the SKILL.md as embedded code blocks

??? success "Answer"
    **B) In the skill's own directory alongside the SKILL.md file, typically in a `scripts/` subdirectory**

    The scripts directory pattern places Python helpers inside the skill's folder structure. This keeps the skill self-contained — the SKILL.md, its helper scripts, and any supporting files travel together. The skill invokes these helpers using a relative path from the skill directory. Storing scripts globally or in system paths creates fragile dependencies that break when the skill is shared or installed on a different machine. Self-contained skills are portable and installable.

---

**Question 2** *(Bloom's: Understand)*
*Concept: Learning graph as data artifact (C147)*

What distinguishes a data format skill's primary deliverable from that of a code generation skill?

- [ ] A) Data format skills produce larger files than code generation skills
- [ ] B) Data format skills produce data artifacts (structured files that reshape or transform information) rather than executable programs or narrative text
- [ ] C) Data format skills require Python; code generation skills do not
- [ ] D) Data format skills cannot be used in pipelines; they only work in isolation

??? success "Answer"
    **B) Data format skills produce data artifacts (structured files that reshape or transform information) rather than executable programs or narrative text**

    The defining characteristic of a data format skill is that its primary deliverable is a data artifact — a JSON file, a normalized CSV, a metadata schema, a structured learning graph. The content going in and coming out is largely the same information; the skill's value is in reshaping it for a specific consumer. This contrasts with code generation skills (which produce executable programs) and analysis skills (which produce evaluative reports). The distinction matters because data format output validation is deterministic: a schema check replaces subjective quality judgment.

---

**Question 3** *(Bloom's: Apply)*
*Concept: Python helper script integration (C149)*

A data format skill needs to normalize column names in a CSV file (converting spaces to underscores, lowercasing everything). Why is a Python helper script preferred over asking Claude to do this transformation in its context window?

- [ ] A) Python scripts run faster than Claude's reasoning
- [ ] B) A Python script applies the transformation deterministically and identically every time, while Claude's in-context normalization may produce inconsistent results across invocations
- [ ] C) Claude cannot read CSV files directly
- [ ] D) Python helper scripts are required by the agentskills.io specification for all data skills

??? success "Answer"
    **B) A Python script applies the transformation deterministically and identically every time, while Claude's in-context normalization may produce inconsistent results across invocations**

    Data format skills benefit from Python helpers for exactly the same reason skills benefit over ad-hoc prompting: determinism. Parsing CSVs, validating JSON schemas, and normalizing strings are tasks where a five-line Python script is more reliable than prompting Claude to do it in its head. The script produces the same output for the same input every time — a property that in-context reasoning cannot guarantee. This makes the skill's output more predictable, testable, and debuggable.

---

**Question 4** *(Bloom's: Understand)*
*Concept: Data format transformation skill (C145)*

The `data.json` pattern used by data format skills achieves which key architectural goal?

- [ ] A) It reduces file size by compressing data before storage
- [ ] B) It separates data from rendering logic, allowing the data to be regenerated without touching the visualization code
- [ ] C) It provides a standard format that all Claude Code skills must use for output
- [ ] D) It enables multiple users to share a single data file simultaneously

??? success "Answer"
    **B) It separates data from rendering logic, allowing the data to be regenerated without touching the visualization code**

    The `data.json` pattern reflects a separation of concerns principle. A MicroSim or visualization reads its configuration and data from `data.json` at initialization. This separation means a data format skill can update the data — regenerating it with new survey results, corrected values, or a different time range — without modifying the visualization JavaScript. The rendering code stays stable; only the data layer changes. This is particularly valuable in textbook workflows where data may be updated multiple times without wanting to rewrite the interactive component.

---

**Question 5** *(Bloom's: Apply)*
*Concept: Metadata schema skill (C148)*

A skill produces a `metadata.json` file alongside its primary output. What is the role of this metadata file?

- [ ] A) It stores the skill's quality score from the most recent invocation
- [ ] B) It provides structured, machine-readable description of the primary output — including its type, version, creation date, and schema — enabling downstream tools and skills to validate and consume it correctly
- [ ] C) It contains the skill's YAML frontmatter in JSON format for cross-platform compatibility
- [ ] D) It logs the user's session interactions for analytics purposes

??? success "Answer"
    **B) It provides structured, machine-readable description of the primary output — including its type, version, creation date, and schema — enabling downstream tools and skills to validate and consume it correctly**

    A metadata schema file describes the artifact it accompanies. For a MicroSim, it might include the simulation type, the concept illustrated, the library used (p5.js, Chart.js), the expected canvas dimensions, and the data ranges. This makes the artifact self-describing: a downstream skill or tool can read the metadata to understand what it has received before attempting to consume it. Metadata files are a cornerstone of reliable handoffs in multi-skill pipelines.

---
