from nlp.tasks import celery_app

if __name__ == "__main__":
    celery_app.worker_main(["worker", "-l", "info", "-Q", "nlp_queue"])
