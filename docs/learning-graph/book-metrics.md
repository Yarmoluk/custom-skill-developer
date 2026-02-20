# Book Metrics

Overall quality statistics for the *Custom Skill Developer* guide, generated from a full scan of all 17 chapters, the glossary, FAQ, references, and MicroSim index files.

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total chapters | 17 |
| Total word count (estimated) | ~47,470 |
| Average words per chapter | ~2,792 |
| Total glossary terms | 30 |
| Total FAQ questions | 16 |
| Total MicroSims | 4 |
| Total references cited | 33 |
| Total fenced code blocks (all chapters) | 246 |
| Total Mermaid diagrams | 13 |
| Total tables | 45 |
| Total admonitions (tip, note, warning, example) | 14 |
| External links (chapters + glossary + FAQ + references) | 40 |

---

## Content Coverage by Section

### Chapters (17 total)

The guide spans 17 chapters organized into four parts:

- **Part I — Foundations (Chapters 1–3):** What skills are, how the ecosystem works, and building your first skill from scratch
- **Part II — Skill Anatomy (Chapters 4–7):** SKILL.md structure, YAML frontmatter, workflow design, and quality scoring systems
- **Part III — Advanced Patterns (Chapters 8–11):** Meta-skill routers, token efficiency design, session logging, and pipeline orchestration
- **Part IV — Specialized Skills & Deployment (Chapters 12–17):** Data format skills, code generation skills, analysis and validation skills, installation, testing, and publishing

### Glossary

The glossary defines **30 terms** following [ISO 11179](https://en.wikipedia.org/wiki/ISO/IEC_11179) metadata registry standards — precise, concise, distinct, non-circular, and free of business rules.

### FAQ

The FAQ contains **16 questions** organized across four sections:

- Getting Started (4 questions)
- Building Skills (4 questions)
- Advanced Patterns (4 questions)
- Token Efficiency (2 questions)
- Deployment (3 questions)
- This Guide (3 questions)

### MicroSims (4 total)

| MicroSim | Directory | Purpose |
|----------|-----------|---------|
| Skill Anatomy Explorer | `docs/sims/skill-anatomy-explorer/` | Interactive visualization of SKILL.md components and how they connect |
| Routing Simulator | `docs/sims/routing-decision-tree/` | Simulates how a meta-skill routes requests through a decision tree |
| Quality Score Calculator | `docs/sims/quality-score-calculator/` | Live rubric scoring tool for evaluating skill output quality |
| Cognify Ecosystem Graph | `docs/sims/cognify-ecosystem/` | vis-network graph of the Cognify skill ecosystem and concept relationships |

### References

The references file contains **33 cited works** organized across six sections:

- Foundational Reading (2 Dario Amodei essays)
- The Agent Skills Standard — Anthropic Official (5 sources)
- Community Analysis (2 sources)
- By Chapter tables (Chapters 1–3, 4–7, 8–11, 12–14, 15–17)
- Industry Context (4 sources)

---

## Content Density Metrics

### Code Examples

**246 total fenced code blocks** across all 17 chapters, covering:

- YAML frontmatter examples
- Markdown skill body templates
- Python helper scripts (`transform.py`, `validate_dag.py`, `classify.py`, `validate_schema.py`)
- Bash shell scripts (`install.sh`, `uninstall.sh`, `list-skills.sh`)
- JavaScript (MicroSim templates, smoke test scripts)
- HTML (MicroSim output template)
- JSON (state files, data.json, metadata.json, learning graph format)
- Plain text (directory structures, example session transcripts)

Chapters 6 (Workflow Design) and 5 (YAML Frontmatter) are the most code-intensive with 31 and 22 blocks respectively.

### Mermaid Diagrams (13 total)

| Chapter | Count | Diagram Type |
|---------|-------|--------------|
| 1 | 1 | Skill execution flowchart |
| 2 | 1 | Three-tier skill hierarchy graph |
| 3 | 2 | Iteration loop flowchart |
| 4 | 1 | SKILL.md document structure graph |
| 6 | 2 | Sequential execution graph, Quality gate decision tree |
| 11 | 1 | 12-step textbook pipeline flowchart |
| 12 | 1 | Learning graph data flow |
| 13 | 1 | Multi-pass code generation flowchart |
| 14 | 2 | Analysis skill flowchart, Quality gate in pipeline |
| 15 | 1 | Skill discovery sequence diagram |
| 16 | 1 | Test-iterate-refine loop flowchart |

### Tables (45 total)

Tables are concentrated in chapters covering comparison and reference material — particularly Chapters 7 (Quality Scoring), 10 (Session Logging), 2 (Skill Ecosystem), and 3 (Your First Skill).

### Admonitions (14 total)

| Type | Count | Chapters |
|------|-------|---------|
| `!!! tip` | 5 | 1, 2, 3, 3, 3 |
| `!!! warning` | 4 | 2, 2, 3, 15 |
| `!!! example` | 4 | 1, 2, 3, 3 |
| `!!! note` / other | 1 | (embedded in Ch05 prose) |

Admonitions are concentrated in the early foundational chapters (1–3) and the installation chapter (15), where callouts flag critical constraints like the 30-skill limit and session restart requirements.

### External Links

| Source | Count |
|--------|-------|
| Chapters (all 17) | 2 |
| Glossary | 1 |
| FAQ | 4 |
| References | 33 |
| **Total** | **40** |

---

## How These Metrics Were Generated

This report was produced by the `book-metrics-generator` skill applied to the `custom-skill-developer` repository on **2026-02-20**. Counts are based on:

- **Word counts:** Estimated from line counts with content-density adjustment for markdown files mixing prose and code
- **Code blocks:** Counted as pairs of triple-backtick delimiters (```` ``` ````); each pair = one block
- **Mermaid diagrams:** Counted as occurrences of ` ```mermaid ` opening fences
- **Tables:** Counted as separator rows matching `| --- |` patterns; each separator = one table
- **Admonitions:** Counted as lines beginning with `!!!`
- **External links:** Counted as occurrences of `[text](https?://...)` patterns
- **Glossary terms:** Counted as `**Term**` bold definition headers
- **FAQ questions:** Counted as `### Question` H3 headings
- **References:** Counted as distinct hyperlinked citations in `references.md`
