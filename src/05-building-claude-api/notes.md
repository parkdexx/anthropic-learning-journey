# Building with the Claude API — Learning Notes

## Model Types

1. **Opus** — Most intelligent; highest cost
2. **Sonnet** — Well-balanced; most widely used
3. **Haiku** — Fastest; lowest cost

---

## Anthropic API Request Flow

> My App → My Server → Anthropic API → My Server → My App

1. **Why a server is required** (can't we connect directly?): Security — exposing the API key on the client side creates a significant security risk.

---

## Anthropic API Internal Processing

When Anthropic receives a request, it follows the steps below:

1. **Tokenization** — Splits the incoming text into tokens
2. **Embedding** — Converts tokens into numerical vectors
3. **Contextualization** — Determines the meaning of each token based on surrounding tokens
4. **Generation** — Predicts the next token to produce a response

---

## Anthropic API Response Structure

1. **Message** — The generated response text
2. **Usage** — Input and output token counts
3. **Stop Reason** — The reason the generation process ended

---

## Issuing an API Key

1. Visit `https://console.anthropic.com/`
2. Enter a name for the key and complete the creation flow
3. A popup will display the key — **copy it to a safe place immediately**
    * It cannot be viewed again after the popup is closed

---

## Data That Is Not Stored

The following are not retained by Anthropic:

1. User questions and requests
2. Anthropic's responses

---

## Anthropic API — Additional Notes

1. The Anthropic API does **not** accept `None` for the `system` parameter — the key must be omitted entirely rather than passed as `null`/`None`.
