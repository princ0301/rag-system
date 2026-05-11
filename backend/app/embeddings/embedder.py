from langchain_huggingface import HuggingFaceEmbeddings

class Embedder:
    def __init__(self):
        self.model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True}
        )

    def get_model(self) -> HuggingFaceEmbeddings:
        return self.model