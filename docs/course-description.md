# Course Description

## Title

Custom Skill Developer: Building Autonomous Agents for Claude Code

## Audience

Intermediate to advanced users of Claude Code who want to extend its capabilities by creating custom skills — autonomous agent definitions that Claude executes step-by-step to accomplish complex, repeatable tasks. Readers should be comfortable with markdown, YAML, and basic command-line operations. No traditional programming experience is required; this guide is designed for AI-first builders who work at the speed of thought.

## Prerequisites

- Working installation of Claude Code CLI
- Familiarity with markdown syntax
- Basic understanding of YAML configuration files
- A GitHub account for publishing and distribution
- Experience using at least 2-3 existing Claude Code skills

## Course Summary

This knowledge base teaches you to design, build, test, and deploy custom Claude Code skills. Skills are markdown-defined autonomous agents that give Claude structured workflows, quality standards, and domain expertise. You will learn the complete skill anatomy — from YAML frontmatter and trigger conditions to multi-step workflows with quality scoring rubrics. The guide covers advanced patterns including meta-skill routers (which consolidate multiple sub-skills under one entry point to work within Claude Code's 30-skill limit), token-efficient lazy loading, session logging for continuity across context windows, and pipeline orchestration where skills chain together in dependency order. By the end, you will be able to create production-quality skills for any domain and distribute them to other Claude Code users.

## Topics Covered

1. **Skill Fundamentals** — What skills are, how Claude Code loads and executes them, the relationship between skills and the system prompt
2. **The Skill Ecosystem** — Surveying existing skill categories (book generation, analysis, specialized), understanding the 30-skill limit, skill discovery mechanisms
3. **Building Your First Skill** — Creating a minimal SKILL.md, testing it locally, iterating on behavior
4. **SKILL.md Deep Dive** — Complete anatomy of the skill definition file: frontmatter schema, section conventions, step numbering
5. **YAML Frontmatter** — The `name`, `description`, `license`, and `allowed-tools` fields; how descriptions appear in Claude's system prompt
6. **Workflow Design** — Step 0 environment setup, sequential vs. parallel steps, user dialog triggers, conditional branching, error handling
7. **Quality Scoring Systems** — Designing 1-100 point rubrics, weighted sub-categories, threshold-based proceed/stop logic, quality gates
8. **Meta-Skill Routing** — Consolidating related skills under a router, keyword-based routing tables, the `references/` directory pattern, decision trees for ambiguous requests
9. **Token Efficiency** — Lazy loading of reference documents, tiered information retrieval (MCP → shell → file read), skip-if-complete detection, minimal context strategies
10. **Session Logging** — Writing structured session logs, enabling cross-session continuity, log format conventions, state tracking with JSON files
11. **Pipeline Orchestration** — Chaining skills in dependency order, checkpoint patterns, the 12-step intelligent textbook pipeline as a case study
12. **Data Format Skills** — Skills that transform data (CSV → JSON, learning graphs, metadata schemas), working with Python helper scripts
13. **Code Generation Skills** — Skills that produce executable code (MicroSims, scripts, configurations), template patterns, output validation
14. **Analysis & Validation Skills** — Skills that score, audit, or report on content quality, DAG validation, metrics generation
15. **Installation & Registry** — Global vs. project-local installation, symlink patterns, the skill listing system, MCP server integration
16. **Testing & Debugging** — Manual testing workflows, common failure modes, debugging skill behavior, iteration strategies
17. **Publishing & Distribution** — Packaging skills for sharing, GitHub-based distribution, versioning conventions, documentation requirements

## Learning Outcomes (Bloom's Taxonomy)

By completing this knowledge base, learners will be able to:

- **Remember**: Identify the required components of a SKILL.md file and list the standard sections
- **Understand**: Explain how Claude Code discovers, loads, and executes skill definitions during a session
- **Apply**: Create a complete, functional skill that follows all conventions and passes quality validation
- **Analyze**: Diagnose why a skill is not behaving as expected by tracing execution through its workflow steps
- **Evaluate**: Assess whether a skill design is token-efficient, maintainable, and follows best practices using the quality scoring framework
- **Create**: Design and publish a meta-skill router that consolidates multiple related sub-skills with lazy-loaded reference documents

## Estimated Scope

- 17 chapters across 5 sections
- ~200 concepts in the learning dependency graph
- Target reading level: professional/technical (accessible to non-engineers who build with AI)
- Interactive elements: MicroSims for skill workflow visualization, routing decision trees, quality score calculators
