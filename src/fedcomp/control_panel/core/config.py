from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "My FastAPI App"

    class Config:
        env_file = ".env"


settings = Settings()
