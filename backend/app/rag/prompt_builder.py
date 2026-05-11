from langchain_core.prompts import PromptTemplate

RAG_TEMPLATE = """You are a helpful assistant answering questions based on the provided context.

Context:
{context}

Question: {question}

Instructions:
- Answer based on the context above
- If the context contains relevant information, use it to give a complete answer
- Be specific and detailed in your response
- Only say you don't know if the context has absolutely no relation to the question

Answer:"""

def build_prompt() -> PromptTemplate:
    return PromptTemplate(
        input_variables=["context", "question"],
        template=RAG_TEMPLATE
    )