from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My FastAPI Service"
    debug: bool = False
    database_url: str               # e.g., "postgresql+asyncpg://user:pass@db:5432/mydb"
    redis_url: str                  # e.g., "redis://redis:6379/0"
    secret_key: str                 # for JWT signing
    access_token_expire_minutes: int = 15

    class Config:
        env_file = ".env"           # load variables from .env in dev
        case_sensitive = True

settings = Settings()
