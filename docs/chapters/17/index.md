# Chapter 17: Publishing and Distribution

Building a skill for personal use and publishing it for others to use are fundamentally different activities. A personal skill can be rough around the edges — it knows your file paths, your naming conventions, your context. A published skill must be discoverable by a stranger, installable in under five minutes, and robust enough to handle environments it has never encountered.

This chapter covers the full lifecycle of publishing a skill: packaging for sharing, GitHub-based distribution, versioning, documentation requirements, the install script pattern for a collection, license considerations, and how to build a skill collection that others will actually use.

---

## What "Publishing" Means for a Skill

Publishing a skill means making it available for other Claude Code users to install and use. The primary distribution mechanism is GitHub: a repository containing one or more skills, with an install script that creates the symlinks and an uninstall script that removes them.

There is no central registry or marketplace. Discovery happens through:
- Personal recommendation and sharing
- GitHub search (repository names, topics, README content)
- Community lists maintained by skill authors
- References in textbooks and tutorials (like this one)

This means your README and repository description are your primary marketing. If they do not clearly communicate what the skill does and who it is for, it will not be used.

---

## Repository Structures for Publishing

### Single-Skill Repository

The simplest publishable unit is a repository that contains exactly one skill.

```
my-book-metrics-skill/
  SKILL.md                  # The skill definition
  metrics.py                # Python helper
  validate_schema.py        # Validation helper
  examples/
    sample-mkdocs.yml       # Example input
    sample-metrics.json     # Example output
  tests/
    test-cases.md           # Documented test cases
  install.sh                # One-line install script
  uninstall.sh              # One-line uninstall script
  LICENSE                   # MIT or Apache 2.0
  README.md                 # Required — see below
  .gitignore
```

### Skill Collection Repository

A collection repository contains multiple related skills with a shared install script.

```
claude-textbook-skills/
  skills/
    book-metrics-generator/
      SKILL.md
      metrics.py
      README.md             # Per-skill README
    dag-validator/
      SKILL.md
      validate_dag.py
      README.md
    microsim-generator/
      SKILL.md
      template.html
      generate.py
      README.md
    concept-classifier/
      SKILL.md
      classify.py
      categories.json
      README.md
  install.sh                # Installs all skills or selected skills
  install-profile.sh        # Profile-based install (textbook, data, etc.)
  uninstall.sh
  LICENSE
  README.md                 # Collection overview
  CHANGELOG.md              # Version history
  .gitignore
```

---

## Documentation Requirements for Published Skills

A published skill needs two levels of documentation: the SKILL.md (which Claude reads) and the README.md (which humans read). These are not the same document.

### SKILL.md Requirements for Publication

The SKILL.md for a published skill must be more explicit than a personal skill because the author cannot assume a shared understanding of conventions:

```markdown
---
name: book-metrics-generator
description: |
  Analyzes a MkDocs textbook project and produces a structured metrics report.
  Reads mkdocs.yml for project structure, scans all chapter files, and outputs
  metrics.json with chapter completeness, content density, and quality scores.
triggers:
  - /book-metrics
  - /textbook-audit
  - /course-metrics
allowed-tools:
  - Read
  - Bash
  - Write
  - Glob
version: 2.1.0
author: Your Name
repository: https://github.com/yourname/claude-textbook-skills
requires-python: ">=3.9"
dependencies: []
---
```

Note the addition of `author`, `repository`, `requires-python`, and `dependencies` fields. These are not required by Claude Code for skill execution, but they are essential for users who need to debug installation issues or evaluate whether the skill is compatible with their environment.

### The README for a Single Skill

A well-structured per-skill README answers four questions in order:

1. What does this skill do? (One sentence)
2. Who is it for? (Target user)
3. How do I install it? (Exact commands)
4. How do I use it? (Invocation examples with expected output)

```markdown
# book-metrics-generator

Analyzes a MkDocs textbook project and produces a structured quality
metrics report in JSON format.

## Who This Is For

Authors building intelligent textbooks with the MkDocs Material theme who want
an objective, automated assessment of their course's completeness and quality.

## Installation

### Prerequisite

Python 3.9 or later must be installed and available as `python3`.

### Install via symlink (recommended)

```bash
# Clone the collection
git clone https://github.com/yourname/claude-textbook-skills.git ~/claude-skills

# Run the install script
cd ~/claude-skills && ./install.sh book-metrics-generator
```

### Manual install

```bash
# Create the skill directory
mkdir -p ~/.claude/skills/book-metrics-generator

# Copy files
cp skills/book-metrics-generator/* ~/.claude/skills/book-metrics-generator/
```

Start a new Claude Code session. Type `/book-metrics` to verify installation.

## Usage

### Basic invocation

From your textbook project directory:

```
/book-metrics
```

The skill reads `mkdocs.yml` from the current directory, scans all chapter
files, and writes `metrics.json` to the project root.

### Specify a path

```
/book-metrics path/to/my-textbook/mkdocs.yml
```

### Example output

```json
{
  "summary": {
    "total_chapters": 12,
    "complete_chapters": 10,
    "avg_word_count": 2847,
    "overall_score": 78
  },
  "issues": [
    {
      "severity": "warning",
      "file": "docs/chapters/06/index.md",
      "issue": "Word count (847) below minimum (2000)"
    }
  ]
}
```

## Configuration

The skill reads scoring thresholds from
`~/.claude/skills/book-metrics-generator/config.json` if present.
See `config.json.example` for available settings.

## Troubleshooting

**"No mkdocs.yml found"** — Run the skill from your textbook project root.

**"ModuleNotFoundError"** — The Python helper uses only standard library modules.
If you see this error, verify you are running Python 3.9+: `python3 --version`

**Skill not recognized** — Start a new Claude Code session. Skills are loaded
at session start; editing SKILL.md in an existing session has no effect.
```

### The README for a Skill Collection

The collection README is the entry point for users who find your repository. It must communicate the collection's purpose, list the included skills, and provide a clear installation path.

```markdown
# Claude Textbook Skills

A collection of Claude Code skills for authors building intelligent textbooks
with MkDocs Material and the Dan McCreary methodology.

## Included Skills

| Skill | Trigger | Description |
|-------|---------|-------------|
| book-metrics-generator | `/book-metrics` | Audit textbook completeness and quality |
| dag-validator | `/validate-dag` | Validate learning graphs for cycles and orphans |
| microsim-generator | `/microsim` | Generate p5.js interactive simulations |
| concept-classifier | `/classify-concept` | Classify concepts by cognitive type |
| survey-to-chart-data | `/survey-to-chart` | Convert survey CSV to Chart.js data |

## Quick Install

```bash
git clone https://github.com/yourname/claude-textbook-skills.git ~/claude-skills
cd ~/claude-skills && ./install.sh
```

Start a new Claude Code session and type `/skills` to see all installed skills.

## Requirements

- Claude Code (any recent version)
- Python 3.9+ available as `python3`
- macOS or Linux (Windows via WSL)

## Install Individual Skills

```bash
./install.sh book-metrics-generator
./install.sh dag-validator
```

## Profiles

Install only the skills you need:

```bash
./install-profile.sh textbook    # book-metrics, dag-validator, microsim-generator
./install-profile.sh data        # survey-to-chart-data, concept-classifier
```

## Contributing

See CONTRIBUTING.md for guidelines on adding skills to this collection.
```

---

## Versioning Conventions

Skills use semantic versioning with three components: `MAJOR.MINOR.PATCH`.

| Component | When to increment | Example |
|-----------|-------------------|---------|
| MAJOR | Breaking change to the skill's interface (changed trigger names, changed output schema) | 1.x.x → 2.0.0 |
| MINOR | New capability added, backwards-compatible (new trigger, new optional parameter) | x.1.x → x.2.0 |
| PATCH | Bug fix, documentation improvement, performance improvement | x.x.1 → x.x.2 |

The version field in SKILL.md frontmatter must match the version in CHANGELOG.md and in any Git tags.

### CHANGELOG.md

Maintain a CHANGELOG.md in the collection root using the Keep a Changelog format:

```markdown
# Changelog

All notable changes to this skill collection are documented here.

## [2.1.0] - 2026-02-20

### Added
- book-metrics-generator: Added `diagram_density` metric
- book-metrics-generator: New `/textbook-audit` trigger alias

### Fixed
- dag-validator: Handle empty graph (0 concepts) without crashing
- concept-classifier: Improve classification confidence for procedural concepts

## [2.0.0] - 2026-01-15

### Breaking Changes
- book-metrics-generator: Output schema changed — `quality_score` field
  renamed to `overall_score`. Update any downstream scripts that read metrics.json.

### Added
- New skill: survey-to-chart-data

## [1.3.2] - 2025-12-01

### Fixed
- dag-validator: Correctly detect cycles in graphs with self-referencing nodes
```

### Git Tagging

Tag releases in Git so users can install a specific version:

```bash
git tag -a v2.1.0 -m "Add diagram density metric, fix empty graph crash"
git push origin v2.1.0
```

Users can then clone a specific version:

```bash
git clone --branch v2.1.0 https://github.com/yourname/claude-textbook-skills.git
```

---

## The Install Script for a Collection

The collection install script must handle several cases cleanly: installing all skills, installing a single skill by name, dry-run mode for previewing what will happen, and updating existing symlinks when the repository is pulled.

```bash
#!/usr/bin/env bash
# install.sh — Install Claude Code skills from this collection
# Usage:
#   ./install.sh              — Install all skills
#   ./install.sh skill-name   — Install one skill
#   ./install.sh --list       — List available skills
#   ./install.sh --dry-run    — Preview without making changes

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="${SCRIPT_DIR}/skills"
SKILLS_DEST="${HOME}/.claude/skills"
DRY_RUN=false
LIST_ONLY=false
SPECIFIC_SKILL=""

# Parse arguments
for arg in "$@"; do
  case $arg in
    --dry-run) DRY_RUN=true ;;
    --list) LIST_ONLY=true ;;
    --help|-h)
      echo "Usage: ./install.sh [skill-name] [--dry-run] [--list]"
      exit 0
      ;;
    -*) echo "Unknown flag: $arg"; exit 1 ;;
    *) SPECIFIC_SKILL="$arg" ;;
  esac
done

# List mode
if [ "${LIST_ONLY}" = true ]; then
  echo "Available skills:"
  for d in "${SKILLS_SRC}"/*/; do
    name="$(basename "$d")"
    if [ -f "${d}/SKILL.md" ]; then
      desc=$(python3 -c "
import re, sys
with open('${d}/SKILL.md') as f: c = f.read()
m = re.search(r'description:\s*\|?\n?\s*(.+)', c)
print(m.group(1).strip() if m else '(no description)')
" 2>/dev/null || echo "(no description)")
      printf "  %-35s %s\n" "$name" "$desc"
    fi
  done
  exit 0
fi

# Create destination directory
[ -d "${SKILLS_DEST}" ] || { [ "${DRY_RUN}" = false ] && mkdir -p "${SKILLS_DEST}"; }

install_skill() {
  local skill_name="$1"
  local src="${SKILLS_SRC}/${skill_name}"
  local dest="${SKILLS_DEST}/${skill_name}"

  if [ ! -d "${src}" ]; then
    echo "ERROR: Skill '${skill_name}' not found in ${SKILLS_SRC}"
    return 1
  fi

  if [ ! -f "${src}/SKILL.md" ]; then
    echo "WARNING: ${skill_name}/ has no SKILL.md — skipping"
    return 0
  fi

  if [ -L "${dest}" ]; then
    if [ "${DRY_RUN}" = false ]; then
      ln -sfn "${src}" "${dest}"
      echo "  [updated] ${skill_name}"
    else
      echo "  [dry-run] Would update symlink: ${skill_name}"
    fi
  elif [ -d "${dest}" ]; then
    echo "  [skip]    ${skill_name} (real directory exists at destination — manual install?)"
  else
    if [ "${DRY_RUN}" = false ]; then
      ln -s "${src}" "${dest}"
      echo "  [new]     ${skill_name}"
    else
      echo "  [dry-run] Would create symlink: ${skill_name}"
    fi
  fi
}

# Install specific skill or all skills
if [ -n "${SPECIFIC_SKILL}" ]; then
  install_skill "${SPECIFIC_SKILL}"
else
  echo "Installing all skills to ${SKILLS_DEST}..."
  for d in "${SKILLS_SRC}"/*/; do
    install_skill "$(basename "$d")"
  done
fi

echo ""
echo "Done. Start a new Claude Code session to activate installed skills."
[ "${DRY_RUN}" = true ] && echo "(Dry run — no changes made)"
```

---

## License Considerations

Skills are code and documentation combined. The license you choose affects how others can use, modify, and redistribute your skills.

| License | Use when... |
|---------|-------------|
| MIT | You want maximum adoption. Anyone can use, modify, fork, and sell derivatives with minimal restriction. |
| Apache 2.0 | Similar to MIT but includes explicit patent protection. Good choice if your skills implement novel methods. |
| CC BY 4.0 | Skills that are primarily documentation rather than code. Requires attribution. |
| CC BY-SA 4.0 | Requires that derivatives use the same license. Good for community-oriented skill collections. |
| Proprietary | Skills that encode competitive advantage. Do not publish to GitHub without careful consideration. |

For most open skill collections, MIT is the appropriate choice: it maximizes adoption and places minimal burden on users.

The LICENSE file must be at the repository root. GitHub will display it prominently.

---

## Building a Skill Collection

A skill collection is more than a directory of SKILL.md files. A well-built collection has a coherent purpose, clear quality standards across all skills, shared helper utilities, and a governance model that allows it to grow without losing consistency.

### Defining Collection Scope

Before adding skills to a collection, define what the collection is for. A collection with a clear scope is easier to discover and easier to trust:

- **Textbook skills** — skills for authors using MkDocs Material and intelligent textbook patterns
- **Data engineering skills** — skills for CSV/JSON transformation, schema validation, pipeline automation
- **Analysis skills** — skills for scoring and auditing content quality
- **MicroSim skills** — skills for generating interactive educational simulations

Resist the temptation to add a skill to a collection just because it is convenient. A "textbook skills" collection that also includes a Slack message formatter and a Docker compose generator is not a textbook skills collection.

### Shared Utilities

Skills in a collection often share utility code: JSON validation, frontmatter parsing, file discovery patterns. Factor these into shared utility scripts:

```
skills/
  _shared/
    frontmatter.py     # Parse YAML frontmatter from Markdown
    validate_json.py   # Validate JSON against a schema file
    file_utils.py      # Common file discovery patterns
```

Each skill that uses shared utilities imports from `_shared/`:

```python
import sys
from pathlib import Path

# Add shared utilities to path
sys.path.insert(0, str(Path(__file__).parent.parent / '_shared'))
from frontmatter import parse_frontmatter
from validate_json import validate_against_schema
```

### Collection Quality Standards

Document the standards that all skills in the collection must meet. This serves as both a contribution guide and a self-imposed quality bar:

```markdown
## Collection Quality Standards

All skills in this collection must meet these criteria before merging:

### Required Files
- [ ] SKILL.md with complete frontmatter (name, description, triggers, allowed-tools, version)
- [ ] README.md with installation instructions and usage examples
- [ ] At least one example input and expected output in examples/

### Code Quality
- [ ] Python helpers exit non-zero on failure
- [ ] Python helpers validate output before writing to disk
- [ ] No hardcoded absolute paths — use Path(__file__).parent for relative paths
- [ ] All file paths that may contain spaces are quoted in shell commands

### Testing
- [ ] At least 3 documented test cases in tests/test-cases.md
- [ ] Happy path test passes
- [ ] Empty/missing input test passes
- [ ] Manual testing confirmed in a clean Claude Code session

### Documentation
- [ ] SKILL.md workflow has numbered steps
- [ ] Error handling behavior is documented for all failure modes
- [ ] Version is incremented correctly per semantic versioning rules
```

---

## Summary

Publishing a skill means making it work for someone who does not know your conventions, your file structure, or your context. The requirements are: a README that answers "what, who, how to install, how to use"; a SKILL.md with explicit author, version, and dependency fields; semantic versioning with a CHANGELOG; an install script that handles all common installation scenarios; and a clear license. Skill collections add a shared scope definition, shared utility code, and documented quality standards that ensure consistency across all included skills. The filesystem-based distribution model via GitHub symlinks is simple, reliable, and makes it trivially easy to update skills by pulling the repository.
