from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Redis Configuration
    redis_host: str = "localhost"
    redis_port: int = 6380
    redis_broker_db: int = 0
    redis_backend_db: int = 1

    # FastAPI Configuration
    fastapi_host: str = "0.0.0.0"
    fastapi_port: int = 8000

    # Celery Configuration
    celery_log_level: str = "info"

    # Service URLs
    split_service_url: Optional[str] = None
    transcription_service_url: Optional[str] = None
    sentiment_service_url: Optional[str] = None

    @property
    def redis_broker_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}/{self.redis_broker_db}"

    @property
    def redis_backend_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}/{self.redis_backend_db}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

import os

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://microservice-redis:6379/0")
CELERY_BACKEND_URL = os.getenv("CELERY_BACKEND_URL", "redis://microservice-redis:6379/1")
# task_config.py

class TaskNames:
    SPLIT_AUDIO = "split.tasks.split_audio"
    TRANSCRIBE_AUDIO = "transcription.tasks.transcribe_audio"
    DETECT_SENTIMENT = "nlp.tasks.detect_sentiment"


class Queues:
    SPLIT = "split_queue"
    TRANSCRIPTION = "transcription_queue"
    NLP = "nlp_queue"