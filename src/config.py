from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    GROQ_API_KEY: str
    OPENAI_API_KEY: str
    COHERE_API_KEY: str
    MODEL: str
    LANGUAGE: str

    class Config:
        env_file = ".env"

settings = Settings()
