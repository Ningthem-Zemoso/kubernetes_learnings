from .celery_app import celery_app

@celery_app.task(name="app.worker.tasks.print_message")
def print_message(message: str):
    print(f"[CELERY WORKER] Received message: {message}")
    return f"Printed: {message}"
