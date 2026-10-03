"""Document ingestion and embedding pipeline.

This script loads files from the `data/` directory, splits long documents into
chunks, creates embeddings using OpenAI, and stores them in Chroma DB for later
retrieval by the RAG application.

It acts as the knowledge-base indexing step in a retrieval pipeline.
"""

import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

load_dotenv()

DATA_DIR = "data"
COLLECTION_NAME = "rag_collection"


def load_documents_from_dir(directory):
    """Load text and PDF documents from a local folder."""
    documents = []
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if filename.lower().endswith(".pdf"):
            loader = PyPDFLoader(path)
            documents.extend(loader.load())
        elif filename.lower().endswith((".txt", ".md")):
            with open(path, "r", encoding="utf-8") as f:
                documents.append({"page_content": f.read(), "metadata": {"source": filename}})
    return documents


def create_vector_store():
    """Split documents, generate embeddings, and persist them to Chroma."""
    raw_docs = load_documents_from_dir(DATA_DIR)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    if raw_docs and hasattr(raw_docs[0], "page_content"):
        docs = text_splitter.split_documents(raw_docs)
    else:
        docs = []
        for doc in raw_docs:
            content = doc.get("page_content", "")
            metadata = doc.get("metadata", {})
            docs.append(Document(page_content=content, metadata=metadata))

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory="chroma_db",
    )
    vector_store.persist()
    print("Vector store created successfully.")


if __name__ == "__main__":
    create_vector_store()
