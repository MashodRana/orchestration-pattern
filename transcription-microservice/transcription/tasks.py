from celery import Celery
from task_config import TaskNames, Queues, CELERY_BROKER_URL,CELERY_BACKEND_URL

celery_app = Celery(
    "transcription_service",
    broker=CELERY_BROKER_URL,
    backend=CELERY_BACKEND_URL
)

celery_app.conf.task_routes = {
    TaskNames.TRANSCRIBE_AUDIO: {"queue": Queues.TRANSCRIPTION},
}

@celery_app.task(name=TaskNames.TRANSCRIBE_AUDIO)
def transcribe_audio(audio_chunks: list):
    print(f"Transcribing {audio_chunks}")
    return {"status": "success", "transcript": "Hello world"}
