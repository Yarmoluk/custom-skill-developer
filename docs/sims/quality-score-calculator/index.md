# Skill Quality Score Calculator

Use the sliders below to score your Agent Skill across seven dimensions. The total score updates in real time along with a letter grade and a verdict. Load a preset to see how a minimal, good, or production-ready skill compares.

<div style="display: flex; justify-content: flex-end; margin-bottom: 8px;">
  <a href="main.html" target="_blank"
     style="font-size: 13px; color: #007AFF; text-decoration: none; border: 1px solid #007AFF;
            padding: 4px 12px; border-radius: 6px; font-weight: 600;">
    Open Fullscreen
  </a>
</div>

<iframe
  src="main.html"
  width="100%"
  height="650"
  style="border: none; border-radius: 12px; display: block;"
  title="Skill Quality Score Calculator">
</iframe>

## Scoring Dimensions

| Dimension | Max Points | What It Checks |
|---|---|---|
| Frontmatter Compliance | 20 | Required YAML fields: name, description, version, author, category, tags |
| Structure Compliance | 20 | All required top-level sections present and in order |
| Workflow Quality | 15 | Step clarity, error handling paths, logical flow |
| Quality Scoring System | 15 | Internal success metrics, rubrics, self-evaluation criteria |
| Token Efficiency | 10 | Concise prompts — no bloat, repetition, or over-specification |
| Ecosystem Quality | 10 | Tool declarations, cross-skill integration, discovery metadata |
| Cross-Platform Readiness | 10 | Works in Claude.ai, Claude Code CLI, and API without modification |

## Grade Scale

| Score | Grade | Verdict |
|---|---|---|
| 85 – 100 | A | Production ready. Ship it. |
| 70 – 84 | B | Solid foundation. Address the gaps before publishing. |
| 55 – 69 | C | Needs work. Focus on the lowest-scoring dimensions. |
| 40 – 54 | D | Significant gaps. Review the guide chapters for each weak area. |
| 0 – 39 | F | Start with Chapter 3: Your First Skill. |
