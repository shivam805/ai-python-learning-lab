# Python AI & DSA Practice

This workspace contains multiple Python learning and project folders for:
- Data Structures and Algorithms (DSA)
- Problem-solving techniques
- Generative AI / RAG projects

## Folder structure

- `dsa_practice/` — beginner to intermediate DSA questions and solutions
- `problem_solving_technique/` — structured problem-solving exercises and patterns
- `genai/` — GenAI project using OpenAI + Chroma DB + RAG flow

## Notes

- The root workspace includes a `.gitignore` file to exclude environment variables, credentials, and local runtime data.
- `.env` files are not committed, so OpenAI keys and secrets stay protected.
- Local virtual environments and generated vector store data are also ignored.

## Running scripts

For any Python file:

```bash
python file_name.py
```

## Security

Sensitive values like OpenAI API keys must never be committed to Git. Use:

```bash
.env
```

and keep examples in:

```bash
.env.example
```
