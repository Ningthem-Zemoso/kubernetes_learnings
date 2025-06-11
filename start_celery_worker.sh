#!/bin/bash
# Start Celery worker for the FastAPI app
celery -A app.worker.celery_app.celery_app worker --loglevel=info -Q messages
