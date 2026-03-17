You are translating a Korean learning notes file (`notes-kor.md`) into an English `notes.md` for an Anthropic Academy learning repository.

**Input file:** $ARGUMENTS
**Output file:** Replace `notes-kor.md` with `notes.md` in the same directory path.

Follow these steps:

1. **Read** the input file at `$ARGUMENTS` using the Read tool.

2. **Determine the output path** by replacing `notes-kor.md` with `notes.md` in the same directory.

3. **Translate** the content from Korean to English using these rules:
   - Use accurate AI/ML technical terminology in English
     - 위임 → Delegation, 설명 → Description, 분별력 → Discernment, 성실성 → Diligence
     - 에이전트 → Agent, 사전학습 → Pre-training, 미세조정 → Fine-tuning
     - 환각 → Hallucination, 트랜스포머 → Transformer, 어텐션 → Attention
     - 생성형 AI → Generative AI, 강화 학습 → Reinforcement Learning
     - 온도 → Temperature, 맥락 창 → Context Window
   - Keep proper nouns as-is: Claude, RAG, Artifact, LLM, AI, API, etc.
   - Preserve all relative paths (e.g., `./res/...`) without modification
   - Preserve all Markdown image tags (`![alt](path)`) without modification

4. **Enhance Markdown quality** during translation:
   - Add `---` horizontal rules between major `##` sections
   - **Bold** key technical terms on first use within each section
   - Clean up nested list indentation (use 4-space indent for sub-items)
   - Ensure header hierarchy is clear (`#` for title, `##` for sections, `###` for subsections)
   - Convert inline `->` arrows to proper prose or use `→` where appropriate

5. **Write** the translated content to the output `notes.md` file using the Write tool.

6. Confirm the output path and briefly summarize the sections translated.

**Quality reference:** The file `src/01-claude-101/notes.md` in this repository is an example of the target style and quality — concise, well-structured, technically accurate English notes.
