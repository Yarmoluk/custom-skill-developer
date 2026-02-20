# Chapter Metrics

Per-chapter content breakdown for the *Custom Skill Developer* guide, generated from a full scan of all 17 chapters.

---

## Per-Chapter Breakdown

| Chapter | Title | Word Count | Code Examples | Diagrams | Tables | Admonitions | Links |
|---------|-------|-----------|--------------|----------|--------|-------------|-------|
| 1 | What Are Claude Code Skills? | ~1,390 | 3 | 1 | 1 | 2 | 1 |
| 2 | The Skill Ecosystem | ~2,010 | 9 | 1 | 4 | 5 | 0 |
| 3 | Your First Skill | ~4,100 | 18 | 1 | 3 | 6 | 1 |
| 4 | SKILL.md Structure | ~3,440 | 18 | 1 | 3 | 0 | 0 |
| 5 | YAML Frontmatter | ~2,280 | 22 | 0 | 3 | 0 | 0 |
| 6 | Workflow Design | ~4,740 | 31 | 2 | 4 | 0 | 0 |
| 7 | Quality Scoring Systems | ~3,170 | 16 | 0 | 6 | 0 | 0 |
| 8 | Meta-Skill Routers | ~2,890 | 10 | 0 | 2 | 0 | 0 |
| 9 | Token Efficiency Design | ~2,120 | 13 | 0 | 2 | 0 | 0 |
| 10 | Session Logging | ~2,580 | 11 | 0 | 6 | 0 | 0 |
| 11 | Pipeline Orchestration | ~2,610 | 10 | 1 | 3 | 0 | 0 |
| 12 | Data Format Skills | ~3,545 | 15 | 1 | 1 | 0 | 0 |
| 13 | Code Generation Skills | ~3,400 | 16 | 1 | 0 | 0 | 0 |
| 14 | Analysis and Validation Skills | ~3,290 | 9 | 2 | 2 | 0 | 0 |
| 15 | Installation and Registry | ~2,735 | 14 | 1 | 1 | 1 | 0 |
| 16 | Testing and Debugging | ~1,945 | 11 | 1 | 1 | 0 | 0 |
| 17 | Publishing and Distribution | ~3,225 | 20 | 0 | 3 | 0 | 0 |
| **Totals** | | **~47,470** | **246** | **13** | **45** | **14** | **2** |

---

## Column Definitions

| Column | Definition |
|--------|------------|
| **Word Count** | Estimated from line count with content-density adjustment for mixed prose and code markdown |
| **Code Examples** | Count of fenced code blocks (each opening+closing ``` pair = one block) |
| **Diagrams** | Count of Mermaid diagram blocks (` ```mermaid ` opening fences) |
| **Tables** | Count of distinct tables, identified by separator rows matching `| --- |` patterns |
| **Admonitions** | Count of lines beginning with `!!!` (tip, note, warning, example callouts) |
| **Links** | Count of inline external hyperlinks matching `[text](https?://...)` pattern |

---

## Notable Patterns

### Most Code-Intensive Chapters

| Rank | Chapter | Code Examples |
|------|---------|--------------|
| 1 | Chapter 6 — Workflow Design | 31 |
| 2 | Chapter 5 — YAML Frontmatter | 22 |
| 3 | Chapter 17 — Publishing and Distribution | 20 |
| 4 | Chapter 3 — Your First Skill | 18 |
| 4 | Chapter 4 — SKILL.md Structure | 18 |

Chapter 6 and 5 are the most code-dense because they cover the technical specification of skill structure — every rule is illustrated with a concrete YAML or markdown code block.

### Most Table-Intensive Chapters

| Rank | Chapter | Tables |
|------|---------|--------|
| 1 | Chapter 7 — Quality Scoring Systems | 6 |
| 1 | Chapter 10 — Session Logging | 6 |
| 3 | Chapter 2 — The Skill Ecosystem | 4 |
| 3 | Chapter 6 — Workflow Design | 4 |

Chapters 7 and 10 lead in tables because they cover reference-heavy material — rubric criteria, scoring thresholds, and log schema specifications that are naturally expressed in tabular form.

### Admonition Distribution

Admonitions (tip, warning, note, example callouts) are concentrated in the early foundational chapters:

| Chapter | Admonitions |
|---------|-------------|
| Chapter 3 — Your First Skill | 6 |
| Chapter 2 — The Skill Ecosystem | 5 |
| Chapter 1 — What Are Claude Code Skills? | 2 |
| Chapter 15 — Installation and Registry | 1 |

Chapters 1–3 use admonitions heavily to flag critical constraints for new readers (the 30-skill limit, session restart requirements, minimum viable skill format). Chapters 4–17 rely on structured prose and code blocks instead.

### Longest Chapters by Word Count

| Rank | Chapter | Word Count |
|------|---------|-----------|
| 1 | Chapter 6 — Workflow Design | ~4,740 |
| 2 | Chapter 3 — Your First Skill | ~4,100 |
| 3 | Chapter 4 — SKILL.md Structure | ~3,440 |
| 4 | Chapter 13 — Code Generation Skills | ~3,400 |
| 5 | Chapter 12 — Data Format Skills | ~3,545 |

### Shortest Chapters by Word Count

| Rank | Chapter | Word Count |
|------|---------|-----------|
| 1 | Chapter 1 — What Are Claude Code Skills? | ~1,390 |
| 2 | Chapter 16 — Testing and Debugging | ~1,945 |
| 3 | Chapter 2 — The Skill Ecosystem | ~2,010 |

Chapter 1 is intentionally lean — it establishes vocabulary and mental models without overwhelming new readers. Chapter 16 is concise because testing methodology is demonstrated through practical walkthroughs rather than extended explanation.

---

## Part Summary

| Part | Chapters | Total Words | Total Code Examples | Total Diagrams |
|------|----------|------------|--------------------|----|
| Part I — Foundations | 1–3 | ~7,500 | 30 | 3 |
| Part II — Skill Anatomy | 4–7 | ~13,630 | 87 | 3 |
| Part III — Advanced Patterns | 8–11 | ~10,200 | 44 | 1 |
| Part IV — Specialized Skills & Deployment | 12–17 | ~18,140 | 85 | 6 |

Part II (Skill Anatomy) is the most code-intensive section, covering the detailed technical specification of SKILL.md structure, YAML frontmatter, workflow design, and quality scoring. Part IV is the longest by word count, spanning six chapters across specialized skill types and the full deployment lifecycle.

---

## How These Metrics Were Generated

This report was produced by the `book-metrics-generator` skill applied to the `custom-skill-developer` repository on **2026-02-20**. All counts use the same methodology as `book-metrics.md`:

- **Word counts:** Estimated from non-empty line counts with a content-density multiplier (~8 words per line for markdown with mixed prose and code)
- **Code blocks:** Counted as pairs of triple-backtick delimiters; each pair = one block
- **Mermaid diagrams:** Counted as occurrences of ` ```mermaid ` opening fences
- **Tables:** Counted as separator rows matching `| --- |` patterns; each separator = one table
- **Admonitions:** Counted as lines beginning with `!!!`
- **External links:** Counted as occurrences of `[text](https?://...)` patterns within chapter files only
