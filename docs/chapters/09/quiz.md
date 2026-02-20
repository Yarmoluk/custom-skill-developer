# Chapter 9 Quiz

Test your understanding of token efficiency design and tiered information retrieval.

---

**Question 1** *(Bloom's: Remember)*
*Concept: Tier 1 metadata (C103)*

In the tiered information retrieval pattern, what is Tier 1 and when is it loaded?

- [ ] A) Full SKILL.md content, loaded when the skill is invoked
- [ ] B) Skill name, description, and invocation syntax — always loaded at session start as part of the skill registry
- [ ] C) Reference guides for variant workflows, loaded only when that variant is selected
- [ ] D) Python helper scripts and external data files, loaded only when explicitly requested

??? success "Answer"
    **B) Skill name, description, and invocation syntax — always loaded at session start as part of the skill registry**

    Tier 1 is the metadata that is always present — the skill's name and description injected into the system prompt at session start. This is unavoidable and unconditional. Tier 2 is the full SKILL.md instructions, loaded when the skill is actually activated. Tier 3 is additional resources (reference guides, data files) loaded on demand during execution. The tiered model ensures that the token cost for detail is deferred until that detail is actually needed, keeping base session overhead minimal.

---

**Question 2** *(Bloom's: Remember)*
*Concept: Tier 3 resources (C105)*

Tier 3 resources in the tiered retrieval pattern are best described as:

- [ ] A) Resources loaded unconditionally at skill activation
- [ ] B) The YAML frontmatter fields read at session start
- [ ] C) Files, guides, or data loaded on demand during execution — only when a specific workflow branch requires them
- [ ] D) Log files written after skill completion

??? success "Answer"
    **C) Files, guides, or data loaded on demand during execution — only when a specific workflow branch requires them**

    Tier 3 includes reference guides, data files, and any supplementary resources that are only relevant to a specific execution path. For a meta-skill, this means the variant's reference guide is Tier 3 — it is loaded only after routing determines which variant to run. For any skill, external data files or large examples belong in Tier 3. Loading Tier 3 resources unconditionally (the anti-pattern) wastes the token budget on content that may never be needed for a given invocation.

---

**Question 3** *(Bloom's: Understand)*
*Concept: Context window competition (C110)*

Why does skill design need to account for token efficiency?

- [ ] A) Claude charges per token, so efficiency reduces costs
- [ ] B) The context window is shared among the system prompt, skill definitions, conversation history, and generated output — bloated skills reduce how long the session can run before context fills
- [ ] C) Token limits apply only to the system prompt, not to conversation content
- [ ] D) Claude processes skills faster when they contain fewer tokens

??? success "Answer"
    **B) The context window is shared among the system prompt, skill definitions, conversation history, and generated output — bloated skills reduce how long the session can run before context fills**

    The context window is a shared, finite resource. Every token in a skill definition is unavailable for conversation history, file reads, and Claude's generated output. In a pipeline session invoking multiple skills sequentially, an extra 6,000 tokens per skill adds 48,000 tokens of overhead — enough to meaningfully shorten how long the session runs before context fills and the user must compact or restart. Token efficiency is not about saving money; it is about maximizing useful work per session.

---

**Question 4** *(Bloom's: Apply)*
*Concept: Skip-if-complete detection (C106)*

A chapter-writing skill processes chapters 1-12 sequentially and writes each to disk. If the session ends after chapter 7, how should a skip-if-complete detection pattern enable resumption?

- [ ] A) The skill re-runs all 12 chapters from the start to ensure consistency
- [ ] B) At the start of each chapter step, the skill checks whether the output file already exists and is non-empty; if it does, the step is skipped and the skill proceeds to the next chapter
- [ ] C) The skill asks the user to specify which chapter to start from
- [ ] D) The skill deletes all completed chapters and starts fresh to avoid conflicts

??? success "Answer"
    **B) At the start of each chapter step, the skill checks whether the output file already exists and is non-empty; if it does, the step is skipped and the skill proceeds to the next chapter**

    Skip-if-complete detection checks for the presence of an expected output file before executing a step. If the file exists and is non-empty, the step was completed in a prior session and can be safely skipped. This pattern makes skills idempotent with respect to completed work — running the skill again after a partial completion picks up where it left off rather than redoing or overwriting completed work. Combined with a state file, this enables precise resumption after any interruption.

---

**Question 5** *(Bloom's: Apply)*
*Concept: MCP-first retrieval order (C108)*

What is the token-efficient order for retrieving skill information when Claude needs to know what skills are available?

- [ ] A) Load all SKILL.md files first, then check the MCP registry
- [ ] B) Read all reference guides first, then load the relevant SKILL.md
- [ ] C) Check MCP server metadata first (minimal tokens), then load the SKILL.md only when the skill is activated, then load reference guides only when a specific branch requires them
- [ ] D) Load the most recently used skill first, regardless of the user's request

??? success "Answer"
    **C) Check MCP server metadata first (minimal tokens), then load the SKILL.md only when the skill is activated, then load reference guides only when a specific branch requires them**

    MCP-first retrieval follows the tiered model: Tier 0 (MCP metadata, ~0 tokens) for skill discovery, Tier 1/2 (SKILL.md, 800-4,000 tokens) only on activation, Tier 3 (reference guides, 500-1,200 tokens each) only when a specific variant is needed. This ordering ensures Claude never pays the token cost for skill detail it does not need for a given session. Loading all reference guides at activation — even when only one will be used — is the anti-pattern that wastes 3,000-8,000 tokens unconditionally.

---
