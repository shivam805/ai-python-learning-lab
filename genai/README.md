# GenAI RAG Project

This repository contains a simple Retrieval-Augmented Generation (RAG) setup using:
- Python
- OpenAI
- Chroma DB
- LangChain

## Structure

- `app.py` - Main RAG flow
- `vector_store.py` - Chroma DB setup and retrieval
- `ingest.py` - Load documents and store embeddings
- `requirements.txt` - Python dependencies
- `.env.example` - Environment variables
- `data/` - Documents folder

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and add your OpenAI API key.

4. Add your PDF/text files under `data/`.

5. Run ingestion:
   ```bash
   python ingest.py
   ```

6. Start the app:
   ```bash
   python app.py
   ```
