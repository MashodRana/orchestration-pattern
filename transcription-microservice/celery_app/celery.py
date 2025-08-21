from celery import Celery
from celery_app.config.settings import CELERY_BROKER_URL, CELERY_BACKEND_URL

celery_app = Celery(
    'celery_app',
    broker=CELERY_BROKER_URL,
    backend=CELERY_BACKEND_URL
)

celery_app.autodiscover_tasks(['celery_app.tasks'])
