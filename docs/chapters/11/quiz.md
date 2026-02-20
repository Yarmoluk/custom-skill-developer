# Chapter 11 Quiz

Test your understanding of pipeline orchestration, dependency graphs, and checkpoint design.

---

**Question 1** *(Bloom's: Remember)*
*Concept: Directed Acyclic Graph (C128)*

In the context of pipeline orchestration, what does DAG stand for and what does it represent?

- [ ] A) Dynamic Agent Gateway — a routing mechanism for skill invocations
- [ ] B) Directed Acyclic Graph — a structure where pipeline stages are nodes and dependency relationships are edges, with no circular dependencies
- [ ] C) Data Aggregation Grid — a pattern for collecting outputs from parallel stages
- [ ] D) Deployment Automation Guide — a document describing how to publish a pipeline

??? success "Answer"
    **B) Directed Acyclic Graph — a structure where pipeline stages are nodes and dependency relationships are edges, with no circular dependencies**

    A DAG (Directed Acyclic Graph) is the dependency model for pipelines. Each stage is a node; each "must complete before this can start" relationship is a directed edge. The acyclic constraint means no stage can depend on itself — no circular prerequisite chains. Drawing the DAG before writing any skill definitions reveals which stages can be parallelized (independent nodes), which are on the critical path (chains with no parallel alternatives), and whether any circular dependencies exist that would make the pipeline impossible to execute.

---

**Question 2** *(Bloom's: Understand)*
*Concept: File contract definition (C138)*

What is a "file contract" in the context of pipeline orchestration?

- [ ] A) A legal agreement about how skill output files may be distributed
- [ ] B) An agreement between pipeline stages specifying what files a stage produces (output contract) and what files it expects to receive (input contract), including paths and formats
- [ ] C) A configuration file that lists all pipeline stages and their dependencies
- [ ] D) The quality scoring rubric applied to files produced by each pipeline stage

??? success "Answer"
    **B) An agreement between pipeline stages specifying what files a stage produces (output contract) and what files it expects to receive (input contract), including paths and formats**

    File contracts are the handoff mechanism between pipeline stages. Each skill defines two contracts in its SKILL.md: what files it expects as input (paths, formats, required vs. optional) and what files it produces as output (paths, formats, which downstream stages consume them). When the output contract of Stage N exactly matches the input contract of Stage N+1, the handoff is automatic. Mismatches between contracts — a file path off by one character, a JSON schema that evolved — are the primary source of pipeline failures.

---

**Question 3** *(Bloom's: Understand)*
*Concept: Checkpoint design principles (C133)*

What distinguishes a checkpoint from a general user dialog trigger in a pipeline?

- [ ] A) Checkpoints are optional suggestions; dialog triggers are mandatory pauses
- [ ] B) Checkpoints are hard stops at deliberate pipeline decision points where Claude presents completed work and waits for explicit user approval before proceeding — the pipeline will not advance without that approval
- [ ] C) Checkpoints are automated quality gates; dialog triggers require human input
- [ ] D) Checkpoints only occur at the beginning and end of a pipeline; dialog triggers occur within individual steps

??? success "Answer"
    **B) Checkpoints are hard stops at deliberate pipeline decision points where Claude presents completed work and waits for explicit user approval before proceeding — the pipeline will not advance without that approval**

    Checkpoints in a pipeline context are stronger than ordinary dialog triggers. They are deliberate pauses at high-leverage decision points — where approval gates large amounts of downstream work, at irreversibility boundaries, after quality validation, and before expensive steps. The pipeline will not advance to the next stage until the user explicitly approves (e.g., types "approve"). This is not a suggestion or an FYI — it is a hard stop enforced by the skill definition. The 12-step textbook pipeline has 5 mandatory checkpoints.

---

**Question 4** *(Bloom's: Apply)*
*Concept: Prerequisite detection in pipeline (C125)*

A chapter-writer skill (Step 5) depends on `chapter-outline.md` and `definitions.md` from earlier steps. How should prerequisite detection be implemented?

- [ ] A) Trust that prior steps completed successfully and begin writing chapters immediately
- [ ] B) Attempt to generate substitute content if either file is missing
- [ ] C) Check that both files exist and are non-empty at the start of Step 5; if either is missing, halt immediately and report specifically which file is missing and which earlier step must be completed first
- [ ] D) Ask the user to confirm that the files exist before beginning

??? success "Answer"
    **C) Check that both files exist and are non-empty at the start of Step 5; if either is missing, halt immediately and report specifically which file is missing and which earlier step must be completed first**

    Prerequisite detection follows the "fail loudly and specifically" principle. The check should verify file existence and basic validity (read first 100 words to confirm non-empty). If a prerequisite is missing, the skill halts immediately with a specific error: "Step 5 (chapter-writer) cannot start: `definitions.md` is missing. Complete Step 4 first." A skill that attempts to generate substitute content for a missing prerequisite produces subtly wrong output that is harder to debug than an explicit failure.

---

**Question 5** *(Bloom's: Evaluate)*
*Concept: Monolithic orchestrator anti-pattern (C142)*

A developer builds a `textbook-pipeline` skill that contains the full workflow logic for all 12 steps directly in its SKILL.md. What is wrong with this design?

- [ ] A) Nothing — having all logic in one file makes the pipeline easier to maintain
- [ ] B) It violates the 30-skill limit since pipelines count as multiple skills
- [ ] C) It creates a monolithic orchestrator anti-pattern: the SKILL.md becomes enormous, individual steps cannot be tested or updated independently, and the token cost of loading all step logic unconditionally defeats the composability benefits of the pipeline design
- [ ] D) Orchestrators are not permitted by the agentskills.io specification

??? success "Answer"
    **C) It creates a monolithic orchestrator anti-pattern: the SKILL.md becomes enormous, individual steps cannot be tested or updated independently, and the token cost of loading all step logic unconditionally defeats the composability benefits of the pipeline design**

    The correct orchestrator design separates concerns: the orchestrator's SKILL.md contains the pipeline definition (which steps exist, their order, dependencies, checkpoint positions) — not the execution logic for any individual step. Each step's logic lives in its own skill. This allows individual steps to be updated, tested, or replaced without touching the orchestrator. It also means only the orchestrator's compact pipeline definition is loaded into context — each step's detail is only loaded when that step executes.

---
