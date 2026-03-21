# Getting the Most Out of Claude Code

## CLAUDE.md

Don't write down every rule — write down **how to find them**.

---

## Disable Unused MCPs

Turn off any **MCP** servers you aren't actively using to reduce noise and overhead.

---

## Status Line

Use `/statusline` to monitor **token usage** in real time.

---

## Compact

Use `/compact` when transitioning to a different conversation thread or context.

---

## Choosing the Right Model

| Task | Model |
|------|-------|
| File search, simple edits | **Haiku** |
| General coding tasks | **Sonnet** |
| Architecture design / debugging | **Opus** |

---

## Plan Mode

Follow this workflow: **Plan** → Review (by you) → Execute coding.

Use **Plan Mode** before writing any code to align on approach first.

---

## Provide Reference Code

Bring well-written code from external sources and share it alongside your request — giving Claude a concrete quality target improves output significantly.

---

## Sub-Agents

**Delegate** work to specialized agents, each with a single responsibility:

- Agent that only creates plans
- Agent that only handles architecture design
- Agent that only writes code
- (and so on...)

---

## Git Worktree

**Git Worktree** lets you create multiple working folders from the same repository.

This enables N agents to work on N independent tasks simultaneously — maximizing parallel throughput.

---

## Hooks

Configure **Hooks** to automate actions at key lifecycle events:

`Session Start` → `Pre-compact` → `Stop`
