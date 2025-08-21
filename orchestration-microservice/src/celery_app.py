from celery import Celery
from src.config import CELERY_BROKER_URL, CELERY_BACKEND_URL, TaskNames, Queues
# Central Celery app for orchestration
celery_app = Celery(
    "orchestration_service",
    broker=CELERY_BROKER_URL,  # Redis as broker
    backend=CELERY_BACKEND_URL  # Redis as backend
)

# Define routing keys for microservices (different queues)
celery_app.conf.task_routes = {
    "split_service.tasks.split_audio": {"queue": "split_queue"},
    "transcription_service.tasks.transcribe_audio": {"queue": "transcription_queue"},
    "sentiment_service.tasks.detect_sentiment": {"queue": "sentiment_queue"},
}

celery_app.conf.task_routes = {
    TaskNames.SPLIT_AUDIO: {"queue": Queues.SPLIT},
    TaskNames.TRANSCRIBE_AUDIO: {"queue": Queues.TRANSCRIPTION},
    TaskNames.DETECT_SENTIMENT: {"queue": Queues.NLP},
}