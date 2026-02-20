# Chapter 9: Token Efficiency Design

Every skill you write operates within a fixed budget: the context window. That budget is shared among the system prompt, the skill definition, the conversation history, and all content Claude generates. There is no escaping this constraint, only designing around it intelligently.

Token efficiency is not about writing short skills. It is about ensuring that every token in your skill definition is doing necessary work — and that tokens for detail you do not currently need are deferred until you do.

This chapter covers the mechanics of token consumption in skills, the tiered retrieval pattern that keeps individual sessions lean, lazy loading, skip-if-complete detection, and how to measure the actual token impact of your design decisions.

---

## Why Token Efficiency Matters

### The System Prompt Budget

When Claude Code loads a skill, the SKILL.md content is injected into the context. This happens before the user has typed a single word. Every token in your SKILL.md is spent unconditionally — whether or not that content is relevant to the specific invocation.

In a typical Claude Code session with a complex project, the context might look like this:

| Component | Approximate Tokens |
|---|---|
| Base system prompt | 2,000 - 4,000 |
| Active skill definition (SKILL.md) | 500 - 8,000 |
| Project files read during session | 2,000 - 40,000+ |
| Conversation history | Grows linearly |
| Claude's output so far | Grows linearly |

The context window for Claude Sonnet is 200,000 tokens. That sounds large until you realize a multi-hour deep work session with file reads, iterations, and conversation history can consume 80,000-150,000 tokens. A bloated skill definition is dead weight from the moment the session starts.

### The Cascade Effect

Token waste compounds. A SKILL.md with 8,000 tokens instead of 2,000 does not just cost 6,000 tokens up front. Every time that skill is invoked in a session where Claude maintains context, those tokens remain loaded. In a pipeline session that invokes 8 skills sequentially, an extra 6,000 tokens per skill adds 48,000 tokens of overhead — enough to noticeably shorten how long the session can run before context fills and the user must compact.

### The Real Cost in Concrete Numbers

Here is what different skill design choices actually cost:

| Design Decision | Token Cost | Notes |
|---|---|---|
| Reading skill name from MCP server registry | ~0 tokens | MCP metadata is external |
| Shell script returning skill description | ~67 tokens | A brief description string |
| Loading full SKILL.md (lean) | ~800 - 1,500 tokens | Well-designed, single-variant skill |
| Loading full SKILL.md (average) | ~2,000 - 4,000 tokens | Typical production skill |
| Loading full SKILL.md (bloated) | ~6,000 - 12,000 tokens | Skills with embedded examples and verbose prose |
| Loading one reference guide | ~500 - 1,200 tokens | Via lazy load on demand |
| Loading all reference guides unconditionally | ~3,000 - 8,000 tokens | The anti-pattern to avoid |
| Full project file (2,000 lines of code) | ~6,000 - 15,000 tokens | Context of the read, not the skill |

The difference between a lean skill and a bloated one is roughly equivalent to reading a 500-line source file — every invocation, whether or not that detail was needed.

---

## The Tiered Information Retrieval Pattern

Tiered retrieval is the organizing principle of token-efficient skill design. Information is classified by when it is needed and retrieved at the appropriate tier — never earlier.

### Tier 0: MCP Server Metadata (0 tokens)

The MCP (Model Context Protocol) server maintains a registry of installed skills. Claude can query this registry to get a skill's name, description, and invocation syntax without reading the skill file itself.

A skill's MCP metadata — its name, one-line description, and invocation signature — is retrieved from the server at essentially zero token cost to the context window. This is how skill discovery works: Claude can list available skills and describe them without loading any of them.

Design implication: your one-line description in the YAML frontmatter needs to be precise enough that a user can select the right skill from a list. This description lives at Tier 0. It needs to work without any supporting context.

```yaml
description: >
  Generates four variants of business reports (executive summary,
  technical spec, sales performance, ops dashboard) with routing
  and quality scoring.
```

This description tells a user everything they need to know to decide whether to invoke this skill. It is also all the information available at Tier 0.

### Tier 1: The SKILL.md (~800 - 4,000 tokens)

When a user invokes the skill, Claude reads the SKILL.md. This is the first real token expenditure. Everything in SKILL.md is loaded unconditionally for every invocation.

**Principle: SKILL.md should contain only what is needed for every invocation.**

What belongs at Tier 1:
- Purpose and audience
- Invocation examples
- The routing table (for meta-skills)
- Shared workflow steps that run regardless of variant
- Shared quality checklist
- Output naming conventions
- Log format specification
- Disambiguation protocol
- Pointers to reference guides (not the guides themselves)

What does not belong at Tier 1:
- Full variant workflows (unless only one variant exists)
- Detailed examples
- Lengthy background explanations
- Reference material that is only relevant sometimes
- Anything that is a variant-specific detail

### Tier 2: Reference Guides (~500 - 1,200 tokens each)

Reference guides are loaded lazily — only when routing selects them. A meta-skill with four variants loads exactly one reference guide per invocation. The other three guides cost zero tokens.

This is the payload of the meta-skill pattern. Without lazy loading, a four-variant skill would need to carry all four workflows in SKILL.md. With lazy loading, you only pay for the workflow you are actually using.

**Principle: reference guides should be self-contained execution specifications.**

A reference guide cannot assume context from other reference guides. Once loaded, it must have everything Claude needs to execute the variant. Do not use "see the executive-summary-guide.md for an example" in a technical-spec guide — that would require loading a second guide.

### Tier 3: External Files (variable, loaded on demand)

Some skills need to read actual project files — source code, data, configuration, prior outputs. These are loaded at the explicit direction of the workflow steps, not automatically.

Token-efficient skills defer these reads as long as possible and read only what they need. "Read the entire codebase" is an anti-pattern. "Read `src/auth/login.py` to check the current error handling pattern" is a targeted read.

---

## Lazy Loading in Practice

Lazy loading means: do not read the file until you need what is in it.

In skill design, this applies at two levels.

### Level 1: Reference Guide Lazy Loading

The meta-skill pattern is the primary example. The SKILL.md contains the routing table but not the reference content. The reference guide is loaded only after routing resolves.

In the workflow section of your SKILL.md, the lazy load is expressed as an explicit step:

```markdown
## Execution Protocol

1. Parse the user's request for routing keywords
2. Resolve routing using the table above
3. **Read the matched reference guide** (and only that guide)
4. Execute the variant workflow from the reference guide
```

Step 3 is where the lazy load occurs. Until routing resolves, no reference guide is read. After routing resolves, exactly one guide is read. Claude executes this naturally when the workflow is written this way.

### Level 2: Project File Lazy Loading

Within a skill's workflow, reads of external files should be deferred to the step that requires them:

**Inefficient (eager loading):**
```markdown
## Workflow

1. Read all files in the `src/` directory
2. Read the existing test suite
3. Read the configuration files
4. Identify which component needs updating
...
```

**Efficient (lazy loading):**
```markdown
## Workflow

1. Identify which component needs updating from the user's description
2. Read ONLY the source file for that component: `src/[component-name].py`
3. Read the existing tests for that component: `tests/test_[component-name].py`
4. Generate the update
5. If the update affects configuration, read the relevant config section
```

The lazy version reads substantially fewer tokens in the common case where only one component is involved. The eager version reads everything regardless.

---

## Skip-If-Complete Detection

Skip-if-complete is a pattern where a skill checks whether its output already exists before running the full workflow. This is especially valuable in pipeline contexts where a skill might be re-invoked after a failure partway through.

### The Pattern

At the beginning of the workflow (before any heavy work), add a detection step:

```markdown
## Pre-Flight Check

Before executing, check:

1. Does the expected output file already exist?
   - Check: `./reports/[variant]-[YYYY-MM-DD].md`
   - If YES and file is >500 words: report completion to user, offer to
     regenerate or skip
   - If NO: proceed with full workflow

2. Does a session log from today already exist for this skill?
   - Check: `./logs/report-generator-v1.2.0-[TODAY'S DATE].md`
   - If YES: read the log summary only (not the full report) to understand
     what was completed
```

The critical detail: when checking for prior output, read as little as possible. A word count check or header check often tells you everything you need to know without reading the full file. "Does a file exist at this path and is it substantial?" requires far fewer tokens than reading the file to determine its completeness.

### When Skip-If-Complete Matters Most

Skip-if-complete pays the largest dividend in:

1. **Batch operations** — when the same skill runs against 12 items and a crash occurred on item 7, you resume from item 8, not item 1

2. **Pipeline resumption** — when a 12-step pipeline is re-started after a checkpoint, skills that already completed their step can skip

3. **Idempotent workflows** — when a skill might be invoked twice with the same parameters (user reruns without realizing), duplicate work is avoided

### State Tracking with JSON

For batch operations and pipeline resumption, a simple JSON state file tracks what has and has not been completed. This is the `sim-status.json` pattern (covered in depth in Chapter 10), but the token efficiency angle is worth noting here:

A small JSON file (200-500 tokens when read) encodes the state of a batch operation that might otherwise require reading 20+ output files to reconstruct. Reading the state file is dramatically cheaper than reconstructing state from the outputs.

```json
{
  "batch_id": "report-batch-2024-11-15",
  "total": 12,
  "completed": ["item-01", "item-02", "item-03", "item-04", "item-05"],
  "in_progress": ["item-06"],
  "failed": [],
  "pending": ["item-07", "item-08", "item-09", "item-10", "item-11", "item-12"],
  "last_updated": "2024-11-15T14:23:11Z"
}
```

Reading this file tells Claude exactly where to resume without reading any of the five completed outputs.

---

## Minimal Context Strategies

Beyond tiered retrieval and lazy loading, several structural strategies reduce token consumption.

### Strategy 1: Tables Over Prose

Tables convey structured information at roughly half the token cost of equivalent prose. A routing table is not just visually cleaner than a paragraph describing routing rules — it is substantially cheaper to load.

**Prose version (~60 tokens):**
> If the user mentions the word "executive" or "summary" or "leadership" in their request, route to the executive summary variant. If they mention "technical" or "spec" or "architecture" or "system," route to the technical specification variant.

**Table version (~25 tokens):**
```
| executive, summary, leadership | → executive-summary-guide.md |
| technical, spec, architecture  | → technical-spec-guide.md    |
```

Apply this consistently across your SKILL.md. Checklists, routing rules, output structures, quality criteria — all of these are more token-efficient as structured lists or tables than as narrative prose.

### Strategy 2: Code Blocks for Structured Output

When specifying output structure, a code block template costs fewer tokens than describing the same structure in prose, and is less ambiguous:

**Prose (~80 tokens):**
> The output should begin with a title block containing the report title, the date it was generated, the author name, and the period the report covers. Below that should be an executive summary section...

**Template (~40 tokens):**
```markdown
# [Report Title]
**Generated:** [DATE] | **Author:** [NAME] | **Period:** [PERIOD]

## Executive Summary
[2-3 sentence summary]
```

### Strategy 3: Pointer, Not Payload

In SKILL.md, reference information that lives elsewhere with a path, not the content itself:

**Payload (high tokens, always loaded):**
```markdown
## ChartJS Configuration Reference

To create a bar chart, use the following configuration:
[200 lines of configuration examples]
```

**Pointer (low tokens, loads on demand):**
```markdown
## Chart Reference
For chart configuration details, read: references/chartjs-guide.md
```

The pointer loads with SKILL.md (minimal cost). The chartjs-guide.md only loads when the workflow actually reaches a charting step.

### Strategy 4: Compress Examples

Examples are among the highest-value content in a skill definition and also among the most token-expensive. The balance point is compressed examples — enough structure to be useful, stripped of all non-essential words.

**Full example (~150 tokens):**
> Here is an example of a well-formed executive summary. Notice how the first line immediately states the business outcome. The key findings section uses specific numbers rather than qualitative descriptors. The recommended actions section uses strong action verbs and includes explicit owners and deadlines.
>
> **Q3 Revenue Performance — Executive Summary**
> Q3 closed at $4.2M, 8% above plan, driven by enterprise segment outperformance...

**Compressed example (~60 tokens):**
```
# Q3 Revenue Performance — Executive Summary
Closed $4.2M, 8% above plan (enterprise outperformed, SMB -12%).

**Key Findings:** [3 bulleted numbers] | **Actions:** [2 owner+deadline pairs]
```

The compressed version demonstrates the pattern without wasting tokens on narration.

---

## Measuring Token Impact

Before shipping a skill, audit it. Here is a practical measurement process.

### Step 1: Estimate SKILL.md Token Cost

Copy the raw text of your SKILL.md and paste it into a token counting tool (many are available online for the tokenizers used by major models). Alternatively, estimate at approximately 750 words per 1,000 tokens for English prose, or 450-600 words per 1,000 tokens for structured markdown with code blocks (which tokenize less efficiently).

Target benchmarks:
- Single-variant skill: 600 - 1,500 tokens
- Meta-skill SKILL.md (routing only): 1,000 - 2,500 tokens
- Each reference guide: 400 - 1,000 tokens

If your SKILL.md exceeds 4,000 tokens, audit it aggressively. Something belongs in a reference guide or can be compressed.

### Step 2: Identify the Most Expensive Sections

Within the SKILL.md, identify the three heaviest sections by word count. For each:

- Is this section needed for every invocation? If no → move to a reference guide
- Is it in prose when it could be a table? If yes → convert
- Does it include examples? If yes → compress the examples

### Step 3: Calculate Worst-Case Session Budget

For any skill that is part of a larger pipeline, calculate the worst-case token consumption for the full pipeline session:

```
Base system prompt:          3,000 tokens (estimate)
All skill SKILL.md files:    N × avg_skill_tokens
Reference guides loaded:     M × avg_reference_tokens
Project files read:          Sum of files read
Conversation history:        grows_linearly
Claude output:               grows_linearly
─────────────────────────────────────────
Total at completion:         [sum]
```

If the estimated total approaches 150,000 tokens, the session will likely hit context limits before completing. Either compact the skill definitions or add compaction checkpoints to the pipeline (see Chapter 11).

### Step 4: Measure Reference Guide Savings

For each meta-skill, calculate the savings from lazy loading:

```
Total reference content:    4 guides × 800 tokens = 3,200 tokens
Lazy-load cost per invoke:  1 guide × 800 tokens = 800 tokens
Savings per invocation:     2,400 tokens (75%)
```

Over 10 invocations in a session, that 2,400-token saving per invocation represents 24,000 tokens of freed context — enough to read several more project files or extend the conversation substantially.

---

## The Cost of Loading the Full SKILL.md

There is one more token efficiency consideration that is easy to overlook: the difference between what the user sees when discovering a skill versus what Claude loads when executing it.

At the discovery stage (Tier 0), Claude sees only the description metadata — about 30-50 tokens. At the invocation stage (Tier 1), Claude reads the full SKILL.md — 800 to 4,000 tokens. This is a 20-80x token multiplication that happens the moment the user types the `/skill-name` command.

This means every token in your SKILL.md must justify itself against the question: "Is this worth paying for on every single invocation of this skill, including invocations where this content turns out to be irrelevant?"

If the answer is no — if there is a realistic invocation scenario where this content is not needed — it belongs in a reference guide, not in SKILL.md.

---

## A Practical Audit Checklist

Run this checklist on every skill before deploying it:

- [ ] SKILL.md is under 3,000 tokens (use a token counter to verify)
- [ ] All variant-specific detail is in reference guides, not in SKILL.md
- [ ] Routing tables use tables, not prose
- [ ] Quality criteria use bullet lists, not narrative
- [ ] Examples are compressed to their minimum useful form
- [ ] Output structure is shown as a template, not described in prose
- [ ] Pre-flight check is present and reads as little as possible
- [ ] Reference guide paths in the routing table are exact (no typos)
- [ ] Each reference guide is self-contained (requires no cross-guide reads)

---

## Summary

Token efficiency is an engineering discipline, not an afterthought. The key principles:

**Tiered retrieval** classifies information into tiers by when it is needed: MCP metadata (0 tokens), SKILL.md (loaded on invoke), reference guides (loaded on demand), project files (loaded when needed by the workflow).

**Lazy loading** defers reference guide reads until routing resolves, and defers project file reads until the specific workflow step that requires them.

**Skip-if-complete** checks for prior output before running the full workflow, enabling safe resumption in batch and pipeline contexts.

**Structural compression** uses tables, templates, and code blocks instead of prose wherever the content is inherently structured.

**Measurement** involves actually counting tokens, auditing the heaviest sections, and calculating worst-case session budgets for pipeline skills.

The payoff compounds. A well-optimized skill that saves 2,000 tokens per invocation enables longer sessions, larger batch operations, and more complex pipelines — without requiring any changes to the user's workflow.

Chapter 10 extends this efficiency conversation into the temporal domain: how session logs enable complex work to survive context window limits and resume cleanly across multiple sessions.
