# Learning Graph: Concept Map Overview

This page documents the complete concept dependency graph for the *Custom Skill Developer* knowledge base. The graph contains **200 concepts** spanning all 17 chapters, organized by category, difficulty, and Bloom's Taxonomy level. Each concept is specific, testable, and linked to its prerequisite concepts via the `dependencies` column in [`concepts.csv`](./concepts.csv).

---

## Concept Inventory Summary

| Metric | Count |
|--------|-------|
| Total concepts | 200 |
| Categories | 12 |
| Difficulty levels | 3 |
| Bloom's levels | 5 |
| Chapters covered | 16 of 17 |

---

## Breakdown by Category

| Category | Concept Count | Description |
|----------|---------------|-------------|
| Pipeline Orchestration | 32 | DAG design, checkpoints, file contracts, state management, orchestrator patterns |
| Meta-Skills | 25 | Routing tables, decision trees, references directory, disambiguation protocols |
| Specialized Skills | 23 | Data format, code generation, analysis, and validation skill types |
| Deployment | 22 | Installation paths, symlink patterns, registry, distribution, versioning |
| Skill Anatomy | 20 | SKILL.md sections, workflow steps, development process, iteration loop |
| Foundations | 17 | Core definitions, execution model, skill categories, background concepts |
| Token Efficiency | 12 | Lazy loading, progressive disclosure, skip-if-complete, tiered retrieval |
| Workflow Design | 11 | Step patterns, branching, user dialog triggers, error handling |
| Quality Systems | 10 | Rubric design, scoring, thresholds, gap reports, pipeline integration |
| Testing | 10 | Manual testing, debugging, branch testing, edge cases |
| Ecosystem | 9 | Skill registry, discovery, 30-skill limit, taxonomy, distribution |
| YAML Specification | 9 | Required and optional frontmatter fields and their constraints |

---

## Breakdown by Difficulty Level

| Difficulty | Concept Count | Coverage |
|------------|---------------|----------|
| Beginner | 46 | Foundational vocabulary, core definitions, first principles |
| Intermediate | 144 | Applied patterns, design decisions, multi-concept integration |
| Advanced | 10 | Pipeline coordination, parallel execution, orchestrator design |

The distribution reflects the knowledge base's audience: intermediate-to-advanced Claude Code users who need precise, actionable knowledge at the applied level.

---

## Breakdown by Bloom's Taxonomy Level

| Bloom's Level | Concept Count | Example Concepts |
|---------------|---------------|------------------|
| Remember | 33 | SKILL.md file format, name field requirement, 30-skill limit |
| Understand | 73 | Skill execution model, meta-skill routing, lazy loading definition |
| Apply | 65 | Routing table construction, quality rubric design, symlink installation |
| Analyze | 15 | Routing failure modes, common skill failure modes, critical path identification |
| Evaluate | 14 | Production-readiness checklist, meta-skill anti-patterns, escape hatch rate |
| Create | 0 | Covered implicitly through applied project work across all chapters |

The heavy concentration at the **understand** and **apply** levels reflects the knowledge base's emphasis on building functional skills over memorizing theory.

---

## Concept Count by Chapter

| Chapter | Title | Concepts |
|---------|-------|----------|
| 1 | What Are Claude Code Skills? | 27 |
| 2 | The Skill Ecosystem | 8 |
| 3 | Your First Skill | 12 |
| 4 | SKILL.md Structure | 12 |
| 5 | YAML Frontmatter | — |
| 6 | Workflow Design | 4 |
| 7 | Quality Scoring Systems | 9 |
| 8 | Meta-Skill Routers | 25 |
| 9 | Token Efficiency Design | 11 |
| 10 | Session Logging | 7 |
| 11 | Pipeline Orchestration | 29 |
| 12 | Data Format Skills | 6 |
| 13 | Code Generation Skills | 9 |
| 14 | Analysis & Validation Skills | 8 |
| 15 | Installation & Registry | 18 |
| 16 | Testing & Debugging | 9 |
| 17 | Publishing & Distribution | 6 |

> Note: YAML Specification concepts (Chapter 5) are attributed to Chapter 1 where they first appear structurally, since frontmatter is introduced with the first SKILL.md definition.

---

## Dependency Graph Structure

Concepts build on each other in a directed acyclic graph (DAG). The root node is `C001: Claude Code skill definition` — all other concepts ultimately depend on it. Key dependency chains:

**Foundations chain:**
`C001 → C002 → C027 → C028/C029/C031` (skill → file → frontmatter → fields)

**Workflow chain:**
`C001 → C007 → C047 → C048/C053 → C055/C056` (skill → execution → steps → patterns → error handling)

**Quality chain:**
`C002 → C043 → C060 → C062/C063 → C065 → C069` (skill → section → rubric → scoring → gate → pipeline gate)

**Meta-skill chain:**
`C001 → C076 → C082 → C083/C087 → C091/C092 → C093` (skill → meta-skill → routing → table/tree → references → lazy loading)

**Pipeline chain:**
`C001 → C121 → C122 → C127 → C128/C133 → C137/C138` (skill → pipeline → stage → DAG → checkpoints → state/contracts)

---

## How to Use This Graph

The CSV file [`concepts.csv`](./concepts.csv) contains the following columns:

| Column | Description |
|--------|-------------|
| `id` | Unique concept identifier (C001–C200) |
| `concept_name` | Human-readable concept label |
| `category` | Top-level category (12 total) |
| `subcategory` | Finer grouping within the category |
| `difficulty_level` | beginner / intermediate / advanced |
| `bloom_level` | remember / understand / apply / analyze / evaluate |
| `dependencies` | Comma-separated list of prerequisite concept IDs |
| `chapter` | Primary chapter where the concept is introduced |

Use this data to:

- **Sequence learning** — follow dependency chains from C001 outward
- **Assess readiness** — verify prerequisite concepts before introducing advanced ones
- **Generate quizzes** — filter by Bloom's level to create targeted assessments
- **Visualize curriculum** — import into graph visualization tools (vis-network, D3.js) using the `id` and `dependencies` columns as edges
- **Identify coverage gaps** — compare chapter concept counts to ensure balanced coverage

---

## Data File

The raw concept data is stored at:

```
docs/learning-graph/concepts.csv
```

The file is UTF-8 encoded, comma-delimited, with a header row. Multi-valued dependency fields use comma-separated values enclosed in double quotes per standard CSV conventions.
