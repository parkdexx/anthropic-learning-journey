# Building with the Claude API — Learning Notes

## Model Types

1. **Opus** — Most intelligent; highest cost
2. **Sonnet** — Well-balanced; most widely used
3. **Haiku** — Fastest; lowest cost

---

## Anthropic API Access Flow

> My App → My Server → Anthropic API → My Server → My App

- **Why a server is required** (can't I connect directly?): Security — exposing your API key on the client side creates a serious vulnerability.

---

## Anthropic API Internal Processing

When Anthropic receives a request, it follows this pipeline:

1. **Tokenization** — Splits the input text into tokens
2. **Embedding** — Converts tokens into numerical representations
3. **Contextualization** — Determines the meaning of each token based on surrounding tokens
4. **Generation** — Predicts the next token iteratively to produce a response

---

## Anthropic API Response Structure

1. **Message** — The generated response text
2. **Usage** — Input and output token counts
3. **Stop Reason** — Why the generation process ended

---

## Issuing an API Key

1. Visit `https://console.anthropic.com/`
2. Enter a name for the key and generate it
3. A popup displays the key — **copy it to a secure location immediately**
    - It cannot be viewed again after closing the popup

---

## Data That Is Not Stored

The following are **not persisted** by Anthropic:

1. User questions and requests
2. Claude's responses

---

## Anthropic API — Additional Notes

- The Anthropic API does **not** accept `None` for the `system` parameter — the key must be omitted entirely if no system prompt is used.

---

## Temperature Control

**Temperature** controls the randomness and creativity of the model's output.

1. **Low Temperature (0.0 – 0.3)**
    - Fact-based answers
    - Coding assistance
    - Data extraction
    - Content moderation

2. **Mid Temperature (0.4 – 0.7)**
    - Summarization
    - Educational content
    - Problem solving
    - Constrained creative writing

3. **High Temperature (0.8 – 1.0)**
    - Brainstorming
    - Creative writing
    - Marketing content
    - Joke generation

---

## Prompt Pipeline

Running prompts through an **evaluation pipeline** provides objective performance metrics across a broader range of test cases. This data-driven approach offers the following benefits:

- Identify weaknesses and address them before they become production issues
- Objectively compare different prompt versions
- Iterate with confidence based on measurable improvements
- Build more reliable AI applications

This approach requires more upfront investment and time to set up the testing infrastructure, but significantly improves the stability and robustness of the final application. The goal is to catch problems during development — not after users have already experienced them.

---

## Prompt Evaluation

Evaluate the prompts you intend to give to AI — using AI itself.

Three evaluation approaches:

- **Model-based evaluation** — Use a model to score prompt outputs
- **Code-based evaluation** — Write programmatic checks to assess outputs
- **Human-based evaluation** — Have people review and rate outputs

Model-based and code-based evaluations can be implemented and run as code through the API. The course walks through this process hands-on.

---

## Prompt Writing — Clear Communication

**"Clear"** means:

- Use plain language that anyone can understand
- State exactly what you want — don't beat around the bush
- Start with a concise, unambiguous description of Claude's task

**Example:**
- Vague: *"I want to know about that solar device you put on a roof — solar panels."*
- Clear: *"Explain how solar panels work in three paragraphs."*

---

## Prompt Writing — Be Direct

**"Direct"** focuses on how you structure the request:

- Use instructions, not questions
- Start with action verbs: *"Write," "Create," "Generate"*

**Example:**
- Indirect: *"I read about renewable energy and geothermal seems interesting. Which countries use it?"*
- Direct: *"List three countries that use geothermal energy. Include electricity generation statistics for each."*

---

## Prompt Writing — Output Guidance

Specify the **characteristics** the result should have. These instructions help control:

- Response length
- Structure and format
- Specific attributes or elements to include
- Tone or style requirements

---

## Prompt Writing — Process-Oriented Instructions

When solving complex problems, use **step-by-step processes**. Add procedural instructions when handling:

- Complex problem solving
- Decision-making scenarios
- Critical thinking tasks
- Any situation where you want Claude to consider multiple perspectives

---

## Prompt Writing — Using XML Tags

You do not need to use official XML tag names — create descriptive names that fit your content.

- `<sales_records>` is better than `<data>`
- `<athlete_information>` clearly identifies the content type
- `<my_code>` and `<docs>` separate different content types

The more specific and descriptive the tag name, the better Claude understands the purpose of each section.

**XML tags are most useful when:**

- Including large amounts of context or data
- Mixing different content types (code, documents, data)
- Requiring very clear content boundaries
- Working with complex prompts that interpolate multiple variables

Even for short content, XML tags act as delimiters that make the prompt structure clearer to Claude.

---

## Prompt Writing — Multi-Shot and One-Shot Prompting

**Adding examples** helps Claude handle edge cases and exceptional situations.

Examples are especially useful for:

- Capturing edge cases or unusual scenarios
- Defining complex output formats (e.g., a specific JSON structure)
- Demonstrating the exact style or tone you want
- Showing how to handle ambiguous inputs
