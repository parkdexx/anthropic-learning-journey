# Intro to Agent Skills — Learning Notes

## Skills
- Instructions recorded in a `SKILL.md` file.
- **Global** (all projects): `~/.claude/skills`
- **Single project**: `.claude/skills`
- Example structure:
```
name: pr-review
description: Reviews pull requests for code quality. Use when reviewing PRs or checking code changes.
```

- Claude Code reads context from the user's request and **automatically selects the appropriate skill**.

- **CLAUDE.md vs. `/` Commands vs. Skills**:
    - `CLAUDE.md` — Project-wide standing instructions
    - `/` Commands — One-off instructions; must be invoked manually
    - **Skills** — Instructions for recurring tasks; invoked automatically

---

## Skill Metadata Fields

Beyond `name` and `description`, several additional fields are available:

```
name (required)         — Must match the folder name. Max 64 chars. Use lowercase only.
description (required)  — Tells Claude when to use this skill. Max 1024 chars.
allowed-tools (optional)— Tools Claude may use when this skill runs. Unrestricted if omitted.
model (optional)        — Constrain the model used (right tool for the right job).
```

---

## Skills++ (Advanced Structure)

When skill content grows large and complex, dumping everything into `SKILL.md` wastes tokens. Instead, organize with subdirectories:

- `/scripts` — Script files
- `/references` — Reference documents
- `/assets` — Images, videos, and other assets

Place the appropriate descriptions, files, and code in each folder, then **use `SKILL.md` only as a map** pointing to those locations.

> Keep `SKILL.md` under 500 lines.

---

## Summary: Claude Code Extension Points

| Component | Role |
|-----------|------|
| **CLAUDE.md** | Always-on project standards |
| **Skills** | Task-specific expertise loaded on demand |
| **Hooks** | Actions that run automatically on events |
| **Subagents** | Independent execution contexts for delegated work |
| **MCP Servers** | External tool integrations |

---

## Subagents

**Primary reason to use:** Prevent pollution of the main context window.

- A **subagent** is a separate agent with its own independent execution context.
- The main agent can invoke a subagent to **delegate** tasks.
- A subagent can have its own `CLAUDE.md`, skills, hooks, subagents, and MCP servers.
- Subagents return results back to the main agent.

Subagent metadata fields (a superset of skill fields):

```
name (required)         — Must match the folder name. Max 64 chars. Use lowercase only.
description (required)  — Tells Claude when to use this subagent. Max 1024 chars.
allowed-tools (optional)— Tools Claude may use. Unrestricted if omitted.
model (optional)        — Constrain the model used.
color (optional)        — Display color for the subagent in the UI.
skills (optional)       — List of skills available to the subagent.
```
