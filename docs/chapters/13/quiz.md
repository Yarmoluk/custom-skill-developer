# Chapter 13 Quiz

Test your understanding of code generation skills, MicroSim patterns, and template-driven output.

---

**Question 1** *(Bloom's: Remember)*
*Concept: MicroSim generation skill (C152)*

What is a MicroSim in the context of Claude Code code generation skills?

- [ ] A) A small Python script that runs automated tests on a skill
- [ ] B) A self-contained, single-file interactive simulation used in intelligent textbooks, produced as a deployable standalone HTML artifact
- [ ] C) A compressed version of a skill that uses fewer tokens
- [ ] D) A minimal skill definition with only frontmatter and no workflow steps

??? success "Answer"
    **B) A self-contained, single-file interactive simulation used in intelligent textbooks, produced as a deployable standalone HTML artifact**

    MicroSims are self-contained, single-file interactive simulations — the canonical output of a MicroSim generation skill. The standard output is a complete, deployable `index.html` with embedded CSS and JavaScript, accompanied by a `metadata.json` describing the simulation. A MicroSim generation skill produces a complete, ready-to-use artifact every invocation, not a code snippet requiring additional assembly. This "complete artifact" property is what distinguishes code generation skills from general-purpose code assistance.

---

**Question 2** *(Bloom's: Understand)*
*Concept: Template pattern for code output (C153)*

Why do code generation skills use a strict HTML template structure rather than letting Claude generate the HTML structure from scratch each time?

- [ ] A) The HTML template reduces the skill's SKILL.md file size
- [ ] B) A fixed template ensures consistent base layout, responsive behavior, and correct boilerplate across every invocation — eliminating the variability that occurs when structure is improvised
- [ ] C) Claude cannot generate valid HTML without a template
- [ ] D) Templates are required by browser standards for iframe embedding

??? success "Answer"
    **B) A fixed template ensures consistent base layout, responsive behavior, and correct boilerplate across every invocation — eliminating the variability that occurs when structure is improvised**

    Template-driven output is the code generation equivalent of workflow steps in text-generating skills: it constrains the structure so Claude focuses on the meaningful variation (the simulation logic, data, and interactivity) rather than reinventing the scaffold each time. Without a template, invocations might use different viewport meta tags, different CSS reset approaches, or forget the responsive wrapper. The template encodes all best-practice boilerplate once; every generated MicroSim inherits it automatically.

---

**Question 3** *(Bloom's: Apply)*
*Concept: JavaScript library selection logic (C156)*

A skill is generating an interactive MicroSim for a concept that requires particle physics simulation with continuous animation. Which JavaScript library should it select, and why?

- [ ] A) Chart.js — because it is the default for all data visualizations
- [ ] B) p5.js — because it is purpose-built for creative coding and continuous animation loops, making it appropriate for physics simulations
- [ ] C) React — because component-based architecture scales better for complex simulations
- [ ] D) D3.js — because it handles all types of visualizations equally well

??? success "Answer"
    **B) p5.js — because it is purpose-built for creative coding and continuous animation loops, making it appropriate for physics simulations**

    Library selection logic in a code generation skill matches the visualization type to the most appropriate library. p5.js is purpose-built for creative coding and continuous animation — its `draw()` loop runs at 60fps, making it ideal for physics simulations, particle systems, and anything requiring frame-by-frame updates. Chart.js excels at static or near-static data charts (bar, line, pie). D3.js is powerful but heavy — appropriate for complex data-driven documents. The skill should select the library based on the interaction model required, not use a single default for all cases.

---

**Question 4** *(Bloom's: Apply)*
*Concept: Output validation for generated code (C154)*

A MicroSim generation skill produces an `index.html` file. What output validation should the skill apply before declaring completion?

- [ ] A) No validation is needed since Claude generates syntactically correct HTML by default
- [ ] B) Ask the user to open the file in a browser and report back whether it works
- [ ] C) Check that the required structural elements are present (DOCTYPE, viewport meta, canvas or chart container, required library CDN links, and the JavaScript entry point), and flag any that are missing
- [ ] D) Validate that the file is exactly the same length as the template

??? success "Answer"
    **C) Check that the required structural elements are present (DOCTYPE, viewport meta, canvas or chart container, required library CDN links, and the JavaScript entry point), and flag any that are missing**

    Output validation for generated code focuses on structural completeness, not byte-for-byte identity with a template. The validation checks: Does the HTML include the correct DOCTYPE? The responsive viewport meta tag? The required library CDN link? A container element with the expected ID? A JavaScript entry point that calls the main function? These checks can be performed without running a browser. Missing any of these elements produces a broken simulation that users cannot diagnose without the validation feedback.

---

**Question 5** *(Bloom's: Analyze)*
*Concept: Standalone HTML output pattern (C159)*

What is the primary advantage of the standalone HTML output pattern — embedding all CSS and JavaScript within a single HTML file rather than using separate files?

- [ ] A) Single-file HTML loads faster than multi-file projects
- [ ] B) The simulation is deployable anywhere without a build step, server configuration, or asset management — a single file can be opened locally, dropped into a textbook's `docs/sims/` directory, or shared directly
- [ ] C) Single-file HTML is required for MkDocs Material theme compatibility
- [ ] D) Embedded JavaScript cannot be blocked by browser security policies

??? success "Answer"
    **B) The simulation is deployable anywhere without a build step, server configuration, or asset management — a single file can be opened locally, dropped into a textbook's `docs/sims/` directory, or shared directly**

    The standalone HTML pattern prioritizes deployability over separation of concerns. A single self-contained HTML file can be opened in any browser locally, embedded in a MkDocs Material textbook by dropping it into `docs/sims/`, emailed as an attachment, or hosted on any static server without configuration. Multi-file projects require maintaining correct relative paths, running a dev server, or managing asset bundling — complexity that a textbook MicroSim does not justify. Self-containment makes MicroSims usable without infrastructure.

---
