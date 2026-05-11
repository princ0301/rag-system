from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    anthropic_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None
    gemini_api_key: Optional[str] = None
    groq_api_key: Optional[str] = None

    chroma_persist_dir: str = "./chroma_db"
    chroma_collection_name: str = "kb_persistent"
    backend_host: str = "0.0.0.0"
    backend_port: int = 8080

    llm_provider: str = "groq"
    llm_model: str = "meta-llama/llama-4-scout-17b-16e-instruct"

    class Config:
        env_file = ".env"

settings = Settings()