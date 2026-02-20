# Meta-Skill Routing Simulator

When a meta-skill receives a request, it does not load every reference file into context. It inspects the request, extracts keywords, and routes to exactly one guide — loading only what is needed.

This simulator lets you see that decision process in real time.

<div style="width: 100%; margin: 1.5rem 0 0.5rem;">
  <div style="display: flex; justify-content: flex-end; margin-bottom: 0.5rem;">
    <a
      href="./main.html"
      target="_blank"
      style="
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #191920;
        border: 1px solid #28282D;
        border-radius: 6px;
        color: #007AFF;
        font-size: 12px;
        font-weight: 600;
        padding: 6px 12px;
        text-decoration: none;
        transition: border-color 0.2s;
      "
    >
      &#x26F6; Open fullscreen
    </a>
  </div>
  <iframe
    src="./main.html"
    style="
      width: 100%;
      height: 550px;
      border: 1px solid #28282D;
      border-radius: 10px;
      background: #0C0C10;
    "
    scrolling="no"
    title="Meta-Skill Routing Simulator"
  ></iframe>
</div>

## How it works

The meta-skill router follows three steps on every invocation:

1. **Keyword extraction.** The request is tokenized and stop words are removed. The remaining terms are matched against each route's keyword list.

2. **Route selection.** The reference file with the most keyword hits is selected. All other guides are skipped entirely.

3. **Selective loading.** Only the matched guide is injected into context before Claude generates its response.

## The routing table

| Keywords | Reference file | Library |
|----------|---------------|---------|
| chart, bar, line, pie, donut | `chartjs-guide.md` | Chart.js |
| timeline, dates, chronological | `timeline-guide.md` | vis-timeline |
| network, graph, nodes, edges | `vis-network-guide.md` | vis-network |
| map, geographic, location | `map-guide.md` | Leaflet |
| flowchart, sequence, diagram | `mermaid-guide.md` | Mermaid |
| simulation, physics, animation | `p5-guide.md` | p5.js |
| venn, overlap, sets | `venn-guide.md` | Venn.js |

## Why token efficiency matters

Loading all seven reference guides on every invocation would cost roughly 5,600 tokens of context before Claude writes a single line of code. The router loads one guide — typically 650–900 tokens — and skips the rest. That is an 85–90% reduction in reference overhead, which translates directly to faster responses and lower API costs at scale.
