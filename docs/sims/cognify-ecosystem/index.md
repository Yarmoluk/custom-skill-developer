# Cognify Skill Ecosystem

Explore how 19 production Agent Skills connect across the Cognify business intelligence pipeline. Click any node to see its outputs, upstream dependencies, and downstream consumers.

<div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center;margin-bottom:1rem;">
  <a href="./main.html" target="_blank" style="display:inline-flex;align-items:center;gap:6px;background:#007AFF;color:#fff;font-size:13px;font-weight:600;padding:8px 16px;border-radius:8px;text-decoration:none;">
    Open Fullscreen
  </a>
  <span style="font-size:13px;color:#8E8E93;">21 nodes &nbsp;·&nbsp; 28 edges &nbsp;·&nbsp; 6 phases &nbsp;·&nbsp; vis-network</span>
</div>

<iframe
  src="./main.html"
  width="100%"
  height="700px"
  style="border:1px solid #28282D;border-radius:12px;display:block;"
  title="Cognify Skill Ecosystem — interactive dependency graph"
></iframe>

---

## What This Sim Shows

The graph maps the **complete Cognify skill ecosystem** — every skill that powers the ABM methodology from market discovery through ongoing operations. Nodes are colored by pipeline phase:

| Phase | Color | Skills |
|-------|-------|--------|
| **Discovery** | Blue | market-intel-generator, market-sizing-calculator, competitor-mapper |
| **Analysis** | Purple | buyer-persona-builder, pain-point-analyzer, decision-mapper |
| **Strategy** | Cyan | value-prop-generator, positioning-matrix, pricing-strategist |
| **Execution** | Orange | outreach-sequencer, content-personalizer, objection-handler, crm-field-mapper |
| **Operations** | Green | pipeline-tracker, win-loss-analyzer, territory-planner, campaign-optimizer, roi-calculator, qbr-generator |
| **Ecosystem** | White | Custom Skill Developer (this guide), Skill Quality Analyzer |

Edges show **data flow** — which skill's output feeds into which skill's input. This is pipeline orchestration in practice: skills don't call each other directly, they chain through file contracts.

---

## How to Read the Graph

- **Click a node** to see its detail panel: description, outputs, and connection counts
- **Use phase filter buttons** at the top to isolate pipeline stages
- **Drag nodes** to rearrange the layout
- **Scroll to zoom** in and out
- **Stats bar** at the bottom shows totals for nodes, edges, and phases

!!! tip "Architecture insight"
    The graph reveals a clear funnel pattern: Discovery skills feed Analysis, which feeds Strategy, which feeds Execution, which feeds Operations. The Ecosystem layer (this guide + the analyzer) sits outside the funnel — it's meta-tooling that improves the skills themselves.

!!! note "Related"
    Chapter 8 covers meta-skill routing patterns. Chapter 11 covers pipeline orchestration — the technique that makes this ecosystem work. The [Skill Quality Analyzer](https://github.com/Yarmoluk/skill-quality-analyzer) scores each node against a 100-point rubric.
