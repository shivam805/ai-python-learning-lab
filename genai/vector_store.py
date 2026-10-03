"""Chroma DB vector store utilities.

This file creates and returns the vector database connection and exposes a
`similarity_search` function that retrieves the top-k most relevant document
chunks for a given user query.

The file is used by the RAG app to ground responses in document context instead
of relying only on model memory.
"""

import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()

COLLECTION_NAME = "rag_collection"
PERSIST_DIRECTORY = "chroma_db"


def get_vector_store():
    """Create a Chroma vector store with OpenAI embeddings."""
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=os.getenv("OPENAI_API_KEY"),
    )
    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=PERSIST_DIRECTORY,
    )
    return vector_store


def similarity_search(query, k=4):
    """Return the top-k most relevant chunks for the query."""
    store = get_vector_store()
    return store.similarity_search(query, k=k)
