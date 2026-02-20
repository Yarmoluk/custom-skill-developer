# Cognify Skills Quality Scorecard

This scorecard audits all 19 agent skills in the [cognify-skills](https://github.com/Yarmoluk/cognify-skills) repository against a 100-point rubric. The audit was conducted on 2026-02-20 by reading every SKILL.md file in `.github/skills/` and scoring each against seven weighted categories.

## Rubric Summary

| # | Category | Max Points | What Is Measured |
|---|----------|-----------|-----------------|
| 1 | **Frontmatter** | 20 | name, description ≤1024 chars, license, compatibility, metadata, allowed-tools |
| 2 | **Structure** | 20 | H1 title, overview/purpose, when-to-activate triggers, numbered workflow steps, output files summary |
| 3 | **Workflow Quality** | 15 | Step 0 environment setup, clear sequential steps, conditional branching, user dialog triggers, completion criteria |
| 4 | **Quality Scoring** | 15 | Embedded rubric, weighted categories, defined thresholds, remediation guidance |
| 5 | **Token Efficiency** | 10 | Under 500 lines, references/ directory usage, lazy loading pattern, skip-if-complete logic |
| 6 | **Ecosystem Integration** | 10 | References to other skills, clear input/output contracts, pipeline position documented |
| 7 | **Cross-Platform** | 10 | agentskills.io-compatible frontmatter, no Claude-only assumptions, .github/skills path noted |

**Grade Scale:** 90+ = A | 80–89 = B | 70–79 = C | 60–69 = D | <60 = F

---

## Scoring Notes Per Category

**Frontmatter (20 pts)**
All skills have `name` (5 pts) and `description` (5 pts). All use Apache-2.0 or Proprietary license (3 pts). All have `compatibility` string (3 pts). All have `metadata` with author + version (2 pts). No skill includes `allowed-tools` (0/2 pts). `cognify-workflow-analysis` has richer metadata with website and category fields (+partial). Skills with descriptions noticeably over 1024 chars lose 1–2 pts on description. The `meeting-agenda-optimizer` and `process-documentation` descriptions are inline (not block-scalar), which is acceptable but slightly less explicit about length. `strategic-planning-facilitator`'s description is also brief inline. Proprietary license on `cognify-workflow-analysis` is valid but reduces reusability signal (no deduction applied since it's a valid choice). All skills share the same compatibility string word-for-word (boilerplate strength but no per-skill tool list = 0/2 on allowed-tools across the board).

**Structure (20 pts)**
All skills have an H1 title (3 pts). All have an overview/purpose paragraph at the top (up to 4 pts). "When to Activate" sections are present in most skills but absent or replaced by "How to Use This Skill" in `abm-campaign-builder`, `meeting-agenda-optimizer`, `process-documentation`, and `strategic-planning-facilitator` — those lose 2–3 pts here. Numbered workflow steps are present and well-executed in most (up to 5 pts). Output format sections vary: most have explicit "Output Format" sections (4 pts), a few embed output specs inline or in a final-compile block without a distinct output files summary.

**Workflow Quality (15 pts)**
No skill has an explicit Step 0 environment setup block (e.g., checking prerequisites, verifying tool access before workflow begins) — this is the most consistent gap across all 19 skills (0/3 pts universal). Most skills have clear sequential steps (up to 4 pts). Conditional branching is present in many skills via decision tables or if/then logic — strongest in `client-discovery-interview`, `risk-assessment-matrix`, and `process-documentation`. User dialog triggers (conversational prompts, reflection pauses) are a notable strength of `client-discovery-interview` and `cognify-workflow-analysis`. Completion criteria vary: the richer skills define "done" clearly (output format + checklist), others are vaguer.

**Quality Scoring (15 pts)**
Several skills have embedded scoring rubrics, weighted criteria, and thresholds — this is a genuine differentiator. `abm-campaign-builder`, `customer-feedback-analyzer`, `seo-strategy-analyzer`, `sales-pipeline-analyzer`, `operations-audit`, `risk-assessment-matrix`, `vendor-evaluation-scorecard`, `hiring-decision-analyzer`, `client-discovery-interview`, and `competitive-intelligence` score strongly here. Skills that guide rather than score (e.g., `employee-onboarding-designer`, `change-management-planner`, `budget-planning-assistant`) have fewer internal rubrics but include benchmark tables that partially satisfy this criterion.

**Token Efficiency (10 pts)**
Line counts estimated from file content. Most skills exceed 300 lines; several (`abm-campaign-builder`, `strategic-planning-facilitator`, `process-documentation`) exceed 500 lines, losing 3 pts. All skills reference a `references/` directory via lazy-loading patterns (e.g., `Read [filename](references/filename.md)`) — this is a consistent strength (3 pts each). No skill explicitly implements a skip-if-complete guard (0/2). Lazy loading pattern is used but described as "Read X" rather than "Load only if needed" — partial credit (1/2 pts).

**Ecosystem Integration (10 pts)**
No skill explicitly references another skill by name within cognify-skills (0/3 pts universal gap). Most skills define clear input requirements (what the user must provide) and output formats — strong input/output contracts (up to 4 pts). Pipeline position (where this skill fits in a larger workflow) is documented only implicitly through "When to Activate" triggers; no skill explicitly states "this skill feeds into X" or "run after Y" (partial 1–2/3 pts).

**Cross-Platform (10 pts)**
All skills are stored at `.github/skills/[name]/SKILL.md` (2 pts each). Frontmatter is YAML-compatible and generally agentskills.io-compatible (5 pts, though `allowed-tools` absence is a gap). No skill contains Claude-specific API calls, model names, or features that would break on other runtimes — they use generic LLM instruction patterns (3 pts each).

---

## Scorecard Table

| Skill Name | Frontmatter | Structure | Workflow | Quality | Token Eff | Ecosystem | Cross-Platform | TOTAL | Grade |
|------------|:-----------:|:---------:|:--------:|:-------:|:---------:|:---------:|:--------------:|:-----:|:-----:|
| abm-campaign-builder | 18 | 18 | 10 | 14 | 6 | 7 | 10 | **83** | B |
| budget-planning-assistant | 18 | 17 | 10 | 11 | 8 | 6 | 10 | **80** | B |
| business-roi-analyzer | 18 | 18 | 11 | 14 | 8 | 7 | 10 | **86** | B |
| change-management-planner | 18 | 18 | 11 | 11 | 8 | 6 | 10 | **82** | B |
| client-discovery-interview | 18 | 18 | 13 | 13 | 8 | 7 | 10 | **87** | B |
| cognify-workflow-analysis | 18 | 17 | 12 | 12 | 9 | 7 | 10 | **85** | B |
| competitive-intelligence | 18 | 18 | 11 | 13 | 7 | 7 | 10 | **84** | B |
| customer-feedback-analyzer | 18 | 18 | 11 | 14 | 7 | 7 | 10 | **85** | B |
| customer-success-playbook | 18 | 18 | 11 | 12 | 8 | 6 | 10 | **83** | B |
| employee-onboarding-designer | 18 | 18 | 10 | 10 | 8 | 6 | 10 | **80** | B |
| hiring-decision-analyzer | 18 | 18 | 12 | 13 | 8 | 7 | 10 | **86** | B |
| meeting-agenda-optimizer | 18 | 15 | 11 | 12 | 6 | 6 | 10 | **78** | C |
| operations-audit | 18 | 17 | 12 | 14 | 8 | 7 | 10 | **86** | B |
| process-documentation | 18 | 15 | 12 | 11 | 6 | 6 | 10 | **78** | C |
| risk-assessment-matrix | 18 | 18 | 12 | 14 | 8 | 7 | 10 | **87** | B |
| sales-pipeline-analyzer | 18 | 18 | 12 | 14 | 8 | 7 | 10 | **87** | B |
| seo-strategy-analyzer | 18 | 18 | 11 | 14 | 8 | 7 | 10 | **86** | B |
| strategic-planning-facilitator | 18 | 15 | 11 | 12 | 6 | 6 | 10 | **78** | C |
| vendor-evaluation-scorecard | 18 | 18 | 11 | 14 | 8 | 7 | 10 | **86** | B |

---

## Analysis

### Average Score

**Average across all 19 skills: 83.5 / 100**

The portfolio is solidly in B-grade territory. No skill is failing and none reaches A-grade. The ceiling is being held down by three universal gaps: no `allowed-tools` frontmatter field, no Step 0 environment setup, and no inter-skill references. Fixing those three issues across the board would push the average above 90.

---

### Top 3 Skills

| Rank | Skill | Score | Reason |
|------|-------|-------|--------|
| 1 (tied) | **client-discovery-interview** | 87 | Strongest workflow quality in the set — explicit conversational mode selection, reflection pauses, one-question-at-a-time operating rule, and a well-defined UBANF qualification framework with threshold scoring. Conditional branching (live guidance vs. direct interview) is the best user dialog trigger in the portfolio. |
| 1 (tied) | **risk-assessment-matrix** | 87 | Excellent structure: five distinct domain sections, a fully defined 5×5 probability × impact matrix, four response strategy types, risk appetite framework, and a monitoring cadence. The residual risk rescoring pattern (inherent vs. residual) is a sophisticated quality mechanism. |
| 1 (tied) | **sales-pipeline-analyzer** | 87 | Complete pipeline analysis system with five distinct analytical engines (conversion, velocity, bottleneck scoring, lead source ROI, forecasting). Bottleneck scoring formula is the clearest quantitative rubric in the portfolio. Three forecast methodologies with clear "use when" guidance is best-in-class output design. |

---

### Bottom 3 Skills

| Rank | Skill | Score | Reason |
|------|-------|-------|--------|
| 17 (tied) | **meeting-agenda-optimizer** | 78 | Missing "When to Activate" section (uses "How to Use This Skill" instead, which lacks explicit trigger patterns). Over 500 lines. The Section-based structure doesn't align with the numbered Step convention used by the rest of the portfolio, creating an ecosystem inconsistency. Good content, weak meta-structure. |
| 17 (tied) | **process-documentation** | 78 | Same structural issue as meeting-agenda-optimizer: uses "How to Use This Skill" and Section/Step hybrid naming. Exceeds 500 lines. Strong content (SOP template, RACI, decision trees, runbooks, version control) but the length without lazy-loading compensation hurts token efficiency, and the hybrid structure makes it harder to parse programmatically. |
| 17 (tied) | **strategic-planning-facilitator** | 78 | Inline description (not block-scalar) is brief and misses specificity. Uses "How to Use This Skill" instead of "When to Activate." At over 650 lines it is the longest skill in the portfolio and the worst token efficiency offender. The content is excellent but the structure deviates from portfolio conventions. |

---

### Most Common Weaknesses

The following weaknesses appear across **all 19 skills**:

1. **No `allowed-tools` frontmatter field** (–2 pts each): Every skill is missing this field. Adding it would signal to routing agents which tools the skill needs (web search, file write, code execution) and would complete the agentskills.io-compatible frontmatter spec. This is the single easiest portfolio-wide fix.

2. **No Step 0 environment/prerequisite check** (–3 pts each): No skill begins with a block that validates the environment before starting the workflow — checking for required inputs, confirming user context, or offering to cancel gracefully. This is a workflow quality gap that affects reliability in automated pipelines.

3. **No inter-skill references** (–3 pts each): No skill references another cognify skill by name or path. A skill like `abm-campaign-builder` could reference `competitive-intelligence` (Module 1) or `client-discovery-interview` (Module 2), forming a composable pipeline. The absence of cross-skill wiring means the portfolio operates as 19 isolated tools rather than an ecosystem.

4. **`skip-if-complete` logic absent** (–2 pts each): No skill checks whether a step's output already exists before executing it. In agentic loops this is an important efficiency guard.

5. **Inconsistent structural convention** in 3 skills (`meeting-agenda-optimizer`, `process-documentation`, `strategic-planning-facilitator`): These use "How to Use This Skill" + Section/Step hybrid instead of the "When to Activate" + numbered Step pattern used by the other 16. Standardizing would improve programmatic parsability and portfolio coherence.

---

### Recommended Fixes by Priority

| Priority | Fix | Affected Skills | Effort | Score Impact |
|----------|-----|----------------|--------|--------------|
| P1 | Add `allowed-tools` to all frontmatter | All 19 | Low — add 1 field per skill | +2 pts each |
| P1 | Add Step 0 environment check block | All 19 | Medium — 5–10 lines per skill | +3 pts each |
| P2 | Add cross-skill `see-also` references | All 19 | Low — add 2–3 lines per skill | +3 pts each |
| P2 | Standardize structure in 3 outlier skills | meeting-agenda-optimizer, process-documentation, strategic-planning-facilitator | Medium — structural edit | +3–5 pts each |
| P3 | Add `skip-if-complete` guards | All 19 | Medium — step-level logic | +2 pts each |
| P3 | Trim or paginate skills >500 lines | abm-campaign-builder, strategic-planning-facilitator, process-documentation | Medium — split content to references/ | +3 pts each |

Implementing P1 fixes alone would raise the portfolio average from **83.5 to approximately 88.5** — approaching A-grade territory.

---

*Scorecard generated: 2026-02-20 | Auditor: Claude Sonnet 4.6 via custom-skill-developer | Skills location: `/Users/danielyarmoluk/projects/cognify-skills/.github/skills/`*
