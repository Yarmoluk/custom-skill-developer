# Frequently Asked Questions

---

## Getting Started

### What is an Agent Skill?
A skill is a folder containing a `SKILL.md` file — a markdown document with YAML metadata and structured instructions that teaches an AI agent how to perform a specific task. Skills work across Claude Code, Claude.ai, VS Code, Cursor, OpenAI Codex, Gemini CLI, and any platform that supports the [agentskills.io](https://agentskills.io) open standard.

### Do I need to know how to code to build skills?
No. Skills are written in markdown and YAML. If you can write structured text and think in sequences, you can build skills. Some advanced skills include Python scripts, but most production skills are pure markdown.

### How is a skill different from a prompt?
A prompt is ephemeral — it disappears after the conversation. A skill is persistent, structured, quality-gated, and reusable. Skills survive across sessions, enforce standards through scoring rubrics, and produce consistent output every time. See [Chapter 1](chapters/01/index.md) for the full comparison.

### Where do I put my skill files?
Two options:

- **Global**: `~/.claude/skills/my-skill/SKILL.md` — available in every project
- **Project-local**: `.github/skills/my-skill/SKILL.md` — available only in that project (and portable across platforms via the open standard)

---

## Building Skills

### What's the minimum viable skill?
A directory with a single `SKILL.md` file containing YAML frontmatter with `name` and `description`. That's it. See [Chapter 3](chapters/03/index.md) for a step-by-step walkthrough.

```yaml
---
name: my-skill
description: Does X when the user asks for Y.
---

# My Skill

Step 1: Do the thing.
```

### How long should my SKILL.md be?
Under 500 lines. The agentskills.io spec recommends keeping the main file concise and moving detailed reference material to the `references/` directory. The progressive disclosure model means Claude only loads the full SKILL.md when the skill activates — but shorter files mean less context consumed.

### What's the difference between `name` and the H1 title?
The `name` field in frontmatter is machine-readable — Claude uses it for skill discovery and routing. It must be lowercase kebab-case and match the directory name. The H1 title is human-readable — it's what people see when they open the file. They serve different audiences.

### When should I add quality scoring?
Always, if the skill produces deliverable output. Quality scoring turns a skill from "do the thing" into "do the thing and verify it meets standards." Skills without quality gates produce inconsistent results across invocations. See [Chapter 7](chapters/07/index.md) for rubric design patterns.

---

## Advanced Patterns

### What is a meta-skill?
A meta-skill is a router that consolidates multiple related skills under one entry point. Instead of registering 14 separate visualization skills, you register one `microsim-generator` meta-skill that routes to the right sub-skill based on keywords in the request. See [Chapter 8](chapters/08/index.md).

### Why does the 30-skill limit exist?
Every loaded skill's `name` and `description` are injected into the system prompt at session start. With 30 skills averaging ~100 tokens each, that's ~3,000 tokens of the context window consumed before you even send a message. The limit keeps the system prompt budget manageable.

### How do I make skills work across sessions?
Session logging. Write structured logs to a `logs/` directory recording what was completed, what's pending, and the current state. When a new session starts, the skill reads the log and resumes from where it left off. See [Chapter 10](chapters/10/index.md).

### Can skills call other skills?
Not directly. But skills can produce output files that serve as input to other skills — this is pipeline orchestration. The 12-step intelligent textbook pipeline is the canonical example of skills chaining through file contracts. See [Chapter 11](chapters/11/index.md).

---

## Token Efficiency

### How many tokens does a skill cost?
Three tiers:

- **Tier 1 — Always loaded**: ~100 tokens per skill (name + description in the registry)
- **Tier 2 — On activation**: <5,000 tokens (full SKILL.md body)
- **Tier 3 — On demand**: Variable (reference files loaded only when a step needs them)

### What's the most common token efficiency mistake?
Loading everything upfront. New skill authors put all reference material in the main SKILL.md instead of splitting it into `references/` files. A 2,000-line SKILL.md consumes ~8,000 tokens on every activation. Split it into a 200-line SKILL.md + 5 focused reference files, and you'll use ~1,000 tokens on activation plus ~500-800 tokens per reference file loaded on demand.

---

## Deployment

### How do I share skills with others?
Package them in a GitHub repository with an install script. Users clone the repo and run the script, which creates symlinks from the skill directories to their local skill path. See [Chapter 17](chapters/17/index.md).

### What license should I use?
Apache 2.0 is the ecosystem standard — it's what Anthropic uses for their own skills. Use MIT if you want maximum permissiveness. Use a proprietary license if you're selling skill packs commercially.

### Do skills work outside Claude Code?
Yes. The agentskills.io open standard is supported by Claude Code, Claude.ai, VS Code, Cursor, OpenAI Codex, Gemini CLI, and 20+ other platforms. Skills placed in `.github/skills/` follow the cross-platform convention.

---

## This Guide

### Who wrote this?
Daniel Yarmoluk — [GitHub](https://github.com/Yarmoluk) | [LinkedIn](https://linkedin.com/in/danielyarmoluk) | daniel.yarmoluk@gmail.com

Built from the experience of creating 20+ production Agent Skills for business operations as part of the [Cognify](https://github.com/Yarmoluk/cognify-skills) ecosystem.

### Can I contribute?
Yes. The guide is Apache 2.0 licensed. Submit issues or pull requests on [GitHub](https://github.com/Yarmoluk/custom-skill-developer).

### I want custom skills built for my business. How?
Reach out: daniel.yarmoluk@gmail.com
