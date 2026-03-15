# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal learning laboratory for the Anthropic Academy curriculum — a structured journey through Claude AI technologies from basic prompting to production-grade AI infrastructure. The repository is bilingual (English/Korean).

## Repository Structure

```
src/
  base/                          # Shared/foundational resources
  01-claude-101/                 # Phase 1: Completed
  02-ai-fluency-foundations/     # Phase 1b: Planned
  ...                            # Future phases follow the same pattern
```

Each module follows a consistent layout:
- `notes.md` — English learning notes
- `notes-kor.md` — Korean translation of the same notes
- `res/` — Supporting resources (screenshots, HTML, visualizations)

## Learning Phases

| Phase | Topic | Level |
|-------|-------|-------|
| 1 | Claude 101 + AI Fluency Foundations | Entry |
| 2 | Claude Code in Action + Agent Skills | Intermediate |
| 3 | Claude API + Model Context Protocol (basic + advanced) | Advanced |
| 4 | Amazon Bedrock + Google Vertex AI | Expert |
| 5 | Domain-specific AI Fluency (students, educators, nonprofits) | Specialized |

## No Build System

This is a pure documentation/notes repository. There are no build commands, test suites, or dependencies to install.

## Conventions

- New modules go under `src/` with a two-digit prefix matching the curriculum order (e.g., `03-claude-code-in-action/`).
- Each new module should include `notes.md`, `notes-kor.md`, and a `res/` directory.
- Notes files use Markdown. Korean translations mirror the structure of the English originals.
- The README tracks completion status with checkmarks (✅) and calendar icons (📅) for planned items — update it when a module is completed.
