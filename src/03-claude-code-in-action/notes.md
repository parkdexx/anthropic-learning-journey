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

---

## Pasting Screenshots into the Terminal (Ctrl+V)

*TODO:* This does not work in a Windows + VSCode integrated terminal environment. Need to find a workaround.

---

## Thinking Mode

Claude offers multiple levels of reasoning through **Thinking Mode**, allowing it to spend more time reasoning before presenting a solution to complex problems.

| Trigger Phrase | Reasoning Level |
|----------------|-----------------|
| "think" | Basic reasoning |
| "think harder" | Extended reasoning |
| "think a lot" | Comprehensive reasoning |
| "think longer" | Time-extended reasoning |
| "ultrathink" | Maximum reasoning capacity |

Each mode progressively allocates more tokens to Claude, enabling deeper analysis of difficult problems.

---

## Esc Key

- Press **Esc** to pause Claude when it is heading in the wrong direction, then provide a course correction.
- Press **Esc twice** to roll back to a desired previous state.

---

## `compact` and `clear`

| Command | Behavior |
|---------|----------|
| `compact` | Summarizes the conversation while preserving key information |
| `clear` | Wipes all existing context and starts a fresh conversation |

---

## Custom Commands (Slash Commands)

You can create custom commands manually at `.claude/commands/myCommand.md`, but asking Claude to generate them for you is the more practical approach.

Just like the utility methods built in legacy codebases, these commands can (and should) accept parameters — ask Claude to set that up.

> Arguments do not need to be file paths — any string that provides context or direction for the task will work.

The flexibility to pass any arbitrary string as an argument for conveying task direction is remarkably powerful.

---

## MCP Servers

To extend Claude Code's capabilities, add **MCP (Model Context Protocol)** servers. These servers run either remotely or on your local machine and provide new tools and features not included in Claude Code by default.

**Installation example:**
```bash
claude mcp add playwright npx @playwright/mcp@latest
```

**Places to discover MCP servers:**
1. https://smithery.ai/servers
2. https://mcp.so/

---

## Claude + GitHub MCP Server

**Benefits of integrating the GitHub MCP Server:**

1. **Expanded code context** — understand the codebase as a continuous narrative, not just a snapshot ("lines" not "dots")
2. **Direct collaboration tooling** — Claude acts as a teammate, not just an assistant
3. **Workflow productivity boost** — reduced context switching

**Conclusion:** Claude gains the ability to understand and act on the full lifecycle of your code: past (Commits), present (Files), and future (Issues/PRs).

- [x] TODO: Modify this repository's `README.md` via the GitHub MCP Server integration (Pull Request → Merge)

---

## Hook Definition Locations

| Scope | File | Notes |
|-------|------|-------|
| Global | `~/.claude/settings.json` | Affects all projects on the machine |
| Project (shared) | `.claude/settings.json` | Shared with teammates |
| Project (personal) | `.claude/settings.local.json` | Personal settings; not shared |

---

## Hook Events

| Event | When It Fires |
|-------|---------------|
| `PreToolUse` | Immediately before a tool executes |
| `PostToolUse` | Immediately after a tool executes |
| `Notification` | When Claude sends a notification |
| `Stop` | When Claude's response is complete |
| `SubagentStop` | When a sub-agent completes |

---

## Hook Tools

**Built-in tools (always available):**

| Tool | Description |
|------|-------------|
| `Read` | Read a file |
| `Write` | Write a file |
| `Edit` | Edit a file (partial edit) |
| `Glob` | Search files by pattern |
| `Grep` | Search file contents (regex) |
| `Bash` | Execute shell commands |
| `Agent` | Launch a sub-agent |
| `Skill` | Execute a skill (slash command) |
| `ToolSearch` | Look up deferred tool schemas |

**Deferred tools (lazy-loaded) — Task management:**

| Tool | Description |
|------|-------------|
| `TaskCreate` | Create a task |
| `TaskGet` | Retrieve a task |
| `TaskList` | List tasks |
| `TaskUpdate` | Update a task |
| `TaskStop` | Stop a task |
| `TaskOutput` | View task output |

**Deferred tools — Scheduling:**

| Tool | Description |
|------|-------------|
| `CronCreate` | Create a cron job |
| `CronDelete` | Delete a cron job |
| `CronList` | List cron jobs |

**Deferred tools — Other:**

| Tool | Description |
|------|-------------|
| `WebFetch` | Fetch URL contents |
| `WebSearch` | Web search |
| `AskUserQuestion` | Ask the user a question |
| `EnterPlanMode` / `ExitPlanMode` | Toggle plan mode |
| `EnterWorktree` / `ExitWorktree` | Switch Git worktree |
| `NotebookEdit` | Edit a Jupyter notebook |

---

## Hook Usage Example

> "Claude, before creating anything new, check whether there is a reusable item in the existing directory. If one already exists, reuse it. Otherwise, create a new one."
