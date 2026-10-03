"""RAG application entry point.

This file is the main chatbot interface for the GenAI project. It takes a user
question, performs a similarity search in Chroma DB to find the most relevant
chunks, and then sends the retrieved context to the OpenAI model for a grounded
answer.

Environment variables used:
- OPENAI_API_KEY
- OPENAI_MODEL
- TOP_K
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from vector_store import similarity_search

load_dotenv()


def ask_question(question, top_k=None):
    """Find relevant documents and answer the user's question using them."""
    top_k = top_k or int(os.getenv("TOP_K", "4"))

    relevant_docs = similarity_search(question, k=top_k)
    context = "\n\n".join(doc.page_content for doc in relevant_docs)

    llm = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0,
    )

    prompt = f"""
You are a helpful assistant. Answer the user's question using only the context provided below.
If the answer is not available in the context, say that clearly.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)
    return response.content


if __name__ == "__main__":
    while True:
        query = input("Ask a question (type 'exit' to quit): ")
        if query.lower() == "exit":
            break
        print(ask_question(query))
