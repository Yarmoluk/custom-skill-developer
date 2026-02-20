# Chapter 8: Meta-Skill Routers

A single skill handles one job well. But what happens when a domain naturally splits into multiple related workflows — each sharing a common entry point, the same quality standards, and many of the same concepts, but diverging sharply in execution?

That is the problem meta-skill routers solve.

This chapter explains the routing pattern in depth: how it works, when to use it, and how to build a production-quality meta-skill from scratch. By the end you will have a complete worked example — a `report-generator` meta-skill with four distinct sub-skill variants — including every file in the directory structure.

---

## What Is a Meta-Skill?

A meta-skill is a skill whose primary job is *routing*. When invoked, it does not immediately begin producing output. Instead, it analyzes the user's request, identifies which sub-skill variant is appropriate, loads the relevant reference guide, and then executes within that variant's context.

From the user's perspective, they invoke one skill. Under the hood, the meta-skill transparently selects and runs the right workflow for their specific request.

This pattern solves three real problems:

**1. The proliferation problem.** If every sub-variant were its own skill, users would need to know which variant to pick before they even understood the domain. A `report-generator` entry point is more intuitive than having to choose between `executive-summary-generator`, `technical-spec-generator`, `sales-report-generator`, and `ops-dashboard-generator`.

**2. The token budget problem.** A SKILL.md file that tries to embed full instructions for fourteen sub-variants would balloon to 15,000+ tokens. The system prompt budget is fixed. Lazy loading reference guides means you only pay the token cost for the variant you actually need. (This is covered in depth in Chapter 9.)

**3. The maintenance problem.** Shared scaffolding — quality scoring, log format, file naming conventions — lives in the meta-skill SKILL.md. Variant-specific detail lives in the reference guide. You update each in exactly one place.

---

## When to Build a Meta-Skill

Use a meta-skill when all of the following are true:

- You have **3 or more sub-variants** that share a common user intent but diverge in workflow steps
- The variants share **quality criteria, output format conventions, or file naming patterns**
- The correct variant is usually **determinable from the user's request** without interactive disambiguation
- Each variant's detail is **substantial enough** (500+ tokens) to justify lazy loading

Do not use a meta-skill for two variants with minor differences. A conditional in a single SKILL.md handles that cleanly. Reserve the routing pattern for genuine divergence.

---

## The Routing Table Pattern

The core mechanism is a routing table — a structured mapping from keywords or request patterns to reference file paths.

```yaml
routing:
  keywords:
    executive:     references/executive-summary-guide.md
    summary:       references/executive-summary-guide.md
    leadership:    references/executive-summary-guide.md
    technical:     references/technical-spec-guide.md
    spec:          references/technical-spec-guide.md
    architecture:  references/technical-spec-guide.md
    sales:         references/sales-report-guide.md
    pipeline:      references/sales-report-guide.md
    revenue:       references/sales-report-guide.md
    ops:           references/ops-dashboard-guide.md
    operations:    references/ops-dashboard-guide.md
    metrics:       references/ops-dashboard-guide.md
    dashboard:     references/ops-dashboard-guide.md
```

Claude reads this table as part of the SKILL.md. When the user's request contains a matching keyword, Claude loads the corresponding reference file and proceeds with that variant's workflow.

Multiple keywords mapping to the same file is intentional and important. Users rarely use the exact vocabulary you expect. "Revenue breakdown" should route the same as "sales report." Covering synonyms and related terms dramatically reduces routing failures.

### Keyword Matching Rules

The routing logic Claude applies when reading this table follows a priority order:

1. **Exact keyword match** in the user's request — highest confidence
2. **Semantic match** — the concept is clearly present even if the word differs ("Q3 numbers" implies sales/revenue context)
3. **Context from prior messages** — if the conversation already established report type, use it
4. **Decision tree** — when ambiguity remains after the above

This is not regex matching. Claude uses natural language understanding, which means the routing table functions as a *signal vocabulary* rather than a rigid parser. Write your keyword list to seed Claude's semantic understanding, not to enumerate every possible phrasing.

---

## The Decision Tree for Ambiguous Requests

Not every request resolves cleanly to one route. "Generate a report on Q3 performance" is ambiguous — it could be executive, sales, or ops depending on context.

A decision tree handles this. In the meta-skill SKILL.md, after the routing table, include an explicit disambiguation section:

```markdown
## Disambiguation Protocol

If routing is ambiguous after keyword matching, apply this decision tree:

1. Is the primary audience C-suite or board-level?
   YES → executive-summary-guide.md
   NO  → continue

2. Does the request emphasize technical architecture, APIs, or system design?
   YES → technical-spec-guide.md
   NO  → continue

3. Does the request emphasize revenue, deals, pipeline, or quota?
   YES → sales-report-guide.md
   NO  → continue

4. Default to ops-dashboard-guide.md for operational metrics, KPIs, or
   process performance.

5. If still unclear after applying this tree, ask the user ONE clarifying
   question: "Is this report primarily for leadership, technical review,
   sales tracking, or operational monitoring?"
```

The decision tree has two properties that make it effective:

- **It is deterministic.** Working through the tree from top to bottom always produces an answer.
- **It has an escape hatch.** If the tree still cannot resolve ambiguity, Claude asks one targeted question rather than guessing or refusing.

Keep the escape hatch tight. "Ask ONE clarifying question" is a constraint, not a suggestion. Users who invoke a skill want immediate output, not an interview.

---

## The References Directory

The `references/` directory lives inside the skill folder:

```
~/.claude/skills/report-generator/
├── SKILL.md
└── references/
    ├── executive-summary-guide.md
    ├── technical-spec-guide.md
    ├── sales-report-guide.md
    └── ops-dashboard-guide.md
```

Each reference guide contains the full, detailed workflow for that variant. It is written as a standalone document that Claude can execute once loaded.

Reference guides are **never loaded speculatively**. The meta-skill loads exactly one guide — the one that matched the routing decision. All other variant guides consume zero tokens in that session.

### What Goes in a Reference Guide

A reference guide is not a summary or a pointer. It is the complete execution specification for its variant. It should contain:

- **Workflow steps** — numbered, sequential, specific
- **Output format** — exact structure, sections, headings expected in the output document
- **Quality criteria** — what "good" looks like for this variant
- **Examples** — at least one condensed example of correct output structure
- **Variant-specific warnings** — common mistakes unique to this type

Think of the reference guide as a sub-skill SKILL.md that happened to be stored separately for token efficiency reasons. Write it with the same completeness you would give a standalone skill.

---

## Worked Example: report-generator

Here is the complete file structure and content for a production `report-generator` meta-skill.

### File Structure

```
~/.claude/skills/report-generator/
├── SKILL.md
└── references/
    ├── executive-summary-guide.md
    ├── technical-spec-guide.md
    ├── sales-report-guide.md
    └── ops-dashboard-guide.md
```

---

### SKILL.md

```markdown
---
name: report-generator
version: 1.2.0
description: >
  Generates structured business reports. Routes to one of four variants:
  executive summary, technical specification, sales performance, or
  operational dashboard. Provide a topic, time period, and any available
  data — the skill selects the appropriate format automatically.
author: your-name
tags: [reports, business, meta-skill, router]
---

# Report Generator

## Purpose

Generate professional business reports in the format appropriate for your
audience and purpose. This skill routes automatically between four variants
based on the keywords and context in your request.

## Invocation

```
/report-generator [describe your report topic and audience]
```

Examples:
- `/report-generator Q3 executive summary for the board`
- `/report-generator technical spec for the authentication service redesign`
- `/report-generator sales pipeline report, week ending Nov 15`
- `/report-generator ops dashboard for customer support team, October`

## Routing Table

| Keywords | → Variant | Reference |
|----------|-----------|-----------|
| executive, summary, board, leadership, C-suite | Executive Summary | references/executive-summary-guide.md |
| technical, spec, architecture, system, API, design | Technical Spec | references/technical-spec-guide.md |
| sales, pipeline, revenue, quota, deals, ARR, MRR | Sales Report | references/sales-report-guide.md |
| ops, operations, metrics, dashboard, KPIs, SLA, support | Ops Dashboard | references/ops-dashboard-guide.md |

## Disambiguation Protocol

If routing is ambiguous after keyword matching:

1. Is the primary audience C-suite or board-level? → executive-summary-guide.md
2. Does the request center on technical architecture or system design? → technical-spec-guide.md
3. Does the request center on revenue, deals, or quota attainment? → sales-report-guide.md
4. Default: ops-dashboard-guide.md

If still unclear: ask "Is this report for leadership review, technical
documentation, sales tracking, or operational monitoring?"

## Execution Protocol

1. Parse the user's request for routing keywords
2. Apply the routing table (highest-confidence match wins)
3. If ambiguous, apply the disambiguation protocol
4. Read the matched reference guide
5. Execute the variant workflow from the reference guide
6. Apply the shared quality checklist below
7. Write the session log

## Shared Quality Checklist

Before delivering any output, verify:
- [ ] Report has a clear title with date/period
- [ ] Executive summary / TL;DR section present (even technical reports)
- [ ] All data claims are attributed or flagged as estimates
- [ ] Recommendations section present if report type supports it
- [ ] Output written in the correct register for the target audience

## Output Location

Reports are saved to: `./reports/[variant]-[YYYY-MM-DD].md`

## Session Log

After completion, write a log entry to:
`./logs/report-generator-v1.2.0-[DATE].md`

Include: variant selected, routing confidence (high/medium/low), time to
complete, word count, quality score (0-10).
```

---

### references/executive-summary-guide.md

```markdown
# Executive Summary Variant — Workflow Guide

## Audience

C-suite leaders, board members, investors. Readers who have 3 minutes, not 30.
Every sentence must earn its place. Cut ruthlessly.

## Output Structure

1. **Title Block** — Report title, date, author, period covered
2. **One-Sentence Summary** — The single most important thing
3. **Key Findings** (3-5 bullets, each under 20 words)
4. **Business Impact** — Dollar amounts, percentages, customer counts
5. **Recommended Actions** (2-4 items, each with an owner and deadline)
6. **Supporting Context** — Optional, max 200 words, for readers who want more

Total target length: 400-600 words. Never exceed 800.

## Workflow Steps

1. Identify the primary business question the report must answer
2. Extract the 3-5 findings that most directly answer that question
3. Quantify each finding (no qualitative-only bullets in an exec summary)
4. Write the one-sentence summary last, after findings are clear
5. Write recommendations as action verbs: "Hire," "Approve," "Pause," "Redirect"
6. Remove all jargon. If a term needs defining, the term is wrong for this audience.

## Quality Criteria

- Findings are quantified (not "significantly improved" but "improved 23%")
- Recommendations have explicit owners or owner roles
- No sentence exceeds 25 words
- A reader who skips to page 2 of supporting context still has everything they need from pages 0-1

## Common Mistakes

- Including methodology in the body (it belongs in an appendix if anywhere)
- Writing "As you can see..." — the reader should see without narration
- Using passive voice for recommendations ("Action should be taken" → "CMO to approve budget by Nov 30")
```

---

### references/technical-spec-guide.md

```markdown
# Technical Specification Variant — Workflow Guide

## Audience

Engineers, architects, technical leads. Readers who will implement or review
the system being specified. Precision over brevity. Ambiguity is a defect.

## Output Structure

1. **Title Block** — Document title, version, date, authors, status (Draft/Review/Approved)
2. **Overview** — What the system does and why it exists (2-3 paragraphs)
3. **Scope** — What is in scope, what is explicitly out of scope
4. **Architecture Diagram** — Mermaid block required for any system with >2 components
5. **Component Specifications** — One subsection per component
6. **Data Model** — Entity relationships, key fields, types
7. **API Contracts** (if applicable) — Endpoint, method, request/response schema
8. **Error Handling** — What can go wrong and how the system responds
9. **Open Questions** — Unresolved decisions, flagged explicitly
10. **Revision History** — Version table at bottom

## Workflow Steps

1. Identify all system components from the user's description
2. Determine boundaries (what this system owns vs. what it calls)
3. Draft the architecture diagram before writing prose
4. Write component specs in dependency order (upstream components first)
5. Flag every assumption explicitly as [ASSUMPTION: ...]
6. Flag every open decision explicitly as [OPEN: ...]

## Quality Criteria

- No ambiguous pronoun references ("it," "they," "this") without clear antecedents
- Every interface is specified bidirectionally (what caller sends, what callee returns)
- Error states are enumerated, not handwaved ("handles errors appropriately" is not acceptable)
- Open questions are distinguished from decisions already made

## Common Mistakes

- Writing prose for things that should be tables or diagrams
- Assuming the reader shares context the author has
- Omitting the "out of scope" section (creates scope creep later)
```

---

### references/sales-report-guide.md

```markdown
# Sales Performance Report Variant — Workflow Guide

## Audience

Sales leadership, RevOps, finance. Readers tracking quota attainment,
pipeline health, and revenue trends against targets.

## Output Structure

1. **Title Block** — Report title, period, author, date generated
2. **Period Summary** (4 key metrics in a 2x2 grid):
   - Closed revenue vs. target
   - Pipeline coverage ratio
   - New opportunities created
   - Average deal cycle (days)
3. **Closed Deals Table** — Deal name, ACV, close date, rep, stage
4. **Pipeline Snapshot** — By stage, with aging flags (>90 days at stage = flag)
5. **Rep Performance** — Quota attainment % per rep (no names if requested)
6. **Trend Line** — Last 4 periods, same metrics as Period Summary
7. **Risk Flags** — Deals at risk, slippage, churn signals
8. **Forecast** — Current quarter projection with confidence range

## Workflow Steps

1. Extract all deal/revenue data from user input
2. Compute period-over-period changes for all key metrics
3. Flag any deal >90 days at current stage
4. Calculate pipeline coverage (pipeline value / remaining quota target)
5. Generate forecast as a range, not a point estimate
6. Write risk flags before recommendations — risks inform recommendations

## Quality Criteria

- All percentages reference a clear baseline
- Forecast includes confidence range, not just a number
- Aging flags use consistent threshold (default: 90 days)
- Rep performance section is present even if data is aggregate-only

## Common Mistakes

- Reporting revenue without comparing to target
- Presenting a point forecast without confidence range
- Omitting pipeline coverage ratio (most critical leading indicator)
```

---

### references/ops-dashboard-guide.md

```markdown
# Operational Dashboard Variant — Workflow Guide

## Audience

Operations managers, team leads, department heads. Readers monitoring
process performance against SLAs, capacity, and efficiency targets.

## Output Structure

1. **Title Block** — Dashboard title, period, team/system, date generated
2. **Health Summary** — RAG (Red/Amber/Green) status for each key area
3. **Volume Metrics** — Throughput, load, transaction counts for the period
4. **SLA Performance** — Each SLA with target, actual, variance
5. **Incident Summary** — Count, severity breakdown, MTTR, top repeat issues
6. **Capacity Utilization** — Current utilization vs. designed capacity
7. **Trend Comparison** — Same period last month / last quarter
8. **Action Items** — Prioritized list, each with owner and due date

## Workflow Steps

1. Identify the team or system being monitored
2. List all SLAs or KPIs the user has provided
3. Assign RAG status to each: Red = missed target, Amber = within 10% of threshold, Green = on target
4. Calculate MTTR for incidents if incident data is available
5. Flag capacity risks if utilization >80%
6. Write action items last, after all data sections are populated

## Quality Criteria

- Every metric has a target to compare against (no contextless numbers)
- RAG status is applied consistently using the defined thresholds
- Capacity section flags utilization >80% as amber, >95% as red
- Action items are specific and assigned (not "review this area")

## Common Mistakes

- Reporting metrics without targets
- Mixing rolling averages with point-in-time snapshots without labeling
- Burying critical incidents in narrative rather than surfacing in the summary
```

---

## Building Your Own Meta-Skill: The Process

### Step 1: Inventory Your Variants

List all the sub-variants your domain needs. For each one, write a one-sentence description of who uses it and what they need. If you cannot write that sentence clearly, the variant is not well-defined yet — clarify it before building.

### Step 2: Build the Routing Table

Extract the vocabulary each variant's users naturally use. Include:
- The canonical term (what you'd call it)
- Synonyms users might reach for
- Related concepts that correlate with this variant

Aim for 4-6 keywords per variant. Fewer than 3 creates routing gaps. More than 8 starts to introduce false matches across variants.

### Step 3: Design the Decision Tree

Walk through three deliberately ambiguous request examples. If your routing table resolves all three correctly, the decision tree is a safety net for edge cases. If the table fails on any of the three, refine it before writing the decision tree.

The decision tree should have at most 4-5 nodes. If it requires more, your variants are not well enough differentiated and you should reconsider the decomposition.

### Step 4: Write the Reference Guides

Write each reference guide as if it were a standalone SKILL.md. Include the full workflow, complete output structure, quality criteria, and common mistakes. Do not abbreviate or summarize — the whole point of the reference file is to carry the full detail that you offloaded from the main SKILL.md.

A reference guide that is too thin defeats the purpose. If a guide is under 300 words, it probably should not be a separate file — fold it back into the main SKILL.md as a conditional section.

### Step 5: Test the Routing

Before deploying, test with a set of requests that includes:
- One clear example of each variant
- Two ambiguous requests that require the decision tree
- One request that should trigger the clarifying question

Document the routing result for each test case. If any case routes incorrectly, adjust the keyword table or decision tree before releasing.

---

## Routing Failures and How to Handle Them

Even well-designed routing tables fail. These are the common failure modes and their fixes:

| Failure Mode | Symptom | Fix |
|---|---|---|
| Vocabulary mismatch | User says "briefing" but no variant covers that | Add synonym to routing table |
| Cross-variant pollution | Technical terms appear in sales requests | Add negative signals or decision tree guard |
| Over-specification | Decision tree asks 3 questions before routing | Simplify tree; add more keywords |
| Ambiguity explosion | >30% of requests hit the escape hatch | Variants are not well-differentiated; redesign |
| Reference guide not found | Claude cannot locate the reference file | Verify path in routing table exactly matches filesystem |

The most important diagnostic is the escape hatch rate. If more than 20-30% of invocations end up at the clarifying question, the routing design needs work, not just the keyword list.

---

## Anti-Patterns to Avoid

**Do not embed full variant workflows in the SKILL.md.** The entire purpose of the meta-skill pattern is to keep the main file lean. If you find yourself writing 2,000 words of variant-specific workflow in SKILL.md, move it to a reference guide.

**Do not build a meta-skill for two variants.** Two variants is a conditional, not a router. Use an `if/else` block in a single SKILL.md instead.

**Do not let reference guides diverge in quality.** If three guides are excellent and one is thin, routing to that thin guide will produce noticeably worse output. Maintain all guides to the same standard.

**Do not silently default.** If routing fails and the skill silently picks a default variant without informing the user, errors are invisible. Always log the routing decision and, if using the escape hatch, always tell the user which variant you selected and why.

---

## Summary

The meta-skill router pattern solves the consolidation-vs-detail tension by separating routing logic from execution detail. The SKILL.md stays lean and handles routing. The reference guides carry full execution specifications, loaded only when needed.

The four components are:
1. A routing table mapping keywords to reference file paths
2. A decision tree for ambiguous cases with a single escape-hatch question
3. A `references/` directory containing complete variant guides
4. Shared scaffolding (quality checklist, log format, output naming) in the main SKILL.md

In Chapter 9, we examine why this architecture also solves a token budget problem — and how to measure the token cost of every design decision you make in a skill.
