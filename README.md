# Custom Skill Developer Guide

[![Agent Skills](https://img.shields.io/badge/Agent_Skills-Open_Standard-blue)](https://agentskills.io)
[![MkDocs](https://img.shields.io/badge/MkDocs-Material-526CFE)](https://yarmoluk.github.io/custom-skill-developer/)
[![GitHub Pages](https://img.shields.io/badge/Live_Site-GitHub_Pages-green)](https://yarmoluk.github.io/custom-skill-developer/)
[![License](https://img.shields.io/badge/License-Apache_2.0-orange)](LICENSE)

**The comprehensive guide to building Agent Skills for the [agentskills.io](https://agentskills.io) open standard.**

17 chapters. 55,000+ words. From your first skill to meta-skill routers, quality scoring systems, and multi-skill pipeline orchestration.

> Skills work across Claude Code, Claude.ai, VS Code, Cursor, OpenAI Codex, Gemini CLI, and 20+ AI agent platforms.

## Read the Guide

**[https://yarmoluk.github.io/custom-skill-developer/](https://yarmoluk.github.io/custom-skill-developer/)**

## What You'll Learn

| Section | Chapters | What You'll Build |
|---------|----------|-------------------|
| **Foundations** | 1-3 | Your first working skill — from zero to production |
| **Skill Anatomy** | 4-7 | SKILL.md structure, YAML frontmatter, workflows, quality scoring rubrics |
| **Advanced Patterns** | 8-11 | Meta-skill routers, token efficiency, session logging, pipeline orchestration |
| **Specialized Skills** | 12-14 | Data transformation, code generation, and analysis/validation skills |
| **Deployment** | 15-17 | Installation, testing, debugging, publishing, and distribution |

## Why This Guide Exists

Anthropic launched Agent Skills as an open standard. The format is simple — a folder with a `SKILL.md` file. But building *production-quality* skills that handle edge cases, score output quality, manage tokens efficiently, and chain together in pipelines requires patterns that aren't documented anywhere else.

This guide documents those patterns.

## Key Topics

- **SKILL.md anatomy** — Every section, why it exists, what happens if it's missing
- **Quality scoring systems** — 100-point rubrics with weighted categories and threshold gates
- **Meta-skill routing** — Consolidating 14+ sub-skills under one entry point with keyword-based routing
- **Token efficiency** — Progressive disclosure, lazy loading, skip-if-complete detection
- **Pipeline orchestration** — Chaining skills in dependency order with checkpoint patterns
- **The 30-skill limit** — Strategies for working within Claude Code's constraint

## The Skill Architecture

```
~/.claude/skills/           # or .github/skills/ for the open standard
├── my-skill/
│   └── SKILL.md            ← Frontmatter + workflow instructions
├── my-meta-skill/
│   ├── SKILL.md            ← Router logic
│   └── references/         ← Sub-skill guides (loaded on demand)
│       ├── variant-a.md
│       └── variant-b.md
├── scripts/                ← Optional helper scripts
└── assets/                 ← Optional templates and resources
```

## Related Projects

| Project | What It Does |
|---------|-------------|
| [agentskills.io](https://agentskills.io) | The open standard specification |
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic's example skills (72K+ stars) |
| [cognify-skills](https://github.com/Yarmoluk/cognify-skills) | 20+ production business skills built to the standard |
| [skill-quality-analyzer](https://github.com/Yarmoluk/skill-quality-analyzer) | Audit skills against the spec with a 100-point rubric |

## Built With

- [MkDocs Material](https://squidfundingmaterial.io/) — Documentation framework
- [Agent Skills Standard](https://agentskills.io) — Open format by Anthropic
- [Claude Code](https://claude.ai/code) — AI-powered development

## License

Apache 2.0
