from langchain_chroma import Chroma

def retrieve(store: Chroma, query: str, k: int = 6) -> list[dict]:
    results = store.similarity_search_with_score(query, k=k)

    seen = set()
    unique = []
    for doc, score in results:
        if doc.page_content not in seen:
            seen.add(doc.page_content)
            unique.append({
                "content": doc.page_content,
                "source": doc.metadata.get("source", "unknown"),
                "score": score
            })

    return unique[:4]