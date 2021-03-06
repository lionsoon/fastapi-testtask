from pydantic import Field, BaseSettings
from typing import Optional

class GunicornEnv(BaseSettings):
    workers_per_core: int = Field(1, env="WORKERS_PER_CORE")
    max_workers: int = Field(2, env="MAX_WORKERS")
    web_concurrency: Optional[int] = Field(None, env="WEB_CONCURRENCY")
    host: str = Field("localhost", env="APP_HOST")
    port: str = Field("8080", env="APP_PORT")

    timeout: int = Field(120, env="GUNICORN_TIMEOUT")
    keepalive: int = Field(5, env="GUNICORN_KEEP_ALIVE")


gunicorn_env = GunicornEnv()