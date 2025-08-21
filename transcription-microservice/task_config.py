import os

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://microservice-redis:6379/0")
CELERY_BACKEND_URL = os.getenv("CELERY_BACKEND_URL", "redis://microservice-redis:6379/1")


class TaskNames:
    SPLIT_AUDIO = "split.tasks.split_audio"
    TRANSCRIBE_AUDIO = "transcription.tasks.transcribe_audio"
    DETECT_SENTIMENT = "nlp.tasks.detect_sentiment"


class Queues:
    SPLIT = "split_queue"
    TRANSCRIPTION = "transcription_queue"
    NLP = "nlp_queue"

