from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "NoteVault AI"
    APP_ENV: str = "development"
    
    # Security
    SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    
    # Database
    DATABASE_URL: str
    REDIS_URL: str
    
    # AWS
    AWS_ACCESS_KEY: str
    AWS_SECRET_KEY: str
    AWS_BUCKET_NAME: str
    AWS_REGION: str
    
    # AI Services
    OPENAI_API_KEY: str
    CHROMA_PERSIST_DIRECTORY: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

@lru_cache()
def get_settings() -> Settings:
    """
    Get cached settings instance.
    """
    return Settings()
