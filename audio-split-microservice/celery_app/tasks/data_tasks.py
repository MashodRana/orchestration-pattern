from celery_app.celery import celery_app
from celery_app.services.data_service import process_data

@celery_app.task(name="process_data_task")
def process_data_task(data):
    return process_data(data)
