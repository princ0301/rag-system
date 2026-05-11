from app.config import settings

def get_llm():
    provider = settings.llm_provider.lower()
    model = settings.llm_model

    if provider == "anthropic":
        from langchain_anthropic import ChatAnthropic
        return ChatAnthropic(
            model=model,
            anthropic_api_key=settings.anthropic_api_key
        )

    if provider == "openai":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(
            model=model,
            openai_api_key=settings.openai_api_key
        )

    if provider == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(
            model=model,
            google_api_key=settings.gemini_api_key
        )

    if provider == "groq":
        from langchain_groq import ChatGroq
        return ChatGroq(
            model=model,
            groq_api_key=settings.groq_api_key
        )

    raise ValueError(f"Unsupported provider: {provider}")