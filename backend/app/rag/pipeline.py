from app.rag.llm_factory import get_llm
from app.rag.prompt_builder import build_prompt
from app.vectorstore.retriever import retrieve
from langchain_chroma import Chroma

def run_pipeline(store: Chroma, question: str) -> dict:
    chunks = retrieve(store, question, k=4)

    if not chunks:
        return {
            "answer": "No relevant information found in the knowledge base.",
            "sources": []
        }
    
    context = "\n\n".join([c["content"] for c in chunks])
    sources = [{"source": c["source"], "chunk": c["content"][:200]} for c in chunks]

    llm = get_llm()
    prompt = build_prompt()

    chain = prompt | llm

    response = chain.invoke({"context": context, "question": question})

    return {
        "answer": response.content.strip(),
        "sources": sources
    }