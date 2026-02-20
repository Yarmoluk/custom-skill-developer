# Custom Skill Developer Guide

A comprehensive knowledge base for building custom Claude Code skills — from single-purpose agents to meta-skill routers and full pipeline orchestration.

## What You'll Learn

Skills are the most powerful extension mechanism in Claude Code. They transform Claude from a general-purpose assistant into a domain expert that follows structured workflows, enforces quality standards, and produces consistent, production-quality output every time.

This guide teaches you to build them from scratch.

## Who This Is For

You already use Claude Code and existing skills. Now you want to create your own — whether that's a skill for your specific domain, a meta-skill that routes to multiple sub-skills, or a full pipeline that chains skills together in dependency order.

No traditional programming background required. If you can write markdown and think in systems, you can build skills.

## Guide Structure

| Section | Chapters | What You'll Build |
|---------|----------|-------------------|
| **Foundations** | 1-3 | Your first working skill |
| **Skill Anatomy** | 4-7 | Production-quality skill definitions with quality scoring |
| **Advanced Patterns** | 8-11 | Meta-skill routers, token-efficient designs, pipelines |
| **Specialized Skills** | 12-14 | Data transformation, code generation, and analysis skills |
| **Deployment** | 15-17 | Installation, testing, and distribution to other users |

## The Skill Architecture at a Glance

```
~/.claude/skills/
├── my-skill/
│   └── SKILL.md          ← The skill definition (markdown + YAML)
├── my-meta-skill/
│   ├── SKILL.md           ← Router logic
│   └── references/        ← Sub-skill guides (lazy-loaded)
│       ├── variant-a-guide.md
│       └── variant-b-guide.md
└── ...
```

Every skill is a markdown file. Claude reads it, follows the workflow, and produces structured output. That simplicity is what makes the system powerful — and extensible.

## Get Started

Head to [Chapter 1: What Are Claude Code Skills?](chapters/01/index.md) to begin.
