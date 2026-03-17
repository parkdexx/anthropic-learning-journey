# AI Fluency Foundations — Learning Notes

## Objective

Over the past few years, artificial intelligence has evolved from a specialized technology into an interactive system used daily by millions of people.
This shift has created both opportunity and uncertainty.
Bridging the gap between what AI makes possible and what feels comfortable and intuitive is essential.

---

## The 4D Framework *(also covered in Lesson 1)*

1. **Delegation**: Distributing work by deciding what the human does versus what the AI does.
2. **Description**: Communicating effectively with the AI system — defining outputs clearly and guiding processes.
3. **Discernment**: The ability to cautiously and critically evaluate AI-generated results.
4. **Diligence**: Using AI responsibly and ethically.

---

## TEST *(see /res folder)*

---

## Why Large Language Models Advanced

1. **The Transformer Architecture** breakthrough
    - The **Transformer** architecture is a deep learning model structure centered on the **Attention** mechanism, which simultaneously captures relationships between words in a sentence — driving innovation in natural language processing and Generative AI.
2. Vast amounts of digital data
3. Powerful computing performance

---

## Traditional AI vs. Generative AI

- **Traditional AI**: Primarily analyzes and categorizes existing data.
    - Example: Analyzing patterns in emails to classify whether a message is spam or not.
- **Generative AI**: Goes beyond analysis to create entirely new content that did not previously exist.
    - Example: Instead of just classifying spam, it drafts a completely new email on the user's behalf.

---

## Pre-training vs. Fine-tuning

> **Summary**: If **Pre-training** teaches the model the rules of language and vast knowledge, **Fine-tuning** uses that knowledge to teach the model how to interact with humans safely and helpfully.

- **Pre-training**: The initial training stage where the model analyzes billions of text examples to build a complex map of language and knowledge.
- **Fine-tuning**:
    - *Purpose and process*: An additional training stage applied after pre-training, designed to help the model follow user instructions, provide useful responses, and avoid generating harmful content.
    - *Training method*: Primarily uses human feedback to improve model performance, and employs **Reinforcement Learning** — using rewards and penalties — to shape the model's behavior toward being more helpful, honest, and harmless.

---

## Limitations of AI

1. **Knowledge Cutoff Date**:
    LLMs operate based on their training data, so they have a "knowledge cutoff" — the point at which training was completed.
    For example, a model with a cutoff of November 2024 has no built-in knowledge of events or information after that date.
    This is similar to a person who has been cut off from the internet after a specific date — external tools like web search are essential to access recent changes or the latest information.

2. **Hallucination** *(confidently stating incorrect information)*:
    The training process does not perfectly verify every fact in the data, and models can make mistakes when piecing together learned information.
    This leads to **Hallucination** — where the AI states something that sounds plausible but is entirely incorrect, with great confidence.
    This occurs because the model generates text probabilistically based on statistical patterns, rather than simply retrieving existing documents like a search engine.
    → Mitigated through **RAG** (Retrieval-Augmented Generation)

3. **Context Window Limit**:
    There is a maximum limit to the amount of information an AI can consider and process in a single interaction.
    When this limit is exceeded, the model forgets past information outside the window on a first-in, first-out (FIFO) basis.
    Depending on model size, this limitation can make it difficult to process very large documents at once or retain the full context of very long conversations.

4. **Non-deterministic Behavior** *(responses vary each time)*:
    Unlike traditional software that always produces the same output for the same input, LLMs are fundamentally **non-deterministic** — their outputs are difficult to predict.
    The model probabilistically decides which word comes next based on data patterns, so the same question can yield slightly different answers each time.
    This randomness is highly advantageous for creative tasks like brainstorming, but caution is needed for tasks where accuracy and consistency are critical.
    Some interfaces allow users to control this randomness via a **Temperature** setting.
    → Temperature adjusts whether AI responses lean creative or precise, depending on the nature of the task.

---

## 3 Core Elements of Delegation Competency

1. **Problem Awareness**: Clearly define the goal to be achieved and understand the nature of the task based on human expertise.
2. **Platform Awareness**: A deep understanding of the unique strengths and limitations of various — and constantly evolving — AI systems.
3. **Task Delegation**: Combining the analyzed problem with the characteristics of the available tools to strategically distribute work between human and AI.

> **Conclusion**: Successful collaboration is not simply handing off tasks — it is a creative process of finding the optimal balance between human judgment and technical tools.

---

## 3 Core Elements of Description Competency

1. **Product Description**:
    The ability to clearly define what you want the AI to create or deliver.
    The AI should never be left to guess your intent — you must explicitly provide all relevant details: the context behind the task, exactly what the AI should do, the desired output format, the target audience, and the appropriate style.

2. **Process Description**:
    The ability to guide how the AI should approach a request.
    You can provide step-by-step instructions or examples — like a manual or cookbook — to direct the AI's working method.
    This includes specifying particular data to reference, the sequence or specific problems to address, and any particular analysis style or workflow to follow.

3. **Performance Description**:
    The ability to define the behavioral aspects of the AI interaction.
    Unlike a vending machine, AI is a conversational system capable of adapting to context — so you need to tell the AI what kind of thinking partner you need at any given moment.
    For example: whether to explore multiple possibilities or narrow down to a specific answer; whether to challenge your assumptions or simply follow instructions; whether to provide detailed explanations or respond concisely.

---

## 6 Elements of Effective Prompt Writing

1. **Give context**:
    Clearly and specifically explain what you want, why you need it, and who you are (e.g., your knowledge level or current situation).
    Providing this background information greatly helps the AI optimize its response to your specific circumstances.

2. **Show examples of what good looks like**:
    Provide concrete examples that the AI can reference to understand the desired output.
    Examples spanning diverse cases and styles help the AI far more accurately understand the pattern you're aiming for.

3. **Specify output constraints**:
    Define clear constraints such as desired format, length, programming language, button colors on a web page design, etc. — to get results that precisely match your expectations.

4. **Break complex tasks into steps**:
    For complex requests, list out the steps to be performed one by one, so the AI can follow the process properly.

5. **Ask to think first**:
    Give the AI space to carefully consider the problem, potential constraints, and various approaches before generating a response.
    Allowing time to think before acting produces far more thorough and in-depth results.

6. **Define role, style, or tone**:
    Specify what perspective the AI should take or what communication style it should use.
    For example, assigning a role like "explain this from the perspective of an experienced science teacher" can significantly change the AI's approach and the quality of the final output.

> **Tip**: When you're stuck on how to write a prompt, asking the AI to improve the prompt itself is a powerful technique. Prompt writing is an iterative process — review outputs and refine your approach.

---

## 3 Core Elements of Discernment for AI Fluency

1. **Product Discernment**:
    The ability to judge the accuracy and value of AI-generated output.
    This means evaluating whether the AI's content is factually accurate, appropriate for its purpose and audience, coherent and well-structured, and whether it meets requirements and adds genuine value.

2. **Process Discernment**:
    The ability to judge the quality and effectiveness of the AI's reasoning process.
    This involves identifying whether the AI makes logical errors, takes inappropriate steps, or gets stuck on narrow details without considering alternatives.
    This is especially critical in complex tasks where the correct answer isn't immediately obvious — it helps keep both user and AI aligned throughout and moving in a successful direction.

3. **Performance Discernment**:
    The ability to judge the quality of human–AI interaction.
    This involves evaluating whether the AI responds well to feedback and instructions, provides information in a helpful manner, and communicates efficiently — neither too verbose nor too brief — to foster a more productive collaborative relationship.

---

## How to Give Effective Feedback on Problematic AI Output

1. **Pinpoint what the problem is**: Identify precisely which part of the AI's output is incorrect or insufficient.
2. **Explain why it's a problem**: Clearly state why the identified issue does not align with your intent or goal.
3. **Provide specific improvement suggestions**: Give actionable direction on how the AI should revise or supplement the content to fix the problem.
4. **Update instructions or examples**: Review the original instructions or examples you provided and update them clearly so the AI can better understand your expectations.

---

## 3 Core Elements of Diligence

1. **Creation Diligence**:
    The ability to approach the selection and use of AI systems critically and intentionally.
    Before starting work, this means reviewing whether the system has appropriate data protection policies, whether it complies with organizational regulations, and what impact your actions may have.

2. **Transparency Diligence**:
    The ability to openly and accurately communicate AI involvement and usage to everyone who needs to know.
    When AI plays a significant role in content creation or decision-making, disclosing this honestly maintains trust and respect in relationships.

3. **Deployment Diligence**:
    The ability to take informed, final responsibility for AI-assisted output when using or sharing it externally.
    Since AI-generated content may contain errors or bias, the responsibility to fact-check and verify accuracy before releasing the final output to the world rests with the user.

---

## Key Takeaway

Effective AI fluency requires mastering all four dimensions:

- **Delegation** — distributing work appropriately between human and AI
- **Description** — communicating intent clearly and precisely
- **Discernment** — critically evaluating outputs and processes
- **Diligence** — acting with ethical responsibility at every step

> Reference: [AI Fluency Framework (Practical Summary)](https://ringling.libguides.com/ai/framework)
