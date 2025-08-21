from celery import Celery
from task_config import TaskNames, Queues, CELERY_BROKER_URL, CELERY_BACKEND_URL

celery_app = Celery(
    "split_service",
    broker=CELERY_BROKER_URL,
    backend=CELERY_BACKEND_URL
)

celery_app.conf.task_routes = {
    TaskNames.SPLIT_AUDIO: {"queue": Queues.SPLIT},
}

@celery_app.task(name=TaskNames.SPLIT_AUDIO)
def split_audio(file_s3_path: str):
    # fake splitting logic

    print(f"Splitting audio from {file_s3_path}")
    return {"status": "success", "chunks": ["chunk1.mp3", "chunk2.mp3"]}