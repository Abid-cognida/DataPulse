"""Celery worker module."""

import os

from celery import Celery
from celery.signals import worker_process_init

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("CELERY_CONFIG_MODULE", "app.core.celery_config")

# Create the Celery app
celery_app = Celery("datapulse")

# Load configuration from a module
celery_app.config_from_object("app.core.celery_config")

# Auto-discover tasks from all registered app modules
celery_app.autodiscover_tasks(["app.tasks"])


@worker_process_init.connect
def setup_worker_process_init(**kwargs):
    """Initialize worker process.

    This function is called when a worker process starts.
    It can be used to set up database connections, etc.
    """
    # You can initialize resources here that should be created
    # for each worker process
    pass


@celery_app.task(bind=True, name="app.worker.debug_task")
def debug_task(self):
    """Debug task to verify Celery is working."""
    print(f"Request: {self.request!r}")
    return {"status": "ok", "message": "Debug task executed successfully"}


# Example of a task with exponential backoff retry
@celery_app.task(
    bind=True,
    name="app.worker.example_retry_task",
    max_retries=5,
    retry_backoff=True,
    retry_backoff_max=600,
    retry_jitter=True,
)
def example_retry_task(self, x, y):
    """Retry a task with exponential backoff."""
    try:
        # Simulate some operation that might fail
        result = x / y
        return result
    except Exception as exc:
        # Retry with exponential backoff
        self.retry(exc=exc)
