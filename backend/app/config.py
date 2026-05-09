from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    anthropic_api_key: str
    openai_api_key: str
    chroma_persist_dir: str = "./chroma_db"
    chroma_collection_name: str = "kb_persistent"
    backend_host: str = "0.0.0.0"
    backend_port: int = 8000

    class Config:
        env_file = ".env"

settings = Settings()