# Glossary

Definitions follow the [ISO 11179](https://en.wikipedia.org/wiki/ISO/IEC_11179) metadata registry standard: precise, concise, distinct, non-circular, and free of business rules.

---

**Agent Skill**
:   A directory containing a SKILL.md file and optional supporting resources that teaches an AI agent how to perform a specific task through structured instructions.

**Activation**
:   The process by which an agent loads a skill's full SKILL.md body into context after determining relevance from the skill's description.

**allowed-tools**
:   An optional YAML frontmatter field specifying which tools a skill is permitted to use during execution. Experimental.

**Assets Directory**
:   An optional `assets/` subdirectory within a skill containing static files used in output — templates, images, schemas, fonts.

**Bloom's Taxonomy**
:   A six-level classification of cognitive objectives (Remember, Understand, Apply, Analyze, Evaluate, Create) used to design learning outcomes and quality scoring rubrics.

**Checkpoint**
:   A designated point in a multi-skill pipeline where execution pauses for user review before proceeding to the next stage.

**Context Window**
:   The maximum number of tokens an AI model can process in a single session, shared across system prompt, conversation history, skill instructions, and generated output.

**DAG (Directed Acyclic Graph)**
:   A graph structure where edges have direction and no cycles exist. Used for learning concept dependencies and skill pipeline ordering.

**Description Field**
:   The required YAML frontmatter field (max 1,024 characters) that tells agents what a skill does and when to use it. Loaded into the skill registry at session start.

**Discovery**
:   The startup phase where an agent scans skill directories and loads only the name and description of each available skill into its registry.

**Frontmatter**
:   The YAML metadata block at the top of a SKILL.md file, delimited by `---`, containing required fields (`name`, `description`) and optional fields (`license`, `compatibility`, `metadata`, `allowed-tools`).

**ISO 11179**
:   An international standard for metadata registries that defines five qualities of good definitions: precise, concise, distinct, non-circular, and free of business rules.

**Lazy Loading**
:   A token efficiency pattern where reference documents are read into context only when a specific workflow step requires them, rather than at skill activation.

**MCP (Model Context Protocol)**
:   An open protocol that tells agents what tools exist and how to call them. Complementary to skills: MCP provides tool discovery, skills provide workflow knowledge.

**Meta-Skill**
:   A skill that routes requests to one of several sub-skills based on keyword matching. Uses a `references/` directory containing guide files for each variant.

**MicroSim**
:   An interactive browser-based simulation built with JavaScript libraries (p5.js, Chart.js, vis-network) for educational visualization.

**Name Field**
:   The required YAML frontmatter field (max 64 characters) that identifies a skill. Must be lowercase with hyphens only and match the parent directory name.

**Pipeline**
:   A sequence of skills executed in dependency order where each skill's output serves as the next skill's input.

**Progressive Disclosure**
:   The three-tier architecture for managing skill token costs: Tier 1 metadata (~100 tokens) loaded always, Tier 2 instructions (<5,000 tokens) loaded on activation, Tier 3 resources loaded on demand.

**Quality Gate**
:   A threshold-based checkpoint within a skill where output is scored against a rubric and execution continues only if the score meets the minimum (typically 70-85 out of 100).

**Quality Scoring Rubric**
:   A structured evaluation framework within a skill that decomposes output quality into weighted criteria summing to 100 points, with defined thresholds for proceed/stop decisions.

**References Directory**
:   An optional `references/` subdirectory within a skill containing documentation that agents load on demand during execution.

**Routing Table**
:   A mapping within a meta-skill that associates keywords or request patterns with specific reference guide files in the `references/` directory.

**Scripts Directory**
:   An optional `scripts/` subdirectory within a skill containing executable code (Python, Bash, JavaScript) that agents run during workflow steps.

**Session Logging**
:   The practice of writing structured log files to a `logs/` directory recording timing, files created, quality scores, and decisions made — enabling cross-session continuity.

**Skill Collection**
:   A repository containing multiple related skills packaged together with a shared install script and documentation.

**Skill Registry**
:   The in-memory index an agent builds at startup from all available skill names and descriptions, used to match incoming requests to relevant skills.

**SKILL.md**
:   The required markdown file defining a skill's metadata, instructions, and workflow. Contains YAML frontmatter followed by structured markdown content.

**Skip-if-Complete**
:   A token efficiency pattern where a workflow step checks for existing output before executing, avoiding redundant work when resuming from a prior session.

**Step 0**
:   The conventional first step in a skill workflow dedicated to environment setup — detecting project context, validating prerequisites, and prompting for missing information.

**System Prompt Budget**
:   The portion of the context window allocated to system-level instructions, including all loaded skill descriptions. The 30-skill limit exists to keep this budget manageable.

**30-Skill Limit**
:   The maximum number of skills that can be loaded into a single Claude Code session, determined by the system prompt token budget.

**Token Efficiency**
:   The practice of minimizing unnecessary token consumption within skills through progressive disclosure, lazy loading, skip-if-complete detection, and concise instruction writing.

**User Dialog Trigger**
:   A condition defined within a skill workflow that causes the agent to pause and ask the user a question before proceeding — typically at quality gates, destructive actions, or ambiguous decision points.

**Workflow Step**
:   A numbered section within a SKILL.md body containing specific instructions for one logical unit of work within the skill's execution sequence.
