# Skill Anatomy Explorer

Explore the structure of a `SKILL.md` file interactively. Click any section block in the diagram to reveal what that section does, whether it is required, its approximate token cost, and a real example.

<div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center;margin-bottom:1rem;">
  <a href="./main.html" target="_blank" style="display:inline-flex;align-items:center;gap:6px;background:#007AFF;color:#fff;font-size:13px;font-weight:600;padding:8px 16px;border-radius:8px;text-decoration:none;">
    Open Fullscreen
  </a>
  <span style="font-size:13px;color:#8E8E93;">9 sections &nbsp;·&nbsp; 5 required, 4 optional &nbsp;·&nbsp; 3-tier token model</span>
</div>

<iframe
  src="./main.html"
  width="100%"
  height="600px"
  style="border:1px solid #28282D;border-radius:12px;display:block;"
  title="Skill Anatomy Explorer — interactive SKILL.md diagram"
></iframe>

---

## What This Sim Shows

The explorer maps the nine standard sections of a production `SKILL.md` file to a color-coded diagram. Each section is tagged with:

- **Required vs. Optional** — five sections are required for Claude Code to execute a skill reliably; four are best-practice additions
- **Token cost estimate** — the approximate tokens each section contributes to context
- **Type** — whether the section is structural metadata, instructional content, or a quality gate

The file tree in the top-left panel shows where `SKILL.md` lives relative to the other directories in a skill package (`scripts/`, `references/`, `assets/`).

---

## The 3-Tier Token Model

The bottom strip of the sim visualizes the **progressive disclosure** design pattern for skills:

| Tier | When Loaded | What It Contains | Cost |
|------|-------------|------------------|------|
| **Tier 1 — Metadata** | Every session | YAML frontmatter + H1 title | ~100 tokens |
| **Tier 2 — Instructions** | On invocation | Full SKILL.md body | < 5,000 tokens |
| **Tier 3 — Resources** | On demand | Files in `references/` and `assets/` | As needed |

This design keeps skills lightweight in the global skill registry while making full workflow detail available exactly when Claude needs it.

---

## Sections at a Glance

| Section | Color | Required | Tokens |
|---------|-------|----------|--------|
| YAML Frontmatter | Blue | Yes | ~100 |
| H1 Title | White | Yes | ~5 |
| Overview / Purpose | Purple | Yes | ~80 |
| When to Activate | Green | Yes | ~120 |
| Workflow Steps | Orange | Yes | ~1,200 |
| Output Files Summary | Blue | Yes | ~150 |
| Example Session | Purple | No | ~300 |
| Common Pitfalls | Orange | No | ~200 |
| Quality Scoring Rubric | Green | No | ~400 |

!!! tip "Design principle"
    The five required sections are the minimum contract between the skill and Claude Code. The four optional sections are what separate a working skill from a production-quality skill. Add them when the skill will be used by others or invoked frequently.

!!! note "Related"
    Chapter 4 covers the full SKILL.md structure in depth. Chapter 7 covers quality scoring rubric design. Chapter 9 covers token budget management and the progressive disclosure pattern.
