from celery import Celery
from task_config import TaskNames, Queues, CELERY_BROKER_URL, CELERY_BACKEND_URL

celery_app = Celery(
    "nlp_service",
    broker=CELERY_BROKER_URL,
    backend=CELERY_BACKEND_URL
)

celery_app.conf.task_routes = {
    TaskNames.DETECT_SENTIMENT: {"queue": Queues.NLP},
}

@celery_app.task(name=TaskNames.DETECT_SENTIMENT)
def detect_sentiment(transcript: str):
    print(f"Analyzing sentiment for: {transcript}")
    return {"status": "success", "sentiment": "positive"}
