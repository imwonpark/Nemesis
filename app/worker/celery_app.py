import os
from celery import Celery

celery_broker_url = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
celery_result_backend = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0")

# celery application instance
celery_app = Celery(
    "tasks",
    broker=celery_broker_url,
    backend=celery_result_backend,
    include=["app.worker.tasks"] # task definition file
)

# optional configuration
celery_app.conf.update(
    task_track_started=True,
)
