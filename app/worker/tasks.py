from .celery_app import celery_app

@celery_app.task
def debug_task():
    """
    A simple task that prints a message to the worker's log.
    Useful for confirming that the Celery setup is working correctly.
    """
    print("Celery worker is running and executing debug_task!")
    return "Task completed successfully."
