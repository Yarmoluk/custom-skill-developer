# Chapter 5: YAML Frontmatter

## The Four Fields That Define Every Skill

The YAML frontmatter is the first thing Claude Code reads when it loads a skill. Before executing a single workflow step, before reading the overview, before processing any instruction in the markdown body — Claude reads the four fields in the frontmatter block. Those fields determine whether the skill loads at all, what name it registers under, what permissions it has, and how Claude will describe it when asked about available skills.

This chapter covers each field in depth: what it does mechanically, how it influences Claude's behavior, and the failure modes that result from common mistakes.

---

## The Frontmatter Block Structure

A frontmatter block is valid YAML enclosed between two triple-dash lines at the very start of the file:

```yaml
---
name: skill-name-in-kebab-case
description: Single paragraph describing what the skill does and WHEN to use it.
license: MIT
allowed-tools: Bash(some-path:*)
---
```

**Strict requirements:**

- The opening `---` must be the very first line of the file — no blank lines, no comments, no byte-order marks before it
- The closing `---` must appear on its own line immediately after the last field
- Field names are case-sensitive (`name`, not `Name` or `NAME`)
- Values containing colons, special characters, or line breaks must be quoted or use YAML block scalar syntax

If the frontmatter is malformed, Claude Code will either fail to load the skill entirely or load it with corrupted metadata. There is no graceful degradation — invalid YAML is a hard failure.

---

## Field 1: `name`

### What It Does

The `name` field is the machine identifier for your skill. It is the string users type when invoking the skill, the string that appears in skill registry listings, and the string that must match the directory name containing the SKILL.md file.

```yaml
name: glossary-generator
```

### Format Requirements

The `name` field must be in **kebab-case**: all lowercase, words separated by hyphens, no spaces, no underscores, no special characters.

| Value | Valid? | Reason |
|-------|--------|--------|
| `glossary-generator` | Yes | Correct kebab-case |
| `glossaryGenerator` | No | camelCase not allowed |
| `glossary_generator` | No | Underscores not allowed |
| `Glossary Generator` | No | Spaces not allowed |
| `GLOSSARY-GENERATOR` | No | Must be lowercase |
| `glossary-generator-v2` | Yes | Version suffix acceptable |

### The Name-Directory Relationship

The `name` field must match the directory name that contains the SKILL.md file. If the directory is `~/.claude/skills/readme-generator/`, the `name` field must be `readme-generator`. A mismatch between directory name and `name` field creates ambiguity in skill resolution and should be treated as a configuration error.

```
~/.claude/skills/
├── readme-generator/        ← Directory name
│   └── SKILL.md             ← name: readme-generator (must match)
├── glossary-generator/
│   └── SKILL.md             ← name: glossary-generator (must match)
```

### Choosing a Good Name

A well-chosen skill name communicates what the skill does in two to four words. The noun-verb or verb-noun pattern works best.

```
verb-noun pattern:    generate-glossary, analyze-course, validate-graph
noun-verb pattern:    glossary-generator, course-analyzer, graph-validator
```

The noun-verb pattern (ending in `-er` or `-or`) is more common in the McCreary ecosystem and reads more naturally as a tool name: `glossary-generator`, `readme-generator`, `learning-graph-generator`.

Avoid names that are too generic (`content-creator`, `file-processor`) or that describe the technology rather than the function (`markdown-writer`, `json-builder`). The name should answer "what does it produce?" not "how does it work?"

---

## Field 2: `description`

### What It Does — The System Prompt Connection

The `description` field is more than metadata. When Claude selects or is instructed to use a skill, the description field is injected into Claude's context as part of its operational instructions. It is not merely a label — it is Claude's primary reference for understanding what it is supposed to do and when.

This has a critical implication: **your description is a prompt.** Every word you write in the description field is part of the instructions Claude operates under while executing that skill. Vague descriptions produce vague behavior. Precise descriptions produce precise behavior.

### The Two-Sentence Structure

The most effective descriptions follow a two-sentence structure:

**Sentence 1:** What the skill does (the transformation it performs)
**Sentence 2:** When to use it (the trigger condition)

```yaml
description: This skill automatically generates a comprehensive glossary of terms
  from a learning graph's concept list, ensuring each definition follows ISO 11179
  metadata registry standards (precise, concise, distinct, non-circular, and free
  of business rules). Use this skill when creating a glossary for an intelligent
  textbook after the learning graph concept list has been finalized.
```

Let's break down why this works:

- "automatically generates a comprehensive glossary" — tells Claude the scope and nature of the output
- "from a learning graph's concept list" — specifies the required input
- "ensuring each definition follows ISO 11179 standards" — embeds the quality standard directly
- "Use this skill when creating a glossary for an intelligent textbook after the learning graph concept list has been finalized" — the trigger condition is specific and checkable

### Descriptions as Skill-Selection Signals

When a user asks "which skill should I use to validate my course description?", Claude reads the descriptions of available skills and performs a semantic matching operation. The description with the closest match to the user's stated need wins.

This means your description must contain the vocabulary a user would naturally use when describing their problem. If users will say "I need to check my course description," your description should include phrases like "analyze," "validate," "course description," and "quality check."

```yaml
# Good: contains user-natural vocabulary
description: This skill analyzes or creates course descriptions for intelligent
  textbooks by checking for completeness of required elements (title, audience,
  prerequisites, topics, Bloom's Taxonomy outcomes) and providing quality scores
  with improvement suggestions. Use this skill when working with course descriptions
  in /docs/course-description.md that need validation or creation for learning
  graph generation.

# Bad: describes mechanism instead of user need
description: This skill reads markdown files containing course description data
  and parses their contents to produce a structured JSON report. Use when you
  have a markdown file you want analyzed.
```

The "bad" example fails because it describes what the skill does technically rather than what user problem it solves. A user thinking "I need to check if my course description is complete" will not search for "read markdown files."

### Length Constraints

The description should be one paragraph — typically 50 to 100 words. There is no hard maximum, but descriptions beyond 150 words begin to lose effectiveness for two reasons:

1. **Context window cost**: Long descriptions consume context space that could be used for executing workflow steps.
2. **Trigger precision**: Longer descriptions include more vocabulary, which can cause accidental matching against unrelated user requests.

If you find yourself writing a description longer than 150 words, it is usually a sign that either your skill is doing too many things (consider splitting it) or you are including information that belongs in the Overview section of the markdown body.

### The "Use this skill when..." Clause

Every description should end with a "Use this skill when..." clause. This clause is the trigger condition — the specific circumstances under which this skill is the correct choice.

```
# Too vague — matches everything
Use this skill when you need to generate content.

# Too narrow — misses valid use cases
Use this skill when you have exactly 200 concepts in a file named
02-concept-list-v1.md and your course is on computer science.

# Well-calibrated — specific but not over-specified
Use this skill when creating a glossary for an intelligent textbook
after the learning graph concept list has been finalized.
```

The trigger condition should be specific enough to distinguish this skill from similar skills, but not so narrow that valid use cases are excluded.

### Common Description Mistakes

**Mistake 1: Describing implementation instead of function**

```yaml
# Wrong: tells Claude how the skill works, not what it does for the user
description: This skill uses a multi-step process to iterate through concept labels,
  apply ISO 11179 rules programmatically, and output formatted markdown entries.

# Right: tells Claude what problem it solves
description: This skill generates ISO 11179-compliant glossary definitions for all
  concepts in a learning graph. Use this skill when your textbook needs a glossary
  after the concept list is finalized.
```

**Mistake 2: No trigger condition**

```yaml
# Wrong: no "when to use" signal — Claude cannot distinguish use cases
description: This skill generates glossary definitions for concept lists.

# Right: trigger condition makes selection unambiguous
description: This skill generates glossary definitions for concept lists. Use
  this skill after the learning graph concept list has been reviewed and approved.
```

**Mistake 3: Vague quality claims**

```yaml
# Wrong: "high-quality" is meaningless without criteria
description: This skill generates high-quality glossary definitions.

# Right: specific quality standard named
description: This skill generates ISO 11179-compliant glossary definitions
  (precise, concise, distinct, non-circular, free of business rules).
```

**Mistake 4: First-person reference**

```yaml
# Wrong: skill descriptions should not use first person
description: I will analyze your course description and tell you what's missing.

# Right: objective, third-person description
description: This skill analyzes course descriptions and reports on missing or
  incomplete elements required for learning graph generation.
```

---

## Field 3: `license`

### What It Does

The `license` field declares the open-source license under which the skill is distributed. For skills in the McCreary ecosystem and most custom skill development, the standard value is `MIT`.

```yaml
license: MIT
```

### Why It Exists

The `license` field enables skill sharing and distribution. When a skill is published to a shared registry, other users need to know whether they can:

- Use the skill for commercial projects
- Modify the skill and redistribute it
- Include it in products without attribution requirements

The MIT license is the most permissive common open-source license and is appropriate for most public skills. It allows unrestricted use, modification, and distribution with attribution.

### License Options

| License | Use Case |
|---------|----------|
| `MIT` | Maximum permissibility, standard for public skills |
| `Apache-2.0` | Enterprise-safe with patent protections |
| `GPL-3.0` | Requires derivative works to be open-sourced |
| `Proprietary` | Skills that should not be redistributed |
| `CC-BY-4.0` | Creative Commons for documentation-heavy skills |

For skills you intend to keep private (personal workflow automations, proprietary business logic), using `Proprietary` signals clearly that the skill should not be shared.

### License Field in Practice

For most skill authors reading this guide, the license field will always be `MIT`. The important thing is to include it — a missing license field forces anyone who wants to share or build on your skill to make assumptions about redistribution rights.

---

## Field 4: `allowed-tools`

### What It Does

The `allowed-tools` field restricts which tools Claude can use while executing the skill. It is a security and consistency mechanism: it prevents Claude from taking actions outside the defined scope of the skill, and it creates predictable, auditable behavior.

```yaml
allowed-tools: Bash(~/.claude/skills/glossary-generator:*)
```

### Why Tool Restriction Matters

Without `allowed-tools`, a skill running in Claude Code has access to every tool Claude can use: file reads, file writes, bash commands in any directory, network requests, and more. This is appropriate for open-ended conversations but dangerous for structured skills.

Consider a skill designed to analyze a course description. Without tool restrictions, Claude could hypothetically:
- Write to unintended directories
- Execute shell commands outside the project scope
- Make network requests to external services

The `allowed-tools` field eliminates these possibilities by explicitly declaring what Claude is permitted to do.

### Glob Pattern Syntax

The `allowed-tools` field uses glob patterns to specify which tools are allowed and what scopes are permitted.

**Basic syntax:**

```
ToolName(path-pattern:operation)
```

**Common patterns:**

```yaml
# Allow bash commands only within the skill's own directory
allowed-tools: Bash(~/.claude/skills/my-skill:*)

# Allow bash commands in the skill directory AND a temp directory
allowed-tools: Bash(~/.claude/skills/my-skill:*), Bash(/tmp:*)

# Allow bash commands anywhere in the project docs folder
allowed-tools: Bash(~/projects/my-project/docs:*)

# Allow file reads anywhere (no path restriction on Read tool)
allowed-tools: Read(*), Bash(~/.claude/skills/my-skill:*)

# Allow all tools (equivalent to no allowed-tools field - use with caution)
allowed-tools: "*"
```

**Multiple tools:**

Multiple tool permissions are separated by commas:

```yaml
allowed-tools: Bash(~/.claude/skills/my-skill:*), Bash(/tmp:*), Read(~/projects:*)
```

### Designing Your Tool Permission Set

When designing `allowed-tools` for a new skill, ask four questions:

1. **Does this skill need to run shell commands?** If yes, which directories need bash access?
2. **Does this skill read files outside the project?** If yes, which paths?
3. **Does this skill write files?** If yes, which directories?
4. **Does this skill need network access?** (Rare for most skills — most skills read and write local files)

A well-designed skill has the minimum permissions necessary to accomplish its workflow. If a skill only needs to read files in `docs/` and write to `docs/`, there is no reason to allow bash access to the entire filesystem.

### Common allowed-tools Patterns by Skill Type

**Documentation generator (reads project, writes to docs/):**
```yaml
allowed-tools: Bash(~/projects:*), Read(~/projects:*)
```

**Validator (reads only, no writes):**
```yaml
allowed-tools: Read(*)
```

**MkDocs skill (needs to run mkdocs CLI):**
```yaml
allowed-tools: Bash(~/projects:*), Bash(/usr/local/bin:*)
```

**Skill that runs Python scripts from the skill package:**
```yaml
allowed-tools: Bash(~/.claude/skills/learning-graph-generator:*), Bash(~/projects:*)
```

### What Happens Without allowed-tools

If the `allowed-tools` field is omitted, Claude operates without tool restrictions. This is appropriate during skill development and prototyping, but is not recommended for production skills that will be shared or used in automated workflows.

The risk is not necessarily malicious behavior — it is unpredictable behavior. A skill without tool restrictions may work correctly in your environment and fail unexpectedly in someone else's environment because Claude makes different tool choices when not constrained.

```admonition note
**Development vs. Production Practice**

During development, it is reasonable to omit `allowed-tools` to avoid debugging permission issues while iterating on the workflow. Once the skill is working correctly, add explicit `allowed-tools` restrictions before sharing or deploying the skill.
```

---

## The Frontmatter as a Whole

Understanding each field individually is useful, but the real insight is how they work together as a system.

```yaml
---
name: course-description-analyzer     # 1. Registration key
description: This skill analyzes or creates course descriptions for intelligent
  textbooks by checking for completeness of required elements and providing
  quality scores with improvement suggestions. Use this skill when working with
  course descriptions in /docs/course-description.md that need validation or
  creation for learning graph generation.   # 2. Context injection + selection signal
license: MIT                           # 3. Distribution rights
allowed-tools: Bash(~/.claude/skills/course-description-analyzer:*)   # 4. Permission boundary
---
```

When a user invokes this skill:

1. Claude Code finds the skill directory `course-description-analyzer/` in `~/.claude/skills/`
2. It reads the `name` field to confirm the skill identity matches the invocation
3. It reads the `description` and injects it into Claude's context
4. It applies the `allowed-tools` restrictions for the duration of the skill session
5. It records the `license` field in any distributed artifacts

This four-step sequence happens before any workflow step runs. The frontmatter is not documentation — it is the initialization phase of every skill execution.

---

## Frontmatter Validation Checklist

Before publishing or sharing a skill, verify all four fields against this checklist:

| Field | Check | Pass Condition |
|-------|-------|----------------|
| `name` | Is it kebab-case? | All lowercase, hyphens only, no spaces |
| `name` | Does it match the directory name? | Exact string match |
| `name` | Is it descriptive? | Communicates function in 2-4 words |
| `description` | Is it one paragraph? | 50-100 words recommended |
| `description` | Does it contain a "Use this skill when..." clause? | Explicit trigger condition present |
| `description` | Does it name the output? | Clear statement of what is produced |
| `description` | Does it use user-natural vocabulary? | Matches how users would describe their need |
| `license` | Is it present? | Field exists with a valid license identifier |
| `allowed-tools` | Are permissions minimal? | No broader than required by the workflow |
| `allowed-tools` | Are all required tools included? | Skill can execute all workflow steps |

---

## Key Takeaways

- The frontmatter is not decoration — it is the initialization layer that runs before any workflow step
- The `description` field functions as a prompt that shapes Claude's behavior throughout the skill session; treat it as instructions, not a label
- The two-sentence description structure (what it does + when to use it) is the most effective format
- The `name` field must match the directory name exactly and must be in kebab-case
- `allowed-tools` creates predictable, auditable behavior by restricting Claude to the permissions the skill actually needs
- Omitting any field is never safe — each field either enables core functionality or prevents a class of errors

In Chapter 6, we move into the workflow body — how to structure multi-step workflows, the Step 0 environment setup pattern, user dialog triggers, and conditional branching.
