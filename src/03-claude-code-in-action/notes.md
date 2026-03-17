# Claude Code in Action — Learning Notes

## Limitations of the Language Model Itself

A **language model** on its own only processes text and returns text — it cannot read files or execute commands. If you ask a standalone language model to read a file, it will simply respond that it lacks that capability.

---

## Collaboration Between a Coding Assistant and a Language Model

1. **User** → "What code is in `main.go`?" → Coding Assistant
2. **Coding Assistant** → Appends user request + tool-use instructions → Language Model
3. **Language Model** → Responds: `ReadFile: main.go` → Coding Assistant
4. **Coding Assistant** → Returns the contents of `main.go` → Language Model
5. **Language Model** → Provides a final answer based on the file contents → User

---

## Language Models Require a Variety of Tools

To be useful in real development workflows, a language model must be equipped with tools — such as file readers, code writers, command runners, and directory managers — that bridge the gap between text generation and actual system interaction.

---

## Strengths of Claude Code

Claude Code provides a comprehensive set of built-in tools for common development tasks: reading files, writing code, executing commands, and managing directories.

What makes Claude Code truly powerful, however, is its ability to **intelligently combine these tools** to solve complex, multi-step problems.

---

## The CLAUDE.md File

**Context management** is critical when working on coding projects with Claude. A project may contain dozens or hundreds of files, but Claude only needs the information relevant to the task at hand. Feeding Claude too much unnecessary context can degrade its performance, so learning to guide Claude toward the right files and documentation is essential.

`CLAUDE.md` briefs Claude on your codebase — key commands, architecture decisions, and coding style conventions — and allows you to give specific, customized instructions.

| File | Scope | Shared? |
|---|---|---|
| `CLAUDE.md` | Project-level; created via `/init`, committed to source control | Yes — shared with other engineers |
| `CLAUDE.local.md` | Project-level personal overrides and custom settings | No — gitignored |
| `~/.claude/CLAUDE.md` | Global; applies to all projects on the machine | N/A |

---

## Memory Feature

Originally, typing `#` was supposed to save content directly to `CLAUDE.md`, but as of **2026-03-17** this behavior does not appear to work.

The `/memory` slash command opens the memory file for viewing but does not save directly.

The current working method is to **ask Claude conversationally** to save a specific piece of information somewhere (e.g., "Please remember X in CLAUDE.md"). *(This may vary — it could also be a local configuration issue.)*

---

## The `@` File-Path Syntax

**Using `@<file-path>`:**
- The file's contents are immediately and automatically injected into the conversation context.
- Claude can read the content without making a separate `Read` tool call.
- The response is faster, with no tool-approval step.

**Mentioning a file path without `@`:**
- The file is not loaded automatically.
- Claude must invoke the `Read` tool explicitly to access it.
- An additional tool-call approval step is required.

**Practical difference:**

```
# With @ → file is loaded immediately, analysis begins right away
"@src/lib/auth.ts — explain this file"

# Without @ → Claude must call the Read tool separately
"src/lib/auth.ts — explain this file"
```

**Conclusion:** When asking questions or requesting edits based on a specific file, using `@` is the more efficient approach.

---

## Including Database Schemas in CLAUDE.md

Storing your database schema path in `CLAUDE.md` is advantageous. For example:

> The database schema is located at `@<file-path>`. Please remember this in CLAUDE.md.

This ensures Claude always has direct access to your schema without needing to search for it.
