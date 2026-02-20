# References

Curated references organized by chapter. Each entry includes a relevance note explaining why it matters for skill development.

---

## Foundational Reading

These sources provide the intellectual and technical foundation for the Agent Skills ecosystem.

### Dario Amodei

**[Machines of Loving Grace: How AI Could Transform the World for the Better](https://www.darioamodei.com/essay/machines-of-loving-grace)**
Dario Amodei, October 2024

A 14,000-word vision of how powerful AI compresses decades of scientific, economic, and governance progress into years. The essay's core argument — that AI systems become exponentially more valuable when they can be specialized for domains while maintaining general reasoning — is the philosophical foundation for why skills exist. Skills are the mechanism by which a general-purpose model becomes a domain expert.

**[The Adolescence of Technology: Confronting and Overcoming the Risks of Powerful AI](https://www.darioamodei.com/essay/the-adolescence-of-technology)**
Dario Amodei, January 2026

The sequel to "Machines of Loving Grace" catalogs five civilization-level risks from powerful AI and proposes concrete countermeasures. Relevant to skill development because it frames the safety argument for structured, quality-gated agent behavior — skills constrain AI output to validated workflows rather than unbounded generation.

---

## The Agent Skills Standard

### Anthropic Official

**[Introducing Agent Skills](https://www.anthropic.com/news/skills)**
Anthropic, October 2025 (updated December 2025)

The official product announcement for Agent Skills. Explains the product vision: skills as "onboarding guides" that transform a general-purpose agent into a domain specialist. Covers Claude.ai, Claude Code, the Agent SDK, and API integration.

**[Equipping Agents for the Real World with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)**
Barry Zhang, Keith Lazuka, Mahesh Murag — Anthropic Engineering, October 2025

The technical deep-dive into the skills architecture. Covers the SKILL.md format, progressive disclosure (the 3-tier token model), bundled scripts, security considerations, and the relationship between Skills and MCP. **This is the most important technical reference for skill developers.**

**[Agent Skills Open Standard Specification](https://agentskills.io)**
Anthropic, December 2025

The formal specification for the Agent Skills format. Defines frontmatter requirements (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`), directory structure (`scripts/`, `references/`, `assets/`), progressive disclosure model, and validation rules. Cross-platform: Claude Code, Claude.ai, VS Code, Cursor, OpenAI Codex, Gemini CLI, and 20+ platforms.

**[Agent Skills Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)**
Anthropic

Official documentation for using and creating skills. Covers installation, configuration, and authoring best practices.

**[Agent Skills Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)**
Anthropic

Anthropic's official authoring guidance for writing effective skills — conciseness, degrees of freedom, progressive disclosure, and common patterns.

### Community Analysis

**[Agent Skills: Anthropic's Next Bid to Define AI Standards](https://thenewstack.io/agent-skills-anthropics-next-bid-to-define-ai-standards/)**
The New Stack

Strategic analysis of how Agent Skills parallels MCP as an industry standard play. Frames skills as the "what to do" complement to MCP's "what tools exist."

**[Agent Skills — Simon Willison](https://simonwillison.net/2025/Dec/19/agent-skills/)**
Simon Willison, December 2025

Technical breakdown of the open standard release. Willison's analysis is consistently the most precise technical commentary in the AI ecosystem.

---

## By Chapter

### Chapters 1-3: Foundations

| Reference | Relevance |
|-----------|-----------|
| [Agent Skills Specification](https://agentskills.io/specification) | The formal format definition — required reading for all skill authors |
| [Anthropic Skills Repository](https://github.com/anthropics/skills) | Official example skills demonstrating patterns across creative, technical, and enterprise domains |
| [What Are Skills?](https://agentskills.io/what-are-skills) | The conceptual overview — discovery, activation, execution model |
| [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code/overview) | How Claude Code discovers and loads skills at session start |

### Chapters 4-7: Skill Anatomy

| Reference | Relevance |
|-----------|-----------|
| [SKILL.md Format Specification](https://agentskills.io/specification#skillmd-format) | Frontmatter field constraints, body content guidelines, validation rules |
| [Skill Creator — Anthropic](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | Anthropic's own meta-skill for creating skills — demonstrates anatomy best practices |
| [Bloom's Taxonomy (2001 Revision)](https://en.wikipedia.org/wiki/Bloom%27s_taxonomy) | The six cognitive levels (Remember through Create) used in quality scoring rubric design |
| [ISO 11179 Metadata Registry Standard](https://en.wikipedia.org/wiki/ISO/IEC_11179) | The standard for precise, concise, distinct, non-circular definitions — used in glossary and rubric design |

### Chapters 8-11: Advanced Patterns

| Reference | Relevance |
|-----------|-----------|
| [Progressive Disclosure in Skills](https://agentskills.io/specification#progressive-disclosure) | The 3-tier token model: metadata (~100 tokens), instructions (<5,000 tokens), resources (as needed) |
| [MCP — Model Context Protocol](https://modelcontextprotocol.io/) | The complementary protocol to skills — MCP provides tool discovery, skills provide workflow knowledge |
| [Dan McCreary — Intelligent Textbook Methodology](https://dmccreary.github.io/claude-skills/) | The 12-step pipeline that demonstrated multi-skill orchestration at scale (19 skills, 200+ concepts per textbook) |
| [Directed Acyclic Graphs — Wikipedia](https://en.wikipedia.org/wiki/Directed_acyclic_graph) | The data structure underlying learning graphs, dependency chains, and pipeline orchestration |

### Chapters 12-14: Specialized Skills

| Reference | Relevance |
|-----------|-----------|
| [vis-network.js Documentation](https://visjs.github.io/vis-network/docs/network/) | The library used for learning graph visualization in data format skills |
| [Chart.js Documentation](https://www.chartjs.org/docs/latest/) | The charting library used in code generation skills for data visualization MicroSims |
| [p5.js Reference](https://p5js.org/reference/) | The creative coding library used for interactive simulation MicroSims |
| [JSON Schema Specification](https://json-schema.org/) | Used for metadata validation in analysis and code generation skills |

### Chapters 15-17: Deployment

| Reference | Relevance |
|-----------|-----------|
| [Integrate Skills into Your Agent](https://agentskills.io/integrate-skills) | How to build a skills-compatible client — the integration specification |
| [skills-ref Validation Library](https://github.com/agentskills/agentskills/tree/main/skills-ref) | The official validation tool: `skills-ref validate ./my-skill` |
| [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) | The recommended license for open-source skills (used by Anthropic's own skills) |
| [Semantic Versioning 2.0.0](https://semver.org/) | The versioning standard for published skill collections |

---

## Industry Context

| Reference | Relevance |
|-----------|-----------|
| [Anthropic Opens Agent Skills Standard — Unite.AI](https://www.unite.ai/anthropic-opens-agent-skills-standard-continuing-its-pattern-of-building-industry-infrastructure/) | Analysis of Anthropic's pattern of publishing open standards (MCP, then Skills) as industry infrastructure |
| [Anthropic Launches Enterprise Agent Skills — VentureBeat](https://venturebeat.com/technology/anthropic-launches-enterprise-agent-skills-and-opens-the-standard) | Enterprise adoption angle and competitive positioning against OpenAI |
| [GitHub Copilot Skills Support](https://docs.github.com/en/copilot) | Microsoft/GitHub adoption of the Agent Skills standard in Copilot and VS Code |
| [MkDocs Material Documentation](https://squidfundingmaterial.io/) | The documentation framework used throughout this guide and the intelligent textbook methodology |
