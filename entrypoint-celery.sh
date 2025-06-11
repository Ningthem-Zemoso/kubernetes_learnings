#!/bin/bash
# Entrypoint for running the Celery worker in Docker
celery -A app.worker.celery_app.celery_app worker --loglevel=info -Q messages
