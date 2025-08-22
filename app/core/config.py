from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI"
    environment: str = "development"
    database_url: str = ""
    secret_key: str = "j9N8cHvXp2K7rF5dZ3qWxA1bE6sT4mY0gL8pD5vR3kF7"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 20
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
