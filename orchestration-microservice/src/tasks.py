from celery import chain
from src.celery_app import celery_app
from src.config import TaskNames, Queues

# Orchestration function
def run_pipeline(payload: dict):
    """
    Orchestration pipeline:
    1. Split audio
    2. Transcribe audio
    3. NLP Analysis
    """

    # Task names (from settings/config so they match remote repos)
    split_task = f"{TaskNames.SPLIT_AUDIO}"
    transcription_task = f"{TaskNames.TRANSCRIBE_AUDIO}"
    nlp_task = f"{TaskNames.DETECT_SENTIMENT}"

    # Build pipeline chain with explicit queues
    tpayload = {
  "container_url": "https://sticklerdev.blob.core.windows.net/own-livestream-1999/splitted_audios",
  "language": "id",
  "livestream_id": 1999,
  "number_of_audio_parts": 4,
  "request_id": "req_456def",
  "split_duration_seconds": 120,
  "total_duration": 420
}
    workflow = chain(
        celery_app.signature(
            split_task,
            args=(payload,),
            queue=Queues.SPLIT
        ),
        celery_app.signature(
            transcription_task,

            queue=Queues.TRANSCRIPTION
        ),
        celery_app.signature(
            nlp_task,
            queue=Queues.NLP
        )
    )

    result = workflow.apply_async()
    return result.id
