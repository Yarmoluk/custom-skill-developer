# Chapter 7: Quality Scoring Systems

## Building Self-Evaluating Skills

A skill without a quality scoring system is a generator. It produces output, but it has no mechanism for determining whether that output is good. A skill with a quality scoring system is a self-evaluating agent — it generates output, assesses it against defined criteria, and makes a decision about whether to deliver, revise, or halt based on that assessment.

This chapter covers everything you need to design quality scoring systems for your skills: the 100-point scale, how to decompose quality into weighted sub-categories, threshold logic, examples from production skills, and a complete template rubric you can adapt for your own work.

---

## Why Quality Scoring Exists

The fundamental problem quality scoring solves is this: Claude generates text and code fluently, but it has no built-in mechanism for determining whether its output meets your specific standards. Left to its own judgment, Claude will produce output that is superficially plausible — well-formatted, grammatically correct, structurally appropriate — but may miss the specific quality criteria your domain requires.

Quality scoring externalizes those criteria. Instead of relying on Claude's implicit judgment, you define the criteria explicitly in the SKILL.md file. Claude then applies those criteria to evaluate its own output before delivering it.

This has three practical benefits:

1. **Consistency**: The same criteria are applied every run, regardless of context, session state, or how the conversation began.
2. **Transparency**: Users see the score and understand why the output received it. A score of 74/100 with a note "Missing examples for 3 of 8 terms" is actionable. "The output is okay" is not.
3. **Automation of revision**: A skill that scores its own output can automatically revise low-scoring sections without user involvement, delivering a better first draft.

---

## The 100-Point Scale

The 100-point scale is the standard across the McCreary skill ecosystem. It is not arbitrary — it was chosen for three reasons:

1. **Familiar interpretation**: Humans interpret 100-point scores intuitively. A score of 73 communicates "this is passing but not great" immediately, without explanation.
2. **Granularity for meaningful weighting**: Sub-categories can be weighted in increments of 5 or 10 points, producing natural integer totals.
3. **Threshold alignment**: Common thresholds (70, 80, 85) fall on round numbers that align with letter grades and standard quality tiers.

### Standard Threshold Definitions

| Score Range | Grade | Standard Meaning |
|-------------|-------|------------------|
| 85-100 | Excellent | Deliver immediately, no caveats |
| 70-84 | Good | Deliver with optional improvement notes |
| 55-69 | Adequate | Ask user whether to deliver or revise |
| 40-54 | Needs Work | Revise before asking user |
| Below 40 | Insufficient | Halt — cannot produce acceptable output |

These thresholds are defaults. For skills that generate high-stakes content (medical education, legal documentation, production code), you may raise the minimum acceptable threshold to 80. For skills that generate draft content intended for human revision, you may lower the interactive threshold to 60.

The key is that thresholds must be defined explicitly in the SKILL.md. A skill that says "if quality is acceptable, proceed" leaves "acceptable" undefined and produces inconsistent behavior.

---

## Decomposing Quality into Sub-Categories

A single undifferentiated score is less useful than a score broken into sub-categories. Sub-categories do three things:

1. They force you to think precisely about what "quality" means for this specific type of output
2. They give Claude a structured framework for assessment rather than a vague instruction to "assess quality"
3. They give users specific, actionable feedback: "Your score was low due to Precision (8/25), not Conciseness (23/25)"

### The Weighting Principle

Sub-category weights should reflect the relative importance of each criterion to the final output quality. Not all criteria are equally important. For glossary definitions, Non-circularity is binary — a circular definition is broken regardless of how well it performs on other criteria — so you might weight it higher. For README files, Accuracy is paramount because false claims are actively harmful.

**Design rule:** Weights should sum to 100. Use multiples of 5 for clean arithmetic.

### Common Weight Distributions

**Equal weighting (4 criteria):** 25-25-25-25
Best for: when all four criteria are genuinely equal in importance.
Used in: glossary-generator (Precision, Conciseness, Distinctiveness, Non-circularity)

**Dominant criterion:** 40-20-20-20
Best for: when one criterion is primary and failure on it invalidates the output regardless of other scores.
Used in: course validators where learning outcome completeness is the primary criterion.

**Tiered weighting:** 35-30-20-15
Best for: when criteria form a priority hierarchy.
Used in: chapter content generation (Conceptual Accuracy 35, Coverage 30, Clarity 20, Formatting 15).

---

## Real Example: Glossary Generator Rubric

The glossary-generator skill uses a four-criterion rubric derived directly from ISO 11179 metadata registry standards. Each criterion is equally weighted at 25 points.

### The Rubric

```markdown
Score each definition on four criteria (25 points each, 100 points total):

**Precision (25 points)**
Does the definition accurately capture the concept's meaning in the course context?

- 25: Definition is exact, unambiguous, and precisely correct for this domain
- 20: Definition is accurate but slightly broader or narrower than ideal
- 15: Definition captures the concept but contains one inaccuracy or overstatement
- 10: Definition is partially correct but misses the core meaning
- 0-9: Definition is inaccurate or misleading

**Conciseness (25 points)**
Is the definition the shortest it can be while remaining complete?

- 25: 20-50 words, every word necessary
- 20: 15-60 words, one or two unnecessary qualifiers
- 15: 60-80 words, could be shortened by 25%
- 10: Over 80 words, contains redundant explanation
- 0-9: Severely over-length or padded

**Distinctiveness (25 points)**
Does the definition clearly distinguish this concept from related concepts?

- 25: Definition uniquely identifies this concept; could not be applied to a similar concept
- 20: Mostly distinctive; one related concept could be confused
- 15: Some distinctiveness; student might confuse this with a closely related concept
- 10: Low distinctiveness; definition could apply to multiple concepts
- 0-9: Definition applies equally well to other concepts (not distinctive)

**Non-circularity (25 points)**
Does the definition avoid circular reasoning?

- 25: No circular references; does not use the term to define itself
- 20: One indirect circularity (uses a near-synonym of the term)
- 10: Direct circularity (defines term using itself)
- 0: Severely circular (definition adds no information)
```

### Applying the Rubric

The glossary-generator applies this rubric in Step 7 (Generate Quality Report). For each definition, Claude scores each criterion and computes an overall score:

```
Learning Graph:
  Precision: 25/25 — Exact definition, matches ISO standard precisely
  Conciseness: 20/25 — 47 words, slightly verbose
  Distinctiveness: 25/25 — Clearly distinguishes from Linear Curriculum
  Non-circularity: 25/25 — No self-reference
  Total: 95/100

Concept Dependency:
  Precision: 20/25 — Slightly broader than the canonical definition
  Conciseness: 25/25 — 31 words, concise
  Distinctiveness: 15/25 — Could be confused with Learning Graph
  Non-circularity: 25/25 — No self-reference
  Total: 85/100
```

The skill then aggregates across all definitions:

```
Overall Quality Score: 89/100
Definitions below 70: 3 (will list specific issues)
Circular definitions: 0
Average length: 34 words
```

### Threshold Logic for the Glossary Generator

```markdown
After scoring all definitions:

**Overall Score >= 85:** Report score and proceed to write output.
**Overall Score 70-84:** Proceed with note about which definitions to review.
**Overall Score < 70:** Automatically revise definitions scoring below 60.
  Re-score. If still < 70 overall, ask user whether to proceed or stop.

**For individual definitions:**
**Score >= 85:** Include as-is.
**Score 70-84:** Include with a comment in the quality report.
**Score < 70:** Revise before including. Log original and revision.
```

---

## Real Example: Course Description Analyzer Rubric

The course-description-analyzer uses a completeness-based rubric. Instead of evaluating quality of writing, it evaluates presence and completeness of required structural elements.

### The Rubric

```markdown
| Element | Points | Criteria for Full Points |
|---------|--------|--------------------------|
| Title | 5 | Clear, descriptive course title present |
| Target Audience | 5 | Specific audience identified |
| Prerequisites | 5 | Prerequisites listed or explicitly "None" |
| Main Topics Covered | 10 | Comprehensive list of 5-10 topics |
| Topics Excluded | 5 | Clear boundaries on scope |
| Learning Outcomes Header | 5 | "After this course, students will be able to..." present |
| Remember Level | 10 | 3+ specific recall outcomes |
| Understand Level | 10 | 3+ specific comprehension outcomes |
| Apply Level | 10 | 3+ specific application outcomes |
| Analyze Level | 10 | 3+ specific analysis outcomes |
| Evaluate Level | 10 | 3+ specific evaluation outcomes |
| Create Level | 10 | 3+ specific synthesis outcomes; includes capstone |
| Descriptive Context | 5 | Context on course importance and relevance |
| **Total** | **100** | |
```

### Why This Rubric Works

This rubric is entirely structural. Each element is either present and complete (full points), present but incomplete (partial points), or missing (zero points). There is almost no subjective judgment required. This makes it:

- **Consistent**: Two runs against the same file produce the same score
- **Actionable**: A score of 55 with "Create Level: 0" tells you exactly what to add
- **Automatable**: Claude can check these conditions mechanically

For content quality rubrics (like the glossary generator), some judgment is required. For completeness rubrics (like the course description analyzer), the rubric can be almost entirely mechanical.

### Threshold Logic for Course Description Analysis

```markdown
**Score >= 85:** Course description is ready for learning graph generation.
  Proceed to recommend the learning-graph-generator skill.

**Score 70-84:** Course description is adequate but incomplete.
  Report: "Score [N]/100. The following elements need strengthening: [list].
  You may proceed to learning graph generation, but the graph quality will
  be limited by these gaps."

**Score < 70:** Course description needs significant work before generating
  a learning graph.
  Report specific missing elements with examples of what should be added.
  Do not recommend proceeding to learning graph generation yet.
```

---

## Real Example: Learning Graph Quality Metrics

The learning-graph-generator uses a structural validity rubric that evaluates the mathematical properties of a directed acyclic graph (DAG) rather than content quality.

### The Rubric

```markdown
**Learning Graph Quality Score (100 points)**

Structural Integrity (40 points):
- Zero circular dependencies (DAG constraint): 20 pts
  - Any circular dependency: 0 pts (automatic failure indicator)
- All concepts reachable (connected graph): 10 pts
- No orphaned leaf nodes (every concept depends on or is depended on): 10 pts

Coverage Balance (30 points):
- Foundational concepts (zero dependencies) are 10-20% of total: 10 pts
- No single taxonomy category exceeds 30% of concepts: 10 pts
- Average dependencies per concept is 2-4: 10 pts

Vocabulary Quality (30 points):
- All concept labels in Title Case: 10 pts
- All concept labels under 32 characters: 10 pts
- Zero duplicate concept labels: 10 pts
```

### The Critical Sub-Category

Note that "Zero circular dependencies" receives 20 points but functions as a veto criterion: any circular dependency in the graph means the graph cannot be used, regardless of the other scores. The workflow handles this with special logic:

```markdown
**Special Case: Circular Dependency Detected**

If analyze-graph.py reports any circular dependencies:
Halt immediately with this message:

"CRITICAL: [N] circular dependencies detected in the learning graph.
A circular dependency means concept A depends on B, which depends on A —
creating an impossible learning order.

Circular dependencies found:
- [Concept A] → [Concept B] → [Concept A]
- [Concept X] → [Concept Y] → [Concept Z] → [Concept X]

The learning graph CANNOT be used until these cycles are removed.
Please remove the listed dependency edges and re-run this skill."

Do not calculate an overall quality score when circular dependencies exist.
```

This is an example of a sub-category that, when it fails, overrides the overall scoring calculation. Not every rubric needs this pattern, but for constraints that are mathematically required (like DAG acyclicity), it is appropriate.

---

## Scoring vs. Checklist Validation

Quality scoring is not always the right tool. Some outputs are better validated by a checklist — a list of binary yes/no conditions that must all be satisfied.

### When to Use Quality Scoring

Use a numeric quality score when:

- Output quality exists on a spectrum (not just pass/fail)
- Different users might have different acceptable thresholds
- You want to produce graduated responses (proceed / proceed with notes / ask / halt)
- Sub-category scores provide useful diagnostic information

Examples: glossary definitions, chapter content, README files, quiz questions

### When to Use Checklist Validation

Use a checklist when:

- The conditions are binary (present or absent, valid or invalid)
- All conditions must be satisfied — partial compliance is not acceptable
- Failure on any single item is a blocker

Examples: DAG cycle detection (a cycle exists or it does not), required file presence checks, syntax validation of generated JSON or YAML

### Hybrid Approach: Checklist Gates + Quality Score

Many production skills use both:

1. **Step 1:** Run checklist validation. Halt if any blocker condition is triggered.
2. **Step 2:** After passing validation, run quality scoring on the content.

```markdown
### Step 2: Validate Structure

Run checklist validation before quality scoring:

Required conditions (all must pass):
- [ ] JSON file is syntactically valid (parseable)
- [ ] All required fields present (id, label, dependencies, taxonomyID)
- [ ] No duplicate ConceptIDs
- [ ] No circular dependencies (run analyze-graph.py)

If any condition fails: Halt with specific error message.
If all conditions pass: Proceed to quality scoring.

### Step 3: Quality Scoring

Only reached if Step 2 passes completely.

[Apply quality rubric to concept labels, taxonomy distribution, dependency density...]
```

---

## Designing Your Own Rubric

The following template is a starting point for any new skill rubric. Fill in the blanks based on your skill's specific output.

### Template: 4-Category 100-Point Rubric

```markdown
## Quality Scoring Reference

Score the [output type] on four criteria (total: 100 points):

**[Category 1 Name] ([Weight] points)**
[One sentence describing what this criterion measures]

Definition of scores:
- [Weight] points: [Describe excellent performance]
- [Weight * 0.8] points: [Describe good performance]
- [Weight * 0.6] points: [Describe adequate performance]
- [Weight * 0.4] points: [Describe poor performance]
- 0-[Weight * 0.2] points: [Describe failing performance]

**[Category 2 Name] ([Weight] points)**
[One sentence describing what this criterion measures]

[Scoring levels as above]

**[Category 3 Name] ([Weight] points)**
[One sentence describing what this criterion measures]

[Scoring levels as above]

**[Category 4 Name] ([Weight] points)**
[One sentence describing what this criterion measures]

[Scoring levels as above]

**Overall Score Thresholds:**

| Score | Action |
|-------|--------|
| [High threshold]-100 | [e.g., 85-100: Deliver immediately] |
| [Mid threshold]-[High threshold-1] | [e.g., 70-84: Deliver with notes] |
| [Low threshold]-[Mid threshold-1] | [e.g., 55-69: Ask user] |
| Below [Low threshold] | [e.g., Below 55: Revise before delivering] |
```

### Worked Template Application: Quiz Question Rubric

Here is the template applied to a quiz question generator:

```markdown
## Quality Scoring Reference

Score each quiz question on four criteria (total: 100 points):

**Alignment to Bloom's Level (30 points)**
Does the question genuinely require the cognitive operation specified by its
assigned Bloom's Taxonomy level?

- 30 points: Question clearly requires the specified cognitive operation; could not
  be answered by a student operating at a lower level
- 24 points: Question mostly aligns; minor ambiguity in required cognitive level
- 18 points: Question is at the right level but the wording allows shortcuts
  (e.g., a "Analyze" question that can be answered by recall)
- 12 points: Question is at the wrong level (e.g., labeled "Create" but only
  requires recall)
- 0-9 points: Level assignment is incorrect and misleading

**Concept Specificity (25 points)**
Does the question test a specific, identifiable concept from the learning graph?

- 25 points: Question targets one specific concept; correct answer requires
  mastery of exactly that concept
- 20 points: Question targets one concept but has one minor ambiguity
- 15 points: Question could be answered with knowledge of multiple unrelated concepts
- 10 points: Question is too broad (tests general knowledge rather than specific concepts)
- 0-9 points: Question does not map to any concept in the learning graph

**Distractors Quality (25 points)**
Are the incorrect answer choices plausible but unambiguously wrong?

- 25 points: All distractors are plausible to a student who misunderstood the concept;
  none are obviously wrong
- 20 points: Most distractors are plausible; one is too easy to eliminate
- 15 points: Some distractors are implausible; a student could guess without knowledge
- 10 points: Multiple distractors are obviously wrong
- 0-9 points: Distractors are trivially wrong; question is a giveaway

**Clarity and Fairness (20 points)**
Is the question unambiguous and fair to all students?

- 20 points: Question has one unambiguous correct answer; no cultural or language bias
- 16 points: Question is clear but slightly technical in phrasing
- 12 points: Question has minor ambiguity that could cause debate about the answer
- 8 points: Question is ambiguous; reasonable argument could be made for multiple answers
- 0-7 points: Question is ambiguous, biased, or has multiple defensible answers

**Overall Score Thresholds:**

| Score | Action |
|-------|--------|
| 80-100 | Include in quiz as-is |
| 65-79 | Include with a note in the quality log |
| 50-64 | Revise before including |
| Below 50 | Discard and regenerate |
```

---

## Scoring in Practice: What Claude Actually Does

When you include a quality scoring rubric in your SKILL.md, Claude does not merely output a score. It applies the rubric through a structured self-evaluation process:

1. **It reads the rubric criteria** from the Quality Scoring section
2. **It evaluates the output** against each criterion and assigns a score with reasoning
3. **It computes the total** and applies the threshold logic
4. **It acts on the result** — proceeding, noting, asking, or halting

The scoring narration might look like this in practice:

```
Evaluating definition for "Directed Acyclic Graph":

Precision: 22/25 — Captures the mathematical concept accurately, though
"directed" could be more clearly explained as "one-directional edges."

Conciseness: 25/25 — 28 words, no filler.

Distinctiveness: 20/25 — Could be confused with "Directed Graph" by a
student who does not yet know the difference.

Non-circularity: 25/25 — No self-reference.

Total: 92/100 — Excellent. Proceeding.
```

This narration is valuable even if the user never explicitly requests it, because it makes the scoring transparent. If the score is unexpectedly low, the user can see exactly why.

---

## Calibrating Thresholds for Your Domain

The standard thresholds (85/70/55) are starting points. Adjust them based on the stakes and revision cost of your output:

**Raise thresholds when:**
- Output will be published without human review
- Errors in the output are difficult or costly to fix
- The audience requires high precision (medical, legal, financial domains)

**Lower thresholds when:**
- Output is a draft intended for human revision
- The cost of re-running the skill is low
- The user explicitly wants to see lower-quality output for reference or iteration

**Example: Medical education content**

```markdown
**Overall Score Thresholds:**

| Score | Action |
|-------|--------|
| 90-100 | Deliver immediately |
| 80-89 | Deliver with specific improvement notes |
| 70-79 | Ask: "Score [N]/100. Recommend revision. Deliver or revise?" |
| Below 70 | Halt. Medical content with score below 70 should not be delivered. |
```

**Example: First-draft blog content**

```markdown
**Overall Score Thresholds:**

| Score | Action |
|-------|--------|
| 75-100 | Deliver immediately |
| 60-74 | Deliver with notes about weakest sections |
| Below 60 | Ask: "Score [N]/100. Continue or revise?" |
```

---

## Common Rubric Design Mistakes

**Mistake 1: Criteria that overlap**

If two criteria measure the same thing, scores will be inflated and the diagnostic value is lost.

```
# Wrong: Precision and Accuracy measure the same thing
Precision (25 pts): Is the definition correct?
Accuracy (25 pts): Does the definition accurately describe the concept?

# Right: Each criterion measures a distinct dimension
Precision (25 pts): Does the definition target the specific concept exactly,
  without being too broad or too narrow?
Accuracy (25 pts): Are all claims in the definition factually correct?
```

**Mistake 2: Subjective criteria without anchor descriptions**

A criterion like "Is the definition good?" gives Claude nothing to evaluate against. Every criterion needs level descriptions that anchor the score to observable properties.

```
# Wrong: No anchor descriptions
Clarity (25 pts): Is the definition clear?

# Right: Anchored to observable properties
Clarity (25 pts):
- 25: An intelligent reader unfamiliar with the domain can understand the definition
  without additional context
- 15: The definition is understandable to someone with general domain familiarity
- 5: The definition requires domain expertise to interpret correctly
```

**Mistake 3: Weights that do not reflect actual importance**

If you use 25-25-25-25 but actually care far more about one criterion, the score will not reflect real quality. Be honest about the relative importance of your criteria.

**Mistake 4: A threshold of exactly 70 as both "proceed" and "ask"**

Define thresholds as ranges with clear boundaries. "Score >= 70: proceed. Score < 70: ask." is clear. "Score = 70: unclear." is ambiguous. Use `>=` and `<` with clear boundaries.

---

## Key Takeaways

- Quality scoring transforms skills from generators into self-evaluating agents
- The 100-point scale is standard across the McCreary ecosystem because it is intuitive and provides natural weighting granularity
- Sub-categories make quality diagnostic: a score of 73/100 with "Distinctiveness: 8/25" is more actionable than just "73/100"
- Standard thresholds are 85 (excellent/deliver), 70 (good/deliver with notes), 55 (adequate/ask), below 55 (needs work/halt)
- Some criteria function as veto conditions: if circular dependencies exist, the learning graph score is irrelevant
- Use quality scoring for spectrum outputs; use checklists for binary conditions; combine them in the order checklist gate → quality score
- Calibrate thresholds to the stakes of your domain — raise them for high-stakes content, lower them for first-draft work
- Anchor every criterion level to observable, measurable properties — not subjective impressions

This chapter completes the Skill Anatomy section of this guide. You now have everything you need to write complete, production-quality SKILL.md files with proper frontmatter, structured workflows, and self-evaluating quality scoring systems. In Chapter 8, we move into Advanced Patterns — starting with meta-skill routers that consolidate multiple skills under a single invocation point.
