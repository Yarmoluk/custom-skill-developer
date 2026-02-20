# Chapter 10: Session Logging

Complex skills do complex work. A skill that generates a 12-chapter textbook, processes a batch of 20 reports, or orchestrates multiple downstream tools can run for an hour before completing. During that time, the context window fills incrementally with conversation history, file reads, and generated output. Eventually, the session must be compacted or a new session started — and the work must continue.

Session logging is the infrastructure that makes continuation possible. It is also the infrastructure that makes debugging possible, quality measurement possible, and batch resumption possible.

This chapter covers why session logs exist, what they must contain, the conventions used across the skill ecosystem, state tracking for batch operations, and how to build skills that detect and resume from prior session state.

---

## Why Session Logging Exists

### The Context Window Fills

Every token generated — by Claude and by the user — accumulates in the context window. In a long session involving deep file reads, iterative revisions, and substantial output generation, the window fills faster than you might expect.

When context fills, there are two options:

1. **Compact the session** — Claude Code summarizes the conversation, freeing space but losing detail
2. **Start a new session** — the fresh session has no memory of what was accomplished

Without session logs, both options destroy continuity. After compaction, Claude may not remember that chapters 1-7 are complete and chapter 8 is in progress. After a new session, Claude has no information at all.

With a session log, the first step in any continuation session is a single, cheap read: load the log, understand the state, resume from exactly where work stopped. The log is the external memory that survives context resets.

### Batch Operations Fail Partway Through

When a skill processes 20 items in a batch, statistical reality guarantees occasional failures — a malformed input, an unexpected file format, a tool call that times out. Without state tracking, the only recovery option is to re-run the entire batch and deduplicate the results.

With a session log and a state file, recovery is precise: identify the failed item, fix the input, and resume from that item. Items 1-19 that completed successfully are not touched.

### Quality is Invisible Without Measurement

If a skill produces output without logging anything, you cannot answer the question "are our outputs getting better or worse over time?" You cannot identify which variants have lower quality scores. You cannot correlate output quality with session duration or input complexity.

Session logs create the data that makes quality measurement possible. Every logged session contributes to a corpus that answers questions like: "The technical-spec variant has an average quality score of 7.2, while the executive-summary variant scores 8.8 — what accounts for the gap?"

---

## The Logs Directory Convention

Every skill that produces substantial output should write logs to a `logs/` directory relative to the working directory. The convention used across the skill ecosystem is:

```
./logs/[skill-name]-v[VERSION]-[YYYY-MM-DD].md
```

Examples:
```
./logs/report-generator-v1.2.0-2024-11-15.md
./logs/microsim-generator-v2.0.1-2024-11-15.md
./logs/chapter-writer-v1.0.0-2024-11-14.md
```

### Why Markdown, Not JSON?

Logs use `.md` format (not `.json`) for two reasons:

1. **Human readability** — a developer can open a log and understand what happened without a parser
2. **Claude readability** — when Claude reads a session log to resume work, markdown is parsed naturally without any schema overhead

State files (covered later) use `.json` because they are read programmatically and precision matters more than human readability.

### One Log Per Skill Per Day

The convention is one log file per skill per calendar day. If a skill is invoked three times in a day, all three invocations append to the same log file under separate `## Session [N]` headers. This keeps the log corpus from proliferating into dozens of tiny files.

The exception is batch operations, where each batch run gets its own log file identified by batch ID.

---

## Log Format Reference

A complete session log entry has seven sections. Not every section applies to every skill — a simple single-purpose skill might omit timing details — but more complex skills should populate all seven.

```markdown
# [Skill Name] Session Log
**Version:** [x.y.z] | **Date:** [YYYY-MM-DD] | **Session:** [N]

## Invocation

**Trigger:** [How the skill was invoked — full command or description]
**Variant:** [Which variant was selected, if meta-skill]
**Routing Confidence:** [High / Medium / Low]

## Timing

| Phase | Start | End | Duration |
|-------|-------|-----|----------|
| Routing resolution | 14:03:22 | 14:03:24 | 2s |
| Reference guide load | 14:03:24 | 14:03:25 | 1s |
| Draft generation | 14:03:25 | 14:11:40 | 8m 15s |
| Quality scoring | 14:11:40 | 14:11:55 | 15s |
| Log write | 14:11:55 | 14:12:00 | 5s |
| **Total** | | | **8m 38s** |

## Files Created

| File | Size | Status |
|------|------|--------|
| `./reports/executive-summary-2024-11-15.md` | 612 words | Complete |
| `./reports/executive-summary-2024-11-15-appendix.md` | 203 words | Complete |

## Token Usage Estimate

| Phase | Estimated Tokens |
|-------|------------------|
| Skill load (SKILL.md) | 1,840 |
| Reference guide load | 720 |
| User input | 145 |
| Files read | 0 |
| Claude output | 3,200 |
| **Session total** | **5,905** |

## Quality Score

**Overall Score:** 8.2 / 10

| Criterion | Score | Note |
|-----------|-------|------|
| Findings are quantified | 9/10 | All 4 findings have numbers |
| Recommendations have owners | 7/10 | 2/3 have explicit owners |
| Register appropriate for audience | 9/10 | Clean executive language |
| Length within target | 8/10 | 612 words, target 400-600 |

## Decisions Made

- Routed to executive-summary variant (confidence: high — "board" keyword present)
- Excluded raw financials from body; referenced as appendix per audience guidance
- Used Q3 vs Q2 comparison frame rather than Q3 vs plan (data provided supported both)

## Resume State

**Status:** Complete
**Next Step:** N/A — standalone invocation
**Outstanding:** None
```

Each section serves a purpose:

- **Invocation** — lets future sessions understand exactly what was requested
- **Timing** — identifies bottlenecks and tracks performance over time
- **Files Created** — tells a resume session exactly what exists and is ready
- **Token Usage Estimate** — informs optimization decisions
- **Quality Score** — creates the measurement corpus
- **Decisions Made** — documents judgment calls that might need to be reversed or referenced
- **Resume State** — the most critical section for continuation sessions

---

## What to Log: A Decision Framework

Not every detail belongs in a log. Over-logging wastes tokens when Claude reads the log to resume. Under-logging defeats the purpose. Apply this decision framework:

**Always log:**
- Which variant was selected and at what confidence
- What files were created (name, size, completion status)
- Overall quality score
- Resume state (complete / in-progress / blocked)
- Any decision that involved a judgment call rather than a deterministic rule

**Log if the skill runs for more than 5 minutes:**
- Timing data for each phase
- Token usage estimates

**Log if the skill is part of a batch or pipeline:**
- Item ID or step number
- Whether this item/step is unblocked for the next stage
- Dependencies satisfied

**Do not log:**
- The full text of generated outputs (they are in the output files)
- Intermediate draft revisions
- Standard workflow steps that completed normally (only log deviations)
- Anything that is recoverable from the output files themselves

The goal of a log is to reconstruct session state, not to duplicate output. If Claude can derive the information by reading the output file, it should not be duplicated in the log.

---

## State Tracking with JSON Files

For batch operations and pipeline orchestration, a small JSON state file provides precise status tracking at minimal token cost.

### The sim-status.json Pattern

The name "sim-status.json" comes from the MicroSim Generator skill ecosystem, but the pattern applies to any batch skill. The file tracks the lifecycle state of each item in a batch:

```json
{
  "batch_id": "textbook-ch-batch-2024-11-15",
  "skill": "chapter-writer",
  "version": "1.0.0",
  "created": "2024-11-15T10:00:00Z",
  "last_updated": "2024-11-15T14:23:11Z",
  "total_items": 12,
  "summary": {
    "complete": 7,
    "in_progress": 1,
    "pending": 4,
    "failed": 0
  },
  "items": {
    "ch-01": {
      "status": "complete",
      "output_file": "./docs/chapters/01/index.md",
      "quality_score": 8.4,
      "word_count": 3241,
      "completed_at": "2024-11-15T10:47:33Z"
    },
    "ch-02": {
      "status": "complete",
      "output_file": "./docs/chapters/02/index.md",
      "quality_score": 7.9,
      "word_count": 2987,
      "completed_at": "2024-11-15T11:31:05Z"
    },
    "ch-08": {
      "status": "in_progress",
      "output_file": "./docs/chapters/08/index.md",
      "started_at": "2024-11-15T14:18:00Z",
      "progress_note": "Draft complete, quality scoring in progress"
    },
    "ch-09": {
      "status": "pending",
      "output_file": null,
      "depends_on": []
    },
    "ch-10": {
      "status": "failed",
      "output_file": null,
      "error": "Input data missing: no section outline provided",
      "failed_at": "2024-11-15T13:45:22Z",
      "retry_ready": false
    }
  }
}
```

### Lifecycle States

Items in a batch state file move through defined lifecycle states:

```
pending → in_progress → complete
                     ↘ failed → (retry) → in_progress → complete
```

| State | Meaning | Resume Action |
|---|---|---|
| `pending` | Not yet started | Start next available |
| `in_progress` | Started but not confirmed complete | Verify output file exists; mark complete or restart |
| `complete` | Output file exists and passed quality check | Skip |
| `failed` | Encountered an error | Check `retry_ready` flag before re-queueing |

The `in_progress` state requires special handling on resume. When a session ends unexpectedly (crash, timeout, context limit), items marked `in_progress` may or may not have produced usable output. The resume protocol for `in_progress` items:

1. Check if the output file exists
2. If yes: read the first 200 words and the final 200 words to assess completeness
3. If the file appears complete: run quality scoring and mark as `complete`
4. If the file appears truncated: mark as `failed` and add to the retry queue
5. If no file: mark as `pending` and add to the next run queue

---

## Writing Skills That Resume from Prior State

A skill that supports resumption has a different first step than one that does not. Instead of immediately beginning work, it begins by understanding what has already been done.

### The Resume Detection Block

Add this block at the start of your workflow section, before any execution steps:

```markdown
## Pre-Flight: Resume Detection

Before any work begins:

1. Check for a state file at `./[skill-name]-status.json`
   - If found: read it (it is small, ~500 tokens)
   - If not found: this is a fresh run; initialize the state file

2. If state file found:
   - Report current batch status to user: N complete, M in-progress, K pending
   - Ask: "Resume from in-progress items, or start a fresh run?"
   - If resume: skip all `complete` items, re-validate `in_progress` items,
     queue `pending` items
   - If fresh: rename old state file with timestamp, initialize new state file

3. For each `in_progress` item found on resume:
   - Check if output file exists at the logged path
   - If yes and >500 words: quality-score and mark complete
   - If yes and <500 words: mark failed, add to queue
   - If no: mark pending, add to queue
```

This block costs the user nothing — it is fast, requires reading only one small file, and almost always produces the right result automatically. The only user prompt is the fresh-vs-resume decision, which cannot be automated because it depends on user intent.

### Writing the State File Incrementally

The state file must be updated after each item completes, not at the end of the batch. If the session ends after completing item 7 of 12 but before the final write, and the state file only reflects items 1-6, item 7's work is lost.

The incremental update pattern in a skill's workflow:

```markdown
## Batch Execution Protocol

For each item in the queue:

1. Mark item as `in_progress` in the state file (write immediately)
2. Execute the workflow for this item
3. Write the output file
4. Run quality scoring
5. Mark item as `complete` in the state file with quality score (write immediately)
6. Proceed to next item

If any step fails:
- Mark item as `failed` in the state file with error note (write immediately)
- Log the failure
- Continue to next item (do not halt the batch)
```

The two write-immediately instructions are critical. They ensure the state file accurately reflects current reality at every point in execution. A state file that is updated in batches is unreliable during resumption.

---

## Log Continuity Across Sessions

When a new session reads a log to resume work, it should be able to reconstruct everything it needs from three sources:

1. **The state file** — what is complete, in-progress, pending, failed
2. **The log file** — what decisions were made, what quality scores were assigned, what is outstanding
3. **The output files** — the actual work product

The resume session should never need to re-read files that are already marked complete in the state file. It should never need to re-derive decisions that are documented in the log. It should never need to re-run quality scoring on outputs that already have scores in the log.

This is the efficiency principle of session logging: logs exist to eliminate redundant work on resume, not to provide a narrative history.

### The Resume Session Opening Protocol

Build this into skills that support multi-session work:

```markdown
## Session Opening (Resume Mode)

1. Read state file (one read, ~500 tokens)
2. Read the most recent log entry (one read, ~1,000 tokens)
3. Report to user:
   - Items complete: [N]
   - Items in-progress: [M] (will be re-validated)
   - Items pending: [K]
   - Estimated session work remaining: [time estimate]
   - Quality scores so far: [average and range]
4. Re-validate any in-progress items
5. Begin next pending item
```

Total token cost of resuming: ~1,500 tokens for the state + log read, plus the re-validation work on in-progress items. This is dramatically cheaper than re-reading all output files to reconstruct state, which might cost 10,000-50,000 tokens for a large batch.

---

## Quality Scoring in Logs

Quality scores are a first-class element of session logs. Every skill that produces substantial output should include a quality score in its log, derived from the skill's quality checklist.

### Scoring Mechanics

Quality scores are calculated from a rubric defined in the SKILL.md or reference guide. Each criterion is scored on a 0-10 scale, then averaged (or weighted if some criteria are more important than others).

Example rubric from the executive summary variant:

```markdown
## Quality Scoring

Score each criterion 0-10:

| Criterion | Weight | How to Score |
|-----------|--------|--------------|
| Findings are quantified | 1.0x | 10 = all findings have numbers; 5 = half do; 0 = no numbers |
| Recommendations have owners | 0.8x | 10 = all have owners; 5 = some have owners; 0 = none do |
| Register is appropriate | 1.0x | 10 = clean executive language throughout; 5 = some jargon or passive voice |
| Length within target | 0.6x | 10 = within target; 7 = 10% over; 3 = 50% over; 0 = 2x over |
| One-sentence summary present | 1.0x | 10 = present and strong; 5 = present but weak; 0 = missing |

Overall score = weighted average of all criteria × 10
```

The log records both the overall score and the individual criterion scores. This enables diagnosis: if a skill consistently underperforms on one criterion, that is a signal that the workflow step addressing that criterion needs improvement.

### Using Scores for Skill Improvement

Aggregate quality scores across log files to identify systemic issues:

- If the average score for a variant is below 7.0, the reference guide workflow needs revision
- If one criterion is consistently low, the instruction for that criterion is unclear
- If scores dropped after a version update, the update regressed something

This feedback loop — log quality scores, aggregate across sessions, identify patterns, revise the skill — is how skills improve over time. Without logs, this loop does not exist.

---

## Implementing Logging in a New Skill

When you build a new skill, add logging from the start. Retrofitting logging into an existing skill is harder than building it in.

### Minimum Viable Log Entry

For a simple single-variant skill, the minimum useful log entry is:

```markdown
## [Skill Name] — [YYYY-MM-DD]

**Invocation:** [command / description]
**Output:** [file path] ([word count] words)
**Quality Score:** [X.X / 10]
**Status:** Complete
```

That is 4 lines and approximately 60 tokens to write. A resume session can read it in under 50 tokens. This minimum-viable format is enough to answer the question "has this skill run on this input before?" at trivial cost.

Add more structure as the skill grows in complexity. Do not start with a fully instrumented log if the skill is simple — let the log format evolve with the skill's complexity.

### Log Directory Setup Step

Add a log setup step as the first step in every skill's execution protocol:

```markdown
## Execution Protocol

**Step 0: Initialize logging**
- Ensure `./logs/` directory exists
- Open log file: `./logs/[skill-name]-v[VERSION]-[TODAY].md`
- Write the invocation header immediately (before any other work)
```

Writing the invocation header before any work begins ensures that even if the skill crashes in the first step, there is evidence in the log that an attempt was made. This makes debugging significantly easier.

---

## Anti-Patterns

**Do not log full output text.** Logs should reference output files, not duplicate them. A log entry that includes the full generated report is wasteful — reading the log to resume work would cost as much as reading the report directly.

**Do not write state files only at the end of a batch.** If the session ends before the final write, the state file is wrong. Write after every item.

**Do not use logs as the primary recovery mechanism.** Logs support recovery; output files are the primary artifact. A log that says "complete" for an item whose output file is missing is in an inconsistent state. The resume protocol must check both.

**Do not skip logging for "simple" skills.** Simple skills become complex over time. A skill that starts as a single-variant, single-output tool often grows into a multi-variant pipeline component. Starting with no logging makes that transition harder. Even a minimum-viable log entry is better than none.

---

## Summary

Session logging exists because complex skills do non-trivial work that cannot be reliably resumed without external memory. The context window fills, sessions end, batches fail partway — and the infrastructure for continuing is the log.

The key components of a robust logging implementation:

**The logs/ directory** holds human- and Claude-readable `.md` files, one per skill per day, with multiple sessions appending to the same file under separate headers.

**The log format** captures invocation, timing, files created, token estimates, quality scores, decisions made, and resume state.

**The state file** (JSON) tracks batch item lifecycle states with precision, updated after every item, readable in ~500 tokens.

**Resume detection** is the first step in any multi-session skill — read the state file, report current status, re-validate in-progress items, queue next pending items.

**Quality scores** in logs create the measurement corpus that enables systematic skill improvement over time.

Chapter 11 extends these concepts into the pipeline context — how multiple skills chain together in dependency order, how checkpoints work, and how a 12-step orchestration manages the continuity of an entire textbook production pipeline.
