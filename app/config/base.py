from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # App
    APP_NAME: str = "Shopping Assistant"
    DEBUG: bool = False

    # API Keys
    OPENAI_API_KEY: str = Field(..., description="OpenAI Secret Key")
    FIRECRAWL_API_KEY: str = Field(..., description="FireCrawl Secret Key")
    SERPER_API_KEY: str = Field(..., description="Serper Secret Key")

    # Nested configs
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

